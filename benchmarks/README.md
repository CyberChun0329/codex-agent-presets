# Model, data and reproduction

[简体中文](README.zh-CN.md)

## GPT-6.2 data · 18 November 2026

| Table | Contents |
| --- | --- |
| [Launch comparisons](gpt-6.2-launch.csv) | Five comparisons reported by OpenAI at launch |
| [Scores and task costs](quality-6.2.csv) | OpenAI and Artificial Analysis results by model and reasoning effort |
| [Supplementary task comparisons](task-tradeoffs-6.2.csv) | Tool work, evidence synthesis, visual extraction and professional deliverables, including rule interpretation and quantitative analysis |
| [Frontend](frontend.csv) | AA-3D overall and domain scores, AA task cost inputs, and Vals functional web application scores and costs |

The frontend table keeps the source units and settings. AA-3D averages the votes against each opponent with equal weight in `opponent_balanced_vote_share_pct`. Domain rows have no matching costs. To reproduce the overall AA-3D cost, multiply cacheable input by the hit rate, price those hits at the read rate and all remaining input at the write rate, then price answer and reasoning tokens at the output rate. Divide the total by `task_count` and one million. Vals rows record the run's effort and reported costs. Luna/Max is included for context and excluded by the presets. [Frontend choices](../EVIDENCE.md#frontend-design-and-implementation)

## Inspect or reproduce

The v0.5.0 baseline (15 November 2026) uses GPT-6.1 Sol and GPT-6 Astra.

| File | Contents |
| --- | --- |
| [observations.csv](data/observations.csv) | 660 rows: 15 model/effort candidates across 44 AA metric views, including missing and excluded observations |
| [cost-inputs.csv](data/cost-inputs.csv) | Source token counts, prices, caching assumptions and task denominators for checking estimated cost |
| [components.csv](data/components.csv) | Automation, Omniscience, Briefcase and MLCR components, including conflicting quality/risk dimensions |
| [sources.json](data/sources.json) | Source URLs, snapshot dates and hashes, units and interpretation limits |
| [presets.json](presets.json) | The 68 v0.5.0 defaults, including the source associated with each of the eight specific task branches |
| [evaluate.py](evaluate.py) | Offline calculation using Python's standard library |
| [comparisons.csv](results/comparisons.csv) | 195 comparisons: observed Pareto status and conditional preference intervals for 13 selected metric views |
| [profile-tradeoffs.csv](results/profile-tradeoffs.csv) | Quality differences, cost premiums and relevant components for the eight branches across four profiles |

From the repository root, run:

```sh
python3 benchmarks/evaluate.py --output-dir /tmp/codex-preset-analysis
```

This reproduces the published result tables and checks every available source cost against its token/price inputs. It runs offline without model calls or changes to Codex configuration. [summary.json](results/summary.json) records input hashes and coverage; [cost-checks.csv](results/cost-checks.csv) records 338 reproduced costs and 322 unknown costs.

The numerical snapshot is AA data. Vals, CUA Speedrun, DeepFinance, Snorkel and vendor guidance are separate coverage and transfer checks described in [Benchmarks and preset design](../EVIDENCE.md); their scores are not pooled into these tables. The 44 views include shared runs and derived metrics, not 44 independent experiments. General task defaults without a matching benchmark retain a null source in `presets.json`.

## Supplementary task tradeoffs

The [supplementary table](task-tradeoffs-6.2.csv) includes OpenAI’s LifeVal, BenchCAD and PatchBench results, AA’s MLCR accuracy and overall pass rate, MMMU-Pro, and AA-Briefcase rubric checks overall and by file type. Direct AA scores use fractions. Scores from OpenAI charts use percentages. Separate columns identify the source’s task cost, costs reconstructed using the AA client, and costs estimated under a cache assumption. AutomationBench assigns the same run cost to its strict score. Briefcase file-type rows count the fraction of rubric checks passed and leave the cost blank. See the [Quality data](quality-6.2.csv) for earlier comparisons, including SciCode.

Harvey LAB-AA v1.1 and AA-AnalystAgent each have eight matched rows for GPT-6.2 Sol and Astra from Medium through Max. The Harvey rows use the AA evaluation scores and costs reported in OpenAI’s launch chart. Count this evidence once. AnalystAgent uses `pass_power_5_all_attempts`, the fraction of 80 questions answered correctly in all five attempts. Its cost fields are blank because the cost per single attempt and the cost for the five-attempt bundle could not be aligned. Each new row includes the source URL, field locator and snapshot SHA-256. [OpenAI launch chart](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa) · [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent)

To reproduce the Sol estimates, use each row’s input (`I`), answer (`A`), reasoning (`R`) and cacheable input (`C`) token totals, along with task count `N`. With hit fraction `h` among cacheable input tokens, the AA client’s convention gives the cost per task in USD:

```text
(C*h*0.10 + (I-C*h)*2.50 + (A+R)*10) / (1,000,000*N)
```

The low, 95%-hit and high cost scenarios use `h` of 1, 0.95 and 0. If the source omits `C`, use `(I*2 + (A+R)*10) / (1,000,000*N)`. This is why all three HLE-Diamond estimates coincide. Rates are per million tokens at OpenAI Standard short-context prices on 18 November 2026, with 30-minute cache writes. Actual cache use and context length can change the task cost. [API prices](https://developers.openai.com/api/docs/pricing#latest-models) · [AA client](https://artificialanalysis.ai/_next/static/chunks/17016-9e1b20384a9bc1ed.js)

## Quality 6.2 panels

[quality-6.2.csv](quality-6.2.csv) retains the complete captured candidate rows for AA FrontierCode 2.0, TerminalBench 4.0, SciCode, Terminal-Bench Science, HLE-Diamond and AutomationBench strict results, plus OpenAI's launch-chart FrontierCode 2.0, Terminal-Bench Science and AutomationBench. AA violations per task are a separate, lower-is-better risk measure, not a quality objective. SciCode has no captured 6.2 quality or cost; its older results do not establish a 6.2 comparison.

Each row identifies its source, metric, native unit, model/effort and direct source URL. AA JSON pointers and the captured source SHA-256 identify the specific source snapshot; OpenAI values were extracted from the launch page's Vega-Lite chart. AA's fraction and OpenAI's percent are different scales and their runs must not be pooled. `usd_per_task` is the source-reported task cost or AA client reconstruction identified in `cost_basis`, not a Codex bill. `cost_scope` distinguishes the generic same-run AutomationBench cost attached to its strict/risk metrics from the panel cost. Blank values mean unavailable, not zero; eligible does not imply measured. Low, non-reasoning and Luna/Max are recorded but excluded by the Quality policy. The other metrics are quality-eligible; violations are not.

To verify the recorded original frontier and conditional intervals for every captured panel, run from the repository root:

```sh
python3 - <<'PYCODE'
import csv, importlib.util, sys
sys.dont_write_bytecode = True
from collections import defaultdict
from fractions import Fraction
spec = importlib.util.spec_from_file_location('evaluator', 'benchmarks/evaluate.py')
e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
rows = list(csv.DictReader(open('benchmarks/quality-6.2.csv', newline='', encoding='utf-8')))
groups = defaultdict(list)
for r in rows:
    groups[(r['source'], r['panel'], r['metric'], r['unit'])].append(r)
for group in groups.values():
    points = [((r['model'], r['effort']), Fraction(r['quality']), Fraction(r['usd_per_task']))
              for r in group if r['quality_preset_eligible'] == 'True' and r['metric_eligible'] == 'True'
              and r['quality'] and r['usd_per_task'] and Fraction(r['usd_per_task']) > 0]
    result = e.classify(points)
    for r in group:
        pair = (r['model'], r['effort']); status, interval = result.get(pair, ('', None))
        assert r['costed_candidates_in_panel'] == str(len(points))
        assert r['pareto'] == str(status) if pair in result else r['pareto'] == ''
        assert r['linear_supported'] == str(interval is not None) if pair in result else r['linear_supported'] == ''
        assert r['v_min_exact'] == (str(interval[0]) if interval else '')
        assert r['v_max_exact'] == (str(interval[1]) if interval and interval[1] is not None else '')
print('All captured panel classifications match.')
PYCODE
```

The calculation excludes missing quality or cost, and uses only the recorded eligible candidate set in each source/condition/metric/unit panel. Compare candidate pairs within those panels, then weigh the observed quality and cost changes alongside risk, task requirements and the uncertainty of point estimates. The frontier and intervals alone do not choose a task route. An omitted or unpriced candidate could change the result.

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
