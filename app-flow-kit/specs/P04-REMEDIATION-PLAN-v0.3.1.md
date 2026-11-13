# PROCESS 04 — REMEDIATION PLAN v0.3.1

## Cross-Process Change Management Contract

| Field                              | Value                                                                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Document ID                        | `P04-REMEDIATION-PLAN`                                                                                                       |
| Version                            | `0.3.1`                                                                                                                      |
| Status                             | `DRAFT_FOR_OWNER_DECISION — HOLD`                                                                                            |
| Applies to                         | Process 04 — App Flow                                                                                                        |
| Repository reference               | `kimducanh27-cpu/app-adr-ui`                                                                                                 |
| Baseline cited by Round 2 reviewer | `main` @ `99ac2c629a5e3ecc53e45f2b923163b0593d5b6a`                                                                          |
| Approval authority                 | Repository Owner                                                                                                             |
| Implementation authority           | Not granted by this document                                                                                                 |
| Change mode                        | Specification only; no repository changes made                                                                               |
| Corrects                           | Process 04 Remediation Plan v0.3, limited to D3-01 (abort-pair/hash-chain semantics) and D3-02 (Phase 0 clarification count) |

> **Current decision: HOLD.** This document is a narrowly scoped micro-diff correction to v0.3 for D3-01 and D3-02. It does not authorize implementation, migration, branch creation, commits, pull requests, or changes to `main`. All ADR and CL owner decisions remain `PENDING` until explicitly approved by the repository owner.

---

## 0. Document purpose and decision rules

### 0.0.1 v0.3.1 micro-diff boundary

This revision changes only the following v0.3 locations: document version metadata; Sections 4.1, 4.4, 5.2, 5.4, 5.5, 5.6, and 5.7; the abort-pair test expectation in Section 15; the Phase 0 clarification count in Section 16; the CL-01 wording in Section 17.1; and the change log/provenance/review notes. These edits address D3-01 and D3-02 from the v0.3 diff review. All other v0.3 policy content is carried forward unchanged.

This version is a narrowly scoped correction to v0.3. It resolves only D3-01 (the abort-pair receipt/hash-chain boundary) and D3-02 (the Phase 0 clarification count). It does not reopen the full P04 architecture review, change the NF-01…NF-12 dispositions, or grant implementation authority.

### 0.1 Normative language

- **MUST / MUST NOT**: mandatory requirement for an implementation to pass review.
- **SHOULD / SHOULD NOT**: recommended unless the Owner records an explicit rationale for deviation.
- **MAY**: optional behavior.
- **HOLD**: implementation is prohibited until all release criteria are met.
- **NOT_VERIFIED**: integrity cannot be established; fail closed.
- **NOT RUN**: a runtime test has not actually been executed and evidenced.

### 0.2 Source-of-truth hierarchy

1. The approved version of `.agents/skills/app-flow/SKILL.md` is the canonical P04 process contract.
2. Templates define the serialized shape of P04 artifacts and MUST agree with the Skill.
3. Prompts define tab-specific execution instructions and MUST reference the Skill rather than independently redefining business rules.
4. README and checklist files are operator-facing indexes and MUST describe the same paths, versions, ownership, and gates; they MUST NOT create a competing policy.
5. The P04 Change Request Register is the sole source of truth for CR business state.
6. The P04 Control File is the source of committed sequence, receipts, integrity checkpoints, Gate state, and frozen-output binding. It MUST NOT duplicate a per-CR business-status table.
7. The Decision Log remains append-only. The Control File's `DECISION_LOG_UPDATED` event is the commit receipt and sequence anchor; the Decision Log body MUST NOT contain a predicted or committed Control File sequence.
8. P03 remains an external upstream source. P04 reads and verifies the actual P03 v2 fields; P04 MUST NOT rewrite or upgrade P03 as part of this remediation.

If two artifacts disagree, the canonical contract wins for interpretation, but the workspace is `NOT_VERIFIED` until the inconsistent artifact is corrected through an approved change. Readers MUST NOT silently choose one copy and continue.

---

## 1. Executive disposition

### 1.1 Round 2 verdict

**HOLD — v0.2 is not implementation-ready.** Round 2 identified five P0 findings and seven P1/P2 findings:

| Finding | Severity | Required disposition in v0.3                                                                                                                             |
| ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NF-01   | P0       | Remove predicted Control sequence from Register events; define deterministic recovery and abort handling for a staged tail.                              |
| NF-02   | P0       | Define canonical bytes and complete prefix-chain verification from the initialization anchor through the last committed event.                           |
| NF-03   | P0       | Remove `control_state_seq` from Decision Log event bodies; retain Control File receipt as the sole committed sequence anchor.                            |
| NF-04   | P0       | Make all legal CR transitions explicit, including reopen and reversion paths, exact commands, evidence, permissions, receipt, Gate effect, and recovery. |
| NF-05   | P0       | Close the Freeze-to-CR-closure publication gap; downstream remains blocked until every CR for the freeze batch is closed and verified.                   |
| NF-06   | P1       | Initialize the Register at workspace creation and migration, including a non-null hash anchor when there are zero CRs.                                   |
| NF-07   | P1       | Make on-disk Gate approval events the only cross-tab handoff evidence.                                                                                   |
| NF-08   | P1       | Add a no-upstream-change resolution for P03 returns and bind every return to its own P03 hash snapshot.                                                  |
| NF-09   | P1       | Define safe v3→v4 migration, explicit attestation about unrecorded CRs, backup manifest, and inherited-freeze behavior.                                  |
| NF-10   | P1       | Validate duplicate/supersession/dependency graph targets and reject cycles before append.                                                                |
| NF-11   | P2       | Define deterministic `frozen_version` increment and prohibit no-op re-freeze.                                                                            |
| NF-12   | P2       | Upgrade `product/app-flow/README.md` from SHOULD CHANGE to MUST CHANGE.                                                                                  |

### 1.2 Round 1 closure status retained

The following Round 1 topics remain resolved or partially resolved as reported by the reviewer. They MUST be rechecked against the implementation diff during Phase 6; this document does not convert a prior paper assessment into a runtime pass.

| Round 1 topic                | Round 2 status                       | v0.3 treatment                                                                      |
| ---------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------- |
| Decision Log enum mismatch   | Partially resolved; NF-03 regression | Fix the token mismatch; do not embed Control sequence in the Decision Log.          |
| Dual CR state source         | Resolved                             | Register owns CR state; Control File keeps pointers and receipts only.              |
| Register/Control consistency | Partially resolved                   | Replace v0.2 transaction design with Section 5.                                     |
| Submission boundary          | Resolved                             | P03 and downstream submit immutable payloads; they do not write P04 files.          |
| CR-ID ownership              | Resolved                             | Tab 01 alone assigns CR-ID after intake validation.                                 |
| Incomplete state machine     | Not resolved                         | Use Section 7 and transition contract T01–T18.                                      |
| REFROZEN ambiguity           | Resolved                             | No CR state named `REFROZEN`; use `CLOSED_IMPLEMENTED` and explicit freeze binding. |
| Rejection semantics          | Resolved                             | Rejection only removes its own blocking obligation, after proof of no byte change.  |
| Gate/downstream mixing       | Resolved                             | Gate validity and downstream eligibility are separate calculations.                 |
| P03 re-entry                 | Partially resolved                   | Use T08/T09 and per-CR return snapshots.                                            |
| SHA-256 semantic confusion   | Resolved                             | Hash proves byte identity only, not semantic equivalence.                           |
| v3 compatibility             | Partially resolved                   | Use Section 10 migration rules.                                                     |
| Tab write contention         | Partially resolved                   | Enforce one logical writer and disk-based handoff; no claim of OS-level lock/CAS.   |
| Template/active path mapping | Resolved                             | Preserve the exact path mapping in Section 3.                                       |
| Documentation duplication    | Partially resolved                   | Canonical rules live in Skill; all README files are mandatory synchronized indexes. |
| P03 schema compatibility     | Resolved                             | P03 stays schema v2; read only fields that actually exist.                          |
| Post-freeze CR closure       | Not resolved                         | Close through the publication contract in Section 9.                                |

---

## 2. Scope, ownership, and exclusions

### 2.1 P04 owns

Process 04 owns functional task/flow architecture, navigation, functional `SCREEN-ID` inventory, transitions, functional states, exceptions, recovery, and the frozen App Flow contract. The P04 CR mechanism governs requests that seek to change those P04-owned artifacts.

### 2.2 P04 does not own

P04 MUST NOT define or modify visual design decisions, wireframes, typography, color systems, API architecture, database architecture, implementation code, or the internal policies of downstream processes unless the Owner explicitly expands P04 scope.

P04 MUST NOT modify:

- `templates/03-PRODUCT-DEFINITION/*`
- `prompts/03-PRODUCT-DEFINITION/*`
- `.agents/skills/product-definition/SKILL.md`
- `product-definition-kit/*`

P03 remains `schema_version: 2`. P04 must not invent a P03 field named `gate_3.approved_state_seq`; the Round 2 baseline states that this field does not exist in P03 v2.

P05 and Processes 01, 02, 06, and 07 are outside this remediation scope. P04 may publish evidence for downstream consumption but MUST NOT prescribe unapproved downstream design policy.

### 2.3 Submission boundary

P03 or a downstream process may prepare and submit an immutable change-request payload. It MUST NOT write directly to P04's Control File, Register, Decision Log, review history, or functional artifacts. The user carries the payload to Tab 01. Tab 01 verifies source identity, source hashes, initiative binding, duplicate fingerprint, and then assigns the P04 CR-ID.

---

## 3. Repository baseline and canonical paths

### 3.1 Baseline facts from the Round 2 packet

The uploaded Round 2 review reports that the repository snapshot `app-adr-ui-main6.zip` matched:

- Repository: `kimducanh27-cpu/app-adr-ui`
- Branch: `main`
- HEAD: `99ac2c629a5e3ecc53e45f2b923163b0593d5b6a`
- P03 Control Template: `schema_version: 2`
- P04 Control Template: `schema_version: 3`

These are **packet-reported baseline facts**, not a fresh verification of the current remote repository in this task. Before implementation, the implementer MUST fetch and verify the actual target branch HEAD and all affected paths again.

### 3.2 Template-to-working-file mapping

Template numbering is local to `templates/04-APP-FLOW/`; it is not the working-artifact number. Preserve these exact mappings:

| Template                                              | Working artifact / purpose                              |
| ----------------------------------------------------- | ------------------------------------------------------- |
| `templates/04-APP-FLOW/10-DECISION-LOG.md`            | `product/app-flow/09_DECISION_LOG.md`                   |
| `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` | `product/app-flow/10_CHANGE_REQUEST_REGISTER.md`        |
| `templates/04-APP-FLOW/08-APP-FLOW-DRAFT.md`          | `product/app-flow/08_APP_FLOW_DRAFT.md`                 |
| `templates/04-APP-FLOW/09-APP-FLOW.md`                | Frozen-output schema for `product/app-flow/APP_FLOW.md` |

The mapping `11-CHANGE-REQUEST-REGISTER.md` → `10_CHANGE_REQUEST_REGISTER.md` is intentional and MUST NOT be renumbered to match template numbering.

### 3.3 Canonical P04 files

| Path                                                  | Role                           | Owner                           |
| ----------------------------------------------------- | ------------------------------ | ------------------------------- |
| `.agents/skills/app-flow/SKILL.md`                    | Canonical P04 process contract | Process 04                      |
| `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md`        | Control File schema v4         | Tab 01/02/03 by event ownership |
| `templates/04-APP-FLOW/10-DECISION-LOG.md`            | Decision Log template          | Tab 01/02 by Gate ownership     |
| `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` | CR Register schema             | Tab 01 only writer              |
| `templates/04-APP-FLOW/07-FLOW-REVIEW.md`             | Review rounds and CR snapshot  | Tab 03                          |
| `prompts/04-APP-FLOW/01-TASK-MODEL.md`                | Tab 01 prompt                  | Tab 01                          |
| `prompts/04-APP-FLOW/02-NAVIGATION-FLOW.md`           | Tab 02 prompt                  | Tab 02                          |
| `prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md`        | Tab 03 prompt                  | Tab 03                          |
| `app-flow-kit/README.md`                              | Kit guide                      | Documentation                   |
| `app-flow-kit/VERIFICATION-CHECKLIST.md`              | Static and scenario checklist  | Verification                    |
| `product/app-flow/README.md`                          | Active workspace guide         | Documentation                   |
| `README.md`                                           | Repository-level process index | Documentation                   |
| `product/app-flow/00_APP_FLOW_CONTROL.md`             | Active Control File            | Tab 01/02/03 by event ownership |
| `product/app-flow/09_DECISION_LOG.md`                 | Active Decision Log            | Tab 01/02 by Gate ownership     |
| `product/app-flow/10_CHANGE_REQUEST_REGISTER.md`      | Active CR Register             | Tab 01 only writer              |
| `product/app-flow/APP_FLOW.md`                        | Frozen App Flow output         | Tab 03 freeze executor          |

---

## 4. Canonical state and data model

### 4.1 Separation of business state and commit evidence

The following concepts MUST remain distinct:

1. **Register event exists**: a `### CRE-<NNNN>` block is present in the Register. Existence alone does not make it effective.
2. **Register event is structurally valid**: required fields, initiative binding, event identity, `register_seq`, transition legality, and prefix hash are valid.
3. **Register record is accounted by a matching receipt**: a normal event is accounted by exactly one `CHANGE_REQUEST_REGISTER_UPDATED` receipt; the two events in an abort unit are accounted together by exactly one `CHANGE_REQUEST_EVENT_ABORTED` receipt.
4. **Register receipt unit is committed**: structural validity, the permitted receipt shape, and complete chain verification from initialization through the current checkpoint all pass. For a normal unit, its business event is effective. For an abort unit, the staged business event is accounted in the immutable history but classified `ABORTED_NOT_EFFECTIVE`; the abort marker is audit-only.
5. **Current CR business state**: reconstructed only from the latest effective, committed state-changing normal event for that CR-ID. Neither member of an abort unit changes CR business state. Current CR business state exists only in the Register.
6. **P04 workspace integrity**: all relevant files, sequences, event receipts, and hashes verify. Otherwise `NOT_VERIFIED`.
7. **Downstream eligibility**: a separate predicate over workspace integrity, all three Gates, lifecycle, frozen artifact, Register chain, and an empty reconstructed blocking-CR set.

The Control File MUST NOT store a second per-CR status table or authoritative copy of `active_blocking_cr_count` / `blocking_cr_ids`. Any such count/list is a derived view and MUST be recomputed from the Register and receipts by every reader.

### 4.2 P04 Control File v4 — required structural changes

The P04 Control File template MUST:

- set `schema_version: 4`;
- remove `change_requests: []`;
- add a `change_request_register` checkpoint containing at minimum:
  - `path: product/app-flow/10_CHANGE_REQUEST_REGISTER.md`
  - `schema_version: 1`
  - `last_verified_sha256`
  - `last_register_seq`
  - `last_event_id`;
- add Control event kinds `CHANGE_REQUEST_REGISTER_INITIALIZED`, `CHANGE_REQUEST_REGISTER_UPDATED`, and `CHANGE_REQUEST_EVENT_ABORTED`;
- support `SCHEMA_MIGRATED` from v3 to v4;
- preserve existing P04 Gate approval fields and `state_seq` semantics, while ensuring all new receipts have strictly increasing unique `state_seq` values;
- define Gate validity independently from downstream eligibility.

`state_seq` is a monotonic stale-read detector and committed event sequence. It is **not** an atomic lock, compare-and-swap operation, filesystem mutex, or distributed lock.

### 4.3 Register v1 — required header and event shape

`10_CHANGE_REQUEST_REGISTER.md` MUST begin with immutable identity fields:

- `Process: 04`
- `Initiative ID: <verified_initiative_id>`
- `Register Schema Version: 1`
- a stable schema/header declaration and serialization rule.

Each appended event MUST contain, as applicable:

- `change_request_event_id: CRE-<NNNN>`
- `change_request_id: CR-<NNN>`
- `register_seq: <1..N>`
- `event_type`
- `from_status` and `to_status` for status transitions
- `exact_user_command`
- `recorded_by_tab: TAB_01`
- `timestamp_local`
- `submission_id` and `submission_payload_sha256` when applicable
- `source_process`, `source_initiative_id`, `source_artifact_path`, `source_artifact_sha256` when applicable
- `affected_gate` and `affected_artifact_paths`
- `control_state_seq_before_append`
- `control_file_sha256_before_append`
- `previous_register_sha256`
- transition-specific evidence fields
- `event_end_marker: END_CRE`.

The Register event MUST NOT contain `planned_control_state_seq`, a predicted committed `control_state_seq`, or `resulting_register_sha256`. The Control File receipt assigns the committed `state_seq` and records the resulting whole-file hash.

### 4.4 Register serialization and hash rules (NF-02)

To remove Windows/Linux line-ending and delimiter ambiguity, the canonical file encoding is:

- UTF-8 without BOM;
- LF (`\n`) line endings only;
- no CR (`\r`) bytes;
- no trailing spaces or tabs on any line;
- exact field names and field order as defined by the approved schema;
- every event ends with `event_end_marker: END_CRE` followed by LF, and event blocks are separated by exactly one blank line;
- the file ends with the canonical line terminator defined by the template.

Readers MUST reject noncanonical serialization instead of silently normalizing the file and accepting a hash that does not match the bytes on disk.

Hash definitions:

- `previous_register_sha256`: SHA-256 of the exact entire Register byte sequence on disk immediately before appending that event.
- `event_block_sha256`: SHA-256 of the exact UTF-8/LF bytes from the first byte of `### CRE-<NNNN>` through the LF after `event_end_marker: END_CRE` (excluding the following blank separator line).
- `resulting_register_sha256`: SHA-256 of the exact entire Register byte sequence after the append, including the canonical separator.
- hashes are lowercase hexadecimal.

**Receipt units and the abort-pair exception:**

1. A **normal commit unit** contains exactly one business Register event at sequence `k` and exactly one `CHANGE_REQUEST_REGISTER_UPDATED` receipt. Its `previous_register_sha256` must equal the last trusted committed Register hash before sequence `k`.
2. An **abort commit unit** contains exactly two consecutive Register events, at sequences `k` and `k+1`: (a) the complete but uncommitted staged business event and (b) its immediately following `CHANGE_REQUEST_EVENT_ABORTED` audit marker. Exactly one `CHANGE_REQUEST_EVENT_ABORTED` Control receipt accounts for this pair. There MUST NOT be a normal `CHANGE_REQUEST_REGISTER_UPDATED` receipt for either member.
3. In an abort unit, the staged event's `previous_register_sha256` equals the trusted committed hash `H(k-1)`. After appending that event and its canonical separator, the reader computes the intermediate hash `H(k)`. The abort marker's `previous_register_sha256` MUST equal this intermediate hash `H(k)`. `H(k)` is an internal hash-chain link only; it is not a committed checkpoint and MUST NOT be published as `last_verified_sha256`.
4. After appending the abort marker and its canonical separator, the reader computes final hash `H(k+1)`. The single abort receipt MUST bind the trusted prior hash `H(k-1)`, staged event ID/sequence/block hash, intermediate hash `H(k)`, abort marker ID/sequence/block hash, final hash `H(k+1)`, and the receipt's Control `state_seq`. The Control Register pointer advances directly from `H(k-1)` to `H(k+1)` and `last_register_seq` advances from `k-1` to `k+1`; there is no committed checkpoint at `k`.
5. The next normal Register event, if any, MUST use `register_seq: k+2` and `previous_register_sha256: H(k+1)`. No reader may treat the staged business event at `k` as an independently committed event.

For every Register sequence covered by the committed history, the reader MUST verify:

1. `register_seq` values are contiguous and each receipt unit has the permitted shape: one event for a normal unit or exactly two events for an abort unit.
2. The first event of each receipt unit links to the previous committed checkpoint (or the initialization hash for the first unit). Within an abort unit only, the second event links to the intermediate hash produced after the first event; that intermediate hash is not a commit checkpoint.
3. Every event-block hash matches the exact event bytes.
4. A normal receipt's `resulting_register_sha256` equals the exact full-file hash after its one event. An abort receipt's `resulting_register_sha256` equals the exact full-file hash after both events.
5. Every normal commit unit has exactly one `CHANGE_REQUEST_REGISTER_UPDATED` receipt; every abort commit unit has exactly one `CHANGE_REQUEST_EVENT_ABORTED` receipt covering both events; no event is double-accounted or left unaccounted.
6. The last receipt agrees with `change_request_register.last_verified_sha256`, `last_register_seq`, and `last_event_id`. For an abort unit, `last_event_id` is the abort marker's CRE-ID.

A reader MUST verify the complete history from the initialization anchor to `last_register_seq`; checking only the final whole-file hash is insufficient. An abort unit commits the audit disposition and bytes of the pair, not the business effect of the original staged transition.

### 4.5 Register initialization (NF-06)

Register initialization is mandatory at Tab 01 workspace initialization, even when there are zero CRs.

Procedure:

1. Verify P03 identity and frozen source using the actual P03 v2 fields.
2. Confirm no existing Register conflicts with the Control File checkpoint.
3. Create `product/app-flow/10_CHANGE_REQUEST_REGISTER.md` from `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md`.
4. Set immutable identity header; no CR event blocks are added.
5. Read the file back and compute `H_init` over its exact bytes.
6. Append `CHANGE_REQUEST_REGISTER_INITIALIZED` to the P04 Control File, anchoring `register_seq: 0`, `last_event_id: INITIALIZATION`, `last_verified_sha256: H_init`, path, schema version, initiative ID, and actual Control `state_seq`.
7. Read both files again and verify the initialization receipt and exact hash before proceeding.

A v4 workspace with zero CRs still MUST have non-null `last_verified_sha256` and `last_register_seq: 0`.

Abnormal cases:

- Register missing and checkpoint null: initialize only at a clean new-workspace boundary, or inside the approved v3→v4 migration transaction.
- Empty 0-byte file: `NOT_VERIFIED`; do not auto-overwrite.
- Header-only file with null checkpoint: may be initialized only if its bytes exactly match the approved template serialization and Initiative ID matches.
- Register contains `CRE` events but Control checkpoint is null: `NOT_VERIFIED`.
- Initiative ID mismatch: `NOT_VERIFIED`; never rebind or edit the header to make it match.
- Register schema mismatch: stop and require a separately approved migration.
- Checkpoint exists but Register is missing: `NOT_VERIFIED`; preserve evidence, invalidate P04 conservatively, and restore only from a trusted backup.

---

## 5. Paired append-and-receipt transaction protocol

### 5.1 Core rule

The Register stores CR business events. The Control File stores the commit receipt and current verified checkpoint. A CR state transition becomes effective only after the Register event and its matching Control File receipt have both been read back and verified.

### 5.2 Normal commit protocol

This protocol applies to a normal business-state Register event. The two-event abort unit is governed exclusively by Section 5.6. Before any normal write, Tab 01 MUST:

1. Read the current Control File, Register, and relevant artifacts from disk; never use conversation memory as a source of current sequence or hash.
2. Verify the complete Register receipt/hash chain and Control File event sequence.
3. Verify there is no unresolved staged tail or competing writer operation.
4. Reconstruct the CR's current status and validate the requested transition.
5. Recompute all preconditions, source hashes, affected-file hashes, graph constraints, and Gate evidence.
6. Capture `control_state_seq_before_append` and `control_file_sha256_before_append`.
7. Append exactly one canonical Register event with `register_seq = previous + 1`, and without a predicted Control sequence.
8. Read the Register back; verify exact event bytes, previous hash, event hash, resulting full-file hash, sequence continuity, and event schema.
9. Append one `CHANGE_REQUEST_REGISTER_UPDATED` receipt to the Control File using the **next currently available** Control `state_seq`. The receipt MUST bind: initiative ID, CR-ID, CRE-ID, register sequence, previous Register hash, event-block hash, resulting Register hash, and receipt state sequence.
10. Read both files back; verify the normal event-to-receipt one-to-one match, pointer update, full chain, and final hashes. Abort-pair verification MUST use the distinct two-event/one-receipt rule in Sections 4.4 and 5.6.
11. Report success only after read-back verification passes.

There MUST be one logical writer for a transaction. Tab 01 is the sole Register writer. Tab 02 and Tab 03 MUST NOT write Register receipts. This is a workflow ownership rule, not an OS-level lock guarantee.

### 5.3 Recovery when Control state_seq has advanced (NF-01)

A staged Register event MUST NOT reserve or hard-code a future Control `state_seq`. The receipt uses the next available sequence at recovery time.

When one complete staged tail exists but its Control receipt is missing:

1. Stop every other write operation.
2. Verify that the trusted Register prefix hash equals the last committed Control checkpoint.
3. Verify there is exactly one staged event, structurally complete, with a valid event hash and correct next `register_seq`.
4. Re-read the current Control File and confirm the Register pointer still references the same trusted prefix.
5. Re-evaluate all current business preconditions against disk. Do not assume the original transition is still valid merely because the staged bytes are valid.
6. If the transition is still valid, use `RECOVER CHANGE REQUEST EVENT [CRE-ID]` to write the missing receipt at the next available Control sequence. A prior unrelated Control event may consume the previously observed sequence; this does not itself prevent recovery.
7. Read back and verify both files before resuming operations.

This removes the deadlock caused by a `planned_control_state_seq` embedded in the Register. If current business preconditions no longer allow the staged transition, use the abort path in Section 5.6 instead of committing it.

### 5.4 Ambiguous Control File write

If the writer cannot tell whether the Control File receipt was persisted:

- do not append again immediately;
- reopen and read both files;
- if exactly one matching normal receipt exists and every hash/checkpoint matches, treat the normal transaction as committed and do not repeat it;
- if exactly one matching `CHANGE_REQUEST_EVENT_ABORTED` receipt exists and it binds the exact two-event abort unit as specified in Sections 4.4 and 5.6, treat the abort unit as accounted and do not repeat it;
- if no receipt exists and exactly one valid staged business event exists, follow Section 5.3 or begin Section 5.6 after re-evaluating its business precondition;
- if no receipt exists and exactly one complete staged business event plus its immediately following complete abort marker exist, use `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` under Section 5.5; do not append a second abort marker;
- if a duplicate receipt, orphan receipt, malformed Control File, sequence gap, partial event, unexpected tail length, or hash mismatch exists, stop at `NOT_VERIFIED` and restore/forensically reconcile from a trusted backup.

### 5.5 Bounded recovery limits

`RECOVER CHANGE REQUEST EVENT [CRE-ID]` is permitted only for exactly one complete staged business event whose preceding prefix equals the last trusted Register hash, whose next `register_seq` is correct, and whose current business preconditions still pass. It MUST NOT commit an event whose preconditions have become invalid.

`RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` is a separate, narrowly bounded recovery command. It is permitted only when all of the following are true:

1. exactly two complete, consecutive, unreceipted Register events exist after the trusted checkpoint;
2. the first is the staged business event identified by `[STAGED-CRE-ID]`;
3. the second is its immediately following `CHANGE_REQUEST_EVENT_ABORTED` marker and references the first event exactly;
4. the first event links to the last trusted checkpoint, the second links to the computed intermediate hash after the first event, and both event-block hashes and the final Register hash verify;
5. no later Register event exists and no matching abort receipt exists;
6. the current Control File remains structurally valid and its Register pointer still equals the trusted pre-pair checkpoint.

When these preconditions pass, Tab 01 MUST append only the missing `CHANGE_REQUEST_EVENT_ABORTED` receipt at the next currently available Control `state_seq`; it MUST NOT append either Register event again. The receipt MUST bind the complete abort pair as specified in Section 5.6, followed by a full read-back.

Any partial event, malformed abort marker, more than two unreceipted events, missing historical event, invalid sequence gap, changed trusted prefix, malformed Control File, or unrecognized receipt shape MUST be refused. Restore the Register and Control File to the last mutually verified backup; do not truncate or rewrite historical append-only events in place. The sole two-event exception is the exact abort pair defined above.

### 5.6 Abort of a staged event whose business precondition is no longer valid

The abort path MUST preserve the append-only Register and account for the staged bytes without committing the staged business transition. It is a two-event, one-receipt **abort commit unit**, not two independent Register commits.

**Preconditions:**

- exactly one structurally complete staged business event exists at the next `register_seq: k` after the last trusted committed checkpoint;
- no later Register event exists and the staged event has no normal `CHANGE_REQUEST_REGISTER_UPDATED` receipt;
- the staged event's `previous_register_sha256` equals the trusted checkpoint hash `H(k-1)`;
- the current Control File pointer still identifies that same trusted checkpoint;
- re-evaluation against current on-disk state proves that the staged business precondition is no longer valid;
- the event is not itself an earlier committed event and is eligible for this bounded abort protocol.

**Append and receipt procedure:**

1. Tab 01 preserves the staged event at sequence `k` exactly as written. It MUST NOT edit, remove, renumber, or rewrite it.
2. Compute the intermediate hash `H(k)` over the exact Register bytes after the staged event and its canonical separator. This intermediate hash MUST be retained as evidence for the abort marker and receipt but MUST NOT be written as a Control checkpoint or treated as a committed Register state.
3. Append one new audit event at `register_seq: k+1`, with a new CRE-ID, `event_type: CHANGE_REQUEST_EVENT_ABORTED`, and `previous_register_sha256: H(k)`. The marker MUST identify the staged CRE-ID, staged CR-ID, staged `event_block_sha256`, `H(k-1)`, `H(k)`, and an explicit abort rationale. It MUST NOT describe a CR business-state transition. Its own event block ends with the canonical `event_end_marker: END_CRE`.
4. Compute final hash `H(k+1)` over the entire Register after the abort marker and its canonical separator.
5. Append exactly one `CHANGE_REQUEST_EVENT_ABORTED` receipt to the Control File at the next currently available Control `state_seq`. The receipt MUST bind at least: `initiative_id`; `receipt_type`; `first_register_seq: k`; `last_register_seq: k+1`; staged CRE-ID and CR-ID; abort-marker CRE-ID; trusted prior hash `H(k-1)`; staged event-block hash; intermediate Register hash `H(k)`; abort-marker event-block hash; final Register hash `H(k+1)`; `status_effect: NONE`; and the committed Control `state_seq`.
6. The Control File Register checkpoint advances directly from `(k-1, H(k-1))` to `(k+1, H(k+1))`. It MUST set `last_register_seq: k+1`, `last_event_id` to the abort-marker CRE-ID, and `last_verified_sha256: H(k+1)`. There is no independently committed checkpoint for sequence `k`.
7. Read both files back. Verify the exact staged event bytes, the internal hash edge `H(k-1) → H(k) → H(k+1)`, both event-block hashes, the single abort receipt, the final Register pointer, and all earlier receipt units. Only after all checks pass may the workspace return to `VERIFIED`.

**Deterministic reconstruction:**

- The original staged business event at sequence `k` is retained in history and classified `ABORTED_NOT_EFFECTIVE`. It MUST NOT change the CR's business state.
- The abort marker at sequence `k+1` is an audit event only and MUST NOT change the CR's business state.
- The prior committed CR state remains authoritative.
- The pair is accounted for by one abort receipt; no normal `CHANGE_REQUEST_REGISTER_UPDATED` receipt may exist for either member.
- The next event, if any, starts at sequence `k+2` and links from `H(k+1)`.

**Interrupted abort handling:**

- If interruption occurs before the abort-marker append has begun, the Register still contains only the one complete staged business event. Re-open the files and restart this Section 5.6 only after rechecking all preconditions.
- If interruption occurs during the abort-marker append and leaves partial/malformed bytes, the Register is `NOT_VERIFIED`; preserve evidence and restore from the last mutually verified backup. Do not append a second marker after a partial marker.
- If the abort marker is complete but the Control receipt is absent, do not append another marker. Run `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` under Section 5.5; it validates the exact pair and writes only the missing receipt.
- If the Control receipt may have been written but acknowledgement was lost, re-read both files. If the exact abort receipt and all bindings verify, treat the abort unit as complete and do not duplicate it.

If the staged tail cannot be proven to descend from the trusted prefix, is more than one event long before the abort marker is added, or fails any pair validation, this abort protocol is not permitted. Owner approval is required for this explicit exception to the ordinary one-event/one-\`CHANGE_REQUEST_REGISTER_UPDATED\` receipt rule.

### 5.7 Integrity failure policy

Any of the following means `NOT_VERIFIED` and fail closed: missing/duplicate receipt outside the bounded recovery cases in Sections 5.4–5.5, wrong initiative, wrong CR-ID, incorrect event-block hash, incorrect resulting hash, sequence gap, stale rollback, modified historical event, noncanonical serialization, broken prefix chain, more than two unreceipted tail events, an unrecognized two-event tail, or an untrusted Control File. An exact two-event abort pair with its receipt missing is `NOT_VERIFIED / ABORT_RECEIPT_PENDING` and may proceed only through `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]`; it is not eligible for ordinary writes.

When the Register is not verified, all ordinary P04 writes, Gate approvals, Freeze, and downstream consumption are prohibited. Only the narrowly bounded recovery command expressly allowed by Sections 5.3 or 5.5 may run. Preserve evidence before attempting recovery.

---

## 6. Decision Log pairing and legacy compatibility (NF-03)

### 6.1 Exact isolated template correction

In `templates/04-APP-FLOW/10-DECISION-LOG.md`, correct the deterministic reconstruction token:

- incorrect: `decision_event_kind: STATUS_CHANGED`
- canonical: `decision_event_kind: DECISION_STATUS_CHANGED`

Do not use substring replacement. The correction must not produce `DECISION_DECISION_STATUS_CHANGED`.

### 6.2 No Control sequence in Decision Log body

The Decision Log MUST NOT embed a predicted or committed `control_state_seq` in event bodies. This preserves v3 `DLE-<NNNN>` records and avoids a second sequence reservation problem.

The Control File's `DECISION_LOG_UPDATED` event is the sole commit receipt and MUST bind, at minimum:

`initiative_id`, `decision_id`, `decision_log_event_id`, `decision_event_kind`, `decision_status_before_update`, `decision_status_after_update`, `affected_gate`, `path`, `resulting_sha256`, and `state_seq`.

If optional pre-append diagnostics are desired in a new v4 record, use only `Control File state_seq before append`; do not require it for legacy records.

### 6.3 Legacy events

Historical Decision Log bytes MUST NOT be rewritten as part of migration. A record whose event type or status cannot be deterministically paired is marked `LEGACY_UNVERIFIED` for reconstruction purposes and MUST NOT be treated as a currently approved decision. This does not authorize silently rewriting its bytes or changing historical Control receipts.

---

## 7. Change Request state machine

### 7.1 Canonical states (13)

| State                            | Meaning                                                                                               | Blocking by default?                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `RECORDED`                       | Immutable submission accepted into P04 intake; not yet triaged.                                       | Yes                                      |
| `TRIAGE`                         | Tab 01 is classifying ownership, scope, affected Gates, conflicts, and dependencies.                  | Yes                                      |
| `NEEDS_CLARIFICATION`            | More information is required before a decision.                                                       | Yes                                      |
| `ACCEPTED_FOR_IMPLEMENTATION`    | Owner accepted the defined P04 scope; implementation may proceed under assigned tab permissions.      | Yes                                      |
| `IMPLEMENTED_PENDING_REAPPROVAL` | Changes are recorded and affected Gate 1/2 approvals have been renewed; Tab 03 review/freeze remains. | Yes                                      |
| `RETURN_TO_P03`                  | The request crosses P04 ownership and has been returned to upstream Process 03.                       | Yes                                      |
| `REVERSION_PENDING`              | User requested cancellation after bytes changed; restoration and re-approval remain incomplete.       | Yes                                      |
| `REJECTED_WITH_NO_CHANGE`        | Rejected in TRIAGE with proof that no relevant P04 bytes changed.                                     | No                                       |
| `CANCELLED_NO_CHANGE`            | Cancelled before implementation, or accepted but proven to have changed no bytes.                     | No                                       |
| `CANCELLED_AFTER_REVERSION`      | Changes were reverted and required Gate/Review/Freeze approvals were restored.                        | No                                       |
| `CLOSED_IMPLEMENTED`             | Implemented CR is bound to one exact frozen version/hash and is terminal.                             | No, once bound to a valid current freeze |
| `DUPLICATE`                      | Pointer-terminal state delegating the blocking obligation to a canonical CR.                          | Derived from target                      |
| `SUPERSEDED`                     | Pointer-terminal state delegating the blocking obligation to an approved successor CR.                | Derived from target                      |

`NOT_VERIFIED` is not a business state transition. It is a derived integrity condition and always blocks.

`REFROZEN` is prohibited. A closed CR binds to one freeze only. A later change requires a new CR-ID.

### 7.2 Closed transition set

Only T01–T18 below are legal in the reviewed 18-transition model. Any unlisted `from_status → to_status` pair is forbidden (fail closed). The table is the complete transition contract and carries the 11 required dimensions: ID, states, actor, exact command, machine preconditions, evidence, permissions, Register event, Control receipt, Gate effect, and bounded recovery.

| ID  | From → To                                                                                                                                                              | Actor  | Exact user command                                         | Machine-checkable preconditions                                                                                                                                         | Required evidence                                                                   | Write permission                                                             | Register event / Control receipt                                                      | Gate and downstream effect                                                                                                                             | Bounded recovery                                                                 |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| T01 | Submission → `RECORDED`                                                                                                                                                | Tab 01 | `RECORD APP FLOW CHANGE SUBMISSION [SUBMISSION-ID]`        | Control + Register `VERIFIED`; submission ID and payload hash are new; initiative matches.                                                                              | Submission ID/hash, source path/hash, current P04 snapshot.                         | Register + Control only.                                                     | `CR_RECORDED` / `CHANGE_REQUEST_REGISTER_UPDATED`                                     | No Gate invalidation before byte change; downstream blocked immediately.                                                                               | `RECOVER CHANGE REQUEST EVENT [CRE-ID]`; abort only under 5.6.                   |
| T02 | `RECORDED` → `TRIAGE`                                                                                                                                                  | Tab 01 | `START APP FLOW CHANGE TRIAGE [CR-ID]`                     | CR is currently RECORDED; integrity verified.                                                                                                                           | Candidate Gate and candidate affected paths.                                        | Register + Control only.                                                     | `CR_TRIAGE_STARTED` / `CHANGE_REQUEST_REGISTER_UPDATED`                               | No Gate invalidation; remains blocked.                                                                                                                 | Recover one valid staged event.                                                  |
| T03 | `TRIAGE` → `NEEDS_CLARIFICATION`                                                                                                                                       | Tab 01 | `REQUEST CLARIFICATION FOR APP FLOW CHANGE [CR-ID]`        | CR is TRIAGE; concrete unanswered questions are recorded.                                                                                                               | Questions and current hashes of related artifacts.                                  | Register + Control only.                                                     | `CR_CLARIFICATION_REQUESTED` / `CHANGE_REQUEST_REGISTER_UPDATED`                      | No Gate invalidation; remains blocked.                                                                                                                 | Recover one valid staged event.                                                  |
| T04 | `NEEDS_CLARIFICATION` → `TRIAGE`                                                                                                                                       | Tab 01 | `RESUME APP FLOW CHANGE TRIAGE [CR-ID]`                    | CR is NEEDS_CLARIFICATION; user response is present.                                                                                                                    | Response summary and evidence hash, if any.                                         | Register + Control only.                                                     | `CR_TRIAGE_RESUMED` / `CHANGE_REQUEST_REGISTER_UPDATED`                               | No Gate invalidation; remains blocked.                                                                                                                 | Recover one valid staged event.                                                  |
| T05 | `TRIAGE` → `ACCEPTED_FOR_IMPLEMENTATION`                                                                                                                               | Tab 01 | `ACCEPT APP FLOW CHANGE [CR-ID]`                           | CR in TRIAGE; P04 ownership confirmed; no unresolved conflict or graph cycle.                                                                                           | Accepted scope, affected Gate/paths, pre-implementation hashes for artifacts 01–09. | Register + Control only; no artifact edit in this transition.                | `CR_ACCEPTED_FOR_IMPLEMENTATION` / `CHANGE_REQUEST_REGISTER_UPDATED`                  | Gate remains as-is until bytes change; downstream remains blocked.                                                                                     | Recover one valid staged event.                                                  |
| T06 | `TRIAGE` → `REJECTED_WITH_NO_CHANGE`                                                                                                                                   | Tab 01 | `REJECT APP FLOW CHANGE NO CHANGE [CR-ID]`                 | User rationale supplied; all relevant P04 artifact hashes match intake snapshot.                                                                                        | Rejection rationale and verified unchanged hashes.                                  | Register + Control only.                                                     | `CR_REJECTED_NO_CHANGE` / `CHANGE_REQUEST_REGISTER_UPDATED`                           | No Gate invalidation; releases only this CR's blocker.                                                                                                 | Recover one valid staged event.                                                  |
| T07 | `TRIAGE` → `RETURN_TO_P03`                                                                                                                                             | Tab 01 | `RETURN APP FLOW CHANGE TO P03 [CR-ID]`                    | Request concerns P03-owned CAP-ID/product scope.                                                                                                                        | Rationale, P03 Control hash, returned P03 frozen hash.                              | Register + P04 Control only; never edit P03 files.                           | `CR_RETURNED_TO_P03` / `CHANGE_REQUEST_REGISTER_UPDATED` plus P04 invalidation record | P03 source marked reopened for P04 consumption; P04 Gates 1–3 reopen; downstream blocked.                                                              | Recover one valid staged event; otherwise stop and verify P03 boundary.          |
| T08 | `RETURN_TO_P03` → `TRIAGE`                                                                                                                                             | Tab 01 | `RESUME APP FLOW CHANGE AFTER P03 FREEZE [CR-ID]`          | P03 v2 Control is APPROVED/FROZEN; initiative matches; actual P03 hash matches P03 frozen hash and differs from this CR's own `returned_p03_frozen_sha256`.             | New P03 Control hash, new frozen hash, this CR's returned snapshot.                 | Register + P04 Control only.                                                 | `CR_RESUMED_FROM_P03` / `CHANGE_REQUEST_REGISTER_UPDATED`                             | P03 source VERIFIED at new hash; P04 Gates remain reopened for revalidation.                                                                           | Recover one valid staged event; compare each CR to its own return snapshot.      |
| T09 | `RETURN_TO_P03` → `TRIAGE`                                                                                                                                             | Tab 01 | `RESOLVE P03 RETURN WITHOUT UPSTREAM CHANGE [CR-ID]`       | P03 remains APPROVED/FROZEN and actual P03 hash still equals this CR's returned snapshot; user supplies rationale.                                                      | User rationale and verified unchanged P03 hashes.                                   | Register + P04 Control only.                                                 | `CR_P03_RETURN_RESOLVED_NO_UPSTREAM_CHANGE` / `CHANGE_REQUEST_REGISTER_UPDATED`       | P03 source returns VERIFIED; CR resumes triage; P04 Gates still require valid reapproval if previously reopened.                                       | Recover one valid staged event.                                                  |
| T10 | `ACCEPTED_FOR_IMPLEMENTATION` → `IMPLEMENTED_PENDING_REAPPROVAL`                                                                                                       | Tab 01 | `RECORD APP FLOW CHANGE IMPLEMENTATION [CR-ID]`            | Owner tabs changed only accepted files; required Gate 1 and/or Gate 2 approvals are new and later than acceptance.                                                      | Implemented hashes, approval state sequences, ID-to-artifact traceability.          | Register + P04 Control only; prior artifact edits remain owned by Tab 01/02. | `CR_IMPLEMENTATION_RECORDED` / `CHANGE_REQUEST_REGISTER_UPDATED`                      | Gate 1/2 approved at new hashes; Gate 3 awaits independent review/freeze.                                                                              | Recover one valid staged event; re-read on-disk Gate receipts before recording.  |
| T11 | `IMPLEMENTED_PENDING_REAPPROVAL` → `ACCEPTED_FOR_IMPLEMENTATION`                                                                                                       | Tab 01 | `REOPEN APP FLOW CHANGE IMPLEMENTATION [CR-ID]`            | Tab 03 review found blockers or Owner requires implementation correction.                                                                                               | Reopen rationale and Finding IDs/review round, if applicable.                       | Register + Control only; next artifact edits remain with original owner tab. | `CR_IMPLEMENTATION_REOPENED` / `CHANGE_REQUEST_REGISTER_UPDATED`                      | Affected Gate(s) reopen when files change; downstream remains blocked.                                                                                 | Recover one valid staged event.                                                  |
| T12 | `IMPLEMENTED_PENDING_REAPPROVAL` → `CLOSED_IMPLEMENTED`                                                                                                                | Tab 01 | `CLOSE IMPLEMENTED APP FLOW CHANGE [CR-ID]`                | A valid GATE_3_FROZEN event exists; this CR was reviewed; frozen artifact hash matches; this CR belongs to the freeze batch.                                            | Frozen version, GATE_3_FROZEN state sequence, APP_FLOW SHA-256, review evidence.    | Register + Control only.                                                     | `CR_CLOSED_IMPLEMENTED` / `CHANGE_REQUEST_REGISTER_UPDATED`                           | Releases this CR only after receipt verification; downstream remains blocked while any other blocker exists.                                           | Recover one valid staged event; do not repeat an ambiguous close.                |
| T13 | `RECORDED` / `TRIAGE` / `NEEDS_CLARIFICATION` → `CANCELLED_NO_CHANGE`                                                                                                  | Tab 01 | `CANCEL APP FLOW CHANGE [CR-ID]`                           | CR is one of the listed pre-implementation states; it has not changed P04 bytes.                                                                                        | Cancellation rationale and unchanged hashes.                                        | Register + Control only.                                                     | `CR_CANCELLED_NO_CHANGE` / `CHANGE_REQUEST_REGISTER_UPDATED`                          | No Gate invalidation; releases only this CR.                                                                                                           | Recover one valid staged event.                                                  |
| T14 | `ACCEPTED_FOR_IMPLEMENTATION` → `CANCELLED_NO_CHANGE`                                                                                                                  | Tab 01 | `CANCEL APP FLOW CHANGE [CR-ID]`                           | Accepted CR, but every relevant artifact byte still matches the T05 pre-implementation snapshot.                                                                        | Cancellation rationale and full unchanged-hash comparison.                          | Register + Control only.                                                     | `CR_CANCELLED_NO_CHANGE` / `CHANGE_REQUEST_REGISTER_UPDATED`                          | No Gate invalidation; releases only this CR. If any byte changed, T14 is forbidden and T15 is required.                                                | Recover one valid staged event.                                                  |
| T15 | `ACCEPTED_FOR_IMPLEMENTATION` or `IMPLEMENTED_PENDING_REAPPROVAL` → `REVERSION_PENDING`                                                                                | Tab 01 | `START APP FLOW CHANGE REVERSION [CR-ID]`                  | User requests cancellation after byte changes or after implementation was recorded.                                                                                     | Reversion rationale and target baseline hashes.                                     | Register + Control only; restoration is performed by artifact owner tab.     | `CR_REVERSION_STARTED` / `CHANGE_REQUEST_REGISTER_UPDATED`                            | Reopen every Gate touched by changed files; downstream blocked.                                                                                        | Recover one valid staged event; restoration must be evidence-based.              |
| T16 | `REVERSION_PENDING` → `CANCELLED_AFTER_REVERSION`                                                                                                                      | Tab 01 | `COMPLETE APP FLOW CHANGE REVERSION [CR-ID]`               | All changed files restored to approved baseline; every reopened Gate is reapproved; if Gate 3 was touched, Review + Freeze are complete.                                | Restored hashes and verified Gate approval sequences.                               | Register + Control only after artifact/Gate work is complete.                | `CR_CANCELLED_AFTER_REVERSION` / `CHANGE_REQUEST_REGISTER_UPDATED`                    | CR blocker released only after verified restoration and reapproval.                                                                                    | Recover one valid staged event; refuse early completion.                         |
| T17 | `RECORDED` / `TRIAGE` / `NEEDS_CLARIFICATION` → `DUPLICATE`                                                                                                            | Tab 01 | `MARK APP FLOW CHANGE DUPLICATE [CR-ID] OF [CANONICAL-ID]` | Source has not changed files; target exists, is not self, is same initiative, creates no cycle, and is valid open blocker or CLOSED_IMPLEMENTED with proven coverage.   | Canonical ID and duplicate rationale; coverage evidence if target is closed.        | Register + Control only.                                                     | `CR_MARKED_DUPLICATE` / `CHANGE_REQUEST_REGISTER_UPDATED`                             | Blocker delegates to canonical target; source cannot disappear if target is invalid.                                                                   | Recover one valid staged event; cycle/target validation is mandatory.            |
| T18 | `RECORDED` / `TRIAGE` / `NEEDS_CLARIFICATION` / `ACCEPTED_FOR_IMPLEMENTATION` (no bytes changed, or approved successor inherits complete changed scope) → `SUPERSEDED` | Tab 01 | `SUPERSEDE APP FLOW CHANGE [OLD-ID] WITH [NEW-ID]`         | New ID exists, differs, same initiative, is an open blocking target, creates no cycle; if old bytes changed, successor inheritance is explicitly approved and complete. | Old/new IDs, rationale, transferred scope/path/hash evidence.                       | Register + Control only.                                                     | `CR_SUPERSEDED` / `CHANGE_REQUEST_REGISTER_UPDATED`                                   | Blocker delegates to successor; it remains blocking if the successor is missing, invalid, cancelled, or rejected without explicit transfer resolution. | Recover one valid staged event; target and graph are revalidated at append time. |

**Transition-table consistency note:** the Round 2 narrative mentions returning an accepted-but-unmodified CR to TRIAGE, but the reviewer’s closed T01–T18 table does not define that edge. v0.3 therefore does **not** silently permit `ACCEPTED_FOR_IMPLEMENTATION → TRIAGE`. The Owner must either approve this restriction or authorize a separately specified additional transition; until then, only T14 cancellation is legal when no bytes changed, and T15 reversion is required after byte changes.

### 7.3 Terminal-state and pointer integrity

- `CLOSED_IMPLEMENTED` is terminal and binds exactly one `(resolved_frozen_version, resolved_freeze_state_seq, resolved_app_flow_sha256)` tuple. Later changes require a new CR-ID.
- `REJECTED_WITH_NO_CHANGE` is terminal. New evidence requires a new submission/CR-ID linked through `related_cr_ids`; do not reopen the rejected CR.
- `CANCELLED_NO_CHANGE` and `CANCELLED_AFTER_REVERSION` are terminal.
- `DUPLICATE` and `SUPERSEDED` are pointer-terminal states. Their blocking behavior is projected through their target and cannot be used to erase a blocker.
- A closed target is a valid duplicate target only when the duplicate scope is proven fully covered by that target's exact frozen version/hash.
- `SUPERSEDED` must not point to a non-existent, self, terminal nonblocking, or cyclic target. If bytes have changed, ownership of every changed artifact and its approved scope must be explicitly inherited by the successor.

### 7.4 State machine consistency guard

Every state-changing Register event MUST carry the exact command, from/to status, actor tab, evidence tuple, affected paths, and current on-disk snapshot. Every transition MUST be validated against the closed set. No natural-language interpretation may create an unlisted edge.

---

## 8. Gate validity and blocking-CR reconstruction

### 8.1 Derived blocking function

Every reader (all three tabs and downstream consumer) MUST reconstruct CR status from the complete Register plus Control receipts. Never trust a stored count or list.

For each CR-ID:

- invalid or unreceipted chain/status/receipt → `NOT_VERIFIED` → blocking `TRUE`;
- `RECORDED`, `TRIAGE`, `NEEDS_CLARIFICATION`, `ACCEPTED_FOR_IMPLEMENTATION`, `IMPLEMENTED_PENDING_REAPPROVAL`, `RETURN_TO_P03`, `REVERSION_PENDING` → `TRUE`;
- `REJECTED_WITH_NO_CHANGE`, `CANCELLED_NO_CHANGE`, `CANCELLED_AFTER_REVERSION` → `FALSE`;
- `CLOSED_IMPLEMENTED` → `FALSE` only when its resolved freeze tuple matches a valid `GATE_3_FROZEN` event and its committed freeze sequence is no later than the current valid frozen Gate 3 checkpoint; otherwise `TRUE`;
- `DUPLICATE(target)` → recursively evaluate target; invalid/missing/cyclic target → `TRUE`;
- `SUPERSEDED(target)` → recursively evaluate target; invalid/missing/cyclic target or a target cancelled/rejected without explicit valid transfer resolution → `TRUE`.

Traversal depth MUST be bounded by the total number of CRs. Any cycle MUST be detected and return blocking `TRUE`. The graph validator MUST reject cycles before an append, not merely discover them during downstream reads.

A CR becomes blocking at `RECORDED`, not at TRIAGE. Intake is the earliest safe blocking point because an untriaged submission may invalidate assumptions used downstream.

### 8.2 Gate validity is separate from downstream eligibility

A newly recorded CR blocks downstream consumption immediately but does not invalidate previously approved Gates until relevant source/artifact bytes change.

| Change detected                                          | Gate effect                                                                              |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| New CR only; no relevant bytes changed                   | Existing Gate approvals remain valid; downstream blocked by CR.                          |
| P03 frozen source changes                                | P04 Gates 1–3 reopen; lifecycle becomes `REVIEW_REQUIRED`.                               |
| Artifact 01 or 02 changes                                | Gates 1–3 reopen.                                                                        |
| Artifact 03–06 changes                                   | Gates 2–3 reopen; Gate 1 may remain approved only if its evidence remains byte-valid.    |
| Artifact 07 or 08 changes                                | Gate 3 reopens.                                                                          |
| Decision Log changes                                     | Apply the existing Gate-binding rules; Gate(s) bound to the changed Decision Log reopen. |
| Register becomes NOT_VERIFIED                            | All P04 writes and downstream consumption blocked; conservative invalidation applies.    |
| Frozen `APP_FLOW.md` bytes change outside a valid freeze | Gate 3 reopens; lifecycle becomes `REVIEW_REQUIRED`; downstream blocked.                 |

The original detailed Gate invalidation matrix in the canonical Skill remains authoritative after it is updated. This table is a summary and MUST be checked against that matrix during implementation review.

### 8.3 Downstream eligibility predicate

A downstream process may consume `APP_FLOW.md` only when **all** are true:

1. P04 workspace integrity is `VERIFIED`.
2. P04 Control File schema is v4 and every Control event sequence is valid.
3. P03 initiative ID matches and P03's actual frozen file hash matches its P03 v2 Control File frozen hash.
4. P04 `gate_1`, `gate_2`, and `gate_3` are APPROVED with valid approval sequence anchors and matching current artifact hashes.
5. P04 lifecycle is `FROZEN`.
6. `APP_FLOW.md` exists and its actual SHA-256 equals the valid Gate 3 frozen artifact hash.
7. Register initialization and the full event/receipt chain verify.
8. `reconstructed_blocking_cr_ids` is empty.
9. Every CR in the freeze batch that reached `IMPLEMENTED_PENDING_REAPPROVAL` has a committed `CLOSED_IMPLEMENTED` event bound to that exact frozen version, Gate 3 freeze sequence, and frozen artifact hash.
10. The latest Review snapshot binds the exact Register hash, sequence, last event ID, and CR set used at Freeze.

`lifecycle_status: FROZEN` and `gate_3.status: APPROVED` alone do not authorize downstream consumption.

---

## 9. Freeze-to-CR-closure publication contract (NF-05)

### 9.1 Two-stage freeze publication

Tab 03 remains the only tab authorized to perform the mechanical Freeze. Tab 01 remains the only writer of the Register. Therefore a Freeze and subsequent CR closure cannot be represented as one cross-file atomic transaction.

The v0.3 contract handles this explicitly:

**Stage A — Freeze committed by Tab 03**

1. Tab 03 verifies Control File, Register, Decision Log, artifacts, and latest Review snapshot.
2. Register hash, `last_register_seq`, `last_event_id`, open CR IDs, blocking CR IDs, and the list of `IMPLEMENTED_PENDING_REAPPROVAL` CRs are snapshotted in the Review round.
3. Freeze is refused if any CR is in a state other than those explicitly eligible for the current implementation batch. In particular, `RECORDED`, `TRIAGE`, `NEEDS_CLARIFICATION`, `ACCEPTED_FOR_IMPLEMENTATION`, `RETURN_TO_P03`, and `REVERSION_PENDING` block Freeze.
4. Tab 03 writes the versioned frozen output and the `GATE_3_FROZEN` Control receipt. The frozen file may carry `> Status: FROZEN`, but this is not yet sufficient for downstream consumption.
5. The downstream predicate remains false while one or more implementation CRs are still `IMPLEMENTED_PENDING_REAPPROVAL`.

**Stage B — CR closure by Tab 01**

1. User returns to Tab 01 and executes `CLOSE IMPLEMENTED APP FLOW CHANGES FOR FREEZE [FROZEN-VERSION]` (batch command) or the single-item `CLOSE IMPLEMENTED APP FLOW CHANGE [CR-ID]` for each eligible CR.
2. Tab 01 reads the just-committed Gate 3 event and verifies the frozen version, Gate 3 state sequence, actual `APP_FLOW.md` hash, and Review snapshot.
3. For every CR in that exact freeze batch, Tab 01 appends an individual `CR_CLOSED_IMPLEMENTED` Register event and its matching Control receipt. Each receipt receives its own next monotonically increasing `state_seq`; no shared or repeated state sequence is allowed.
4. Each closure event binds `resolved_frozen_version`, `resolved_freeze_state_seq` (the `GATE_3_FROZEN` event sequence), `resolved_app_flow_sha256`, and the actual closure receipt sequence.
5. If interrupted midway, completed closures remain committed, unfinished CRs remain blockers, and downstream stays blocked. Resume by reading the files and closing only CRs that remain `IMPLEMENTED_PENDING_REAPPROVAL`; never duplicate a committed close.
6. Downstream becomes eligible only after every expected CR in the batch is validly closed and the reconstructed blocking set is empty.

No Control File status field may override the Register's business state. A convenience indicator such as `downstream_freeze_publication_state` may be computed for display, but it is derived and must not become a second CR status source.

### 9.2 Deterministic freeze versioning (NF-11)

- The first valid Freeze is `frozen_version: 1`.
- Each subsequent valid `GATE_3_FROZEN` event increments the version by exactly one (`v + 1`).
- Before a new Freeze, preserve the previous frozen file as `APP_FLOW.v<N>.md` using the exact prior version number.
- A no-op re-freeze is refused when all source/artifact/Decision Log/Review hashes and CR state are unchanged and no new accepted implementation is awaiting publication: `Already frozen at current state; no-op re-freeze prohibited`.
- A changed P03 source binding, approved artifact scope, or implemented CR batch requires a new version even if portions of output bytes remain unchanged.
- A frozen output written without a matching `GATE_3_FROZEN` receipt is an orphan/incomplete file and MUST NOT be consumed downstream.

---

## 10. P03 return, re-entry, and upstream drift (NF-08)

### 10.1 Return to P03

When a request affects P03-owned product definition or CAP-ID scope, Tab 01 records `RETURN_TO_P03`; it MUST NOT edit P03 files. The event stores `returned_p03_control_sha256` and `returned_p03_frozen_sha256` specific to that CR.

### 10.2 Resume after a new P03 freeze

`RESUME APP FLOW CHANGE AFTER P03 FREEZE [CR-ID]` compares the new actual P03 frozen hash with the `returned_p03_frozen_sha256` stored in that particular CR's return event, not with a mutable global current P04 hash. This permits several CRs to resume against the same new P03 freeze one by one.

P03's new file hash must match P03 Control v2 `gate_3.frozen_artifact.sha256`; initiative IDs must match. On success, source status becomes VERIFIED at the new hash and the CR returns to TRIAGE. P04 Gates remain reopened for revalidation.

### 10.3 P03 returns without upstream change

If the Owner decides P03 will retain its prior frozen definition, use `RESOLVE P03 RETURN WITHOUT UPSTREAM CHANGE [CR-ID]`. Require a user rationale and verify P03 remains frozen with the exact hash stored in that CR's return event. The CR returns to TRIAGE; it may then be rejected, cancelled where allowed, or handled within P04 ownership.

### 10.4 Upstream drift not initiated by a P04 CR

If P03 has a valid new freeze not initiated by a P04 CR, P04 detects drift on tab entry, marks the P03 source binding reopened, reopens P04 Gates 1–3, sets lifecycle to `REVIEW_REQUIRED`, and records `INVALIDATED` with reason `UPSTREAM_P03_DRIFT`. P04 MUST NOT fabricate a CR to explain the drift.

If P03 initiative identity, actual file hash, or P03 Control receipt is inconsistent, set source status `NOT_VERIFIED` and stop. Do not infer or transfer P03 approval to P04.

---

## 11. Three-tab permission and disk handoff contract

### 11.1 Ownership matrix

| Artifact / action                                             | Tab 01 — Task/Flow + CR coordinator                                                     | Tab 02 — Navigation/Screens/States                             | Tab 03 — Independent Review/Freeze                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `00_APP_FLOW_CONTROL.md`                                      | Writes Gate 1 events, CR receipts, Register pointer, and authorized P03 binding events. | Writes Gate 2 events and its authorized Decision Log receipts. | Writes review receipts, residual-risk receipts, Gate 3 Freeze, and authorized invalidation events. |
| `10_CHANGE_REQUEST_REGISTER.md`                               | **Sole writer**; initialize and append every CR event.                                  | Read only.                                                     | Read only.                                                                                         |
| `01_TASK_MODEL.md`, `02_FLOW_ARCHITECTURE.md`                 | Owner/writer for Gate 1 and its CR scope.                                               | Read only.                                                     | Read only.                                                                                         |
| `03_NAVIGATION_MODEL.md`–\`06_STATE_AND_EXCEPTION_MATRIX.md\` | Read only; may inspect hashes/evidence.                                                 | Owner/writer for Gate 2 and its CR scope.                      | Read only.                                                                                         |
| `07_FLOW_REVIEW.md`, `08_APP_FLOW_DRAFT.md`                   | Read only.                                                                              | Read only.                                                     | Owner/writer; records independent review and assembles draft.                                      |
| `09_DECISION_LOG.md`                                          | Append-only for Gate 1 decisions.                                                       | Append-only for Gate 2/3 decisions.                            | Strictly read only.                                                                                |
| `APP_FLOW.md`, `APP_FLOW.v<N>.md`                             | Read only; verifies hashes and closes CRs after Freeze.                                 | Read only.                                                     | Authorized Freeze executor; archives and publishes output after explicit user command.             |
| CR state decisions                                            | Coordinates all CR lifecycle commands.                                                  | No independent CR state updates.                               | No independent CR state updates.                                                                   |

User approval is expressed through exact commands. The user does not hand-edit hashes or sequence numbers. P03 and downstream are read-only with respect to P04 workspace state.

### 11.2 Disk is the handoff channel

The tabs run in fresh conversations and reconstruct state from files, not prior chat history. Consequently:

- Tab 02 completes Gate 2 artifacts and the `GATE_2_APPROVED` Control event before returning to Tab 01.
- Tab 01 rereads Control File and Register from disk and verifies the new Gate event sequence and hashes before recording `CR_IMPLEMENTATION_RECORDED`.
- For mixed Gate 1+2 scope, Tab 01 completes and approves Gate 1 first; Tab 02 then completes and approves Gate 2; Tab 01 finally records the CR as `IMPLEMENTED_PENDING_REAPPROVAL`.
- Tab 03 snapshots the Register and Control hashes at Review start and rechecks immediately before Freeze. Any changed Register hash/sequence/event ID invalidates the Review snapshot and requires a new Review round.
- A stale chat context is never accepted as current state.

### 11.3 Single-writer limitation

The workflow MUST enforce one logical writer at a time and stale-read checks. It MUST NOT claim `active_owner_tab` or `state_seq` is an OS lock, atomic CAS, or distributed mutex. If actual concurrent writes occur, any duplicate sequence, lost event, unexpected hash, or malformed pair causes `NOT_VERIFIED`; stop and restore from a trusted backup.

---

## 12. Review snapshot and frozen downstream binding

### 12.1 Required Review round fields

Each `### Review round <N>` entry in `07_FLOW_REVIEW.md` MUST include:

- P03 initiative ID and frozen source hash;
- P04 Control File `state_seq` and whole-file SHA-256 snapshot;
- Register path, schema version, full-file SHA-256, `last_register_seq`, `last_event_id`;
- all open CR IDs and reconstructed blocking CR IDs;
- CR IDs verified in this review and implementation CR IDs expected in the Freeze batch;
- Decision Log path/hash and relevant event references;
- artifact hashes for 01–06 and draft 08;
- latest Review round identity/hash and findings dispositions;
- test environment, reproduction evidence, and review verdict.

Freeze MUST be refused if the current Register snapshot differs from the Review snapshot.

### 12.2 Downstream binding tuple

P04 publishes evidence through the Control File, Register, and frozen `APP_FLOW.md`; it MUST NOT add a circular whole-file hash inside `APP_FLOW.md`.

A downstream reader must verify at least these 12 binding groups:

1. `initiative_id` is identical in P03 Control, P04 Control, Decision Log, Register, and `APP_FLOW.md`.
2. `p04_schema_version == 4`.
3. P04 `lifecycle_status == FROZEN` and `gate_3.status == APPROVED`.
4. `frozen_version` is a positive integer matching the latest valid `GATE_3_FROZEN` event.
5. Actual `product/app-flow/APP_FLOW.md` SHA-256 matches the Control File frozen artifact hash and the Freeze event.
6. `reviewed_draft_sha256` and `latest_review_sha256` prove the frozen output came from the independently reviewed draft; the frozen output differs only by the approved status line.
7. `gate_1.approved_state_seq`, `gate_2.approved_state_seq`, and `gate_3.approved_state_seq` exist in P04 v4, are ordered, and point to valid matching Gate events and current approved artifact hashes.
8. `source_process_03` matches P03 v2 initiative ID, status VERIFIED, frozen path, frozen hash, and actual bytes.
9. `change_request_register` path/schema/hash/sequence/last event matches disk, and the full chain is verified.
10. `reconstructed_blocking_cr_ids == []`.
11. Every implementation CR in the freeze batch is `CLOSED_IMPLEMENTED` and bound to the same frozen version, Gate 3 freeze sequence, and `APP_FLOW.md` hash.
12. Accepted residual risks are explicitly recorded and approved by the Owner for downstream inheritance.

The P04 downstream contract proves artifact and workflow integrity; it does not determine whether a hash change is semantically major or minor. That policy belongs to the downstream process.

---

## 13. Schema v3 → v4 migration contract (NF-09)

### 13.1 Migration command and attestation

Migration requires an explicit user command and one of two mutually exclusive paths:

- `MIGRATE APP FLOW CONTROL V3 TO V4 WITH ZERO EXTERNAL CRS` — user attests that no unrecorded/out-of-band CRs are pending.
- `MIGRATE APP FLOW CONTROL V3 TO V4 WITH PENDING SUBMISSIONS` — migration may proceed only into a blocked/review-required state; pending payloads are registered through Tab 01 after migration.

The operator MUST NOT infer the absence of unrecorded CRs from the old `change_requests: []` field alone. The user attestation is explicit and recorded in migration evidence.

### 13.2 Preconditions

- P04 v3 Control File is structurally readable and its event sequence is valid.
- P03 v2 identity and frozen binding are verified.
- The migration tool/agent has read the exact approved v3 schema and migration plan.
- All required P04 artifact hashes and old approval sequences have been captured.
- The user selects one of the two explicit migration commands.
- No other writer is active.

### 13.3 Backup and manifest

Before changing any file, create a byte-preserving backup of the full active P04 workspace, including Control File, Decision Log, Review history, artifacts, draft, frozen output, and relevant README state. Create `ARCHIVE_MANIFEST.md` recording relative path, byte size, SHA-256, schema version, initiative ID, source HEAD, timestamp, and backup destination. Verify every backup hash before proceeding.

### 13.4 Preserve only verified approvals

Migration MAY preserve a v3 Gate approval only if:

- the relevant v3 event exists exactly once and has a valid `state_seq`;
- the v3 approval sequence fields match the latest valid events;
- all artifact hashes, Decision Log hash, Review hash, reviewed draft hash, frozen output hash, and P03 source hash still match the bytes on disk;
- the v3 event log has no sequence gaps or integrity conflicts.

If a relevant hash does not match, reopen the affected Gate conservatively before or during migration. Do not blanket-reset all approvals when they remain verifiably valid, and do not preserve approval merely because the old Control File says APPROVED.

Legacy Decision Log records with unmatched status tokens remain byte-identical and are marked `LEGACY_UNVERIFIED` for current reconstruction.

### 13.5 One logical migration transaction, one Control File replacement

To resolve the initialization/SCHEMA_MIGRATED ambiguity:

1. Preserve and verify the v3 backup and manifest.
2. Create the v1 Register header with correct initiative identity and compute `H_init`.
3. Construct the complete v4 Control File in a temporary file. It MUST contain both sequential Control events:
   - `SCHEMA_MIGRATED` (`from_schema_version: 3`, `to_schema_version: 4`, migration command/attestation, backup manifest hash, preserved/reopened Gate summary);
   - `CHANGE_REQUEST_REGISTER_INITIALIZED` (`register_seq: 0`, `last_event_id: INITIALIZATION`, `last_verified_sha256: H_init`, path and Register schema version).
4. Assign distinct strictly increasing Control `state_seq` values to those two events.
5. Validate the temporary v4 Control File and all hashes before replacing the active v3 Control File.
6. Replace the Control File in one complete filesystem replacement operation on the same filesystem; do not expose a partially serialized v4 file.
7. Read the new Control File and Register back from disk and verify both events, the checkpoint, the manifest, and the v4 schema.
8. Treat migration as complete only after read-back succeeds.

The two Control events are one **logical migration transaction** and one complete Control File replacement. The Register initialization receipt is not deferred to a later chat/session.

### 13.6 Interrupted migration recovery

- If failure occurs before the v4 Control File replacement, retain v3 as canonical; remove or quarantine only the newly created uncommitted Register after preserving its bytes as evidence.
- If replacement may have occurred but caller confirmation is missing, reopen and read both files. If v4 Control + initialization receipt + Register hash all verify, treat migration as complete; do not rerun.
- If active Control is corrupt or the pair is inconsistent, restore the complete v3 workspace byte-for-byte from the verified archive and verify every path against `ARCHIVE_MANIFEST.md`; then restart migration only after correction.
- Never leave a v3 Control File paired with an unreceipted v4 Register and claim migration success.

### 13.7 Inherited frozen v3 workspaces

A v3 workspace previously marked FROZEN may preserve that historical Gate 3 evidence only if all v3 frozen hashes and receipts verify. The v4 Register initialization is anchored by the migration transaction. If the user selected ZERO EXTERNAL CRS, the new Register starts at sequence 0 and has no blocking CRs. If the user selected PENDING SUBMISSIONS, downstream remains blocked until every pending payload has been registered and resolved. A historical v3 Freeze does not create `CLOSED_IMPLEMENTED` CR records retroactively.

---

## 14. File impact matrix

The following changes are mandatory for the implementation phase. Exact edits must be made only after Owner approval and after verifying the current repository baseline.

| Path                                                  | Classification     | Required change                                                                                                                                                                                   |
| ----------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.agents/skills/app-flow/SKILL.md`                    | MUST CHANGE        | Canonical contract: CR states/transitions, init, paired protocol, abort/recovery, hash rules, Gate effects, three-tab ownership, blocking algorithm, P03 re-entry, migration, downstream binding. |
| `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md`        | MUST CHANGE        | Schema v4, remove `change_requests: []`, add Register checkpoint and event receipts, migration 3→4, abort receipt type, initialization event.                                                     |
| `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` | MUST CREATE        | Register v1 header, canonical encoding, CRE block schema, event enum, prefix chain and abort marker shape.                                                                                        |
| `templates/04-APP-FLOW/10-DECISION-LOG.md`            | MUST CHANGE        | Correct only `decision_event_kind: STATUS_CHANGED` to `DECISION_STATUS_CHANGED`; do not add committed `control_state_seq` to event body.                                                          |
| `templates/04-APP-FLOW/07-FLOW-REVIEW.md`             | MUST CHANGE        | Add exact Register hash/sequence/event, open/blocking CR snapshot, batch CR IDs, and recheck fields.                                                                                              |
| `prompts/04-APP-FLOW/01-TASK-MODEL.md`                | MUST CHANGE        | Initialize/verify Register on entry; Tab 01 sole CR coordinator; exact lifecycle command reference to Skill.                                                                                      |
| `prompts/04-APP-FLOW/02-NAVIGATION-FLOW.md`           | MUST CHANGE        | Read-only Register entry check; only edit accepted Gate 2 scope; return to Tab 01 after on-disk Gate 2 approval.                                                                                  |
| `prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md`        | MUST CHANGE        | Read-only Register audit, Review snapshot, freeze blocker rules, post-freeze handoff to Tab 01 for CR closure.                                                                                    |
| `app-flow-kit/README.md`                              | MUST CHANGE        | List active artifact 10 and template 11 mapping, user commands, migration summary, point to Skill.                                                                                                |
| `app-flow-kit/VERIFICATION-CHECKLIST.md`              | MUST CHANGE        | Static checks, v4 schema, hash/receipt verification, 20 stress cases, runtime test register (NOT RUN until performed).                                                                            |
| `product/app-flow/README.md`                          | MUST CHANGE        | Upgrade schema reference to v4; list `10_CHANGE_REQUEST_REGISTER.md` (Owner: Tab 01); define downstream eligibility using Register and blocking set.                                              |
| `README.md`                                           | MUST CHANGE        | Change working artifacts from 01–09 to 01–10; add Register integrity and zero-blocking-CR handoff requirements.                                                                                   |
| P04 functional templates 01–06, 08, 09                | NO CHANGE          | Do not embed CR business-state machinery into functional artifacts.                                                                                                                               |
| All P03 templates/prompts/Skill/kit                   | STRICTLY NO CHANGE | Preserve P03 schema v2 and ownership.                                                                                                                                                             |
| Processes 01, 02, 05, 06, 07                          | OUT OF SCOPE       | No policy or file changes in this remediation.                                                                                                                                                    |

### 14.1 Canonical contract placement

The complete state machine, transaction protocol, migration, permissions, and downstream rules are defined once in `SKILL.md`. Templates encode fields and event shapes. Prompts only enforce tab-specific duties and link to the Skill. README files summarize, not redefine. The Verification Checklist tests the canonical contract without creating a competing copy.

---

## 15. Failure simulation suite

The following 20 scenarios are mandatory static/simulation tests. Expected outcomes are summarized here; detailed step-by-step test fixtures and assertions must be added to `app-flow-kit/VERIFICATION-CHECKLIST.md` during implementation.

| Test  | Scenario                                                    | Required expected result                                                                                                                                          |
| ----- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ST-01 | Initialize Register with null Control pointer               | Create header-only Register; commit `CHANGE_REQUEST_REGISTER_INITIALIZED`; `register_seq: 0`, non-null init hash.                                                 |
| ST-02 | Register exists with wrong Initiative ID                    | `NOT_VERIFIED`; do not rewrite identity or accept its hash as baseline.                                                                                           |
| ST-03 | One complete staged tail without receipt                    | Block all writes; recover only by validating trusted prefix and re-evaluating preconditions.                                                                      |
| ST-04 | Receipt has wrong `event_block_sha256`                      | `NOT_VERIFIED`; no auto-correction of receipt.                                                                                                                    |
| ST-05 | Duplicate Control receipts for one Register event           | `NOT_VERIFIED`; restore trusted Control File.                                                                                                                     |
| ST-06 | `register_seq` gap                                          | `NOT_VERIFIED`; restore trusted Register/Control pair.                                                                                                            |
| ST-07 | Control `state_seq` gap                                     | `NOT_VERIFIED`; never invent the missing event.                                                                                                                   |
| ST-08 | More than one unreceipted Register tail event               | Reject normal recovery; allow only the exact two-event staged+abort pair through `RECOVER CHANGE REQUEST ABORT`; otherwise restore to last trusted Register hash. |
| ST-09 | Tab 01 uses stale chat state after Tab 02 Gate 2 approval   | Tab 01 rereads disk and uses new Gate receipt/sequence; stale memory ignored.                                                                                     |
| ST-10 | Tab 02 edits Gate 2 while Gate 1 is reopened                | Stop at Tab 02 Entry Gate; no Gate 2 edits.                                                                                                                       |
| ST-11 | Register changes after Tab 03 Review snapshot               | Freeze refused; new Review round required.                                                                                                                        |
| ST-12 | Freeze succeeds but CR closure receipt fails                | Downstream stays blocked; recover the single staged close or abort; do not report eligible.                                                                       |
| ST-13 | Two CRs return to P03 and resume against one new P03 freeze | Each CR compares against its own `returned_p03_frozen_sha256`; both may resume.                                                                                   |
| ST-14 | Supersede target missing or terminal-invalid                | Reject before append; original CR remains blocking.                                                                                                               |
| ST-15 | User cancels after a partial artifact edit                  | Reject T14; require T15 reversion and T16 after Gate restoration.                                                                                                 |
| ST-16 | Reversion bytes restored but required Gate approval missing | Reject T16; remain `REVERSION_PENDING`.                                                                                                                           |
| ST-17 | New evidence arrives after terminal rejection               | Preserve old CR; create new submission/CR linked to old ID.                                                                                                       |
| ST-18 | v3→v4 migration interrupted                                 | Restore/verify full v3 archive or verify completed v4 pair; never claim partial success.                                                                          |
| ST-19 | Legacy v3 reader reads v4 Control File                      | Fail closed with unsupported schema; no writes.                                                                                                                   |
| ST-20 | New CR appears after prior CR closed in v1                  | Old CR remains bound to v1; new CR blocks downstream until resolved for a later version.                                                                          |

Additional targeted tests MUST cover: one staged event whose expected Control sequence has been consumed by an unrelated event; abort-pair hash edges `H(k-1) → H(k) → H(k+1)`, one-receipt coverage, and recovery when the complete abort pair exists but its receipt is missing; canonical LF/UTF-8 enforcement; prefix-chain tampering; cycles across duplicate/supersession/dependency edges; no-op re-freeze; mixed Gate 1+2 handoff; and downstream eligibility after a partially completed multi-CR close batch.

---

## 16. Implementation sequence and phase gates

**No phase from 1 onward may begin until Phase 0 is approved and complete.** All implementation work MUST occur on a dedicated branch; no direct commits to `main`.

| Phase | Scope                                                                                                                                                                                                      | Exit criteria                                                                                                                                                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | Owner architecture approval; incorporate all required NF-01…NF-12 amendments; resolve explicit Owner decisions for ADR-P04-01…10 and all five clarification items (`CL-01` through `CL-05`) in Section 17. | All P0/P1 decisions approved; no contradictory protocol rules; v0.3.1 micro-diff accepted.                                                                                                                                                  |
| 1     | Isolated Decision Log enum correction in `10-DECISION-LOG.md`.                                                                                                                                             | Grep confirms zero exact occurrences of `decision_event_kind: STATUS_CHANGED` and zero accidental `DECISION_DECISION_STATUS_CHANGED` across affected P04 Skill/templates. Separate commit.                                                  |
| 2     | Create Register template v1 and upgrade Control template to schema v4.                                                                                                                                     | Exact schema/field/event names agree; init and update/abort receipts validate; migration event supports v3→v4.                                                                                                                              |
| 3     | Update canonical Skill and Review template.                                                                                                                                                                | Skill fully defines serialization, hash/receipt chain, initialization, recovery/abort, state machine, blockers, 3-tab permissions, P03 re-entry, migration, Freeze closure, downstream tuple. Review captures required immutable snapshots. |
| 4     | Update the three P04 prompts.                                                                                                                                                                              | Tab 01 sole Register writer; Tab 02 only edits Gate 2 scope and hands off via disk; Tab 03 read-only Register reviewer and mechanical Freeze executor. No prompt duplicates or contradicts Skill rules.                                     |
| 5     | Update all README files and Verification Checklist.                                                                                                                                                        | All docs show artifacts 01–10, correct template mapping, schema v4, downstream requirements; all 20 stress tests and additional edge cases included. `product/app-flow/README.md` is mandatory.                                             |
| 6     | Static verification and independent Hard Review on actual implementation diff.                                                                                                                             | No unresolved P0/P1/P2 findings; schema consistency and tests pass; no P03/out-of-scope changes; dedicated branch diff reviewed.                                                                                                            |
| 7     | Live Windows Antigravity three-tab runtime testing and Owner merge approval.                                                                                                                               | At least six end-to-end runtime flows pass with actual file/log/hash evidence; runtime test statuses change from NOT RUN to PASS only with evidence; Owner explicitly approves merge.                                                       |

### 16.1 Minimum live runtime flows

At minimum, test:

1. Fresh P04 initialization with zero CRs.
2. Gate 1 CR from intake through implementation, Review, Freeze, and closure.
3. Gate 2 CR using Tab 02 disk handoff to Tab 01.
4. Mixed Gate 1+2 CR and ordered approvals.
5. P03 return/re-entry, including no-upstream-change resolution.
6. Freeze with multiple implementation CRs, interrupted close receipt, recovery, and downstream eligibility check.

Also test migration of a verified v3 workspace and at least one deliberately invalid/NOT_VERIFIED recovery case before declaring runtime confidence.

---

## 17. Owner decision register and explicit clarifications

All Owner Decision cells intentionally remain `PENDING`. The reviewer recommendation is not an Owner approval.

| ADR        | Decision                                             | Reviewer recommendation carried into v0.3                                                                                                                                                                | Owner decision |
| ---------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| ADR-P04-01 | Decision Log enum and pairing                        | Accept with modification: fix token; preserve legacy bytes; Control receipt alone carries committed sequence.                                                                                            | PENDING        |
| ADR-P04-02 | Sole CR source of truth                              | Accept with modification: Register owns CR status; Control File stores pointer/receipts only; initialize at seq 0.                                                                                       | PENDING        |
| ADR-P04-03 | Paired append-and-receipt protocol                   | Accept with modification: no planned Control seq in Register; canonical LF serialization; full prefix verification; bounded recovery and explicit abort-pair exception.                                  | PENDING        |
| ADR-P04-04 | Submission boundary and CR-ID ownership              | Accept: immutable intake payload; Tab 01 alone assigns CR-ID after source/hash/dedup verification.                                                                                                       | PENDING        |
| ADR-P04-05 | Tab 01 sole CR coordinator and three-tab permissions | Accept with modification: disk-persisted Gate approval receipts are cross-tab handoff evidence; no chat-memory handoff.                                                                                  | PENDING        |
| ADR-P04-06 | CR lifecycle                                         | Accept with modification: 13 states; no REFROZEN; T01–T18 closed transitions; exact commands/evidence; reopen/reversion paths; graph validation.                                                         | PENDING        |
| ADR-P04-07 | Gate validity vs downstream eligibility              | Accept with modification: blocking starts at RECORDED; reconstruct blockers; downstream remains blocked until post-Freeze CR closure receipts verify.                                                    | PENDING        |
| ADR-P04-08 | P03 return and same-CR re-entry                      | Accept with modification: keep CR-ID; retain P03 v2; add T09 no-upstream-change resolution; compare each CR with its own return snapshot.                                                                | PENDING        |
| ADR-P04-09 | P04 Control schema v4 and migration                  | Accept with modification: preserve only hash-verified v3 approvals; explicit zero-CR or pending-submission attestation; backup manifest; Register init and migration in one logical Control replacement. | PENDING        |
| ADR-P04-10 | Frozen downstream binding                            | Accept with modification: Control + Register + APP_FLOW evidence tuple; deterministic frozen version; no no-op re-freeze.                                                                                | PENDING        |

### 17.1 Clarifications introduced while consolidating v0.3

These clarifications close internal ambiguities found while translating the reviewer report into a single contract. They require explicit Owner approval before implementation:

**CL-01 — Abort semantics and receipt exception.** Approve the Section 4.4 / 5.5 / 5.6 abort commit unit: preserve the staged business event at sequence `k`; calculate its intermediate prefix hash `H(k)` without publishing it as a checkpoint; append the abort marker at `k+1` with `previous_register_sha256: H(k)`; and commit the pair with exactly one `CHANGE_REQUEST_EVENT_ABORTED` receipt binding the prior trusted hash `H(k-1)`, both event-block hashes, intermediate hash `H(k)`, and final hash `H(k+1)`. The Control checkpoint advances directly from `k-1` to `k+1`; the staged event is `ABORTED_NOT_EFFECTIVE`, the marker is audit-only, and neither changes CR business state. If the marker is present but the receipt is missing, `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` writes only the missing receipt after validating the exact pair; it never appends a second marker. This is the sole exception to the normal one-event/one-\`CHANGE_REQUEST_REGISTER_UPDATED\` receipt rule. If not approved, a different fully specified append-only abort model is required before implementation.

**CL-02 — Initialization anchor.** Approve `CHANGE_REQUEST_REGISTER_INITIALIZED` as a dedicated Control event at `register_seq: 0`, containing the non-null hash of the header-only Register. Normal transition receipts begin at `register_seq: 1`. This avoids pretending the zero-event initialization is a normal `CHANGE_REQUEST_REGISTER_UPDATED` event.

**CL-03 — Migration write boundary.** Approve migration as one logical transaction and one complete Control File replacement containing sequential `SCHEMA_MIGRATED` and `CHANGE_REQUEST_REGISTER_INITIALIZED` events, after a verified backup and Register creation. Interruption handling follows Section 13.6.

**CL-04 — Accepted-but-unmodified CR re-triage.** The reviewer narrative mentions returning an accepted CR to TRIAGE when no bytes changed, but the 18-edge table does not include that transition. v0.3 keeps the T01–T18 table closed and disallows that edge. Owner must approve this restriction or request a separately specified T19 before the state machine is frozen.

**CL-05 — Batch closure behavior.** Approve one batch command as an operator convenience that expands into individual CR close events and individual monotonically increasing receipts. A partial batch remains blocked; recovery resumes only uncommitted CR closures.

---

## 18. Final release criteria — no implementation before PASS

All criteria below are mandatory. A partial pass is not authorization to implement.

- Owner explicitly approves ADR-P04-01 through ADR-P04-10, with any required modifications.
- Owner explicitly approves CL-01 through CL-05, or the specification is revised to resolve them.
- NF-01 closed: no predicted Control sequence in Register; valid recovery at the next available sequence; append-only abort behavior fully specified.
- NF-02 closed: canonical byte serialization and full prefix-chain validation from initialization through last committed event.
- NF-03 closed: no committed `control_state_seq` in Decision Log bodies; Control receipt is the only sequence anchor.
- NF-04 closed: complete T01–T18 transition contract is consistent with the canonical state enum and all commands/events/evidence/recovery rules.
- NF-05 closed: Freeze and CR closure are two explicit stages; downstream remains blocked until every freeze-batch CR closure is committed and verified.
- NF-06 closed: all v4 workspaces initialize Register at seq 0 with a non-null hash.
- NF-07 closed: cross-tab handoff is persisted to disk through Gate approval events; stale conversation context is ignored.
- NF-08 closed: T09 exists; every P03 return is compared to that CR's own return snapshot; multiple CRs can resume against one P03 freeze.
- NF-09 closed: migration backup + `ARCHIVE_MANIFEST.md`, explicit external-CR attestation, preservation of only verified approvals, one logical migration transaction, and deterministic rollback are specified.
- NF-10 closed: duplicate/supersession/dependency targets are validated for existence, state, initiative, scope inheritance, and cycles before append.
- NF-11 closed: frozen version increments by one per valid new Freeze; no-op re-freeze is refused.
- NF-12 closed: `product/app-flow/README.md` is MUST CHANGE and synchronized.
- P03 is untouched and remains schema v2; no invented P03 fields are required.
- No downstream policy is embedded in P04 beyond the published binding/evidence contract.
- All 20 static stress scenarios and additional CL/edge-case tests are present in the Verification Checklist.
- Current repository HEAD and exact paths are freshly reverified before work begins.
- Implementation is on a dedicated branch, not `main`.
- Static Hard Review has zero unresolved P0/P1/P2 findings on the actual diff.
- Runtime tests remain `NOT RUN` until executed on Windows Antigravity with evidence; at least six minimum flows pass before merge approval.
- Owner explicitly approves the final merge after reviewing the diff and runtime evidence.

Only when every item is satisfied may the implementation status move from `HOLD` to `GO`.

---

## 19. Known limitations and evidence provenance

This v0.3.1 is a narrowly scoped micro-diff correction to v0.3. Its two change requests are grounded in the user-supplied Round 3 diff-only review: D3-01 (abort-pair/hash-chain semantics) and D3-02 (clarification count). The wider v0.3 content continues to be based on the Round 2 report in **“Văn bản đã dán (1)(20261112-073212).txt”**, sections A–N and Final Release Criteria. It preserves the reported repository baseline and does not claim a fresh GitHub inspection, repository implementation, or Antigravity runtime test. The micro-diff re-review below is a document-level consistency check only.

The source is a plain-text file and has no stable printed page numbers or embedded page images. Section labels, finding IDs, transition IDs, and test IDs are used as precise locators instead.

No repository files were modified. No commit, branch, pull request, migration, or runtime action was performed.

---

## 20. Change log

| Version | Change                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.2     | Prior remediation proposal reviewed as HOLD in Independent Hard Review — Round 2.                                                                                                                                                                                                                                                                                                                                                           |
| 0.3     | Consolidates NF-01…NF-12; adds canonical Register serialization and chain verification; defines initialization, recovery and abort; corrects Decision Log pairing; expands CR transition contract; closes Freeze-to-closure gap; defines P03 re-entry, v3→v4 migration, three-tab permissions, downstream binding, file impact, 20 stress tests, implementation phases, ADR register, and release criteria. Owner decisions remain PENDING. |
| 0.3.1   | Micro-diff correction only: defines the abort pair as one receipt unit with an explicit intermediate hash `H(k)` that is not a committed checkpoint; adds deterministic recovery for a complete abort pair with a missing receipt; aligns the Phase 0 requirement with all five clarifications CL-01…CL-05. No other v0.3 policy is reopened. Owner decisions remain PENDING.                                                               |

## 21. Micro diff re-review — D3-01 and D3-02 only

| Finding                                                 | Corrected locations                                                                  | Verification result                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D3-01 — Abort pair vs. committed hash-chain checkpoints | Sections 4.1, 4.4, 5.2, 5.4, 5.5, 5.6, 5.7; Section 15 ST-08/additional tests; CL-01 | `PASS`: the staged event links from the trusted checkpoint; the abort marker links from the intermediate hash; one abort receipt binds prior/intermediate/final hashes and both event blocks; the checkpoint advances directly across the two-event unit; recovery of a complete pair writes only the missing receipt. |
| D3-02 — Phase 0 clarification count                     | Section 16, Phase 0; Section 17.1 (`CL-01`…\`CL-05\`)                                | `PASS`: Phase 0 explicitly requires all five clarification items.                                                                                                                                                                                                                                                      |

**Review scope:** This is a targeted document-level micro diff review of D3-01 and D3-02 only. It is not a new full-document review, repository verification, static implementation test, or Antigravity runtime test. No repository files were changed. ADR-P04-01…ADR-P04-10 and CL-01…CL-05 remain `PENDING` until the Repository Owner explicitly decides. The document remains `DRAFT_FOR_OWNER_DECISION — HOLD`; implementation is not authorized.