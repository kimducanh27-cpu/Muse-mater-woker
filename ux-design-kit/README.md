# Process 05 — UX Design Kit

Process 05 follows a frozen App Flow. It converts functional screens into an experience contract: what the user must understand and be able to do on each screen, in every state the flow defines.

**It defines experience. It does not define visual design, components or implementation.**

## Three independent Antigravity tabs

1. **Tab 01 — Screen UX Model:** `prompts/05-UX-DESIGN/01-SCREEN-UX-MODEL.md`
2. **Tab 02 — Patterns, States, Content, Accessibility:** `prompts/05-UX-DESIGN/02-UX-SPEC.md`
3. **Tab 03 — Independent Review and authorized freeze:** `prompts/05-UX-DESIGN/03-INDEPENDENT-REVIEW.md`

Active Skill: `.agents/skills/ux-design/SKILL.md`

All paths are repository-root-relative. Do not confuse this Process 05 review prompt with `prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md` or any other process's similarly named prompt.

## Input contract

Require:

- `product/app-flow/00_APP_FLOW_CONTROL.md`
- `product/app-flow/APP_FLOW.md`
- `product/definition/PRODUCT_DEFINITION.md` — verified transitively

Process 04 Gate 3 must be `APPROVED`, lifecycle `FROZEN`, the reconstructed blocking Change Request set empty, and the actual App Flow SHA-256 must equal `gate_3.frozen_artifact.sha256`. The Product Definition is verified through Process 04's recorded `source_process_03.frozen_artifact_sha256`; Process 05 never reads or modifies a Process 03 Control File.

A missing, stale, unreadable or mismatched source blocks entry.

## Outputs

Canonical state: `product/ux-design/00_UX_CONTROL.md` (schema v1)

Working artifacts:

- `01_SCREEN_UX_MODEL.md`
- `02_INTERACTION_PATTERNS.md`
- `03_STATE_EXPERIENCE.md`
- `04_CONTENT_AND_COPY_INTENT.md`
- `05_ACCESSIBILITY_REQUIREMENTS.md`
- `06_UX_REVIEW.md` — append-only rounds
- `07_UX_SPEC_DRAFT.md` — complete reviewed candidate
- `08_DECISION_LOG.md` — append-only decisions

Frozen output: `product/ux-design/UX_SPEC.md`
Frozen-output schema: `templates/05-UX-DESIGN/09-UX-SPEC.md`

Template `NN` initializes working artifact `NN` for `01`–`08`. Template `09` is the frozen-output schema only. This numbering is deliberately different from Process 04, where the frozen schema occupies an earlier template slot — do not copy Process 04's numbering.

## Human gates

| Tab | Gate | Exact command |
|---|---|---|
| 01 | Screen UX model approved | `APPROVE SCREEN UX MODEL` |
| 02 | UX spec approved | `APPROVE UX SPEC` |
| 03 | Review completed; freeze only after all preconditions pass | `FREEZE UX SPEC` |

Additional exact commands:

- `APPROVE UX DECISION [DECISION-ID]`
- `REJECT UX DECISION [DECISION-ID]`
- `DEFER UX DECISION [DECISION-ID]`
- `ACCEPT RESIDUAL RISK [FINDING-ID]` (MAJOR/MINOR only, with rationale)
- `REJECT SCREEN UX MODEL` / `REJECT UX SPEC`
- `REQUEST UX CHANGE [description]`
- `ABANDON UX SPEC`
- `RECOVER DECISION LOG [DECISION-ID]`
- `RECOVER REVIEW ROUND [N]`

Tab 03 must not freeze automatically after a `GO` verdict. The user must issue the separate exact freeze command. Tab 03 is read-only on the Decision Log; decision outcomes return to their owning tab. No automatic handoff; each tab runs in a fresh conversation and reads persisted workspace artifacts.

## The boundary that this process is judged on

Process 05 is the easiest process in the sequence to contaminate. Three lexical audits are mandatory at Gate 2 and again at review:

1. **No named components.** button, card, modal, dialog, toast, chip, tab, drawer, tooltip, badge, banner, accordion — plus the Android affordances an agent absorbs without noticing: app bar, bottom sheet, navigation rail, FAB, snackbar, system back, window size class. Naming one pre-empts Process 06 and makes the design system a rubber stamp.
2. **No visual values.** No hex, font family, font size, spacing, radius, shadow. The first process allowed to produce concrete visual values is Process 06.
3. **No final copy.** Intent only. Final strings need layout constraints that do not exist until Process 07.

## Structural blocks

Artifact 01 may contain one fenced `text` block per screen, at most 100 characters wide, showing spatial grouping only. The block is illustrative; the ordered hierarchy list is the contract. A block that disagrees with the list is a Gate 1 defect. No images, no screenshots, no external file references.

## Decision Log integrity

The identity header must read `Process: 05` and an Initiative ID equal to the Control File and the verified Process 04 initiative. Each proposal has an immutable `PROPOSED` block and a unique DLE ID; each user outcome is a separate append-only status event with its own unique DLE ID. Every DLE ID pairs one-to-one with a `DECISION_LOG_UPDATED` Control event. Current status is reconstructed from the valid chain ordered by committed `state_seq`. Legacy inline status fields are not proof of approval.

Gate 2 binds the whole Decision Log file. Any byte change after Gate 2 reopens Gates 2–3 regardless of apparent scope.

## Review-history integrity

Before Round 1, initialize `06_UX_REVIEW.md` from its exact template, compute and read back its SHA-256, and bind it with `REVIEW_HISTORY_INITIALIZED`. Each appended round is bound by `REVIEW_ROUND_RECORDED`. An interrupted append may be recovered only with `RECOVER REVIEW ROUND [N]` and the exact preimage checks in the Skill. Never append the same round twice.

## Freeze integrity

The reviewed draft is the complete canonical candidate. Freeze copies it byte-for-byte and changes only the status line. It does not rebuild or re-summarise.

Before freeze: Gate 1 and Gate 2 hashes valid, at least one review round, matching review and draft hashes, zero open findings, user-originated acceptance records for accepted risks, and every coverage counter equal to its source count. The final SHA-256 lives in the Control File, never inside `UX_SPEC.md`.

Before re-freeze, archive the prior canonical output as `UX_SPEC.v<N>.md`. If the canonical write succeeds but the Control write or read-back fails, report `INCOMPLETE — NOT FROZEN`. An orphan `UX_SPEC.md` is not eligible downstream.

## Boundaries

Do not create colour, typography, spacing, elevation, iconography, components, design tokens, wireframes, images, prototypes, final copy, APIs, data models or code. Do not add a screen, a state or a capability. A needed screen or state returns to Process 04; a needed capability returns to Process 03.

The product is Android native (recorded in `process-charters/06-DESIGN-SYSTEMS.md` section 8a), and this process is deliberately platform-neutral anyway. That is not an oversight: a requirement stated in platform terms here would decide the design system before anyone audited the decision.

## Upstream method sources

This kit supplies gates, hashes and handoff rules. It does not supply design method, and it does not pretend to.

**Copied verbatim** into `upstream/anthropics/knowledge-work-plugins/design/skills/` (Apache-2.0, blob SHAs in `SOURCE.md`):

| Local file | Used for |
|---|---|
| `accessibility-review/SKILL.md` | Accessibility criterion coverage for artifact 05 |
| `ux-copy/SKILL.md` | Copy-intent method for artifact 04 |
| `design-critique/SKILL.md` | Review structure for Tab 03 |

**Cited, not copied:** `pbakaus/impeccable` `skill/reference/shape.md` (task discovery) and `critique.md` (heuristic scoring). It is a design agent that writes production code and ships a runtime binary, so vendoring its playbooks would bake a broken dependency into the repository. See `UPSTREAMS.md` section 4.

Two deviations bind when using the copied files: upstream audits WCAG 2.1 while this process records 2.2, and upstream assumes connectors that do not exist here. Both are recorded in `SOURCE.md` and neither is patched in the copied bytes.

## Verification status

The checklist distinguishes repository/paper checks from live runtime verification. Nothing in this kit has been executed against a real workspace. Do not label Process 05 production-ready until live tests have evidence.
