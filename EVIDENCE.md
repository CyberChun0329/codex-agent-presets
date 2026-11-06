# Model-selection evidence

[简体中文](EVIDENCE.zh-CN.md) · External benchmarks: **2026-11-03** · Local comparison: **2026-11-06**.

Luna means GPT-6 Luna; Terra and Sol mean GPT-6.1 Terra and Sol; Astra means GPT-6 Astra.

## Artificial Analysis

These comparisons use Intelligence Index v5.0. Percentages are rounded as displayed;
confidence intervals were not provided. **II cost/task** is the index's weighted
average task cost, not the price of an individual benchmark or a measure of Codex credits.

### Terra: Max versus Xhigh

| Measure | Max | Xhigh |
| --- | ---: | ---: |
| Terminal-Bench 4.0 | 56% | 46% |
| Terminal-Bench-Science 0.1 | 58% | 42% |
| AutomationBench-AA | 60% | 60% |
| II cost/task | $0.96 | $0.40 |

Balance allows Terra Max for suitable terminal and scientific tasks. The unchanged
automation result gives no reason to use Max routinely for automation.
[Source](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-terra-xhigh).

### Sol: Max versus Xhigh

| Measure | Max | Xhigh |
| --- | ---: | ---: |
| Terminal-Bench 4.0 | 56% | 54% |
| Terminal-Bench-Science 0.1 | 58% | 50% |
| AutomationBench-AA | 65% | 67% |
| GDP.pdf | 31% | 32% |
| II cost/task | $1.27 | $0.76 |

The results vary by task. Balance reserves Sol Max for work that benefits from
deeper reasoning; the small score differences do not establish a general advantage.
[Source](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-1-sol-xhigh).

### Terra High versus Sol Medium

| Measure | Terra High | Sol Medium |
| --- | ---: | ---: |
| Terminal-Bench 4.0 | 42% | 48% |
| FrontierCode 2.0 | 37% | 33% |
| II cost/task | $0.26 | $0.36 |
| Time to first answer token | 20.82 s | 9.35 s |
| Whole-task time | 171.39 s | 217.80 s |

Lower token prices and faster first output do not settle total cost or completion
time. Economy therefore makes no promise of fastest completion. Timing is a snapshot.
[Source](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-high-vs-gpt-6-1-sol-medium).

### Terra Max versus Sol High

| Measure | Terra Max | Sol High |
| --- | ---: | ---: |
| Terminal-Bench 4.0 | 56% | 52% |
| Terminal-Bench-Science 0.1 | 58% | 46% |
| AA-Briefcase v1.1 Elo | 1402 | 1467 |
| AA-Omniscience v1.1 net score | 30 | 41 |
| GDP.pdf | 29% | 32% |
| II cost/task | $0.96 | $0.59 |

These mixed results support choosing by task rather than replacing Sol with
higher-effort Terra across the board.
[Source](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-sol-high).

### Luna: Max versus Xhigh

Max improves Terminal-Bench 4.0 from **8% to 13%**, science from **5% to 9%**, and
AutomationBench-AA from **48% to 53%**. II cost/task rises from **$0.10 to $0.15**.
Balance allows Luna Max for bounded, well-checked work when the added reasoning is
useful. These scores do not establish it as a substitute for Terra.
[Source](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-luna-xhigh).

## Benchmark-author results

- **Terminal-Bench 4.0:** 66 tasks, Harbor, pinned `terminal-bench@4.0.0`, Codex,
  Max. Resolution rates: Sol **58.2% ±3.1**, Astra **58.2% ±2.8**, Luna **16.4% ±2.7**.
  The reviewed page had no Terra result. Costs and tokens cover the whole benchmark.
  These runs differ from Artificial Analysis's runs above.
  [Leaderboard and methodology](https://snorkel.ai/leaderboard/terminal-bench/).
- **ALE v1.1:** 122 tasks across 55 sub-industries. Terra/Max with Codex achieved
  **41.8% pass rate** and **69.8% score**, taking **124h36m** and **5.5M output tokens**
  in total. Pass rate requires full completion; score includes partial credit.
  [Leaderboard](https://snorkel.ai/leaderboard/agents-last-exam/).

## OpenAI results and guidance

The official **ALE v1** chart reports:

| Model / effort | Score | Cost/task |
| --- | ---: | ---: |
| Luna / Max | 50.9% | $0.14 |
| Terra / Low | 55.9% | $0.16 |
| Terra / Medium | 57.6% | $0.29 |
| Terra / Max | 60.0% | $1.01 |

This supports considering lower effort on a stronger model, as Balance and Economy
do. The chart reports v1 scores; compare them separately from v1.1 pass rates.
[Official chart](https://openai.com/index/introducing-gpt-6-1-terra/).

OpenAI recommends Terra for natural writing, visual reasoning and precise computer
use. Briefcase measures complete work products, not prose style alone.
[Official guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-61-terra).

## Local fixed-criteria document comparison — 2026-11-06

Terra/High and Sol/High revised the same English and Chinese technical sections
using supplied facts and criteria. Both first drafts met the requirements without
rework. Each model also reviewed the same seven short technical sections.

| Task / model, High | Task time | Uncached input tokens | Cached input tokens | Output tokens |
| --- | ---: | ---: | ---: | ---: |
| Two revisions / Terra | 38.7 s | 31,763 | 89,088 | 1,069 |
| Two revisions / Sol | 44.0 s | 31,864 | 89,472 | 1,163 |
| Seven-section review / Terra | 31.8 s | 18,195 | 71,296 | 841 |
| Seven-section review / Sol | 44.4 s | 18,217 | 100,480 | 1,333 |

Terra/High took less time and used fewer output tokens in this small test. Task
time includes checks, waiting and tool use; it is not a full-workflow measurement.
Cached input is part of input, and output includes reasoning tokens.

## Applying the evidence

| Profile | Fixed-criteria revision and source-bound review |
| --- | --- |
| Economy | Prefer Terra: Low/Medium for bounded, effectively checked work, High for normal reasoning, Xhigh for interacting constraints; the pool is Luna/Terra. |
| Balance | Prefer Terra and choose effort by task; use Sol for substantive ambiguity, architecture or method choices, and evidence synthesis. |
| Quality and Extra Quality | Normally start with Terra/High; use Sol for substantive ambiguity or coupled conceptual decisions. Reviewer status alone does not require Sol. |

The local test covered High and short technical documents only; it does not
establish results at Low/Medium or on long manuscripts. No comparison here measures
complete profiles, Ultra primary performance or Codex subscription usage.
