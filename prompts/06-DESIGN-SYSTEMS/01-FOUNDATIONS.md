# Tab 01 — Foundations and Tokens

You are running **Process 06 Design Systems, Tab 01** in a fresh conversation.

## Before anything else

1. Read `.agents/skills/design-system/SKILL.md` in full.
2. Read `product/ux-design/00_UX_CONTROL.md` and verify: `initiative_id` present; `gate_3.status = APPROVED`; `lifecycle_status = FROZEN`; `gate_3.frozen_artifact.path` equals `product/ux-design/UX_SPEC.md`; actual SHA-256 equals `gate_3.frozen_artifact.sha256`; no open Change Request; `source_process_04.frozen_artifact_sha256` non-null and equal to the actual SHA-256 of `product/app-flow/APP_FLOW.md`.
3. Read `product/ux-design/UX_SPEC.md` — every screen, every state, every accessibility requirement.
4. Initialize or verify `product/design-system/00_DS_CONTROL.md` from `templates/06-DESIGN-SYSTEMS/00-DS-CONTROL.md`, including the `platform` block.
5. Initialize or verify `product/design-system/07_DECISION_LOG.md` with its immutable identity header.

If any check in step 2 fails, stop and report the exact missing evidence.

## Your job

Produce `product/design-system/01_DESIGN_FOUNDATIONS.md` from template `01`.

- Colour as **roles**, each with a "must not be used for" column. A role without a prohibition will be used for everything within a week.
- Type scale with a stated ratio and the role of each step.
- Spacing, radius, elevation and motion scales, each with a stated use.
- On Android: elevation is tonal, state layers are a platform behaviour, and dynamic colour is a decision (adopted or not) with a rationale.
- Every value must name the role it serves and where a screen would use it.

This is the first artifact in the sequence allowed to contain concrete values. Do not flinch from that: a foundation that refuses to commit to a number has not decided anything.

## What you must not do

- Do not define components. That is Tab 02.
- Do not describe screen layout, regions or placement.
- Do not write final copy.
- Do not write code, Compose snippets or theme files.
- Do not adopt a Material 3 value merely because it exists. Either justify it against a screen requirement or leave it out.

## Gate 1

Gate 1 requires, shown explicitly rather than asserted:

- Every foundation value has a role statement and a stated use.
- No value exists without a role.
- The Decision Log hash equals the non-null `decision_log.latest_sha256`.
- Both source statuses `VERIFIED`.

Then wait for exactly:

```
APPROVE DESIGN FOUNDATIONS
```

One Control File update: set `gate_1.approved_state_seq`, `gate_1.decision_log_sha256`, the coverage snapshot, and append `GATE_1_APPROVED` with artifact 01's path and hash. Read back and verify before reporting success.

Stop after Gate 1. Do not start Tab 02.
