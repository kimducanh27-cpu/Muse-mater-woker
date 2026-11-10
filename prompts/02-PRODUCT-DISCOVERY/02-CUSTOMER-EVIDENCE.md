# PROCESS 02 — TAB 02: CUSTOMER EVIDENCE

Use the active product-discovery Skill. This must be a fresh conversation in the same workspace.

## Read first

- product/discovery/00_DISCOVERY_CONTROL.md
- product/discovery/00_DISCOVERY_BRIEF.md
- product/discovery/01_OPPORTUNITY_MAP.md
- Any source material supplied by the user (transcripts, notes, survey exports, analytics, support feedback).
- Relevant upstream sources: interview-script/SKILL.md, summarize-interview/SKILL.md, and the matching identify-assumptions-*/SKILL.md.

## Entry gate

Before doing research work, verify that Gate 1 is APPROVED in the control file for this initiative. If it is missing, PENDING, REJECTED or REOPENED, stop and identify the blocker. Do not rely on a phrase in chat or the opportunity map alone.

## Research tasks

1. Identify the claims that need direct customer evidence.
2. If interviews have not happened, create a focused interview guide using Mom Test principles: recent concrete past behavior, actual workarounds, time/money/effort invested, prior attempts and consequences. Avoid pitching or leading questions.
3. If source interviews/data are provided, read them before summarizing. Keep the exact sample count and context. Anonymize participants.
4. Build an evidence register. Every important insight must link to a source or be labeled as an interpretation/hypothesis.
5. Look for disconfirming evidence, contradictions, selection bias, missing segments and alternative explanations.
6. Map risks relevant to this product: Value, Usability, Feasibility, Viability; for a new product also consider ethics, go-to-market, strategic and team risks if applicable.
7. Never invent participants, quotes, metrics, survey responses, sample size, source URLs or research outcomes.

## Evidence labels

Use only:
- OBSERVED
- USER-REPORTED
- ANALYTICS
- SECONDARY SOURCE
- INTERPRETATION
- HYPOTHESIS
- UNKNOWN

If not yet gathered, mark NOT COLLECTED; if source access failed, mark NOT VERIFIED.

Set the control file's evidence_status accurately:
- PRIMARY_EVIDENCE_PRESENT: real first-hand customer behavior/interviews or first-party product analytics were supplied and inspected.
- SECONDARY_ONLY: only desk research or other second-hand sources are available.
- NOT_COLLECTED: no usable evidence has been supplied or collected.

An interview guide, AI persona, hypothetical answer or planned interview is not primary evidence.

## Boundaries

No PRD, Product Definition, App Flow, UX/UI, architecture or code. Do not state that a problem or solution is validated when there are no suitable primary data sources. A desk-research report is not a replacement for interviews or observed behavior.

## Output

Create/update:
- product/discovery/02_INTERVIEW_GUIDE.md
- product/discovery/03_EVIDENCE_REGISTER.md
- product/discovery/04_INTERVIEW_SYNTHESIS.md only if actual source data exists
- product/discovery/05_ASSUMPTION_MAP.md

State the strongest supporting evidence, strongest counter-evidence, evidence gaps and which decision would change based on the evidence. If no primary evidence exists, describe this as an evidence gap and research plan, not a validation result.

## Gate 2 — Evidence Review

Stop and wait for the exact command: APPROVE EVIDENCE REVIEW.

When received:
1. Update Gate 2 in product/discovery/00_DISCOVERY_CONTROL.md to APPROVED.
2. Preserve evidence_status as PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY or NOT_COLLECTED. Gate approval must never upgrade evidence quality.
3. Record the exact command, user decision and local timestamp (Asia/Ho_Chi_Minh).
4. Add a log entry. Do not claim Gate 2 passed until the file is saved successfully.

Gate 2 approves the evidence review and the documented gaps; it does not mean the problem is validated. Never start Tab 03 automatically.
