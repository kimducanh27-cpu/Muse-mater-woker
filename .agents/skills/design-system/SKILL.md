---
name: design-system
description: Run Process 06 Design Systems from a frozen UX Spec. Define colour roles, type scale, spacing, elevation, motion and a token contract, then a component library in which every component cites the screens that require it. Includes measured contrast, independent review and an explicitly authorized freeze.
---

# Design Systems — Process 06

## Mission and process boundary

Turn a frozen set of screen requirements into a reusable visual language and component contract, so that Process 07 composes screens instead of inventing styles.

- Process 04 defines the functional flow and the state space.
- Process 05 defines what each screen must communicate and let the user do.
- Process 06 defines **what the product looks like as a system**: values, roles, tokens, components, and the rules for using them.
- Process 07 composes screens from that system. Process 08 measures conformance.

This is the **first process in the sequence allowed to produce concrete visual values** — hex, point sizes, spacing units, durations. Everything before it is deliberately value-free. Do not carry that caution forward into vagueness: a design system that refuses to commit to a value has not done its job.

Process 06 does not place components on screens, define screen layouts, write final copy, produce code, or add a screen, a state or a capability.

## Platform

The target platform is recorded in the Control File and is immutable for the workspace: `android` / `jetpack-compose` / `material-3`.

Platform is a vocabulary, not a decision. Material 3 supplies roles and scales; this process still decides which of them the product uses and must justify each component against a citing screen. A component that exists only because Material 3 has one is speculative and is rejected at Gate 2.

## Required input and fail-closed eligibility

Canonical Process 05 files:
- Control: `product/ux-design/00_UX_CONTROL.md`
- Frozen output: `product/ux-design/UX_SPEC.md`

Verify, in order:
1. Process 05 `initiative_id` present.
2. `gate_3.status = APPROVED`.
3. `lifecycle_status = FROZEN`.
4. `gate_3.frozen_artifact.path` equals `product/ux-design/UX_SPEC.md`.
5. Actual SHA-256 of `UX_SPEC.md` equals `gate_3.frozen_artifact.sha256`.
6. No open Change Request in the Process 05 workspace.
7. Process 05 `source_process_04.frozen_artifact_sha256` is non-null and equals the actual SHA-256 of `product/app-flow/APP_FLOW.md`.

Check 7 is transitive on purpose. Process 06 reads the App Flow for screen and state IDs, but it does not re-open Process 04 and never reads a Process 03 file.

If any check fails, set `source_process_05.status = NOT_VERIFIED`, stop, and report the exact missing evidence.

At every tab entry and before each approval or freeze, re-read both sources and recompute both hashes. If either changes, mark sources `REOPENED`, reopen all gates, set lifecycle `REVIEW_REQUIRED`, append `INVALIDATED`, and stop.

## Canonical state, templates and artifacts

Canonical Control File: `product/design-system/00_DS_CONTROL.md`
Control template: `templates/06-DESIGN-SYSTEMS/00-DS-CONTROL.md`

Working artifacts:
- `01_DESIGN_FOUNDATIONS.md` — colour roles, type scale, spacing scale, radius, elevation, motion, grid
- `02_TOKEN_CONTRACT.md` — three-layer tokens, naming, allowed and forbidden usage
- `03_COMPONENT_INVENTORY.md` — every component with anatomy, variants, sizes, states, slots and citing screens
- `04_COMPONENT_ACCESSIBILITY.md` — measured contrast pairs, focus, target size, announcement intent
- `05_DS_REVIEW.md` — append-only review history
- `06_DS_DRAFT.md` — complete reviewed candidate
- `07_DECISION_LOG.md` — append-only decisions

Frozen output: `product/design-system/DESIGN_SYSTEM.md`
Frozen-output schema: `templates/06-DESIGN-SYSTEMS/08-DESIGN-SYSTEM.md`

Template `NN` initializes working artifact `NN` for `01`–`07`. Template `08` is the frozen-output schema only.

Use each named template and preserve its headings, tables and columns. Where a section does not apply, write NOT APPLICABLE with a specific rationale. Never leave a placeholder blank.

## The token layering rule

Three layers, and each layer may only reference the one above it. **The three-tier model is Material 3's, not a local invention**: Material names the tiers reference (`ref`), system (`sys`) and component (`comp`). Adopt those tier labels so this contract maps cleanly onto the platform. The token *names* inside each tier are product decisions — a product system token sits at Material's `sys` tier and may either extend `md.sys.*` or replace it.

1. **Reference (`ref`)** — a raw value with no meaning: `ref.palette.blue.600`, `ref.size.4`. Never referenced by a component.
2. **System (`sys`)** — a role: `sys.color.action.primary`, `sys.space.inline.md`, `sys.elevation.raised`. This is the tier that makes a second theme possible and that accessibility is measured against.
3. **Component (`comp`)** — a component-scoped alias: `comp.button.primary.container`. May reference system tokens only.

A component that references a reference token directly is a Gate 2 defect, because it silently opts out of theming and of the contrast measurement that system tokens carry. A system token with no role statement is a naming defect: "blue" is not a role, "action.primary" is.

## Component admission rule

A component may exist only if at least one frozen Process 05 screen requires it, and its inventory entry must cite the SCREEN IDs.

This is the rule that keeps a design system honest. Without it, every process produces a component library of everything the author could imagine, and Process 07 then composes screens from whatever is available rather than from what is needed. With it, the system has a proof of demand for every line.

A component cited only by a screen that does not exist in the frozen inventory is `NOT_VERIFIED`, not a near miss.

## Hashes and timestamps

SHA-256 over exact on-disk bytes. On Windows:

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath ".\product\design-system\01_DESIGN_FOUNDATIONS.md").Hash.ToLowerInvariant()
```

Real local timestamp in Asia/Ho_Chi_Minh:

```powershell
$zone = [TimeZoneInfo]::FindSystemTimeZoneById('SE Asia Standard Time')
[TimeZoneInfo]::ConvertTime([DateTimeOffset]::UtcNow, $zone).ToString('yyyy-MM-dd HH:mm:ss zzz')
```

Never invent a hash or a timestamp. If hashing or file read is unavailable, record `NOT_VERIFIED` and block the gate.

## Control File and state integrity

Initialize the Control File from the template only after both sources are `VERIFIED`. Every update is single-writer:

1. Read the Control File and record `state_seq`.
2. Recompute prerequisite hashes and verify current state.
3. Compute the next committed sequence, apply exactly one state change, append one event whose `state_seq` equals that value.
4. Persist `state_seq` and a real local timestamp.
5. Read back and verify state, event and hashes.
6. Report success only after read-back succeeds.

`state_seq` is a stale-read detector, not a lock. Only one tab may write at a time.

## Decision log

`07_DECISION_LOG.md` is append-only and belongs to one initiative. Its immutable identity header must contain `Process: 06` and an Initiative ID equal to the Control File and the verified Process 05 source.

Each proposal is an immutable block with a unique `Proposal Event ID: DLE-<NNNN>` and `Status at proposal: PROPOSED`. Each outcome is a separate appended status event with its own ID, `Event kind: DECISION_STATUS_CHANGED`, before/after status, exact command, rationale, timestamp, affected gate, affected artifact IDs and `Supersedes status event ID`.

Every append pairs one-to-one with a Control File `DECISION_LOG_UPDATED` event. Current status is reconstructed from paired events ordered by committed `state_seq`. A broken chain makes that DEC ID `NOT_VERIFIED`.

Gate classification from actual scope:
- `GATE_1` — foundations, colour roles, type scale, spacing, elevation, motion.
- `GATE_2` — token contract, component inventory, component accessibility.
- `GATE_3` — review or draft changes that do not alter 01–04.
- If more than one layer is affected, choose the earliest. Any change to a frozen screen's requirements returns to Process 05.

Tab 03 is read-only on the Decision Log.

## Review history

Before Round 1, initialize `05_DS_REVIEW.md` from its template, read back, hash, and bind with `REVIEW_HISTORY_INITIALIZED`.

Before appending round N: verify the current review hash equals `review.latest_review_sha256`, that `review.round = N-1`, and record the pre-append Control `state_seq`, pre-append Control hash and previous review hash inside the round. Append exactly one round, read back, hash, then register with `REVIEW_ROUND_RECORDED` in one Control update.

If the append succeeds but the Control update fails, do not append again. Recovery requires `RECOVER REVIEW ROUND [N]` and every precondition in the template.

## Method references

Design method lives in `upstream/anthropics/knowledge-work-plugins/design/skills/`, copied verbatim from an Apache-2.0 source:

| File | Read it for |
|---|---|
| `design-system/SKILL.md` | Component inventory completeness, component documentation and consistency audit (Tab 02, Tab 03). It is a **maintenance** method — audit, document, extend an existing system. It does not say how to choose a colour role or a scale ratio; that remains local work. |
| `accessibility-review/SKILL.md` | Contrast and focus measurement |
| `design-critique/SKILL.md` | Review structure for Tab 03 |

These are **method, not authority**, and they sit outside `.agents/skills/` so they cannot be loaded in place of this contract.

Deviations recorded in `upstream/anthropics/knowledge-work-plugins/SOURCE.md` bind here: upstream audits **WCAG 2.1** while this process records **2.2**, so contrast and criterion coverage are audited against 2.2; and upstream assumes connected tools, so a connector-dependent step is `NOT APPLICABLE` and the skip is recorded.

When method and contract disagree, the contract wins.

## Three-tab workflow

### Tab 01 — Foundations and tokens

Entry: read this Skill, verify both sources, initialize or verify the Control File and the Decision Log identity, and record `platform` at initialization.

Work:
- Define colour as **roles**, not swatches: what is "primary", "surface", "danger", "disabled" for. A palette without roles is a mood board.
- Define a type scale with a stated ratio and the role of each step.
- Define a spacing scale, radius scale, elevation levels and motion durations/easing.
- Every value must state the role it serves and where a screen would use it. A value with no role is decoration.
- On Android, elevation is tonal; state layers and dynamic colour are platform behaviours that must be decided, not inherited silently.

Artifact: `01_DESIGN_FOUNDATIONS.md` from template `01`.

Gate 1 requires: every foundation value has a named role; no value lacks a role statement; the Decision Log hash matches `decision_log.latest_sha256`; both sources `VERIFIED`; the user sending exactly `APPROVE DESIGN FOUNDATIONS`; and one Control update setting `gate_1.approved_state_seq`, `gate_1.decision_log_sha256`, the coverage snapshot and appending `GATE_1_APPROVED`.

Stop after Gate 1.

### Tab 02 — Tokens, components, accessibility

Entry: re-verify both sources, Gate 1 with a matching event and sequence anchor, every Gate 1 hash, and the Decision Log identity and hash.

Work:
- Build the three-layer token contract. Every system token names a role and every component token references a system token only.
- Build the component inventory. For each component: purpose, anatomy, variants, sizes, interaction states, slots, content limits, and the **citing SCREEN IDs**.
- A component with no citing screen is not admitted. A screen with no citing component means either a missing component or an inexpressible requirement — decide which, and record it.
- Measure contrast from actual token values for every text/background and icon/background pair the inventory can produce. Declared contrast is not evidence.
- Record target size, focus visibility and announcement intent per component. Requirements here, ARIA or semantics attributes in Process 07.

Before Gate 2, run and show these set comparisons:
- Every component's citing SCREEN IDs exist in the frozen Process 05 inventory.
- Every SCREEN ID in the frozen inventory cites at least one component.
- Every component token references a system token; every system token has a role statement.
- Every contrast pair has a computed ratio and a pass/fail against the recorded conformance level.
- No screen layout, placement or composition appears anywhere in 02–04.
- No final copy, no code, no image.

Gate 2 binds 02–04 and the whole Decision Log. The user must send exactly `APPROVE COMPONENT LIBRARY`. One Control update sets `gate_2.approved_state_seq`, `gate_2.decision_log_sha256`, the coverage snapshot and appends `GATE_2_APPROVED`.

Stop after Gate 2.

### Tab 03 — Independent review and authorized freeze

Entry: re-verify both sources, Gates 1 and 2 with matching events and sequence anchors, every bound hash, and the Decision Log hash equal to both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`. No `DECISION_LOG_UPDATED` may follow Gate 2.

Reviewer permissions: read-only on 01–04 and 07; may append to 05, create and update 06, and update the Control File only for review state, user-authorized risk acceptance, invalidation and explicit freeze.

Review:
- Build `06_DS_DRAFT.md` from template `06`, containing the full detail of 01–04 and the approved decisions. Not a summary.
- The draft begins with the exact line `> Status: REVIEWED CANDIDATE — NOT FROZEN`.
- Audit every artifact in full.
- Append one review round with findings, severity, exact artifact and IDs, evidence, scenario, impact, minimal correction and confidence.
- Severity: BLOCKER = a required screen cannot be expressed by the system; CRITICAL = a contrast or target-size failure on a required interaction; MAJOR = material gap or contradiction; MINOR = bounded ambiguity.
- Verdict GO / CONDITIONAL GO / HOLD. `READY_FOR_FREEZE` only when every finding is RESOLVED or ACCEPTED_BY_USER.

Remediation: BLOCKER and CRITICAL must be fixed. MAJOR and MINOR are fixed or accepted one at a time with `ACCEPT RESIDUAL RISK [FINDING-ID]` plus rationale.

Freeze waits for the separate exact command `FREEZE DESIGN SYSTEM`.

## Freeze protocol

Before writing, verify: both sources `VERIFIED`; Gates 1 and 2 `APPROVED` with all bound hashes; `review.round >= 1` and the review hash matching; the latest round's artifact hashes matching current files; draft hash equal to both `review.reviewed_draft_sha256` and the latest round's draft hash; review status `READY_FOR_FREEZE` with zero open findings; `components_cited = components_defined`, `screens_citing_a_component = screens_in_source`, `contrast_pairs_measured = contrast_pairs_total`; candidate version equal to `gate_3.frozen_version + 1`.

Create `DESIGN_SYSTEM.md` by copying the exact bytes of the reviewed draft and replacing only the status line. Do not insert a hash or timestamp.

Before re-freeze: verify the existing canonical hash, archive it byte-for-byte as `DESIGN_SYSTEM.v<N>.md`, verify the archive, then replace.

Then update Gate 3 `APPROVED`, lifecycle `FROZEN`, set `gate_3.approved_state_seq` and append `GATE_3_FROZEN` in one update. Read back and recompute. If the canonical file is written but the Control update fails, report **INCOMPLETE — NOT FROZEN**.

## Abandonment

On exactly `ABANDON DESIGN SYSTEM`, record command and rationale, set lifecycle `ABANDONED`, stop. ABANDONED is terminal.

## Invalidation matrix

| Changed input or artifact | State action |
|---|---|
| Process 05 Control File, `UX_SPEC.md`, or the App Flow hash bound through it | both sources `REOPENED`; Gates 1–3 reopened; lifecycle `REVIEW_REQUIRED` |
| `platform` field | Gates 1–3 reopened; new design system required under a new initiative |
| `01_DESIGN_FOUNDATIONS.md` | Gates 1–3 reopened |
| `02`–`04` | Gates 2–3 reopened; Gate 1 remains valid only if no foundation value changed |
| `05_DS_REVIEW.md` or `06_DS_DRAFT.md` | Gate 3 reopened; new review round required |
| `07_DECISION_LOG.md` before Gate 2 | reopen the earliest independently verified affected gate and all downstream gates |
| Any `07` byte change after Gate 2 | always reopen Gates 2–3; also Gate 1 when classification is `GATE_1` |
| `DESIGN_SYSTEM.md` after freeze | Gate 3 reopened; lifecycle `REVIEW_REQUIRED`; downstream use prohibited |

Every invalidation appends timestamp, `state_seq`, changed paths, previous and new hashes, affected gates and reason.

## Required quality checks

- Every foundation value has a role statement and a stated use.
- Every token is layered correctly; no component reaches past the system layer.
- Every component cites at least one frozen SCREEN ID.
- Every frozen screen cites at least one component, or has a recorded decision explaining why not.
- Every contrast pair has a computed ratio, not an assertion.
- Every component states target size, focus behaviour and announcement intent.
- Zero screen layout, placement or composition.
- Zero final copy, zero code, zero image.
- No component exists because the platform has one.
- All set comparisons are shown, not asserted.

If any check cannot be verified, report `NOT_VERIFIED` rather than `PASS`.
