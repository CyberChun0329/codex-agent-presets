"""Recompute observed quality/cost frontiers within each supplemental panel.

Usage: python3 benchmarks/compare_refresh.py > /tmp/benchmark-refresh-comparison.csv
Missing score or matched cost is excluded; unobserved choices are not dominated.
"""
import csv
import sys
from collections import defaultdict
from evaluate import HERE, classify, number

rows = csv.DictReader((HERE / 'benchmark-refresh-6.2.csv').open(encoding='utf-8', newline=''))
panels = defaultdict(list)
for row in rows:
    panels[(row['source'], row['panel'], row['metric'], row['unit'])].append(row)
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(('source', 'panel', 'metric', 'unit', 'model', 'effort', 'score', 'usd_per_task',
                 'costed_candidates', 'pareto', 'linear_supported', 'v_min_exact', 'v_max_exact'))
for key, observations in sorted(panels.items()):
    points = []
    for r in observations:
        q, c = number(r['score']), number(r['usd_per_task'])
        if q is not None and c is not None and c > 0:
            points.append(((r['model'], r['effort']), q, c))
    if len({p[0] for p in points}) != len(points):
        raise ValueError(f'duplicate costed model/effort in {key}')
    results = classify(points)
    for r in observations:
        result = results.get((r['model'], r['effort']))
        pareto, interval = result if result else ('', None)
        writer.writerow((*key, r['model'], r['effort'], r['score'], r['usd_per_task'], len(points), pareto,
                         bool(interval) if result else '', str(interval[0]) if interval else '',
                         str(interval[1]) if interval and interval[1] is not None else ''))
