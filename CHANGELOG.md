# Changelog / 版本记录

## 0.5.2

### English

- Added subagent guidance for frontend design and implementation, image analysis, terminal recovery, and document QA.

### 简体中文

- 补充前端设计与实现、图像分析、终端环境恢复和文档验收的子代理分工。

## 0.5.1

### English

- Initial support for GPT-6.2 Sol and GPT-6.2 Astra.
- Added benchmark scores and per-task costs by reasoning effort, with estimates labeled. [Benchmark data](benchmarks/README.md)

### 简体中文

- 初步支持 GPT-6.2 Sol 和 GPT-6.2 Astra。
- 补充了各推理档位的评测得分和每题费用，并标明费用估算值。[评测数据](benchmarks/README.zh-CN.md)

## 0.5.0

### English

- Rework all four profiles around task-specific quality and cost tradeoffs, with direct model and effort choices for distinct kinds of work.
- Explain the benchmark evidence, comparison method, source limits and profile preferences in [Benchmarks and preset design](EVIDENCE.md).
- Publish the aggregate data, cost inputs and offline [comparison script](benchmarks/README.md).

### 简体中文

- 按具体任务的质量与成本取舍调整四档配置，为不同工作直接选择模型和推理档位。
- 在[评测依据与预设设计](EVIDENCE.zh-CN.md)中说明评测、比较方法、来源局限及各档偏好。
- 公开汇总数据、费用输入和离线[比较程序](benchmarks/README.zh-CN.md)。

## 0.4.2

### English

- Choose child models for each task and reassess when the work changes.
- Simplify delegation and retry rules across all four profiles.

### 简体中文

- 按子任务选择模型，任务变化时重新判断。
- 简化四档的委派和重试规则。

## 0.4.1 — 2026-11-06

### English

- Prefer Terra for fixed-criteria document revision and review. Quality and Extra Quality normally start with Terra/High; Balance and Economy retain task-based effort selection.
- Added a local Terra/High vs Sol/High comparison for revision and review.

### 简体中文

- 四档固定标准的文稿修订和审阅优先 Terra：Quality、Extra Quality 通常从 Terra/High 开始，Balance、Economy 仍按任务选择推理档位。
- 补充 Terra/High 与 Sol/High 的本地修订、审阅对比。

## 0.4.0 — 2026-11-03

- Provide four independent English profiles and eight shared roles, with bilingual documentation and subscription-based recommendations.
- Install only the selected profile. Reinstalling or switching profiles replaces the same marked `AGENTS.md` block; other `config.toml` settings are preserved.
- Keep the three installation choices: scope, profile and optional daily repository update check.
- Limit child agents working at once to 3 for Economy, 6 for Balance, and 8 for Quality and Extra Quality.

- 提供四份独立的英文配置、八个共用角色及双语文档和订阅选档建议。
- 仅安装所选配置。重装或切换档位时替换 `AGENTS.md` 中同一个标记区块；保留 `config.toml` 的其他设置。
- 保留三个安装选项：作用域、档位和可选的每日仓库更新检查。
- Economy 最多同时使用 3 个子 agent，Balance 最多 6 个，Quality 和 Extra Quality 最多 8 个。
