---
name: product-definition
description: Run Process 03 Product Definition after Product Discovery. Define target segment, value proposition, product concept, product principles, capability scope, success measures and non-goals. Do not create App Flow, UX/UI or engineering specifications.
---

# Product Definition — Process 03

## Mission and boundary

Turn the approved Product Discovery result into a clear, evidence-traceable definition of the product: what it is, who it is for, what customer outcome it promises, which high-level capabilities deliver that outcome, what is in/out of the first release, and how success will be recognized.

This is the decision boundary between Process 02 (what opportunity matters) and Process 04 — App Flow (how users move through the product).

This process is NOT a full engineering PRD, App Flow, information architecture, wireframe, UI/UX design, design system, API/database architecture, implementation plan, sprint backlog or code. Do not cross those boundaries.

## Operating principles

- **Evidence before conviction:** carry forward evidence IDs, confidence, counter-evidence and unresolved assumptions from Process 02. User approval is a decision, not customer evidence.
- **What and why before how:** define product outcomes, promise, core mechanism and capability boundaries. Leave screen order, navigation, interaction details and technical design to later processes.
- **Sparring:** challenge the strongest idea respectfully. Present a recommendation and its strongest counterargument.
- **Deep research, selectively:** research only decision-relevant unknowns that could change target user, positioning, product promise, constraints or scope. Cite source, date and confidence in research notes. Do not research for volume.
- **Human-owned decisions:** no automatic tab handoff, silent approval or inferred freeze.
- **Keep it proportional:** resolve only unknowns that could change the product's shape.

## Required inputs and eligibility

Read:
- product/definition/00_PRODUCT_DEFINITION_CONTROL.md if it exists;
- product/discovery/00_DISCOVERY_CONTROL.md;
- product/discovery/07_DISCOVERY_DECISION.md;
- product/discovery/08_DISCOVERY_OUTCOME.md if present;
- relevant Discovery Brief, Opportunity Map, Evidence Register, Assumption Map and cited source material.

Eligible input is one of:
1. A frozen Process 02 Discovery Outcome, with Process 02 Gate 3 APPROVED and Outcome state FROZEN; or
2. A Process 02 Decision Brief with Gate 3 APPROVED and status READY FOR TESTING, provided the user explicitly accepts that unresolved evidence risk may carry into Product Definition.

If neither condition is met, stop and state the missing artifact/gate. Do not invent a Discovery Outcome. Existing products may use documented existing-product context instead of Process 02 only when the user explicitly requests that route and the source context is recorded.

If Process 02 control state cannot be read, mark the handoff NOT VERIFIED and stop.

## Canonical control state

The only source of truth for Process 03 approvals is product/definition/00_PRODUCT_DEFINITION_CONTROL.md.

- If missing, initialize it by copying templates/03-PRODUCT-DEFINITION/00-PRODUCT-DEFINITION-CONTROL.md. Record the initiative ID and exact Process 02 input paths/status.
- Never overwrite a control file belonging to another initiative.
- Do not rely on prior tab chat history or approval phrases embedded only in other documents.
- When the user sends an exact command, update the control file first. Record command, decision, local timestamp (Asia/Ho_Chi_Minh) and artifact revision. Do not claim a gate passed unless the file was saved successfully.
- Preserve an append-only approval/change log.
- If a source input or approved artifact changes, invalidate dependent gates and record why.

Gate commands:
- Gate 1: APPROVE PRODUCT INTENT
- Gate 2: APPROVE PRODUCT SCOPE
- Gate 3 / freeze: FREEZE PRODUCT DEFINITION

## Three-tab workflow

### Tab 01 — Product Intent & Positioning

Inputs:
- Eligible Process 02 artifacts and control state.
- Existing product constraints, strategy or business context supplied by the user.
- Relevant evidence sources from Process 02.

Work:
1. Summarize what Process 02 actually supports, what remains unknown and what decision was made.
2. Define the primary target segment and context. Do not create a fictional persona or claim a hypothetical segment is validated.
3. Define the customer's job/outcome and the specific change the product intends to enable.
4. Draft a positioning statement: For [target segment] who [need/opportunity], [product] is a [category] that [customer outcome]. Unlike [current alternative], it [credible differentiation].
5. Clarify why this product should exist now, how it relates to alternatives and what would make it meaningfully distinct. Use verified research only.
6. Identify product-level assumptions and decisions that would change the product's shape.
7. Recommend a product intent and state the strongest counterargument.

Artifacts:
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md

Stop at Gate 1. Require exact instruction APPROVE PRODUCT INTENT. Update the control file before proceeding.

### Tab 02 — Product Shape & Scope

Entry: Gate 1 must be APPROVED in the canonical control file.

Work:
1. Define the product concept and core mechanism at high level: what the user brings, what the product enables, and what outcome changes. Do not describe screen-by-screen interaction.
2. Define 3–7 product principles only when each guides a real trade-off.
3. Translate the opportunity into a small set of customer-facing capabilities. Phrase capabilities as outcomes/abilities, not UI widgets or technical components.
4. Define first-release scope with explicit IN, NOT NOW and OUT boundaries. Use a cut-line test: if an item is removed, does the primary value promise still hold?
5. Identify dependencies, external constraints, ethical/privacy considerations, platform constraints and product risks at product level only.
6. Define leading and lagging success measures. For each metric include definition, source, baseline, target, time window and owner where known. Use UNKNOWN or BASELINE NEEDED instead of inventing values.
7. Record key decisions, alternatives rejected and deferred unknowns. Do not force unresolved implementation questions into this process.

Artifacts:
- product/definition/03_PRODUCT_SHAPE.md
- product/definition/04_CAPABILITY_SCOPE.md
- product/definition/05_SUCCESS_MEASURES.md
- product/definition/06_DECISION_LOG.md

Stop at Gate 2. Require exact instruction APPROVE PRODUCT SCOPE. Update the control file before Tab 03.

### Tab 03 — Independent Definition Review

Entry: Gates 1 and 2 must both be APPROVED in the canonical control file.

Run in a fresh conversation. Read source artifacts, not the previous tab's chat. Review independently:
1. Trace every material product promise and capability to Process 02 evidence or explicitly label it as a hypothesis/strategic choice.
2. Check target-segment specificity and avoid pretending a generic persona is evidence.
3. Check whether the product promise describes a customer outcome rather than a feature list.
4. Check whether capability scope is small enough to deliver the primary outcome and whether IN / NOT NOW / OUT are unambiguous.
5. Check product principles for actual trade-off utility rather than slogans.
6. Check success measures for observable definitions, available sources and non-fabricated baselines/targets.
7. Find contradictions, hidden dependencies, risky assumptions, ethical/privacy concerns and scope creep.
8. Identify missing decisions that would materially alter the product. Do not ask about low-impact implementation detail.
9. Produce a severity-ranked review with BLOCKER / MAJOR / MINOR findings and cite exact artifact sections.

If BLOCKER findings exist, do not prepare a freeze candidate. Return findings for remediation and wait for revised artifacts. After remediation, re-review changed sections and invalidate affected gates.

Artifacts:
- product/definition/07_DEFINITION_REVIEW.md
- product/definition/08_PRODUCT_DEFINITION_DRAFT.md only when no BLOCKER remains.

When the user explicitly sends FREEZE PRODUCT DEFINITION:
1. Confirm no unresolved BLOCKER findings.
2. Copy the reviewed draft to product/definition/PRODUCT_DEFINITION.md.
3. Update Gate 3 and lifecycle state in the control file to FROZEN.
4. Record exact command, user decision, local timestamp and reviewed artifact revision.
5. Do not claim freeze succeeded if the workspace write fails.

## Change invalidation

- Material Process 02 input changes reopen Gates 1 and 2; set draft lifecycle REVIEW_REQUIRED.
- Product Intent or Positioning changes reopen Gates 1 and 2 and require a fresh review.
- Product Shape, Capability Scope, Success Measures or Decision Log changes reopen Gate 2 and require a fresh review.
- Any change to PRODUCT_DEFINITION.md after freeze changes lifecycle to REVIEW_REQUIRED until re-reviewed and re-frozen.
- Preserve old decisions and artifact revisions in the control log.

## Upstream method library

- Primary shaping reference: existing verbatim copy at upstream/ferminrp/product-shaping/SKILL.md and its references. Its upstream README declares MIT; the source repository root had no standalone LICENSE file at the prior source check. See LICENSES/FERMINRP-LICENSE-STATUS.md.
- Working-backwards reference: references/upstream/pm-product-brief/SKILL.md, copied verbatim from marfoerst/the-pragmatic-pm under MIT. It informs customer-outcome framing and outcome ladders; it is reference-only.
- The upstream PM Product Brief mentions domain-context.md and personal-context.md; these are not dependencies of this kit.
- Never present fictional/sample personas, customer quotes or metrics from an upstream as real evidence.
- Do not activate engineering-ready PRD skills here. Product Definition stays above App Flow and engineering specification.

## Evidence and quality rules

- Labels: OBSERVED, USER-REPORTED, ANALYTICS, SECONDARY SOURCE, INTERPRETATION, HYPOTHESIS, UNKNOWN.
- Link claims to Process 02 evidence IDs wherever available.
- Separate a product decision from a fact about customers.
- Do not claim validation merely because a direction is selected or a product definition is frozen.
- Do not invent customer identities, interviews, market size, competitor capabilities, metrics, baselines, targets, legal conclusions or technical feasibility.
- If a claim needs current research, cite source and date and state limitations.
- A product principle must guide a trade-off. Remove generic slogans.
- A capability is not a UI screen, button, data model or API.
- A metric is not a target unless its baseline, measurement source and rationale are known.
- Respect consent, data minimization and participant privacy.

## Definition of done

A frozen Product Definition must contain:
1. A specific target segment and usage context, with evidence status and limitations.
2. A clear customer problem/job and intended outcome.
3. A concise product positioning and value proposition.
4. A product concept/core mechanism at high-level fidelity.
5. Product principles that guide trade-offs.
6. Capability-level first-release scope plus NOT NOW and OUT boundaries.
7. Leading/lagging success measures with unknown baselines visible.
8. Key decisions, rejected alternatives, dependencies, risks and deferred unknowns.
9. Independent review with no unresolved BLOCKER findings.
10. A recorded human freeze in the canonical control file.

Do not produce App Flow, UX/UI, wireframes, information architecture, design system, detailed PRD, acceptance criteria, API/database architecture, technical implementation plan, tickets or code.
