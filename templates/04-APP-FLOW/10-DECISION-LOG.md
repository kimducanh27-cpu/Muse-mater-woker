# Process 04 — Append-only Flow Decision Log

This file is append-only. Never edit or delete an earlier decision entry. To change a decision, append a new event for the same DEC ID and explain what supersedes it.

## Decision entry template

### DEC-<NNN> — <short decision title>
- Status: PROPOSED / APPROVED / REJECTED / DEFERRED
- Raised by:
- Raised at local time:
- Owning tab: TAB_01 / TAB_02
- Affected gate: GATE_1 / GATE_2 / GATE_3
- Affected artifact paths and IDs:
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

A proposal remains PROPOSED until the user sends exact command \`APPROVE FLOW DECISION [DECISION-ID]\`. Append a new status event for approval; do not rewrite the proposal. A rejected or deferred option must not be treated as an approved policy. If the decision changes a source artifact, update that artifact and follow the invalidation matrix.

## Initial state
No material flow-policy decisions recorded yet.
