# Process 04 — Verification Checklist

This checklist distinguishes repository/paper checks from live runtime verification. A checked paper scenario is not proof that Antigravity executed it correctly.

## Repository and workspace setup
- [ ] Repository is at workspace root; `.agents/skills/app-flow/SKILL.md` is discoverable.
- [ ] All three prompts exist at their fully qualified paths under `prompts/04-APP-FLOW/`.
- [ ] Every prompt names the exact templates it must use.
- [ ] Control template exists and declares `schema_version: 4`.
- [ ] Register template `11-CHANGE-REQUEST-REGISTER.md` exists and maps to active artifact `10_CHANGE_REQUEST_REGISTER.md`.
- [ ] Control schema v4 has a `change_request_register` checkpoint and no `change_requests` business-status array.
- [ ] Decision Log template defines immutable proposal entries and canonical append-only status events with unique DLE IDs.
- [ ] Review template records pre-append Control File sequence/hash and previous review-history hash.
- [ ] Review-history initialization stores the exact template SHA-256 and a `REVIEW_HISTORY_INITIALIZED` event before Round 1.
- [ ] Process 03 source files are readable in the same workspace.
- [ ] Process 04 initiative ID equals Process 03 initiative ID.
- [ ] No prompt-name collision causes the wrong review prompt to be selected.

## Entry-gate simulations
| Scenario | Expected behavior |
|---|---|
| Process 03 Gate 3 not APPROVED | Stop; NOT_VERIFIED / ineligible |
| Process 03 lifecycle not FROZEN | Stop |
| Product Definition hash differs from Process 03 `gate_3.frozen_artifact.sha256` | Stop; do not initialize approval |
| Product Definition or Process 03 Control File missing/unreadable | Stop |
| Initiative IDs conflict | Stop; do not overwrite either initiative |
| Existing Decision Log has a missing/wrong Process 04 initiative identity | Stop; do not adopt it by computing a new baseline |
| Existing Control File uses schema version 2 | Stop; migrate only after exact `MIGRATE APP FLOW CONTROL V2 TO V3`; archive the entire old workspace with a verified per-file SHA-256 manifest, remove old frozen/review files from active paths, restore the tracked active `product/app-flow/README.md` from checked-out HEAD, and re-approve all gates |
| `SCHEMA_MIGRATED` event lacks exact archive directory/manifest/control/log fields | Migration NOT_VERIFIED; do not activate schema-v3 workspace |
| Process 03 frozen and hash matches | Eligible to initialize Process 04 |
| Process 04 source_status still NOT_VERIFIED | Gate 1 must refuse |
| Decision Log missing/unreadable or `decision_log.latest_sha256` is null | Gate 1 and Tab 02 refuse; NOT_VERIFIED |
| Actual Decision Log SHA-256 differs from `decision_log.latest_sha256` | Reopen Gates 1–3, invalidate review, record expected/observed hashes and stop |
| `DECISION_LOG_UPDATED` with `affected_gate: GATE_1` occurs after the latest Gate 1 approval | Reopen Gates 1–3 and return to Tab 01 |
| Decision Log approval/update events cannot be ordered by `state_seq` | NOT_VERIFIED; do not assume Gate 1 is current |
| Gate 1 status is APPROVED but no well-formed `GATE_1_APPROVED` event exists | NOT_VERIFIED; `gate_1.approved_state_seq` and `gate_1.decision_log_sha256` must equal the event sequence and hash snapshot |
| Gate 1 event exists but its Decision Log hash or approved artifact hashes differ | Reopen Gates 1–3; stop |
| Tab 03 sees Gate 1 sequence matches but `gate_1.decision_log_sha256` differs from the `GATE_1_APPROVED` event snapshot | Reopen Gates 1–3; freeze blocked |
| A decision affecting 01/02 or capability-to-task mapping is labeled GATE_2/GATE_3 | NOT_VERIFIED; classify by semantic scope, do not trust the label |

## Template and capability coverage simulations
| Scenario | Expected behavior |
|---|---|
| Agent writes prose-only task model without template tables | Gate 1 refuses |
| Required template heading/column is missing or blank | Gate refuses; report exact missing section |
| One approved capability has no task | Gate 1 refuses unless user-approved deferral exists |
| A task has no approved capability | Gate 1 refuses and flags scope mismatch |
| Deferred capability has no approved Decision ID | Gate 1 refuses |
| Decision is only PROPOSED | It is not treated as approved product/flow policy |
| Proposal has no unique DLE Proposal Event ID or no matching `DECISION_LOG_UPDATED` Control File event | Decision is LEGACY_UNVERIFIED / NOT_VERIFIED; do not treat it as active policy |
| A status event has no matching Control File event with the same DLE ID, DEC ID, kind, before/after status, scope and resulting hash | Decision is NOT_VERIFIED; do not treat it as approved |
| Status event chain has a duplicate DLE ID, wrong previous status or wrong superseded-event ID | Decision is NOT_VERIFIED; stop and reconcile |
| Status event exact command does not map to its resulting status or rationale is missing | Reject the status update; no policy change |
| Legacy inline `Status: APPROVED` exists without a canonical matched status event | LEGACY_UNVERIFIED; preserve bytes and require a new canonical decision if still needed |

## Gate and invalidation simulations
| Scenario | Expected behavior |
|---|---|
| Gate 1 absent | Tab 02 and Tab 03 blocked |
| Decision Log hash is correct and no later GATE_1 update exists | Tab 02 may pass the Decision Log entry check |
| Decision Log changes with affected_gate GATE_1 after Gate 1 approval | Gates 1–3 reopened; Tab 02 stops |
| Decision Log changes with affected_gate GATE_2 after Gate 1 approval but before Gate 2 approval | Gates 2–3 reopened; Gate 1 may remain valid only after scope validation |
| Any Decision Log byte change after Gate 2 approval, including a GATE_3-labeled change | Gates 2–3 reopened because Gate 2 binds the whole file; also Gate 1 if scope is actually GATE_1 |
| Gate 2 status is APPROVED but no well-formed `GATE_2_APPROVED` event exists | NOT_VERIFIED; `gate_2.approved_state_seq` and `decision_log_sha256` must match the event |
| Gate 2 event snapshot differs from `gate_2.decision_log_sha256` or the current Decision Log SHA-256 | Reopen Gates 2–3; stop |
| Tab 03 is asked to approve/reject/defer a flow decision | It must not edit 09; hand the decision back to Tab 01/02 |
| Decision Log actual hash matches `resulting_sha256` in one valid persisted update event but baseline refresh failed | Recovery only after exact `RECOVER DECISION LOG [DECISION-ID]`; record `DECISION_LOG_RECOVERED` and reopen affected gates |
| Decision Log append succeeded but Control File update is ambiguous; a matching valid update event is already persisted | Stop all writers; do not repeat the append; require exact recovery command and bounded recovery procedure |
| Decision Log append succeeded but no matching valid update event is persisted | Do not adopt observed bytes; restore trusted bytes matching old baseline or remain NOT_VERIFIED |
| Control File event history is partial, malformed or unreadable during recovery | Restore a trusted Control File copy or stop for human-led reconciliation; never synthesize events |
| `affected_gate` conflicts with decision semantics or affected artifact IDs, or scope is ambiguous | NOT_VERIFIED; independently classify and reopen earliest affected gate plus downstream gates |
| Tab 03 receives an approve/reject/defer decision command during review | Tab 03 remains read-only on 09; record unresolved review item and route outcome to owning Tab 01/02 |
| Decision Log hash mismatch has no matching persisted update event | Do not adopt observed bytes; restore trusted bytes matching old baseline or remain NOT_VERIFIED |
| Proposal/status DLE ID is paired with more than one Control File event | NOT_VERIFIED; stop; IDs must pair one-to-one |
| Current decision status is reconstructed from valid paired events | Highest committed `state_seq` event determines status; without a status event the proposal remains PROPOSED |
| Gate 1 artifact hash changed | Gate 1 and downstream gates REOPENED |
| Gate 2 absent | Tab 03 and freeze blocked |
| Tab 02 artifact hash changed after Gate 2 | Gate 2/3 and review invalidated |
| Process 03 Product Definition changes | Source REOPENED; Gates 1–3 reopened |
| User says "looks good" without exact approval command | No gate approval |
| Hash/read-back fails | INCOMPLETE / NOT_VERIFIED; no success claim |
| state_seq stale | Stop, reload and reconcile; no concurrent write |
| Two tabs may have written concurrently | Stop all writers; `state_seq` is not a lock/CAS and cannot prove no event was lost; reconcile against trusted persisted state |
| Change request without exact user decision | Log request; do not infer approval |

## Review-history and freeze simulations
| Scenario | Expected behavior |
|---|---|
| No review file or review_round = 0 | Freeze refuses |
| Review history is absent before Round 1 | Initialize from the exact review template, read back/hash it, store `review.latest_review_sha256` and append `REVIEW_HISTORY_INITIALIZED` before adding Round 1 |
| Review history exists but baseline is null and bytes exactly equal the template with no round/addendum | It may be initialized through the same verified baseline transaction |
| Review history exists with null baseline but contains any non-template round/addendum/content | NOT_VERIFIED; do not adopt an untrusted history |
| Review round 1 exists, then round 2 is appended | Round 1 remains byte-for-byte intact |
| Review append succeeds but Control File update fails; exact pre-append Control File SHA-256, state_seq, round number and previous review hash still match, and exactly one complete new round is appended | Recover only after exact `RECOVER REVIEW ROUND [N]`; register existing round with `REVIEW_ROUND_RECOVERED`; do not append again |
| Review append exists but prefix hash does not reproduce the previously trusted review hash | NOT_VERIFIED; no automatic recovery |
| Control File state_seq changed, round number changed, or a review event for N already exists | Stop; no recovery or duplicate event; human-led reconciliation |
| Review round is partial, duplicated, or current source/artifact/draft hashes differ | NOT_VERIFIED; preserve review history and require reconciliation/new review |
| Review file hash differs from Control File | Freeze refuses |
| Draft 08 changes after review | Freeze refuses; new review round required |
| Latest review status BLOCKERS_FOUND | Freeze refuses |
| Unresolved BLOCKER or CRITICAL | Freeze refuses; cannot accept |
| Open MAJOR/MINOR | Freeze refuses until fixed or individually accepted |
| User says "accept all" without exact finding command and rationale | No residual-risk acceptance |
| User accepts one MAJOR/MINOR with exact command and rationale | One structured acceptance record and appended review addendum |
| Freeze before independent review | Freeze refuses |
| GO verdict without explicit freeze command | No freeze |
| Draft 08 contains a summary, not full canonical sections | Freeze refuses |
| APP_FLOW.md differs from draft beyond exact status line | Freeze refuses |
| APP_FLOW.md has no matching Control File Gate 3 record | Orphan; downstream use prohibited |
| Canonical write succeeds but Control File write/read-back fails | INCOMPLETE — NOT FROZEN |
| Re-freeze requested | Verify and archive prior version as APP_FLOW.v<N>.md before replacement |
| Existing archive contains different bytes | Stop; never overwrite archive |
| Frozen APP_FLOW.md is modified | At the next Process 04 tab entry or downstream read, Gate 3 REOPENED; lifecycle REVIEW_REQUIRED; expected hash retained; downstream use blocked |
| Frozen APP_FLOW.md is modified but no tab/downstream consumer has read it yet | No background watcher exists; immediate detection is not claimed |
| Freeze event missing or `gate_3.approved_state_seq` differs from its event sequence | NOT_VERIFIED; frozen output is not eligible downstream |
| ABANDON APP FLOW command | Lifecycle ABANDONED; terminal for that initiative |

## Structural integrity tests
- [ ] Every approved capability maps to task(s) or a user-approved deferral.
- [ ] Every task maps to approved capability ID(s).
- [ ] Every task appears in task-to-flow mapping.
- [ ] All flow/node/screen/transition IDs are unique.
- [ ] Screen IDs in 04 equal screen references in navigation nodes, except justified exclusions.
- [ ] Every transition source/destination references a valid node or declared external/terminal endpoint.
- [ ] Every flow has an entry and observable completion/terminal condition.
- [ ] Explicit reachability traversal is recorded; no unexplained unreachable node, orphan screen or dead end.
- [ ] State matrix agrees with flow specification and screen inventory.
- [ ] Every excluded state has a rationale.
- [ ] No capability expansion or visual/technical design leakage.
- [ ] All material decisions are approved or unresolved questions.

## Live Antigravity test record
Run in the actual Windows workspace. Do not mark these passed based only on repository inspection. All rows intentionally remain `NOT RUN` until actual runtime evidence is supplied; repository/document edits do not change these results.

| Test | Result (PASS/FAIL/NOT RUN) | Evidence path | Notes |
|---|---|---|---|
| Skill discovery and explicit invocation | NOT RUN | | |
| Tab 01 rejects Process 03 Gate 3 PENDING | NOT RUN | | |
| Tab 01 writes 01–02 using templates | NOT RUN | | |
| Capability reverse-coverage failure is caught | NOT RUN | | |
| Exact Gate 1 command and read-back | NOT RUN | | |
| Fresh Tab 02 reconstructs Gate 1 from files | NOT RUN | | |
| Tab 02 writes 03–06 with template conformance | NOT RUN | | |
| Orphan screen / invalid transition is detected | NOT RUN | | |
| Exact Gate 2 command and read-back | NOT RUN | | |
| Fresh Tab 03 reconstructs all state | NOT RUN | | |
| Review round 2 preserves round 1 | NOT RUN | | |
| Freeze without a review refuses | NOT RUN | | |
| Freeze with open MAJOR finding refuses | NOT RUN | | |
| Explicit risk acceptance persists and is appended | NOT RUN | | |
| Draft 08 → APP_FLOW.md differs only by status line | NOT RUN | | |
| Canonical/control partial-write failure reports INCOMPLETE | NOT RUN | | |
| Re-freeze archives prior version | NOT RUN | | |
| Modified frozen artifact reopens Gate 3 | NOT RUN | | |

## Release decision
Do not label Process 04 production-ready until all mandatory live tests have evidence. Record limitations and unresolved defects in independent review. Repository inspection is not live Antigravity verification.

## Schema v4 static stress tests — ST-01 to ST-22

These 22 scenarios are mandatory static/simulation fixtures. Marking a row reviewed on paper does not prove runtime behavior; every result remains NOT RUN until evidence is captured.

| Test | Scenario | Required expected result | Result |
|---|---|---|---|
| ST-01 | Initialize Register with null Control pointer | Create header-only Register; commit `CHANGE_REQUEST_REGISTER_INITIALIZED`; `register_seq: 0`; non-null init hash. | NOT RUN |
| ST-02 | Register exists with wrong Initiative ID | `NOT_VERIFIED`; do not rewrite identity or accept its hash as baseline. | NOT RUN |
| ST-03 | One complete staged tail without receipt | Block all writes; recover only after validating trusted prefix and re-evaluating current business preconditions. | NOT RUN |
| ST-04 | Receipt has wrong `event_block_sha256` | `NOT_VERIFIED`; no automatic receipt correction. | NOT RUN |
| ST-05 | Duplicate Control receipts for one Register event | `NOT_VERIFIED`; restore/reconcile from trusted Control state. | NOT RUN |
| ST-06 | `register_seq` gap | `NOT_VERIFIED`; restore trusted Register/Control pair. | NOT RUN |
| ST-07 | Control `state_seq` gap | `NOT_VERIFIED`; never invent a missing event. | NOT RUN |
| ST-08 | More than one unreceipted Register tail event | Reject normal recovery; allow only the exact two-event staged+abort pair through `RECOVER CHANGE REQUEST ABORT [STAGED-CRE-ID]`; otherwise restore to last trusted hash. | NOT RUN |
| ST-09 | Tab 01 uses stale chat state after Tab 02 Gate 2 approval | Tab 01 rereads disk and uses the current Gate receipt/sequence; stale chat memory ignored. | NOT RUN |
| ST-10 | Tab 02 edits Gate 2 while Gate 1 is reopened | Stop at Tab 02 entry gate; no Gate 2 edits. | NOT RUN |
| ST-11 | Register changes after Tab 03 Review snapshot | Freeze refused; new Review round required. | NOT RUN |
| ST-12 | Freeze succeeds but CR closure receipt fails | Downstream stays blocked; recover the single valid staged close or abort path; do not report eligibility. | NOT RUN |
| ST-13 | Two CRs return to P03 and resume against one new P03 freeze | Each CR compares against its own `returned_p03_frozen_sha256`; both may resume independently. | NOT RUN |
| ST-14 | Supersede target missing or terminal-invalid | Reject before append; original CR remains blocking. | NOT RUN |
| ST-15 | User cancels after a partial artifact edit | Reject T14; require T15 reversion and T16 after Gate restoration. | NOT RUN |
| ST-16 | Reversion bytes restored but required Gate approval missing | Reject T16; remain `REVERSION_PENDING`. | NOT RUN |
| ST-17 | New evidence arrives after terminal rejection | Preserve old CR; create a new linked submission/CR. | NOT RUN |
| ST-18 | v3→v4 migration interrupted | Restore/verify full v3 archive or verify completed v4 pair; never claim partial success. | NOT RUN |
| ST-19 | Legacy v3 reader reads v4 Control File | Fail closed with unsupported schema; no writes. | NOT RUN |
| ST-20 | New CR appears after prior CR closed in v1 | Old CR remains bound to v1; new CR blocks downstream until resolved for a later version. | NOT RUN |
| ST-21 | Stored `event_block_sha256` is the literal sentinel `<HASH_OMITTED>` | `NOT_VERIFIED`. The sentinel is a hashing placeholder only; it must never be persisted as a digest. | NOT RUN |
| ST-22 | Reader recomputes the event-block hash with the stored digest left in place | Hash mismatch. The reader must substitute `<HASH_OMITTED>` before recomputing; a digest computed over its own value is a protocol violation, not a tolerable variant. | NOT RUN |

## Additional targeted tests

| Test | Scenario / required assertion | Result |
|---|---|---|
| AT-01 | A staged event's previously expected Control sequence is consumed by an unrelated event; recovery re-evaluates current preconditions and uses the next available sequence. | NOT RUN |
| AT-02 | Abort hash edges are exactly H(k-1) → H(k) → H(k+1); one receipt covers both events and all hashes. | NOT RUN |
| AT-03 | Complete abort pair with missing receipt; recovery writes only the receipt and never a second marker. | NOT RUN |
| AT-04 | Partial/malformed abort marker is NOT_VERIFIED; do not append a retry marker; restore trusted backup only. | NOT RUN |
| AT-05 | Canonical UTF-8 without BOM, LF-only, no CR/trailing whitespace, exact-byte hashes. | NOT RUN |
| AT-06 | Prefix-chain tampering at any historical event is detected from the initialization anchor. | NOT RUN |
| AT-07 | Cycles/missing/invalid targets across DUPLICATE/SUPERSEDED/dependency graph are rejected before append. | NOT RUN |
| AT-08 | No-op re-freeze is refused; valid frozen version increments exactly by one. | NOT RUN |
| AT-09 | Mixed Gate 1 + Gate 2 CR uses ordered tab approvals and persisted disk handoff. | NOT RUN |
| AT-10 | Partial multi-CR closure batch remains downstream-blocking and resumes idempotently. | NOT RUN |

## Schema v4 repository assertions

- [ ] No exact `decision_event_kind: STATUS_CHANGED` remains in affected P04 Skill/templates.
- [ ] No accidental `DECISION_DECISION_STATUS_CHANGED` exists.
- [ ] Control template declares `schema_version: 4` and has no `change_requests: []`.
- [ ] Register template declares schema v1 and canonical byte/hash rules.
- [ ] The canonical state-machine contract contains exactly the approved 13 business states and T01–T18; `NOT_VERIFIED` is integrity-only; `REFROZEN` and T19 are absent.
- [ ] CL-04 restriction is explicit: no `ACCEPTED_FOR_IMPLEMENTATION → TRIAGE/NEEDS_CLARIFICATION` edge.
- [ ] Tab 01 is sole Register writer; Tabs 02/03 are read-only for CR business state.
- [ ] Freeze Stage A and CR-closure Stage B are separate; partial batch stays downstream-blocking.
- [ ] Migration is v3→v4 with a verified backup/manifest, explicit attestation and one complete Control File replacement containing sequential migration and Register-initialization events.
- [ ] P03 files remain untouched and P03 remains schema v2.
- [ ] All three prompts reference the canonical Skill and enforce their tab-specific Register permissions.
- [ ] README artifact mapping shows template 11 → active artifact 10.
- [ ] No live test is marked PASS without actual Windows Antigravity evidence.

## Live runtime evidence register

All six minimum end-to-end flows, v3→v4 migration and the deliberately invalid recovery case remain NOT RUN until executed in the actual Windows Antigravity workspace with logs, file/hash snapshots and screenshots as evidence. Repository inspection is not runtime verification.
