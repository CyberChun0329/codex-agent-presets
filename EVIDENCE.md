# Benchmarks and preset design

[简体中文](EVIDENCE.zh-CN.md)

The [industry evidence guide](INDUSTRY.md) gives the six Capability Index portfolios and the conditions for case-specific rule application and constrained model construction.

## GPT-6.2 model choices

All four presets use GPT-6.2 for Sol and Astra. In OpenAI’s launch results, Sol/Max scored within 0.5 points of Astra/Max on FrontierCode 2.0 at about one-fifth of its cost. On Terminal-Bench-Science 0.1, Astra gained nine percentage points over the previous Astra at less than a third of its task cost. OpenAI’s launch announcement reports a GDPval v2 gain of 5.3 percentage points for GPT-6.2 Sol over GPT-6.1 Sol. [OpenAI launch results](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Launch comparisons](benchmarks/gpt-6.2-launch.csv)

On Standard API requests with up to 272,000 input tokens, GPT-6.2 Sol costs $2 per million input tokens, $0.10 per million cached input tokens and $10 per million output tokens. GPT-6.2 Astra costs $8, $0.40 and $40 per million, respectively. Actual task cost also depends on token use. [OpenAI pricing](https://developers.openai.com/api/docs/pricing#latest-models)

### From Balance to the other presets

Choose Balance using the task's acceptance requirements and its budget or quality target. Examine alternatives on the same benchmark. Economy saves where the requirements can still be met. Quality and Extra Quality pay more when the evidence supports a useful gain. Two presets can share a pair. [Selection method](INDUSTRY.md#choose-balance-first)

| Task | Choice and evidence |
| --- | --- |
| Established tool workflows | In AA AutomationBench, Economy’s Terra/Medium passed 31.05% under strict scoring at $0.09567 and averaged 0.65753 violations per task. Balance’s Sol/Medium passed 41.40% at $0.17998 with 0.39726 violations. Quality’s Sol/High passed 40.49% at $0.20910 with 0.36073 violations. Economy uses the cheaper pair for bounded, lower-risk workflows. The higher observed violation count makes this a cost tradeoff. In a separate OpenAI run, Sol/Medium scored 40.2% at $0.18 and Sol/High scored 41.2% at $0.21. |
| Tool work with exploration and feedback | Balance uses Sol/High. On LifeVal it scores 80.8% at $0.65 versus 70.3% at $0.38 for Sol/Medium. On BenchCAD the same upgrade raises the score from 41.2% to 64.0% and the cost from $0.29 to $0.75. Economy keeps Terra/Medium and can use Terra/High when a wrong turn would force later steps to be repeated. |
| Scientific computation | On AA Terminal-Bench-Science, Terra/Xhigh scores 41.90% at $1.04 and Sol/Medium scores 60.48% at a reported $1.03 per task. Balance chooses Sol/Medium, or Sol/High when numerical error or stability determines acceptance. For small scientific code with a specified method and independent tests, Economy can use Luna/Xhigh. On SciCode, Luna/Xhigh earned 51.74% of subproblem credit and Terra/Medium earned 51.62%. Using the AA client formula with a denominator of 288, the reconstructed costs were $0.00144 and $0.00518 per evaluated subproblem, respectively. AA currently lists SciCode as legacy and under review. [AA SciCode](https://artificialanalysis.ai/evaluations/scicode) |
| Hard questions with a fixed answer | On AA HLE-Diamond, Terra/Medium scored 31.3% at $0.00896 per question. Sol/Medium scored 50.7% at an estimated $0.01872. This gain is worth the extra cent even for Economy. Both Economy and Balance can use Sol/High for stricter accuracy requirements (58.3%, estimated $0.04219). |
| Demanding code integration | Balance uses Sol/Medium for cross-component changes with established behavior. In AA FrontierCode, it earned 41.40% of scoring credit at $0.458, up from 37.46% at $0.392 for Economy’s Terra/High. Quality uses Sol/Max (44.38%, $1.30) and Extra Quality uses Astra/Xhigh (48.95%, $3.75). On PatchBench, Astra/Xhigh scored 79.7% at $2.45, matching Astra/Max at $4.18. |
| Heavy evidence synthesis | On AA MLCR, the Economy, Balance, Quality and Extra Quality pairs score 30.56% (Terra/Max, $0.06395), 35.00% (Sol/Xhigh, $0.08963), 37.22% (Sol/Max, $0.10856) and 39.44% (Astra/Max, $0.42003). Costs are reconstructed using AA’s canonical-token cost formula. Passing requires completeness and accuracy. On accuracy alone, Sol/Max scores 98.89% and Astra/Max 96.67%. Consider Sol/Max when factual accuracy takes priority over coverage. The medical-record tasks inform evidence synthesis. Independent review of coupled code behavior still needs review-specific evidence. |

The supplementary tables give reported costs and document any reconstructions or estimates. [Benchmark results](benchmarks/quality-6.2.csv) · [Supplementary results and cost estimates](benchmarks/task-tradeoffs-6.2.csv) · [Routing table and evidence notes](benchmarks/routing-0.7.0.csv)

### How Quality assigns four tasks

These comparisons use score estimates and costs per task from their respective evaluations. Artificial Analysis (AA) and OpenAI use different test setups. [Scores and task costs by model and effort](benchmarks/quality-6.2.csv)

| Task | Quality default | Evidence and exceptions |
| --- | --- | --- |
| Demanding code integration | Sol/Max | On AA FrontierCode 2.0, Sol/Max earned 44.38% of scoring credit at $1.30 per task, versus 42.75% at $0.80 for Sol/Xhigh and 42.32% at $1.29 for Terra/Max. OpenAI's separate run showed a 4-point gain over Sol/Xhigh for $0.31 more per task. Quality keeps Max for demanding integration. Ordinary implementation uses Terra/High. |
| Scientific computation and validation | Sol/High | On AA Terminal-Bench-Science, Terra/Max scored 57.62% and Sol/High scored 67.62%. In OpenAI’s run, Sol/High scored 67.7% at $1.51 and Sol/Max scored 68.0% at $2.21. Consider Astra/High (74.9% at $5.20 in OpenAI’s run) when the extra accuracy matters. |
| Hard questions with a fixed answer | Astra/High | On AA HLE-Diamond (1,000 questions), Astra/High scored 65.9% at $0.14656 versus 64.0% at $0.14888 for Sol/Max. Astra/Xhigh reached 67.3% at $0.23407 when higher accuracy is worth the cost. |
| Multi-step tool use under established rules | Sol/High | OpenAI’s AutomationBench score was 41.2% at $0.21 for High and 40.6% at $0.23 for Xhigh. AA found a slight pass-rate advantage for Xhigh, but fewer violations per task for High. Consider Astra/High when one permission or state violation would invalidate the result. Tool work that requires exploring the environment and adapting to feedback stays on Sol/Xhigh. |

**Extra Quality scientific execution.** Astra/Xhigh is the default. In AA Terminal-Bench-Science, Astra/Xhigh scored 78.57% at $6.27 per task and Astra/Max scored 78.10% at $9.78. In OpenAI’s separate run, the same pairs scored 74.0% at $5.37 and 77.1% at $7.15. Choose Max directly when evidence close to the task supports an accuracy gain that matters to its acceptance. Once the method and numeric tests are established, code integration can determine the route. When assessing stability, approximation error or numerical validity is central, use scientific execution. [OpenAI launch results](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Benchmark results](benchmarks/quality-6.2.csv)

## Frontend design and implementation

Balance uses Sol/High for original 2D interfaces that need visual or interaction decisions and browser feedback. Economy shares that default and uses Terra/Medium for straightforward implementation with a settled design and behavior. Quality uses Sol/Xhigh for original interfaces and Astra/High when visual design is a primary acceptance criterion. Extra Quality starts with Astra/High and uses Xhigh for several interacting screens or flows that must be designed and tested together. These are starting choices based on the work involved and [OpenAI's design guidance](https://developers.openai.com/api/docs/guides/model-selection). [WebDev Arena Frontend](https://arena.ai/leaderboard/code/webdev/frontend) and [Image-to-WebDev](https://arena.ai/leaderboard/code/image-to-webdev) test useful 2D distinctions. The 20 November WebDev snapshot includes 6.2 Max results. The comparison still lacks Medium, High and Xhigh results for 6.2. [WebDev scores and costs](benchmarks/benchmark-refresh-6.2.csv)

For interactive browser 3D, AA-3D uses 55 Three.js scenes and blind human votes. Sol/Max scores 1259.28 Elo at $3.77 per scene. Astra/Max scores 1317.62 at $15.29. Both costs are reconstructed from AA's chart inputs. Balance and Economy choose Sol/Max. Quality also defaults to Sol/Max and pays the Astra premium when the brief requires both high visual fidelity and polished interaction. Extra Quality defaults to Astra/Max. The board has no Terra results or lower-effort results for 6.2 Sol and Astra. [AA-3D](https://artificialanalysis.ai/evaluations/aa-3d) · [Scores and cost inputs](benchmarks/frontend.csv)

The seven AA-3D domains help qualify that choice. On the opponent-balanced vote share, Astra leads Sol by 9.3 percentage points on games, sports and piloting, while Sol leads by 4.5 points on stories and fantasy. Each domain has five to ten scenes. The rates average over other opponents and have no matching domain costs. They support checking the brief's actual visual and interaction requirements before paying more. [AA-3D domain results](https://artificialanalysis.ai/evaluations/aa-3d)

| Functional application work | Sol/Max | Astra/Max |
| --- | ---: | ---: |
| Build an app from scratch and pass its browser workflows | 87.62%, $3.23/test | 89.90%, $7.92/test |
| Extend a working app through successive requests with regression checks | 40.94%, $12.74/scenario | 55.16%, $45.66/scenario |

Vals used OpenHands for both tests. The first measures application functionality. The second averages the fraction of consecutive requests passed, including regression checks, across 50 starting scenarios. Astra completed 18 full sequences and Sol completed 9. The 1–100 costs include unsuccessful generation work. The reported cost excludes evaluation. The individual change-type results cover the requests each model reached, so their denominators differ. For work whose difficulty is preserving behavior across dependent changes, use the integration branch and check the affected regressions. [Vibe Code Bench](https://www.vals.ai/benchmarks/vibe-code) · [Vibe Code Bench 1–100](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)

## Visual extraction, terminal recovery and deliverables

**Reading an image.** On AA MMMU-Pro, Luna/Medium scores 77.86% at $0.00038 per question, slightly ahead of Luna/High. Terra/Medium scores 82.77% at $0.00164 and Terra/High 83.82% at $0.00240. Costs are reconstructed from AA's inputs. Balance picks Terra/High when positions, labels or graphical relations determine the answer. Economy picks Medium. Quality and Extra Quality share High for this bounded work. Terra/Xhigh has the same score as High in this run, and Astra/Medium adds 2.31 points at about 3.8 times the cost. MMMU-Pro tests multimodal reasoning, so the results serve as a proxy for visual extraction. [MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro)

**Restoring a terminal environment.** Balance and Quality use Sol/High for an unfamiliar setup with a repeatable acceptance check. On AA Terminal-Bench 4.0, Sol/High scores 58.59% at $0.77057 per task, Xhigh scores 56.06% at $0.93389, and Max scores 60.10% at $1.29354. Economy chooses Terra/High, which scores 41.92% at $0.44 versus Terra/Medium’s 32.32% at $0.28. Extra Quality chooses Astra/Xhigh, which matches Astra/Max at 64.14% for $2.88 versus $4.66. The suite includes several kinds of terminal work, so these results are a proxy for recovery with a fixed check. [Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

**Delivering a usable file.** On AA-Briefcase, Terra/High passes 37.68% of pooled rubric checks at $0.28 per task. Sol/High passes 49.90% at $0.79306 and Sol/Xhigh passes 51.82% at $1.00819. These percentages are shares of all binary rubric checks passed across tasks. In the 38 spreadsheet tasks, Sol/High scores 51.59% and Astra/High 53.86%. In the 22 presentation tasks, they score 44.08% and 55.92%. Matched costs for individual file types are unavailable for these comparisons. When assembling or verifying an editable deliverable requires exploring tools and iterating, use the end-to-end tools branch even with a supplied layout. [AA-Briefcase rubric](https://artificialanalysis.ai/evaluations/aa-briefcase?results=rubric-score) · [Comparison data](benchmarks/task-tradeoffs-6.2.csv)

In OpenAI’s Agents’ Last Exam v1.1 run of long-horizon professional workflows, Astra/Xhigh scored 78.33% at $2.89 per task and Astra/Max scored 77.61% at $4.47. [OpenAI launch results](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Publisher observations](benchmarks/publisher-observations-6.2.csv)

**Designing visual communication.** Building slides to a supplied layout is prescribed work when how to assemble and verify the output is established. Choosing an original visual hierarchy, diagram or visual narrative involves design decisions. Inspect the rendered composition against the brief in either case. Briefcase pools different presentation tasks, and the web results above cover browser interfaces. The relative performance of model and effort pairs on original slide, diagram and motion design remains open. [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase) · [Frontend comparisons](benchmarks/frontend.csv)

## Applying the task evidence

**Answering from documents.** Use literal lookup when text or structured data gives a single unambiguous answer directly. Document Q&A combines stated facts from supplied material. On AA GDP.pdf, Terra/Medium passes all criteria on 28.4% of attempts at $0.167 per task, Sol/Medium on 29.2% at $0.33444, and Sol/High on 28.8% at $0.34114. Economy uses Terra/Medium. The other tiers use Sol/Medium for this task. GDP.pdf is a broader document-reasoning benchmark, and its aggregate scores differ little between Medium and High. When rule interpretation, conflicting records or visual inference determines the answer, use the corresponding evidence branch. [GDP.pdf](https://artificialanalysis.ai/evaluations/gdp-pdf) · [Comparison rows](benchmarks/task-tradeoffs-6.2.csv)

**Finding sources.** A scout can search a predefined scope using criteria that can be applied mechanically. Economy and Balance use Terra/Medium and Quality and Extra Quality use Terra/High as prescribed-work defaults. Open research requires judging which sources can answer the question, their authority or their coverage. State what the sources cover and where the record is incomplete. Epoch’s real-work evaluation offers cases for checking coverage and completeness. Evidence for choosing model and effort pairs on either kind of source discovery remains limited. [Epoch real-work evaluation](https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work)

**Interpreting rules.** Harvey LAB-AA v1.1 gives credit when a legal deliverable satisfies every criterion and contains no material hallucinations. In the AA results reported by OpenAI, Sol/Max scored 11.1% at $1.92 per task, and Astra/High scored 13.3% at $3.86. Cite the governing text, explain applicable exceptions and flag any unresolved priority among rules. Use the branch for constructing premises or contracts if the work calls for deciding what the rule or acceptance criteria should be. [OpenAI launch chart](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa)

**Reconciling figures.** On AA-AnalystAgent, Sol/High answered 52.5% of the 80 questions correctly on all five attempts and Astra/High answered 61.25%. For source-based calculations, record the input figures, units, assumptions and formulas needed to reproduce the result. [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · [Matched benchmark rows](benchmarks/task-tradeoffs-6.2.csv)

The Vals release results for Astra and Sol at Max show different gaps by index. Astra scores 68.44% to Sol’s 57.76% on science, 57.31% to 56.66% on finance and 69.68% to 66.67% on legal. The indices pool different tasks and each model was evaluated at one effort. [Vals Astra results](https://www.vals.ai/models/openai_gpt-6.2-astra) · [Vals Sol results](https://www.vals.ai/models/openai_gpt-6.2-sol)

In Plotly DataAnalyticsBench, Astra passed 41 of 43 questions for $4.11 and Sol passed 40 of 43 for $1.22. Costs cover one full run per model. Plotly does not disclose the reasoning effort, and the one-question gap falls within the run-to-run variation Plotly observed on retests of other models. [Plotly Astra run](https://plotly.com/blog/gpt-6-2-astra-plotly-data-analytics-bench/) · [Plotly Sol run](https://plotly.com/blog/gpt-6-2-sol-plotly-data-analytics-bench/)

**Reading a repository, reviewing behavior and making a change.** Use local diagnosis for a bounded code or log investigation. A read-only review of an invariant across components calls for a reviewer and a pair suited to the technical reasoning involved. An authorized fix follows the implementation branch. Use heavy evidence synthesis when the work turns on reconstructing a disputed timeline or causal chain across records. Cite the code or records that support the finding. ITBench-AA tests diagnosis from offline incident records. ReviewBench offers criteria for missed findings and false alarms in code review. [ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) · [ReviewBench](https://github.com/review-bench/ReviewBench)

Coding Agent Index v2.1 illustrates why repository Q&A and terminal execution merit separate comparisons. In the same Codex harness, Sol/High, Xhigh and Max pass **50.54%, 51.34% and 46.24%** on SWE-Atlas-QnA-AA, and **53.54%, 57.58% and 58.08%** on Terminal-Bench 4.1. Version 4.1 rescored the same 66 tasks as Terminal-Bench 4.0. Average API costs for the full suite, including FrontierCode-AA 2.0, are **$0.764, $0.898 and $1.216** per task, respectively. Independent cross-component review needs its own evaluation. [Coding Agent Index methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking/) · [Codex results](benchmarks/codex-agent-2.1.csv)

**Answering when uncertainty is allowed.** On AA-Omniscience v1.1, Astra/Medium has a net score of 44.77 and 64.17% accuracy at $0.00673 per question. Sol/Max scores 40.37 net and 61.63% accuracy at $0.05284. The net score adds credit for correct answers and subtracts credit for errors. Astra/Medium is worth testing on knowledge questions that permit abstention. Evaluate finding and validating sources on separate evidence tasks. [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience) · [Comparison rows](benchmarks/task-tradeoffs-6.2.csv)

**Solving a research-level physics problem.** On the CritPt v2 hard subset, Astra/Medium scores 67.5% at $0.1928 per problem. High and Max both score 71.5%, at $0.4471 and $1.2756 respectively. These subset costs accompany the subset scores and support considering Medium for tool-assisted problems with defined acceptance. The full suite uses a different task denominator. [CritPt v2](https://artificialanalysis.ai/evaluations/critpt-v2) · [Full and hard-subset comparisons](benchmarks/task-tradeoffs-6.2.csv)

**Reasoning from visual sources.** Use visual extraction for details read directly from images, including simple comparisons across views. Use the relevant evidence or QA branch when the conclusion depends on interpreting visual cues or applying domain knowledge. VIALS-AA tests interpretation of scientific images, and MKA tests professional deliverables built from visually dense files. [VIALS-AA](https://artificialanalysis.ai/evaluations/vials-aa) · [MKA](https://artificialanalysis.ai/evaluations/mka)

**Checking delivered files and operations.** Reopen CAD models to verify the required geometry, constraints and editability. For timed media, check sequence and timing in rendered playback, and verify source timing where applicable. For authorized operations, compare the final state with the requested outcome and the allowed scope of changes. BenchCAD, Code2Video-AA and EnterpriseOps-Gym-AA cover geometry, rendered media and final-state checks, respectively. [BenchCAD 2.1](https://benchcad.com/blog/benchcad-2-1) · [Code2Video-AA](https://artificialanalysis.ai/methodology/intelligence-benchmarking#code2video-aa) · [EnterpriseOps-Gym-AA](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

In OpenAI's BenchCAD 2.1 Core run, Sol/High scores 64.0% at $0.75 per task, Sol/Xhigh 70.4% at $1.00, and Sol/Max 73.1% at $1.60. These results help choose comparison pairs for parametric CAD. Check the requested geometry and constraints in the delivered model itself. [OpenAI launch chart](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Comparison rows](benchmarks/task-tradeoffs-6.2.csv)

The captured AA-PersonalityBench data lack Terra, and the captured Decision Index and HealthBench Professional results lack Sol and Astra. OpenAI's HealthBench Professional system-card table gives aggregate results without matched scores and costs by effort. [AA-PersonalityBench](https://artificialanalysis.ai/evaluations/aa-personalitybench) · [Decision Index](https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index) · [HealthBench Professional](https://artificialanalysis.ai/evaluations/healthbench) · [OpenAI system card](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf#page=74)

Benchmark costs cover the benchmark runs. Codex workflow costs, including handoffs and rework, remain unmeasured.

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

Balance weighs the score gain against the extra cost for each task. The figures below come from the AA snapshot.

| Task / v0.5.0 Balance pair | Tradeoff informing the choice |
| --- | --- |
| Ordinary code / Terra/High | Terra/Medium→High adds about 2.92 scoring-credit percentage points at 1.52× cost. High→Max adds 4.86 points at 3.30× cost; the historical policy reserved that additional spend for demanding integration. The source did not separately test those two difficulty groups. |
| Complete document answers / Sol/High | Terra/Medium→Sol/High adds 3.6 all-pass percentage points at 2.10× cost. Sol/High→Astra/Xhigh adds only 0.2 points at 5.47× cost. This informs the shared Sol/High default for similar answers, not every form of document reasoning. |
| End-to-end tool work / Sol/Medium | On Terminal-Bench 4.0, Sol/Medium scores 47.98% at $0.614 per source task, versus Terra/Xhigh's 46.46% at $0.657. This is a point comparison under that harness, not proven native superiority. |

For demanding code, Terra/Max→Astra/Max adds about **0.055 scoring-credit percentage points** at **5.06×** source cost. In that historical baseline the higher profiles shared Terra/Max; this does not prove equal quality or that ordinary code has reached a plateau.

The defaults reflect the benchmark results, how closely each benchmark matches the task and the profile’s cost preference. The defaults use no fitted probability of acceptance or fixed dollar value per score point. Differences in tasks and test setups may account for conflicting rankings. The comparisons do not isolate those effects.

### Extending the quality and cost preferences

Economy accepts some loss of quality margin to reduce cost where the task's requirements permit it. Quality retains Sol/High or Xhigh for normal substantive judgments and pays more for gains relevant to the task. Extra Quality accepts larger premiums for further gains. The task's acceptance requirements still apply in all four.

Heavy evidence synthesis illustrates this approach: reconstructing chronology or causal chains, resolving conflicting records and answering composite questions under a fixed framework. MLCR informs this narrow route; a long document, citations or a medical label alone do not trigger it.

| Profile | Pair | MLCR complete-answer pass | Source cost/task |
| --- | --- | ---: | ---: |
| Economy | Terra/Max | 30.56% | $0.06395 |
| Balance | Sol/Xhigh | 35.56% | $0.09374 |
| Quality | Sol/Max | 38.33% | $0.11193 |
| Extra Quality | Astra/Max | 41.67% | $0.57256 |

In this snapshot, Terra/Max costs less than Sol/Medium, which is why an Economy route can use Max. Sol/High→Sol/Max gains 6.67 pass percentage points for about 29% more source cost. Extra's final 3.33-point gain over Sol/Max costs about 5.12×: it is a quality premium, not better cost efficiency. MLCR has matching observations for 12 of 15 pairs; Terra/Medium, High and Xhigh are missing. Its accuracy component is not monotone along this sequence, so the overall pass increase is not improvement on every dimension.

AA-LCR provides a countercheck: Sol/Medium, High and Max score about 83.33%, 82.33% and 83.00%. Longer context therefore does not justify a general Max rule. The heavy-synthesis mapping remains a policy choice, not a causal result about a single task feature.

These point estimates come from the benchmarks. They do not establish a unique best model or statistically significant differences. AA's weighted Cost per Task summarizes AA's task mix. Use the individual comparisons for a specific task. Subscription allowances require separate data.

Profiles can share a model/effort pair. Difficult integration, a complete answer from documents and a tool workflow with several states can call for different choices even when all involve files or code. Base the assignment on the work required, even for lengthy or medical tasks or those involving a terminal. Check the defaults against your quality requirements and observed workflow costs. The profiles impose no fixed sequence of models, usage quota or requirement that a cheaper attempt fail first.
