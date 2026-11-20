"""Compare the v0.6.1 task defaults within their selected benchmark panels."""
import argparse
import re
from collections import defaultdict
from pathlib import Path

from evaluate import HERE, classify, decimal, number, read_csv, write_csv

PROFILES = ('economy', 'balance', 'quality', 'extra-quality')
MODELS = {
    'Luna': 'gpt-6-luna', 'Terra': 'gpt-6.1-terra',
    'Sol': 'gpt-6.2-sol', 'Astra': 'gpt-6.2-astra',
}
EFFORTS = {'M': 'medium', 'H': 'high', 'X': 'xhigh', 'Max': 'max'}
PAIRS = {(model, effort): f'{name}/{level}'
         for name, model in MODELS.items() for level, effort in EFFORTS.items()
         if (name, level) != ('Luna', 'Max')}
ROW = re.compile(r'^\| (.*?) \| (\w+/\w+) \|$', re.M)


def read_panels(keys):
    panels = defaultdict(dict)
    for filename in sorted({key[0] for key in keys}):
        for row in read_csv(HERE / filename):
            pair = PAIRS.get((row['model'], row['effort']))
            if pair is None:
                continue
            key = (filename, row['source'], row.get('panel', row.get('benchmark')),
                   row['metric'], row.get('unit') or row['metric'])
            if key not in keys:
                continue
            if pair in panels[key]:
                raise ValueError(f'Duplicate observation for {key} / {pair}')
            quality = number(row.get('quality', row.get('score')))
            reported = row.get('source_reported_usd_per_task')
            if 'usd_per_task' in row:
                cost = number(row['usd_per_task'])
                basis = row['cost_basis']
            elif reported:
                cost, basis = number(reported), 'reported'
            else:
                cost = number(row.get('aa_client_reconstructed_usd_per_task'))
                basis = 'AA client reconstruction' if cost is not None else ''
            panels[key][pair] = (quality, cost, basis)
    return panels


def compare_panel(panel):
    points = [(pair, quality, cost) for pair, (quality, cost, _) in panel.items()
              if quality is not None and cost is not None and cost > 0]
    if not points:
        return {}, ''
    classifications = classify(points)
    ordered = sorted(points, key=lambda point: (point[2], point[0]))
    frontier = ' '.join(pair for pair, _, _ in ordered if classifications[pair][0])
    return classifications, frontier


def compare():
    routes = read_csv(HERE / 'routing-0.6.1.csv')
    labels = [route['task'] for route in routes]
    if len(labels) != len(set(labels)):
        raise ValueError('Duplicate task in routing table')
    for profile in PROFILES:
        actual = ROW.findall((HERE.parent / 'profiles' / f'{profile}.md').read_text(
            encoding='utf-8'))
        expected = [(route['task'], route[profile]) for route in routes]
        if actual != expected:
            raise ValueError(f'Routing table differs from {profile} profile')

    fields = ('data_file', 'source', 'benchmark', 'metric', 'unit')
    keys = [tuple(route[k] for k in fields) for route in routes]
    panels = read_panels({key for key in keys if key[0]})
    panel_results = {key: compare_panel(panel) for key, panel in panels.items()}
    rows = []
    for route, key in zip(routes, keys):
        panel = panels.get(key, {})
        if route['data_file'] and not panel:
            raise ValueError(f'Missing benchmark panel for {route["task"]}: {key}')
        classifications, frontier = panel_results.get(key, ({}, ''))
        bq, bc, _ = panel.get(route['balance'], (None, None, ''))
        for profile in PROFILES:
            pair = route[profile]
            q, c, basis = panel.get(pair, (None, None, ''))
            pareto, interval = classifications.get(pair, ('', None))
            rows.append({
                'task': route['task'], 'profile': profile, 'pair': pair,
                'evidence_fit': route['evidence_fit'], 'source': route['source'],
                'benchmark': route['benchmark'], 'metric': route['metric'],
                'unit': route['unit'], 'quality': decimal(q), 'usd_per_task': decimal(c),
                'cost_basis': basis if c is not None else '',
                'quality_delta_from_balance': decimal(q - bq) if q is not None and bq is not None else '',
                'cost_delta_from_balance': decimal(c - bc) if c is not None and bc is not None else '',
                'cost_multiple_of_balance': decimal(c / bc) if c is not None and bc else '',
                'costed_candidates': len(classifications) if panel else '',
                'pareto': pareto,
                'linear_supported': interval is not None if pair in classifications else '',
                'v_min_exact': str(interval[0]) if interval else '',
                'v_max_exact': str(interval[1]) if interval and interval[1] is not None else '',
                'frontier_pairs': frontier,
            })
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    output = parser.parse_args().output
    rows = compare()
    write_csv(output, rows)
    print(f'Wrote {len(rows)} profile comparisons to {output}')
