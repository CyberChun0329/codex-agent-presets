# Model, data and reproduction

[简体中文](README.zh-CN.md) · Snapshot: **15 November 2026**

This directory provides the data and calculator for task-specific quality/cost comparisons. Preset task mappings and willingness to pay for quality are supplied as inputs. The calculator compares those choices; it does not select or validate the mappings.

## Inspect or reproduce

| File | Contents |
| --- | --- |
| [observations.csv](data/observations.csv) | 660 rows: 15 model/effort candidates across 44 AA metric views, including missing and excluded observations |
| [cost-inputs.csv](data/cost-inputs.csv) | Source token counts, prices, caching assumptions and task denominators for checking estimated cost |
| [components.csv](data/components.csv) | Automation, Omniscience, Briefcase and MLCR components, including conflicting quality/risk dimensions |
| [sources.json](data/sources.json) | Source URLs, snapshot dates and hashes, units and interpretation limits |
| [presets.json](presets.json) | The four profiles' 68 defaults, including the source associated with each of the eight specific task branches |
| [evaluate.py](evaluate.py) | Offline calculation using Python's standard library |
| [comparisons.csv](results/comparisons.csv) | 195 comparisons: observed Pareto status and conditional preference intervals for 13 selected metric views |
| [profile-tradeoffs.csv](results/profile-tradeoffs.csv) | Quality differences, cost premiums and relevant components for the eight branches across four profiles |

From the repository root, run:

```sh
python3 benchmarks/evaluate.py --output-dir /tmp/codex-preset-analysis
```

This reproduces the published result tables and checks every available source cost against its token/price inputs. It runs offline without model calls or changes to Codex configuration. [summary.json](results/summary.json) records input hashes and coverage; [cost-checks.csv](results/cost-checks.csv) records 338 reproduced costs and 322 unknown costs.

The numerical snapshot is AA data. Vals, CUA Speedrun, DeepFinance, Snorkel and vendor guidance are separate coverage and transfer checks described in [Benchmarks and preset design](../EVIDENCE.md); their scores are not pooled into these tables. The 44 views include shared runs and derived metrics, not 44 independent experiments. General task defaults without a matching benchmark retain a null source in `presets.json`.

## What the calculation means

For a candidate `i` within one source and metric, let `q_i` be its source quality score and `c_i` its estimated USD per source task. Keep the source units: some scores are fractions, while Elo and net scores are not. Quality divided by cost is useful when the measure has a defined output unit and the objective is output per budget; Elo and net scores are not divided by price. Do not average scores or quality/cost ratios across benchmarks.

- **Observed Pareto frontier:** no observed alternative is at least as good and no costlier, with a strict improvement in one dimension.
- **Conditional preference:** `U_i(v) = v × q_i − c_i`, where `v ≥ 0` is an assumed USD value per source quality unit. The script finds the interval in which each candidate maximizes this expression against all usable observations. Endpoints include ties; a supported point with a blank upper endpoint is unbounded. These are preference intervals, not confidence intervals.
- **Task tradeoff:** inspect quality differences and cost differences/multiples between the chosen defaults, alongside risk and conflicting components. No arbitrary extra hallucination penalty is added to a score that already penalizes errors.

A Pareto point need not be selected by a linear objective; it can still make sense under a hard budget or quality constraint. Missing quality or cost is not zero, exclusion is not proof of unsuitability, and an unobserved candidate can change the frontier. The published calculation uses exact fractions for the preference intervals.

## From comparisons to defaults

First match the remaining work and acceptance requirements to relevant evidence. Then compare usable candidates, quality gains, premiums and risk conflicts. A quality floor comes from the actual task requirements; neither the median candidate nor the top half of a leaderboard establishes one. Benchmark scores alone do not prove that any candidate meets your task's requirements.

Balance chooses a competitive quality/cost compromise using those comparisons. Economy accepts less quality margin where the requirements permit it. Quality and Extra Quality accept larger task-relevant premiums. There is no fitted universal `v` for the four profiles, no automatic maximum-ratio selection, and no requirement to change pair at every tier. [The design explanation](../EVIDENCE.md#choosing-the-balance-defaults) gives concrete Balance choices and the four-profile heavy-synthesis example.

The 32 branch rows are calculated comparisons of the supplied defaults. Open-ended judgment, writing and the general defaults also rely on task structure and vendor guidance. Native application quality, rework, handoff cost and subscription usage remain unmeasured.

## Cost units and exclusions

Source prices are USD per million tokens. Estimated cost is input cost plus answer/reasoning output cost, divided by one million and the source client's task denominator. For cacheable input, cached reads use the source hit rate and cache-hit price; the remaining input uses the cache-write price. A missing cache price falls back to the input price as in the source client. Missing required inputs remain unknown. These are source accounting assumptions, not measured Codex bills.

HealthBench is excluded from quality/cost analysis while its version/field binding remains unresolved. AnalystAgent's five-attempt all-correct score has no established matching bundle cost. CritPt Hard retains its separate token field and task denominator. MLCR's missing Terra efforts and non-monotone accuracy component remain visible.
