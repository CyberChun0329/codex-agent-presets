# 行业证据与派发

[English](INDUSTRY.md)

先按决定验收的工作选中现有分工。需要行业判断，或存在该行业特有的关键错误时，再用行业证据选择模型和推理档位。混合项目中，能独立验收的工作可以分别交付；相互依赖的判断由一个负责人贯通，再把已确认的结果交给下游。

## 先定 Balance

1. **四档共用验收要求。** 把会使交付失效的错误单独检查。费用或关键错误缺测时，保留这个缺口。
2. **比较同口径数据。** 优先使用与任务相近、且模型、推理档、运行条件、分数和费用相匹配的评测。把验收相关的错误、质量和成本一起比较。有复核和返工费用时，合计到总成本。公开评测通常只覆盖执行成本。
3. **在已测组合中比较。** 有平均预算时，在预算内选质量最高的，同分取价格较低的。有质量目标时，选满足目标的最低成本组合。两者都未定时，列出各组合领先的预算区间。预设给出常见任务的建议默认。成本或出错代价不同的任务可按条件换档。 [复算预算区间](benchmarks/README.zh-CN.md#比较-v070-的默认组合)
4. **从 Balance 延伸。** Economy 在能达到同一验收要求时少花钱。Quality 和 Extra Quality 愿意为任务上重要的质量多付费。继续升档如果缺乏收益证据，或带来新的关键错误，两档可以选择同一个组合。

AA 行业指数给出一组任务的加权得分和费用。用权重和分项检查是否覆盖关键工作、筛选候选；加权费用可用于同一指数内的组合比较。实际派发优先看与交付最相近的分项或专项评测。总分与其分项共享证据。 [AA 方法](https://artificialanalysis.ai/methodology/capability-indexes) · [六项得分与加权成本](benchmarks/aa-capability-indexes.csv) · [32 项组成权重](benchmarks/aa-capability-weights.csv)

## 六个行业怎样接进现有决策树

| 行业 | 什么工作决定验收 | 证据与选择 |
| --- | --- | --- |
| 金融与会计 | 按指定流程对账走规定工作。需要判断差异和口径走定量分析。既定框架下、需要独立推理的可核验建模答案，可走困难固定问答。需要交付可编辑工作簿，且要核对公式和情景如何联动时，走受约束模型构建。估值假设未定时走设计。 | Vals Finance Agent 的一般定量分析中，Sol/Max 为 **79.94%／$1.43**，优于 Astra/Max 的 78.08%／$5.50。金融建模中，Astra/Max 为 **50.74%／$6.07**，高于 Sol/Max 的 39.65%／$1.54。建模分项缺低档对照，AA-AnalystAgent 则覆盖多个领域。沿用现有分工，按实际分析任务选候选。 [Vals](https://www.vals.ai/benchmarks/fabv2-1) · [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent) |
| 战略与运营 | 固定步骤走规定工作。依赖实时权限和状态走有状态工具。要随反馈规划交付走端到端工具。流程和考核规则未定时走设计。 | AutomationBench 上 Sol/Medium→High，运营的违规从 **30 降到 23 次／100 题**，财务则从 **47 升到 52 次／120 题**，分项缺对应费用。EnterpriseOps 全榜最终状态测试支持继续比较同一行的 Medium 与 High。现有默认保留。 [AutomationBench](https://artificialanalysis.ai/evaluations/automationbench-aa) · [EnterpriseOps](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |
| 法律 | 直接引用明文走查找或文档问答。具体结论依赖相互影响的规则、例外和关键事实时，走个案规则适用。重建案情控制验收时走重证据综合。制定新的规则走设计。 | Harvey LAB-AA 测完整法律交付，并检查对给定案情记录的忠实性。任务依赖外部判例、法规或法律教义时，仍要单独核查这些依据。 [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa) · [评分方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking#harvey-lab-aa-v11) |
| 医疗健康 | 汇总病历明示事实走文档问答。消解矛盾记录、重建关键时间线走重证据综合。其他专业判断按实际证据与科学任务派发。 | MLCR-AA 的准确和完整是两项指标，支持现有病历综合路线。原版 HealthBench 是一般健康对话。HealthBench Professional 的 6.2 汇总结果缺匹配推理档和任务成本，现有默认保留。 [MLCR-AA](https://artificialanalysis.ai/evaluations/mlcr-aa) · [HealthBench](https://artificialanalysis.ai/evaluations/healthbench) |
| 工程 | 软件行为已定时走实现或集成；数值有效性决定验收时走科学计算。规格明确且须核对修改后的几何或装配约束时，走受约束模型构建。待定需求、公差或方法走设计。 | BenchCAD Core 的 Codex 成绩可参考这类 CAD 任务。以原生文件中的几何、约束和可编辑性验收。保留 CritPt 对有固定答案的工具辅助研究级物理问题的现有例外。 [BenchCAD](https://benchcad.com/blog/benchcad-2-1) · [CritPt](https://artificialanalysis.ai/evaluations/critpt-v2) |
| 经济学 | 比较研究及其识别假设走证据判断。估计方法已定、数值有效性决定验收时走科学计算。选择识别策略、变量或观测方式走设计。 | AA 经济学指数混合知识、端到端知识工作、推理和长文本。缺独立的计量执行与因果识别分档成本对照，因此保留现有默认。 [AA 经济学指数](https://artificialanalysis.ai/indexes/economics) |

## 两类任务与组合

**个案规则适用**交付的是具体结论，结果取决于既有规则如何相互作用以及哪些关键事实成立。例如判断过渡条款是否会改变一项申请适用的要求。按完整决策表判定走规定操作，解释条款含义走规则解释，重建有争议的申请时间线走重证据综合，制定新条款走设计。

**受约束模型构建**要求按已定规格制作或修改可编辑模型，并验证关联元素在变化后仍满足要求。例如修改参数化装配或搭建情景联动工作簿。若编辑或运行步骤及检查已完全给定，走规定操作。主要工作在于选择工具或组织文件时，走端到端工具。验收取决于软件行为时走代码集成，取决于数值有效性时走科学计算。

有相近任务证据时，使用下表组合。证据不足时，分别从通用规则解释或端到端工具的组合起步。下方评测只支持与各自任务可比的选型。

| 任务 | Economy | Balance | Quality | Extra Quality |
| --- | --- | --- | --- | --- |
| 个案规则适用 | Sol/High | Sol/Max | Sol/Max | Astra/High |
| 受约束模型构建 | Terra/Medium | Sol/Xhigh | Sol/Max | Astra/Xhigh |

**法律案例。** Harvey 的 Sol/Max 全项通过分数为 **11.1%／$1.92**，Sol/High 为 **5.8%／$1.03**。每个已检查任务的实质性记录错误从 High 的 **0.025 次**升至 Max 的 **0.050 次**。Balance 重视覆盖度时用 Max。优先避免与案情记录相悖的实质性错误，且后续能核对关键争点的覆盖时，用 High。Economy 从 High 开始。Quality 可在额外覆盖与更少记录错误值得付费时选 Astra/High。Extra Quality 默认 Astra/High，得分 **13.3%／$3.86**。Astra/Max 达 **15.0%／$6.35**，实质性记录错误为 **0.058 次**，高于 Astra/High 的 **0.033 次**。交付时核对相关法源和决定结论的事实。 [法律分档数据](benchmarks/task-tradeoffs-6.2.csv)

**CAD 建模案例。** 同场 BenchCAD 中，Sol/High、Xhigh、Max 分数为 **64.0、70.4、73.1**，每例 **$0.75、$1.00、$1.60**。Balance 默认花 **$0.25** 多拿 **6.4 分**。局部迭代修改可以在下游工作前用原生工具验证且有省费需求时，选 High。Quality 为下一段 **2.7 分**付费。Extra Quality 默认 Astra/Xhigh，得分 **77.6／$3.36**。若修正几何会牵连后续装配，用户优先追求质量且预算允许，可选 **82.5／$5.43** 的 Astra/Max。Economy 沿用工具任务的 Terra/Medium 起点。BenchCAD 缺少 Terra 的匹配结果。实际验收以可编辑模型中的几何和约束为准。 [BenchCAD 分档数据](benchmarks/task-tradeoffs-6.2.csv)
