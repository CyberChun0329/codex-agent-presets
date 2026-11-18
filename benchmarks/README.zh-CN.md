# 评价模型、数据与复算

[English](README.md)

## GPT-6.2 数据 · 2026 年 11 月 18 日

| 表格 | 内容 |
| --- | --- |
| [发布对照](gpt-6.2-launch.csv) | OpenAI 发布时公布的五项对比 |
| [得分与任务费用](quality-6.2.csv) | OpenAI 和 Artificial Analysis 按模型与推理档位给出的评测结果 |
| [补充任务对照](task-tradeoffs-6.2.csv) | 工具任务、证据综合、读图提取和专业交付，包括规则解读与定量分析 |
| [前端评测](frontend.csv) | AA-3D 总分、分场景得分和费用输入，以及 Vals Web 应用功能测试的成绩与费用 |

前端数据保留各来源的计量单位和测试设置。AA-3D 的 `opponent_balanced_vote_share_pct` 将对每个对手的胜率等权平均。分场景数据没有对应费用。复算 AA-3D 总体费用时，以可缓存输入乘命中率计算缓存命中量，命中部分按读取费率计费，其余输入按写入费率计费，答案和推理 token 按输出费率计费。总额除以 `task_count` 和一百万。Vals 行保留实际推理档位与来源报告的费用。Luna/Max 供比较，四档预设均不派发该组合。[前端分工依据](../EVIDENCE.zh-CN.md#前端设计与实现)

## 查看或复算

v0.5.0 基线取自 2026 年 11 月 15 日，其中 Sol 和 Astra 分别指 GPT-6.1 Sol 和 GPT-6 Astra。

| 文件 | 内容 |
| --- | --- |
| [observations.csv](data/observations.csv) | 15 个模型与推理组合、44 个 AA 指标视图，共 660 行，保留缺失和排除项 |
| [cost-inputs.csv](data/cost-inputs.csv) | 用于核算费用估计的来源令牌量、价格、缓存假设及任务分母 |
| [components.csv](data/components.csv) | Automation、Omniscience、Briefcase、MLCR 分项，保留质量与风险的冲突 |
| [sources.json](data/sources.json) | 来源链接、快照时间与哈希、单位和解释边界 |
| [presets.json](presets.json) | v0.5.0 的 68 项默认及八类具体任务对应的主要来源 |
| [evaluate.py](evaluate.py) | 只依赖 Python 标准库的离线计算程序 |
| [comparisons.csv](results/comparisons.csv) | 13 个所选指标视图的 195 行比较：观察点的 Pareto 状态与条件偏好区间 |
| [profile-tradeoffs.csv](results/profile-tradeoffs.csv) | 八类具体任务在四档间的质量差、费用溢价及相关分项 |

在仓库根目录运行：

```sh
python3 benchmarks/evaluate.py --output-dir /tmp/codex-preset-analysis
```

程序复算公开结果表，并核对所有已提供的来源费用是否与令牌、价格输入一致。程序离线运行，不调用模型或修改 Codex 配置。[summary.json](results/summary.json)记录输入哈希与覆盖情况，[cost-checks.csv](results/cost-checks.csv)记录 338 个已复算费用和 322 个未知费用。

数值快照来自 AA。Vals、CUA Speedrun、DeepFinance、Snorkel 和厂商建议分别用于任务覆盖及迁移检查，见[评测依据与预设设计](../EVIDENCE.zh-CN.md)，不把它们的成绩混入这些表。44 个视图包含共享运行和派生指标，不是 44 次独立实验。没有对应评测的一般任务默认，在 `presets.json` 中保留空来源。

## 补充任务对照

[补充表](task-tradeoffs-6.2.csv)收录 OpenAI 的 LifeVal、BenchCAD 和 PatchBench 成绩，以及 AA 的 MLCR 准确性和整体通过率、MMMU-Pro、Briefcase 总体及各文件类型的评分项通过率。直接取自 AA 的分数用比例，OpenAI 图表中的分数用百分数。来源给出的任务费用、按 AA 客户端公式复算的费用和假设缓存命中率后估算的费用各列一栏。AutomationBench 严格通过率对应整次运行的每题费用。Briefcase 文件类型分组统计通过的评分项比例，费用留空。SciCode 等对照见 [Quality 数据表](quality-6.2.csv)。

Harvey LAB-AA v1.1 和 AA-AnalystAgent 各收录八行，覆盖 GPT-6.2 Sol 和 Astra 从 Medium 到 Max 的四个档位。Harvey 采用 OpenAI 发布图转引的 AA 评测得分和费用，作为同一组证据计算一次。AnalystAgent 的 `pass_power_5_all_attempts` 是 80 道题中五次尝试均答对的比例。单次尝试与五次合计的费用口径尚未对齐，费用留空。新增行均提供来源链接、字段位置和快照 SHA-256。[OpenAI 发布图](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [Harvey LAB-AA](https://artificialanalysis.ai/evaluations/harvey-lab-aa) · [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent)

复算 Sol 的估算费用时，取每行的输入（`I`）、回答（`A`）、推理（`R`）、可缓存输入（`C`）token 总数及任务数 `N`。按 AA 客户端的计价方式，可缓存输入中的命中比例为 `h` 时，每题美元费用为

```text
(C*h*0.10 + (I-C*h)*2.50 + (A+R)*10) / (1,000,000*N)
```

最低费用、95% 命中和最高费用分别取 `h` 为 1、0.95 和 0。来源缺少 `C` 时使用 `(I*2 + (A+R)*10) / (1,000,000*N)`，因此 HLE-Diamond 的三种估算相同。价格取自 2026 年 11 月 18 日的 OpenAI Standard 短上下文价目，每百万 token 计价，缓存写入按 30 分钟计算。实际命中率和上下文长度都会影响每题成本。[API 价目](https://developers.openai.com/api/docs/pricing#latest-models) · [AA 客户端](https://artificialanalysis.ai/_next/static/chunks/17016-9e1b20384a9bc1ed.js)

## Quality 6.2 面板

[quality-6.2.csv](quality-6.2.csv)保留 AA 的 FrontierCode 2.0、TerminalBench 4.0、SciCode、Terminal-Bench Science、HLE-Diamond、AutomationBench 严格通过率，以及 OpenAI 发布图中 FrontierCode 2.0、Terminal-Bench Science 和 AutomationBench 的完整采集候选行。AA 每题违规次数是越低越好的独立风险指标，不作为质量最大化目标。SciCode 未采集到 6.2 的质量或费用，旧模型数据不能证明 6.2 的比较。

每行保留来源、指标、原始单位、模型档位和直接来源链接；AA 的 JSON 指针和来源快照 SHA-256 标识具体字段，OpenAI 数据提取自发布页的 Vega-Lite 图表。AA 的比例与 OpenAI 的百分数口径和运行条件各自保留，不合并比较。`usd_per_task` 是来源报告的任务费用或 `cost_basis` 标明的 AA 客户端重算值，不是 Codex 账单。`cost_scope` 区分严格通过率和风险指标所附的同次运行通用 AutomationBench 费用与面板费用。空值表示未知，不是零；允许参与不代表已测量。Low、非推理及 Luna/Max 保留数据但按 Quality 策略排除，违规指标也不作为质量指标。

按[英文说明中的命令](README.md#quality-62-panels)可逐面板复核记录的 Pareto 前沿和条件偏好区间。计算只纳入同来源、条件、指标和单位下，质量与费用均已知且符合策略的候选。比较候选组合时，还须结合风险、任务要求和点估计的不确定性；前沿及区间本身不决定分工，未观察或未定价候选可能改变结果。

## 计算的含义

在同一来源、同一指标内，以 `q_i` 表示候选 `i` 的来源质量分，以 `c_i` 表示每个来源任务的美元费用估计。保留原单位：部分分数是比例，Elo 和净分则不是。质量指标有明确产出单位、且目标是单位预算产出时，质量除以成本才有用途；Elo 和净分不除以价格。不能跨评测平均分数或质量/费用比。

- **观察集 Pareto 前沿：**不存在一个已观察候选，质量不低、费用不高，且至少一项严格更好。
- **条件偏好：**`U_i(v) = v × q_i − c_i`，其中 `v ≥ 0` 是假设的“每一来源评分单位值多少美元”。程序对全部可用观察计算各候选使该式最大时的区间。端点包含并列；受支持点的上界为空表示无上界。这是偏好区间，不是置信区间。
- **任务取舍：**查看已选默认之间的质量差、费用差及倍数，同时保留风险和分项冲突。已经惩罚错误的分数，不额外叠加任意幻觉罚分。

Pareto 点不一定被线性目标选中，但仍可能适合硬预算或质量约束。缺质量或费用不等于零，排除不证明不适用，未观察候选也可能改变前沿。公开程序用精确分数计算偏好区间。

## 从比较到默认

先把剩余工作和验收要求对应到相关证据，再比较可用候选的质量收益、费用溢价和风险冲突。质量底线来自任务要求；候选中位数或榜单前半名都不能证明底线。单凭评测成绩，也不能证明某个候选满足你的实际任务。

Balance 根据这些比较选择有竞争力的质量与费用折中。Economy 在要求允许时减少质量余量；Quality 和 Extra Quality 接受更高的任务相关溢价。四档没有拟合出的通用 `v`，不自动选择质量/费用比最大者，也不要求每档都换一个组合。[设计说明](../EVIDENCE.zh-CN.md#如何选择-balance-基准)提供 Balance 的具体选择及重证据综合的四档例子。

32 行分支数据是对已给定默认的计算比较。开放判断、写作及一般默认还参考任务结构和厂商建议。原生应用质量、返工、交接费用和订阅用量尚未测量。

## 费用单位与排除项

来源价格为美元/百万令牌。费用估计为输入费用与回答、推理输出费用之和，除以一百万和来源客户端的任务分母。可缓存输入按来源命中率计算缓存读取，使用缓存读取价；剩余输入使用缓存写入价。缓存价格缺失时，按来源客户端规则退回普通输入价。必要输入缺失则保持未知。这些是来源的计费假设，不是 Codex 实际账单。

HealthBench 的版本与字段绑定尚未解决，因此不纳入质量与费用分析；AnalystAgent 的五次全对分数没有已确认对应的整组费用；CritPt Hard 保留独立令牌字段和任务分母。MLCR 缺失的 Terra 档位及不单调的 accuracy 分项仍可见。
