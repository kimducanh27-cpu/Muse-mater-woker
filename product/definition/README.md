# Product Definition artifacts

Artifacts for one initiative live in this folder. Copy the control template before beginning.

| File | Owner tab | Purpose |
|---|---|---|
| 00_PRODUCT_DEFINITION_CONTROL.md | All tabs | Canonical approvals, Process 02 handoff and freeze lifecycle |
| 01_PRODUCT_INTENT.md | Tab 01 | Target segment, job, outcome and strategic choices |
| 02_POSITIONING.md | Tab 01 | Value proposition, alternatives and differentiation |
| 03_PRODUCT_SHAPE.md | Tab 02 | Product concept, core mechanism and principles |
| 04_CAPABILITY_SCOPE.md | Tab 02 | First-release capabilities, NOT NOW and OUT |
| 05_SUCCESS_MEASURES.md | Tab 02 | Leading/lagging measures and data gaps |
| 06_DECISION_LOG.md | Tab 02 | Decisions, rejected options, deferred unknowns and accepted risks |
| 07_DEFINITION_REVIEW.md | Tab 03 | Independent severity-ranked review |
| 08_PRODUCT_DEFINITION_DRAFT.md | Tab 03 | Review-ready draft |
| PRODUCT_DEFINITION.md | Tab 03 after freeze | Canonical frozen product definition |

Never overwrite a control file from another initiative. Do not store raw participant identifiers, private transcripts, credentials or secrets in a public repository.


## Control and integrity requirements

Use the schema-version-2 Control File template. Every approval must be bound to SHA-256 hashes of its approved artifact set. Gate 3 is APPROVED; lifecycle_status is FROZEN only after PRODUCT_DEFINITION.md is written, hashed and read back successfully.

Re-verify Process 02 source hashes at Tab 02, Tab 03 and before freeze. READY FOR TESTING requires the persisted exact command ACCEPT RESIDUAL UNCERTAINTY. Process 02 decisions PIVOT, PAUSE and STOP are not eligible. Tab 03 is read-only on artifacts 01–06 and review rounds are append-only.

Do not use a canonical Product Definition whose hash does not match the Control File. If hashing, timestamp, write or read-back is unavailable, stop with NOT_VERIFIED.
