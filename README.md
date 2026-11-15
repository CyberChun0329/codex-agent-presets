# Codex Agent Presets

**v0.5.0** · [简体中文](README.zh-CN.md)

Four task-based presets for Codex's primary model and subagents. Choose how much
quality premium to accept, install globally or for one project, and keep your
existing primary reasoning effort.

| Profile | Preference | Primary model | Active child limit |
| --- | --- | --- | ---: |
| [Economy](profiles/economy.md) | Give more weight to cost while retaining the task's requirements | `gpt-6.1-terra` | 3 |
| [Balance](profiles/balance.md) | Competitive task quality and cost | `gpt-6.1-sol` | 6 |
| [Quality](profiles/quality.md) | Pay more for task-relevant quality | `gpt-6.1-sol` | 8 |
| [Extra Quality](profiles/extra-quality.md) | Accept larger premiums for difficult work | `gpt-6-astra` | 8 |

All profiles consider GPT-6 Luna, GPT-6.1 Terra, GPT-6.1 Sol and GPT-6 Astra with
Medium, High, Xhigh or Max effort. Low, non-reasoning, child Ultra and Luna/Max
are excluded. Defaults differ by task; higher effort or a larger model does not
automatically mean better quality or lower total cost. Check account availability
for the models you intend to use.

Limits count active children, excluding the primary. Use only as many as the work
needs. Any lower client or user limit applies; installation preserves existing
concurrency settings. The primary's effort is kept, including Ultra if already
selected; installation does not enable Ultra.

## Why these defaults?

Version 0.5.0 compares quality, task cost and risk within relevant benchmarks.
Balance provides the reference tradeoff; the other profiles express different
willingness to pay for quality. Some tasks share a pair across profiles. Natural
writing, document answers, code integration and tool workflows have distinct
routes, and ordinary unknown root causes do not automatically require a stronger
reasoning model.

See [Benchmarks and preset design](EVIDENCE.md) for the third-party references,
comparison method, Balance defaults and limits. These are evidence-informed
defaults, not measured subscription savings or guarantees for every workflow.

### Model and data

The [reproducible analysis](benchmarks/README.md) includes the aggregate benchmark
snapshot, token/price cost inputs, calculation script and four-profile tradeoff
tables. It compares source-level quality and cost within tasks; task mappings
and profile preferences remain explicit design choices, not an automatically
optimized universal score.

## Choose by subscription

These are usage suggestions, not quota estimates:

| ChatGPT monthly subscription | Recommendation |
| --- | --- |
| Pro $500 | Quality or Extra Quality |
| Pro $200 | Balance or Quality |
| Pro $100 | Economy or Balance |
| Plus $20 | Avoid Ultra reasoning effort for routine work |

See [OpenAI pricing](https://learn.chatgpt.com/docs/pricing) for current plans and
usage limits.

## Install

Paste this prompt into Codex:

```text
Install Codex Agent Presets v0.5.0 from:
https://github.com/CyberChun0329/codex-agent-presets
Use tag v0.5.0, or the matching release ZIP, for all source files.

Before reading profiles or making changes, resolve these three choices. If any are missing, ask for the missing choices together:
1. Scope: global or current project; show the target paths.
2. Profile: economy, balance, quality, or extra-quality.
3. Daily repository update check at 09:00 local time: yes or no.

After selection, fetch and read only profiles/<chosen-profile>.md and the eight agents/cqp_*.toml files from that version. Do not read the other profiles.

Global targets are AGENTS.md, config.toml and agents/ under $CODEX_HOME (default ~/.codex). Project targets are <project>/AGENTS.md, <project>/.codex/config.toml and <project>/.codex/agents/.

Add the complete selected profile to AGENTS.md using its start/end markers. Replace the existing marked block when present; preserve all text outside it. Copy the eight role files to the selected scope's agents/.

In config.toml, set only the root-level model to the selected primary model. Preserve primary reasoning effort and every other setting, including concurrency and subagent defaults. Preserve unrelated files and agent definitions. Do not silently substitute models or install a different profile.

Only if I choose yes, create or reuse a built-in daily check at 09:00 local time. Check only the repository's latest commit; notify on change or failure, stay quiet otherwise, and do not auto-update configuration. Ask if the time zone is unknown; report if built-in scheduling is unavailable.

Verify the selected profile's version and target contents, and report changed paths. Start a fresh chat to use the installed configuration.
```

The role files use Codex's [standalone custom-agent format](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents).
