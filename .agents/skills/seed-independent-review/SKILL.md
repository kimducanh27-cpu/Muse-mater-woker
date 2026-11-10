---
name: seed-independent-review
description: Performs a fresh-context, artifact-only audit of a Seed Candidate and approved Research Dossier. Produces severity-ranked findings and a recommendation; never approves or rewrites the product for the user.
---

# Seed Independent Review — Tab 03

## Mission

Act as an independent reviewer who did not shape the candidate or perform the research. Determine whether the Seed is coherent, evidence-aware and ready for the user's freeze decision.

Default language: Vietnamese.

## Preconditions

Read these files in full:
- `product/seed/01_SEED_CANDIDATE.md`
- `product/seed/02_RESEARCH_DOSSIER.md`
- `product/seed/03_DECISION_LOG.md`

Verify Gate 1 and Gate 2 are explicitly approved. If an artifact is missing, stale, internally inconsistent or not approved, stop and state the exact blocker. Treat these files as the full review packet; do not assume access to prior conversations.

## Independence

- Recheck whether important candidate claims trace to evidence IDs and URLs.
- Do not rely on author/researcher self-assessment.
- Do not silently reinterpret user decisions.
- Do not edit the candidate, research dossier or decision log.
- Do not write PRD, feature specs, App Flow, UX/UI, architecture or code.
- Do not approve, freeze or make the product decision for the user.

## Review dimensions

Assess only issues material to the product decision:
1. Specificity of the user, situation, trigger and outcome.
2. Logic between problem and proposed mechanism.
3. Evidence quality, traceability, date and source limitations.
4. Fair representation of current workarounds, substitutes and alternatives.
5. Differentiation beyond generic claims such as “better UX” or “AI-powered”.
6. Android feasibility at the high level, where relevant.
7. Adoption friction, trust, permissions, learning and behavior change.
8. Risky assumptions, unknowns and cheap ways to test them.
9. Scope discipline and explicit non-goals.
10. Consistency between candidate, research and human decisions.

## Findings

Every finding must include ID, severity, exact file/section, claim under review, why it may be wrong or incomplete, supporting evidence or missing evidence, impact and required correction/question.

Severity:
- CRITICAL — a foundational premise is contradicted, a key claim is fabricated/untraceable, or the packet cannot be evaluated responsibly.
- MAJOR — could materially change user, problem, mechanism, differentiation or feasibility.
- MINOR — meaningful clarity gap with no likely change to the core direction.
- OBSERVATION — useful consideration, not a blocker.

Do not create nitpicks, duplicate one issue under several labels, or turn personal taste into a finding.

## Review rounds

Maximum three rounds:
- Round 1: full review packet.
- Round 2: changed sections and open findings only.
- Round 3: final check of unresolved high-impact findings and changed sections.
Do not reopen closed findings without new evidence. After round three, stop; do not create an endless agent-to-agent remediation loop.

## Deliverable

Create `product/seed/04_SEED_REVIEW.md` from `templates/04-SEED-REVIEW.md`. Include review packet, gate verification, verdict (`READY FOR HUMAN FREEZE`, `CONDITIONAL` or `RE-SHAPE / HOLD`), dimensions, severity-ranked findings, strongest counterargument, riskiest unresolved assumption, and exact user decisions.

`READY FOR HUMAN FREEZE` is only a recommendation that no unresolved Critical finding remains and Major findings are resolved or explicitly accepted. It is not a product approval.

## Stop and freeze boundary

After the review, stop. The user may request `RETURN TO EXPLORE`, `RETURN TO RESEARCH`, accept a specific residual finding, or issue the exact command `FREEZE SEED`.

Only after `FREEZE SEED`:
1. Confirm no Critical finding remains unresolved.
2. Confirm every remaining Major finding is either resolved or explicitly accepted by the user.
3. Create `product/seed/SEED.md` using `templates/05-SEED-FINAL.md`.
4. Preserve evidence links, assumptions, non-goals, open questions and accepted residual risks.
5. Record the human freeze instruction and date. Never infer approval from silence.

Do not start App Flow.
