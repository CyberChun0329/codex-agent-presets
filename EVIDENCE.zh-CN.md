# 评测依据与预设设计

[English](EVIDENCE.md)

## 为什么换用 GPT-6.2

四档预设中的 Sol 和 Astra 均使用 GPT-6.2。在 OpenAI 的 FrontierCode 2.0 测试中，Sol/Max 与 Astra/Max 的得分相差不超过 0.5 分，前者的成本约为后者的五分之一。在 Terminal-Bench-Science 0.1 上，新版 Astra 比上一代高 9 个百分点，每题成本低于上一代的三分之一。OpenAI 的发布公告称，GPT-6.2 Sol 在 GDPval v2 上比 GPT-6.1 Sol 高 5.3 个百分点。[OpenAI 发布评测](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [发布对照数据](benchmarks/gpt-6.2-launch.csv)

按标准 API 费率，输入量不超过 272,000 token 时，GPT-6.2 Sol 的每百万输入、缓存命中输入和输出 token 分别为 2、0.10 和 10 美元。GPT-6.2 Astra 对应的每百万 token 费率为 8、0.40 和 40 美元。实际任务成本还取决于 token 用量。[OpenAI 定价](https://developers.openai.com/api/docs/pricing#latest-models)

### 怎样从 Balance 确定其他档位

每类任务先选 Balance，衡量额外成本能带来多少得分提升，以及出错会带来什么后果。Economy 更重视成本，Quality 和 Extra Quality 依次更愿意为有依据的质量收益付费。有些任务可共用一个组合，例如 Economy 和 Balance 的答案固定的困难问答。

| 任务 | 选择依据 |
| --- | --- |
| 按既定规则操作并跟踪状态 | 在 AA AutomationBench 上，Economy 的 Terra/Medium 严格通过率为 31.05%，每题 $0.09567、平均违规 0.65753 次。Balance 的 Sol/Medium 为 41.40%、$0.17998、0.39726 次。Quality 的 Sol/High 为 40.49%、$0.20910、0.36073 次。Economy 在范围明确、风险较低的流程中使用费用较低的组合。测试中观察到的违规次数更多，是这项成本取舍的依据之一。在 OpenAI 另行进行的测试中，Sol/Medium 为 40.2%、每题 $0.18，Sol/High 为 41.2%、每题 $0.21。 |
| 需要探索环境、按反馈调整的工具任务 | Balance 选 Sol/High。LifeVal 上，High 为 80.8%、每题 $0.65，Medium 为 70.3%、每题 $0.38。BenchCAD 上，同样的升级让得分从 41.2% 升至 64.0%，每题费用从 $0.29 升至 $0.75。Economy 保留 Terra/Medium，如果走错一步会导致后续步骤重做，可直接选 Terra/High。 |
| 科学计算 | 在 AA Terminal-Bench-Science 上，Terra/Xhigh 为 41.90%、每题 $1.04，Sol/Medium 为 60.48%、AA 报告每题 $1.03。Balance 选 Sol/Medium，数值误差或稳定性决定验收时选 Sol/High。对于方法已定、有独立测试可验收的小型科学代码，Economy 可选 Luna/Xhigh。在 SciCode 上，Luna/Xhigh 和 Terra/Medium 的子题得分率分别为 51.74% 和 51.62%。按 AA 客户端公式以 288 道参评子题为分母复算，平均每道参评子题的费用分别为 $0.00144 和 $0.00518。AA 目前将 SciCode 标为旧版评测，正在重新审查。 [AA SciCode](https://artificialanalysis.ai/evaluations/scicode) |
| 答案固定的困难问答 | 在 AA HLE-Diamond 上，Terra/Medium 的准确率为 31.3%，每题 $0.00896。Sol/Medium 的准确率为 50.7%，估算每题 $0.01872。即使是 Economy，这段准确率提升也值得每题多花约一美分。Economy 和 Balance 在准确率要求更高时都可选 Sol/High（58.3%，估算每题 $0.04219）。 |
| 困难代码集成 | Extra Quality 选 Astra/Xhigh，Quality 选 Sol/Max。在 AA FrontierCode 上，两者分别拿到 48.95% 和 44.38% 的评分点，每题分别为 $3.75 和 $1.30。OpenAI FrontierCode 测得的差距较小（44.1% 对 43.8%）。在 PatchBench 上，Astra/Xhigh 和 Astra/Max 同为 79.7%，每题分别为 $2.45 和 $4.18。 |
| 重证据综合 | 在 AA MLCR 上，Economy、Balance、Quality 和 Extra Quality 所用组合的通过率分别为 30.56%（Terra/Max，每题 $0.06395）、35.00%（Sol/Xhigh，$0.08963）、37.22%（Sol/Max，$0.10856）和 39.44%（Astra/Max，$0.42003）。费用均按 AA 客户端的分词计价公式复算。该评测要求答案完整且准确。单看准确性，Sol/Max 为 98.89%，Astra/Max 为 96.67%。验收更重视事实准确性时可选 Sol/Max。医疗记录题可为证据综合提供参考，独立审查耦合代码行为仍需要审查任务的证据。 |

补充表列出来源报告的费用，并说明复算或估算的依据。[评测结果](benchmarks/quality-6.2.csv) · [补充结果与费用估算](benchmarks/task-tradeoffs-6.2.csv) · [分工与证据对照表](benchmarks/routing-0.6.0.csv)

### Quality 的四类任务怎么分

各组比较使用对应评测的得分点估计和每题成本，费用以美元计。Artificial Analysis（AA）与 OpenAI 的测试环境不同。[各模型和推理档位的得分与成本](benchmarks/quality-6.2.csv)

| 任务 | Quality 默认组合 | 选择依据与例外 |
| --- | --- | --- |
| 困难代码集成 | Sol/Max | 在 AA FrontierCode 2.0 上，Sol/Max 拿到 44.38% 的评分点，每题 $1.30。Sol/Xhigh 为 42.75%、$0.80，Terra/Max 为 42.32%、$1.29。OpenAI 的另一组测试中，Sol/Max 比 Xhigh 高 4 个百分点，每题多 $0.31。Quality 的困难集成继续用 Max，普通代码实现用 Terra/High。 |
| 科学计算与验证 | Sol/High | 在 AA Terminal-Bench-Science 上，Terra/Max 得分为 57.62%，Sol/High 为 67.62%。在 OpenAI 的测试中，Sol/High 为 67.7%、每题 $1.51，Sol/Max 为 68.0%、每题 $2.21。如果任务值得为准确率支付更多，可以选 Astra/High（在 OpenAI 的测试中为 74.9%、每题 $5.20）。 |
| 答案固定的困难问答 | Astra/High | 在 AA HLE-Diamond 的 1,000 道题上，Astra/High 答对 65.9%，每题 $0.14656。Sol/Max 答对 64.0%，每题 $0.14888。需要更高准确率时可选 Astra/Xhigh（67.3%、每题 $0.23407）。 |
| 按既定规则操作、需要跟踪状态的多步工具任务 | Sol/High | 在 OpenAI 的 AutomationBench 上，High 的得分为 41.2%，每题 $0.21，Xhigh 为 40.6%，每题 $0.23。AA 测得 Xhigh 的严格通过率略高，但 High 每题违规次数略少。若一次违反权限或状态约束就会让结果失效，可选 Astra/High。需要探索环境、按反馈调整操作的端到端任务继续用 Sol/Xhigh。 |

**Extra Quality 的科学计算。** 默认用 Astra/Xhigh。在 AA Terminal-Bench-Science 上，Astra/Xhigh 为 78.57%、每题 $6.27，Astra/Max 为 78.10%、$9.78。OpenAI 的另一组测试中，两者分别为 74.0%、$5.37 和 77.1%、$7.15。接近实际任务的证据支持对验收有价值的准确性提升时，可直接用 Max。数值方法和测试已定后，若验收取决于代码集成，按代码工作分配。验收取决于判断稳定性、近似误差或数值有效性时，按科学计算分配。[OpenAI 发布评测](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [评测结果](benchmarks/quality-6.2.csv)

## 前端设计与实现

原创 2D 界面要决定视觉或交互并在浏览器中验证时，Balance 和 Economy 用 Sol/High。已有设计与行为规范的局部实现，Economy 用 Terra/Medium。Quality 的原创界面默认用 Sol/Xhigh，视觉设计本身是主要验收项时用 Astra/High。Extra Quality 默认用 Astra/High，多个相互影响的页面或流程需要一并设计和测试时用 Xhigh。这些默认依据工作特点和 [OpenAI 的设计建议](https://developers.openai.com/api/docs/guides/model-selection)。[WebDev Arena Frontend](https://arena.ai/leaderboard/code/webdev/frontend) 和 [Image-to-WebDev](https://arena.ai/leaderboard/code/image-to-webdev) 分别提供前端生成与参考图还原的评测。2026 年 11 月 18 日可查到的快照没有 6.2 成绩，无法据此确定推理档位的排序。

AA-3D 用 55 个 Three.js 场景进行人工盲评。Sol/Max 为 1259.28 Elo，每场景约 $3.77。Astra/Max 为 1317.62 Elo，每场景约 $15.29。两项费用均按 AA 图表输入复算。Balance 和 Economy 选 Sol/Max。Quality 也默认用 Sol/Max，明确要求较高视觉保真度和成熟交互时选 Astra/Max。Extra Quality 默认用 Astra/Max。榜单没有 Terra 的结果，也没有两款 6.2 的较低推理档结果。[AA-3D](https://artificialanalysis.ai/evaluations/aa-3d) · [得分与费用输入](benchmarks/frontend.csv)

AA-3D 的七个子场景能看出差异。在按对手等权的票数胜率上，Astra 在游戏、运动与驾驶组领先 Sol 9.3 个百分点，Sol 在故事与幻想组领先 4.5 个百分点。每组有 5 到 10 个场景，胜率是对其他对手的平均值，也没有对应的分组费用。是否值得加价，仍要结合交付要求的视觉和交互质量。[AA-3D 分场景结果](https://artificialanalysis.ai/evaluations/aa-3d)

| Web 应用功能任务 | Sol/Max | Astra/Max |
| --- | ---: | ---: |
| 从零搭建应用，验收浏览器里的功能流程 | 87.62%，每题 $3.23 | 89.90%，每题 $7.92 |
| 连续修改既有应用，每轮检查回归 | 40.94%，每组 $12.74 | 55.16%，每组 $45.66 |

两项 Vals 测试均使用 OpenHands。第一项测应用功能，第二项在 50 个起始场景上计算连续通过的请求比例，包含回归检查。Astra 完成了 18 组完整请求，Sol 完成了 9 组。1–100 的费用涵盖未成功的生成过程，评估开销另计。按变更类型拆出的成绩只统计各模型实际到达的请求，分母不同。若任务的难点是跨多个相互依赖的改动保留既有行为，应按代码集成分工，并验收受影响的旧流程。[Vibe Code Bench](https://www.vals.ai/benchmarks/vibe-code) · [Vibe Code Bench 1–100](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)

## 读图提取、终端恢复与成品交付

**读图提取。** 在 AA MMMU-Pro 上，Luna/Medium 得分为 77.86%、每题 $0.00038，略高于 Luna/High。Terra/Medium 为 82.77%、$0.00164，Terra/High 为 83.82%、$0.00240。费用按 AA 输入复算。当图中的位置、标注或关系决定答案时，Balance 选 Terra/High，Economy 选 Medium，Quality 和 Extra Quality 都选 High。Terra/Xhigh 此次与 High 同分。Astra/Medium 高 2.31 个百分点，费用约为 Terra/High 的 3.8 倍。MMMU-Pro 测的是多模态推理，结果用来间接参考读图提取。 [MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro)

**终端环境恢复。** 对于需要探索陌生环境且能用可重复检查验收的恢复任务，Balance 和 Quality 用 Sol/High。AA Terminal-Bench 4.0 上，Sol/High 为 58.59%、每题 $0.77057，Xhigh 为 56.06%、$0.93389，Max 为 60.10%、$1.29354。Economy 选 Terra/High，得分 41.92%、每题 $0.44，Terra/Medium 为 32.32%、$0.28。Extra Quality 选 Astra/Xhigh，与 Astra/Max 同为 64.14%，每题分别为 $2.88 和 $4.66。这套评测包含多种终端任务，可为有明确验收检查的环境恢复提供间接参考。[Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

**可用成品交付。** AA-Briefcase 中 Terra/High 的评分项通过率为 37.68%，每题 $0.28。Sol/High 为 49.90%、$0.79306，Sol/Xhigh 为 51.82%、$1.00819。通过率按所有任务的二元评分项汇总。在 38 项工作簿任务上，Sol/High 为 51.59%，Astra/High 为 53.86%。在 22 项演示稿任务上，两者分别为 44.08% 和 55.92%。这些格式分项缺少对应的费用数据。即使已有版式，制作或验证可编辑成品仍需探索工具并按反馈调整时，按端到端工具工作分配。[AA-Briefcase 评分项](https://artificialanalysis.ai/evaluations/aa-briefcase?results=rubric-score) · [任务对照数据](benchmarks/task-tradeoffs-6.2.csv)

OpenAI 用 Agents’ Last Exam v1.1 评估耗时较长、涉及多步的专业工作。Astra/Xhigh 得分为 78.33%，每题 $2.89，Astra/Max 为 77.61%、$4.47。[OpenAI 发布评测](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [发布方评测数据](benchmarks/publisher-observations-6.2.csv)

**设计视觉表达。** 已提供版式且制作和验收方式已定的演示稿，按既定要求处理。需要原创信息层级、图解或视觉叙事时，按设计工作分配。两种情况都要根据要求核对渲染效果。Briefcase 合并了不同类型的演示稿任务，上文的 Web 结果针对浏览器界面。原创演示稿、图解和动效设计还缺少可比较的模型与推理档位成绩。[AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase) · [前端对照](benchmarks/frontend.csv)

## 如何按任务使用补充证据

**依据文档作答。** 文本或结构化数据能直接给出唯一且无歧义的答案时，按直接查找处理。汇集给定材料中明示的事实属于文档问答。在 AA GDP.pdf 上，Terra/Medium 的全项通过率为 28.4%，每题 $0.167，Sol/Medium 为 29.2%、$0.33444，Sol/High 为 28.8%、$0.34114。三者得分接近。Economy 用 Terra/Medium，Balance 用 Sol/Medium。Quality 和 Extra Quality 面向更广的文档问答，暂保留 Sol/High，等待同条件案例对照。若答案取决于解释规则、消解记录冲突或根据图像推断，则使用对应的取证分支。[GDP.pdf](https://artificialanalysis.ai/evaluations/gdp-pdf) · [对照数据](benchmarks/task-tradeoffs-6.2.csv)

**查找来源。** 搜索范围预先界定、筛选标准可直接应用时，可交给 scout。Economy 和 Balance 默认用 Terra/Medium，Quality 和 Extra Quality 用 Terra/High。若要判断哪些来源能回答问题、来源是否权威或覆盖是否充分，按开放找证处理。报告实际覆盖和记录缺口。Epoch 的实际工作评测提供了检查来源覆盖和结论完整性的案例。两类来源查找适用的模型与推理档位仍缺少直接证据。[Epoch 实际工作评测](https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work)

**解读既定规则。** Harvey LAB-AA v1.1 只有在法律交付物满足全部评分标准、没有实质性幻觉时才计为通过。在 OpenAI 转引的 AA 结果中，Sol/Max 为 11.1%、每题 $1.92，Astra/High 为 13.3%、每题 $3.86。引用适用条文，说明相关例外，并报告尚未厘清的规则优先顺序。若工作要决定规则或验收标准本身，则按构造前提或系统约定的分工处理。[OpenAI 发布图](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa)

**核对并计算数据。** AA-AnalystAgent 的 80 道题中，Sol/High 五次均答对的比例为 52.5%，Astra/High 为 61.25%。依据材料计算时，记录可供复算的原始数值、单位、假设和公式。[AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · [分档对照数据](benchmarks/task-tradeoffs-6.2.csv)

Vals 发布的 Astra 与 Sol Max 档结果在各指数的差距不同。科学指数上，Astra 为 68.44%，Sol 为 57.76%。金融指数分别为 57.31% 和 56.66%，法律指数分别为 69.68% 和 66.67%。各指数汇总的任务不同，每个模型只测试了一个推理档位。[Vals Astra 结果](https://www.vals.ai/models/openai_gpt-6.2-astra) · [Vals Sol 结果](https://www.vals.ai/models/openai_gpt-6.2-sol)

在 Plotly DataAnalyticsBench 上，Astra 通过 43 题中的 41 题，费用为 $4.11。Sol 通过 40 题，费用为 $1.22。费用均对应一次完整测试。Plotly 未披露推理档位，一题之差落在 Plotly 对其他模型复测时观察到的波动范围内。[Plotly Astra 结果](https://plotly.com/blog/gpt-6-2-astra-plotly-data-analytics-bench/) · [Plotly Sol 结果](https://plotly.com/blog/gpt-6-2-sol-plotly-data-analytics-bench/)

**读代码、审查行为与修复。** 范围明确的代码或日志排查按局部诊断处理。跨组件只读审查需要沿执行路径核对既定不变量，交给 reviewer，并按所需技术判断选择组合。已获授权的修复进入实现分支。若关键在于跨记录重建有争议的时间线或因果链，则按重证据综合分工。引用支持结论的代码或记录。ITBench-AA 用离线事故记录考查诊断。ReviewBench 可参考其代码审查漏报与误报的标准。[ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) · [ReviewBench](https://github.com/review-bench/ReviewBench)

Coding Agent Index v2.1 的分项表现支持分别比较仓库问答和终端执行。在同一 Codex 环境中，Sol/High、Xhigh、Max 在 SWE-Atlas-QnA-AA 的通过率分别为 **50.54%、51.34%、46.24%**，在 Terminal-Bench 4.1 则为 **53.54%、57.58%、58.08%**。4.1 对 4.0 的同一批 66 道题重新评分。包括 FrontierCode-AA 2.0 在内的整套评测，平均 API 费用分别为每题 **$0.764、$0.898、$1.216**。独立的跨组件审查仍需用审查任务评估。[Coding Agent Index 方法](https://artificialanalysis.ai/methodology/coding-agents-benchmarking/) · [Codex 成绩](benchmarks/codex-agent-2.1.csv)

**允许保留未知的问答。** AA-Omniscience v1.1 上，Astra/Medium 的净分为 44.77，准确率为 64.17%，每题 $0.00673。Sol/Max 为 40.37、61.63%、每题 $0.05284。净分计入答对的得分并扣除错误答案的分数。允许弃答的知识问答值得考虑 Astra/Medium。查找和核实来源的能力需用取证任务另行评估。[AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience) · [对照数据](benchmarks/task-tradeoffs-6.2.csv)

**求解研究级物理题。** 在 CritPt v2 困难子集上，Astra/Medium 得分为 67.5%，每题 $0.1928。High 与 Max 同为 71.5%，每题分别为 $0.4471 和 $1.2756。得分和费用均对应困难子集，支持在验收明确、可借助工具的求解任务中考虑 Medium。完整题集使用不同的题目分母。[CritPt v2](https://artificialanalysis.ai/evaluations/critpt-v2) · [完整题集与困难子集对照](benchmarks/task-tradeoffs-6.2.csv)

**从图像证据推断。** 可直接从图中读取的细节，包括跨视图的简单对照，按读图提取分工。如果结论依赖解释视觉线索或应用领域知识，按相应的证据判断或问答任务处理。VIALS-AA 测试科学图像解读，MKA 测试依据视觉信息密集的材料制作专业交付物。[VIALS-AA](https://artificialanalysis.ai/evaluations/vials-aa) · [MKA](https://artificialanalysis.ai/evaluations/mka)

**验收交付物和操作结果。** 重新打开 CAD 模型，核对所要求的几何、约束和可编辑性。对有时序要求的媒体，在渲染回放中检查顺序与时间，适用时核对源文件中的时序。对于已授权的操作，按预期结果和允许的变更范围核对最终状态。BenchCAD、Code2Video-AA 和 EnterpriseOps-Gym-AA 分别覆盖几何、渲染媒体和最终状态的检查。[BenchCAD 2.1](https://benchcad.com/blog/benchcad-2-1) · [Code2Video-AA](https://artificialanalysis.ai/methodology/intelligence-benchmarking#code2video-aa) · [EnterpriseOps-Gym-AA](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

在 OpenAI 的 BenchCAD 2.1 Core 测试中，Sol/High 为 64.0%、每题 $0.75，Sol/Xhigh 为 70.4%、每题 $1.00，Sol/Max 为 73.1%、每题 $1.60。这组结果可用于选择参数化 CAD 的对照组合。交付时仍要在成品中检查要求的几何和约束。[OpenAI 发布图](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [对照数据](benchmarks/task-tradeoffs-6.2.csv)

归档的 AA-PersonalityBench 数据缺少 Terra，Decision Index 和 HealthBench Professional 数据缺少 Sol 与 Astra。OpenAI 系统卡给出 HealthBench Professional 汇总成绩，缺少按推理档位匹配的得分和费用。[AA-PersonalityBench](https://artificialanalysis.ai/evaluations/aa-personalitybench) · [Decision Index](https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index) · [HealthBench Professional](https://artificialanalysis.ai/evaluations/healthbench) · [OpenAI 系统卡](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf#page=74)

要测量 v0.6.0 规则对首次分派、返工、用量和耗时的影响，需要在 Codex 中运行同任务对照。实际 Codex 工作流的总成本也尚未测量，其中包括主代理、工具、交接和返工。

## v0.5.0 评测基线

下文的例子和表格使用 2026 年 11 月 15 日的快照，其中 Sol 指 GPT-6.1 Sol，Astra 指 GPT-6 Astra，另两个模型为 GPT-6 Luna 和 GPT-6.1 Terra。共 15 个组合，覆盖 Medium、High、Xhigh 和 Max，排除 Luna/Max。[数据与复算程序](benchmarks/README.zh-CN.md)

### 参考依据

主要比较使用 [Artificial Analysis（AA）](https://artificialanalysis.ai/methodology/intelligence-benchmarking)：

| 任务依据 | 评测 |
| --- | --- |
| 仓库变更、终端工作与科学执行 | [FrontierCode-AA 2.0](https://artificialanalysis.ai/evaluations/frontiercode-2-0)、[Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)、[Terminal-Bench-Science](https://artificialanalysis.ai/evaluations/terminal-bench-science) |
| 有状态工具流程 | [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa)：严格通过、目标完成和防护规则违规分别保留 |
| 来源约束回答与长上下文推理 | [GDP.pdf](https://artificialanalysis.ai/evaluations/gdp-pdf)、[MLCR-AA](https://artificialanalysis.ai/evaluations/mlcr-aa)、[AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) |
| 困难知识、推理与物理求解 | [HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond)、[CritPt v2 及其困难子集](https://artificialanalysis.ai/evaluations/critpt-v2) |
| 专业产物与知识可靠性 | [Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase)、[Omniscience](https://artificialanalysis.ai/evaluations/omniscience) |

我们还用 [Vals Finance Agent](https://www.vals.ai/benchmarks/fabv2-1) 和 [Legal Research](https://www.vals.ai/benchmarks/legal_research)、CUA Speedrun 的 [OSWorld](https://cuaspeedrun.com/dataset-osworld-energy50-representative.html) 和 [OSWorld2](https://cuaspeedrun.com/dataset-osworld2-k52.html)、[DeepFinance](https://arxiv.org/pdf/2611.10926) 及 [Snorkel Terminal-Bench 排行榜](https://snorkel.ai/leaderboard/terminal-bench/)交叉检查任务覆盖与执行条件。这些来源并非对四个模型及所有推理档位的完整实验。发布方的任务、运行框架、计分、尝试次数和费用定义各不相同；不能跨评测平均分数，也不能把缺失或无效观察填成零。

另外，OpenAI 的[模型选择指南](https://developers.openai.com/api/docs/guides/model-selection)和 [Terra 发布说明](https://openai.com/index/introducing-gpt-6-1-terra/)提供厂商建议，包括 Terra 的自然写作和视觉优势。这些建议不是独立评测或独立复现。

### 如何比较质量与成本

在同一来源、同一任务内，保留原始单位比较质量收益、成本差或倍数及相关风险。[计算说明](benchmarks/README.zh-CN.md#计算的含义)解释 Pareto 前沿和有条件的 `价值 × 质量 − 成本` 比较。质量底线来自任务要求，而非候选的中位数或前半名。

### 如何选择 Balance 基准

Balance 按任务权衡得分提升与额外费用。下表数值来自 AA 快照。

| 任务／v0.5.0 Balance 组合 | 选择依据 |
| --- | --- |
| 普通代码／Terra/High | Terra/Medium→High 增加约 2.92 个评分百分点，费用约 1.52 倍；High→Max 再增加 4.86 点，费用约 3.30 倍。当时的预设将后面这段投入留给困难集成；来源没有分别测试这两个难度组。 |
| 完整文档回答／Sol/High | Terra/Medium→Sol/High 增加 3.6 个完整通过百分点，费用约 2.10 倍；Sol/High→Astra/Xhigh 只增加 0.2 点，费用约 5.47 倍。这支持相近回答共享 Sol/High，不代表所有文档推理。 |
| 端到端工具工作／Sol/Medium | Terminal-Bench 4.0 中，Sol/Medium 为 47.98%／$0.614，Terra/Xhigh 为 46.46%／$0.657。这是该运行框架下的点比较，不证明原生任务优胜。 |

困难代码中，Terra/Max→Astra/Max 约增加 **0.055 个评分百分点**，来源费用约 **5.06 倍**，该历史基线中高档共享 Terra/Max。这不证明两者等质，也不证明普通代码已经达到质量平台。

这些默认组合取决于评测结果、评测与任务的相似程度，以及各档对成本的偏好。选择时不使用拟合出的验收通过概率，也不为每个得分点设定固定的美元价值。任务和测试环境的差别都可能造成排序冲突，现有结果无法区分各自的影响。

### 如何延伸质量与成本偏好

Economy 在任务要求允许时接受部分质量余量损失，以降低成本。Quality 做常规实质判断时保留 Sol/High 或 Xhigh，愿为任务所需的质量提升多花费用。Extra Quality 愿为进一步提升质量支付更高的溢价。四档均保留任务本身的验收要求。

重证据综合体现了这种设计：在固定框架下重构时序或因果链、消解冲突记录并回答复合问题。MLCR 约束这一窄路线；长文档、需要引用或医疗标签本身不触发。

| 档位 | 组合 | MLCR 完整回答通过率 | 来源费用/任务 |
| --- | --- | ---: | ---: |
| Economy | Terra/Max | 30.56% | $0.06395 |
| Balance | Sol/Xhigh | 35.56% | $0.09374 |
| Quality | Sol/Max | 38.33% | $0.11193 |
| Extra Quality | Astra/Max | 41.67% | $0.57256 |

该快照中 Terra/Max 比 Sol/Medium 便宜，因此 Economy 也可能使用 Max。Sol/High→Sol/Max 增加 6.67 个通过百分点，来源费用约多 29%；Extra 相对 Sol/Max 再增加 3.33 点，费用约 5.12 倍，这是质量溢价，不是更高性价比。MLCR 只有 15 个候选中的 12 个对应观察，Terra/Medium、High 和 Xhigh 缺失；accuracy 分项不沿该序列单调提高，所以整体通过率上升不等于所有维度都改善。

AA-LCR 提供反向检查：Sol/Medium、High、Max 约为 83.33%、82.33%、83.00%，长上下文因此不能成为普遍使用 Max 的理由。重证据综合映射仍是政策选择，不是某个任务特征的因果实验结果。

这些点估计来自各项评测，不能证明唯一最优模型或差异具有统计显著性。AA 的加权 Cost per Task 汇总的是 AA 自身的任务组合。具体任务应看对应的比较，订阅额度则需要另有数据。

不同档位可以共享模型与推理档位组合。困难集成、依据文档给出完整答案，以及需要跟踪多个状态的工具流程，即使都涉及文件或代码，也可能需要不同选择。任务较长、涉及医疗或使用终端时，也应按实际工作分派。请结合质量要求和实际工作流成本检验默认选择。预设不规定固定的模型使用顺序或用量配额，也不要求先尝试较便宜的组合并等它失败。
