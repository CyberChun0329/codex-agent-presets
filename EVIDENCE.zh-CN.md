# 评测依据与预设设计

[English](EVIDENCE.md) · 依据读取日期：**2026 年 11 月 15 日**

四档预设表达不同的任务质量与成本偏好。考虑的模型为 GPT-6 Luna、GPT-6.1 Terra、GPT-6.1 Sol 和 GPT-6 Astra。根据剩余工作及验收要求选择模型和推理档位。

比较池包含这四个家族的 Medium、High、Xhigh、Max，排除 Luna/Max，共 15 个组合。Low 与非推理不在预设范围内；来源不一定提供每个组合的结果。

[评价模型、数据与复算](benchmarks/README.zh-CN.md)提供数值快照、费用输入、计算程序及四档取舍表。

## 参考依据

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

## 如何比较质量与成本

在同一来源、同一任务内，保留原始单位比较质量收益、成本差或倍数及相关风险。[计算说明](benchmarks/README.zh-CN.md#计算的含义)解释 Pareto 前沿和有条件的 `价值 × 质量 − 成本` 比较。质量底线来自任务要求，而非候选的中位数或前半名。

## 如何选择 Balance 基准

Balance 选择有依据的任务质量与成本折中，不直接选最便宜或质量/成本比最高的组合。以下例子说明默认背后的取舍，数值来自所参考的 AA 快照：

| 任务／Balance 组合 | 选择依据 |
| --- | --- |
| 普通代码／Terra/High | Terra/Medium→High 增加约 2.92 个评分百分点，费用约 1.52 倍；High→Max 再增加 4.86 点，费用约 3.30 倍。预设将后面这段投入留给困难集成；来源没有分别测试这两个难度组。 |
| 完整文档回答／Sol/High | Terra/Medium→Sol/High 增加 3.6 个完整通过百分点，费用约 2.10 倍；Sol/High→Astra/Xhigh 只增加 0.2 点，费用约 5.47 倍。这支持相近回答共享 Sol/High，不代表所有文档推理。 |
| 端到端工具工作／Sol/Medium | Terminal-Bench 4.0 中，Sol/Medium 为 47.98%／$0.614，Terra/Xhigh 为 46.46%／$0.657。这是该运行框架下的点比较，不证明原生任务优胜。 |

困难代码中，Terra/Max→Astra/Max 约增加 **0.055 个评分百分点**，来源费用约 **5.06 倍**，因此高档可以共享 Terra/Max。这不证明两者等质，也不证明普通代码已经达到质量平台。

这些基准选择结合来源观察、任务匹配与明确的资源偏好，并非由拟合出的接受概率或精确支付意愿参数唯一决定。任务和运行框架差异都可能造成排序冲突；此处没有隔离它们各自的影响。

## 如何延伸质量与成本偏好

Economy 在任务要求允许时接受部分质量余量损失，以降低成本。Quality 对常规实质判断保留 Sol/High 或 Xhigh，并愿为任务相关质量付费。Extra Quality 更愿为最后一段质量接受较大溢价。四档均保留任务本身的验收要求。

重证据综合体现了这种设计：在固定框架下重构时序或因果链、消解冲突记录并回答复合问题。MLCR 约束这一窄路线；长文档、需要引用或医疗标签本身不触发。

| 档位 | 组合 | MLCR 完整回答通过率 | 来源费用/任务 |
| --- | --- | ---: | ---: |
| Economy | Terra/Max | 30.56% | $0.06395 |
| Balance | Sol/Xhigh | 35.56% | $0.09374 |
| Quality | Sol/Max | 38.33% | $0.11193 |
| Extra Quality | Astra/Max | 41.67% | $0.57256 |

该快照中 Terra/Max 比 Sol/Medium 便宜，因此 Economy 也可能使用 Max。Sol/High→Sol/Max 增加 6.67 个通过百分点，来源费用约多 29%；Extra 相对 Sol/Max 再增加 3.33 点，费用约 5.12 倍，这是质量溢价，不是更高性价比。MLCR 只有 15 个候选中的 12 个对应观察，Terra/Medium、High 和 Xhigh 缺失；accuracy 分项不沿该序列单调提高，所以整体通过率上升不等于所有维度都改善。

AA-LCR 提供反向检查：Sol/Medium、High、Max 约为 83.33%、82.33%、83.00%，长上下文因此不能成为普遍使用 Max 的理由。重证据综合映射仍是政策选择，不是某个任务特征的因果实验结果。

这些来源点估计不能证明唯一最优模型或差异具有统计显著性，也不是 Codex 原生实测。AA 加权 Cost per Task 可作为其自身任务组合的费用背景，不能替代各任务比较或预测订阅额度。完整工作流费用还包括主 agent、工具、交接和必要返工；此处尚未测量原生总成本。

不同档位可以共享模型与推理档位组合。困难集成、基于文档的完整回答和多状态工具流程，即使都涉及文件或代码，也可能需要不同选择；仅凭任务长度、医疗标签或使用终端不能确定路线。请结合自己的质量要求与实际工作流成本检验默认选择。预设不规定固定模型梯子、使用比例，也不要求先尝试较便宜的组合并等它失败。
