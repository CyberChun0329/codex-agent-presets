"""Compare measured benchmark combinations at each average execution budget."""
import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import groupby
from pathlib import Path

from compare_routing import PAIRS, PROFILES, read_panels
from evaluate import classify, number, read_csv, write_csv

BENCHMARKS = Path(__file__).resolve().parent
PANEL_FIELDS = ('data_file', 'source', 'benchmark', 'metric', 'unit')
AUTOMATION_RISK = ('quality-6.2.csv', 'AA', 'automation-violations',
                   'violations_per_task', 'violations per task')
LEGAL_RISK = ('task-tradeoffs-6.2.csv', 'AA', 'Harvey-LAB-AA v1.1',
              'material_hallucinations_per_checked_task', 'count_per_checked_task')


def published_decimal(value):
    if value is None:
        return ''
    # CSV inputs are finite decimals. Keep every digit at a budget boundary.
    with localcontext() as context:
        context.prec = len(str(abs(value.numerator))) + value.denominator.bit_length()
        return format(Decimal(value.numerator) / Decimal(value.denominator), 'f')


def budget_intervals(points):
    """All tied winners, with inclusive lower and exclusive upper budget endpoints."""
    steps = []
    for cost, group in groupby(sorted(points, key=lambda p: p[2]), key=lambda p: p[2]):
        at_cost = list(group)
        quality = max(q for _, q, _ in at_cost)
        if not steps or quality > steps[-1][1]:
            steps.append((cost, quality, [pair for pair, q, _ in at_cost if q == quality]))
    return {
        pair: (cost, steps[i + 1][0] if i + 1 < len(steps) else None)
        for i, (cost, _, pairs) in enumerate(steps) for pair in pairs
    }


def panel_rows(route, panel, case, risk=None, ceiling=None):
    if len({basis for _, cost, basis in panel.values() if cost is not None}) > 1:
        raise ValueError(f'Mixed cost bases for {route["benchmark"]} / {case}')
    risk = risk or {}
    points = []
    gates = {}
    for pair in PAIRS.values():
        q, c, _ = panel.get(pair, (None, None, ''))
        status = 'not_applied'
        if ceiling is not None:
            value = risk.get(pair)
            status = 'unknown' if value is None else 'passes_point_ceiling' if value <= ceiling else 'exceeds_point_ceiling'
        gates[pair] = status
        if q is not None and c is not None and status in ('not_applied', 'passes_point_ceiling'):
            points.append((pair, q, c))
    intervals = budget_intervals(points)
    linear = classify(points)
    for pair in PAIRS.values():
        q, c, basis = panel.get(pair, (None, None, ''))
        lo, hi = intervals.get(pair, (None, None))
        yield {
            'task': route['task'], 'case': case, 'evidence_fit': route['evidence_fit'],
            'source': route['source'], 'benchmark': route['benchmark'],
            'metric': route['metric'], 'unit': route['unit'], 'pair': pair,
            'current_profiles': ' '.join(profile for profile in PROFILES if route[profile] == pair),
            'score': published_decimal(q), 'execution_usd': published_decimal(c), 'cost_basis': basis,
            'risk_point_observation': published_decimal(risk.get(pair)),
            'illustrative_risk_ceiling': published_decimal(ceiling),
            'point_ceiling_status': gates[pair],
            'budget_comparison': (
                'score_or_cost_unknown' if q is None or c is None else
                gates[pair] if pair not in linear else
                'leads_observed_points' if lo is not None else 'dominated_observed_points'
            ),
            'budget_min_inclusive_usd': published_decimal(lo),
            'budget_max_exclusive_usd': published_decimal(hi),
            'budget_unbounded': lo is not None and hi is None,
            'linear_supported_observed_points': linear[pair][1] is not None if pair in linear else '',
            'costed_and_comparable_pairs': len(points),
        }


def cache_costs(rows, key, panel, column):
    costs = {}
    for row in rows:
        pair = PAIRS.get((row['model'], row['effort']))
        if pair is None or tuple(row[field] for field in PANEL_FIELDS[1:]) != key[1:]:
            continue
        matches = (number(row['quality']), number(row['source_reported_usd_per_task']))
        if pair in costs or matches != panel[pair][:2]:
            raise ValueError(f'Cache scenario row cannot be matched to {key[2]} / {pair}')
        costs[pair] = number(row[column])
    return costs


def replay():
    routes = read_csv(BENCHMARKS / 'routing-0.7.0.csv')
    keys = [tuple(route[f] for f in PANEL_FIELDS) for route in routes]
    panels = read_panels({key for key in keys if key[0]} | {AUTOMATION_RISK, LEGAL_RISK})
    data = read_csv(BENCHMARKS / 'task-tradeoffs-6.2.csv')
    for route, key in zip(routes, keys):
        panel = panels[key] if key[0] else {}
        if key[0] and not panel:
            raise ValueError(f'Missing declared benchmark panel: {key}')
        yield from panel_rows(route, panel, 'published_score_and_execution_cost')
        if route['task'].startswith('Case-specific rule application:'):
            risk = {pair: q for pair, (q, _, _) in panels[LEGAL_RISK].items()}
            yield from panel_rows(route, panel, 'example_record_errors_per_checked_task',
                                  risk, Fraction('0.03'))
        if key[2] == 'automation-strict':
            risk = {pair: q for pair, (q, _, _) in panels[AUTOMATION_RISK].items()}
            ceiling = Fraction('0.38')
            yield from panel_rows(route, panel, 'example_violation_events_per_task',
                                  risk, ceiling)
            for cache, column in (('100', 'scenario_min_usd_per_task'),
                                  ('95', 'scenario_95pct_hit_usd_per_task'),
                                  ('0', 'scenario_max_usd_per_task')):
                costs = cache_costs(data, key, panel, column)
                adjusted = {
                    pair: (q, costs.get(pair), f'AA token reconstruction, {cache}% cache scenario')
                    for pair, (q, _, _) in panel.items()
                }
                yield from panel_rows(route, adjusted, f'example_cache_hit_{cache}_percent')
                if cache == '95':
                    yield from panel_rows(route, adjusted, 'example_cache_95_and_violation_ceiling',
                                          risk, ceiling)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rows = list(replay())
    write_csv(args.output, rows)
    defaults = Counter(row['budget_comparison'] for row in rows
                       if row['case'] == 'published_score_and_execution_cost'
                       for _ in row['current_profiles'].split())
    print(f'{len(rows)} comparisons. Existing defaults by observed-point result: {dict(defaults)}')
