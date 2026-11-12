# Process 06 — Design Systems Kit

Process 06 follows a frozen UX Spec. It defines the reusable visual language and the component contract: values, roles, tokens, components and the rules for using them.

**It defines what the product looks like as a system. It does not place anything on a screen.**

## Three independent Antigravity tabs

1. **Tab 01 — Foundations and Tokens:** `prompts/06-DESIGN-SYSTEMS/01-FOUNDATIONS.md`
2. **Tab 02 — Tokens, Components, Accessibility:** `prompts/06-DESIGN-SYSTEMS/02-COMPONENT-LIBRARY.md`
3. **Tab 03 — Independent Review and authorized freeze:** `prompts/06-DESIGN-SYSTEMS/03-INDEPENDENT-REVIEW.md`

Active Skill: `.agents/skills/design-system/SKILL.md`

Do not confuse this Process 06 review prompt with `prompts/05-UX-DESIGN/03-INDEPENDENT-REVIEW.md` or any other process's similarly named prompt.

## Input contract

Require:

- `product/ux-design/00_UX_CONTROL.md`
- `product/ux-design/UX_SPEC.md`
- `product/app-flow/APP_FLOW.md` — verified transitively through the hash Process 05 recorded

Process 05 Gate 3 must be `APPROVED`, lifecycle `FROZEN`, no open Change Request, and the actual UX Spec SHA-256 must equal `gate_3.frozen_artifact.sha256`. Process 06 never re-opens Process 04 and never reads a Process 03 file.

## Outputs

Canonical state: `product/design-system/00_DS_CONTROL.md` (schema v1)

Working artifacts:

- `01_DESIGN_FOUNDATIONS.md`
- `02_TOKEN_CONTRACT.md`
- `03_COMPONENT_INVENTORY.md`
- `04_COMPONENT_ACCESSIBILITY.md`
- `05_DS_REVIEW.md` — append-only rounds
- `06_DS_DRAFT.md` — complete reviewed candidate
- `07_DECISION_LOG.md` — append-only decisions

Frozen output: `product/design-system/DESIGN_SYSTEM.md`
Frozen-output schema: `templates/06-DESIGN-SYSTEMS/08-DESIGN-SYSTEM.md`

Template `NN` initializes working artifact `NN` for `01`–`07`. Template `08` is the frozen-output schema only.

## Human gates

| Tab | Gate | Exact command |
|---|---|---|
| 01 | Foundations approved | `APPROVE DESIGN FOUNDATIONS` |
| 02 | Component library approved | `APPROVE COMPONENT LIBRARY` |
| 03 | Review completed; freeze only after all preconditions pass | `FREEZE DESIGN SYSTEM` |

Additional exact commands:

- `APPROVE DESIGN DECISION [DECISION-ID]`
- `REJECT DESIGN DECISION [DECISION-ID]`
- `DEFER DESIGN DECISION [DECISION-ID]`
- `ACCEPT RESIDUAL RISK [FINDING-ID]` (MAJOR/MINOR only, with rationale)
- `REJECT DESIGN FOUNDATIONS` / `REJECT COMPONENT LIBRARY`
- `REQUEST DESIGN SYSTEM CHANGE [description]`
- `ABANDON DESIGN SYSTEM`
- `RECOVER DECISION LOG [DECISION-ID]`
- `RECOVER REVIEW ROUND [N]`

Tab 03 never freezes automatically after `GO`. Tab 03 is read-only on the Decision Log. No automatic handoff.

## Platform

Recorded in the Control File, immutable per workspace: `android` / `jetpack-compose` / `material-3`, decided in `process-charters/06-DESIGN-SYSTEMS.md` section 8a.

Changing it reopens every gate and requires a new design system, because target size, type scale, elevation semantics and motion budget all derive from it. A workspace with a different platform is not wrong — it is a different product with its own initiative.

Material 3 is a vocabulary, not a decision. Every component still needs a citing screen.

## The three boundaries this process is judged on

1. **Component admission.** A component exists only if a frozen Process 05 screen requires it, and it must cite the SCREEN IDs. `components_defined` must equal `components_cited` at Gate 2. Without this rule, every design system becomes a library of everything the author could imagine, and Process 07 composes from what is available rather than from what is needed.
2. **Token layering.** Reference → system → component (`ref` / `sys` / `comp`), each referencing only the tier above. The three-tier model is Material 3's, adopted rather than invented. A component token pointing at a reference token opts out of theming and out of the contrast guarantee. A system token with no role statement is a naming defect.
3. **Measured contrast.** Every text/background and icon/background pair the inventory can produce, computed from resolved values, with the method stated. A declared ratio is not evidence. `contrast_pairs_measured` must equal `contrast_pairs_total` at Gate 2.

## Decision Log integrity

Identity header must read `Process: 06` and an Initiative ID equal to the Control File and the verified Process 05 initiative. Immutable proposals, append-only status events, one-to-one pairing with `DECISION_LOG_UPDATED`. Current status reconstructed by committed `state_seq`. Gate 2 binds the whole log; any later byte change reopens Gates 2–3.

## Review-history integrity

Before Round 1, initialize `05_DS_REVIEW.md` from its exact template and bind the hash with `REVIEW_HISTORY_INITIALIZED`. Each round is append-only and bound by `REVIEW_ROUND_RECORDED`. Interrupted appends recover only through `RECOVER REVIEW ROUND [N]`. Never append the same round twice.

## Freeze integrity

The reviewed draft is the complete canonical candidate. Freeze copies it byte-for-byte and changes only the status line. Before freeze: both gates valid, at least one review round, matching review and draft hashes, zero open findings, and all three coverage equalities satisfied. The final SHA-256 lives in the Control File, never inside `DESIGN_SYSTEM.md`.

Before re-freeze, archive the prior output as `DESIGN_SYSTEM.v<N>.md`. If the canonical write succeeds but the Control write fails, report `INCOMPLETE — NOT FROZEN`.

## Boundaries

Do not create screen layout, placement, regions, composition, wireframes, final copy, code, Compose theme files, assets or images. Do not add a screen, a state or a capability. A needed screen returns to Process 04; a needed requirement returns to Process 05.

## Upstream method sources

**Copied verbatim** into `upstream/anthropics/knowledge-work-plugins/design/skills/` (Apache-2.0, blob SHAs in `SOURCE.md`):

| Local file | Used for |
|---|---|
| `design-system/SKILL.md` | Foundations and token method |
| `accessibility-review/SKILL.md` | Contrast and focus measurement |
| `design-critique/SKILL.md` | Review structure for Tab 03 |

**Cited, not copied:** `pbakaus/impeccable` `extract.md`, `document.md`, `craft-floor.md`, `android.md`. Its playbooks call a runtime binary, so vendoring them would bake a broken dependency into the repository.

Two deviations bind: upstream audits WCAG 2.1 while this process records 2.2, and upstream assumes connectors that do not exist here. Recorded in `SOURCE.md`, not patched in the copied bytes.

## Verification status

Nothing in this kit has been executed against a real workspace. Do not label Process 06 production-ready until live tests have evidence.
