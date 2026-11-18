# Codex Agent Presets

**v0.6.0** · [English](README.md)

四套预设为 Codex 设置主模型，并提供按任务分派子代理的规则。按愿意为质量多付多少来选档，可安装到全局或单个项目。安装保留主代理已有的推理档位。

| 档位 | 偏好 | 主模型 | 同时工作的子代理上限 |
| --- | --- | --- | ---: |
| [Economy](profiles/economy.md) | 保留任务要求，更重成本 | `gpt-6.1-terra` | 3 |
| [Balance](profiles/balance.md) | 有竞争力的任务质量与成本折中 | `gpt-6.2-sol` | 6 |
| [Quality](profiles/quality.md) | 愿为任务相关质量支付更多 | `gpt-6.2-sol` | 8 |
| [Extra Quality](profiles/extra-quality.md) | 愿为困难工作接受更高溢价 | `gpt-6.2-astra` | 8 |

四档均考虑 GPT-6 Luna、GPT-6.1 Terra、GPT-6.2 Sol 和 GPT-6.2 Astra，以及 Medium、High、Xhigh、Max 推理档位。子代理排除 Low、非推理、Ultra 和 Luna/Max。提高推理档位或换用更大的模型，对质量和总成本的影响随任务而变。请确认账户可用模型。

上限只统计同时工作的子代理。按工作需要启动，客户端或用户更低的限制仍适用。安装保留已有并发设置和主代理推理档位，包括已选的 Ultra。

## Codex 怎样分工？

简单检查由主代理直接处理，值得委派且可独立验收的工作交给子代理。派发时，主代理先判断哪项工作决定结果能否满足要求，再按已安装的预设选择角色、模型和推理档位。四档采用相同的任务分类。

1. **按既定要求处理**，例如直接读取无歧义的数据、按完整规则筛选或映射、执行已明确的步骤。范围预先界定、筛选标准可直接应用的来源查找，可交给 scout。
2. **取证与解释**，例如判断哪些来源能回答开放问题、汇集文档中明示的事实、适用规则、消解证据之间的冲突。
3. **实现、操作与恢复**，例如修改代码、按状态约束操作、恢复可用的工作环境。
4. **设计、方法或推导**，例如决定要做什么或如何度量、原创设计、构造证明。

互相依赖的判断由同一个代理负责。可以独立验收的检查可并行。

## 为什么这样分工？

每类任务以 Balance 为基准，选择质量有竞争力、成本也合适的模型和推理档位。Economy 在验收要求允许时，用一部分质量余量换取更低成本。Quality 和 Extra Quality 则依次更愿意为与任务相关的质量提升付费。同一任务可以在几个档位使用同一个组合。

| 任务 | Economy | Balance | Quality | Extra Quality |
| --- | --- | --- | --- | --- |
| 在既定范围内按明确标准查找来源 | Terra/Medium | Terra/Medium | Terra/High | Terra/High |
| 汇集给定材料中明示事实的文档问答 | Terra/Medium | Sol/Medium | Sol/High | Sol/High |
| 按既定步骤操作并跟踪状态的工具任务 | Terra/Medium | Sol/Medium | Sol/High | Astra/Max |
| 需要探索环境并按反馈调整的工具任务 | Terra/Medium | Sol/High | Sol/Xhigh | Astra/Xhigh |
| 科学计算与验证 | Terra/High | Sol/Medium | Sol/High | Astra/Xhigh |
| 答案固定的困难问答 | Sol/Medium | Sol/Medium | Astra/High | Astra/Max |
| 困难代码集成 | Terra/High | Terra/High | Sol/Max | Astra/Xhigh |
| 原创 2D 界面设计 | Sol/High | Sol/High | Sol/Xhigh | Astra/High |
| 浏览器内复杂交互式 3D | Sol/Max | Sol/Max | Sol/Max | Astra/Max |
| 必须读图才能完成的有界提取 | Terra/Medium | Terra/High | Terra/High | Terra/High |
| 有可重复验收检查的陌生终端环境恢复 | Terra/High | Sol/High | Sol/High | Astra/Xhigh |

Sol 和 Astra 使用 GPT-6.2，Terra 使用 GPT-6.1，Luna 使用 GPT-6。各预设列有对应的例外条件。数值方法与测试已定，且验收取决于代码集成时，按代码工作分配。验收取决于判断数值结果是否有效、稳定或满足误差要求时，按科学计算分配。误差或稳定性决定验收时，Balance 用 Sol/High。直接相关的证据表明准确性提升值得额外成本时，Extra Quality 可选 Astra/Max。

交付可编辑的工作簿、演示稿或文档时，即使版式已给定，只要需要探索如何制作或验证文件、且这项工作决定验收，就按端到端工具任务分配。详见[完整分工表](benchmarks/routing-0.6.0.csv)和[评测依据与预设设计](EVIDENCE.zh-CN.md)。

### 评价模型与数据

[复算说明](benchmarks/README.zh-CN.md)涵盖 v0.5.0 基线和 6.2 数据。当前比较可查阅[评测得分与任务费用](benchmarks/quality-6.2.csv)、[补充任务对照与成本估算](benchmarks/task-tradeoffs-6.2.csv)、[Codex 环境中的仓库问答、终端和代码修改成绩](benchmarks/codex-agent-2.1.csv)和[前端设计与 Web 应用评测](benchmarks/frontend.csv)。

## 按订阅选择

以下是使用建议，不代表实测额度：

| ChatGPT 月订阅 | 建议 |
| --- | --- |
| Pro $500 | Quality 或 Extra Quality |
| Pro $200 | Balance 或 Quality |
| Pro $100 | Economy 或 Balance |
| Plus $20 | 避免常态化使用 Ultra 推理档位 |

当前套餐与用量限制见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/pricing)。

## 安装

将下面这段提示词交给 Codex：

```text
请安装 Codex Agent Presets v0.6.0。如果我提供了对应的 ZIP，就从该 ZIP 安装；否则使用以下仓库的官方 v0.6.0 标签：
https://github.com/CyberChun0329/codex-agent-presets
如果标签还不可用，向我索取对应的 ZIP。全部文件使用同一来源、同一版本。

读取预设或修改前，确定以下三个选择；若有缺项，一次询问所有缺项：
1. 范围：全局或当前项目，并显示目标路径。
2. 档位：economy、balance、quality 或 extra-quality。
3. 是否每天本地时间 09:00 检查仓库更新：是或否。

选择后，只从该来源读取 profiles/<所选档位>.md 及 analyst、bounded_analyst、bounded_worker、critical、implementer、operator、reviewer、scout 对应的 agents/cqp_*.toml。

全局目标为 $CODEX_HOME 下的 AGENTS.md、config.toml 和 agents/（默认 ~/.codex）；项目目标为 <project>/AGENTS.md、<project>/.codex/config.toml 和 <project>/.codex/agents/。

写入前，确认预设的起止标记完整、档位和版本为所选档位和 v0.6.0，并确认八个角色文件齐全。如果我提供了 ZIP 且有官方 SHA-256，就核对摘要。任何一项核验失败时，先停止写入。

检查改动后，预期工作目录会应用哪些指引、角色和模型。如果 AGENTS.override.md、项目预设等更高优先级的文件或设置，或子代理被禁用、项目的信任状态、指引字节上限会妨碍所选预设生效，请说明具体原因，等我决定后再写入。除非我授权，保留这些文件和设置。

按文件自带的起止标记，将所选预设完整加入 AGENTS.md；已有标记区块时替换该区块，保留区块外全部文字。将八个角色文件复制到所选范围的 agents/。

config.toml 只设置根级 model 为所选主模型；主代理推理档位及所有其他设置保持不变，包括并发和子代理默认设置。保留无关文件和其他代理定义。不静默替换模型或安装其他档位。

仅选“是”时，创建或复用内置每日检查：本地时间 09:00，只检查仓库最新提交，变化或失败时通知，无变化则静默，不自动更新配置。时区未知时询问；没有内置调度能力则说明。

回读目标文件并报告修改路径。另行核实所选预设是否完整加载并适用于预期工作目录的新 chat，以及生效的默认模型是否与预设一致。有原生运行证据时以它为准。如果只能核对文件，报告生效情况尚未验证，并告诉我在新 chat 里核对什么。
```

角色文件使用 Codex 的[独立自定义代理格式](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)。
