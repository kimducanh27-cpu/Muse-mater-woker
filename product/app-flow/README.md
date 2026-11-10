# Process 04 — App Flow artifacts

All artifacts for one initiative live in this folder. Initialize the Control File from templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md.

| File | Owner | Purpose |
|---|---|---|
| 00_APP_FLOW_CONTROL.md | All tabs | Canonical gates, hashes, lifecycle |
| 01_TASK_MODEL.md | Tab 01 | Actors, goals, tasks and capability traceability |
| 02_FLOW_ARCHITECTURE.md | Tab 01 | Task-to-flow architecture |
| 03_NAVIGATION_MODEL.md | Tab 02 | Navigation nodes and transitions |
| 04_SCREEN_INVENTORY.md | Tab 02 | Functional screen contracts |
| 05_FLOW_SPECIFICATION.md | Tab 02 | Main and alternate task paths |
| 06_STATE_AND_EXCEPTION_MATRIX.md | Tab 02 | System states, failures and recovery |
| 07_FLOW_REVIEW.md | Tab 03 | Independent audit findings |
| 08_APP_FLOW_DRAFT.md | Tab 03 | Review-ready consolidated draft |
| APP_FLOW.md | Tab 03 after freeze | Canonical frozen output |

Never overwrite a Control File from another initiative. Do not store participant identifiers, private transcripts, credentials or secrets in a public repository.

Process 04 requires a frozen Process 03 Product Definition and matching SHA-256. A hash mismatch or unavailable verification blocks progression. Gate approvals bind exact artifact hashes. Tab 03 is read-only on Tab 01/02 artifacts; remediation invalidates affected approvals and requires a new review round.
