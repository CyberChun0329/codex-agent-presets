<!-- codex-delegation-presets:start -->
<!-- Codex delegation preset: balance; version: 0.7.0 -->

# Codex Delegation Policy

Follow user instructions and respect project permissions. A project preset
takes precedence over the global preset.

## Delegation

Only the primary starts or directs children. The primary owns scope,
assignments and final acceptance. Give each child a task or check that can be
scoped and accepted independently when it is worth the coordination. Keep
dependent work with one owner. Use tools directly for simple checks or
calculations.

Use at most 6 active child turns at once, excluding the primary. Respect lower
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

## Selected delegation profile: balance

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

After choosing the task row, use industry evidence when domain judgment or a
domain-specific error determines acceptance. Compare model and effort using
quality and cost evidence from similar work. Use industry indexes to identify
relevant skills and candidates. Keep the applicable default when evidence is
inconclusive.

#### Prescribed work

| Remaining work | Pair |
| --- | --- |
| Literal lookup of an unambiguous text or data value, copying, counting or fixed replacement | Luna/H |
| Structural mapping under complete fields and rules | Luna/H |
| Specified execution with behavior, mechanism and steps fixed | Terra/M |
| Bounded source discovery: search a predefined scope using mechanical selection criteria | Terra/M |
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
| Open-ended evidence research: discover sources, verify their authority and judge coverage under a defined question | Sol/M |
| Substantive evidence judgment within a given framework | Sol/M |
| Explain established rules or resolve a bounded question about their meaning or scope | Sol/M |
| Case-specific rule application: determine an outcome from interacting established rules and decisive facts | Sol/Max |
| Quantitative analysis under a defined metric, with material differences in sources or measurements to reconcile | Sol/M |
| Interpret visual evidence under a given framework when the image determines the conclusion | Sol/M |
| Heavy evidence synthesis or coupled behavior review: reconstruct disputed chronology, causal chains or interacting execution paths under established criteria | Sol/X |
| Closed hard QA: fixed answer acceptance requires independent problem solving or external domain knowledge | Sol/M |

- In open-ended evidence research, check the sources that can support the
  conclusion and report gaps that affect it.
- When documents require rule interpretation, reconciliation or visual
  inference, use the relevant evidence row. Cite governing facts, rules and
  material exceptions. Report unresolved priority conflicts. Record input and
  measurement choices needed to reproduce key quantitative results.
- Use case-specific rule application when an outcome for a particular case
  depends on interactions among established rules or exceptions and decisive
  facts. Examples include applying a transition rule in an eligibility decision
  or resolving competing contract terms. Verify the governing sources and facts.
  Explain the rules when their meaning is the deliverable. Use heavy synthesis
  when establishing the case facts controls acceptance, and design when the
  rules need to be chosen. The listed pair draws on comparable work such as
  complex legal determinations. For less comparable work, start with the
  general rule-interpretation pair.
  For work comparable to the legal evaluation, use Sol/High when avoiding
  material errors against the supplied record takes priority and follow-up
  can check coverage of all decisive issues.
- For a checkable financial modeling answer under an agreed framework that
  requires independent reasoning, use closed hard QA. Use quantitative
  analysis to reconcile figures under a defined metric, and design when
  valuation or identification assumptions are open.
- For economics, use evidence judgment to assess studies and identification
  claims, scientific execution to validate a settled estimator, and design
  to choose a new method or observables.
- For healthcare records, use document QA for stated facts and heavy evidence
  synthesis when reconciling a material conflict across records. Use the
  scientific or evidence row that fits any remaining technical judgment.

- Route a bounded code trace to local investigation. Use heavy synthesis or
  coupled behavior review for interacting paths or conflicts across an evidence
  chain. Use a reviewer for independent checks.
- For tool-assisted research-level physics with fixed answer acceptance, see
  the Astra/Medium exception below. Route sustained proofs and formal
  counterexample searches to derivation.

- For closed hard QA, consider Sol/H when greater answer accuracy justifies
  the additional cost.

#### Implementation, operation or recovery

| Remaining work | Pair |
| --- | --- |
| Natural writing with content and claims settled | Terra/H |
| Ordinary code implementation: clear behavior; choose local implementation and tests | Terra/H |
| Demanding code integration: implement established mechanisms while tracking integration constraints | Sol/M |
| Stateful tools: perform established operations where tracking state or applying workflow constraints is central | Sol/M |
| End-to-end tools: figure out the tools or workflow needed to produce a working deliverable | Sol/H |
| Constrained model construction: build or revise an editable model and verify how its linked elements behave together | Sol/X |
| Recovery of an unfamiliar terminal environment with a repeatable check | Sol/H |
| Scientific execution: numerical implementation, computation and validity are the main burden | Sol/M |

- Use constrained model construction when requirements are settled and the
  editable model must preserve relationships across changes. Examples include
  revising an assembly and checking affected constraints, or building a
  scenario-driven workbook and verifying its dependent formulas and outputs.
  Use the authoring tool to verify those relationships. Use prescribed work
  when the edit or model run and all checks are fully specified. Use design for open requirements, code integration
  when software behavior governs acceptance, and scientific execution when
  numerical validity governs it. Use end-to-end tools when the main work is
  figuring out how to use the tools or assemble the file. The listed pair
  draws on comparable work such as iterative CAD. For less comparable work,
  start with the end-to-end tools pair.
  In comparable CAD work, use Sol/High for a lower-cost local change when
  native checks can catch errors before dependent work.
- In operations work, use the stateful row when permissions or the state of
  business systems govern acceptance. Use end-to-end tools when exploration
  and feedback govern delivery, and design for unsettled process rules.
- Route specified UI or media by the execution or implementation required.
  Check rendered UI and affected interactions at relevant screen sizes and
  states. Use fidelity review for independent comparison with an accepted
  reference.
- Choose recovery when the deliverable is a restored environment that passes a
  repeatable check. Use implementation or integration when code changes dominate.
- Use the code rows for numerical work with a settled method and known tests
  when integration determines acceptance. Use scientific execution when
  numerical validity, stability or error requires judgment.
- Reopen or render files to check behavior, editability and sources as
  applicable. Check CAD geometry and constraints in the editable model. For
  timed media, check rendered order and timing and any applicable source timing.

- For scientific computation, choose Sol/H when acceptance depends on
  numerical error or stability. Research-level physics with tool-assisted
  solving and fixed answer acceptance may use Astra/Medium.

#### Design, method or derivation

| Remaining work | Pair |
| --- | --- |
| Construct or reassess premises, system contract or evaluation framework | Sol/H |
| Jointly construct assumptions, methods and observables | Sol/X |
| Sustained difficult proof, deep derivation or counterexample search | Sol/Max |
| Original visual communication beyond interfaces, where the information hierarchy or diagram must be designed | Sol/H |
| Original 2D interface design with key layout or interaction decisions | Sol/H |
| Complex interactive browser 3D with substantial scene design or 3D interaction work | Sol/Max |

Design covers unsettled rules, measures, visual explanations and system
behavior. Apply settled rules and definitions in their evidence or execution
rows. Check whether an original layout or diagram conveys its claims to the
intended audience. A difficult proof belongs here even when the axioms are fixed.

Role, format and importance alone do not justify escalation.

<!-- codex-delegation-presets:end -->
