# Tab 03 — Independent App Flow Review

Read the active Skill at .agents/skills/app-flow/SKILL.md in full.

Act as an adversarial Principal Product Designer, Information Architect and QA Flow Auditor. Your job is to find structural defects, not to defend the previous tabs.

## Entry verification
In a fresh conversation, verify Process 03 frozen source hash, Process 04 Gate 1 and Gate 2 approvals, and all hashes for artifacts 01–06. If any are missing or stale, stop and identify the affected gate.

## Permissions
Read-only for artifacts 01–06 and the Process 03 source. Do not edit them. Write findings only to 07_FLOW_REVIEW.md and the review portion of 08_APP_FLOW_DRAFT.md. Remediation belongs to the owning tab. Review rounds are append-only.

## Adversarial audit
Check:
- Product Definition capability coverage and forbidden scope expansion.
- Task-to-capability traceability and user-goal completeness.
- Entry/exit conditions, task completion and observable outcomes.
- Navigation consistency, back/cancel behavior and external entry.
- Reachability, dead ends, orphan screens, unreachable nodes and accidental loops.
- Branch conditions, validation, permissions, network/system failures and recovery.
- Empty/loading/error/success/interrupted states and relevant state transitions.
- Duplicate actions, repeated submissions, destructive actions and data-loss risks.
- Screen inventory vs flow graph vs state matrix consistency.
- Ambiguous labels or behavior that Process 05 could interpret in conflicting ways.
- Functional specification accidentally prescribing visual UI or implementation details.

For each finding include ID, severity (BLOCKER/CRITICAL/MAJOR/MINOR), exact artifact and IDs, evidence, scenario, user impact, minimal correction and confidence (VERIFIED/LIKELY/NEEDS TEST). Do not invent line numbers.

## Verdict
Return GO / CONDITIONAL GO / HOLD. BLOCKER or CRITICAL prevents freeze. MAJOR/MINOR must be fixed or explicitly accepted by the user with rationale in the Control File. Do not accept on the user's behalf.

Create:
- product/app-flow/07_FLOW_REVIEW.md
- product/app-flow/08_APP_FLOW_DRAFT.md

Do not modify artifacts 01–06 or freeze. Provide a remediation queue grouped by owning tab and state whether a new review round is required. Wait for explicit user direction.
