# Tab 03 — Independent App Flow Review and Authorized Freeze

Read the active Skill at `.agents/skills/app-flow/SKILL.md` in full. The Skill is the governing process contract.

Act as an adversarial Principal Product Designer, Information Architect and QA Flow Auditor. Find structural defects; do not defend previous tabs or optimize for a GO verdict.

## Entry verification
In a fresh conversation, independently re-read Process 03 Control File and Product Definition, Process 04 Control File, artifacts 01–06 and Decision Log 09. Recompute the Product Definition SHA-256 and compare it with Process 03 `gate_3.frozen_artifact.sha256`. Recompute all approved-artifact hashes and verify initiative IDs, including the immutable Process 04 Decision Log identity header. Require `gate_1.approved_state_seq` to equal the latest `GATE_1_APPROVED` event sequence and `gate_1.decision_log_sha256` to equal that event's `decision_log_sha256` snapshot. Require `gate_2.approved_state_seq` and `gate_2.decision_log_sha256` to equal the corresponding `GATE_2_APPROVED` event sequence and hash snapshot. Require the current Decision Log SHA-256 to match both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`, and require no `DECISION_LOG_UPDATED` event after Gate 2 approval. If the Control File lifecycle is FROZEN or a frozen artifact hash exists, also recompute `product/app-flow/APP_FLOW.md` and compare it with `gate_3.frozen_artifact.sha256`. A missing, unreadable or mismatched frozen file reopens Gate 3, sets lifecycle REVIEW_REQUIRED, appends `INVALIDATED`, blocks downstream use and stops. If anything else is missing, stale, unreadable or contradictory, reopen affected gate(s), append a canonical invalidation event, report NOT_VERIFIED and stop.

## Permissions
- Read-only for Process 03 sources and Process 04 artifacts 01–06 and 09.
- May append review rounds/addenda to 07, create/update complete draft 08, and update the Control File only for review metadata, user-authorized residual-risk acceptance, invalidation and explicit freeze. Tab 03 is read-only on Decision Log 09.
- Must not edit 01–06, 09 or Process 03 sources, including when the user gives a decision outcome during review.
- Remediation belongs to Tab 01 or Tab 02. Changed artifacts invalidate affected gate(s), require re-approval and a new review round.

## Step 1 — Build the complete freeze candidate
Use `templates/04-APP-FLOW/08-APP-FLOW-DRAFT.md` as the exact structure for `product/app-flow/08_APP_FLOW_DRAFT.md`. The draft is the complete canonical output candidate, not a summary. Populate every section with full content from 01–06 and approved decisions from 09. Do not invent or silently resolve decisions.

Its first lines must be exactly:
```markdown
# APP FLOW — Process 04 Output
> Status: REVIEWED CANDIDATE — NOT FROZEN
```
The candidate contains no self-referential App Flow hash and no freeze timestamp; those are stored in the Control File.

## Step 2 — Independent adversarial audit
Audit all source artifacts and the complete draft. Check:
- Full bidirectional approved-capability coverage, including user-approved deferrals.
- Task-to-capability and task-to-flow traceability.
- Entry/exit conditions, task completion and observable outcomes.
- Navigation consistency, back/cancel behavior and external entry.
- Reachability, dead ends, orphan screens/nodes/transitions, unreachable nodes and accidental loops.
- Branch conditions, validation, permissions, network/system failures and recovery.
- Empty/loading/error/success/interrupted states and relevant transitions.
- Duplicate actions, repeated submissions, destructive actions and data-loss risks.
- Screen inventory vs navigation graph vs flow specification vs state matrix.
- Ambiguous behavior that a later design process could interpret inconsistently.
- Functional specification accidentally prescribing visual UI or implementation.
- Every material decision is approved, rejected or explicitly unresolved.

Perform explicit set comparisons and graph traversals. Include compared ID sets, set differences and reachable/unreachable node sets. Do not claim a check passed without evidence.

For each finding include stable ID, severity BLOCKER/CRITICAL/MAJOR/MINOR, exact artifact and affected IDs, precise evidence, concrete scenario and impact, minimal correction, confidence VERIFIED/LIKELY/NEEDS TEST, and status OPEN/RESOLVED/ACCEPTED_BY_USER.

Severity:
- BLOCKER: core task cannot be completed or fundamental contract is broken.
- CRITICAL: severe flow-integrity, permission or data-loss barrier making freeze unacceptable.
- MAJOR: material incomplete or contradictory behavior.
- MINOR: bounded ambiguity or low-impact omission.

## Step 3 — Append the review round
Append a new `### Review round <N>` to `product/app-flow/07_FLOW_REVIEW.md`; never overwrite or delete prior rounds. Use `templates/04-APP-FLOW/07-FLOW-REVIEW.md`.

Record Process 03 source hash, initiative IDs, hashes of artifacts 01–06, decision log 09, draft 08, reviewer, timestamp, explicit set/graph evidence, findings, severity counts, verdict GO/CONDITIONAL GO/HOLD and status BLOCKERS_FOUND/READY_FOR_FREEZE.

Before appending Round N, verify `review.round = N-1` and the actual current `07_FLOW_REVIEW.md` SHA-256 equals the previously trusted `review.latest_review_sha256`. Record the Control File `state_seq` before append and the previous full review-history SHA-256 inside Round N. Append exactly one complete round, read it back and compute the resulting full-file SHA-256. Then, in one single-writer Control File update, store round N, open counts, latest review path/hash, reviewed source/artifact hashes and reviewed draft path/hash, and append `REVIEW_ROUND_RECORDED` with round number, review path, previous/resulting review hashes, draft path/hash, verdict and review status. Read the Control File back and verify the new committed sequence, event and all metadata. Do not claim a round is registered before read-back succeeds.

If the review file append succeeds but the Control File update fails or is ambiguous, stop all writers and do not append Round N again. Use only the bounded Skill procedure. The user may send exactly `RECOVER REVIEW ROUND N` only when the Control File is still readable at the recorded pre-append state_seq with round N-1 and the old trusted review hash; exactly one complete Round N is appended; hashing the byte prefix before Round N reproduces that old hash; no recovery/recorded event for N exists; and all source/artifact/draft hashes in Round N still match current files. Then update Control File metadata and append `REVIEW_ROUND_RECOVERED` without editing 07. Otherwise remain NOT_VERIFIED and require human-led reconciliation. Never duplicate, overwrite or silently bless an orphan round.

Set READY_FOR_FREEZE only when every finding is RESOLVED or explicitly ACCEPTED_BY_USER under the rules below; otherwise BLOCKERS_FOUND.

## Step 4 — Remediation, user decisions and residual-risk acceptance

When a proposed flow-policy decision needs an outcome, do not append to or otherwise edit `09_DECISION_LOG.md`. Record the item as unresolved in the review round, identify the owning tab (Gate 1 → Tab 01; Gate 2/3 → Tab 02), and stop the affected review decision. The user resolves it in that owning tab with exactly one command and rationale: `APPROVE FLOW DECISION [DECISION-ID]`, `REJECT FLOW DECISION [DECISION-ID]`, or `DEFER FLOW DECISION [DECISION-ID]`. The owning tab performs the append/read-back/hash/Control File event transaction. Only APPROVED decisions may define current flow policy. A DEFERRED capability requires an explicit affected CAP ID and scope rationale. After the owner tab updates and re-approves affected gates, run a fresh independent review.


- BLOCKER/CRITICAL must be fixed; they cannot be accepted.
- MAJOR/MINOR must be fixed or accepted individually by the user.
- To accept one MAJOR/MINOR finding, the user must send exactly `ACCEPT RESIDUAL RISK [FINDING-ID]` and provide a rationale in the same message.
- Persist the six-field record in the Control File: finding_id, severity, accepted_by=user, exact_command, rationale, accepted_at_local.
- Append a dated user-decision addendum to 07 and update the Control File's latest review hash/status/counts. Never rewrite the historical finding row.
- If an artifact changes, the owning tab remediates it; recompute hashes, reopen affected gate(s), require re-approval and run a new full review round.

## Step 5 — Wait for a separate freeze command
After review, report verdict, findings and remediation queue grouped by owning tab. **Do not freeze automatically.** Wait for the exact user command `FREEZE APP FLOW`. GO/CONDITIONAL GO, praise, "continue" or risk acceptance does not itself authorize freeze.

## Step 6 — Freeze only after the exact command
When—and only when—the user sends `FREEZE APP FLOW`, execute the complete Freeze protocol in the active Skill. Re-read the Control File and all required files; do not rely on conversation memory.

Preconditions:
- Source status VERIFIED; Product Definition hash equals Process 03 `gate_3.frozen_artifact.sha256`.
- Gates 1 and 2 APPROVED and every stored hash matches; latest canonical approval events and `approved_state_seq` fields agree. Gate 1's `decision_log_sha256` equals its `GATE_1_APPROVED` event snapshot; Gate 2's `decision_log_sha256` equals its `GATE_2_APPROVED` event snapshot.
- No Decision Log update follows Gate 2 approval; its identity is correct and actual SHA-256 equals both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`.
- If a previously frozen `APP_FLOW.md` exists, its actual SHA-256 equals `gate_3.frozen_artifact.sha256`; otherwise Gate 3 is reopened and freeze is blocked.
- At least one review round exists; latest review file hash matches the Control File.
- Latest review status READY_FOR_FREEZE.
- Latest round's 01–06, decision-log and draft hashes match current files.
- Draft hash matches the latest review and Control File.
- Open BLOCKER, CRITICAL, MAJOR and MINOR counts are all zero.
- Accepted risks have user-originated commands, rationales and review addenda.
- Candidate version equals previous frozen_version + 1.

Copy 08 to `APP_FLOW.md`, replacing only this exact line:
`> Status: REVIEWED CANDIDATE — NOT FROZEN`
with:
`> Status: FROZEN`

Do not rebuild, summarize, edit, add a self-hash or insert a timestamp. Verify final bytes differ from the reviewed candidate only by that one line.

For re-freeze, first verify and archive the prior canonical artifact as `APP_FLOW.v<N>.md`; never overwrite an existing archive. Then write, hash and read back the new canonical output, update Gate 3/lifecycle/version/archive metadata, set `gate_3.approved_state_seq` to the new committed sequence, and append `GATE_3_FROZEN` with `exact_user_command: FREEZE APP FLOW`, draft hash, canonical path/hash and version in that same Control File update. Event sequence, gate sequence and committed `state_seq` must match. Read the Control File back and verify every hash. If any step fails, report INCOMPLETE — NOT FROZEN. A canonical file without a matching approved Control File is an orphan and is not eligible downstream.

## Strict read-only restriction
This is an independent review, not an implementation task. Do not modify 01–06, 09 or Process 03. Do not silently remediate findings or append decision outcomes. The only allowed writes are review history, the complete draft candidate and documented Control File state transitions after required exact user commands. If a decision is needed, hand it back to Tab 01/02; never bypass this ownership rule.
