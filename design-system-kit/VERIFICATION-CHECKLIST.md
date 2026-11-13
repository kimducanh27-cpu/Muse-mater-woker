# Process 06 — Verification Checklist

Every result below starts as `NOT RUN`. A checked paper scenario is not proof that Antigravity executed it correctly.

## Repository and workspace setup

- [ ] `.agents/skills/design-system/SKILL.md` is discoverable at workspace root.
- [ ] All three prompts exist under `prompts/06-DESIGN-SYSTEMS/`.
- [ ] Every prompt names the exact templates it must use.
- [ ] Templates `00`–`08` exist under `templates/06-DESIGN-SYSTEMS/`.
- [ ] Template `08` is referenced only as the frozen-output schema.
- [ ] `product/ux-design/UX_SPEC.md` is readable in the same workspace.
- [ ] Process 06 initiative ID equals the Process 05 initiative ID.
- [ ] No prompt-name collision selects the Process 05 review prompt.

## Entry-gate simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Process 05 Gate 3 not `APPROVED` | Stop; `NOT_VERIFIED` | NOT RUN |
| Process 05 lifecycle not `FROZEN` | Stop | NOT RUN |
| UX Spec hash differs from Process 05 `gate_3.frozen_artifact.sha256` | Stop; do not initialize | NOT RUN |
| Process 05 has an open Change Request | Stop; entry blocked | NOT RUN |
| Process 05 `source_process_04.frozen_artifact_sha256` is null | Stop; chain broken | NOT RUN |
| App Flow hash differs from the hash Process 05 recorded | Both sources `NOT_VERIFIED` | NOT RUN |
| Control File claims a predecessor schema or carries `SCHEMA_MIGRATED` | `NOT_VERIFIED`; no migration path in v1 | NOT RUN |
| `platform` block missing at initialization | Stop; platform is a recorded decision, not a default | NOT RUN |
| `platform.target` differs from the platform Process 07 is composing for | Downstream blocked | NOT RUN |

## Component admission simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| A component cites no screen | Gate 2 refuses | NOT RUN |
| A component cites a SCREEN ID absent from the frozen inventory | `NOT_VERIFIED`, not a near miss | NOT RUN |
| A component exists because Material 3 provides it | Gate 2 refuses; speculative | NOT RUN |
| A component exists for a hypothetical future screen | Gate 2 refuses | NOT RUN |
| A frozen screen cites no component and has no decision | Gate 2 refuses | NOT RUN |
| A frozen screen cites no component but a decision explains the composition | Permitted | NOT RUN |
| A component has no "when not to use this" statement | Gate 2 refuses | NOT RUN |
| An interaction state exists but is unstyled | Gate 2 refuses | NOT RUN |
| `components_defined` exceeds `components_cited` | Gate 2 refuses | NOT RUN |

## Token layering simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| A component token references a reference token | Gate 2 refuses; opts out of theming and contrast | NOT RUN |
| A system token is named after a colour ("blue") with no role | Naming defect; Gate 2 refuses | NOT RUN |
| A system token references another system token in a cycle | Gate 2 refuses | NOT RUN |
| A component token references a non-existent system token | Gate 2 refuses | NOT RUN |
| A value appears in the token contract but not in foundations | Gate 2 refuses | NOT RUN |
| A token has no forbidden-use entry where the role implies one | Review finding; `MINOR` | NOT RUN |

## Accessibility simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| A contrast pair is declared PASS with no resolved hex pair | Unmeasured; treated as failing | NOT RUN |
| A contrast pair is declared with no stated method | Unmeasured | NOT RUN |
| A required pair fails 4.5:1 | `CRITICAL`; Gate 2 refuses | NOT RUN |
| A failing pair is "fixed" by a per-component exception | Refused; the fix belongs in foundations or tokens | NOT RUN |
| A state is conveyed by colour alone | Gate 2 refuses | NOT RUN |
| `contrast_pairs_measured` is lower than `contrast_pairs_total` | Freeze refused | NOT RUN |
| A component has no target size in dp | Gate 2 refuses | NOT RUN |
| Announcement intent names an ARIA or Compose property | Boundary violation; intent only here | NOT RUN |

## Boundary simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Artifact 03 states where a component goes | `MAJOR`; `BLOCKER` if it covers most of the inventory | NOT RUN |
| Artifact 03 states a component's width on a screen | Boundary violation | NOT RUN |
| Any artifact contains final copy | Boundary violation; copy is Process 07 | NOT RUN |
| Any artifact contains Compose or theme code | Boundary violation | NOT RUN |
| A new screen, state or capability is introduced | `BLOCKER`; returns to Process 04 or 05 | NOT RUN |
| A Material 3 default is adopted without a citing screen | Speculative; Gate 2 refuses | NOT RUN |

## Gate and invalidation simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Gate 1 `status: APPROVED` with no `GATE_1_APPROVED` event | `NOT_VERIFIED` | NOT RUN |
| `gate_1.approved_state_seq` differs from the event's `state_seq` | `NOT_VERIFIED` | NOT RUN |
| `gate_1.decision_log_sha256` differs from the approval event snapshot | Gates 1–3 reopened | NOT RUN |
| Decision Log changes after Gate 2, any apparent scope | Gates 2–3 reopened | NOT RUN |
| A foundations decision is labeled `GATE_2` | `NOT_VERIFIED`; classify by semantic scope | NOT RUN |
| Tab 03 edits artifact 02 | Protocol violation; round invalid | NOT RUN |
| Tab 03 appends a decision to the log | Protocol violation | NOT RUN |
| Review round appended, Control update failed | Do not append again; `RECOVER REVIEW ROUND [N]` only | NOT RUN |
| `platform` field changed after Gate 1 | Gates 1–3 reopened; new design system required | NOT RUN |
| Coverage counter decreases without `INVALIDATED` | Tampering; stop | NOT RUN |

## Freeze simulations

| Scenario | Expected behavior | Result |
|---|---|---|
| Freeze with `review.round = 0` | Refused | NOT RUN |
| Draft differs from `DESIGN_SYSTEM.md` by anything other than the status line | `NOT_VERIFIED` | NOT RUN |
| `DESIGN_SYSTEM.md` contains a self-hash | Protocol violation | NOT RUN |
| Re-freeze with an existing `DESIGN_SYSTEM.v<N>.md` that differs | Refused | NOT RUN |
| Canonical write succeeds, Control write fails | `INCOMPLETE — NOT FROZEN` | NOT RUN |
| Downstream reads a FROZEN status line without recomputing the hash | Must refuse | NOT RUN |
| UX Spec changes after freeze | Gate 3 reopened, lifecycle `REVIEW_REQUIRED`, downstream prohibited | NOT RUN |

## Release decision

Do not label Process 06 production-ready until all mandatory live tests have evidence. Repository inspection is not live Antigravity verification.
