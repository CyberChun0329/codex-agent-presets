# 评测依据与预设设计

[English](EVIDENCE.md)

## 为什么换用 GPT-6.2

四档预设中的 Sol 和 Astra 均使用 GPT-6.2。在 OpenAI 的 FrontierCode 2.0 测试中，Sol/Max 与 Astra/Max 的得分相差不超过 0.5 分，前者的成本约为后者的五分之一。在 Terminal-Bench-Science 0.1 上，新版 Astra 比上一代高 9 个百分点，每题成本低于上一代的三分之一。在 GDPval v2 上，新版 Sol 比上一代高 5.3 个百分点。[OpenAI 发布评测](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [发布对照数据](benchmarks/gpt-6.2-launch.csv)

输入量不超过 272,000 token 时，按标准 API 费率，每百万输入、缓存命中输入和输出 token，GPT-6.2 Sol 分别为 2、0.10、10 美元，GPT-6.2 Astra 分别为 8、0.40、40 美元。实际任务成本还取决于 token 用量。[OpenAI 定价](https://developers.openai.com/api/docs/pricing#latest-models)

### 怎样从 Balance 确定其他档位

每类任务先选 Balance，衡量多花的钱能换来多少质量，以及错误会造成多少返工。Economy 更重视成本，Quality 和 Extra Quality 依次更愿意为有依据的质量收益付费。有些任务适合共用一个组合，例如 Economy 和 Balance 的固定答案难问答。

| 任务 | 选择依据 |
| --- | --- |
| 按既定规则操作并跟踪状态 | 在 AA AutomationBench 上，Terra/Xhigh 的严格通过率为 32.88%，每题违规 0.677 次。Balance 所选的 Sol/Medium 通过率为 41.40%，每题违规 0.397 次。在 OpenAI 的测试中，Sol/Medium 得分为 40.2%，每题 $0.18，Sol/High 为 41.2%，每题 $0.21。 |
| 需要探索环境、按反馈调整的工具任务 | Balance 选 Sol/High。LifeVal 上，High 为 80.8%、每题 $0.65，Medium 为 70.3%、每题 $0.38。BenchCAD 上，同样的升级让得分从 41.2% 升至 64.0%，每题费用从 $0.29 升至 $0.75。Economy 保留 Terra/Medium，如果走错一步会导致后续步骤重做，可直接选 Terra/High。 |
| 科学计算 | 在 AA 科学终端上，Terra/Xhigh 为 41.90%、每题 $1.04，Sol/Medium 为 60.48%。按标准短上下文费率，假设可缓存输入的命中率为 95%，后者估算每题 $1.39。Balance 选 Sol/Medium，数值误差或稳定性决定验收时选 Sol/High。对于方法已定、有独立测试可验收的小型科学代码，Economy 可选 Luna/Xhigh。在 SciCode 上，Luna/Xhigh 和 Terra/Medium 的子题得分率分别为 51.74% 和 51.62%。按 AA 客户端公式复算，每题费用分别为 $0.00144 和 $0.00518。 |
| 答案固定的困难问答 | 在 AA HLE-Diamond 上，Terra/Medium 的准确率为 31.3%，每题 $0.00896。Sol/Medium 的准确率为 50.7%，估算每题 $0.01872。即使是 Economy，这段准确率提升也值得每题多花约一美分。Economy 和 Balance 在准确率要求更高时都可选 Sol/High（58.3%，估算每题 $0.04219）。 |
| 困难代码集成 | Extra Quality 选 Astra/Xhigh，Quality 选 Sol/Max。在 AA FrontierCode 上，两者分别拿到 48.95% 和 44.38% 的评分点，每题分别为 $3.75 和 $1.30。OpenAI FrontierCode 测得的差距较小（44.1% 对 43.8%）。在 PatchBench 上，Astra/Xhigh 和 Astra/Max 同为 79.7%，每题分别为 $2.45 和 $4.18。 |
| 重证据综合 | 需要完整回答复合问题时，Extra Quality 选 Astra/Max。在 AA MLCR 上，其整体通过率为 39.44%，Sol/Max 为 37.22%。该评测要求答案完整且无矛盾才算通过。事实准确性分项上，Sol/Max 为 98.89%，Astra/Max 为 96.67%。验收更重视事实准确性时可选 Sol/Max。 |

上表标为估算的 Sol/Medium、Sol/High 费用均未由 AA 报告。补充数据表列有计算所用的 token 数和价格假设。每组比较使用同一评测条件下的点估计。实际 Codex 工作流的返工量和总成本尚未测量。[评测结果](benchmarks/quality-6.2.csv) · [补充结果与费用估算](benchmarks/task-tradeoffs-6.2.csv)

### Quality 的四类任务怎么分

每组对比使用同一次评测的得分和每题美元成本。Artificial Analysis（AA）与 OpenAI 的测试环境不同。表中得分是点估计，费用是评测任务的费用。[各模型和推理档位的得分与成本](benchmarks/quality-6.2.csv)

| 任务 | Quality 默认组合 | 选择依据与例外 |
| --- | --- | --- |
| 困难代码集成 | Sol/Max | 在 AA FrontierCode 2.0 上，Sol/Max 拿到 44.38% 的评分点，每题 $1.2978。Terra/Max 为 42.32%，每题 $1.2925。普通代码实现继续用 Terra/High。 |
| 科学计算与验证 | Sol/High | 在 AA Terminal-Bench-Science 上，Terra/Max 得分为 57.62%，Sol/High 为 67.62%。AA 缺少 Sol/High 的每题成本。在 OpenAI 的测试中，Sol/High 为 67.7%、每题 $1.51，Sol/Max 为 68.0%、每题 $2.21。如果任务值得为准确率支付更多，可以选 Astra/High（74.9%、每题 $5.20）。 |
| 答案固定的困难问答 | Astra/High | 在 AA HLE-Diamond 的 1,000 道题上，Astra/High 答对 65.9%，每题 $0.14656。Sol/Max 答对 64.0%，每题 $0.14888。需要更高准确率时可选 Astra/Xhigh（67.3%、每题 $0.23407）。 |
| 按既定规则操作、需要跟踪状态的多步工具任务 | Sol/High | 在 OpenAI 的 AutomationBench 上，High 的得分为 41.2%，每题 $0.21，Xhigh 为 40.6%，每题 $0.23。AA 测得 Xhigh 的严格通过率略高，但 High 每题违规次数略少。若一次违反权限或状态约束就会让结果失效，可选 Astra/High。需要探索环境、按反馈调整操作的端到端任务继续用 Sol/Xhigh。 |

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

Balance 选择有依据的任务质量与成本折中，不直接选最便宜或质量/成本比最高的组合。以下例子说明默认背后的取舍，数值来自所参考的 AA 快照：

| 任务／v0.5.0 Balance 组合 | 选择依据 |
| --- | --- |
| 普通代码／Terra/High | Terra/Medium→High 增加约 2.92 个评分百分点，费用约 1.52 倍；High→Max 再增加 4.86 点，费用约 3.30 倍。当时的预设将后面这段投入留给困难集成；来源没有分别测试这两个难度组。 |
| 完整文档回答／Sol/High | Terra/Medium→Sol/High 增加 3.6 个完整通过百分点，费用约 2.10 倍；Sol/High→Astra/Xhigh 只增加 0.2 点，费用约 5.47 倍。这支持相近回答共享 Sol/High，不代表所有文档推理。 |
| 端到端工具工作／Sol/Medium | Terminal-Bench 4.0 中，Sol/Medium 为 47.98%／$0.614，Terra/Xhigh 为 46.46%／$0.657。这是该运行框架下的点比较，不证明原生任务优胜。 |

困难代码中，Terra/Max→Astra/Max 约增加 **0.055 个评分百分点**，来源费用约 **5.06 倍**，该历史基线中高档共享 Terra/Max。这不证明两者等质，也不证明普通代码已经达到质量平台。

这些基准选择结合来源观察、任务匹配与明确的资源偏好，并非由拟合出的接受概率或精确支付意愿参数唯一决定。任务和运行框架差异都可能造成排序冲突；此处没有隔离它们各自的影响。

### 如何延伸质量与成本偏好

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
