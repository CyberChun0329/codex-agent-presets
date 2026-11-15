<!-- codex-delegation-presets:start -->
<!-- Codex delegation preset: quality; version: 0.5.0 -->

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

Choose model and effort together using the task defaults below. Explain any
exception by the remaining work and task fit, using the same criteria for
cheaper and costlier alternatives. Once a decision is settled, assess its
implementation and verification separately.

Keep the pair while it fits. Before reusing a child, check its role, permissions,
pair and useful context against the next assignment. If the pair changes, use a
supported setting change or a new child with that pair. Preserve useful results
and hand off only the remaining work. If no allowed pair fits, report the
limitation to the user.

## Runtime verification

Before substantive work on every child turn, the primary or child verifies the
actual model and effort in current Codex runtime metadata or records. The primary
may relay the child and turn IDs, pair and evidence source. A launch request or
an earlier turn is insufficient.

After verification, read-only work can proceed. Writes and costly checks also
require the primary's approval for the current turn within the user's authority;
the primary may send approval with the verification result.

If verification or approval is missing, check available evidence and tell the
primary what is needed. Wait briefly if it is expected, then stop the affected
work if it remains unavailable. Stop and report a model/effort mismatch. Close
finished children when the client supports it.

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

Primary model recommendation: `gpt-6.1-sol`. Primary effort is the user's choice;
Ultra is used only when explicitly requested.
Allowed child models: `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.1-sol`, `gpt-6-astra`.
Allowed child efforts: `medium`, `high`, `xhigh`, `max`; never Low, non-reasoning,
child Ultra or Luna/Max. Luna, Terra, Sol and Astra below refer to those models;
M, H, X and Max mean Medium, High, Xhigh and Max respectively.

### General task defaults

| Remaining work | Pair |
| --- | --- |
| Literal copying, counting and fixed replacement | Luna/H |
| Structural mapping under complete fields and rules | Luna/H |
| Execution with behavior, mechanism and steps specified | Terra/H |
| Natural writing, fidelity review, ordinary local implementation or diagnosis | Terra/H |
| Tool workflow managing state and constraints under established rules | Sol/X |
| Substantive evidence judgment within a given framework | Sol/H |
| Construct or reassess premises, system contract or evaluation framework | Astra/H |
| Jointly construct assumptions, methods and observables | Astra/X |
| Sustained difficult proof, deep derivation or counterexample search | Astra/Max |

### Specific task branches

| Remaining work and condition | Pair |
| --- | --- |
| Ordinary code implementation: clear behavior; choose local implementation and tests | Terra/H |
| Demanding code integration: implement established mechanisms while tracking integration constraints | Terra/Max |
| Document QA: answer fully and correctly from given documents | Sol/H |
| Stateful tools: perform established operations while maintaining state and policy constraints | Sol/X |
| End-to-end tools: environment exploration, implementation, execution and feedback adjustment determine a working deliverable | Sol/X |
| Scientific execution: numerical/scientific implementation, computation and validation are the main burden | Terra/Max |
| Closed hard QA: fixed answer acceptance; no open adoption or evaluation-standard selection | Sol/Max |
| Heavy evidence synthesis: reconstruct chronology or causal chains, resolve conflicts and answer composite questions from fixed material and framework | Sol/Max |

For established frameworks and criteria requiring sustained joint evaluation of
interacting evidence or interpretations, Sol/X may be selected directly.

Choose based on the remaining work and complete deliverable. When its conditions
apply, a specific branch takes precedence over its general row. Select a
task-matched alternative directly when warranted, without requiring a cheaper
attempt to fail, model quotas or routine duplicate runs. Importance, length, role
title or imperfect machine verification alone does not justify escalation. The
tables give task defaults.

- A patch or calculation with location, mechanism and steps specified uses the
  specified-execution row, even if long or run in a terminal.
- Constructing or reassessing system contracts, failure/recovery semantics,
  premises, evaluation criteria or a scientific solution framework uses the
  premises/contract or joint-construction row. Ordinary local implementation or
  diagnosis includes choosing reproduction, observations, root cause and a local
  fix. An unknown root cause alone does not change its row. Use ordinary code when
  code must be delivered. Interpreting a local bug against records remains local
  diagnosis.
- For mixed tool work, select by the unresolved technical burden, not title,
  file format, scientific label, deliverable name or order. Established algorithms
  with code integration and given error tests use the code branch; sustained
  judgment about numerical approximation, stability or scientific validity under
  a fixed framework uses scientific execution. A result table or renaming results
  does not change the route. Distinguish state constraints from environment repair
  by the work actually remaining.
- Natural writing and fidelity checking use the local-work row. Judging whether a
  source claim holds uses evidence judgment or framework construction, as applicable.
  For overlapping QA, heavy evidence synthesis takes precedence when chain
  reconstruction, conflict resolution and composite adjudication are the main
  burden. Document QA covers complete answers from supplied material. Closed hard
  QA applies when external domain knowledge or independent hard problem solving
  dominates and acceptance is fixed. Length, citations, professional terminology,
  cover label or subject alone does not decide the route. Sustained proof takes
  precedence, including under fixed axioms; ordinary function boundary tests do not.
- Research-level physics problems requiring a tool-assisted scientific solution
  with defined answer acceptance may use Astra/Medium directly. Routine formula
  evaluation or a physics label alone does not trigger this alternative.
- For inseparable mixed work, route by the unresolved part decisive to success.
  Do not split dependencies to lower the model or require additional review or
  duplicate runs. Keep explicit human and external review gates.

<!-- codex-delegation-presets:end -->
