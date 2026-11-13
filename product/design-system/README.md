# Process 06 — Design Systems artifacts

All artifacts for one initiative live in this folder. Initialize `00_DS_CONTROL.md` from `templates/06-DESIGN-SYSTEMS/00-DS-CONTROL.md` (schema version 1) only after both sources are verified. There is no predecessor schema and no migration path.

| File | Owner | Purpose |
|---|---|---|
| `00_DS_CONTROL.md` | single writer per tab | Canonical state: platform, gates, sequence, hashes, coverage |
| `01_DESIGN_FOUNDATIONS.md` | Tab 01 | Colour roles, type, spacing, radius, elevation, motion, grid |
| `02_TOKEN_CONTRACT.md` | Tab 02 | Primitive → semantic → component tokens, with forbidden uses |
| `03_COMPONENT_INVENTORY.md` | Tab 02 | Every component with its citing screens |
| `04_COMPONENT_ACCESSIBILITY.md` | Tab 02 | Measured contrast, target size, focus, announcement intent |
| `05_DS_REVIEW.md` | Tab 03 | Append-only independent review history |
| `06_DS_DRAFT.md` | Tab 03 | Complete review-ready candidate |
| `07_DECISION_LOG.md` | Tab 01 / Tab 02 | Immutable proposals and append-only status events |
| `DESIGN_SYSTEM.md` | Tab 03 after explicit freeze | Canonical frozen output |
| `DESIGN_SYSTEM.v<N>.md` | Tab 03 before re-freeze | Immutable archive of a prior frozen version |

Never overwrite a Control File from another initiative. Do not store participant names, chat excerpts or speculative notes.

Process 06 requires a frozen Process 05 UX Spec and an App Flow whose hash matches the one Process 05 recorded. Both are verified at every tab entry.

Gate approvals bind exact artifact hashes and event snapshots. Gate 2 binds the entire Decision Log, so any later byte change reopens Gates 2–3. Tab 03 is read-only on the Decision Log and on artifacts 01–04.

The frozen output is eligible downstream only when Gate 3 is `APPROVED`, `lifecycle_status` is `FROZEN`, and its actual SHA-256 matches the Control File.

## The rule this folder enforces

A component that cites no screen is a component nobody needs. Every entry in `03_COMPONENT_INVENTORY.md` must name the frozen `SCREEN-` IDs that require it, and every frozen screen must cite at least one component or carry a decision explaining why it does not.

That single rule is what keeps a design system from becoming a catalogue of everything the author could imagine — and what keeps Process 07 composing from demand rather than from availability.
