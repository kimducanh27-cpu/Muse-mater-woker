---
name: app-flow
description: Run Process 04 App Flow from a frozen Product Definition. Model user tasks, navigation, screen inventory, states, transitions and exceptions. Do not design visual UI or technical architecture.
---

# App Flow — Process 04

## Mission
Translate an approved Process 03 Product Definition into a complete, testable model of how users accomplish the product's promised outcomes through the application.

Process 03 defines WHAT and WHY. Process 04 defines the user-facing STRUCTURE and SEQUENCE: actors, entry points, tasks, decisions, navigation, screens as functional nodes, states, transitions, recovery and completion. Process 05 owns UX/UI and visual design.

## Hard boundaries
Do not create wireframes, visual layouts, colors, typography, components, design systems, polished UI mockups, interaction microcopy, animations, API/database architecture, implementation plans, tickets or code. Screen descriptions are functional contracts only, not visual specifications. Do not add capabilities absent from the frozen Product Definition.

## Required input and eligibility
Canonical Process 03 files:
- product/definition/00_PRODUCT_DEFINITION_CONTROL.md
- product/definition/PRODUCT_DEFINITION.md

Require Gate 3 = APPROVED, lifecycle_status = FROZEN, and matching SHA-256 for PRODUCT_DEFINITION.md. Read the source Control File and verify initiative_id, output path, source hash, and any handoff constraints. If control state or hash cannot be verified, stop with NOT_VERIFIED. Never infer approval from chat.

Process 04 must preserve the approved capability IDs, IN/NOT NOW/OUT boundaries, target segment, customer outcomes, constraints, risks and non-goals. A missing flow requirement is not permission to invent a capability. Record gaps as OPEN QUESTIONS or CHANGE REQUESTS and seek user direction.

## Canonical state
Canonical state: product/app-flow/00_APP_FLOW_CONTROL.md
Template: templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md
Frozen output: product/app-flow/APP_FLOW.md

Use SHA-256 for source and approved artifacts. Use real Asia/Ho_Chi_Minh timestamps. On Windows, use PowerShell Get-FileHash -Algorithm SHA256 and TimeZoneInfo. Never invent hashes or timestamps. If terminal/hash/read-back is unavailable, mark NOT_VERIFIED and block the affected gate.

Every gate update is single-writer:
1. Read Control File and state_seq.
2. Verify prerequisite artifact hashes.
3. Save exact command, user decision, timestamp, artifact paths and hashes.
4. Increment state_seq.
5. Read back and verify.
state_seq detects stale reads; it is not a lock or atomic transaction. Never have multiple tabs write Control File concurrently.

Exact commands:
- Gate 1: APPROVE TASK MODEL
- Gate 2: APPROVE APP FLOW
- Gate 3 / freeze: FREEZE APP FLOW
- Reject: REJECT TASK MODEL / REJECT APP FLOW
- Change request: REQUEST APP FLOW CHANGE [description]

No automatic handoff. Each tab runs in a fresh conversation in the same workspace and reads the artifacts, not chat history.

## Three-tab workflow

### Tab 01 — User Tasks & Flow Architecture
Entry: verify Process 03 freeze and hash; initialize or verify Process 04 Control File; verify initiative identity and source constraints.
Work:
- Extract target actors/roles only when supported by Product Definition.
- Map user goals to approved capability IDs and customer outcomes.
- Identify entry points, triggers, preconditions, user tasks, decision points, success criteria and failure/recovery needs.
- Build task inventory and task-to-capability traceability.
- Identify missing requirements and contradictions without inventing solutions.
Artifacts: 01_TASK_MODEL.md and 02_FLOW_ARCHITECTURE.md.
Gate 1 requires APPROVE TASK MODEL. No Tab 02 before approval.

### Tab 02 — Navigation & Screen Flow Specification
Entry: fresh conversation; re-verify Process 03 source hash, Gate 1 approval, and hashes of Tab 01 artifacts.
Work:
- Define navigation model and flow graph with stable IDs.
- Specify screens as functional nodes: purpose, entry conditions, information/actions required, exits and destinations.
- Define transitions, branching conditions, back/cancel behavior, deep-link or external-entry behavior only if supported.
- Specify screen/system states: loading, empty, error, success, permission-denied, offline, interrupted, and retry/recovery where applicable.
- Cover alternate paths, validation failures, destructive-action confirmation, duplicate submission and session interruption where relevant.
- Map every flow node and transition to capability IDs and source requirements.
- Mark assumptions and unresolved questions; do not silently decide product policy.
Artifacts: 03_NAVIGATION_MODEL.md, 04_SCREEN_INVENTORY.md, 05_FLOW_SPECIFICATION.md, 06_STATE_AND_EXCEPTION_MATRIX.md.
Gate 2 requires APPROVE APP FLOW. No Tab 03 before approval.

### Tab 03 — Independent Flow Review
Entry: fresh conversation; re-verify source and all prior gate hashes.
Reviewer is read-only on artifacts 01–06. Check traceability, dead ends, unreachable nodes, orphan screens, missing exits, inconsistent back behavior, uncovered states, unhandled errors, scope creep, ambiguous conditions and accessibility-critical task barriers. Record findings with severity, evidence, affected IDs, consequence and minimal correction. Do not silently edit source artifacts.
Artifacts: 07_FLOW_REVIEW.md and 08_APP_FLOW_DRAFT.md.
Remediation returns to the owning tab, invalidates affected approval, requires re-approval and a new review round.

## Freeze
FREEZE APP FLOW is allowed only after:
- Process 03 source hash still matches.
- Gates 1 and 2 are APPROVED and hashes match.
- Independent review has no unresolved BLOCKER or CRITICAL findings.
- MAJOR/MINOR findings are fixed or explicitly accepted by the user and persisted.
- Draft passes traceability and graph-integrity checks.
- APP_FLOW.md is written, hashed, and read back.
Then Gate 3 = APPROVED and lifecycle_status = FROZEN. A freeze approves the flow contract, not visual design or implementation.

## Required quality checks
- Every user task maps to an approved capability ID.
- Every screen/node has a purpose, entry condition and at least one valid exit, except explicitly terminal outcomes.
- Every transition has a condition or is explicitly unconditional.
- No unreachable node, orphan node, dead-end path or contradictory navigation rule.
- Every critical failure path has recovery or an explicit documented product decision.
- Every flow has a clear completion condition and observable outcome.
- Screen inventory, flow graph and state matrix agree.
- All unresolved assumptions and change requests are visible.
- No new capability or scope expansion is introduced.

If any check cannot be verified, report NOT_VERIFIED rather than PASS.
