# PROCESS 03 — TAB 01: PRODUCT INTENT & POSITIONING

Use the active product-definition Skill. This is Process 03, not Product Discovery and not App Flow.

## Read first
1. product/definition/00_PRODUCT_DEFINITION_CONTROL.md; initialize from the template if missing.
2. product/discovery/00_DISCOVERY_CONTROL.md
3. product/discovery/07_DISCOVERY_DECISION.md
4. product/discovery/08_DISCOVERY_OUTCOME.md if present
5. Discovery Brief, Opportunity Map, Evidence Register, Assumption Map and source material needed to trace claims.
6. Existing strategy, constraints or product context supplied by the user.

Verify Process 02 eligibility exactly as defined in the Skill. If Gate 3 is not APPROVED, source state is missing, or the discovery state is ineligible, stop and report the blocker. If only READY FOR TESTING exists, make inherited uncertainty visible and obtain explicit user acceptance before shaping.

## Your role
Act as a Product Definition sparring partner. Make the product's purpose and value proposition concrete; do not turn Discovery into a feature wishlist.

## Process
1. Summarize what Process 02 supports, what remains unknown and what decision was made.
2. Define the primary target segment and context using evidence, not a synthetic persona.
3. State the customer's job/problem and the outcome the product aims to change.
4. Draft and critique the positioning statement: For [segment] who [need], [product] is a [category] that [outcome]. Unlike [alternative], it [credible difference].
5. Compare the proposed direction with current alternatives and non-consumption.
6. Identify the few strategic choices that determine what this product is and is not.
7. Label unsupported differentiation or market claims HYPOTHESIS / UNKNOWN.
8. Recommend one product intent and show the strongest counterargument.

## Boundaries
- No App Flow, screens, wireframes, navigation, UI, design system or UX spec.
- No detailed PRD, user stories, acceptance criteria, API, database or code.
- Do not invent customer quotes, personas, metrics or market claims.
- User approval is a decision, not evidence of demand.
- Ask one high-value question at a time. Do not send a long questionnaire.
- Do not auto-start Tab 02.

## Output
Create/update:
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md

Use templates in templates/03-PRODUCT-DEFINITION/. Include Process 02 evidence IDs, decision source, uncertainty, counterargument and rejected alternatives.

## Gate 1
Stop and wait for exact command: APPROVE PRODUCT INTENT.

On receipt, update product/definition/00_PRODUCT_DEFINITION_CONTROL.md:
- Gate 1 = APPROVED
- exact command and user decision
- local timestamp (Asia/Ho_Chi_Minh)
- artifact revision/path

Do not say Gate 1 passed until the control file is saved successfully. Never start Tab 02 automatically.
