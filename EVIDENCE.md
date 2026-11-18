# Benchmarks and preset design

[简体中文](EVIDENCE.zh-CN.md)

## GPT-6.2 model choices

All four presets use GPT-6.2 for Sol and Astra. On FrontierCode 2.0, Sol/Max scored within 0.5 points of Astra/Max at about one-fifth of its cost. On Terminal-Bench-Science 0.1, Astra gained nine percentage points over the previous Astra at less than a third of its task cost. On GDPval v2, Sol gained 5.3 percentage points over the previous Sol. [OpenAI launch results](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Launch comparisons](benchmarks/gpt-6.2-launch.csv)

For requests with up to 272,000 input tokens at standard API rates, a million input, cached input and output tokens cost $2, $0.10 and $10 with GPT-6.2 Sol, or $8, $0.40 and $40 with GPT-6.2 Astra. Actual task cost also depends on token use. [OpenAI pricing](https://developers.openai.com/api/docs/pricing#latest-models)

### From Balance to the other presets

Choose Balance first for each task, weighing the score gain against the extra cost and the consequences of an error. Economy places more weight on cost. Quality and Extra Quality pay more when the evidence supports a useful gain. Two presets can share a pair, as Economy and Balance do for hard questions with a fixed answer.

| Task | Choice and evidence |
| --- | --- |
| Established tool workflows | In AA AutomationBench, Terra/Xhigh passed 32.88% under strict scoring, with 0.677 violations per task. Balance’s Sol/Medium passed 41.40%, with 0.397 violations per task. OpenAI scores Sol/Medium at 40.2% for $0.18 per task and Sol/High at 41.2% for $0.21. |
| Tool work with exploration and feedback | Balance uses Sol/High. On LifeVal it scores 80.8% at $0.65 versus 70.3% at $0.38 for Sol/Medium. On BenchCAD the same upgrade raises the score from 41.2% to 64.0% and the cost from $0.29 to $0.75. Economy keeps Terra/Medium and can use Terra/High when a wrong turn would force later steps to be repeated. |
| Scientific computation | On AA Terminal-Bench-Science, Terra/Xhigh scores 41.90% at $1.04 and Sol/Medium scores 60.48%. At standard short-context rates and an assumed 95% hit rate for cacheable input, Sol/Medium would cost $1.39 per task. Balance chooses Sol/Medium, or Sol/High when numerical error or stability determines acceptance. For small scientific code with a specified method and independent tests, Economy can use Luna/Xhigh. On SciCode, Luna/Xhigh earned 51.74% of subproblem credit and Terra/Medium earned 51.62%. Costs reconstructed using the AA client were $0.00144 and $0.00518 per task, respectively. |
| Hard questions with a fixed answer | On AA HLE-Diamond, Terra/Medium scored 31.3% at $0.00896 per question. Sol/Medium scored 50.7% at an estimated $0.01872. This gain is worth the extra cent even for Economy. Both Economy and Balance can use Sol/High for stricter accuracy requirements (58.3%, estimated $0.04219). |
| Demanding code integration | Extra Quality uses Astra/Xhigh and Quality uses Sol/Max. In AA FrontierCode, Astra/Xhigh earns 48.95% of scoring credit at $3.75 versus 44.38% at $1.30 for Sol/Max. OpenAI FrontierCode shows a smaller gap (44.1% versus 43.8%). On PatchBench, Astra/Xhigh scores 79.7% at $2.45, matching Astra/Max at $4.18. |
| Heavy evidence synthesis | Extra Quality uses Astra/Max when the answer must cover a composite question in full. On AA MLCR its overall pass rate is 39.44%, versus 37.22% for Sol/Max. Passing requires a complete answer without contradictions. On the accuracy component, Sol/Max scores 98.89% versus 96.67% for Astra/Max. Consider Sol/Max when factual accuracy takes priority over coverage. |

AA did not report the Sol/Medium and Sol/High task costs quoted as estimates. The supplementary table provides the token counts and pricing assumptions used to calculate them. Each comparison uses point estimates from one test setup. Native Codex rework and full workflow costs remain unmeasured. [Benchmark results](benchmarks/quality-6.2.csv) · [Supplementary results and cost estimates](benchmarks/task-tradeoffs-6.2.csv)

### How Quality assigns four tasks

Each comparison below uses scores and dollars per task from the same evaluation. Artificial Analysis (AA) and OpenAI use different test setups. The scores are point estimates and the costs describe the benchmark runs. [Scores and task costs by model and effort](benchmarks/quality-6.2.csv)

| Task | Quality default | Evidence and exceptions |
| --- | --- | --- |
| Demanding code integration | Sol/Max | On AA FrontierCode 2.0, Sol/Max earned 44.38% of scoring credit at $1.2978 per task, versus 42.32% at $1.2925 for Terra/Max. Ordinary implementation stays on Terra/High. |
| Scientific computation and validation | Sol/High | On AA Terminal-Bench-Science, Terra/Max scored 57.62% and Sol/High scored 67.62%. AA has no task cost for Sol/High. In OpenAI’s run, Sol/High scored 67.7% at $1.51 and Sol/Max scored 68.0% at $2.21. Consider Astra/High (74.9% at $5.20) when the extra accuracy matters. |
| Hard questions with a fixed answer | Astra/High | On AA HLE-Diamond (1,000 questions), Astra/High scored 65.9% at $0.14656 versus 64.0% at $0.14888 for Sol/Max. Astra/Xhigh reached 67.3% at $0.23407 when higher accuracy is worth the cost. |
| Multi-step tool use under established rules | Sol/High | OpenAI’s AutomationBench score was 41.2% at $0.21 for High and 40.6% at $0.23 for Xhigh. AA found a slight pass-rate advantage for Xhigh, but fewer violations per task for High. Consider Astra/High when one permission or state violation would invalidate the result. Tool work that requires exploring the environment and adapting to feedback stays on Sol/Xhigh. |

## Frontend design and implementation

Balance uses Sol/High for original 2D interfaces that need visual or interaction decisions and browser feedback. Economy shares that default and uses Terra/Medium for straightforward implementation with a settled design and behavior. Quality uses Sol/Xhigh for original interfaces and Astra/High when visual design is a primary acceptance criterion. Extra Quality starts with Astra/High and uses Xhigh for several interacting screens or flows that must be designed and tested together. These are starting choices based on the work involved and [OpenAI's design guidance](https://developers.openai.com/api/docs/guides/model-selection). [WebDev Arena Frontend](https://arena.ai/leaderboard/code/webdev/frontend) and [Image-to-WebDev](https://arena.ai/leaderboard/code/image-to-webdev) test useful 2D distinctions. The snapshots available on 18 November 2026 lacked 6.2 results and do not establish an effort ranking.

For interactive browser 3D, AA-3D uses 55 Three.js scenes and blind human votes. Sol/Max scores 1259.28 Elo at $3.77 per scene. Astra/Max scores 1317.62 at $15.29. Both costs are reconstructed from AA's chart inputs. Balance and Economy choose Sol/Max. Quality also defaults to Sol/Max and pays the Astra premium when the brief requires both high visual fidelity and polished interaction. Extra Quality defaults to Astra/Max. The board has no Terra results or lower-effort results for 6.2 Sol and Astra. [AA-3D](https://artificialanalysis.ai/evaluations/aa-3d) · [Scores and cost inputs](benchmarks/frontend.csv)

The seven AA-3D domains help qualify that choice. On the opponent-balanced vote share, Astra leads Sol by 9.3 percentage points on games, sports and piloting, while Sol leads by 4.5 points on stories and fantasy. Each domain has five to ten scenes. The rates average over other opponents and have no matching domain costs. They support checking the brief's actual visual and interaction requirements before paying more. [AA-3D domain results](https://artificialanalysis.ai/evaluations/aa-3d)

| Functional application work | Sol/Max | Astra/Max |
| --- | ---: | ---: |
| Build an app from scratch and pass its browser workflows | 87.62%, $3.23/test | 89.90%, $7.92/test |
| Extend a working app through successive requests with regression checks | 40.94%, $12.74/scenario | 55.16%, $45.66/scenario |

Vals used OpenHands for both tests. The first measures application functionality. The second averages the fraction of consecutive requests passed, including regression checks, across 50 starting scenarios. Astra completed 18 full sequences and Sol completed 9. The 1–100 costs include unsuccessful generation work. The reported cost excludes evaluation. The individual change-type results cover the requests each model reached, so their denominators differ. For work whose difficulty is preserving behavior across dependent changes, use the integration branch and check the affected regressions. [Vibe Code Bench](https://www.vals.ai/benchmarks/vibe-code) · [Vibe Code Bench 1–100](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)

## Visual extraction, terminal recovery and deliverables

**Reading an image.** On AA MMMU-Pro, Luna/Medium scores 77.86% at $0.00038 per question, slightly ahead of Luna/High. Terra/Medium scores 82.77% at $0.00164 and Terra/High 83.82% at $0.00240. Costs are reconstructed from AA's inputs. Balance picks Terra/High when positions, labels or graphical relations determine the answer. Economy picks Medium. Quality and Extra Quality share High for this bounded work. Terra/Xhigh has the same score as High in this run, and Astra/Medium adds 2.31 points at about 3.8 times the cost. MMMU-Pro tests multimodal reasoning, so the results serve as a proxy for visual extraction. [MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro)

**Restoring a terminal environment.** Balance and Quality use Sol/High for an unfamiliar setup with a repeatable acceptance check. On AA Terminal-Bench 4.0, Sol/High scores 58.59% and Xhigh scores 56.06%. Under the same 95% cache-hit assumption for cacheable input, the estimated costs are $1.01 and $1.25 per task. Sol/Max scores 60.10% at an AA-reported $1.29. The High estimate falls below that reported cost at about 90% cache hits or higher, under the documented rates. Economy chooses Terra/High, which scores 41.92% at $0.44 versus Terra/Medium's 32.32% at $0.28. Extra Quality chooses Astra/Xhigh, which matches Astra/Max at 64.14% for $2.88 versus $4.66. The terminal suite also includes other kinds of work, so the default applies to recovery with a fixed check. [Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

**Delivering a usable file.** On AA-Briefcase, Terra/High passes 37.68% of rubric checks at $0.28 per task. Sol/High passes 49.90% at an estimated $1.01 under the same cache assumption, and Sol/Xhigh passes 51.82% at an estimated $1.30. The pooled score covers different kinds of work. In the 38 spreadsheet tasks, Sol/High scores 51.59% and Astra/High 53.86%. In the 22 presentation tasks, they score 44.08% and 55.92%. Rubrics and task mixes differ by file type. The supplementary rows give rubric scores, with costs left blank for these comparisons. Route by the work needed to deliver and verify the file, such as reconciling conflicting inputs and validating formulas in a workbook. [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase) · [Comparison data and assumptions](benchmarks/task-tradeoffs-6.2.csv)

## Applying the task evidence

**Interpreting rules.** Harvey LAB-AA v1.1 gives credit when a legal deliverable satisfies every criterion and contains no material hallucinations. In the AA results reported by OpenAI, Sol/Max scored 11.1% at $1.92 per task, and Astra/High scored 13.3% at $3.86. Cite the governing text, explain applicable exceptions and flag any unresolved priority among rules. Use the branch for constructing premises or contracts if the work calls for deciding what the rule or acceptance criteria should be. [OpenAI launch chart](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa)

**Reconciling figures.** On AA-AnalystAgent, Sol/High answered 52.5% of the 80 questions correctly on all five attempts and Astra/High answered 61.25%. For source-based calculations, record the input figures, units, assumptions and formulas needed to reproduce the result. [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · [Matched benchmark rows](benchmarks/task-tradeoffs-6.2.csv)

**Read-only engineering diagnosis.** Coding Agent Index v2.1 covers repository changes (FrontierCode-AA 2.0), terminal execution (4.1 rescoring of the same 66 Terminal-Bench 4.0 tasks) and repository Q&A (SWE-Atlas-QnA-AA). ITBench-AA tests root-cause diagnosis from offline incident records. Use local diagnosis for a bounded code or log investigation, and heavy evidence synthesis when the work turns on reconstructing a disputed timeline or causal chain across records. Cite the code or records that support the conclusion. [Coding Agent Index methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking/) · [ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa)

**Reasoning from visual sources.** Use visual extraction for details read directly from images, including simple comparisons across views. Use the relevant evidence or QA branch when the conclusion depends on interpreting visual cues or applying domain knowledge. VIALS-AA tests interpretation of scientific images, and MKA tests professional deliverables built from visually dense files. [VIALS-AA](https://artificialanalysis.ai/evaluations/vials-aa) · [MKA](https://artificialanalysis.ai/evaluations/mka)

**Checking delivered files and operations.** Reopen CAD models to verify the required geometry, constraints and editability. For timed media, check sequence and timing in rendered playback, and verify source timing where applicable. For authorized operations, compare the final state with the requested outcome and the allowed scope of changes. BenchCAD, Code2Video-AA and EnterpriseOps-Gym-AA cover geometry, rendered media and final-state checks, respectively. [BenchCAD 2.1](https://benchcad.com/blog/benchcad-2-1) · [Code2Video-AA](https://artificialanalysis.ai/methodology/intelligence-benchmarking#code2video-aa) · [EnterpriseOps-Gym-AA](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

## v0.5.0 benchmark baseline

The examples and tables below use the 15 November 2026 snapshot. In those results, Sol means GPT-6.1 Sol and Astra means GPT-6 Astra. The other candidates are GPT-6 Luna and GPT-6.1 Terra. The 15 pairs cover Medium, High, Xhigh and Max, excluding Luna/Max. [Dataset and calculator](benchmarks/README.md)

### Evidence used

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

### Comparing quality and cost

Within each source and task, compare quality gains, cost differences or multiples, and relevant risks in their original units. The [calculation guide](benchmarks/README.md#what-the-calculation-means) explains the Pareto frontier and conditional `value × quality − cost` comparison. A quality floor comes from the task's requirements, not the median or top half of the available candidates.

### Choosing the Balance defaults

Balance selects a defensible task-quality/cost compromise, rather than the cheapest pair or the highest quality/cost ratio. These examples show the decisions behind its defaults. Figures are from the referenced AA snapshot:

| Task / v0.5.0 Balance pair | Tradeoff informing the choice |
| --- | --- |
| Ordinary code / Terra/High | Terra/Medium→High adds about 2.92 scoring-credit percentage points at 1.52× cost. High→Max adds 4.86 points at 3.30× cost; the historical policy reserved that additional spend for demanding integration. The source did not separately test those two difficulty groups. |
| Complete document answers / Sol/High | Terra/Medium→Sol/High adds 3.6 all-pass percentage points at 2.10× cost. Sol/High→Astra/Xhigh adds only 0.2 points at 5.47× cost. This informs the shared Sol/High default for similar answers, not every form of document reasoning. |
| End-to-end tool work / Sol/Medium | On Terminal-Bench 4.0, Sol/Medium scores 47.98% at $0.614 per source task, versus Terra/Xhigh's 46.46% at $0.657. This is a point comparison under that harness, not proven native superiority. |

For demanding code, Terra/Max→Astra/Max adds about **0.055 scoring-credit percentage points** at **5.06×** source cost. In that historical baseline the higher profiles shared Terra/Max; this does not prove equal quality or that ordinary code has reached a plateau.

These defaults combine source observations, task matching and the stated resource preference. No fitted acceptance probability or precise willingness-to-pay parameter uniquely determines them. Task and harness differences can explain conflicting rankings; their effects have not been isolated.

### Extending the quality and cost preferences

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
