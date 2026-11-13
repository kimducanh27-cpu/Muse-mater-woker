# Process 04 — App Flow artifacts

All artifacts for one initiative live in this folder. Initialize `00_APP_FLOW_CONTROL.md` from `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md` (schema version 4). Existing schema-v2 state must not be silently reused; follow the exact migration procedure in the active Skill.

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
| 09_DECISION_LOG.md | Tab 01/02 | Immutable proposals and append-only status events; DLE IDs pair with Control File events |
| 10_CHANGE_REQUEST_REGISTER.md | Tab 01 only | Append-only sole source of CR business state; Register schema v1; paired Control receipts |
| APP_FLOW.md | Tab 03 after explicit freeze command | Canonical frozen output |
| APP_FLOW.v<N>.md | Tab 03 before re-freeze | Immutable archive of a prior frozen version |

Never overwrite a Control File from another initiative. Do not store participant identifiers, private transcripts, credentials or secrets in a public repository.

Process 04 requires a frozen Process 03 Product Definition and matching SHA-256. The authoritative expected hash is Process 03 Control File `gate_3.frozen_artifact.sha256`. Process 04's initiative ID must equal Process 03's initiative ID.

Gate approvals bind exact artifact hashes and event snapshots. Gate 1 and Gate 2 stored Decision Log hashes must equal the snapshots in their corresponding approval events; Gate 2 binds the entire Decision Log hash and any later byte change reopens Gates 2–3. The immutable Decision Log identity header must match this initiative ID. Each proposal/status event must pair one-to-one with a Control File `DECISION_LOG_UPDATED` event; current status is reconstructed by committed `state_seq`, never by editing a proposal. Tab 03 is read-only on Decision Log 09 and Tab 01/02 source artifacts. Review rounds are append-only and use bounded recovery; remediation invalidates affected approvals and requires re-approval plus a new review round. Before Round 1, `07_FLOW_REVIEW.md` must be initialized from its exact template and its SHA-256 bound by `REVIEW_HISTORY_INITIALIZED`. Each round is append-only; interrupted round recovery requires the exact command and preimage checks in the Skill. The frozen output is eligible downstream only when Gate 3 is APPROVED, lifecycle_status is FROZEN, and its actual hash matches the Control File.

## Schema v4 Change Request integrity

`product/app-flow/10_CHANGE_REQUEST_REGISTER.md` is the sole source of truth for CR business state. Initialize it at `register_seq: 0` even with zero CRs and require a non-null verified hash plus `CHANGE_REQUEST_REGISTER_INITIALIZED` receipt. The Control File stores receipts/checkpoints, not per-CR statuses or blocking counts.

Tab 01 is the sole Register writer and CR Coordinator. Tabs 02 and 03 are read-only for CR state. A new CR blocks downstream from `RECORDED`. Freeze is Stage A (Tab 03); post-Freeze closure is Stage B (Tab 01), one event and receipt per CR. Downstream remains blocked until every implementation CR in the Freeze batch is `CLOSED_IMPLEMENTED` against the same frozen version, Gate 3 sequence and APP_FLOW hash. See the canonical Skill for complete requirements.
