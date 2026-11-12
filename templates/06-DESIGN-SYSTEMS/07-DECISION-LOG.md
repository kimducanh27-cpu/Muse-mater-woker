# 07 — Decision Log

> Append-only. Owner: Tab 01 for `GATE_1` decisions, Tab 02 for `GATE_2`/`GATE_3`. Tab 03 is read-only.
> One initiative only. Never edit or delete a proposal or a status event.

## Immutable identity header

| Field | Value |
|---|---|
| Process | 06 |
| Initiative ID | `<must equal the Process 06 Control File and the verified Process 05 initiative ID>` |
| Initialized at local | `<timestamp>` |
| Initialized by Control event | `DECISION_LOG_UPDATED` / `INITIALIZATION` at `state_seq` `<n>` |

If this header is absent, unreadable or mismatched, the log is `NOT_VERIFIED`. Never rewrite the header and never adopt the file by hashing its current bytes.

---

## Proposal block — immutable, append once per DEC ID

### DEC-<NNNN> — <decision title>

| Field | Value |
|---|---|
| Proposal Event ID | `DLE-<NNNN>` |
| Status at proposal | `PROPOSED` |
| Affected gate | `GATE_1` / `GATE_2` / `GATE_3` |
| Affected artifacts | `01_DESIGN_FOUNDATIONS.md`, … |
| Affected IDs | `CMP-…`, `CP-…` |
| Raised by tab | `TAB_01` / `TAB_02` |
| Raised at local | `<timestamp>` |

**Decision statement.** What is being decided, in one paragraph.

**Alternatives considered.** Each alternative and why it was not chosen.

**Rationale.** Why this option, and what it costs.

**Consequence if not decided.** What stays blocked or ambiguous.

**Provenance.** The frozen screen or UX requirement that forces the decision, or the user instruction that raised it.

---

## Status event — append only after an explicit user command

### Status event — `DLE-<NNNN>`

| Field | Value |
|---|---|
| Event ID | `DLE-<NNNN>` |
| Event kind | `DECISION_STATUS_CHANGED` |
| DEC ID | `DEC-<NNNN>` |
| Status before | `PROPOSED` |
| Status after | `APPROVED` / `REJECTED` / `DEFERRED` |
| Exact user command | `APPROVE DESIGN DECISION DEC-<NNNN>` (or the matching reject/defer command) |
| User rationale | quoted verbatim from the user's message |
| User identity | user |
| Recorded at local | `<timestamp>` |
| Affected gate | |
| Affected artifacts and IDs | |
| Supersedes status event ID | `NONE` for the first event, otherwise the immediately preceding valid status event |

**Rules**

- The exact command must map to the resulting status.
- A rationale is mandatory. A command without a rationale is rejected.
- Do not append a duplicate when the requested status already equals the current status.
- A status event may not change the proposal's scope or affected gate. A scope change needs a new DEC ID.
- Every status event pairs one-to-one with a Control File `DECISION_LOG_UPDATED` event carrying the same IDs, kind, before/after status, affected gate, path and resulting hash.

## Reconstruction rule

Current status of a DEC ID is the status-after of its highest-sequence valid paired event. If only the proposal exists, status is `PROPOSED`. A broken chain makes that DEC ID `NOT_VERIFIED`, and it may not be used as approved policy.

A legacy inline status without a matching canonical event is `LEGACY_UNVERIFIED`. Preserve its bytes, do not treat it as approved.

## Decision index — maintain at the end of the file

| DEC ID | Title | Affected gate | Current status | Latest event ID |
|---|---|---|---|---|
| `DEC-<NNNN>` | | | `PROPOSED` | `DLE-<NNNN>` |
