---
name: ux-design
description: Run Process 05 UX Design from a frozen App Flow. Convert functional screens into an experience contract covering primary action, information hierarchy, interaction patterns, every defined state, content intent and accessibility requirements. Includes independent review and an explicitly authorized freeze.
---

# UX Design — Process 05

## Mission and process boundary

Convert each functional screen in the frozen App Flow into a contract that says what a person must understand and be able to do on that screen, in every state the flow defines.

- Process 03 defines WHAT and WHY.
- Process 04 defines functional tasks, navigation, screens, transitions and the state space.
- Process 05 defines the experience of those screens: hierarchy, primary action, interaction pattern, recovery affordance, content intent, accessibility requirement.
- Process 06 defines the visual language and component contract. Process 07 composes screens. Process 08 validates the chain.

Process 05 does not create colour, typography, spacing, elevation, iconography, components, design tokens, wireframe images, final copy, code or prototypes. It does not add screens, states or capabilities. A screen it needs but the flow lacks is a Change Request to Process 04; a state it needs but the matrix lacks is a Change Request to Process 04; a capability it needs but the definition lacks is a Change Request to Process 03.

## Required input and fail-closed eligibility

Canonical Process 04 files:
- Control: `product/app-flow/00_APP_FLOW_CONTROL.md`
- Frozen output: `product/app-flow/APP_FLOW.md`

Verify, in this order:
1. Process 04 `initiative_id` is present and readable.
2. Process 04 `gate_3.status = APPROVED`.
3. Process 04 `lifecycle_status = FROZEN`.
4. `gate_3.frozen_artifact.path` equals `product/app-flow/APP_FLOW.md`.
5. Actual SHA-256 of `APP_FLOW.md` equals Process 04 `gate_3.frozen_artifact.sha256`.
6. The reconstructed blocking Change Request set is empty.
7. Process 04 `source_process_03.frozen_artifact_sha256` is non-null and equals the actual SHA-256 of `product/definition/PRODUCT_DEFINITION.md`.

Check 7 is the only Process 03 verification this process performs. It is transitive on purpose: Process 05 must not read, repair or extend a Process 03 Control File, and it must not invent a field there. If Process 04 recorded no Process 03 hash, the chain is broken.

If any check fails or is unreadable, set `source_process_04.status = NOT_VERIFIED`, stop, and report the exact missing evidence. Never infer approval from a filename, a status line, a prior agent's claim or a user saying the file has not changed.

At every tab entry and immediately before each approval or freeze, re-read the source Control File and recompute both hashes. If either source changes, mark the handoff `REOPENED`, reopen all gates, set lifecycle `REVIEW_REQUIRED`, append `INVALIDATED`, and stop. Do not continue against a superseded flow.

## Canonical state, templates and artifacts

Canonical Control File: `product/ux-design/00_UX_CONTROL.md`
Control template: `templates/05-UX-DESIGN/00-UX-CONTROL.md`

Working artifacts:
- `01_SCREEN_UX_MODEL.md` — one entry per SCREEN ID
- `02_INTERACTION_PATTERNS.md` — named patterns, each with when to use and when not to
- `03_STATE_EXPERIENCE.md` — one row per screen × state
- `04_CONTENT_AND_COPY_INTENT.md` — required content and message intent, never final wording
- `05_ACCESSIBILITY_REQUIREMENTS.md` — per-screen keyboard, focus, announcement and target requirements
- `06_UX_REVIEW.md` — append-only review history
- `07_UX_SPEC_DRAFT.md` — complete reviewed candidate, not a summary
- `08_DECISION_LOG.md` — append-only user-approved decisions

Frozen output: `product/ux-design/UX_SPEC.md`
Frozen-output schema: `templates/05-UX-DESIGN/09-UX-SPEC.md`

Template `NN` initializes working artifact `NN` for `01`–`08`. Template `09` is the frozen-output schema and has no working counterpart. This differs from Process 04, where the frozen schema occupies an earlier slot; do not copy Process 04's numbering.

Use each named template and preserve its headings, tables and columns. Where a section does not apply, write NOT APPLICABLE with a specific rationale. Never leave a placeholder blank.

## The structural block rule

Artifact 01 may contain one fenced `text` block per screen, at most 100 characters wide, drawn with box characters or ASCII, showing spatial grouping only.

Rules that make it safe to hash and review:
- The block is **not** authoritative. The ordered hierarchy list above it is the contract. If the block and the list disagree, the list wins and the block is a defect.
- The block may not contain colour, typeface, font size, spacing values, shadow, radius or any style token.
- The block may not be an image, a screenshot or an external file reference.
- The block may not introduce a screen, region or element absent from the list.

A block that violates these rules is a Gate 1 defect, not a stylistic preference.

## Hashes and timestamps

Use SHA-256 over exact on-disk bytes. On Windows:

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath ".\product\ux-design\01_SCREEN_UX_MODEL.md").Hash.ToLowerInvariant()
```

Use a real local timestamp in Asia/Ho_Chi_Minh:

```powershell
$zone = [TimeZoneInfo]::FindSystemTimeZoneById('SE Asia Standard Time')
[TimeZoneInfo]::ConvertTime([DateTimeOffset]::UtcNow, $zone).ToString('yyyy-MM-dd HH:mm:ss zzz')
```

Never invent a hash or a timestamp. If hashing, timestamping or file read is unavailable, record `NOT_VERIFIED` and block the affected gate.

## Control File and state integrity

The Control File is canonical state. Initialize it from the template only if it does not exist, and only after both source statuses are `VERIFIED`. Never overwrite another initiative's Control File.

Every update is single-writer:
1. Read the Control File and record `state_seq`.
2. Recompute prerequisite hashes and verify current state.
3. Compute the next committed sequence (`current + 1`), apply exactly one state change, and append one event whose `state_seq` equals that new value.
4. Persist `state_seq` and a real local timestamp.
5. Read the Control File back and verify state, event and hashes. **Compare the event's key set to `templates/CONTROL-FIELDS-v1.yaml` mechanically, key by key.** Do not compare it to what you remember writing: that comparison always passes, including when it is wrong. Report any missing key and any extra key by name.
6. Report success only after read-back succeeds.

`state_seq` is a stale-read detector, not a lock. Only one tab may write at a time. If concurrent writes may have occurred, stop all tabs and reconcile against the last trusted copy; do not certify the history from `state_seq` alone.

## Canonical event schema

Use only the event types in `templates/05-UX-DESIGN/00-UX-CONTROL.md`. Gate sequence anchors work as in Process 04: `gate_1.approved_state_seq`, `gate_2.approved_state_seq` and `gate_3.approved_state_seq` must equal the sequence of their own latest approval or freeze event. A gate may never be treated as approved from its `status` field alone, and never from `approved_command` or prose.

There is no migration event. A Control File that claims a predecessor schema, or that carries a `SCHEMA_MIGRATED` event, is `NOT_VERIFIED`.

## Decision log

`08_DECISION_LOG.md` is append-only and belongs to one initiative. Its immutable identity header must contain `Process: 05` and an Initiative ID equal to the Control File and the verified Process 04 source.

Each proposal is an immutable block with a unique `Proposal Event ID: DLE-<NNNN>` and `Status at proposal: PROPOSED`. Each user outcome is a separate appended status event with its own unique ID, `Event kind: DECISION_STATUS_CHANGED`, status before and after, exact command, rationale, timestamp, affected gate and affected artifact IDs, plus `Supersedes status event ID`. A status event may not change the proposal's scope; a scope change needs a new DEC ID.

Every proposal or status append pairs one-to-one with a Control File `DECISION_LOG_UPDATED` event carrying the same DEC ID, DLE ID, kind, before/after status, affected gate, path and resulting hash. Current status is reconstructed from the paired events ordered by committed `state_seq`. A missing, duplicate, malformed, out-of-order or mismatched pair makes that DEC ID `NOT_VERIFIED`, and it may not be used as approved policy.

Identity absent, unreadable or mismatched is `NOT_VERIFIED`. Never adopt a log by hashing its current bytes, and never rewrite its identity header.

Gate classification, derived from the decision's actual scope and affected artifacts:
- `GATE_1` — changes to `01_SCREEN_UX_MODEL.md`, screen goals, primary actions, information hierarchy or capability-to-screen coverage.
- `GATE_2` — changes limited to `02`–`05`: patterns, state experience, content intent, accessibility requirements.
- `GATE_3` — changes limited to `06` or `07` that do not alter `01`–`05`.
- If more than one layer is affected, choose the earliest affected gate. Any change to Process 04 scope, screens or state space returns to Process 04; Process 05 cannot relabel it as a local decision.

Tab 03 is read-only on the Decision Log. It never appends a proposal or a status event.

## Review history

Before Round 1, initialize `06_UX_REVIEW.md` from `templates/05-UX-DESIGN/06-UX-REVIEW.md`, read it back, hash it, and bind it with `REVIEW_HISTORY_INITIALIZED`. If the file exists while `review.latest_review_sha256` is null, adopt it only when its bytes are identical to the template and it contains no round and no addendum; otherwise stop.

Before appending round N, verify the current review hash equals `review.latest_review_sha256`, that `review.round = N-1`, and record inside the new round the pre-append Control `state_seq`, the pre-append Control hash and the previous review hash. Append exactly one complete round, read it back, hash the file, then register it in one Control update with `REVIEW_ROUND_RECORDED`.

If the append succeeds but the Control update fails, do not append the round again. Recovery requires the exact command `RECOVER REVIEW ROUND [N]` and every precondition in the review template: Control hash and sequence still equal the recorded pre-append values, exactly one new round exists after an unchanged prefix, no registration event exists, and all referenced hashes still match. Otherwise remain `NOT_VERIFIED`.

## Method references

Design method lives in `upstream/anthropics/knowledge-work-plugins/design/skills/`, copied verbatim from an Apache-2.0 source:

| File | Read it for |
|---|---|
| `accessibility-review/SKILL.md` | Accessibility criterion coverage for artifact 05 |
| `ux-copy/SKILL.md` | Copy-intent method for artifact 04 |
| `design-critique/SKILL.md` | Review structure for Tab 03 |

These are **method, not authority**. They are deliberately outside `.agents/skills/`: installed as active skills they would compete with this contract and a tab could load `accessibility-review` instead, losing the gate rules without any error.

Two deviations are recorded in `upstream/anthropics/knowledge-work-plugins/SOURCE.md` and both bind here:

- Upstream audits **WCAG 2.1**; this process records **2.2**. Audit against 2.2 and say so. Do not downgrade to match the copied text.
- Upstream assumes connected tools. A connector-dependent step is `NOT APPLICABLE` here, and skipping it is recorded. Inventing a connector result is fabrication.

When method and contract disagree, the contract wins. Cite the upstream path in the artifact that used it.

## Three-tab workflow

No automatic handoff. Each tab runs in a fresh conversation and reconstructs state from files.

### Tab 01 — Screen UX model

Entry: read this Skill, verify both sources, initialize or verify the Control File and the Decision Log identity.

"Verify the Control File" means exactly these six checks. Nothing else counts as verification, and a Control File that fails any of them is `NOT_VERIFIED`:

1. The YAML frontmatter parses. A file that does not parse is not state.
2. `schema_version` is `1`. Any other value stops the process; there is no migration path.
3. `state_seq` is a non-negative integer, and `len(event_log)` is either `state_seq` or `state_seq` minus the number of uncommitted events — if the two disagree by more than zero, report the discrepancy rather than reconciling it.
4. Every event in `event_log` has exactly the keys its `event_type` requires in `templates/CONTROL-FIELDS-v1.yaml`. Report missing and extra keys by name.
5. `decision_log.latest_sha256` is non-null and equals the actual SHA-256 of the file at `decision_log.path`.
6. `lifecycle_status` is consistent with the gate states: `FROZEN` requires `gate_3.status = APPROVED`; `DRAFT` requires `gate_3.status` not `APPROVED`.

The six checks above describe what verification means. The requirement is not to narrate them — it is to run them.

**Run the checker.** `test-harness/validate-control.py <control-file>` performs all six and prints `PASS` or the specific failures. Run it before writing any artifact and paste its output into the record. **The validator output is the record.** Do not proceed on `FAIL`.

Observed, twice, in both directions:

- An agent read the six checks, produced a correct artifact, ran the artifact validator, and executed none of the six. Its transcript contains no occurrence of `state_seq`, `schema_version`, `decision_log` or `lifecycle`. A checklist written but not run is decoration.
- Once the validator was mandatory, the same agent ran it and passed — but still never read the Control File. It treated the checker as a black box.

Both are acceptable, and the second is better. A requirement to narrate the six values *and* run a checker that already computes them gives two ways to comply, and an agent will pick the cheaper one. **When a mechanical check replaces a prose checklist, delete the prose requirement.** Keeping both does not double the rigour; it halves it.

Work:
- Enumerate **every** SCREEN ID from the frozen Process 04 inventory. A missing screen is a defect; an invented screen is a scope violation.
- For each screen: the user's goal, the primary action, secondary actions, information hierarchy in reading order, entry expectation, exit guarantee, and the capability IDs it serves.
- Describe how the user arrives in words. Do not cite `NODE-` or `TRANSITION-` IDs: the frozen App Flow carries neither, so such a citation can never be verified.
- Name the single primary action. Two primary actions means the hierarchy is unresolved.
- Record the cognitive load risk: what a first-time user is likely to misunderstand.
- Record only `GATE_1` decisions in the Decision Log.

Artifact: `01_SCREEN_UX_MODEL.md` from template `01`.

Gate 1 requires: every SCREEN ID present exactly once; no unknown screen; every entry citing at least one approved capability ID; exactly one primary action per screen; the structural block rule satisfied where a block is used; Decision Log hash matching `decision_log.latest_sha256`; **a `PASS` from `test-harness/validate-control.py` and from `test-harness/validate-ux-model.py`, both quoted in the record**; the user sending exactly `APPROVE SCREEN UX MODEL`; and one Control update that sets `gate_1.approved_state_seq`, `gate_1.decision_log_sha256`, the coverage snapshot and appends `GATE_1_APPROVED`.

Two validators, not one, because they fail independently: the control checker catches an inconsistent workspace, the artifact checker catches an artifact that does not match the frozen flow. An agent that runs only the artifact checker can pass a gate on a workspace the contract would reject.

Stop after Gate 1.

### Tab 02 — Patterns, states, content, accessibility

Entry: re-verify both sources, Gate 1 `APPROVED` with a matching event and sequence anchor, every Gate 1 artifact hash, and the Decision Log identity and hash.

Work:
- Define interaction patterns before using them. Each pattern gets an ID, when to use, when not to use, and the failure it prevents. Screens cite pattern IDs; a screen may not describe bespoke behaviour inline without a pattern.
- Build `03_STATE_EXPERIENCE.md` from the frozen Process 04 state matrix: one row per screen × state that applies to it. For each, what the user sees, understands and can do, and the recovery affordance. A state that exists in the matrix but has no row is a defect. A row for a state the matrix does not define is a scope violation.
- Every error, empty, loading, permission and destructive state needs an explicit recovery affordance or an approved decision stating there is none.
- `04_CONTENT_AND_COPY_INTENT.md` records what content each screen requires and the intent of each message. Intent, not wording. Final strings belong to Process 07.
- `05_ACCESSIBILITY_REQUIREMENTS.md` records the target conformance level once, then per-screen keyboard reachability, focus order intent, announcement intent and minimum target size. It states requirements; it does not choose tokens.

Before Gate 2, run explicit set comparisons and show the compared IDs:
- Set of SCREEN IDs in 01 = set in the frozen Process 04 inventory.
- Set of (screen, state) rows in 03 = the applicable projection of the Process 04 state matrix.
- Every pattern ID cited exists in 02; every pattern in 02 is cited at least once, or is marked as reserved with a reason.
- Every capability ID in the frozen Process 03 scope is served by at least one screen, or has an approved deferral decision.
- No named UI component appears in 01–05. The audit below is a **procedure**, not a word hunt. Run it exactly as written; a different procedure produces a different result on the same file, which makes the gate meaningless.

  **Banned terms.** button, card, modal, dialog, toast, chip, tab, drawer, tooltip, badge, banner, accordion. The target platform is Android, so the list also covers affordances an agent absorbs without noticing: app bar, top bar, bottom sheet, navigation rail, floating action button, FAB, snackbar, system back, predictive back, window size class, inset.

  **Procedure.**

  1. Scope: the artifact body only. Exclude any section headed `Rules for this artifact`, any fenced block that states the rule or draws a structural block, and any text inside a quoted source excerpt marked as quoted.
  2. **Exclude this workflow's own vocabulary before matching.** `Tab 01`, `Tab 02`, `Tab 03` and `TAB_01` are process roles, not UI affordances. So are `screen`, `state`, `pattern` and `component` when they appear as process nouns rather than as the name of something a user taps. Without this exception every artifact fails on its own header line — observed, and it is how an audit loses credibility on first contact.
  3. Matching: case-insensitive, whole word, on word boundaries. `card` matches `card` and `Card`; it does not match `discards` or `cardboard`. `tab` does not match `table`, and it does not match `Tab 01`.
  4. For every match, emit one row: the line number, the exact matched term, and the **full sentence** containing it.
  5. Classify each row: `VIOLATION` if the term names an affordance the user interacts with, `FALSE POSITIVE` if it appears in prose that describes a need rather than an affordance. State the reason in one clause.
  6. Report the count of `VIOLATION` rows. Gate 2 fails on any count above zero.

  **Why the procedure exists.** Two failure modes were observed when the audit was a bare word list. A literal grep matched `card` inside `discards` and failed a correct artifact. A model matched `component`, which is not on the list, and passed the artifact for the wrong reason. Neither implemented the rule. The sentence requirement in step 3 is what makes a wrong match visible in the record instead of buried in a judgement.

  A requirement may describe the need — "the user must be able to abandon this task without losing input" — but the affordance that satisfies it is chosen in Process 06, not named here.
- No colour value, hex code, font family, font size, spacing value, radius or shadow appears anywhere in 01–05.

Gate 2 binds hashes of 02–05 and the whole Decision Log. The user must send exactly `APPROVE UX SPEC`. One Control update sets `gate_2.approved_state_seq`, `gate_2.decision_log_sha256`, the coverage snapshot and appends `GATE_2_APPROVED`.

Stop after Gate 2.

### Tab 03 — Independent review and authorized freeze

Entry: re-verify both sources, Gates 1 and 2 `APPROVED` with matching events and sequence anchors, every bound hash, and the Decision Log hash equal to both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`. No `DECISION_LOG_UPDATED` event may follow Gate 2 approval.

Reviewer permissions: read-only on 01–05 and 08; may append to 06, create and update 07, and update the Control File only for review state, user-authorized risk acceptance, invalidation and explicit freeze. Must not edit 01–05 or 08. A flow-policy or UX-policy outcome requested during review pauses and returns to its owning tab.

Review:
- Build `07_UX_SPEC_DRAFT.md` from template `07`, containing the full detail of 01–05 and 08. It is not a summary.
- The draft begins with the exact line `> Status: REVIEWED CANDIDATE — NOT FROZEN`.
- Audit every artifact in full, not only the draft.
- Append one review round with findings, severity, exact artifact and IDs, evidence, scenario, impact, minimal correction and confidence.
- Severity: BLOCKER = a screen cannot be understood or completed as specified; CRITICAL = a state is unrecoverable or a requirement contradicts an approved capability; MAJOR = material gap or contradiction; MINOR = bounded ambiguity.
- Verdict GO / CONDITIONAL GO / HOLD. Review status becomes `READY_FOR_FREEZE` only when every finding is RESOLVED or explicitly ACCEPTED_BY_USER.

Remediation: BLOCKER and CRITICAL must be fixed and cannot be accepted. MAJOR and MINOR are fixed or accepted individually with the exact command `ACCEPT RESIDUAL RISK [FINDING-ID]` plus a rationale in the same message; persist the six-field record and append a dated addendum to 06. Never rewrite a historical finding row.

Freeze waits for the separate exact command `FREEZE UX SPEC`. It is never implied by GO, CONDITIONAL GO or a request to continue.

## Freeze protocol

Before writing, verify: both sources still `VERIFIED` with matching hashes; Gates 1 and 2 `APPROVED` with all bound hashes; `review.round >= 1` and the review hash matching `review.latest_review_sha256`; the latest round's artifact hashes matching current files; draft hash equal to both `review.reviewed_draft_sha256` and the latest round's draft hash; review status `READY_FOR_FREEZE` with zero open findings; every coverage counter equal to its source count; candidate version equal to `gate_3.frozen_version + 1`.

Create `UX_SPEC.md` by copying the exact bytes of the reviewed draft and replacing only the status line. No other transformation is permitted. Do not insert a hash or timestamp into the output.

Before re-freeze: verify the existing canonical hash, archive it byte-for-byte as `UX_SPEC.v<N>.md`, verify the archive, then replace. Never overwrite an existing archive.

Then update Gate 3 `APPROVED`, lifecycle `FROZEN`, set `gate_3.approved_state_seq` and append `GATE_3_FROZEN` in the same update. Read back and recompute. If the canonical file is written but the Control write or read-back fails, report **INCOMPLETE — NOT FROZEN**. An orphan `UX_SPEC.md` is not eligible downstream.

## Abandonment

On exactly `ABANDON UX SPEC`, record command and rationale, set lifecycle `ABANDONED` and stop. ABANDONED is terminal; restarting requires a new initiative ID and a separate workspace.

## Invalidation matrix

| Changed input or artifact | State action |
|---|---|
| Process 04 Control File, `APP_FLOW.md`, or the Process 03 hash bound through it | both sources `REOPENED`; Gates 1–3 reopened; lifecycle `REVIEW_REQUIRED` |
| `01_SCREEN_UX_MODEL.md` | Gates 1–3 reopened |
| `02`–`05` | Gates 2–3 reopened; Gate 1 remains valid only if no screen goal or primary action changed |
| `06_UX_REVIEW.md` or `07_UX_SPEC_DRAFT.md` | Gate 3 reopened; new review round required |
| `08_DECISION_LOG.md` before Gate 2 | reopen the earliest independently verified affected gate and all downstream gates |
| Any `08_DECISION_LOG.md` byte change after Gate 2 | always reopen Gates 2–3; also Gate 1 when independent classification is `GATE_1` |
| `UX_SPEC.md` after freeze | Gate 3 reopened; lifecycle `REVIEW_REQUIRED`; downstream use prohibited |

Every invalidation appends timestamp, `state_seq`, changed paths, previous and new hashes, affected gates and reason. Never silently overwrite an approval.

## Required quality checks

- Every SCREEN ID has exactly one entry; no unknown screen exists.
- Every screen has exactly one primary action and a stated exit guarantee.
- Every applicable state has a row with a recovery affordance or an approved decision.
- Every capability in the frozen scope is served by at least one screen or has an approved deferral.
- Every pattern cited exists and every pattern exists for a reason.
- Zero named components, zero colour or typography values, zero spacing values.
- Every accessibility requirement is stated as a requirement, not a token choice.
- All set comparisons are shown, not asserted.
- No screen, state or capability was added, removed or reinterpreted.
- Every open question, decision and accepted risk is visible in 06 or 08.

If any check cannot be verified, report `NOT_VERIFIED` rather than `PASS`.
