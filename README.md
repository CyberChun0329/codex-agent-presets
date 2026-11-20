# Codex Agent Presets

**v0.6.1** · [简体中文](README.zh-CN.md)

Four presets set Codex's primary model and guide subagent assignments by task.
Choose a preset based on how much more you are willing to spend for better
results. Install globally or for one project and keep the primary's existing
reasoning effort.

| Profile | Preference | Primary model | Active child limit |
| --- | --- | --- | ---: |
| [Economy](profiles/economy.md) | Give more weight to cost while retaining the task's requirements | `gpt-6.1-terra` | 3 |
| [Balance](profiles/balance.md) | Competitive task quality and cost | `gpt-6.2-sol` | 6 |
| [Quality](profiles/quality.md) | Pay more for task-relevant quality | `gpt-6.2-sol` | 8 |
| [Extra Quality](profiles/extra-quality.md) | Accept larger premiums for difficult work | `gpt-6.2-astra` | 8 |

All profiles consider GPT-6 Luna, GPT-6.1 Terra, GPT-6.2 Sol and GPT-6.2 Astra with
Medium, High, Xhigh or Max effort. Low, non-reasoning, child Ultra and Luna/Max
are excluded. The effect of higher effort or a larger model on quality and total
cost varies by task. Check account availability for the models you intend to use.

Limits count active subagents, excluding the primary. Use only as many as the
work needs. Any lower client or user limit applies. Installation preserves
existing concurrency settings and the primary's effort, including Ultra if
already selected.

## How Codex delegates

The primary handles straightforward checks directly and delegates independent
work when that helps. For each assignment, the primary identifies which work
will determine whether the result meets the requirements. It then uses the
installed profile to choose the role, model and effort. All four profiles use
the same task categories.

1. **Prescribed work** covers direct, unambiguous lookup, applying complete
   selection or mapping rules, and carrying out specified steps. A scout can
   search a predefined scope using objective selection criteria.
2. **Evidence and explanation** cover judging which sources can answer an open
   question, combining stated facts from documents, applying rules and resolving
   conflicts in the evidence.
3. **Implementation, operation or recovery** covers making changes, operating
   under state constraints and restoring a working environment.
4. **Design, method or derivation** covers deciding what to build or measure,
   creating an original design, and developing a proof.

Keep decisions that depend on each other with one owner. Checks that can be
judged independently can run in parallel.

## Why these defaults?

For each task, Balance sets the reference by choosing a model and effort with
competitive quality at a reasonable cost. Economy accepts less quality margin
where the task permits it. Quality and Extra Quality accept progressively larger
premiums for gains that matter to the task. Several profiles can share the same choice.

| Task | Economy | Balance | Quality | Extra Quality |
| --- | --- | --- | --- | --- |
| Bounded source discovery within a predefined scope | Terra/Medium | Terra/Medium | Terra/High | Terra/High |
| Document Q&A combining stated facts from supplied material | Terra/Medium | Sol/Medium | Sol/Medium | Sol/Medium |
| Tools with established steps and state constraints | Terra/Medium | Sol/Medium | Sol/High | Astra/Max |
| Tool work that requires exploration and adjustment | Terra/Medium | Sol/High | Sol/Xhigh | Astra/Xhigh |
| Scientific computation and validation | Terra/High | Sol/Medium | Sol/High | Astra/Xhigh |
| Hard questions with a fixed answer | Sol/Medium | Sol/Medium | Astra/High | Astra/Max |
| Demanding code integration | Terra/High | Sol/Medium | Sol/Max | Astra/Xhigh |
| Original 2D interface design | Sol/High | Sol/High | Sol/Xhigh | Astra/High |
| Complex interactive 3D in the browser | Sol/Max | Sol/Max | Sol/Max | Astra/Max |
| Bounded extraction that requires reading an image | Terra/Medium | Terra/High | Terra/High | Terra/High |
| Recovery of an unfamiliar terminal environment with a repeatable check | Terra/High | Sol/High | Sol/High | Astra/Xhigh |

Sol and Astra refer to GPT-6.2, Terra to GPT-6.1 and Luna to GPT-6. Each profile
lists its exceptions. When a numerical method and its tests are established,
use the code branch if integration determines acceptance. Use scientific
execution when numerical validity, stability or error determines acceptance.
Balance uses Sol/High when error or stability determines acceptance. Extra
Quality can use Astra/Max when directly relevant evidence supports an accuracy
gain worth the cost.

For editable workbooks, presentations and documents, use end-to-end tools when
figuring out how to assemble or verify the file determines acceptance, even
with a supplied layout. See the [full routing table](benchmarks/routing-0.6.1.csv)
and the [benchmark evidence](EVIDENCE.md).

### Model and data

The [calculation guide](benchmarks/README.md) covers the v0.5.0 baseline and the
6.2 comparisons. The current tables include [benchmark scores and task costs](benchmarks/quality-6.2.csv),
[additional task comparisons and cost estimates](benchmarks/task-tradeoffs-6.2.csv),
[Codex repository Q&A, terminal and patch results](benchmarks/codex-agent-2.1.csv),
[frontend design and web application results](benchmarks/frontend.csv),
and [additional GPT-6.2 results](benchmarks/benchmark-refresh-6.2.csv).

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
Install Codex Agent Presets v0.6.1 from the matching ZIP if I supply one. Otherwise use the official v0.6.1 tag at:
https://github.com/CyberChun0329/codex-agent-presets
If the tag is unavailable, ask me for the matching ZIP. Use that same version and source for every file.

Before reading profiles or making changes, resolve these three choices. If any are missing, ask for the missing choices together:
1. Scope: global or current project; show the target paths.
2. Profile: economy, balance, quality, or extra-quality.
3. Daily repository update check at 09:00 local time: yes or no.

After selection, read only profiles/<chosen-profile>.md and the agents/cqp_*.toml files for analyst, bounded_analyst, bounded_worker, critical, implementer, operator, reviewer and scout from that source.

Global targets are AGENTS.md, config.toml and agents/ under $CODEX_HOME (default ~/.codex). Project targets are <project>/AGENTS.md, <project>/.codex/config.toml and <project>/.codex/agents/.

Before writing, check that the selected profile has a complete marked block for the chosen tier and v0.6.1 and that all eight role files are present. For a supplied ZIP, compare its SHA-256 with the official digest if available. Stop before writing if any check fails.

Check which guidance, roles and model would apply in the intended directory after the change. If higher-priority files or settings such as AGENTS.override.md or a project preset, disabled subagents, project trust or the instruction byte limit would prevent the selected preset from taking effect, report the specific blocker and wait for my decision before writing. Keep those files and settings unless I authorize a change.

Add the complete selected profile to AGENTS.md using its start/end markers. Replace the existing marked block when present; preserve all text outside it. Copy the eight role files to the selected scope's agents/.

In config.toml, set only the root-level model to the selected primary model. Preserve primary reasoning effort and every other setting, including concurrency and subagent defaults. Preserve unrelated files and agent definitions. Do not silently substitute models or install a different profile.

Only if I choose yes, create or reuse a built-in daily check at 09:00 local time. Check only the repository's latest commit; notify on change or failure, stay quiet otherwise, and do not auto-update configuration. Ask if the time zone is unknown; report if built-in scheduling is unavailable.

Read back the targets and report the changed paths. Separately verify that the complete selected preset applies in a fresh chat in the intended directory and that the effective default model matches the preset. Use native runtime evidence when available. If you can verify only the files, report activation as unverified and tell me what to check in a fresh chat.
```

The role files use Codex's [standalone custom-agent format](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents).
