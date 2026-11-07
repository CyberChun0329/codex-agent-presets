# Changelog / 版本记录

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
- Add a [local Terra/High vs Sol/High comparison](EVIDENCE.md) for revision and review.

### 简体中文

- 四档固定标准的文稿修订和审阅优先 Terra：Quality、Extra Quality 通常从 Terra/High 开始，Balance、Economy 仍按任务选择推理档位。
- 补充 Terra/High 与 Sol/High 的[本地修订、审阅对比](EVIDENCE.zh-CN.md)。

## 0.4.0 — 2026-11-03

- Provide four independent English profiles and eight shared roles, with bilingual documentation and subscription-based recommendations.
- Install only the selected profile. Reinstalling or switching profiles replaces the same marked `AGENTS.md` block; other `config.toml` settings are preserved.
- Keep the three installation choices: scope, profile and optional daily repository update check.
- Limit child agents working at once to 3 for Economy, 6 for Balance, and 8 for Quality and Extra Quality.

- 提供四份独立的英文配置、八个共用角色及双语文档和订阅选档建议。
- 仅安装所选配置。重装或切换档位时替换 `AGENTS.md` 中同一个标记区块；保留 `config.toml` 的其他设置。
- 保留三个安装选项：作用域、档位和可选的每日仓库更新检查。
- Economy 最多同时使用 3 个子 agent，Balance 最多 6 个，Quality 和 Extra Quality 最多 8 个。
