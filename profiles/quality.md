<!-- codex-delegation-presets:start -->
<!-- Codex delegation preset: quality; version: 0.4.1 -->

# Codex Delegation Policy

Scope: only primary/child model selection and delegated work. This block does not
replace the user's general writing, coding, completion, skills or tool preferences.
Existing user/project authority, permission boundaries and required review gates
still apply. A nearer selected project profile overrides the global profile's
primary recommendation, child pool, routing and active-child limit. Never broaden
scope through delegation.

## Responsibilities and useful delegation

The primary owns scope, permission interpretation, decomposition, coupled decisions,
integration and final acceptance. Only the primary orchestrates; children cannot
spawn agents. Platform approval reviewers are separate. Main effort follows the
user's selection: the package's Ultra recommendation is applied only by explicit
user request, never inferred from its profile name.

Delegate independently useful work when its quality, time or context benefit
exceeds setup, runtime verification, waiting and integration. Zero children is normal.
Use direct tools for mechanical extraction/calculation when sufficient. Keep coupled
work with the primary; batch useful independent units and consume results. Do not pair every
smaller child with a duplicate full investigation by a larger model.

Respect existing live concurrency limits and shared state. Ordinary tasks usually
need 0-3 active children; run at most 8 child turns at once, excluding the primary.
This is a ceiling, not a target: parallel work must be distinct, ready and worth
coordinating. Obey any lower runtime limit and preserve the user's concurrency
settings, including limits on open child threads. Serialize overlapping writes and
shared mutable UI; assign one owner to each coherent UI phase.

Roles describe duties and permissions, not fixed model/effort. Package roles use
the cqp_ prefix to preserve existing custom roles:
- cqp_scout: bounded, checkable collection; no material judgment or writes.
- cqp_bounded_analyst / cqp_bounded_worker: fixed criteria with strong checks.
- cqp_operator: execution under stable constraints and objective checks.
- cqp_analyst / cqp_implementer: independent analysis/execution with in-lane judgment.
- cqp_reviewer: one named material risk or concrete review surface, read-only.
- cqp_critical: one named hard independent bottleneck; write only if expressly scoped.

Roles do not pin model or effort. Each dispatch explicitly states the role, exact
model, exact effort and a short task-based reason. Use native delegation, no separate
model processes for a review or receipt. Standalone CLI/API model transport requires
separate user authority. These rules do not alter parent permissions or service tier.

## Task contracts and effort

Default to fork_turns="none" with a self-contained contract: objective, role/pair,
authoritative sources, scope/ownership, constraints, acceptance/evidence, output and
stop conditions. Include relevant baseline/version and failures, not copied history.
Full-history inheritance needs explicit user approval. Read-only roles return data
and findings, never temporary/report artifacts. Writers have exact authorized paths,
before-state and post-checks; preserve others' changes. Required inputs and interfaces
must be ready before dependent execution/review; no waiting-only lanes.

Choose model and effort separately within the selected profile:
- Low/Medium: available only where the profile permits; bounded work with clear
  goals and effective checks. Benchmark support is task-specific, not universal.
- High: normal baseline when the path/checks are clear, including bounded review.
- Xhigh: materially interacting constraints, alternatives or non-obvious diagnosis.
- Max: a named depth bottleneck or task-matched quality/cost evidence. Compare a
  stronger model at lower effort where the selected profile permits it. Length,
  importance, reviewer status or one failure alone do not establish a need for Max.

A smaller model at Max is not presumed equivalent to a larger model at High.
Keep a coherent task on one pair unless an evidenced gap warrants change. More
effort addresses insufficient depth; missing facts, authority and tool failures
need their own remedies. Preserve valid work and hand off only the unresolved delta.
Never silently exceed a selected profile's pool/cap; report the remaining limitation
and let the user choose a profile change or explicit exception.

## Runtime verification and handoff

Before substantive child work on launch and every resumed turn, verify the actual
model/effort from fresh native evidence for that child/current turn. Launch settings,
role names, self-report and old receipts are not proof. Direct inspection or a primary
receipt naming child, turn, actual pair and exact evidence location suffices.
The primary locates it immediately after launch/resume, before unrelated lengthy work.
Use current native metadata exposed by the client or its readable native records.
Unsupported or missing metadata never waives verification; do not fabricate a receipt.

Verified ordinary read-only work proceeds without another acknowledgement. Writes
and costly checks additionally require current-turn scoped release from the primary,
batched with identity confirmation. Release adds neither human authority nor runtime
permission. A new turn invalidates prior proof and any required release.

Read available evidence before asking/waiting. If proof or required release is missing,
notify once, do safe read-only preflight, wait at most once up to 60 seconds and recheck.
If still blocked, return ESCALATE with runtime_metadata_unavailable or
runtime_release_pending. On a model/effort mismatch, including Ultra children, stop
with runtime_model_effort_mismatch. No READY/resume loop, repeated polling, automatic
respawn or promotion; the primary resolves the cause.

Consume completed results before follow-up. Reuse compatible children for substantive
deltas, not acknowledgement turns. Confirm loaded role/permissions and pair fit the
new contract, then verify the new turn. A changed pair needs a supported setting
change or new explicit-pair child and fresh proof. Closed restoration needs verified
pair restoration; use a fresh verified child if restoration drifts. Close unused
children when supported; otherwise retain idle ones without housekeeping turns.

## Review and integration of delegated work

Identify the authoritative review version and preserved invariants. Recheck actual
targets and required before-state before adoption. Source identity is not semantic
correctness, independence or permission. For blind/fresh review, exclude producer
rationale, prior verdicts and expected winners. Contamination invalidates that blind
attempt; sanitize and use a fresh reviewer. Reviews of prior judgments must be labeled.

Match a delegated check to the user's intended outcome: facts/voice for communication,
calculation/interpretation for analysis, coherence/audience fit for creation, actual
state for tool actions. Keep required project checks and acceptance gates. A child's
PASS does not establish integrated acceptance. For material claim changes, compare
actor, action, quantifiers, conditions and evidence scope; resolve meaningful deltas.
Do not rewrite acceptable delegated prose wholesale or add a full second investigation.

For a delegated visual finding, inspect exact full/adjacent pages and relevant
crop/rotation; contact sheets are triage. For implementation, checks exercise the
real interface and integrated fixtures. These requirements apply to delegated lanes,
not as replacements for the recipient's general document or coding workflow.

One wave per decision phase; later waves need remaining ready independent work, a
new evidence gap or failed acceptance. After two substantive failures on the same
criterion, the primary resolves/replans. Add a reviewer only for a named unresolved
material risk; do not run reviewer and critical lanes on the same risk simultaneously.
Stop delegation when acceptance is met. Report status, decisive evidence, limitations
and unresolved delta; distinguish candidate, adopted, verified and accepted states.

## Call failures and exceptions

For every subagent call, including follow-up, transient capacity/rate/service failure
requires three retries after the initial failed attempt on the same model/effort
(four attempts total) before considering capability reduction. Honor Retry-After,
use bounded backoff, resolve unknown outcomes and retain completed work. Availability
failure is not capability evidence. After exhaustion, preserve required capability,
report the dependency and continue independent authorized work. A same/weaker model
may assist but cannot satisfy a stronger-expert requirement. Permission denials,
invalid contracts and identity mismatches need their own remedies, not blind retries.

Missing/conflicting required input: CONTRACT_INVALID. Changed required before-state:
STALE_CONTRACT. Stop affected work and return the reason/scope to the primary;
unaffected work needs still-valid authority, evidence and required release. Resolve
ordinary in-lane ambiguity; ESCALATE when independence, capability, authority or
adequate verification cannot be maintained. Use COMPLETE for completed scoped work.
The primary owns final verification and acceptance; lower resource use counts only
when the user's required quality, completeness and evidence are met.

## Selected delegation profile: quality

Primary model recommendation: `gpt-6.1-sol`. Primary effort remains the user's
choice; `ultra` is recommended but applied only on explicit request.
Allowed child models: `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.1-sol`, `gpt-6-astra`.
Allowed child efforts: `high`, `xhigh`, `max`; never Ultra.
A nearer selected profile overrides the global profile's routing, pool and
active-child limit.

Use Luna for
clear, checkable search, exact extraction, comparison and simple changes with strong
validation. Prefer Terra for drafting/revision within a clear brief, visual recognition,
computer use with defined outcomes, analysis under an established method and bounded
implementation. Consider Terra/Xhigh directly for bounded interacting coding steps,
and Terra/Max for fitting demanding visual/scientific work when evidence supports it.
Fixed-criteria revision and source-bound document review normally start with
Terra/High. A reviewer role alone does not require Sol. Use Sol for substantive
ambiguity, conceptual/domain judgment, strategy/method choice, coupled decisions
and evidence synthesis. Importance, length or imperfect machine
verification alone do not require Sol.
Proactively consult Astra on a consequential unresolved independent method/design/
strategy/evidence decision or named deep bottleneck when stronger reasoning helps.
Use Astra/Max directly for sustained derivation, counterexample search or tightly
coupled method construction; bounded comparisons can use High/Xhigh. Keep explicit
human/external review gates. Do not duplicate resolved analysis or outsource a settled
plan merely because it is important. High/Xhigh/Max are permitted child efforts.

<!-- codex-delegation-presets:end -->
