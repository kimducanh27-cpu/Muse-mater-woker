---
name: app-flow
description: Run Process 04 App Flow from a frozen Product Definition. Define tasks, navigation, functional screens, transitions, states, exceptions and recovery. Includes independent review and an explicitly authorized freeze protocol.
---

# App Flow — Process 04

## Mission and process boundary
Translate the approved Process 03 Product Definition into a complete, testable functional model of how users accomplish the product's promised outcomes.

- Process 02 establishes opportunity and evidence.
- Process 03 defines WHAT and WHY, including approved capability scope.
- Process 04 defines functional user tasks, flow architecture, navigation, functional screen nodes, transitions, states, exceptions, recovery and completion.
- A later product-design process may derive UX/UI and visual design from the frozen App Flow.

Process 04 does not create wireframes, visual layouts, colors, typography, components, design systems, polished UI mockups, interaction microcopy, animations, APIs, database architecture, implementation plans, tickets or code. Screen descriptions are functional contracts, not visual specifications. Never add a capability absent from the frozen Product Definition.

## Required input and fail-closed eligibility
Canonical Process 03 files:
- Control: `product/definition/00_PRODUCT_DEFINITION_CONTROL.md`
- Frozen output: `product/definition/PRODUCT_DEFINITION.md`

Read the YAML frontmatter of the Process 03 Control File. Verify:
1. Process 03 `initiative_id` is present.
2. Process 03 `gate_3.status = APPROVED`.
3. Process 03 `lifecycle_status = FROZEN`.
4. Process 03 `gate_3.frozen_artifact.path` equals `product/definition/PRODUCT_DEFINITION.md`.
5. The actual SHA-256 of `PRODUCT_DEFINITION.md` equals **Process 03 Control File field `gate_3.frozen_artifact.sha256`**. This is the authoritative comparison target. Do not compare only against a value cached in the Process 04 Control File.
6. Process 04 `initiative_id` and `source_process_03.initiative_id` equal Process 03 `initiative_id`.
7. The frozen Product Definition is readable and contains an identifiable approved capability scope.

If any check is missing, unreadable, contradictory or mismatched, set/retain `source_process_03.status = NOT_VERIFIED`, stop, and report the exact missing evidence. Never infer approval from chat, filenames, a prior agent claim or a user saying that a file has not changed.

At every tab entry and immediately before each approval/freeze, re-read the source Control File and recompute the canonical Product Definition hash. If the Process 03 source changes, mark the handoff REOPENED, reopen all dependent Process 04 gates and set lifecycle to REVIEW_REQUIRED. Do not continue against a superseded definition.

Preserve all approved capability IDs, IN / NOT NOW / OUT boundaries, target segment, customer outcomes, constraints, risks and non-goals. A missing flow requirement is not permission to invent a capability. Record it as an OPEN QUESTION or CHANGE REQUEST and ask the user whether it requires returning to Process 03.

## Canonical state, templates and artifacts
Canonical Control File: `product/app-flow/00_APP_FLOW_CONTROL.md`  
Control template: `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md`

Working artifacts:
- `01_TASK_MODEL.md`
- `02_FLOW_ARCHITECTURE.md`
- `03_NAVIGATION_MODEL.md`
- `04_SCREEN_INVENTORY.md`
- `05_FLOW_SPECIFICATION.md`
- `06_STATE_AND_EXCEPTION_MATRIX.md`
- `07_FLOW_REVIEW.md` — append-only review history
- `08_APP_FLOW_DRAFT.md` — complete reviewed freeze candidate, not a summary
- `09_DECISION_LOG.md` — append-only user-approved flow decisions

Canonical frozen output: `product/app-flow/APP_FLOW.md`  
Frozen-output schema: `templates/04-APP-FLOW/09-APP-FLOW.md`  
Decision-log template: `templates/04-APP-FLOW/10-DECISION-LOG.md`

Use each named template. Preserve required headings, tables and columns. Do not replace a structured template with an unstructured narrative. Required sections must be populated; where a section does not apply, write NOT APPLICABLE with a specific rationale. Do not leave template placeholders blank.

## Hashes and timestamps
Use SHA-256 for the source, gate-approved artifacts, decision log, review history, reviewed draft and frozen output. On Windows, use this exact PowerShell pattern and lowercase the hash:

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath ".\product\app-flow\01_TASK_MODEL.md").Hash.ToLowerInvariant()
```

Use a real local timestamp in Asia/Ho_Chi_Minh. On Windows:

```powershell
$zone = [TimeZoneInfo]::FindSystemTimeZoneById('SE Asia Standard Time')
[TimeZoneInfo]::ConvertTime([DateTimeOffset]::UtcNow, $zone).ToString('yyyy-MM-dd HH:mm:ss zzz')
```

Never invent hashes or timestamps. If terminal/hash/timestamp/file read is unavailable, record NOT_VERIFIED and block the affected gate.

## Control File and state integrity
The Control File is canonical state. Initialize it from the control template only if it does not exist. Never overwrite another initiative's Control File.

Allowed values:
- Gate states: `PENDING`, `APPROVED`, `REJECTED`, `REOPENED`.
- Lifecycle: `DRAFT`, `REVIEW_REQUIRED`, `FROZEN`, `ABANDONED`.
- Process 03 source status: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- Review status: `NOT_STARTED`, `BLOCKERS_FOUND`, `READY_FOR_FREEZE`.
- Finding severity: `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`.
- Finding status: `OPEN`, `RESOLVED`, `ACCEPTED_BY_USER`.

Gate 3 status remains APPROVED after a successful freeze; only `lifecycle_status` becomes FROZEN. A source or artifact change reopens the affected gate(s); do not invent a state value.

Every Control File update is single-writer:
1. Read the current Control File and record `state_seq`.
2. Recompute prerequisite hashes and verify the current state.
3. Calculate the next committed sequence (`current state_seq + 1`), apply one state update and append an event to `event_log`; never delete or rewrite prior events. The event's `state_seq` must equal that new committed sequence, not the stale value read before the update.
4. Persist the new `state_seq` and real local timestamp.
5. Read the Control File back and verify the expected state, event and hashes.
6. Report success only after read-back succeeds.

`state_seq` is a stale-read detector, not a lock or atomic transaction. Never let two tabs write the Control File concurrently. If the sequence changed unexpectedly, stop, reload and reconcile. If a write/read-back fails, report INCOMPLETE / NOT_VERIFIED; do not infer or repair state by guessing.

Exact commands:
- Gate 1: `APPROVE TASK MODEL`
- Gate 2: `APPROVE APP FLOW`
- Approve one user decision: `APPROVE FLOW DECISION [DECISION-ID]`
- Reject one proposed decision: `REJECT FLOW DECISION [DECISION-ID]`
- Defer one proposed decision: `DEFER FLOW DECISION [DECISION-ID]`
- Accept one MAJOR/MINOR review risk: `ACCEPT RESIDUAL RISK [FINDING-ID]`
- Gate 3 / freeze: `FREEZE APP FLOW`
- Reject: `REJECT TASK MODEL` / `REJECT APP FLOW`
- Change request: `REQUEST APP FLOW CHANGE [description]`
- Abandon this initiative: `ABANDON APP FLOW`

A command must be sent explicitly by the user. Natural-language praise, "looks good", "continue", silence, or a freeze request does not substitute for any other command. `FREEZE APP FLOW` never implies acceptance of a finding or decision.

### Residual-risk acceptance
Only MAJOR or MINOR findings may be accepted. BLOCKER and CRITICAL findings cannot be accepted to bypass remediation. For each residual-risk acceptance, the user must send the exact command and provide a rationale in the same message. Persist one record with:
- `finding_id`
- `severity`
- `accepted_by: user`
- `exact_command`
- `rationale`
- `accepted_at_local`

Append a matching user-decision addendum to the review history. Never accept on the user's behalf, infer acceptance, or accept multiple findings from a vague blanket statement.

### Decision log
The append-only `09_DECISION_LOG.md` records material product/flow-policy decisions, alternatives, rationale, affected artifacts and affected gate. A proposal is not a decided policy. The user must send exactly one of `APPROVE FLOW DECISION [DECISION-ID]`, `REJECT FLOW DECISION [DECISION-ID]`, or `DEFER FLOW DECISION [DECISION-ID]` and provide a rationale in the same message. Append a new status event for that DEC ID with the matching status APPROVED, REJECTED or DEFERRED; never edit or delete the original proposal. Only APPROVED decisions may define current flow policy. A DEFERRED decision may justify omitting a capability from the current flow only when the affected capability and scope impact are explicit. Any resulting artifact change must follow the invalidation matrix.

#### Decision Log hash tracking

`decision_log.latest_sha256` is the last verified SHA-256 of the current bytes in `product/app-flow/09_DECISION_LOG.md`; it is not a value to be regenerated merely to make a mismatch disappear.

- When the Decision Log is first initialized, compute its actual SHA-256 and record it in `decision_log.latest_sha256` before Gate 1 can be approved.
- After every append or status event, write and read back the Decision Log, recompute its SHA-256, then update `decision_log.latest_sha256` in the same single-writer Control File transaction. Append a `DECISION_LOG_UPDATED` event with the decision ID (if applicable), `affected_gate`, path, resulting hash and timestamp. The event's `state_seq` must equal the new committed Control File `state_seq` (previous value + 1), not the stale value read before the update. Read the Control File back and verify both the event and hash.
- Do not update `latest_sha256` before the Decision Log write/read-back succeeds. If either file or the Control File cannot be verified, stop with NOT_VERIFIED; do not claim the hash baseline was refreshed.
- A changed Decision Log reopens the earliest gate named by the appended decision's `affected_gate` and all downstream gates. A `GATE_1` change reopens Gates 1–3; a `GATE_2` change reopens Gates 2–3; a `GATE_3` change reopens Gate 3. Record the invalidation in the append-only event log.
- At Tab 02 entry, compare the actual Decision Log hash with the non-null `decision_log.latest_sha256`. Never repair a mismatch by copying the observed hash into the Control File; a mismatch is an unverified, potentially out-of-band edit.

## Three-tab workflow
No automatic handoff. Each tab runs in a fresh conversation in the same workspace and reconstructs state from files, not chat history. The user manually opens the next tab only after the previous gate's exact approval and read-back succeed.

### Tab 01 — User Tasks & Flow Architecture
Entry:
- Read this Skill and the Process 03 source files.
- Verify the source contract above, including comparison to `gate_3.frozen_artifact.sha256`.
- Initialize/verify Process 04 Control File; ensure initiative IDs match.
- Recompute any existing Gate 1/2 hashes before resuming.

Work:
- Extract only evidence-supported actors and roles.
- Enumerate **every** capability ID in the frozen Product Definition.
- Map each capability to one or more user tasks; if a capability cannot be mapped, record it as DEFERRED only after an explicit user-approved decision. Do not silently omit a capability.
- Identify user goals, entry points, triggers, preconditions, decision points, task sequence, alternate paths, interruption/recovery needs, completion criteria and observable outcomes.
- Distinguish evidence, interpretation, assumption and unresolved question.
- Record material flow-policy decisions in `09_DECISION_LOG.md` using its template; seek the exact decision approval command before treating a proposal as settled.

Artifacts:
- `product/app-flow/01_TASK_MODEL.md` from `templates/04-APP-FLOW/01-TASK-MODEL.md`
- `product/app-flow/02_FLOW_ARCHITECTURE.md` from `templates/04-APP-FLOW/02-FLOW-ARCHITECTURE.md`
- Initialize `product/app-flow/09_DECISION_LOG.md` from `templates/04-APP-FLOW/10-DECISION-LOG.md` if absent.

Gate 1 requires:
- All required template sections and columns are present and populated.
- `09_DECISION_LOG.md` exists, is readable, has been hashed, and its actual SHA-256 equals the non-null `decision_log.latest_sha256` recorded in the Control File. The latest hash baseline and a `DECISION_LOG_UPDATED` event must be read back successfully.
- Every approved capability is covered by at least one task or a user-approved DEFERRED decision.
- Every task maps to one or more approved capability IDs.
- No unresolved decision that changes the task model is treated as approved.
- Process 03 source remains VERIFIED.
- The user sends exactly `APPROVE TASK MODEL`.
- The Control File records exact hashes of 01 and 02, command and timestamp, increments `state_seq`, and passes read-back.

Stop after Gate 1. Do not start Tab 02 automatically.

### Tab 02 — Navigation & Screen Flow Specification
Entry in a fresh conversation:
- Re-verify Process 03 control, canonical Product Definition hash and initiative ID.
- Verify Gate 1 = APPROVED and recompute the exact hashes stored in `gate_1.approved_artifacts`.
- Read `product/app-flow/09_DECISION_LOG.md` and the Process 04 Control File. Require the log to be readable, `decision_log.latest_sha256` to be non-null, and the actual log SHA-256 to match that recorded value exactly.
- Inspect Decision Log entries and the append-only Control File `event_log`. Confirm that every decision affecting Gate 1 was settled before the latest `APPROVE TASK MODEL` event, and that no later `DECISION_LOG_UPDATED` event with `affected_gate: GATE_1` exists. Compare event `state_seq` values; if the relevant approval/update events are missing or cannot be ordered reliably, report NOT_VERIFIED.
- Treat only APPROVED decisions as active flow policy. REJECTED, DEFERRED and PROPOSED entries must not be used as approved rules. A PROPOSED or unresolved GATE_1 decision that changes the task model blocks Tab 02 and must return to Tab 01/user resolution; preserve it as an open question only when it does not determine the approved task model.
- If the Decision Log is missing/unreadable, `latest_sha256` is null, the hashes mismatch, or a GATE_1 decision changed after Gate 1 approval, conservatively reopen Gates 1–3, invalidate the review, set lifecycle to REVIEW_REQUIRED, append an invalidation event with expected/observed hash and affected decision/gate where known, read back the Control File, and stop. Do not refresh the expected hash to bless the changed file.
- If any Process 03 source or Gate 1 artifact differs, reopen the affected and downstream gates, append an invalidation event and stop.

Work:
- Define stable FLOW, NODE, SCREEN and TRANSITION IDs.
- Specify navigation structure and each functional screen node: purpose, entry conditions, required information, user actions, exits and destinations.
- Specify transitions with explicit guards, triggers and outcomes.
- Define back, cancel, retry, resume and external-entry behavior where applicable.
- Build the state/exception matrix. Include only applicable states, but justify every exclusion.
- Cover validation, permission, network/system failure, repeated submission, destructive action, interruption and recovery where relevant.
- Maintain traceability from each task, flow, node, screen and transition to approved capability IDs and source sections.
- Record material user decisions in the append-only decision log; use exact decision approval commands.
- Do not silently decide product policy or expand scope.

Artifacts:
- `03_NAVIGATION_MODEL.md` from `templates/04-APP-FLOW/03-NAVIGATION-MODEL.md`
- `04_SCREEN_INVENTORY.md` from `templates/04-APP-FLOW/04-SCREEN-INVENTORY.md`
- `05_FLOW_SPECIFICATION.md` from `templates/04-APP-FLOW/05-FLOW-SPECIFICATION.md`
- `06_STATE_AND_EXCEPTION_MATRIX.md` from `templates/04-APP-FLOW/06-STATE-AND-EXCEPTION-MATRIX.md`
- Append material decisions to `09_DECISION_LOG.md` using `templates/04-APP-FLOW/10-DECISION-LOG.md`.

Before Gate 2, perform explicit set-based integrity checks and show the compared IDs and differences:
- All task IDs in 01 appear in the task-to-flow mapping in 02.
- Every approved capability from Process 03 is covered or explicitly deferred by an approved user decision.
- All NODE IDs are unique; every node's SCREEN ID exists in 04 or is explicitly typed as a non-screen node.
- The set of Screen IDs in 04 equals the set of screen IDs referenced by navigation nodes, except explicitly documented exclusions.
- Every transition source/destination references an existing node, except explicitly declared external entry/terminal endpoints.
- Every flow has an entry and observable terminal/completion condition.
- Traverse each flow from its entry node; report reachable and unreachable node sets. No unexplained unreachable node, orphan screen, orphan transition, accidental loop or dead end is permitted.
- State/exception rows agree with the flow specification; every excluded state has a rationale.
- Required template headings/tables are present and no unresolved placeholder remains.
- Decision log has no unapproved proposal being treated as an approved product/flow rule.

Gate 2 binds exact hashes of 03–06 and the current decision-log file. It also requires Gate 1 and all its artifact hashes to remain valid. The user must send exactly `APPROVE APP FLOW`. Record command, timestamp, hashes, increment `state_seq`, read back, and verify.

Stop after Gate 2. Do not start Tab 03 automatically.

### Tab 03 — Independent Flow Review and authorized freeze
Entry in a fresh conversation:
- Re-verify Process 03 source and initiative identity.
- Verify Gate 1 and Gate 2 are APPROVED and recompute every artifact hash stored in both gates.
- Verify current decision-log hash matches Gate 2.
- If any check fails, reopen affected gate(s), append an invalidation event, and stop.

Reviewer permissions:
- Read-only for artifacts 01–06, 09 and all Process 03 sources.
- May append to 07, create/update complete draft 08, and update the Control File only for review state, user-authorized risk acceptance, invalidation and explicit freeze.
- Must not edit 01–06, 09 or Process 03 sources.
- Remediation returns to the owning tab. Changed artifacts invalidate affected gates and require re-approval plus a new independent review round.

Review:
- Review all artifacts in full, not only the draft or README.
- Build the complete freeze candidate `08_APP_FLOW_DRAFT.md` from the exact structure in `templates/04-APP-FLOW/09-APP-FLOW.md`. It must contain full detail from 01–06 and 09; it is not a summary.
- The draft begins with the exact line `> Status: REVIEWED CANDIDATE — NOT FROZEN`.
- Independently audit the source artifacts and complete candidate. Do not introduce, resolve or invent product decisions while assembling it.
- Append a new review round to `07_FLOW_REVIEW.md`; never overwrite prior rounds. Record hashes of Process 03 source, artifacts 01–06, decision log 09 and draft 08 in the round and Control File.
- Record explicit set-comparison results, graph reachability evidence, findings, severity, exact artifact/IDs, evidence, scenario, impact, minimal correction and confidence.
- Severity: BLOCKER = core task cannot be completed or fundamental contract broken; CRITICAL = severe flow-integrity, permission or data-loss barrier; MAJOR = material incomplete or contradictory behavior; MINOR = bounded ambiguity or low-impact omission.
- Verdict: GO / CONDITIONAL GO / HOLD. Set review status READY_FOR_FREEZE only when every finding is RESOLVED or explicitly ACCEPTED_BY_USER under the rules below; otherwise BLOCKERS_FOUND.

Remediation:
- BLOCKER/CRITICAL must be fixed; they cannot be accepted.
- MAJOR/MINOR must be fixed or accepted individually by the user.
- To accept one MAJOR/MINOR, the user must send exactly `ACCEPT RESIDUAL RISK [FINDING-ID]` and provide a rationale in the same message.
- Persist the six-field record in the Control File and append a dated user-decision addendum to 07. Never rewrite the historical finding row or accept on the user's behalf.
- If an artifact changes, the owning tab remediates it; recompute hashes, reopen affected gate(s), require re-approval and run a new full review round.

Freeze is owned by Tab 03, but is **not** part of the review action by default. Wait until the user sends the separate exact command `FREEZE APP FLOW`. Do not infer it from GO, CONDITIONAL GO or a general request to continue.

### Freeze protocol — execute only after the exact user command
Before writing the canonical output, verify:
1. Process 03 source remains VERIFIED; actual Product Definition hash equals Process 03 `gate_3.frozen_artifact.sha256`.
2. Gates 1 and 2 are APPROVED and every stored approved-artifact hash matches.
3. `review.round >= 1`; `07_FLOW_REVIEW.md` exists and its current hash equals `review.latest_review_sha256`.
4. Latest review records hashes matching current artifacts 01–06 and 09.
5. `08_APP_FLOW_DRAFT.md` exists and its hash equals both `review.reviewed_draft_sha256` and the latest review round's draft hash.
6. Latest review status is READY_FOR_FREEZE; open BLOCKER, CRITICAL, MAJOR and MINOR counts are all zero. Accepted MAJOR/MINOR risks have separate user-originated records and review addenda.
7. Every decision required for the current flow is approved or explicitly recorded as an unresolved question that does not alter the frozen contract.
8. Draft has all required sections and passed set/graph checks.
9. Candidate version equals `gate_3.frozen_version + 1`.

Create `APP_FLOW.md` by copying the exact bytes of the reviewed draft and replacing only:

`> Status: REVIEWED CANDIDATE — NOT FROZEN`

with:

`> Status: FROZEN`

No other editorial, structural or content transformation is allowed. Do not rebuild or re-summarize from 01–06. Do not insert a self-hash or freeze timestamp into the output; the canonical SHA-256 and timestamp belong in the Control File.

Before re-freezing:
- Verify existing `APP_FLOW.md` hash equals the Control File's frozen hash.
- Preserve it byte-for-byte as `APP_FLOW.v<N>.md`, where N is the previous frozen version.
- Never overwrite an existing archive. If it exists, verify it is byte-identical; otherwise stop.
- Hash and record the archive before replacing the canonical file.

Then write APP_FLOW.md, compute its SHA-256, read it back and verify it differs from the draft only by the exact status-line replacement. Update Gate 3 = APPROVED and lifecycle_status = FROZEN; record command, timestamp, source/review/draft/canonical hashes, version and archive metadata; increment state_seq; read the Control File back and recompute the canonical hash. Report success only after all checks pass.

If canonical output is written but Control File write/read-back fails, report **INCOMPLETE — NOT FROZEN**. An orphan APP_FLOW.md is not eligible downstream. File presence or a FROZEN status line alone is never proof of freeze.

## Abandonment
If the user sends `ABANDON APP FLOW`, record command and rationale, set lifecycle_status = ABANDONED and stop. ABANDONED is terminal; restart requires a new initiative ID and separate workspace/control path.

## Invalidation matrix

| Changed input/artifact | State action |
|---|---|
| Process 03 Control File or frozen Product Definition/source hash | source REOPENED; Gates 1–3 REOPENED; lifecycle REVIEW_REQUIRED |
| 01_TASK_MODEL.md or 02_FLOW_ARCHITECTURE.md | Gates 1–3 REOPENED |
| 03_NAVIGATION_MODEL.md, 04_SCREEN_INVENTORY.md, 05_FLOW_SPECIFICATION.md or 06_STATE_AND_EXCEPTION_MATRIX.md | Gates 2–3 REOPENED; Gate 1 remains valid |
| 07_FLOW_REVIEW.md or 08_APP_FLOW_DRAFT.md | Gate 3 REOPENED; new review round required |
| 09_DECISION_LOG.md | Reopen earliest gate named by appended decision's affected_gate and all downstream gates |
| APP_FLOW.md after freeze | Gate 3 REOPENED; lifecycle REVIEW_REQUIRED; downstream use prohibited |

Reopening Gate 1 also reopens Gates 2 and 3. Reopening Gate 2 also reopens Gate 3. Every invalidation appends timestamp, state_seq, changed paths, previous/new hashes, affected gates and reason. Never silently overwrite an approval.

## Required quality checks
- Every approved capability maps to one or more tasks or a user-approved DEFERRED decision.
- Every task maps to one or more approved capability IDs.
- Every flow/task/node/screen/transition has stable, unique IDs and traceable references.
- Every screen/node has purpose, entry condition and valid exit, except explicitly terminal outcomes.
- Every transition has an explicit condition or is explicitly unconditional; endpoints exist.
- Every flow has entry, completion condition and observable outcome.
- No unexplained unreachable node, orphan screen, orphan transition, dead-end path or accidental loop.
- Every critical failure path has recovery or an explicit user-approved decision.
- Screen inventory, flow graph and state matrix agree by explicit set comparisons, not assertion alone.
- All assumptions, decisions, risks and change requests are visible.
- No new capability, unsupported policy or scope expansion is introduced.

If any check cannot be verified, report NOT_VERIFIED rather than PASS.
