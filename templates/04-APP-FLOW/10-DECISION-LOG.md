# Process 04 — Append-only Flow Decision Log

This file is append-only and belongs to exactly one initiative. Never edit or delete an earlier decision entry. To change a decision, append a new event for the same DEC ID and explain what supersedes it.

## Immutable log identity

- Process: 04
- Initiative ID: <exact initiative_id from the verified Process 04 and Process 03 Control Files>

Populate this identity only when initializing a new log. Once written, do not change it. A pre-existing log with a missing or different initiative ID is NOT_VERIFIED; do not adopt it by hashing or silently repair it.

## Decision entry template

### DEC-<NNN> — <short decision title>
- Status: PROPOSED / APPROVED / REJECTED / DEFERRED
- Raised by:
- Raised at local time:
- Owning tab: TAB_01 / TAB_02
- Affected gate (derived, not self-selected): GATE_1 / GATE_2 / GATE_3
- Affected artifact paths and IDs:
- Initiative ID (must equal immutable log identity):
- Decision question:
- Options considered:
- Recommended option:
- User decision:
- Rationale:
- Exact user command: APPROVE FLOW DECISION <DEC-ID> / REJECT FLOW DECISION <DEC-ID> / DEFER FLOW DECISION <DEC-ID>
- Decided by:
- Decided at local time:
- Evidence/source:
- Supersedes / superseded by:

Classify `affected_gate` from actual semantic scope: 01/02 or capability-to-task mapping = GATE_1; only 03–06 = GATE_2; only review/draft 07/08 = GATE_3; mixed scope uses the earliest gate. A proposed Process 03 capability/scope change must return to Process 03. The owning tab must independently validate the label against affected paths/IDs and decision text; a mismatch or ambiguity is NOT_VERIFIED.

A proposal remains PROPOSED until the user sends exactly one outcome command with a rationale: `APPROVE FLOW DECISION [DECISION-ID]`, `REJECT FLOW DECISION [DECISION-ID]`, or `DEFER FLOW DECISION [DECISION-ID]`. Append a new status event for the matching status APPROVED, REJECTED or DEFERRED; never rewrite the original proposal. Only APPROVED decisions may define current flow policy. A DEFERRED decision may justify omitting an approved capability from the current flow only when the affected capability and scope impact are explicit and the Process 03 boundary is preserved. If the decision changes a source artifact, update that artifact and follow the invalidation matrix.

## Initial state
No material flow-policy decisions recorded yet.
