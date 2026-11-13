---
process: "04-app-flow"
initiative_id: "probe-8"
register_schema_version: 1
encoding: "UTF-8 without BOM"
line_endings: "LF"
serialization: "P04-CR-REGISTER-CANONICAL-V1"
---

# Process 04 — Change Request Register v1

This file is the **sole source of truth for Change Request business state**. It is append-only. The Control File stores commit receipts, sequence/checkpoint pointers and integrity evidence only; it MUST NOT duplicate per-CR statuses or authoritative blocking counts/lists.

## Immutable identity and serialization contract

- Process: 04
- Initiative ID: probe-8
- Register Schema Version: 1
- Encoding: UTF-8 without BOM.
- Line endings: LF (`\n`) only; CR (`\r`) bytes are forbidden.
- No trailing spaces or tabs on any line.
- Field names and order MUST match the canonical event schema.
- Each event ends with `event_end_marker: END_CRE` followed by LF.
- Event blocks are separated by exactly one blank line.
- The file ends with the canonical LF terminator.
- Readers reject noncanonical bytes; they MUST NOT normalize before hashing.

Do not populate or repair the identity header from an unverified source. A mismatched Initiative ID is `NOT_VERIFIED`.

## Initialization

A new Register is created from this template with the verified Initiative ID and no event blocks. Compute SHA-256 over the exact header bytes as `H_init`. The Control File must then record exactly one `CHANGE_REQUEST_REGISTER_INITIALIZED` event with `register_seq: 0`, `last_event_id: INITIALIZATION` and `last_verified_sha256: H_init`. Read both files back. The Register is not initialized/usable until that receipt is committed and verified. Normal CR events begin at sequence 1.

## Canonical event block schema

Each event is one immutable block with this field order; transition-specific evidence follows the common fields in the order specified by the Skill.

```yaml
### CRE-<NNNN>
change_request_event_id: CRE-<NNNN>
change_request_id: CR-<NNN>
register_seq: <positive_integer>
event_type: <canonical_event_type>
from_status: <state_or_NOT_APPLICABLE>
to_status: <state_or_NOT_APPLICABLE>
exact_user_command: <exact_command>
recorded_by_tab: TAB_01
timestamp_local: <real_Asia_Ho_Chi_Minh_timestamp>
submission_id: <id_or_NOT_APPLICABLE>
submission_payload_sha256: <sha256_or_NOT_APPLICABLE>
source_process: <P03_or_downstream_or_USER>
source_initiative_id: <verified_initiative_id>
source_artifact_path: <path_or_NOT_APPLICABLE>
source_artifact_sha256: <sha256_or_NOT_APPLICABLE>
affected_gate: <GATE_1_or_GATE_2_or_GATE_3_or_MULTIPLE>
affected_artifact_paths: []
control_state_seq_before_append: <actual_current_control_state_seq>
control_file_sha256_before_append: <actual_sha256>
previous_register_sha256: <prior_exact_full_file_sha256>
transition_evidence: {}
event_block_sha256: <lowercase_sha256_of_normalized_block>
event_end_marker: END_CRE
```

The stored `event_block_sha256` is calculated over the **normalized** event block: the exact bytes from `### CRE-<NNNN>` through the LF after `event_end_marker: END_CRE`, excluding the following blank separator, with the value of this field replaced by the exact sentinel `<HASH_OMITTED>` before hashing. The writer hashes the normalized block and then writes the resulting lowercase digest into the field; the reader replaces the stored digest with the same sentinel before recomputing. A block verified with the stored digest left in place is `NOT_VERIFIED`. This is the only permitted normalization in Register v1 — no other field, byte, whitespace or line ending may be adjusted before hashing. `previous_register_sha256` is SHA-256 of the exact entire Register bytes immediately before the event append.

A Register event MUST NOT contain `planned_control_state_seq`, a predicted committed Control `state_seq`, or `resulting_register_sha256`. The Control receipt owns those committed values.

## Canonical business states (13)

| State | Default blocking |
|---|---|
| `RECORDED` | Yes |
| `TRIAGE` | Yes |
| `NEEDS_CLARIFICATION` | Yes |
| `ACCEPTED_FOR_IMPLEMENTATION` | Yes |
| `IMPLEMENTED_PENDING_REAPPROVAL` | Yes |
| `RETURN_TO_P03` | Yes |
| `REVERSION_PENDING` | Yes |
| `REJECTED_WITH_NO_CHANGE` | No |
| `CANCELLED_NO_CHANGE` | No |
| `CANCELLED_AFTER_REVERSION` | No |
| `CLOSED_IMPLEMENTED` | No, only when bound to the valid current freeze |
| `DUPLICATE` | Derived from target |
| `SUPERSEDED` | Derived from target |

`NOT_VERIFIED` is an integrity condition, not a business state; it always blocks. `REFROZEN` is prohibited. A closed CR binds to one exact freeze tuple; a later change requires a new CR-ID.

## Canonical event types

- T01 `CR_RECORDED`
- T02 `CR_TRIAGE_STARTED`
- T03 `CR_CLARIFICATION_REQUESTED`
- T04 `CR_TRIAGE_RESUMED`
- T05 `CR_ACCEPTED_FOR_IMPLEMENTATION`
- T06 `CR_REJECTED_NO_CHANGE`
- T07 `CR_RETURNED_TO_P03`
- T08 `CR_RESUMED_FROM_P03`
- T09 `CR_P03_RETURN_RESOLVED_NO_UPSTREAM_CHANGE`
- T10 `CR_IMPLEMENTATION_RECORDED`
- T11 `CR_IMPLEMENTATION_REOPENED`
- T12 `CR_CLOSED_IMPLEMENTED`
- T13/T14 `CR_CANCELLED_NO_CHANGE`
- T15 `CR_REVERSION_STARTED`
- T16 `CR_CANCELLED_AFTER_REVERSION`
- T17 `CR_MARKED_DUPLICATE`
- T18 `CR_SUPERSEDED`
- Abort audit marker only: `CHANGE_REQUEST_EVENT_ABORTED` (not a business-state transition).

## Transition contract

Only T01–T18 in the canonical Skill are legal. Any unlisted edge fails closed.

| ID | From → To | Exact command | Actor | Key guard |
|---|---|---|---|---|
| T01 | Submission → `RECORDED` | `RECORD APP FLOW CHANGE SUBMISSION [SUBMISSION-ID]` | Tab 01 | New immutable submission/hash; source/initiative/duplicate checks pass. |
| T02 | `RECORDED` → `TRIAGE` | `START APP FLOW CHANGE TRIAGE [CR-ID]` | Tab 01 | Current status RECORDED; integrity VERIFIED. |
| T03 | `TRIAGE` → `NEEDS_CLARIFICATION` | `REQUEST CLARIFICATION FOR APP FLOW CHANGE [CR-ID]` | Tab 01 | Concrete questions and related artifact hashes recorded. |
| T04 | `NEEDS_CLARIFICATION` → `TRIAGE` | `RESUME APP FLOW CHANGE TRIAGE [CR-ID]` | Tab 01 | User response recorded. |
| T05 | `TRIAGE` → `ACCEPTED_FOR_IMPLEMENTATION` | `ACCEPT APP FLOW CHANGE [CR-ID]` | Tab 01 | P04 ownership; no unresolved conflict/cycle; scope/Gates/paths/pre-edit hashes captured. |
| T06 | `TRIAGE` → `REJECTED_WITH_NO_CHANGE` | `REJECT APP FLOW CHANGE NO CHANGE [CR-ID]` | Tab 01 | User rationale and proof relevant P04 bytes match intake snapshot. |
| T07 | `TRIAGE` → `RETURN_TO_P03` | `RETURN APP FLOW CHANGE TO P03 [CR-ID]` | Tab 01 | P03-owned scope; per-CR P03 Control/frozen hash snapshot. |
| T08 | `RETURN_TO_P03` → `TRIAGE` | `RESUME APP FLOW CHANGE AFTER P03 FREEZE [CR-ID]` | Tab 01 | P03 v2 APPROVED/FROZEN; new hash matches P03 Control and differs from this CR return snapshot. |
| T09 | `RETURN_TO_P03` → `TRIAGE` | `RESOLVE P03 RETURN WITHOUT UPSTREAM CHANGE [CR-ID]` | Tab 01 | User rationale; P03 remains frozen at this CR exact return snapshot. |
| T10 | `ACCEPTED_FOR_IMPLEMENTATION` → `IMPLEMENTED_PENDING_REAPPROVAL` | `RECORD APP FLOW CHANGE IMPLEMENTATION [CR-ID]` | Tab 01 | Only accepted files changed; required Gate 1/2 approvals are new and later than acceptance. |
| T11 | `IMPLEMENTED_PENDING_REAPPROVAL` → `ACCEPTED_FOR_IMPLEMENTATION` | `REOPEN APP FLOW CHANGE IMPLEMENTATION [CR-ID]` | Tab 01 | Tab 03 blocker or Owner correction; evidence/Finding IDs. |
| T12 | `IMPLEMENTED_PENDING_REAPPROVAL` → `CLOSED_IMPLEMENTED` | `CLOSE IMPLEMENTED APP FLOW CHANGE [CR-ID]` | Tab 01 | Valid Freeze event; CR belongs to batch; exact frozen version/sequence/hash verified. |
| T13 | RECORDED/TRIAGE/NEEDS_CLARIFICATION → `CANCELLED_NO_CHANGE` | `CANCEL APP FLOW CHANGE [CR-ID]` | Tab 01 | Pre-implementation state; relevant P04 bytes unchanged. |
| T14 | `ACCEPTED_FOR_IMPLEMENTATION` → `CANCELLED_NO_CHANGE` | `CANCEL APP FLOW CHANGE [CR-ID]` | Tab 01 | Every relevant byte equals T05 snapshot; otherwise forbidden. |
| T15 | `ACCEPTED_FOR_IMPLEMENTATION` / `IMPLEMENTED_PENDING_REAPPROVAL` → `REVERSION_PENDING` | `START APP FLOW CHANGE REVERSION [CR-ID]` | Tab 01 | User cancellation after byte change; baseline hashes recorded. |
| T16 | `REVERSION_PENDING` → `CANCELLED_AFTER_REVERSION` | `COMPLETE APP FLOW CHANGE REVERSION [CR-ID]` | Tab 01 | Bytes restored and all affected Gates reapproved; Gate 3 review/freeze rerun if touched. |
| T17 | RECORDED/TRIAGE/NEEDS_CLARIFICATION → `DUPLICATE` | `MARK APP FLOW CHANGE DUPLICATE [CR-ID] OF [CANONICAL-ID]` | Tab 01 | Valid same-initiative target; no self/cycle; open blocker or exact closed-scope coverage. |
| T18 | Eligible pre-implementation CR → `SUPERSEDED` | `SUPERSEDE APP FLOW CHANGE [OLD-ID] WITH [NEW-ID]` | Tab 01 | Valid open successor; no cycle; complete approved scope inheritance if bytes changed. |

**CL-04:** No `ACCEPTED_FOR_IMPLEMENTATION → TRIAGE` or `→ NEEDS_CLARIFICATION` edge exists. Do not add T19. If no bytes changed and accepted CR is cancelled, use T14 and submit a new linked CR. If bytes changed, use T15/T16. Do not route around the closed transition table.

## Receipt units, hashes and commits

Canonical byte rules: UTF-8 without BOM, LF only, no CR, no trailing spaces/tabs, exact field order, one blank line between events and exact event terminator. Hashes are lowercase SHA-256 of exact on-disk bytes.

- Normal commit unit: one business event at sequence k + one `CHANGE_REQUEST_REGISTER_UPDATED` receipt. Receipt binds initiative, CR-ID, CRE-ID, register_seq, prior hash, event-block hash, resulting full Register hash and Control state_seq.
- Abort commit unit: exactly two consecutive Register events at k and k+1 (staged business event, then abort marker) + exactly one `CHANGE_REQUEST_EVENT_ABORTED` receipt. No normal update receipt may exist for either member.
- In abort unit, staged event links from H(k-1); abort marker links from intermediate H(k); final full-file hash is H(k+1). H(k) is internal only and never a committed checkpoint. Receipt binds H(k-1), H(k), H(k+1), both IDs/sequences/event-block hashes, status_effect NONE and receipt state_seq. Control pointer advances directly from k-1 to k+1.
- Next event after an abort unit is k+2 and links from H(k+1). Readers verify the complete history from initialization anchor; final hash alone is insufficient.

## Recovery

`RECOVER CHANGE REQUEST EVENT [CRE-ID]` applies only to exactly one complete staged business event whose trusted prefix and next sequence verify and whose business preconditions still pass on disk. It writes only the missing receipt at the next available Control sequence.

`RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` applies only to exactly two complete consecutive unreceipted events after the trusted checkpoint: staged event and exact abort marker; both hash edges and final hash verify; no later event/receipt exists; Control pointer still equals trusted pre-pair checkpoint. It writes only the missing receipt; never appends a second marker.

Partial/malformed event or abort marker, duplicate/orphan receipt, unexpected tail, sequence gap or hash mismatch is `NOT_VERIFIED`; preserve evidence and restore/reconcile from a trusted backup. Never truncate or rewrite historical append-only events.

## Initialization and migration

Initialize a header-only Register even when there are zero CRs. Verify P03 v2 identity/frozen hash; confirm no conflict; create exact template bytes; compute H_init; append one Control `CHANGE_REQUEST_REGISTER_INITIALIZED` receipt with register_seq 0 and last_event_id INITIALIZATION; read both files back. Zero-CR v4 workspace must have non-null hash and seq 0. Empty file, identity mismatch, unexpected CR events with null pointer, or missing Register with a non-null pointer is NOT_VERIFIED.

v3→v4 migration requires exactly one explicit Owner command: `MIGRATE APP FLOW CONTROL V3 TO V4 WITH ZERO EXTERNAL CRS` or `MIGRATE APP FLOW CONTROL V3 TO V4 WITH PENDING SUBMISSIONS`. Do not infer absence of unrecorded external CRs from `change_requests: []`. Before modification, create a byte-preserving full workspace backup and `ARCHIVE_MANIFEST.md` with path, size, SHA-256, schema, initiative, source HEAD, timestamp and destination; verify every archived file. Preserve v3 Gate approval only when event sequence and all bound artifact/Decision Log/Review/draft/frozen/P03 hashes verify; otherwise reopen conservatively.

Construct a complete temporary v4 Control File with sequential distinct Control events `SCHEMA_MIGRATED` (3→4, explicit command/attestation and manifest hash) and `CHANGE_REQUEST_REGISTER_INITIALIZED` (seq 0, INITIALIZATION, H_init). Validate then perform one complete same-filesystem Control File replacement. Read both files back. If interrupted before replacement, keep v3 canonical and quarantine only the uncommitted Register. If replacement is ambiguous, read/verify both; if corrupt, restore full verified v3 archive and restart. Legacy v3 readers fail closed on v4. A historical v3 Freeze does not retroactively close any CR.

## P03 boundary and three-tab ownership

P03 remains schema v2 and read-only to P04. Each CR returned to P03 stores its own returned P03 Control and frozen hashes. T08 compares a new P03 frozen hash with that CR return snapshot and actual P03 v2 Control; T09 resolves no-upstream-change only with user rationale and exact equality to that CR return snapshot. Multiple CRs may resume against one new P03 freeze.

- Tab 01: CR Coordinator, sole Register writer; validates source/hash/idempotency, assigns CR-ID, triages, handles all CR lifecycle and post-Freeze closure.
- Tab 02: performs assigned Gate 2 work; Register read-only; cannot independently change CR business status.
- Tab 03: independent review and mechanical Freeze; Register read-only; cannot write CR business status or close batch CRs.
- Handoff is persisted to disk; every tab is a fresh conversation and re-reads files. Chat memory is not evidence. One logical writer at a time.

## Freeze batch and downstream eligibility

Freeze Stage A: Tab 03 verifies the current Register/Control/Review snapshot and refuses states that are not eligible. It writes the frozen artifact and `GATE_3_FROZEN` receipt only. Downstream remains blocked while implementation CRs remain `IMPLEMENTED_PENDING_REAPPROVAL`.

Freeze Stage B: Tab 01 verifies the exact Freeze event/version/sequence/hash/Review snapshot, then appends an individual `CR_CLOSED_IMPLEMENTED` Register event and individual Control receipt for each implementation CR in the batch. `CLOSE IMPLEMENTED APP FLOW CHANGES FOR FREEZE [FROZEN-VERSION]` is a convenience command that expands to per-CR closures. A partial batch remains downstream-blocking; resume only uncommitted closures. Downstream is eligible only when all expected CRs are closed against the same frozen version, Gate 3 state_seq and APP_FLOW SHA-256 and reconstructed blocking set is empty.

Frozen version starts at 1 and increments by exactly one per valid new Freeze. Archive the prior output as APP_FLOW.v<N>.md. Refuse no-op re-freeze when source/artifact/Decision Log/Review hashes and CR state are unchanged and no accepted implementation awaits publication.

### CRE-0001
change_request_event_id: CRE-0001
change_request_id: CR-001
register_seq: 1
event_type: CR_RECORDED
from_status: NONE
to_status: RECORDED
exact_user_command: RECORD APP FLOW CHANGE SUBMISSION SUB-001
recorded_by_tab: TAB_01
timestamp_local: 2026-11-12T18:04:42+07:00
submission_id: SUB-001
submission_payload_sha256: NOT_APPLICABLE
source_process: NOT_APPLICABLE
source_initiative_id: NOT_APPLICABLE
source_artifact_path: NOT_APPLICABLE
source_artifact_sha256: NOT_APPLICABLE
affected_gate: NOT_APPLICABLE
affected_artifact_paths: []
control_state_seq_before_append: NOT_APPLICABLE
control_file_sha256_before_append: NOT_APPLICABLE
previous_register_sha256: 7252fa37d800a70714c7cafe20ff9388c91c613d30b4d406c4c4a23ed7a2bc99
transition_evidence: {}
event_block_sha256: 03d756a98500219c2f6b1fa160530b1b29085a9c34f3146470b39f5280bc5466
event_end_marker: END_CRE
