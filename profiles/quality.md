<!-- codex-delegation-presets:start -->
<!-- Codex delegation preset: quality; version: 0.6.1 -->

# Codex Delegation Policy

Follow user instructions and respect project permissions. A project preset
takes precedence over the global preset.

## Delegation

Only the primary starts or directs children. The primary owns scope,
assignments and final acceptance. Give each child a task or check that can be
scoped and accepted independently when it is worth the coordination. Keep
dependent work with one owner. Use tools directly for simple checks or
calculations.

Use at most 8 active child turns at once, excluding the primary. Respect lower
client limits and user settings, including limits on open child threads. Assign
one owner at a time to overlapping writes or a shared UI.

Choose a role for the work. Scouts collect verifiable facts. Bounded analysts
and workers apply fixed criteria. Operators carry out defined procedures.
Analysts and implementers exercise judgment within an independent assignment.
Reviewers examine a specific risk. Critical agents address a named hard problem.
The role does not set the model or reasoning effort.

## Assignment and model choice

Give each child its goal, scope, relevant sources, acceptance criteria and
only the context it needs. Use `fork_turns="none"` unless the user authorizes
sharing the full history. Name authorized write targets. Start when required
inputs are ready.

Use native delegation. Specify the role, model, effort and a brief reason.
A separate CLI or API model call requires user authorization.

Choose the model and effort together. Use another allowed pair when it fits the
remaining work better. Explain the choice using the same criteria for cheaper and
costlier pairs. Assess implementation and verification separately once the
decision is settled.

Keep the pair while it fits. Before reusing a child, check its role, permissions,
pair and context against the next assignment. Change pairs through a supported
setting or a new child. Preserve useful results and pass on only remaining work.
Tell the user if no allowed pair fits.

## Runtime verification

Before substantive work on each child turn, the primary or child checks the
actual model and effort in Codex runtime metadata or records for that turn.
The primary may relay the child and turn IDs, pair and evidence source.
A launch request or an earlier turn is insufficient.

Read-only work can proceed after verification. Writes and costly checks also
require the primary's approval for that turn within the user's authority.
The primary may send approval with the verification result.

If verification or approval is missing, check available evidence and tell the
primary what is needed. Wait briefly if it is expected. Stop affected work if
it remains unavailable. Stop and report a model or effort mismatch. Close
finished children when the client supports it.

## Review and failures

Keep required reviews and respect human and external gates. Check the actual
version's relevant source, output or behavior against its requirements. For
blind reviews, withhold prior verdicts and producer rationale. Report any
exposure and use a fresh reviewer if a blind verdict is required. Verify the
final state against the authorized outcome. The primary checks child results
before adopting them.

Retry temporary failures when likely to help. Honor Retry-After and use bounded
backoff. If a call's outcome is uncertain, check whether it succeeded before
retrying. Report availability failures and use only models that meet the
requirement.

Resolve ordinary ambiguity within scope. Stop affected work and explain what is
needed if required inputs are missing or conflict, a required starting condition
changes, or the child lacks authority, capability or evidence.

## Selected delegation profile: quality

Primary model recommendation: `gpt-6.2-sol`. Primary effort is the user's choice;
Ultra is used only when explicitly requested.
Allowed child models: `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.2-sol`, `gpt-6.2-astra`.
Allowed child efforts: `medium`, `high`, `xhigh`, `max`; never Low, non-reasoning,
child Ultra or Luna/Max. Luna, Terra, Sol and Astra below refer to those models;
M, H, X and Max mean Medium, High, Xhigh and Max respectively.

### Dispatch decision tree

The primary chooses one branch and table row by what determines acceptance.

1. **Prescribed work** for direct lookup, complete selection or mapping rules,
   or fixed steps.
2. **Evidence and explanation** for judging sources, explaining existing
   behavior or drawing supported conclusions.
3. **Implementation, operation or recovery** when implementation, runtime or
   state determines acceptance.
4. **Design, method or derivation** when the rule, method, design or proof
   needs to be developed.

Use the most specific applicable row. Fixed steps use prescribed work unless
success depends on tracking live state or applying permissions. Separate agreed
implementation from open decisions about behavior, authority or evaluation.

#### Prescribed work

| Remaining work | Pair |
| --- | --- |
| Literal lookup of an unambiguous text or data value, copying, counting or fixed replacement | Luna/H |
| Structural mapping under complete fields and rules | Luna/H |
| Specified execution with behavior, mechanism and steps fixed | Terra/H |
| Bounded source discovery: search a predefined scope using mechanical selection criteria | Terra/H |
| Bounded reading of labels, positions or relations directly from an image | Terra/H |

Use literal lookup when text or structured data gives the answer directly.
Use image reading for facts visible only in the image, even when the item is
named. Use the evidence branch for interpretation or conflicting evidence.
An exact patch or calculation uses specified execution even when it is long or
runs in a terminal. Scouts can do bounded source discovery.

#### Evidence and explanation

| Remaining work | Pair |
| --- | --- |
| Document QA: locate and combine stated facts in supplied material | Sol/M |
| Local investigation: trace bounded code behavior or diagnose a local issue, including by comparing logs | Terra/H |
| Fidelity review against an accepted source or reference | Terra/H |
| Open-ended evidence research: discover sources, verify their authority and judge coverage under a defined question | Sol/H |
| Substantive evidence judgment within a given framework | Sol/H |
| Interpret established rules across sources when applicability, priority or exceptions require judgment | Sol/H |
| Quantitative analysis under a defined metric, with material differences in sources or measurements to reconcile | Sol/H |
| Interpret visual evidence under a given framework when the image determines the conclusion | Sol/H |
| Heavy evidence synthesis or coupled behavior review: reconstruct disputed chronology, causal chains or interacting execution paths under established criteria | Sol/Max |
| Closed hard QA: fixed answer acceptance requires independent problem solving or external domain knowledge | Astra/H |

- In open-ended evidence research, check the sources that can support the
  conclusion and report gaps that affect it.
- When documents require rule interpretation, reconciliation or visual
  inference, use the relevant evidence row. Cite governing facts, rules and
  material exceptions. Report unresolved priority conflicts. Record input and
  measurement choices needed to reproduce key quantitative results.
- Route a bounded code trace to local investigation. Use heavy synthesis or
  coupled behavior review for interacting paths or conflicts across an evidence
  chain. Use a reviewer for independent checks.
- For tool-assisted research-level physics with fixed answer acceptance, see
  the Astra/Medium exception below. Route sustained proofs and formal
  counterexample searches to derivation.

- For established criteria requiring sustained evaluation of interacting
  evidence or interpretations, Sol/X may be selected directly. For closed
  hard QA, consider Astra/X when greater accuracy is required.

#### Implementation, operation or recovery

| Remaining work | Pair |
| --- | --- |
| Natural writing with content and claims settled | Terra/H |
| Ordinary code implementation: clear behavior; choose local implementation and tests | Terra/H |
| Demanding code integration: implement established mechanisms while tracking integration constraints | Sol/Max |
| Stateful tools: perform established operations where tracking state or applying workflow constraints is central | Sol/H |
| End-to-end tools: environment exploration, implementation, execution and feedback determine a working deliverable | Sol/X |
| Recovery of an unfamiliar terminal environment with a repeatable check | Sol/H |
| Scientific execution: numerical implementation, computation and validity are the main burden | Sol/H |

- Route specified UI or media by the execution or implementation required.
  Check rendered UI and affected interactions at relevant screen sizes and
  states. Use fidelity review for independent comparison with an accepted
  reference.
- Choose recovery when the deliverable is a restored environment that passes a
  repeatable check. Use implementation or integration when code changes dominate.
- Use the code rows for numerical work with a settled method and known tests
  when integration determines acceptance. Use scientific execution when
  numerical validity, stability or error requires judgment.
- Use end-to-end tools when figuring out how to assemble or verify an editable
  file determines acceptance, even with a specified layout.
- Reopen or render files to check behavior, editability and sources as
  applicable. Check CAD geometry and constraints in the editable model. For
  timed media, check rendered order and timing and any applicable source timing.

- For scientific computation, consider Astra/H when the expected accuracy
  gain is worth the additional cost. For established tool workflows,
  consider Astra/H when one permission or state violation would invalidate
  the whole result. Research-level physics with tool-assisted solving and
  fixed answer acceptance may use Astra/Medium.

#### Design, method or derivation

| Remaining work | Pair |
| --- | --- |
| Construct or reassess premises, system contract or evaluation framework | Astra/H |
| Jointly construct assumptions, methods and observables | Astra/X |
| Sustained difficult proof, deep derivation or counterexample search | Astra/Max |
| Original visual communication beyond interfaces, where the information hierarchy or diagram must be designed | Astra/H |
| Original 2D interface design with key layout or interaction decisions | Sol/X |
| Complex interactive browser 3D with substantial scene design or 3D interaction work | Sol/Max |

Design covers unsettled rules, measures, visual explanations and system
behavior. Apply settled rules and definitions in their evidence or execution
rows. Check whether an original layout or diagram conveys its claims to the
intended audience. A difficult proof belongs here even when the axioms are fixed.

- For original 2D interfaces, choose Astra/H when the visual design itself
  is a primary acceptance criterion. For complex browser 3D, choose
  Astra/Max when high visual fidelity and polished interaction are required.

Role, format and importance alone do not justify escalation.

<!-- codex-delegation-presets:end -->
