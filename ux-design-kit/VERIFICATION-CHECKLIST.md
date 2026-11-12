# Process 05 — Verification Checklist

This checklist distinguishes repository/paper checks from live runtime verification. A checked paper scenario is not proof that Antigravity executed it correctly. Every result below starts as `NOT RUN`.

## Repository and workspace setup

- [ ] Repository is at workspace root; `.agents/skills/ux-design/SKILL.md` is discoverable.
- [ ] All three prompts exist under `prompts/05-UX-DESIGN/`.
- [ ] Every prompt names the exact templates it must use.
- [ ] Templates `00`–`09` exist under `templates/05-UX-DESIGN/`.
- [ ] Template `09` is referenced only as the frozen-output schema, never as a working artifact.
- [ ] Decision Log template defines an immutable identity header, immutable proposals and append-only status events with unique DLE IDs.
- [ ] Review template records pre-append Control sequence, pre-append Control hash and previous review hash.
- [ ] `product/app-flow/APP_FLOW.md` is readable in the same workspace.
- [ ] Process 05 initiative ID equals the Process 04 initiative ID.
- [ ] No prompt-name collision causes the Process 04 review prompt to be selected.

## Entry-gate simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Process 04 Gate 3 not `APPROVED` | Stop; `NOT_VERIFIED` | NOT RUN |
| Process 04 lifecycle not `FROZEN` | Stop | NOT RUN |
| `APP_FLOW.md` hash differs from Process 04 `gate_3.frozen_artifact.sha256` | Stop; do not initialize | NOT RUN |
| Process 04 Control File or App Flow missing/unreadable | Stop | NOT RUN |
| Initiative IDs conflict | Stop; do not overwrite either initiative | NOT RUN |
| Process 04 has a non-empty blocking Change Request set | Stop; entry blocked | NOT RUN |
| Process 04 `source_process_03.frozen_artifact_sha256` is null | Stop; chain broken, source `NOT_VERIFIED` | NOT RUN |
| Product Definition hash differs from the hash Process 04 recorded | Stop; both sources `NOT_VERIFIED` | NOT RUN |
| Process 04 Control File uses an older schema than the workspace was initialized against | Stop; do not silently re-read | NOT RUN |
| Control File claims a predecessor schema or carries `SCHEMA_MIGRATED` | `NOT_VERIFIED`; no migration path exists in v1 | NOT RUN |
| Sources verified, no artifacts yet | Eligible to initialize Process 05 workspace | NOT RUN |

## Template and boundary simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Artifact 01 has prose but no per-screen table | Gate 1 refuses | NOT RUN |
| A screen in the Process 04 inventory has no entry in 01 | Gate 1 refuses; missing screen is a defect | NOT RUN |
| An entry cites a SCREEN ID that does not exist upstream | Gate 1 refuses; scope violation | NOT RUN |
| A screen has two primary actions | Gate 1 refuses; hierarchy unresolved | NOT RUN |
| A screen entry cites no capability ID | Gate 1 refuses | NOT RUN |
| Structural block contains a colour or size value | Gate 1 refuses; boundary violation | NOT RUN |
| Structural block contradicts the ordered hierarchy list | Gate 1 refuses; the list is authoritative | NOT RUN |
| Structural block is an image or external file reference | Gate 1 refuses | NOT RUN |
| Artifact 01 names a UI component ("button", "card", "modal") | Gate 2 refuses; component-name audit fails | NOT RUN |
| A component name appears inside a quoted source excerpt, marked as quoted | Permitted | NOT RUN |
| Artifact 02–05 contains a hex value, font size or spacing value | Gate 2 refuses | NOT RUN |
| A state in the Process 04 matrix has no row for a screen it applies to | Gate 2 refuses | NOT RUN |
| A row exists for a state the Process 04 matrix does not define | Gate 2 refuses; Change Request to Process 04 required | NOT RUN |
| A failure state has no recovery affordance and no decision | Gate 2 refuses | NOT RUN |
| A pattern is cited but not defined in 02 | Gate 2 refuses | NOT RUN |
| A pattern is defined but never cited and not marked reserved | Gate 2 refuses | NOT RUN |
| A capability in the frozen scope is served by no screen and has no deferral decision | Gate 2 refuses | NOT RUN |
| Artifact 04 contains final copy instead of intent | Review finding; `MAJOR` | NOT RUN |
| Artifact 05 chooses a token or a colour value | Gate 2 refuses; requirement vs token confusion | NOT RUN |

## Gate and invalidation simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Gate 1 `status: APPROVED` with no `GATE_1_APPROVED` event | `NOT_VERIFIED`; sequence anchor missing | NOT RUN |
| `gate_1.approved_state_seq` differs from the event's `state_seq` | `NOT_VERIFIED`; gate not current | NOT RUN |
| `gate_1.decision_log_sha256` differs from the approval event snapshot | Gates 1–3 reopened | NOT RUN |
| Decision Log changes with `affected_gate: GATE_1` after Gate 1 approval | Gates 1–3 reopened; return to Tab 01 | NOT RUN |
| Decision Log changes after Gate 2 approval, any apparent scope | Gates 2–3 reopened | NOT RUN |
| A decision affecting 01 is labeled `GATE_2` | `NOT_VERIFIED`; classify by semantic scope, not label | NOT RUN |
| Tab 03 appends a decision to the Decision Log | Protocol violation; review round invalid | NOT RUN |
| Tab 03 edits artifact 03 | Protocol violation; round invalid, finding recorded | NOT RUN |
| Review round appended but Control update failed | Do not append again; `RECOVER REVIEW ROUND [N]` only with exact preconditions | NOT RUN |
| `REVIEW_ROUND_RECORDED` exists but review hash differs | `NOT_VERIFIED` | NOT RUN |
| Draft hash differs from the latest round's draft hash | Freeze refused | NOT RUN |
| Coverage counter lower than source count | Freeze refused; silent shrink | NOT RUN |
| Open `MAJOR` finding with no user acceptance record | Freeze refused | NOT RUN |
| `ACCEPT RESIDUAL RISK` sent without rationale | Rejected; no record written | NOT RUN |
| `ACCEPT RESIDUAL RISK` targets a `BLOCKER` | Rejected; cannot be accepted | NOT RUN |
| `GO` verdict followed by silence | Freeze refused; explicit command required | NOT RUN |

## Freeze simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Freeze with `review.round = 0` | Refused | NOT RUN |
| Draft differs from `UX_SPEC.md` by anything other than the status line | `NOT_VERIFIED` | NOT RUN |
| `UX_SPEC.md` contains a self-hash | Protocol violation; hash belongs in the Control File | NOT RUN |
| Re-freeze with an existing `UX_SPEC.v<N>.md` | Refused unless the archive is byte-identical | NOT RUN |
| Canonical write succeeds, Control write fails | Report `INCOMPLETE — NOT FROZEN` | NOT RUN |
| Downstream reads a FROZEN status line without recomputing the hash | Must refuse; status line is not proof | NOT RUN |
| App Flow changes after freeze | Gate 3 reopened, lifecycle `REVIEW_REQUIRED`, downstream prohibited | NOT RUN |

## Release decision

Do not label Process 05 production-ready until all mandatory live tests have evidence. Record limitations and unresolved defects in independent review. Repository inspection is not live Antigravity verification.
