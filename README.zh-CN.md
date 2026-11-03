# Codex Agent Presets

**v0.4.0** · [English](README.md)

四档配置，决定 Codex 使用哪个主模型、如何分配子任务。可安装到全局或单个项目，保留你的主模型推理档位。

安装后照常描述任务，由 Codex 按所选档位决定是否启用子 agent、如何分工。

| 预设 | 主模型 | 子模型 | 子模型推理档位 | 同时工作的子 agent 上限 |
| --- | --- | --- | --- | --- |
| Quality | `gpt-6.1-sol` | Luna、Terra、Sol、Astra | High／Xhigh／条件性 Max | 6 |
| Extra Quality | `gpt-6-astra` | Terra、Sol、Astra | High／Xhigh／条件性 Max | 6 |
| Balance | `gpt-6.1-sol` | Luna、Terra、Sol | Low–Max，按条件使用 | 6 |
| Economy | `gpt-6.1-terra` | Luna、Terra | Low–Xhigh | 3 |

上限只统计同时工作的子 agent，不包括主 agent。按需启动，普通任务通常使用 0–3 个；客户端更低的限制仍然适用，安装保留已有并发设置。

表中的子模型分别指 `gpt-6-luna`、`gpt-6.1-terra`、`gpt-6.1-sol` 和 `gpt-6-astra`。请确认你的账户可以使用所选模型。

## 按订阅选择

可按以下建议起步，再根据实际用量调整：

| ChatGPT 月订阅 | 建议 |
| --- | --- |
| Pro $500 | Quality 或 Extra Quality |
| Pro $200 | Balance 或 Quality |
| Pro $100 | Economy 或 Balance |
| Plus $20 | 避免常态化使用 Ultra 推理档位 |

套餐价格与额度见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/pricing)。

## 安装

填入仓库地址，将下面这段提示词交给 Codex：

```text
请从以下仓库安装 Codex Agent Presets：
仓库地址：https://github.com/CyberChun0329/codex-agent-presets

读取预设或改动前，先一次问我三个选择：
1. 范围：全局或当前项目，并显示目标路径。
2. 档位：quality、extra-quality、balance 或 economy。
3. 是否每天本地时间 09:00 检查仓库更新：是或否。

选择后，只获取并读取 profiles/<所选档位>.md 和八个 agents/cqp_*.toml。

全局使用 $CODEX_HOME 下的 AGENTS.md、config.toml 和 agents/（默认 ~/.codex）；项目使用 <project>/AGENTS.md、<project>/.codex/config.toml 和 <project>/.codex/agents/。

按文件自带的起止标记，将所选预设完整加入 AGENTS.md；已有该标记时替换其中内容，保留其他文字。将八个角色文件复制到所选范围的 agents/。config.toml 只设置根级 model 为所选主模型；主模型推理档位及所有其他设置、文件保持不变。

仅选“是”时，创建或复用内置每日检查任务：本地时间 09:00，只检查仓库最新提交，变化或失败时通知，无变化则静默，不自动更新配置。时区未知时询问；没有内置调度能力则说明。完成后报告修改路径。
```

安装后请新建 chat。Economy 已通过隔离项目试装；新 chat 中的生效情况和每日检查尚未实测。

选型依据见[评测说明](EVIDENCE.zh-CN.md)。
