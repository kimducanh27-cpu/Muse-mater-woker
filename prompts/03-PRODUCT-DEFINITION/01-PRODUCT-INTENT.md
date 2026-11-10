# PROCESS 03 — TAB 01: PRODUCT INTENT & POSITIONING

Use the active product-definition Skill in a fresh Antigravity conversation. This is Process 03, not Discovery or App Flow.

## Read first
1. product/definition/00_PRODUCT_DEFINITION_CONTROL.md; initialize from the template if missing.
2. The selected Process 02 source Control File, Decision Brief and Outcome when applicable.
3. Discovery Brief, Opportunity Map, Evidence Register, Assumption Map and material cited sources.
4. Existing strategy, constraints or context supplied by the user.

## Handoff gate
Verify route, initiative identity, Gate 3, discovery decision, outcome status and evidence status exactly as specified in the Skill. Eligible decisions are PROCEED or NARROW only. PIVOT, PAUSE, STOP, conflicting states or unreadable sources stop the process.

For READY FOR TESTING, wait for the exact command ACCEPT RESIDUAL UNCERTAINTY. Persist command, timestamp, evidence status and accepted risks before starting Product Intent. Do not infer it.

For an existing product without Process 02, require the exact command USE EXISTING PRODUCT CONTEXT and record/hash the supplied source path. Do not claim Process 02 was completed.

Record Process 02 source paths and SHA-256 hashes in the canonical Control File. Later tabs must re-verify them.

## Work
1. Summarize what Discovery supports, what remains unknown and the opportunity decision.
2. Inherit Process 02's evidence-supported target segment, context, customer job and current alternatives. Record deviations and rationale in the template.
3. Define the product's target segment, customer problem/job and intended outcome. Do not invent personas or validation.
4. Draft and critique positioning: For [segment] who [need], [product] is a [category] that [outcome]. Unlike [alternative], it [credible difference].
5. Compare current alternatives and non-consumption.
6. Identify strategic choices and product-level assumptions.
7. Label unsupported claims HYPOTHESIS / UNKNOWN.
8. Recommend one intent and state the strongest counterargument.

## Boundaries
- No App Flow, screens, wireframes, navigation, UI, design system or UX spec.
- No detailed PRD, user stories, acceptance criteria, API, database or code.
- Do not invent customer quotes, personas, metrics or market claims.
- User approval is a decision, not evidence of demand.
- Ask one high-value question at a time.
- Do not auto-start Tab 02.

## Output
Create/update:
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md

Use templates in templates/03-PRODUCT-DEFINITION/. Include evidence IDs, discovery decision, uncertainty, counterargument, deviations from Process 02 and rejected alternatives.

## Gate 1
Wait for exact command APPROVE PRODUCT INTENT. A revision request must be logged as REVISION_REQUESTED; REJECT PRODUCT INTENT sets the gate to REJECTED.

On approval:
- Compute SHA-256 for both output artifacts.
- Record Gate 1 = APPROVED, exact command, user decision, real local timestamp and approved_artifacts in the Control File.
- Increment state_seq, save, read back and verify the stored hashes.

If hashing, timestamp, write or read-back fails, report NOT VERIFIED and do not start Tab 02. Never start Tab 02 automatically.

## Invalidation
If either approved file changes, reopen Gates 1–3. Apply the Skill's invalidation matrix and append a Control File log entry.
