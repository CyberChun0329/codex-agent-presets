<!-- codex-delegation-presets:start -->
<!-- Codex delegation preset: quality; version: 0.4.2 -->

# Codex Delegation Policy

Apply this policy to delegation. Follow the user's instructions, project
permissions and required reviews. A project preset takes precedence over the
global preset.

## Delegation

The primary decides scope, divides work and accepts the final result. Only the
primary starts or directs children. It keeps decisions that depend on each other
together. Delegate independent work when it is worth the time and coordination.
Give each child a distinct task or a specific independent check. Use tools
directly for straightforward checks or calculations.

Use at most 8 active child turns at once, excluding the primary. Respect
any lower client limit and the user's settings, including limits on open child
threads. Assign one owner at a time to overlapping writes or a shared UI.

Choose a role for the work. Scouts collect verifiable facts. Bounded analysts
and workers apply fixed criteria. Operators carry out defined procedures.
Analysts and implementers exercise judgment within an independent assignment.
Reviewers examine a specific risk. Critical agents address a named hard problem.
The role does not set the model or reasoning effort.

## Assignment and model choice

Give each child its goal, relevant sources, scope and acceptance criteria.
Include only the context it needs. Use `fork_turns="none"` unless the user
authorizes sharing the full history. For writes, identify the authorized files
or targets. Start when required inputs are ready.

Specify the role, model, reasoning effort and a short reason. Use native
delegation. A separate CLI or API model call requires user authorization.

Choose the pair for the current task. Once a decision is settled, assess its
implementation and verification on their own criteria. When choosing a stronger
model than the profile would normally use for the task, name the remaining
judgment or capability need in the dispatch reason.

Choose model and effort separately within the profile:
- Low or Medium, where allowed, for bounded work with effective checks.
- High for work with a clear approach, including bounded reviews.
- Xhigh for interacting constraints or a difficult diagnosis.
- Max for a specific reasoning bottleneck or task-matched evidence of benefit.
  Consider lower effort on a stronger model when the profile allows it.

Keep the pair while it fits the work. Before reusing a child, check its role,
permissions and pair against the next assignment, including the value of its
existing context. If the pair changes, use a supported setting change or a new
child with an explicit pair. Preserve useful results and pass only the work that
remains. If no allowed pair meets the need, report the limitation to the user.

## Runtime verification

Before substantive work on each child turn, the primary or child checks the
actual model and effort in current Codex runtime metadata or records. The primary
can relay the child and turn IDs, actual pair and source of the check. A launch
request or a previous turn does not establish the current pair.

Read-only work can proceed after verification. Writes and costly checks also
need the primary's approval for that turn within the user's authorization.
The primary can give that approval with the verification result.

If proof or approval is missing, check available evidence and tell the primary
what is missing. Wait briefly only if it is expected, then stop the affected work
if it remains blocked. If the runtime pair differs from the assigned pair, stop
and report the mismatch. Close children when finished if the client supports it.

## Review and failures

Keep required reviews. Review the actual version against its requirements and
check the relevant source, output or behavior. For a blind review, keep prior
verdicts and producer rationale out of the assignment. If exposed, report the
loss of blindness and use a fresh reviewer when a blind verdict is required.
The primary checks delegated results before adoption and accepts the whole task.

Retry temporary failures when a retry is likely to help. Honor Retry-After and
use bounded backoff. Check whether an uncertain call already succeeded before
retrying it. Report availability failures without substituting a model that
cannot meet the requirement.

Resolve ordinary ambiguity within the assignment. Stop affected work and explain
what is needed if required inputs are missing or conflict, a required starting
condition changes, or the child lacks authority, capability or evidence to proceed.

## Selected delegation profile: quality

Primary model recommendation: `gpt-6.1-sol`. Primary effort remains the user's
choice; `ultra` is recommended but applied only on explicit request.
Allowed child models: `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.1-sol`, `gpt-6-astra`.
Allowed child efforts: `high`, `xhigh`, `max`; never Ultra.

Use Luna for checkable search, exact extraction, comparison and simple changes
with strong validation. Prefer Terra for drafting or revision within a clear
brief, visual recognition, computer use with defined outcomes, analysis under
an established method and bounded implementation. Consider Terra/Xhigh directly for bounded interacting coding steps,
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
human/external review gates.

<!-- codex-delegation-presets:end -->
