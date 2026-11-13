# Process 04 — Append-only Flow Decision Log

This file is append-only and belongs to exactly one initiative. Never edit, delete, reorder or rewrite an earlier proposal or status event. Every append to this file must have exactly one matching `DECISION_LOG_UPDATED` event in the Process 04 Control File. The Control File event supplies the committed sequence and resulting whole-file SHA-256; do not place a self-referential whole-file hash inside this file.

## Immutable log identity

- Process: 04
- Initiative ID: <exact initiative_id from the verified Process 04 and Process 03 Control Files>

Populate this identity only when initializing a new log. Once written, do not change it. A pre-existing log with a missing or different initiative ID is NOT_VERIFIED; do not adopt it by hashing or silently repair it.

## Decision proposal template

### DEC-<NNN> — <short decision title>
- Proposal Event ID: DLE-<NNNN> (unique across this log)
- Status at proposal: PROPOSED (immutable)
- Raised by:
- Raised at local time:
- Owning tab: TAB_01 / TAB_02
- Affected gate (derived, not self-selected): GATE_1 / GATE_2 / GATE_3
- Affected artifact paths and IDs:
- Initiative ID (must equal immutable log identity):
- Decision question:
- Options considered:
- Recommended option:
- Evidence/source:
- Supersedes / superseded by:

The proposal block is immutable after append. Do not change `Status at proposal: PROPOSED` or add the user's eventual outcome into the proposal block. Record the outcome only as a separate status event below.

Classify `affected_gate` from actual semantic scope: 01/02 or capability-to-task mapping = GATE_1; only 03–06 = GATE_2; only review/draft 07/08 = GATE_3; mixed scope uses the earliest gate. A proposed Process 03 capability/scope change must return to Process 03. The owning tab must independently validate the label against affected paths/IDs and decision text; a mismatch or ambiguity is NOT_VERIFIED.

## Append-only decision status event template

Append one new block for every user-authorized status outcome. Never modify the original proposal or a prior status event.

### Status event — DLE-<NNNN>
- Event ID: DLE-<NNNN> (unique across this log)
- Event kind: DECISION_STATUS_CHANGED
- Decision ID: DEC-<NNN>
- Status before update: PROPOSED / APPROVED / REJECTED / DEFERRED
- Status after update: APPROVED / REJECTED / DEFERRED
- Exact user command: APPROVE FLOW DECISION <DEC-ID> / REJECT FLOW DECISION <DEC-ID> / DEFER FLOW DECISION <DEC-ID>
- Decided by: user
- User rationale:
- Decided at local time:
- Affected gate: <must exactly match the immutable proposal>
- Affected artifact paths and IDs: <must exactly match the immutable proposal>
- Supersedes status event ID: NONE / <immediately preceding status-event DLE-ID>

The exact command must map to the status after update: APPROVE → APPROVED, REJECT → REJECTED, DEFER → DEFERRED. A status event requires the user's rationale in the same message as the exact command. The first status event must name PROPOSED as its previous status and NONE as its superseded event. Every later event must name the immediately preceding valid status-event ID and its effective status. Do not append an event when the requested status already equals the current status. A new outcome may supersede a prior outcome only through a new explicit user command and a new linked status event.

The affected gate and affected artifact paths/IDs are inherited from the immutable proposal and must not change in a status event. If the scope or decision meaning changes, create a new DEC ID and link the supersession; do not repurpose the old proposal.

## Deterministic status reconstruction

1. A new proposal starts at PROPOSED only when its Proposal Event ID has one matching, valid Control File `DECISION_LOG_UPDATED` event with `decision_event_kind: PROPOSAL_CREATED`, `decision_status_before_update: NOT_APPLICABLE`, `decision_status_after_update: PROPOSED`, the same DEC ID, affected gate, path and resulting log hash.
2. Each status event must have exactly one matching Control File event with the same `decision_log_event_id`, `decision_event_kind: DECISION_STATUS_CHANGED`, DEC ID, status-before/status-after values, affected gate, path and resulting log hash.
3. The Control File `state_seq` orders matched events. For a DEC ID, the current status is the `decision_status_after_update` from its highest-sequence valid matched event. If no status event exists, the status remains PROPOSED.
4. The status-event chain must be continuous: each event's status-before value and superseded event ID must match the immediately preceding valid status event. Event IDs must be unique and paired one-to-one. Missing, duplicate, malformed, out-of-order or mismatched events make that DEC ID NOT_VERIFIED; do not treat it as approved policy.
5. Only a current, verified APPROVED decision may define flow policy. REJECTED, DEFERRED, PROPOSED or NOT_VERIFIED entries are not approved rules. A DEFERRED capability may be omitted only when the affected CAP ID and scope impact are explicit and Process 03 boundaries remain intact.
6. A legacy proposal without a Proposal Event ID, or a legacy inline status/user-decision field without a matching canonical status event and Control File event, is not evidence of approval. Preserve its bytes; treat its outcome as LEGACY_UNVERIFIED. If still needed, create a new canonical proposal with a new DEC ID and obtain a fresh explicit user outcome.

## Initial state

No material flow-policy decisions recorded yet. The first appended proposal starts the log; its write/read-back/hash and Control File event transaction must complete before the proposal is trusted.
