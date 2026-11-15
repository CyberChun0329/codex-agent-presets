# Benchmarks and preset design

[简体中文](EVIDENCE.zh-CN.md) · Evidence reviewed: **15 November 2026**

The presets express different preferences for task quality and cost. The models considered are GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol and GPT-6 Astra. Select model and reasoning effort for the remaining work and its acceptance requirements.

The comparison pool contains Medium, High, Xhigh and Max for these four families, except Luna/Max: 15 possible pairs. Low and non-reasoning are outside the presets. A source need not have results for every pair.

The [model, data and reproduction guide](benchmarks/README.md) provides the numerical snapshot, cost inputs, calculation and profile tradeoff tables.

## Evidence used

The main comparisons use [Artificial Analysis (AA)](https://artificialanalysis.ai/methodology/intelligence-benchmarking):

| Task evidence | Evaluations |
| --- | --- |
| Repository changes, terminal work and scientific execution | [FrontierCode-AA 2.0](https://artificialanalysis.ai/evaluations/frontiercode-2-0), [Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench-Science](https://artificialanalysis.ai/evaluations/terminal-bench-science) |
| Stateful tool workflows | [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa): strict pass, objective completion and guardrail violations read together |
| Source-based answers and long-context reasoning | [GDP.pdf](https://artificialanalysis.ai/evaluations/gdp-pdf), [MLCR-AA](https://artificialanalysis.ai/evaluations/mlcr-aa), [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) |
| Difficult knowledge, reasoning and physics | [HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond), [CritPt v2 and its hard subset](https://artificialanalysis.ai/evaluations/critpt-v2) |
| Professional deliverables and knowledge reliability | [Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase), [Omniscience](https://artificialanalysis.ai/evaluations/omniscience) |

We also checked task and execution conditions against [Vals Finance Agent](https://www.vals.ai/benchmarks/fabv2-1) and [Legal Research](https://www.vals.ai/benchmarks/legal_research), CUA Speedrun's [OSWorld](https://cuaspeedrun.com/dataset-osworld-energy50-representative.html) and [OSWorld2](https://cuaspeedrun.com/dataset-osworld2-k52.html), [DeepFinance](https://arxiv.org/pdf/2611.10926), and [Snorkel's Terminal-Bench leaderboard](https://snorkel.ai/leaderboard/terminal-bench/). These are checks on coverage and transfer, not a complete four-model, all-effort experiment. Publishers use different tasks, harnesses, scoring, attempts and cost definitions; scores cannot be averaged across benchmarks. Missing or invalid observations are not zeros.

Separately, OpenAI's [model selection guide](https://developers.openai.com/api/docs/guides/model-selection) and [Terra release notes](https://openai.com/index/introducing-gpt-6-1-terra/) provide vendor guidance, including Terra's natural writing and visual strengths. This guidance is not independent benchmark evidence or an independent replication.

## Comparing quality and cost

Within each source and task, compare quality gains, cost differences or multiples, and relevant risks in their original units. The [calculation guide](benchmarks/README.md#what-the-calculation-means) explains the Pareto frontier and conditional `value × quality − cost` comparison. A quality floor comes from the task's requirements, not the median or top half of the available candidates.

## Choosing the Balance defaults

Balance selects a defensible task-quality/cost compromise, rather than the cheapest pair or the highest quality/cost ratio. These examples show the decisions behind its defaults. Figures are from the referenced AA snapshot:

| Task / Balance pair | Tradeoff informing the choice |
| --- | --- |
| Ordinary code / Terra/High | Terra/Medium→High adds about 2.92 scoring-credit percentage points at 1.52× cost. High→Max adds 4.86 points at 3.30× cost; the policy reserves that additional spend for demanding integration. The source did not separately test those two difficulty groups. |
| Complete document answers / Sol/High | Terra/Medium→Sol/High adds 3.6 all-pass percentage points at 2.10× cost. Sol/High→Astra/Xhigh adds only 0.2 points at 5.47× cost. This informs the shared Sol/High default for similar answers, not every form of document reasoning. |
| End-to-end tool work / Sol/Medium | On Terminal-Bench 4.0, Sol/Medium scores 47.98% at $0.614 per source task, versus Terra/Xhigh's 46.46% at $0.657. This is a point comparison under that harness, not proven native superiority. |

For demanding code, Terra/Max→Astra/Max adds about **0.055 scoring-credit percentage points** at **5.06×** source cost. The higher profiles can share Terra/Max; this does not prove equal quality or that ordinary code has reached a plateau.

These defaults combine source observations, task matching and the stated resource preference. No fitted acceptance probability or precise willingness-to-pay parameter uniquely determines them. Task and harness differences can explain conflicting rankings; their effects have not been isolated.

## Extending the quality and cost preferences

Economy accepts some loss of quality margin to reduce cost where the task's requirements permit it. Quality retains Sol/High or Xhigh for normal substantive judgment and pays more for task-relevant quality. Extra Quality accepts larger premiums for the last increment of quality. The task's acceptance requirements still apply in all four.

Heavy evidence synthesis illustrates this approach: reconstructing chronology or causal chains, resolving conflicting records and answering composite questions under a fixed framework. MLCR informs this narrow route; a long document, citations or a medical label alone do not trigger it.

| Profile | Pair | MLCR complete-answer pass | Source cost/task |
| --- | --- | ---: | ---: |
| Economy | Terra/Max | 30.56% | $0.06395 |
| Balance | Sol/Xhigh | 35.56% | $0.09374 |
| Quality | Sol/Max | 38.33% | $0.11193 |
| Extra Quality | Astra/Max | 41.67% | $0.57256 |

In this snapshot, Terra/Max costs less than Sol/Medium, which is why an Economy route can use Max. Sol/High→Sol/Max gains 6.67 pass percentage points for about 29% more source cost. Extra's final 3.33-point gain over Sol/Max costs about 5.12×: it is a quality premium, not better cost efficiency. MLCR has matching observations for 12 of 15 pairs; Terra/Medium, High and Xhigh are missing. Its accuracy component is not monotone along this sequence, so the overall pass increase is not improvement on every dimension.

AA-LCR provides a countercheck: Sol/Medium, High and Max score about 83.33%, 82.33% and 83.00%. Longer context therefore does not justify a general Max rule. The heavy-synthesis mapping remains a policy choice, not a causal result about a single task feature.

These source point estimates do not establish a unique best model or statistically significant differences, and are not native Codex measurements. AA's weighted Cost per Task gives background for its own task mix; it cannot replace the individual task comparisons or predict subscription allowance. Full workflow cost also includes the primary agent, tools, handoffs and necessary rework. That native total has not been measured here.

Profiles can share a model/effort pair. A difficult integration, a complete answer from documents and a multi-state tool workflow can call for different choices even when all involve files or code; task length, a medical label or terminal use alone does not determine the route. Check the defaults against your quality requirements and observed workflow costs. The profiles impose no fixed model ladder, usage quota or requirement that a cheaper attempt fail first.
