---
name: product-definition
description: Run Process 03 Product Definition after an eligible Product Discovery decision. Define product intent, positioning, concept, capability scope, measures and non-goals. Do not create App Flow, UX/UI or engineering specifications.
---

# Product Definition — Process 03

## Mission and boundary

Turn an eligible Process 02 result into an evidence-traceable definition of what product is intended, for whom, what customer outcome it promises, which high-level capabilities deliver it, what is in/out of the first release, and how success will be recognized.

Process 02 decides which opportunity matters. Process 03 defines the product and its approved capability scope. Process 04 translates that definition into App Flow.

This process is not a full engineering PRD, App Flow, information architecture, wireframe, UI/UX design, design system, API/database architecture, implementation plan, sprint backlog or code.

## Operating principles

- Evidence before conviction. Carry forward evidence IDs, confidence, counter-evidence and unresolved assumptions.
- User approval is a decision, not customer evidence.
- Define what and why before how. Leave screen order, navigation, interaction and technical design to later processes.
- Spar respectfully. Present a recommendation and its strongest counterargument.
- Research only decision-relevant unknowns that could change target user, positioning, promise, constraints or scope.
- Keep the process proportional. Resolve only unknowns that could change product shape.
- No automatic tab handoff, silent approval or inferred freeze.

## Required inputs and handoff eligibility

For the PROCESS_02 route, read:
- product/discovery/00_DISCOVERY_CONTROL.md
- product/discovery/07_DISCOVERY_DECISION.md
- product/discovery/08_DISCOVERY_OUTCOME.md when the Control File says an Outcome exists
- the relevant Discovery Brief, Opportunity Map, Evidence Register, Assumption Map and source material.

The Process 02 Control File is authoritative for initiative_id, Gate 3 status, evidence_status and discovery_outcome.status. The Decision Brief is authoritative for the opportunity decision and READY FOR TESTING status. If an artifact header conflicts with the Control File, or source files cannot be read and hashed, the handoff is NOT_VERIFIED and the process stops.

The only eligible decisions are PROCEED and NARROW (with the narrowed direction preserved). PIVOT, PAUSE and STOP are not eligible. For PIVOT, return to Process 02 and record the new direction there. Never reinterpret these decisions as PROCEED.

Exactly one of these routes is required:

### Route A — frozen Discovery Outcome

- Process 02 Gate 3 is APPROVED.
- Process 02 Control File discovery_outcome.status is FROZEN.
- The Discovery Outcome exists and its header agrees with the Control File.
- The opportunity decision is PROCEED or NARROW.
- Record and hash the source Control File, Decision Brief, Outcome and every material Discovery artifact used.

### Route B — READY FOR TESTING

- Process 02 Gate 3 is APPROVED.
- The Decision Brief explicitly says READY FOR TESTING.
- Process 02 discovery_outcome.status is NOT_CREATED or absent. DRAFT or REVIEW_REQUIRED Outcome state blocks this route.
- The opportunity decision is PROCEED or NARROW.
- The user sends the exact command ACCEPT RESIDUAL UNCERTAINTY before Gate 1.

Persist that command, timestamp, evidence status, initiative ID and material unresolved risks in the Process 03 Control File. Re-check this acceptance at Tab 02, Tab 03 and immediately before freeze. Do not infer acceptance from "OK", praise, "continue" or FREEZE PRODUCT DEFINITION.

### Existing product route

An existing product may bypass Process 02 only after the user sends the exact command USE EXISTING PRODUCT CONTEXT and supplies a readable source-context path. Record route, source identifier, path and hash. Do not pretend Process 02 gates were passed. If the source context cannot be verified, stop.

If another initiative's Process 02 or Process 03 control file is present, do not overwrite it. Use one initiative per workspace or ask the user to create a separate initiative path.

## Content integrity, timestamps and canonical state

The only source of truth for Process 03 approval and lifecycle state is product/definition/00_PRODUCT_DEFINITION_CONTROL.md. Initialize it from templates/03-PRODUCT-DEFINITION/00-PRODUCT-DEFINITION-CONTROL.md if missing.

Use SHA-256 for every artifact covered by an approval or freeze. On Windows, use PowerShell, for example:

    (Get-FileHash -Algorithm SHA256 -LiteralPath ".\product\definition\01_PRODUCT_INTENT.md").Hash.ToLowerInvariant()

Use a real local timestamp in Asia/Ho_Chi_Minh. On Windows, use:

    $zone = [TimeZoneInfo]::FindSystemTimeZoneById('SE Asia Standard Time')
    [TimeZoneInfo]::ConvertTime([DateTimeOffset]::UtcNow, $zone).ToString('yyyy-MM-dd HH:mm:ss zzz')

Never invent hashes or timestamps. If the terminal, file read, hash or timestamp cannot be verified, record NOT_VERIFIED and stop the affected approval/freeze. User confirmation that a file "has not changed" is not a substitute for a hash.

Every exact approval must:
1. Read the current Control File and check state_seq.
2. Recompute hashes for the exact artifacts being approved.
3. Save command, user decision, timestamp and approved_artifacts.
4. Increment state_seq.
5. Read the saved Control File back and verify the expected state and hashes.
6. Report success only after read-back succeeds.

A stale state_seq means another tab changed the control state: stop, reload and reconcile. state_seq is an optimistic stale-read check, not a file lock or atomic transaction. Only one tab may write the Control File at a time. Do not perform concurrent control updates.

Use exact commands:
- Gate 1: APPROVE PRODUCT INTENT
- Gate 2: APPROVE PRODUCT SCOPE
- Gate 3 / freeze: FREEZE PRODUCT DEFINITION
- Reject intent: REJECT PRODUCT INTENT
- Reject scope: REJECT PRODUCT SCOPE
- Route selection: USE EXISTING PRODUCT CONTEXT
- READY FOR TESTING acceptance: ACCEPT RESIDUAL UNCERTAINTY
- Individual residual risk acceptance: ACCEPT RESIDUAL RISK [FINDING-ID]

When the user accepts a MAJOR/MINOR finding, append a record to the top-level accepted_residual_risks array in the Control File with finding_id, severity, accepted_by, exact command, rationale and accepted_at_local. Mirror that record in the review history and canonical artifact. The reviewer cannot create this acceptance record on the user's behalf.

Any non-approval feedback requesting revision must be logged as REVISION_REQUESTED with its reason. It does not approve a gate. A rejection command records REJECTED; a later approval requires new hashes and a fresh exact approval command.

## Three-tab workflow

### Tab 01 — Product Intent & Positioning

Entry:
- Verify the selected route and handoff eligibility.
- Verify Process 02 initiative identity and source hashes.
- For READY FOR TESTING, verify persisted uncertainty acceptance.
- If any source is missing, changed or contradictory, stop and set handoff status NOT_VERIFIED.

Work:
1. Summarize what Process 02 supports, what remains unknown and the opportunity decision.
2. Inherit Process 02's evidence-supported target segment, context, job and current alternatives. Record any deviation and its rationale; never silently broaden or replace them.
3. Define target segment and customer outcome. Do not create a fictional persona or claim a hypothetical segment is validated.
4. Draft positioning: For [target segment] who [need/opportunity], [product] is a [category] that [customer outcome]. Unlike [current alternative], it [credible differentiation].
5. Explain why this product should exist now and what would make it meaningfully distinct. Use verified research only.
6. Identify product-level assumptions and decisions that could change product shape.
7. Recommend one product intent and state the strongest counterargument.

Artifacts:
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md

Stop at Gate 1. Require APPROVE PRODUCT INTENT. Store hashes for both artifacts. Do not start Tab 02 automatically.

### Tab 02 — Product Shape & Scope

Entry:
- Run in a fresh conversation.
- Re-verify handoff source hashes and uncertainty acceptance if Route B.
- Verify Gate 1 = APPROVED and recompute both Gate 1 artifact hashes. Any mismatch reopens Gate 1 and stops.

Work:
1. Define product concept and core mechanism at high level: what the user brings, what the product enables and what outcome changes.
2. Define 3–7 product principles only when each guides a real trade-off.
3. Translate the opportunity into a small set of customer-facing capabilities. Phrase them as outcomes/abilities, not UI widgets or technical components. Assign stable capability IDs (CAP-01, CAP-02, ...).
4. Define first-release scope with explicit IN, NOT NOW and OUT boundaries. Apply a cut-line test to each IN item.
5. Record dependencies, constraints, ethical/privacy considerations and product risks.
6. Define leading and lagging success measures. Include definition, source, baseline, target status, time window, owner and guardrails where known. Never invent values.
7. Record material decisions, rejected alternatives, accepted risks and deferred unknowns.

Artifacts:
- product/definition/03_PRODUCT_SHAPE.md
- product/definition/04_CAPABILITY_SCOPE.md
- product/definition/05_SUCCESS_MEASURES.md
- product/definition/06_DECISION_LOG.md

Stop at Gate 2. Require APPROVE PRODUCT SCOPE. Store hashes for all four artifacts. Do not start Tab 03 automatically.

### Tab 03 — Independent Definition Review

Entry:
- Run in a fresh conversation.
- Re-verify Process 02 source hashes and residual-uncertainty acceptance.
- Verify Gates 1 and 2 are APPROVED and all six source artifact hashes still match.
- If anything is missing, stale or changed, stop and reopen affected gates.

Reviewer permissions:
- Read-only for artifacts 01–06 and Process 02 sources.
- May create/append review history and create/update the draft candidate.
- Must not edit artifacts 01–06 or Process 02 source artifacts.
- Route remediation to a fresh Tab 01 or Tab 02 conversation based on the finding's source.

Review independently:
1. Trace every material promise and capability to Process 02 evidence or explicitly label it as a hypothesis/strategic choice.
2. Check target specificity and inheritance/deviation from Process 02.
3. Check outcome framing, differentiation and alternatives.
4. Check scope and the IN / NOT NOW / OUT cut-line.
5. Check trade-off utility of product principles.
6. Check metric definitions, sources, baseline and target status.
7. Check contradictions, dependencies, risks, ethics/privacy and scope creep.
8. Identify what would make the product direction wrong or not worth building.
9. Produce BLOCKER / MAJOR / MINOR findings with exact file, section, evidence, consequence and required correction.
10. Test positioning specificity: could the positioning statement describe any competing product without meaningful change? If yes, record the missing differentiation as a finding.

Append a new review round to product/definition/07_DEFINITION_REVIEW.md. Never delete or overwrite prior rounds. Keep finding IDs stable. Record hashes of artifacts 01–06 reviewed in each round.

If BLOCKER findings exist, do not prepare a freeze candidate. Return them for remediation. After remediation, the responsible tab must update artifacts and the user must re-approve the affected gate. Tab 03 then performs a new full review round.

Only when there are no BLOCKER findings may Tab 03 create/update 08_PRODUCT_DEFINITION_DRAFT.md. Verify that the draft:
- preserves all material decisions and evidence status from artifacts 01–06;
- adds no new unsupported promise or capability;
- does not turn HYPOTHESIS into FACT;
- includes residual risks, accepted risks and deferred unknowns;
- contains no App Flow, UX/UI or engineering specification.

Record hashes of 01–06 and 08 in the review round and Control File. Review status and open finding counts must also be stored in the Control File.

### Freeze protocol

Wait for the exact user command FREEZE PRODUCT DEFINITION. Do not treat that command as implicit acceptance of residual MAJOR/MINOR findings.

Before freeze:
1. Re-verify handoff, Gate 1 and Gate 2, all their hashes, and Route B uncertainty acceptance where applicable.
2. Recompute hashes of artifacts 01–06, 07 and 08. They must match the latest reviewed round.
3. Confirm the latest review round has zero unresolved BLOCKER findings.
4. Confirm every remaining MAJOR/MINOR finding is resolved or has explicit user acceptance recorded with ACCEPT RESIDUAL RISK [FINDING-ID].
5. Confirm the draft consistency check passed.

Create product/definition/PRODUCT_DEFINITION.md from the reviewed draft. The only allowed content transformation is replacing the exact Markdown line "> Status: REVIEWED CANDIDATE — NOT FROZEN" with "> Status: FROZEN". Do not make any other editorial change during freeze.

Before re-freezing, preserve the previous canonical artifact as PRODUCT_DEFINITION.v<N>.md; never overwrite an earlier frozen version without archiving it.

Compute the final canonical SHA-256. Update Gate 3 to APPROVED, lifecycle_status to FROZEN, and record exact command, timestamp, reviewed source hashes, draft hash, final canonical path/hash and version. Increment state_seq. Read back the Control File and recompute the canonical hash before reporting success.

If the canonical write succeeds but the Control File write/read-back fails, report INCOMPLETE — NOT FROZEN. An orphan canonical file is not eligible for Process 04. Do not claim freeze success.

## Change invalidation matrix

Any material change to a source artifact must be detected by recomputing its stored hash at tab entry and before freeze.

| Changed artifact | Reopen | Lifecycle after a freeze |
|---|---|---|
| Process 02 control, decision, outcome or material discovery input | Gates 1–3; handoff NOT_VERIFIED | REVIEW_REQUIRED |
| 01_PRODUCT_INTENT.md or 02_POSITIONING.md | Gates 1–3 | REVIEW_REQUIRED |
| 03_PRODUCT_SHAPE.md, 04_CAPABILITY_SCOPE.md, 05_SUCCESS_MEASURES.md or 06_DECISION_LOG.md | Gates 2–3 | REVIEW_REQUIRED |
| 07_DEFINITION_REVIEW.md or 08_PRODUCT_DEFINITION_DRAFT.md | Gate 3 | REVIEW_REQUIRED |
| PRODUCT_DEFINITION.md | Gate 3 | REVIEW_REQUIRED |

Reopening Gate 1 also reopens Gates 2 and 3. Reopening Gate 2 also reopens Gate 3. Log event, reason, timestamp and affected artifacts. An out-of-band change is not excused because no agent witnessed it.

## Upstream method library — reference-only boundaries

The vendored upstream material is reference material, not an additional active workflow.

May borrow selectively:
- outcome ladder and customer-outcome framing;
- weakest assumptions and deferred unknowns;
- no-gos and product-shaping trade-off questions;
- decision framing and risk articulation.

Do not execute or import:
- fictional customer quotes or synthetic personas as evidence;
- customer journey walkthroughs, activation paths or fat-marker flows;
- prototype phases, HTML/UI prototypes or interaction models;
- PRD generation, engineering handoff or routes such as /pm-prd and /pm-prototype-to-epics.

Use only ideas that serve a Process 03 decision. These references do not add workspace dependencies. The ferminrp source license remains unresolved as documented; do not invent copyright notices or legal conclusions. The PM Product Brief copy remains a verbatim reference under its recorded MIT license. Never edit upstream source copies in place.

## Evidence and quality rules

- Labels: OBSERVED, USER-REPORTED, ANALYTICS, SECONDARY SOURCE, INTERPRETATION, HYPOTHESIS, UNKNOWN.
- Reuse Process 02 evidence IDs wherever available.
- Separate product decisions from facts about customers.
- Do not claim validation merely because a direction is selected or a definition is frozen.
- Do not invent customer identities, interviews, market size, competitor capabilities, metrics, baselines, targets, legal conclusions or technical feasibility.
- A product principle must guide a trade-off.
- A capability is a customer outcome/ability, not a screen, button, data model or API.
- Metric target status must be UNKNOWN, HYPOTHESIS or COMMITTED. COMMITTED requires a source, baseline and rationale.
- Respect consent, data minimization and participant privacy.

## Definition of done

A frozen Product Definition contains:
1. Specific target segment and usage context, with evidence status and limitations.
2. Customer job/problem and intended outcome.
3. Positioning and value proposition.
4. Product concept/core mechanism at high-level fidelity.
5. Product principles tied to trade-offs.
6. Capability-level first-release scope plus NOT NOW and OUT boundaries, with stable IDs.
7. Leading/lagging measures with baseline and target status visible.
8. Decisions, rejected alternatives, dependencies, risks and deferred unknowns.
9. Independent review with no unresolved BLOCKER findings.
10. Explicit user acceptance for remaining MAJOR/MINOR risks.
11. Human freeze in the canonical Control File with verified hashes.

Do not produce App Flow, UX/UI, wireframes, information architecture, design system, detailed PRD, acceptance criteria, API/database architecture, technical implementation plan, tickets or code.
