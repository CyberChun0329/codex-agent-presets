# Codex Agent Presets

**v0.5.2** · [简体中文](README.zh-CN.md)

Four task-based presets for Codex's primary model and subagents. Choose how much
quality premium to accept, install globally or for one project, and keep your
existing primary reasoning effort.

| Profile | Preference | Primary model | Active child limit |
| --- | --- | --- | ---: |
| [Economy](profiles/economy.md) | Give more weight to cost while retaining the task's requirements | `gpt-6.1-terra` | 3 |
| [Balance](profiles/balance.md) | Competitive task quality and cost | `gpt-6.2-sol` | 6 |
| [Quality](profiles/quality.md) | Pay more for task-relevant quality | `gpt-6.2-sol` | 8 |
| [Extra Quality](profiles/extra-quality.md) | Accept larger premiums for difficult work | `gpt-6.2-astra` | 8 |

All profiles consider GPT-6 Luna, GPT-6.1 Terra, GPT-6.2 Sol and GPT-6.2 Astra with
Medium, High, Xhigh or Max effort. Low, non-reasoning, child Ultra and Luna/Max
are excluded. Defaults differ by task; higher effort or a larger model does not
automatically mean better quality or lower total cost. Check account availability
for the models you intend to use.

Limits count active children, excluding the primary. Use only as many as the work
needs. Any lower client or user limit applies; installation preserves existing
concurrency settings. The primary's effort is kept, including Ultra if already
selected; installation does not enable Ultra.

## Why these defaults?

Balance is the reference for each task. Choose a model and effort that deliver
competitive quality at a reasonable cost. Economy accepts less quality margin
where the task permits it. Quality and Extra Quality accept progressively larger
premiums for gains that matter to the task. Several profiles can share the same choice.

| Task | Economy | Balance | Quality | Extra Quality |
| --- | --- | --- | --- | --- |
| Tools with established steps and state constraints | Terra/Medium | Sol/Medium | Sol/High | Astra/Max |
| Tool work that requires exploration and adjustment | Terra/Medium | Sol/High | Sol/Xhigh | Astra/Xhigh |
| Scientific computation and validation | Terra/High | Sol/Medium | Sol/High | Astra/Max |
| Hard questions with a fixed answer | Sol/Medium | Sol/Medium | Astra/High | Astra/Max |
| Demanding code integration | Terra/High | Terra/High | Sol/Max | Astra/Xhigh |
| Original 2D interface design | Sol/High | Sol/High | Sol/Xhigh | Astra/High |
| Complex interactive 3D in the browser | Sol/Max | Sol/Max | Sol/Max | Astra/Max |
| Bounded extraction that requires reading an image | Terra/Medium | Terra/High | Terra/High | Terra/High |
| Recovery of an unfamiliar terminal environment with a repeatable check | Terra/High | Sol/High | Sol/High | Astra/Xhigh |

Sol and Astra refer to GPT-6.2, Terra to GPT-6.1 and Luna to GPT-6. Each profile
lists its exceptions. For a usable workbook, presentation or document, choose
by the work required to reconcile sources, assemble the file and verify it.
See the [benchmark evidence](EVIDENCE.md) for the quality
gains and cost differences behind these choices.

### Model and data

The [calculation guide](benchmarks/README.md) covers the v0.5.0 baseline and the
6.2 comparisons. The current tables include [benchmark scores and task costs](benchmarks/quality-6.2.csv),
[additional task comparisons and cost estimates](benchmarks/task-tradeoffs-6.2.csv),
and [frontend design and web application results](benchmarks/frontend.csv).

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
Install Codex Agent Presets v0.5.2 from:
https://github.com/CyberChun0329/codex-agent-presets
Use tag v0.5.2, or the matching release ZIP, for all source files.

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
