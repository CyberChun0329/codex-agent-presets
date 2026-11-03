# 模型选型依据

[English](EVIDENCE.md) · **2026-11-03 复核** · 采用 **2026-10-26** GPT-6.1 Terra 发布后的模型组合

Luna 指 GPT-6 Luna，Terra／Sol 指 GPT-6.1 Terra／Sol，Astra 指 GPT-6 Astra。

## Artificial Analysis

以下比较采用 Intelligence Index v5.0。百分比按网页显示值取整，来源未提供置信区间。
“综合任务成本”是该指数的加权平均任务成本，不是单项测试价格，也不能换算成 Codex 额度。

| 模型与推理档位 | 主要结果，按左／右顺序 | 综合任务成本 |
| --- | --- | --- |
| [Terra Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-terra-xhigh) | Terminal-Bench 4.0：56%／46%；科学计算：58%／42%；自动化：60%／60% | $0.96／$0.40 |
| [Sol Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-1-sol-xhigh) | 科学计算：58%／50%；Terminal-Bench 4.0：56%／54%；自动化：65%／67%；GDP.pdf：31%／32% | $1.27／$0.76 |
| [Terra High／Sol Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-high-vs-gpt-6-1-sol-medium) | Terminal-Bench 4.0：42%／48%；FrontierCode 2.0：37%／33% | $0.26／$0.36 |
| [Terra Max／Sol High](https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-vs-gpt-6-1-sol-high) | 科学计算：58%／46%；Briefcase v1.1 Elo：1402／1467；GDP.pdf：29%／32% | $0.96／$0.59 |
| [Luna Max／Xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-luna-xhigh) | Terminal-Bench 4.0：13%／8%；科学计算：9%／5%；自动化：53%／48% | $0.15／$0.10 |

表中科学计算为 Terminal-Bench-Science 0.1，自动化为 AutomationBench-AA。

这些结果支持 Balance 按任务使用 Max：Terra 可用于合适的终端或科学计算任务；Sol
用于需要更深入推理的工作；Luna 则需要明确范围和有效检查。它们不支持统一提高推理
档位，提高小模型的推理档位也不一定能替代更强的模型。

完整指标和时间比较见英文页。Economy 不保证任务完成得最快。

## 原始测试榜单

- [Terminal-Bench 4.0](https://snorkel.ai/leaderboard/terminal-bench/)：66 个任务，
  Harbor、固定 `terminal-bench@4.0.0` 数据集、Codex、Max。解决率为 Sol
  **58.2% ±3.1**、Astra **58.2% ±2.8**、Luna **16.4% ±2.7**；所查页面没有 Terra。
  成本和 token 数统计整套测试，运行方式与上面的 AA 比较不同。
- [ALE v1.1](https://snorkel.ai/leaderboard/agents-last-exam/)：122 个任务、55 个子行业。
  Terra/Max、Codex 的通过率为 **41.8%**，得分为 **69.8%**。通过率要求完整完成，
  得分包含部分完成。

## OpenAI 数据与建议

[官方 ALE v1 图表](https://openai.com/index/introducing-gpt-6-1-terra/)中，Luna/Max 为
**50.9%、$0.14/任务**，Terra/Low 为 **55.9%、$0.16/任务**；Terra/Medium 为
**57.6%、$0.29/任务**，Terra/Max 为 **60.0%、$1.01/任务**。这支持比较不同模型的
推理档位，也是 Balance、Economy 允许较低档位的依据。v1 得分与 v1.1 通过率应分别比较。

[OpenAI 建议](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-61-terra)
将 Terra 用于自然写作、视觉推理和精确的电脑操作，因此各档都保留这些用途。本次评估
未找到控制当前模型版本和推理档位的独立写作／视觉比较。Briefcase 衡量工作成果，不能单独证明文风优势。

## 这些数据能说明什么

Extra Quality 不使用 Luna、Economy 不使用 Max，都是对可用模型和推理档位的选择。
目前没有四档完整配置、Ultra 主模型表现或 Codex 订阅用量的对照测试。README 中的
订阅选档表是使用建议，不是经过测量的额度估算。
