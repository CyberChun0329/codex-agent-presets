# Codex Agent Presets

**v0.4.2** · [简体中文](README.zh-CN.md)

Choose a profile to set Codex's primary model and delegation rules. Install globally or for one project while keeping your primary reasoning effort.

| Profile | Primary model | Child models | Child effort | Active child limit |
| --- | --- | --- | --- | --- |
| Quality | `gpt-6.1-sol` | Luna, Terra, Sol, Astra | High / Xhigh / conditional Max | 8 |
| Extra Quality | `gpt-6-astra` | Terra, Sol, Astra | High / Xhigh / conditional Max | 8 |
| Balance | `gpt-6.1-sol` | Luna, Terra, Sol | Low–Max, conditional | 6 |
| Economy | `gpt-6.1-terra` | Luna, Terra | Low–Xhigh | 3 |

The limit applies to child agents working at the same time, excluding the primary. Use only as many as the task needs, usually 0–3. Any lower client limit still applies; installation preserves existing concurrency settings.

The model names in the child column refer to `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.1-sol` and `gpt-6-astra`. Check that the models you select are available to your account.

## Choose by subscription

These are usage suggestions, not quota estimates:

| ChatGPT monthly subscription | Recommendation |
| --- | --- |
| Pro $500 | Quality or Extra Quality |
| Pro $200 | Balance or Quality |
| Pro $100 | Economy or Balance |
| Plus $20 | Avoid Ultra reasoning effort for routine work |

See [OpenAI pricing](https://learn.chatgpt.com/docs/pricing) for current prices and usage limits.

## Install

Paste this prompt into Codex:

```text
Install Codex Agent Presets from this repository:
Repository URL: https://github.com/CyberChun0329/codex-agent-presets

Before reading a profile or making changes, ask me these three choices together:
1. Scope: global or current project, showing the target paths.
2. Profile: quality, extra-quality, balance, or economy.
3. Daily repository update check at 09:00 local time: yes or no.

After selection, fetch and read only profiles/<chosen-profile>.md and the eight agents/cqp_*.toml files.

Global targets are AGENTS.md, config.toml and agents/ under $CODEX_HOME (default ~/.codex). Project targets are <project>/AGENTS.md, <project>/.codex/config.toml and <project>/.codex/agents/.

Add the complete selected profile to AGENTS.md using its start/end markers; if those markers already exist, replace their contents and preserve all other text. Copy the eight role files into the selected scope's agents/. In config.toml, set only the root-level model to the selected primary model; preserve primary reasoning effort and all other settings and files.

Only if I choose yes, create or reuse a built-in daily check at 09:00 local time. Inspect only the repository's latest commit; notify on change or failure, stay quiet otherwise, and do not auto-update configuration. Ask if the time zone is unknown; report if built-in scheduling is unavailable. Report the changed paths when finished.
```

Start a fresh chat after installation.

See the [benchmark notes](EVIDENCE.md) for the model-selection evidence.
