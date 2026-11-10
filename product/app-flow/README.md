# Process 04 — App Flow artifacts

All artifacts for one initiative live in this folder. Initialize `00_APP_FLOW_CONTROL.md` from `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md` (schema version 3). Existing schema-v2 state must not be silently reused; follow the exact migration procedure in the active Skill.

| File | Owner | Purpose |
|---|---|---|
| 00_APP_FLOW_CONTROL.md | All tabs | Canonical gates, source binding, hashes, review/lifecycle state |
| 01_TASK_MODEL.md | Tab 01 | Actors, goals, tasks and bidirectional capability coverage |
| 02_FLOW_ARCHITECTURE.md | Tab 01 | Task-to-flow architecture |
| 03_NAVIGATION_MODEL.md | Tab 02 | Navigation nodes, transitions, reachability |
| 04_SCREEN_INVENTORY.md | Tab 02 | Functional screen contracts and screen/node set |
| 05_FLOW_SPECIFICATION.md | Tab 02 | Main, alternate and recovery paths |
| 06_STATE_AND_EXCEPTION_MATRIX.md | Tab 02 | System states, failures and recovery |
| 07_FLOW_REVIEW.md | Tab 03 | Append-only independent review history |
| 08_APP_FLOW_DRAFT.md | Tab 03 | Complete review-ready canonical content candidate |
| 09_DECISION_LOG.md | Tab 01/02 | Append-only material decisions; exact user approval required |
| APP_FLOW.md | Tab 03 after explicit freeze command | Canonical frozen output |
| APP_FLOW.v<N>.md | Tab 03 before re-freeze | Immutable archive of a prior frozen version |

Never overwrite a Control File from another initiative. Do not store participant identifiers, private transcripts, credentials or secrets in a public repository.

Process 04 requires a frozen Process 03 Product Definition and matching SHA-256. The authoritative expected hash is Process 03 Control File `gate_3.frozen_artifact.sha256`. Process 04's initiative ID must equal Process 03's initiative ID.

Gate approvals bind exact artifact hashes. Gate 1 snapshots the Decision Log hash at approval; Gate 2 binds the entire Decision Log hash and any later byte change reopens Gates 2–3. The immutable Decision Log identity header must match this initiative ID. Tab 03 is read-only on Tab 01/02 source artifacts; remediation invalidates affected approvals and requires re-approval and a new review round. The frozen output is eligible downstream only when Gate 3 is APPROVED, lifecycle_status is FROZEN, and its actual hash matches the Control File.
