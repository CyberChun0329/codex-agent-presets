# 模型选型依据

[English](EVIDENCE.md) · **外部评测：2026-11-03** · **本地对比：2026-11-06**

Luna 指 GPT-6 Luna，Terra／Sol 指 GPT-6.1 Terra／Sol，Astra 指 GPT-6 Astra。

## Artificial Analysis

以下比较采用 Intelligence Index v5.0。百分比按网页显示值取整，来源未提供置信区间。
“综合任务成本”是该指数的加权平均任务成本，不是单项测试价格，也不能换算成 Codex 额度。

| 模型与推理档位 | 主要结果，按左／右顺序 | 综合任务成本 |
| --- | --- | --- |
| [Terra Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-terra-xhigh) | Terminal-Bench 4.0：56%／46%；科学计算：58%／42%；自动化：60%／60% | $0.96／$0.40 |
| [Sol Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-1-sol-xhigh) | 科学计算：58%／50%；Terminal-Bench 4.0：56%／54%；自动化：65%／67%；GDP.pdf：31%／32% | $1.27／$0.76 |
| [Terra High／Sol Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-high-vs-gpt-6-1-sol-medium) | Terminal-Bench 4.0：42%／48%；FrontierCode 2.0：37%／33% | $0.26／$0.36 |
| [Terra Max／Sol High](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-sol-high) | Terminal-Bench 4.0：56%／52%；科学计算：58%／46%；Briefcase v1.1 Elo：1402／1467；Omniscience v1.1 净分：30／41；GDP.pdf：29%／32% | $0.96／$0.59 |
| [Luna Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-luna-xhigh) | Terminal-Bench 4.0：13%／8%；科学计算：9%／5%；自动化：53%／48% | $0.15／$0.10 |

表中科学计算为 Terminal-Bench-Science 0.1，自动化为 AutomationBench-AA。

这些结果支持 Balance 按任务使用 Max：Terra 可用于合适的终端或科学计算任务；Sol
用于需要更深入推理的工作；Luna 则需要明确范围和有效检查。它们不支持统一提高推理
档位，提高小模型的推理档位也不一定能替代更强的模型。

Terra High／Sol Medium 的首个回答 token 时间分别为 20.82／9.35 秒，整项任务耗时为 171.39／217.80 秒；这是当时的快照。较低 token 价格或更快的首次输出不能确定总成本或完成时间，Economy 不保证任务完成得最快。

## 原始测试榜单

- [Terminal-Bench 4.0](https://snorkel.ai/leaderboard/terminal-bench/)：66 个任务，
  Harbor、固定 `terminal-bench@4.0.0` 数据集、Codex、Max。解决率为 Sol
  **58.2% ±3.1**、Astra **58.2% ±2.8**、Luna **16.4% ±2.7**；所查页面没有 Terra。
  成本和 token 数统计整套测试，运行方式与上面的 AA 比较不同。
- [ALE v1.1](https://snorkel.ai/leaderboard/agents-last-exam/)：122 个任务、55 个子行业。
  Terra/Max、Codex 的通过率为 **41.8%**，得分为 **69.8%**，总耗时 **124h36m**、输出 **5.5M token**。通过率要求完整完成，
  得分包含部分完成。

## OpenAI 数据与建议

[官方 ALE v1 图表](https://openai.com/index/introducing-gpt-6-1-terra/)中，Luna/Max 为
**50.9%、$0.14/任务**，Terra/Low 为 **55.9%、$0.16/任务**；Terra/Medium 为
**57.6%、$0.29/任务**，Terra/Max 为 **60.0%、$1.01/任务**。这支持比较不同模型的
推理档位，也是 Balance、Economy 允许较低档位的依据。v1 得分与 v1.1 通过率应分别比较。

[OpenAI 建议](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-61-terra)
将 Terra 用于自然写作、视觉推理和精确的电脑操作。Briefcase 衡量完整工作成果，不能单独证明文风优势。

## 本地固定标准文稿对比 — 2026-11-06

Terra/High 与 Sol/High 使用相同事实和标准，分别修订同一组英文、中文技术说明；两组首稿均达到要求，无需返工。两种模型还各审阅了同一组七段短篇技术文字。

| 任务／模型，均为 High | 任务耗时 | 未缓存输入 token | 缓存输入 token | 输出 token |
| --- | ---: | ---: | ---: | ---: |
| 两段修订／Terra | 38.7 s | 31,763 | 89,088 | 1,069 |
| 两段修订／Sol | 44.0 s | 31,864 | 89,472 | 1,163 |
| 七段审阅／Terra | 31.8 s | 18,195 | 71,296 | 841 |
| 七段审阅／Sol | 44.4 s | 18,217 | 100,480 | 1,333 |

Terra/High 在这次小样本中耗时更短、输出 token 更少。任务耗时包含检查、等待和工具调用，不代表完整工作流耗时。缓存输入属于输入，输出已包含推理 token。

## 如何应用

| 档位 | 固定标准修订与基于所给材料的审阅 |
| --- | --- |
| Economy | 优先 Terra：范围明确且可有效检查的工作用 Low／Medium，正常推理用 High，条件相互牵连时用 Xhigh；模型池限于 Luna／Terra。 |
| Balance | 优先 Terra，按任务选择推理档位；实质歧义、架构或方法选择及证据综合使用 Sol。 |
| Quality 和 Extra Quality | 通常从 Terra/High 开始；实质歧义或相互牵连的概念决策使用 Sol。审阅者身份本身不要求 Sol。 |

本地对比只覆盖 High 与短篇技术文稿，不能推广到 Low／Medium 或长篇文稿。现有数据未评估四档完整配置、Ultra 主模型表现或 Codex 订阅用量。
