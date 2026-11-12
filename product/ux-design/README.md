# Process 05 — UX Design artifacts

All artifacts for one initiative live in this folder. Initialize `00_UX_CONTROL.md` from `templates/05-UX-DESIGN/00-UX-CONTROL.md` (schema version 1) only after both sources are verified. There is no predecessor schema and no migration path.

| File | Owner | Purpose |
|---|---|---|
| `00_UX_CONTROL.md` | single writer per tab | Canonical state: gates, sequence, hashes, coverage, review pointer |
| `01_SCREEN_UX_MODEL.md` | Tab 01 | One entry per screen: goal, primary action, hierarchy |
| `02_INTERACTION_PATTERNS.md` | Tab 02 | Named patterns with refusal conditions |
| `03_STATE_EXPERIENCE.md` | Tab 02 | Screen × state: sees, understands, can do, recovery |
| `04_CONTENT_AND_COPY_INTENT.md` | Tab 02 | Required content and message intent, never final copy |
| `05_ACCESSIBILITY_REQUIREMENTS.md` | Tab 02 | Per-screen requirements, not token choices |
| `06_UX_REVIEW.md` | Tab 03 | Append-only independent review history |
| `07_UX_SPEC_DRAFT.md` | Tab 03 | Complete review-ready candidate |
| `08_DECISION_LOG.md` | Tab 01 / Tab 02 | Immutable proposals and append-only status events |
| `UX_SPEC.md` | Tab 03 after explicit freeze command | Canonical frozen output |
| `UX_SPEC.v<N>.md` | Tab 03 before re-freeze | Immutable archive of a prior frozen version |

Never overwrite a Control File from another initiative. Do not store participant names, chat excerpts or speculative notes in these files.

Process 05 requires a frozen Process 04 App Flow and a Product Definition whose hash matches the one Process 04 recorded. Both are verified at every tab entry.

Gate approvals bind exact artifact hashes and event snapshots. Gate 1 and Gate 2 stored Decision Log hashes must equal the snapshots in their approval events. Gate 2 binds the entire Decision Log, so any later byte change reopens Gates 2–3. Tab 03 is read-only on the Decision Log and on artifacts 01–05. Review rounds are append-only and use bounded recovery; remediation invalidates affected approvals and requires re-approval plus a new review round.

The frozen output is eligible downstream only when Gate 3 is `APPROVED`, `lifecycle_status` is `FROZEN`, and its actual SHA-256 matches the Control File.

## The boundary this folder enforces

Nothing here may contain a named UI component, a colour, a typeface, a size, a spacing value, a design token, an image or final copy. Those belong to Processes 06 and 07. A reviewer who finds any of them records a finding rather than fixing it, because fixing it here would move a decision into the wrong process.
