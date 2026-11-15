"""Compare benchmark quality and cost, and report preset tradeoffs offline."""
import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
METRICS = {
    'terminalbench-4-0': 'success_fraction',
    'frontiercode-2-0': 'rubric_credit',
    'terminal-bench-science': 'success_fraction',
    'hle-diamond': 'accuracy',
    'gdp-pdf': 'all_pass_fraction',
    'automation-strict': 'strict_task_fraction',
    'automationbench-aa': 'objective_credit',
    'briefcase-rubric': 'rubric_check_fraction',
    'aa-briefcase': 'elo',
    'omniscience': 'net_score',
    'omniscience-accuracy': 'accuracy',
    'mlcr-aa': 'answer_pass_fraction',
    'artificial-analysis-long-context-reasoning': 'accuracy',
}


def read_csv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def number(value):
    return Fraction(value) if value and value.strip() else None


def decimal(value):
    return '' if value is None else str(float(value))


def classify(points):
    """Observed Pareto status and closed support interval for v*q-c, v >= 0."""
    result = {}
    for identity, quality, cost in points:
        pareto = not any(q >= quality and c <= cost and (q > quality or c < cost)
                         for _, q, c in points)
        lower, upper, possible = Fraction(0), None, True
        for _, other_quality, other_cost in points:
            dq, dc = quality - other_quality, cost - other_cost
            if dq > 0:
                lower = max(lower, dc / dq)
            elif dq < 0:
                bound = dc / dq
                upper = bound if upper is None else min(upper, bound)
            elif dc > 0:
                possible = False
        if upper is not None and lower > upper:
            possible = False
        result[identity] = (pareto, (lower, upper) if possible else None)
    return result


def reconstruct_cost(row):
    """USD per source task from source aggregate tokens, prices and task count."""
    if row['price_fallback'].lower() == 'true':
        return None
    keys = ('input_tokens', 'answer_tokens', 'reasoning_tokens',
            'price_input_per_million', 'price_output_per_million', 'task_count')
    values = {key: number(row[key]) for key in keys}
    if any(value is None for value in values.values()) or values['task_count'] <= 0:
        return None
    cached = number(row['cacheable_input_tokens'])
    if cached is None:
        input_cost = values['input_tokens'] * values['price_input_per_million']
    else:
        hit_rate = number(row['cache_hit_rate'])
        if hit_rate is None:
            return None
        reads = cached * hit_rate
        hit_price = number(row['price_cache_hit_per_million'])
        write_price = number(row['price_cache_write_per_million'])
        if hit_price is None:
            hit_price = values['price_input_per_million']
        if write_price is None:
            write_price = values['price_input_per_million']
        input_cost = reads * hit_price + (values['input_tokens'] - reads) * write_price
    output_cost = (values['answer_tokens'] + values['reasoning_tokens']) * values['price_output_per_million']
    return (input_cost + output_cost) / 1_000_000 / values['task_count']


def write_csv(path, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run(output):
    observations = read_csv(HERE / 'data/observations.csv')
    components = {r['pair']: r for r in read_csv(HERE / 'data/components.csv')}
    cost_inputs = read_csv(HERE / 'data/cost-inputs.csv')
    presets = json.loads((HERE / 'presets.json').read_text())
    lookup = {(r['benchmark'], r['pair']): r for r in observations}
    if len(lookup) != len(observations):
        raise ValueError('Duplicate benchmark/pair observation')
    groups = {benchmark: [] for benchmark in METRICS}
    for row in observations:
        benchmark = row['benchmark']
        quality, cost = number(row['quality']), number(row['cost_usd_per_task'])
        status = (row['quality_cost_status'] + ' ' + row['cost_status']).lower()
        if (benchmark in METRICS and row['metric_kind'] == METRICS[benchmark]
                and quality is not None and cost is not None and cost > 0
                and 'quarantin' not in status and 'unbound' not in status):
            groups[benchmark].append((row['pair'], quality, cost))
    classifications = {b: classify(points) for b, points in groups.items()}
    comparison = []
    for row in observations:
        b, pair = row['benchmark'], row['pair']
        if b not in METRICS:
            continue
        observed = pair in classifications[b]
        pareto, interval = classifications[b].get(pair, (None, None))
        comparison.append({
            'benchmark': b, 'pair': pair, 'quality': row['quality'],
            'metric_kind': row['metric_kind'], 'metric_unit': row['metric_unit'],
            'cost_usd_per_task': row['cost_usd_per_task'],
            'observation_status': 'observed' if observed else 'missing_or_excluded',
            'pareto_observed_set': pareto if observed else 'UNKNOWN',
            'linear_supported': interval is not None if observed else 'UNKNOWN',
            'v_min_exact': str(interval[0]) if interval else '',
            'v_max_exact': str(interval[1]) if interval and interval[1] is not None else '',
        })
    tradeoffs = []
    for branch in presets['task_branches']:
        b = branch['benchmark']
        balance = lookup[b, branch['pairs']['balance']]
        bq, bc = number(balance['quality']), number(balance['cost_usd_per_task'])
        previous = None
        for profile in presets['profiles']:
            pair = branch['pairs'][profile]
            row = lookup[b, pair]
            q, c = number(row['quality']), number(row['cost_usd_per_task'])
            if pair not in classifications[b]:
                raise ValueError(f'Chosen pair lacks usable source data: {b}/{pair}')
            risk = components[pair]
            tradeoffs.append({
                'route': branch['id'], 'benchmark': b, 'profile': profile, 'pair': pair,
                'quality': row['quality'], 'metric_kind': row['metric_kind'],
                'source_cost_usd_per_task': row['cost_usd_per_task'],
                'quality_delta_from_balance': decimal(q-bq),
                'cost_multiple_of_balance': decimal(c/bc),
                'quality_delta_from_previous_tier': decimal(q-previous[0]) if previous else '',
                'cost_delta_from_previous_tier': decimal(c-previous[1]) if previous else '',
                'cost_multiple_of_previous_tier': decimal(c/previous[1]) if previous else '',
                'automation_guardrail_violations_per_task': risk['automation_guardrail_violations_per_task'] if b == 'automation-strict' else '',
                'mlcr_accuracy': risk['mlcr_accuracy'] if b == 'mlcr-aa' else '',
                'mlcr_completeness': risk['mlcr_completeness'] if b == 'mlcr-aa' else '',
            })
            previous = q, c
    cost_checks = []
    for row in cost_inputs:
        expected = number(lookup[row['benchmark'], row['pair']]['cost_usd_per_task'])
        actual = reconstruct_cost(row)
        matches = expected is not None and actual is not None and math.isclose(float(expected), float(actual), rel_tol=1e-10, abs_tol=1e-12)
        if expected is not None and not matches:
            raise ValueError(f'Cost reproduction mismatch: {row["benchmark"]}/{row["pair"]}')
        cost_checks.append({'benchmark': row['benchmark'], 'pair': row['pair'],
                            'source_cost_usd_per_task': decimal(expected),
                            'reconstructed_usd_per_task': decimal(actual),
                            'status': 'matches' if matches else 'source_cost_unknown'})
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / 'comparisons.csv', comparison)
    write_csv(output / 'profile-tradeoffs.csv', tradeoffs)
    write_csv(output / 'cost-checks.csv', cost_checks)
    summary = {'snapshot_rows': len(observations), 'metric_views': len({r['benchmark'] for r in observations}),
               'comparison_rows': len(comparison), 'profile_tradeoff_rows': len(tradeoffs),
               'observed_by_view': {b: len(points) for b, points in groups.items()},
               'cost_rows_reproduced': sum(r['status'] == 'matches' for r in cost_checks),
               'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((HERE / 'data').glob('*')) + [HERE / 'presets.json'] if p.is_file()},
               'calculator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    run(parser.parse_args().output_dir)
