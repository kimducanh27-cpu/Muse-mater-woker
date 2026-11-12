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

If any check is missing, unreadable, contradictory or mismatched, set/retain `source_process_03.status = NOT_VERIFIED`, stop, and report the exact missing evidence. Never infer approval from chat, filenames, a prior agent claim or a user saying that a file has not changed. Any later process consuming `APP_FLOW.md` must independently recompute its SHA-256 and compare it with Process 04 `gate_3.frozen_artifact.sha256` while confirming Gate 3 APPROVED and lifecycle FROZEN. Process 04 has no background file watcher: post-freeze drift is detected at the next tab entry or downstream read, not asynchronously.

At every tab entry and immediately before each approval/freeze, re-read the source Control File and recompute the canonical Product Definition hash. If the Process 03 source changes, mark the handoff REOPENED, reopen all dependent Process 04 gates and set lifecycle to REVIEW_REQUIRED. Do not continue against a superseded definition.

If the Process 04 Control File says `lifecycle_status = FROZEN` or contains a previously frozen canonical artifact hash, every subsequent Process 04 tab entry, re-freeze attempt and downstream handoff must also recompute the actual SHA-256 of `product/app-flow/APP_FLOW.md` and compare it with `gate_3.frozen_artifact.sha256`. If the canonical file is missing, unreadable or mismatched, append a canonical `INVALIDATED` event, set `gate_3.status = REOPENED`, set `lifecycle_status = REVIEW_REQUIRED`, retain the expected hash (never replace it with the observed hash), block downstream use, read the Control File back and stop. This is detection on the next tab entry/downstream read, not a background watcher; the manual three-tab model does not monitor files continuously.

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
- `10_CHANGE_REQUEST_REGISTER.md` — append-only sole source of truth for Change Request business state (Register schema v1)

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

`state_seq` is a stale-read detector, not a lock, compare-and-swap operation or atomic transaction. The manual three-tab model therefore has a hard single-writer invariant: only one tab may perform a Control File or Decision Log write at a time. The operator must not run overlapping write operations. A pre-write re-read and post-write read-back reduce stale-write risk but cannot eliminate a read-read-write-write race. If concurrent writes may have occurred, stop all tabs; do not certify the event history from `state_seq` alone. Reconcile the Control File against the last trusted persisted copy and every surviving event before resuming. If that cannot be done deterministically, remain NOT_VERIFIED.

### Canonical event schema
Every `event_log` object MUST include `event_type`, `state_seq`, `timestamp_local`, `exact_user_command` (or `NOT_APPLICABLE`), `reason`, `changed_paths` and `relevant_hashes`. The event's `state_seq` must equal the new committed Control File sequence. Use only these canonical event types and required type-specific fields:

- `DECISION_LOG_UPDATED`: `decision_id`, `decision_log_event_id`, `decision_event_kind` (`INITIALIZATION`, `PROPOSAL_CREATED` or `DECISION_STATUS_CHANGED`), `decision_status_before_update`, `decision_status_after_update`, `affected_gate`, `path`, `resulting_sha256`.
- `GATE_1_APPROVED`: `gate: GATE_1`, `exact_user_command: APPROVE TASK MODEL`, `approved_artifacts` (01 and 02 path/hash pairs), `decision_log_sha256`.
- `GATE_2_APPROVED`: `gate: GATE_2`, `exact_user_command: APPROVE APP FLOW`, `approved_artifacts` (03–06 path/hash pairs), `decision_log_sha256`.
- `GATE_3_FROZEN`: `gate: GATE_3`, `exact_user_command: FREEZE APP FLOW`, `draft_sha256`, `frozen_artifact_path`, `frozen_artifact_sha256`, `frozen_version`.
- `INVALIDATED`: `reopened_gates`, `affected_gate` when known, `expected_hashes`, `observed_hashes` and reason.
- `DECISION_LOG_RECOVERED`: `decision_id`, `decision_log_event_id`, `recovered_from_event_seq`, `resulting_sha256`, `affected_gate`, `reopened_gates`.
- `REVIEW_HISTORY_INITIALIZED`: `review_path`, `review_sha256`.
- `REVIEW_ROUND_RECORDED`: `review_round`, `review_path`, `previous_review_sha256`, `review_sha256`, `draft_path`, `draft_sha256`, `verdict`, `review_status`.
- `REVIEW_ROUND_RECOVERED`: `review_round`, `review_path`, `previous_review_sha256`, `review_sha256`, `draft_path`, `draft_sha256`, `verdict`, `review_status`, `recovered_from_state_seq`.
- `SCHEMA_MIGRATED`: `from_schema_version: 2`, `to_schema_version: 3`, `archive_directory`, `archive_manifest_path`, `archive_manifest_sha256`, `archived_control_file_path`, `archived_control_file_sha256`, `archived_decision_log_path`, `archived_decision_log_sha256`, `exact_user_command`.
- `RESIDUAL_RISK_ACCEPTED`, `GATE_REJECTED`, `REVISION_REQUESTED` and `APP_FLOW_ABANDONED`: include the exact target IDs/paths, reason and hashes needed to reconstruct the transition.

The Control File's `gate_1.approved_state_seq`, `gate_2.approved_state_seq` and `gate_3.approved_state_seq` must equal the sequence of their latest corresponding approval/freeze event. A gate may not be treated as approved/frozen from its status field alone. Never infer an approval event from `approved_command` or prose.

If a schema-version-2 Control File already exists, do not silently fill missing event fields or sequence anchors. Stop with NOT_VERIFIED. Migration is permitted only after the user sends exactly `MIGRATE APP FLOW CONTROL V2 TO V3`:

1. Stop all tabs and freeze writes. Move the **entire** existing `product/app-flow/` directory, byte-for-byte, to `product/app-flow-migrations/<initiative-id>/schema-v2/`. This includes the Control File, Decision Log, artifacts 01–08, review history, canonical `APP_FLOW.md`, version archives and any other files. Do not leave the old `APP_FLOW.md` or old review/draft at an active Process 04 path. Never overwrite an existing migration archive. Generate an archive manifest listing every relative path, byte size and actual SHA-256; read the manifest back and verify every archived file against it.
2. Re-verify the frozen Process 03 source and Process 04 initiative ID. Because the old directory move also archives the tracked `product/app-flow/README.md`, restore the current repository version from the checked-out HEAD using `git restore --source=HEAD -- product/app-flow/README.md`; do not restore the archived README as the active version. Verify the restored README against the checked-out HEAD, then recreate the remaining active `product/app-flow/` workspace from current schema-v3 templates. Create a fresh Control File for the same initiative ID with source status VERIFIED only after a new Process 03 hash check, all three gates PENDING, `lifecycle_status: REVIEW_REQUIRED`, review round 0, no inherited approval sequence anchors, and `state_seq: 1`. Append one `SCHEMA_MIGRATED` event at sequence 1 recording the archive directory, manifest path/hash, old Control File path/hash, old Decision Log path/hash, old/new schema versions and exact user command. No old frozen output is eligible downstream.
3. Initialize a new schema-v3 Decision Log with the immutable `Process: 04` and matching Initiative ID. Do not alter the archived v2 log. Re-enter each still-relevant legacy decision as a new PROPOSED entry referencing its legacy DEC ID and archive location; no legacy APPROVED/REJECTED/DEFERRED status automatically carries forward. Obtain a fresh exact user outcome for each decision and record each append/hash transaction.
4. Restore artifacts 01–06 from the archive only after validating each against current templates and the newly verified frozen Process 03 scope; otherwise regenerate the affected artifact. Create a new 07 review history and new 08 draft. Do not restore old review status, review counts, draft hashes, frozen output, or version archives to active paths. Re-approve Gate 1 and Gate 2 using canonical events and sequence anchors; run a new independent review before any freeze. Do not carry forward any v2 gate approval or frozen claim.
5. Read back the schema-v3 Control File, identity-bound Decision Log, archive manifest, restored/regenerated artifacts and every recorded hash. If any archive, identity, artifact or event cannot be verified, remain NOT_VERIFIED.

The migration event type `SCHEMA_MIGRATED` must include exactly `from_schema_version: 2`, `to_schema_version: 3`, `archive_directory`, `archive_manifest_path`, `archive_manifest_sha256`, `archived_control_file_path`, `archived_control_file_sha256`, `archived_decision_log_path`, `archived_decision_log_sha256` and `exact_user_command`. The manifest is the authoritative list of all archived files and their hashes.

Exact commands:
- Gate 1: `APPROVE TASK MODEL`
- Gate 2: `APPROVE APP FLOW`
- Approve one user decision: `APPROVE FLOW DECISION [DECISION-ID]`
- Reject one proposed decision: `REJECT FLOW DECISION [DECISION-ID]`
- Defer one proposed decision: `DEFER FLOW DECISION [DECISION-ID]`
- Accept one MAJOR/MINOR review risk: `ACCEPT RESIDUAL RISK [FINDING-ID]`
- Gate 3 / freeze: `FREEZE APP FLOW`
- Recover one interrupted Decision Log transaction only under the bounded procedure below: `RECOVER DECISION LOG [DECISION-ID]`
- Recover one complete but unregistered review round only under the bounded procedure below: `RECOVER REVIEW ROUND [N]`
- Reject: `REJECT TASK MODEL` / `REJECT APP FLOW`
- Change request: `REQUEST APP FLOW CHANGE [description]`
- Abandon this initiative: `ABANDON APP FLOW`
- Migrate a schema-v2 workspace only under the procedure above: `MIGRATE APP FLOW CONTROL V2 TO V3`

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
The append-only `09_DECISION_LOG.md` records material product/flow-policy decisions, alternatives, rationale, affected artifacts and affected gate. A proposal is not a decided policy. The user must send exactly one of `APPROVE FLOW DECISION [DECISION-ID]`, `REJECT FLOW DECISION [DECISION-ID]`, or `DEFER FLOW DECISION [DECISION-ID]` and provide a rationale in the same message. Append a canonical status event for that DEC ID; never edit or delete the original proposal. Only a current, verified APPROVED decision may define flow policy. A DEFERRED decision may justify omitting a capability only when the affected capability and scope impact are explicit. Any resulting artifact change must follow the invalidation matrix.

#### Canonical Decision Log status-event schema

Every new proposal block must have a unique `Proposal Event ID: DLE-<NNNN>` and immutable `Status at proposal: PROPOSED`. Every outcome is a separate append-only `Status event — DLE-<NNNN>` with unique Event ID, `Event kind: DECISION_STATUS_CHANGED`, DEC ID, status-before/status-after, exact user command, user rationale, user identity, local timestamp, affected gate, affected artifact paths/IDs, and `Supersedes status event ID`. The first status event uses previous status PROPOSED and supersedes NONE; each later status event must reference the immediately preceding valid status event and its current status. Do not append a duplicate event when the requested status already equals the current status. A status event cannot change the proposal's scope or affected gate; a scope/meaning change requires a new DEC ID.

For every proposal or status-event append, the single matching Control File `DECISION_LOG_UPDATED` event must carry `decision_id`, `decision_log_event_id`, `decision_event_kind`, `decision_status_before_update`, `decision_status_after_update`, `affected_gate`, path and `resulting_sha256`. Use `decision_event_kind: PROPOSAL_CREATED`, before `NOT_APPLICABLE`, after `PROPOSED` for a proposal; use `DECISION_STATUS_CHANGED` and the exact before/after status for a status event. Initialization uses `decision_log_event_id: INITIALIZATION`, kind `INITIALIZATION`, and NOT_APPLICABLE for the decision-specific fields. Each Decision Log event ID must have exactly one matching Control File event; IDs are unique and event pairs must agree on DEC ID, kind, status, scope, path and resulting hash.

Reconstruct a DEC ID's current status from its valid paired Control File events ordered by committed `state_seq`: the highest-sequence valid event determines status; if only the proposal event exists, status is PROPOSED. The status-event chain must be continuous. Any missing, duplicate, malformed, out-of-order or mismatched pair makes that DEC ID NOT_VERIFIED and it must not be used as approved policy. A legacy entry without a proposal event ID, or a legacy inline status/decision field without a matching canonical status event and Control File event, is LEGACY_UNVERIFIED; preserve its bytes and do not treat it as approved. Re-enter a still-needed legacy decision as a new proposal with a new DEC ID and provenance, then obtain a fresh explicit user outcome.

#### Decision Log identity and gate classification

The immutable identity header at the top of `09_DECISION_LOG.md` must contain `Process: 04` and an `Initiative ID` exactly equal to the Process 04 Control File and verified Process 03 source initiative ID. On initialization, populate the ID from the verified source. If a Decision Log already exists and its identity is absent, unreadable or mismatched, stop with NOT_VERIFIED; never adopt it by hashing its current bytes and never rewrite its identity header. The Decision Log is one-initiative-only.

Derive `affected_gate` from the decision's actual semantic scope and affected artifacts; it is not a free-form assertion:
- `GATE_1`: changes to `01_TASK_MODEL.md`, `02_FLOW_ARCHITECTURE.md`, actors/tasks, approved capability interpretation, or capability-to-task coverage.
- `GATE_2`: changes limited to `03_NAVIGATION_MODEL.md`, `04_SCREEN_INVENTORY.md`, `05_FLOW_SPECIFICATION.md` or `06_STATE_AND_EXCEPTION_MATRIX.md`.
- `GATE_3`: changes limited to review/freeze artifacts `07_FLOW_REVIEW.md` or `08_APP_FLOW_DRAFT.md` that do not alter 01–06.
- If more than one layer is affected, choose the earliest affected gate. Any proposed change to Process 03 scope or approved capability boundaries must return to Process 03; Process 04 cannot relabel it as a local decision.

Before trusting an entry, the owning tab must independently compare `affected_gate` with the affected artifact paths/IDs and decision text. A mismatch or ambiguous classification means NOT_VERIFIED; do not use the self-declared label to preserve an upstream approval.

#### Decision Log hash tracking

`decision_log.latest_sha256` is the last verified SHA-256 of the current bytes in `product/app-flow/09_DECISION_LOG.md`; it is not a value to be regenerated merely to make a mismatch disappear.

- On first initialization, verify the identity header, write the template, read it back, compute its actual SHA-256, then record that hash and a `DECISION_LOG_UPDATED` initialization event (`decision_id: NOT_APPLICABLE`, `decision_status_after_update: NOT_APPLICABLE`, `affected_gate: GATE_1`) before Gate 1 can be approved.
- After every proposal or status append by the owning tab: write the log, read it back, compute its actual SHA-256, then in one single-writer Control File update set `decision_log.latest_sha256`, increment `state_seq`, and append exactly one `DECISION_LOG_UPDATED` event containing `decision_id`, `decision_log_event_id`, `decision_event_kind`, `decision_status_before_update`, `decision_status_after_update`, `affected_gate`, path, `resulting_sha256`, timestamp and the same new committed `state_seq`. Read the Control File back and verify every field and one-to-one event pairing. This rule applies to Tab 01 and Tab 02; Tab 03 is read-only on the Decision Log and must never append to it.
- Do not update `latest_sha256` before the Decision Log write/read-back succeeds. If either file or the Control File cannot be verified, stop with NOT_VERIFIED; do not claim the baseline was refreshed.
- Gate 1 approval must append a distinct `GATE_1_APPROVED` event in the same Control File update that marks Gate 1 APPROVED. That event snapshots the exact Decision Log hash at approval time. Tab 02 locates the latest valid event by `event_type` and maximum `state_seq`, then compares it with later `DECISION_LOG_UPDATED` events.
- Gate 2 approval binds the entire current Decision Log file hash. Therefore, after Gate 2 is APPROVED, any subsequent Decision Log byte change reopens Gates 2 and 3, regardless of whether the entry is labeled GATE_2 or GATE_3. If the independently classified change affects Gate 1, reopen Gates 1–3. Never keep Gate 2 APPROVED against a changed whole-file hash and never rewrite its approved hash in place.
- Before Gate 2 is approved, a valid GATE_2 change reopens Gates 2–3 and a valid GATE_3 change reopens Gate 3; Gate 1 may remain approved only when the decision is independently verified not to affect Gate 1. A GATE_1 change reopens Gates 1–3.
- A missing/unreadable log, wrong initiative ID, null baseline, unexplained hash mismatch or unclassifiable decision makes the decision state NOT_VERIFIED. Conservatively reopen Gates 1–3, invalidate review, set lifecycle REVIEW_REQUIRED, append `INVALIDATED` with expected/observed hashes and reopened gates, read back and stop. Never bless the observed hash.

#### Bounded recovery after an interrupted Decision Log write

Recovery is not automatic. Stop all tabs and do not approve, freeze or append further decisions. Compute the actual log hash and inspect the complete Control File event history.

1. If the actual hash exactly equals the `resulting_sha256` of one well-formed, already persisted `DECISION_LOG_UPDATED` event for the same DEC ID/status/path/affected gate, and that event has a valid committed sequence, the user may authorize `RECOVER DECISION LOG [DECISION-ID]`. Only then may the owning tab set `latest_sha256` to that already-recorded hash, append `DECISION_LOG_RECOVERED` referencing the original `decision_log_event_id` and Control File event sequence, reopen the affected gates (and Gates 2–3 if Gate 2 had already bound the prior whole-file hash), increment `state_seq`, read back and verify. Do not invent or rewrite the original event.
2. If no exact matching event exists, do not adopt the observed bytes. Restore the Decision Log from a trusted copy whose actual hash equals the previously stored `latest_sha256`; read it back and verify. If no such copy exists, remain NOT_VERIFIED and require a human-led forensic reconciliation outside the active workflow.
3. If the Control File itself is partial, malformed or lacks a verifiable event trail, do not synthesize missing events. Restore a trusted Control File copy or stop. Never use a new baseline to make an unexplained mismatch pass.

#### Bounded recovery after an interrupted review-round write

A review round is appended to `07_FLOW_REVIEW.md` before its summary metadata is committed to the Control File. A failed Control File update must not cause the same review round to be appended twice.

Before Round 1, if `07_FLOW_REVIEW.md` is absent, initialize it from `templates/04-APP-FLOW/07-FLOW-REVIEW.md`, read it back and compute its SHA-256. If it already exists while `review.latest_review_sha256` is null, it may be adopted as the initial baseline only when its bytes are exactly identical to that template and it contains no review round or user-decision addendum; otherwise stop with NOT_VERIFIED. In one Control File update set `review.latest_review_sha256` to that verified template-copy hash and append `REVIEW_HISTORY_INITIALIZED` with the canonical path/hash. Read back and verify before any round is appended.

Before appending a new round N, Tab 03 must verify that the current review history SHA-256 equals `review.latest_review_sha256`, `review.round = N-1`, and record inside the new round `Control File state_seq before append`, `Control File SHA-256 before append` and `Previous review history SHA-256`. Append exactly one complete `### Review round N`, read it back and hash the complete file. Then, in one Control File update, set the round number, latest review path/hash, reviewed draft path/hash, reviewed artifact hashes, finding counts and review status, and append `REVIEW_ROUND_RECORDED` with `review_round`, `review_path`, `previous_review_sha256`, `review_sha256`, `draft_path`, `draft_sha256`, verdict and review status. Read back and verify all fields before claiming the round is registered.

If the review-file append/read-back succeeds but the Control File update fails or is ambiguous, stop all writers and do not append the round again. The user may send exactly `RECOVER REVIEW ROUND [N]` only when every condition below holds:

1. The Control File is readable and its actual SHA-256 exactly equals the `Control File SHA-256 before append` recorded inside Round N; its `state_seq` remains the recorded pre-append value, `review.round = N-1` and `review.latest_review_sha256` remains the previously trusted hash.
2. The current review file contains exactly one complete new Round N appended after the prior bytes; hashing the exact prefix before Round N reproduces the previously trusted `review.latest_review_sha256`. No duplicate or later round exists.
3. The new round records the same pre-append state sequence, pre-append Control File hash and previous review hash, and its source, initiative, artifact 01–06, Decision Log and draft hashes all still match the current verified files.
4. No `REVIEW_ROUND_RECORDED` or `REVIEW_ROUND_RECOVERED` event for N exists, and no concurrent writer or intervening Control File update occurred.

After the exact recovery command, do not modify the review file. In one Control File update, register the already-appended round's verified metadata and append `REVIEW_ROUND_RECOVERED` with `review_round`, review path, previous/resulting review hashes, draft path/hash, verdict, review status and `recovered_from_state_seq`. Increment sequence, read back and verify. If any precondition fails, the Control File is partial/unreadable, a matching event already exists, or any source/artifact/draft hash has changed, remain NOT_VERIFIED and require human-led reconciliation or a new complete review round. Never invent a missing `REVIEW_ROUND_RECORDED` event, overwrite prior history or silently bless an orphan.

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
- Record only GATE_1-scope decisions in `09_DECISION_LOG.md`. If a proposed decision affects navigation/screens/flow/state artifacts (GATE_2/GATE_3), do not append it in Tab 01; return it to Tab 02. Classify scope from the actual decision and affected artifacts, not from the proposed label. Seek the exact decision approval command before treating a proposal as settled.

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
- The Control File records exact hashes of 01 and 02, sets `gate_1.decision_log_sha256` to the actual Decision Log SHA-256 at approval time, and sets `gate_1.approved_state_seq` to the new committed `state_seq`; and appends `GATE_1_APPROVED` in the same update. Required event fields: `event_type: GATE_1_APPROVED`, `gate: GATE_1`, `exact_user_command: APPROVE TASK MODEL`, `state_seq`, `timestamp_local`, 01/02 approved-artifact path/hash pairs, `decision_log_sha256`, `changed_paths`, `relevant_hashes` and `reason`. Event sequence, `gate_1.approved_state_seq` and Control File `state_seq` must be identical. `approved_command` or `status: APPROVED` without this event is invalid.

Stop after Gate 1. Do not start Tab 02 automatically.

### Tab 02 — Navigation & Screen Flow Specification
Entry in a fresh conversation:
- Re-verify Process 03 control, canonical Product Definition hash and initiative ID.
- Verify Gate 1 = APPROVED; require the latest valid `GATE_1_APPROVED` event with `gate: GATE_1`, `exact_user_command: APPROVE TASK MODEL` and maximum applicable `state_seq`. Require `gate_1.approved_state_seq` to equal that event's `state_seq` and `gate_1.decision_log_sha256` to equal that event's `decision_log_sha256`; recompute every hash in `gate_1.approved_artifacts`.
- Read `09_DECISION_LOG.md`; require immutable `Process: 04` / `Initiative ID` to match both Control Files, `latest_sha256` to be non-null, and actual SHA-256 to match exactly.
- Independently classify every Decision Log entry from its text and affected paths/IDs. Confirm no GATE_1-affecting update occurred after the latest `GATE_1_APPROVED` event. Require canonical event types/fields and exact committed sequence values. Missing, malformed, mislabeled or unorderable events mean NOT_VERIFIED; never infer approval from `gate_1.approved_command` alone.
- Treat only APPROVED decisions as active flow policy. REJECTED, DEFERRED and PROPOSED entries must not be used as approved rules. A PROPOSED or unresolved GATE_1 decision that changes the task model blocks Tab 02 and must return to Tab 01/user resolution; preserve it as an open question only when it does not determine the approved task model.
- If the Decision Log is missing/unreadable, identity is wrong/missing, `latest_sha256` is null, hashes mismatch, a decision is misclassified, or a GATE_1 decision changed after Gate 1 approval, conservatively reopen Gates 1–3, invalidate the review, set lifecycle to REVIEW_REQUIRED, append canonical `INVALIDATED` with expected/observed hashes, affected decision and `reopened_gates`, read back and stop. Use only the bounded recovery procedure above; never bless unexplained bytes.
- If any Process 03 source or Gate 1 artifact differs, reopen the affected and downstream gates, append an invalidation event and stop.

Work:
- Define stable FLOW, NODE, SCREEN and TRANSITION IDs.
- Specify navigation structure and each functional screen node: purpose, entry conditions, required information, user actions, exits and destinations.
- Specify transitions with explicit guards, triggers and outcomes.
- Define back, cancel, retry, resume and external-entry behavior where applicable.
- Build the state/exception matrix. Include only applicable states, but justify every exclusion.
- Cover validation, permission, network/system failure, repeated submission, destructive action, interruption and recovery where relevant.
- Maintain traceability from each task, flow, node, screen and transition to approved capability IDs and source sections.
- Record material GATE_2/GATE_3 decisions in the append-only Decision Log. Classify scope from affected artifacts and decision meaning; if it affects Gate 1, stop and return it to Tab 01. After every append/status event, execute the full write/read-back/hash/Control File `DECISION_LOG_UPDATED` transaction above, including `decision_status_after_update`, `resulting_sha256` and the same new committed `state_seq`. A Gate 2 decision must not change 01/02 or approved capability-to-task mapping.
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

Gate 2 binds exact hashes of 03–06 and the current entire Decision Log file. It also requires Gate 1 and all its artifact hashes to remain valid. The user must send exactly `APPROVE APP FLOW`. In the same Control File update that sets Gate 2 APPROVED, set `gate_2.approved_state_seq` and `gate_2.decision_log_sha256`, and append `GATE_2_APPROVED` with the exact command, approved path/hash pairs for 03–06 and the current Decision Log path/hash. Event sequence, gate sequence and new committed `state_seq` must be identical. Read back and verify.

Stop after Gate 2. Do not start Tab 03 automatically.

### Tab 03 — Independent Flow Review and authorized freeze
Entry in a fresh conversation:
- Re-verify Process 03 source and initiative identity.
- Verify Gate 1 and Gate 2 are APPROVED and recompute every artifact hash stored in both gates. Require `gate_1.approved_state_seq` to equal the latest `GATE_1_APPROVED` event sequence and `gate_1.decision_log_sha256` to equal that event's `decision_log_sha256` snapshot. Require the same sequence and hash-snapshot equality for Gate 2.
- Verify Decision Log identity/hash match `decision_log.latest_sha256` and `gate_2.decision_log_sha256`; require the latest `GATE_2_APPROVED` event's `decision_log_sha256` to equal `gate_2.decision_log_sha256` and `gate_2.approved_state_seq` to equal that event's `state_seq`. No `DECISION_LOG_UPDATED` event may follow Gate 2 approval. If any post-approval log update exists, reopen Gates 2–3 at minimum; if its verified scope is GATE_1, reopen Gates 1–3. Append canonical `INVALIDATED` and stop.
- If any other check fails, reopen affected gate(s), append an invalidation event, and stop.

Reviewer permissions:
- Read-only for artifacts 01–06, 09 and all Process 03 sources, including all Decision Log outcomes.
- May append to 07, create/update complete draft 08, and update the Control File only for review state, user-authorized risk acceptance, invalidation and explicit freeze.
- Must not edit 01–06, 09 or Process 03 sources. Tab 03 must never append a proposal or status event to 09.
- If a flow-policy outcome is requested during review, pause the affected decision, record it as unresolved in 07, identify the owning tab (Gate 1 → Tab 01; Gate 2/3 → Tab 02), and return it for user resolution. Run a fresh independent review after the owner tab updates the log and re-approves affected gates.
- Remediation returns to the owning tab. Changed artifacts invalidate affected gates and require re-approval plus a new independent review round.

Review:
- Review all artifacts in full, not only the draft or README.
- Build the complete freeze candidate `08_APP_FLOW_DRAFT.md` from the exact structure in `templates/04-APP-FLOW/08-APP-FLOW-DRAFT.md`. It must contain full detail from 01–06 and 09; it is not a summary.
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
4. Latest review records hashes matching current artifacts 01–06 and 09. Gate 1 and Gate 2 approval events exist; each `approved_state_seq` equals its event sequence, and each `gate_1.decision_log_sha256` / `gate_2.decision_log_sha256` equals the `decision_log_sha256` snapshot in its exact approval event. No Decision Log update follows Gate 2 approval; its hash equals both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`.
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

Then write APP_FLOW.md, compute its SHA-256, read it back and verify it differs from the draft only by the exact status-line replacement. Update Gate 3 = APPROVED and lifecycle_status = FROZEN; set `gate_3.approved_state_seq` and append `GATE_3_FROZEN` with `exact_user_command: FREEZE APP FLOW`, draft hash, canonical path/hash and version in that same Control File update. Event sequence, gate sequence and new committed `state_seq` must be identical. Read the Control File back and recompute the canonical hash. Report success only after all checks pass.

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
| 09_DECISION_LOG.md before Gate 2 approval | Reopen earliest independently verified affected gate and all downstream gates: GATE_1 → 1–3; GATE_2 → 2–3; GATE_3 → 3 |
| Any 09_DECISION_LOG.md byte change after Gate 2 approval | Always reopen Gates 2–3 because Gate 2 binds the whole file; additionally reopen Gate 1 when independent scope classification is GATE_1 |
| APP_FLOW.md after freeze | Gate 3 REOPENED; lifecycle REVIEW_REQUIRED; downstream use prohibited; every downstream reader must independently rehash before use |

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


---

# Owner-approved Schema v4 — Change Request Management Contract

> **Normative precedence:** This section implements P04 Remediation Plan v0.3.1 and the Repository Owner's approvals of ADR-P04-01…ADR-P04-10 and CL-01…CL-05 on 2026-11-12. For CR ownership, Register/Control data, migration, Gate/downstream eligibility, Freeze closure, and event protocols, this section supersedes earlier v2/v3-era wording in this Skill. It does not alter P03 or P04 functional task/flow scope.

## 1. Canonical ownership and data source

- `product/app-flow/10_CHANGE_REQUEST_REGISTER.md` is the **sole source of truth for CR business state**.
- `product/app-flow/00_APP_FLOW_CONTROL.md` schema v4 stores Control event sequence, receipts, integrity checkpoints, Gate state, and frozen-output binding only. It MUST NOT store per-CR status rows or an authoritative blocker count/list.
- Register template: `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md`; active artifact: `product/app-flow/10_CHANGE_REQUEST_REGISTER.md`. Template numbering is intentionally one greater than active artifact numbering.
- `state_seq` is a monotonic stale-read detector and committed event sequence, not an atomic lock, compare-and-swap, filesystem mutex, or distributed lock.
- Tab 01 is the CR Coordinator and sole Register writer. Tab 02 and Tab 03 are Register read-only. One logical Control File writer at a time is mandatory.
- P03 remains schema v2, read-only to P04. Never invent a P03 field such as `gate_3.approved_state_seq`.

## 2. Register v1 identity and canonical bytes

Register identity is immutable and binds Process 04 and the verified Initiative ID. Encoding is UTF-8 without BOM; line endings are LF only; CR bytes and trailing spaces/tabs are forbidden; field names/order are canonical; events are separated by exactly one blank line and terminate with `event_end_marker: END_CRE` plus LF. Readers reject noncanonical bytes and MUST NOT normalize before hashing.

Hashes use lowercase SHA-256 over exact on-disk bytes:
- `previous_register_sha256`: whole Register bytes immediately before event append.
- `event_block_sha256`: bytes from first byte of `### CRE-<NNNN>` through LF after `END_CRE`, excluding the following blank line.
- `resulting_register_sha256`: whole Register after append, including canonical separator.
- Verify the complete chain from the initialization anchor through the latest committed sequence; a matching final hash alone is insufficient.

Each event contains as applicable: unique CRE-ID and CR-ID; contiguous register_seq; event_type; from/to status; exact user command; TAB_01; real local timestamp; submission ID/payload hash; source process/initiative/path/hash; affected Gate and paths; pre-append Control state_seq/hash; previous Register hash; transition evidence; event-block hash; end marker. Register events MUST NOT contain a predicted Control sequence or resulting whole-file hash.

## 3. Initialization, including zero-CR workspaces

At new workspace initialization, verify P03 identity and frozen source using actual P03 v2 fields; ensure there is no conflicting Register; create header-only Register from template 11; compute `H_init`; append Control `CHANGE_REQUEST_REGISTER_INITIALIZED` with register_seq 0, last_event_id `INITIALIZATION`, path/schema/initiative and non-null H_init; read both files back. A v4 workspace with zero CRs still has register_seq 0 and a non-null verified hash. Empty 0-byte file, identity mismatch, unexpected CR event with null checkpoint, missing Register with existing pointer, or schema mismatch is NOT_VERIFIED; never overwrite/rebind.

## 4. Paired append-and-receipt transaction

### Normal commit unit

1. Read Control, Register and relevant artifacts from disk; verify every receipt and the full prefix hash-chain.
2. Verify one-writer condition, current CR state, exact legal transition, all current preconditions, source/artifact hashes and graph constraints.
3. Capture actual pre-append Control state_seq and whole-file hash.
4. Append exactly one canonical Register event at next register_seq; never include a planned Control sequence.
5. Read Register back and verify exact bytes, previous hash, event-block hash, resulting full-file hash and sequence continuity.
6. Append exactly one Control `CHANGE_REQUEST_REGISTER_UPDATED` receipt at the next **currently available** Control state_seq. It binds initiative, CR-ID, CRE-ID, register_seq, prior Register hash, event-block hash and resulting Register hash.
7. Read both files back; report success only after exact one-to-one match and full-chain verification.

A CR state transition is effective only after its Register event and exactly one matching Control receipt have both been committed and read back.

### Recovery of a staged normal event

If exactly one complete staged event has no receipt, stop other writes; verify its prefix equals the trusted checkpoint and sequence is next; re-read Control and verify pointer; re-evaluate current business preconditions against disk. If still valid, `RECOVER CHANGE REQUEST EVENT [CRE-ID]` writes only the missing receipt at the next available Control sequence. If now invalid, use bounded abort. Partial/malformed event, extra tail, duplicate/orphan receipt, changed prefix or hash mismatch is NOT_VERIFIED; preserve evidence and restore/reconcile from trusted backup. Never truncate append-only history.

### Abort pair — CL-01

The abort unit is exactly two consecutive Register events at k and k+1 plus one Control receipt:
- staged event k links to trusted checkpoint H(k-1);
- compute intermediate H(k) after staged event and separator; H(k) is an internal hash-chain link only and MUST NOT be published as a committed checkpoint;
- abort marker k+1 links to H(k);
- compute final H(k+1) after marker and separator;
- one `CHANGE_REQUEST_EVENT_ABORTED` receipt binds both IDs/sequences/event-block hashes and H(k-1), H(k), H(k+1), `status_effect: NONE`, and its Control state_seq;
- Control checkpoint advances directly from k-1/H(k-1) to k+1/H(k+1); `last_event_id` is abort-marker CRE-ID; no independently committed checkpoint exists at k;
- next normal event, if any, is k+2 and links from H(k+1).

The staged business event is retained and classified `ABORTED_NOT_EFFECTIVE`; marker is audit-only; neither changes CR business state. Neither event gets a normal Register-updated receipt.

`RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]` is allowed only if exactly two complete consecutive unreceipted events exist, the second is the exact marker for the first, both event-block hashes and all three hash edges verify, no later event/receipt exists, and Control still points to trusted prefix. It writes only the missing abort receipt; never appends a second marker. A partial/malformed abort marker means NOT_VERIFIED and trusted-backup restore; never append another marker. An exact two-event pair with missing receipt is `NOT_VERIFIED / ABORT_RECEIPT_PENDING`; only bounded recovery is allowed.

## 5. CR business states and legal transitions

The 13 business states are `RECORDED`, `TRIAGE`, `NEEDS_CLARIFICATION`, `ACCEPTED_FOR_IMPLEMENTATION`, `IMPLEMENTED_PENDING_REAPPROVAL`, `RETURN_TO_P03`, `REVERSION_PENDING`, `REJECTED_WITH_NO_CHANGE`, `CANCELLED_NO_CHANGE`, `CANCELLED_AFTER_REVERSION`, `CLOSED_IMPLEMENTED`, `DUPLICATE`, and `SUPERSEDED`. `NOT_VERIFIED` is an integrity condition and always blocks; it is not a business state. `REFROZEN` is prohibited.

Only T01–T18 are legal:

| ID | Transition | Exact command | Key precondition |
|---|---|---|---|
| T01 | Submission → RECORDED | `RECORD APP FLOW CHANGE SUBMISSION [SUBMISSION-ID]` | New immutable payload/hash; source, initiative and duplicate checks pass. |
| T02 | RECORDED → TRIAGE | `START APP FLOW CHANGE TRIAGE [CR-ID]` | Current state RECORDED; integrity VERIFIED. |
| T03 | TRIAGE → NEEDS_CLARIFICATION | `REQUEST CLARIFICATION FOR APP FLOW CHANGE [CR-ID]` | Concrete questions and artifact hashes recorded. |
| T04 | NEEDS_CLARIFICATION → TRIAGE | `RESUME APP FLOW CHANGE TRIAGE [CR-ID]` | User response recorded. |
| T05 | TRIAGE → ACCEPTED_FOR_IMPLEMENTATION | `ACCEPT APP FLOW CHANGE [CR-ID]` | P04 ownership; no unresolved conflict/cycle; scope/Gates/paths/pre-edit hashes captured. |
| T06 | TRIAGE → REJECTED_WITH_NO_CHANGE | `REJECT APP FLOW CHANGE NO CHANGE [CR-ID]` | User rationale and relevant bytes unchanged. |
| T07 | TRIAGE → RETURN_TO_P03 | `RETURN APP FLOW CHANGE TO P03 [CR-ID]` | P03-owned scope; per-CR P03 Control/frozen hash snapshot. |
| T08 | RETURN_TO_P03 → TRIAGE | `RESUME APP FLOW CHANGE AFTER P03 FREEZE [CR-ID]` | P03 v2 approved/frozen; new hash matches P03 Control and differs from this CR's return snapshot. |
| T09 | RETURN_TO_P03 → TRIAGE | `RESOLVE P03 RETURN WITHOUT UPSTREAM CHANGE [CR-ID]` | User rationale; P03 remains frozen at this CR's return snapshot. |
| T10 | ACCEPTED_FOR_IMPLEMENTATION → IMPLEMENTED_PENDING_REAPPROVAL | `RECORD APP FLOW CHANGE IMPLEMENTATION [CR-ID]` | Only accepted paths changed; required Gate 1/2 approvals are new and later than acceptance. |
| T11 | IMPLEMENTED_PENDING_REAPPROVAL → ACCEPTED_FOR_IMPLEMENTATION | `REOPEN APP FLOW CHANGE IMPLEMENTATION [CR-ID]` | Tab 03 blocker or Owner correction; evidence/Finding IDs. |
| T12 | IMPLEMENTED_PENDING_REAPPROVAL → CLOSED_IMPLEMENTED | `CLOSE IMPLEMENTED APP FLOW CHANGE [CR-ID]` | Valid Freeze event; CR belongs to batch; exact frozen tuple verified. |
| T13 | RECORDED/TRIAGE/NEEDS_CLARIFICATION → CANCELLED_NO_CHANGE | `CANCEL APP FLOW CHANGE [CR-ID]` | Pre-implementation; relevant bytes unchanged. |
| T14 | ACCEPTED_FOR_IMPLEMENTATION → CANCELLED_NO_CHANGE | `CANCEL APP FLOW CHANGE [CR-ID]` | Every relevant byte equals T05 snapshot; otherwise forbidden. |
| T15 | ACCEPTED_FOR_IMPLEMENTATION or IMPLEMENTED_PENDING_REAPPROVAL → REVERSION_PENDING | `START APP FLOW CHANGE REVERSION [CR-ID]` | User cancellation after byte change; baseline hashes recorded. |
| T16 | REVERSION_PENDING → CANCELLED_AFTER_REVERSION | `COMPLETE APP FLOW CHANGE REVERSION [CR-ID]` | Bytes restored and affected Gates reapproved; Gate 3 review/freeze rerun if touched. |
| T17 | RECORDED/TRIAGE/NEEDS_CLARIFICATION → DUPLICATE | `MARK APP FLOW CHANGE DUPLICATE [CR-ID] OF [CANONICAL-ID]` | Valid same-initiative target; no self/cycle; open blocker or exact closed-scope coverage. |
| T18 | Eligible pre-implementation CR → SUPERSEDED | `SUPERSEDE APP FLOW CHANGE [OLD-ID] WITH [NEW-ID]` | Valid open successor; no cycle; approved scope inheritance if bytes changed. |

**CL-04:** No `ACCEPTED_FOR_IMPLEMENTATION → TRIAGE` or `→ NEEDS_CLARIFICATION` edge exists. Do not add T19. If no bytes changed and accepted CR is cancelled, use T14 and submit a new linked CR. If bytes changed, use T15/T16. Never route around the closed transition table.

Every transition records actor TAB_01, exact user command, from/to, local timestamp, evidence, affected Gate/paths, pre-append Control seq/hash and Register prefix hash. Duplicate/supersession/dependency targets must exist, share initiative, be in an eligible state, prove coverage/scope inheritance and create no cycle. Missing target/cycle fails before append.

## 6. Blocking and Gate rules

Every reader reconstructs CR state from complete Register plus Control receipts; never trust cached counts/lists:
- NOT_VERIFIED or invalid/unreceipted chain: blocking TRUE.
- RECORDED, TRIAGE, NEEDS_CLARIFICATION, ACCEPTED_FOR_IMPLEMENTATION, IMPLEMENTED_PENDING_REAPPROVAL, RETURN_TO_P03, REVERSION_PENDING: TRUE.
- REJECTED_WITH_NO_CHANGE, CANCELLED_NO_CHANGE, CANCELLED_AFTER_REVERSION: FALSE.
- CLOSED_IMPLEMENTED: FALSE only if resolved frozen_version, Gate 3 freeze state_seq and APP_FLOW hash equal valid current GATE_3_FROZEN evidence; else TRUE.
- DUPLICATE/SUPERSEDED: recursively inherit target blocker; missing/invalid/cyclic/terminal target without valid transfer proof remains TRUE.

A new CR blocks downstream immediately at RECORDED but does not invalidate an approved Gate until relevant bound source/artifact bytes change. P03 source → Gates 1–3; artifacts 01/02 → Gates 1–3; 03–06 → Gates 2–3; 07/08 → Gate 3. Any Decision Log byte change after Gate 2 approval reopens Gates 2–3; also Gate 1 if scope is actually GATE_1. Register NOT_VERIFIED blocks every ordinary write, Gate approval, Freeze and downstream.

## 7. Freeze-to-closure and downstream eligibility

Tab 03 performs mechanical Freeze only after exact user command and review checks. At review, record P03 source; Control seq/hash; Register path/schema/full hash/last seq/last event; open/blocking CR IDs; implementation CR batch IDs; Decision Log hash; artifacts 01–06 and draft 08 hashes. Recheck the Register snapshot immediately before Freeze; any difference requires a new Review round.

Freeze Stage A — Tab 03 records GATE_3_FROZEN and freezes the exact reviewed draft by replacing only its status line. This does not close implementation CRs. Downstream remains blocked while any freeze-batch CR is IMPLEMENTED_PENDING_REAPPROVAL.

Freeze Stage B — Tab 01 verifies exact Freeze event/version/sequence/hash/Review snapshot, then writes an individual CR_CLOSED_IMPLEMENTED Register event and individual Control receipt for each batch CR. `CLOSE IMPLEMENTED APP FLOW CHANGES FOR FREEZE [FROZEN-VERSION]` expands to idempotent per-CR closures. Partial batch remains downstream-blocking; resume only uncommitted closures. Downstream is eligible only when all expected CRs are closed against the same frozen version, Gate 3 state_seq and APP_FLOW SHA-256 and reconstructed blocker set is empty.

First valid Freeze is version 1; each subsequent valid Freeze increments by exactly one. Archive the prior output as APP_FLOW.v<N>.md. Refuse no-op re-freeze when all source/artifact/Decision Log/Review hashes and CR state are unchanged and no accepted implementation awaits publication.

## 8. P03 boundary and v3→v4 migration

P03 remains schema v2 and read-only to P04. Each CR returned to P03 stores its own returned Control and frozen hashes. T08 compares the new actual P03 v2 frozen hash with that CR's own return snapshot and actual P03 Control. T09 resolves no-upstream-change only with user rationale and exact equality to that CR's return snapshot. Multiple CRs may resume against one new P03 freeze.

v3→v4 migration requires an exact user command: `MIGRATE APP FLOW CONTROL V3 TO V4 WITH ZERO EXTERNAL CRS` or `MIGRATE APP FLOW CONTROL V3 TO V4 WITH PENDING SUBMISSIONS`. Never infer that no unrecorded external CRs exist from old `change_requests: []`. Before modification create a byte-preserving full P04 workspace backup and `ARCHIVE_MANIFEST.md` with path, size, SHA-256, schema, initiative, source HEAD, timestamp and destination; verify every hash. Preserve v3 Gate approval only when its sequence and all bound artifact/Decision Log/Review/draft/frozen/P03 hashes verify; otherwise reopen conservatively.

Create Register header/H_init; construct a complete temporary v4 Control File containing sequential distinct `SCHEMA_MIGRATED` (3→4) and `CHANGE_REQUEST_REGISTER_INITIALIZED` (seq 0) events. Validate before one complete same-filesystem Control File replacement. Read both files back. If interrupted before replacement, keep v3 canonical; if ambiguous, verify both; if corrupt, restore full verified v3 archive and restart. Legacy v3 readers fail closed on v4. A historical v3 Freeze does not retroactively close a CR.

## 9. Three-tab permissions

- Tab 01: CR Coordinator, sole Register writer; validates source/hash/idempotency, assigns CR-ID, manages intake/triage/lifecycle and post-Freeze closure.
- Tab 02: performs assigned Gate 2 work; Register read-only; cannot independently change CR business state.
- Tab 03: independent review and mechanical Freeze; Register read-only; cannot write CR business status or close batch CRs.
- Handoff is persisted to disk; each tab is a fresh conversation and re-reads files. Chat memory is not evidence. One logical writer at a time.

## 10. Verification and fail-closed rules

All ST-01…ST-20 scenarios and targeted cases in `app-flow-kit/VERIFICATION-CHECKLIST.md` are mandatory static acceptance fixtures, not runtime passes. Live Windows Antigravity tests remain NOT RUN until actual evidence is recorded. Any untrusted bytes, incomplete pair, unexpected tail, broken chain, stale snapshot, graph cycle, mismatched ID, duplicate receipt or partial write is NOT_VERIFIED; preserve evidence and stop. Do not infer, auto-normalize, truncate or invent hashes/timestamps.
