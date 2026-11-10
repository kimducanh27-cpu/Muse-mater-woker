# PROCESS 02 — TAB 02: CUSTOMER EVIDENCE

Use the active `product-discovery` skill. This must be a fresh conversation in the same workspace.

## Read first

- `product/discovery/00_DISCOVERY_BRIEF.md`
- `product/discovery/01_OPPORTUNITY_MAP.md`
- Any source material the user has supplied (transcripts, notes, survey exports, analytics, support feedback).
- The relevant upstream sources: `interview-script/SKILL.md`, `summarize-interview/SKILL.md`, and the matching `identify-assumptions-*/SKILL.md`.

Do not begin synthesis unless the Opportunity Map records `APPROVE OPPORTUNITY FOCUS`. If missing, stop and identify the blocker.

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
- `OBSERVED`
- `USER-REPORTED`
- `ANALYTICS`
- `SECONDARY SOURCE`
- `INTERPRETATION`
- `HYPOTHESIS`
- `UNKNOWN`

If not yet gathered, mark `NOT COLLECTED`; if source access failed, mark `NOT VERIFIED`.

## Boundaries

No PRD, App Flow, UX/UI, architecture or code. Do not state that a problem is validated when there are no primary data sources. A desk-research report is not a replacement for interviews or observed behavior.

## Output

Create/update:
- `product/discovery/02_INTERVIEW_GUIDE.md`
- `product/discovery/03_EVIDENCE_REGISTER.md`
- `product/discovery/04_INTERVIEW_SYNTHESIS.md` only if actual source data exists
- `product/discovery/05_ASSUMPTION_MAP.md`

State the strongest supporting evidence, strongest counter-evidence, evidence gaps and which decision would change based on the evidence.

Stop and wait for: `APPROVE EVIDENCE SYNTHESIS`.
