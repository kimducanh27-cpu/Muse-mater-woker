# P04 — Status reconciliation, 2026-11-12

**Purpose.** The approved remediation plan and the owner decision register now make contradictory statements about authorisation. The plan's own Section 0.2 requires that a workspace with disagreeing artifacts be treated as `NOT_VERIFIED` until the disagreement is corrected through an approved change. This document is that correction.

**What it is not.** It is not a rewrite of the plan. `app-flow-kit/specs/P04-REMEDIATION-PLAN-v0.3.1.md` is an approved artifact with a recorded SHA-256 (`cb982ff1ed2592ea44e8e5173c887b32143b13023c91553ee013ab4839cc32c6`); editing it would invalidate its own provenance. Every statement below was true when the plan was written. What changed is the world, not the document.

**Authority order used.** Plan Section 0.2: the canonical Skill wins for interpretation of the contract; the owner decision register wins for the fact of authorisation, because it is the record that the plan itself defers to (`Approval authority: Repository Owner`).

## 1. Stale statements and their supersession

| Plan location | Statement | Status now | Authority |
|---|---|---|---|
| Line 9, header table | `Status: DRAFT_FOR_OWNER_DECISION — HOLD` | Historical. The plan was held at authoring time. | Decision register: `Decision status: ALL OWNER DECISIONS APPROVED` |
| Line 9, header table | `Implementation authority: Not granted by this document` | Still literally true — the plan never granted it. Authority came from a separate owner instruction. | Decision register §1: authorisation granted by explicit Owner instruction `triển full luôn đi` |
| Line 947 (change log, v0.3) | "Owner decisions remain PENDING." | Historical | Same |
| Line 948 (change log, v0.3.1) | "Owner decisions remain PENDING." | Historical | Same |
| Line 957 (review scope) | "ADR-P04-01…ADR-P04-10 and CL-01…CL-05 remain `PENDING` until the Repository Owner explicitly decides. The document remains `DRAFT_FOR_OWNER_DECISION — HOLD`; implementation is not authorized." | Historical | Decision register §3: 10/10 ADR + 5/5 CL approved; 16/16 total after ADR-P04-11 |
| Line 938 | "No repository files were modified. No commit, branch, pull request, migration, or runtime action was performed." | True of the plan's authoring session only. Implementation happened afterwards on a dedicated branch. | `P04-IMPLEMENTATION-RECORD-v0.3.1.md` |
| Section 18 | "All 20 static stress scenarios … are present in the Verification Checklist" | Superseded by a superset: 22 scenarios. | ADR-P04-11 added ST-21 and ST-22 |

## 2. What is genuinely still open

Reconciliation removes a documentation contradiction. It does not convert any unexecuted work into a pass.

| Item | Status | Why it matters |
|---|---|---|
| Live Windows Antigravity runtime (Phase 7) | `NOT RUN` | No workspace with a frozen Process 03 source and a real initiative has been executed |
| Register writer / migration routine | Not implemented | The sentinel rule is specified, never executed against real bytes |
| Merge to `main` | Not authorised | Decision register §5 and the implementation record both withhold it |
| P04-IMP-01 | Resolved at specification level | ADR-P04-11; see implementation record |

## 3. A second contradiction found during this review

The canonical Skill contained two migration statements that could not both be true:

- The v3-era body said migration "is permitted only after the user sends exactly `MIGRATE APP FLOW CONTROL V2 TO V3`".
- The Schema v4 section requires `MIGRATE APP FLOW CONTROL V3 TO V4 WITH ZERO EXTERNAL CRS` or `… WITH PENDING SUBMISSIONS`.

A Tab 01 reader would have hit the first statement and concluded the only legal migration command is the v2→v3 one, then rejected a correct v4 migration as a protocol violation. The body now states the migration chain explicitly: v2 → v3 → v4, no shortcut, no substituted command, and a schema-v3 file receiving the v2→v3 command is `NOT_VERIFIED` rather than a no-op.

This is the failure mode the v4 patch invited: the contract was **appended** as a section rather than integrated into the body, so present-tense v3 language survived underneath. Any future schema revision should assume the same defect exists until the body is re-read end to end.

## 4. Verification performed

- Abort and recovery commands required by plan Sections 5.3–5.6 exist in the Skill: `RECOVER CHANGE REQUEST EVENT [CRE-ID]`, `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]`.
- `CHANGE_REQUEST_EVENT_ABORTED` receipt fields in the Control template match plan Section 5.6 step 5.
- v3→v4 migration commands exist with the backup and manifest requirements.
- ST-08 now names the exact recovery command instead of paraphrasing it.

No statement in this document changes a `NOT RUN` to a `PASS`.
