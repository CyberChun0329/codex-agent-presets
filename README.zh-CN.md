# Codex Agent Presets

**v0.5.0** · [English](README.md)

四套按任务分工的 Codex 主模型与子代理预设。选择愿意为质量支付的溢价，安装到全局或单个项目，并保留已有主模型推理档位。

| 档位 | 偏好 | 主模型 | 同时工作的子代理上限 |
| --- | --- | --- | ---: |
| [Economy](profiles/economy.md) | 保留任务要求，更重成本 | `gpt-6.1-terra` | 3 |
| [Balance](profiles/balance.md) | 有竞争力的任务质量与成本折中 | `gpt-6.1-sol` | 6 |
| [Quality](profiles/quality.md) | 愿为任务相关质量支付更多 | `gpt-6.1-sol` | 8 |
| [Extra Quality](profiles/extra-quality.md) | 愿为困难工作接受更高溢价 | `gpt-6-astra` | 8 |

四档均考虑 GPT-6 Luna、GPT-6.1 Terra、GPT-6.1 Sol 和 GPT-6 Astra，以及 Medium、High、Xhigh、Max 推理档位；不使用 Low、非推理、子代理 Ultra 或 Luna/Max。默认随任务变化，更高推理强度或更大的模型不自动代表更高质量或更低总成本。请确认账户可用模型。

上限只统计同时工作的子代理，不包括主代理；按工作需要启动，客户端或用户更低的限制仍适用。安装保留已有并发设置。主代理推理档位保持不变，包括已选的 Ultra；安装不会开启 Ultra。

## 为什么这样分工？

0.5.0 在相关评测内比较质量、任务成本和风险。Balance 是折中基准，其他档位体现不同的质量溢价偏好，因此部分任务可以共享组合。自然写作、文档回答、代码集成和工具流程分别选型；普通未知根因也不会自动要求更强的推理模型。

第三方来源、比较方法、Balance 的选择依据和局限见[评测依据与预设设计](EVIDENCE.zh-CN.md)。这些是有证据参考的默认，不是整套工作流的性能保证或订阅额度节省实测。

### 评价模型与数据

[可复算分析](benchmarks/README.zh-CN.md)提供评测汇总快照、令牌与价格输入、计算脚本及四档取舍表。计算在各任务内比较来源质量和成本；任务映射与四档偏好仍是明确的设计取舍，不是一个综合分自动优化的结果。

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
请从以下仓库安装 Codex Agent Presets v0.5.0：
https://github.com/CyberChun0329/codex-agent-presets
全部源文件使用 v0.5.0 标签，或对应发布 ZIP。

读取预设或修改前，确定以下三个选择；若有缺项，一次询问所有缺项：
1. 范围：全局或当前项目，并显示目标路径。
2. 档位：economy、balance、quality 或 extra-quality。
3. 是否每天本地时间 09:00 检查仓库更新：是或否。

选择后，只获取并读取该版本的 profiles/<所选档位>.md 和八个 agents/cqp_*.toml，不读取其他档位。

全局目标为 $CODEX_HOME 下的 AGENTS.md、config.toml 和 agents/（默认 ~/.codex）；项目目标为 <project>/AGENTS.md、<project>/.codex/config.toml 和 <project>/.codex/agents/。

按文件自带的起止标记，将所选预设完整加入 AGENTS.md；已有标记区块时替换该区块，保留区块外全部文字。将八个角色文件复制到所选范围的 agents/。

config.toml 只设置根级 model 为所选主模型；主代理推理档位及所有其他设置保持不变，包括并发和子代理默认设置。保留无关文件和其他代理定义。不静默替换模型或安装其他档位。

仅选“是”时，创建或复用内置每日检查：本地时间 09:00，只检查仓库最新提交，变化或失败时通知，无变化则静默，不自动更新配置。时区未知时询问；没有内置调度能力则说明。

核对所选预设版本与目标内容，完成后报告修改路径。新建 chat 后使用已安装配置。
```

角色文件使用 Codex 的[独立自定义代理格式](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)。
