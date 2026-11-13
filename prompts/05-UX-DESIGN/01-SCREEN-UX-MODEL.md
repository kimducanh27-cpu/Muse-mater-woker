# Tab 01 — Screen UX Model

You are running **Process 05 UX Design, Tab 01** in a fresh conversation. Transfer context through files, not chat history.

## Before anything else

1. Read `.agents/skills/ux-design/SKILL.md` in full.
2. Read `product/app-flow/00_APP_FLOW_CONTROL.md` and verify, in order: `initiative_id` present; `gate_3.status = APPROVED`; `lifecycle_status = FROZEN`; `gate_3.frozen_artifact.path` equals `product/app-flow/APP_FLOW.md`; actual SHA-256 of that file equals `gate_3.frozen_artifact.sha256`; reconstructed blocking Change Request set empty; `source_process_03.frozen_artifact_sha256` non-null and equal to the actual SHA-256 of `product/definition/PRODUCT_DEFINITION.md`.
3. Read `product/app-flow/APP_FLOW.md` — specifically the task model, screen inventory and state matrix.
4. Initialize or verify `product/ux-design/00_UX_CONTROL.md` from `templates/05-UX-DESIGN/00-UX-CONTROL.md`. If it already exists, verify it rather than recreating it.
5. Initialize or verify `product/ux-design/08_DECISION_LOG.md` from `templates/05-UX-DESIGN/08-DECISION-LOG.md`, including its immutable identity header.

If any check in step 2 fails, stop and report the exact missing evidence. Do not begin work on a partially verified source.

## Your job

Produce `product/ux-design/01_SCREEN_UX_MODEL.md` from `templates/05-UX-DESIGN/01-SCREEN-UX-MODEL.md`.

- Enumerate every SCREEN ID in the frozen screen inventory. Every screen gets exactly one entry. No screen is merged, renamed or invented.
- For each screen: the user's goal, exactly one primary action, ordered secondary actions, information hierarchy in reading order, entry expectation, exit guarantee, the capability IDs it serves, and the cognitive load risk.
- You may include one structural block per screen, within the rules in the Skill: fenced `text`, at most 100 characters wide, structural only, never authoritative, never containing colour, type, size or spacing.
- Record only `GATE_1` decisions. A decision about patterns, states, content or accessibility belongs to Tab 02 and must not be appended here.

## What you must not do

- Do not name a UI component. Not "button", not "card", not "modal", not "toast".
- Do not specify colour, typography, spacing, radius, elevation or iconography.
- Do not add a screen, a state or a capability.
- Do not write final copy.
- Do not proceed to patterns, states, content or accessibility.

## Gate 1

Gate 1 requires all of the following, verified by set comparison and shown explicitly:

- Every SCREEN ID present exactly once; no unknown screen ID.
- Every entry cites at least one approved capability ID.
- Exactly one primary action per screen.
- Structural blocks, if used, satisfy the Skill's rules.
- `08_DECISION_LOG.md` hash equals the non-null `decision_log.latest_sha256` in the Control File.
- Both source statuses `VERIFIED`.

Then wait. The gate opens only when the user sends exactly:

```
APPROVE SCREEN UX MODEL
```

Record it in one Control File update: set `gate_1.approved_state_seq` to the new committed `state_seq`, set `gate_1.decision_log_sha256` to the actual log hash, write the coverage snapshot, and append `GATE_1_APPROVED` with the artifact 01 path and hash. Read the Control File back and verify every field before reporting success.

Stop after Gate 1. Do not start Tab 02.
