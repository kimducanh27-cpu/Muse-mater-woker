# PROCESS 02 — TAB 03: SOLUTION & EXPERIMENTS

Use the active product-discovery Skill. This is a fresh conversation in the same workspace.

## Read first

- product/discovery/00_DISCOVERY_CONTROL.md
- product/discovery/00_DISCOVERY_BRIEF.md
- product/discovery/01_OPPORTUNITY_MAP.md
- product/discovery/03_EVIDENCE_REGISTER.md
- product/discovery/04_INTERVIEW_SYNTHESIS.md if present
- product/discovery/05_ASSUMPTION_MAP.md
- Read the relevant upstream sources for assumption prioritization and experiment design.

## Entry gates

Do not begin solution/experiment work unless Gate 1 and Gate 2 are both APPROVED in the control file for this initiative. If either is missing, PENDING, REJECTED or REOPENED, stop and show the blocker. Never infer approval from chat history or artifact text alone.

## Your task

1. Re-check that solution hypotheses map to user opportunities, not just stakeholder feature requests.
2. Identify the riskiest assumptions using Impact × Uncertainty; use qualitative bands unless the data supports numeric scoring.
3. Generate alternative solution mechanisms for the highest-priority opportunities.
4. Design the smallest responsible experiment that can change a decision.
5. For each experiment, specify:
   - hypothesis and assumption tested;
   - target segment / participant criteria;
   - method and procedure;
   - behavioral signal and measurement;
   - success and failure thresholds, including how thresholds were chosen;
   - duration/sample needs and limitations;
   - effort, dependency and ethical/privacy guardrails;
   - what decision follows each possible result.
6. Prefer actual behavior or meaningful commitment over stated enthusiasm.
7. Distinguish a proposed test from an approved, authorized, running or completed test.
8. If no test has run, final decision status must be READY FOR TESTING, not VALIDATED.

## Execution boundary

APPROVE EXPERIMENT PLAN approves the plan only. It does not authorize execution.

Do not contact participants, collect personal data, charge users, publish a landing page, deploy a test, change a live product or incur costs unless the user separately authorizes the specific experiment with the exact command AUTHORIZE EXPERIMENT [ID], and the action is within available capabilities and appropriate safeguards. Record that authorization in the control file before execution. If the action cannot be safely or technically performed, explain the limitation and do not imply it ran.

## Boundaries

- Do not create PRD, Product Definition, App Flow, UX/UI, detailed prototype screens, architecture, database schema, tickets or code.
- Do not claim statistical significance from a small or biased sample.
- Do not fabricate experiment results.
- No autonomous tab handoff.

## Output

Create/update:
- product/discovery/06_EXPERIMENT_PLAN.md
- product/discovery/07_DISCOVERY_DECISION.md

Keep 07_DISCOVERY_DECISION.md as READY FOR TESTING while experiments have not actually run.

Create product/discovery/08_DISCOVERY_OUTCOME.md only after actual experiment results are supplied, traceable to sources and analyzed. Do not create an Outcome containing only a proposed testing plan.

## Gate 3

Stop and wait for the exact command: APPROVE EXPERIMENT PLAN.

When received:
1. Update Gate 3 in product/discovery/00_DISCOVERY_CONTROL.md to APPROVED.
2. Record the exact command, user decision and local timestamp (Asia/Ho_Chi_Minh).
3. Add a log entry. Do not claim Gate 3 passed until the file is saved successfully.

After actual experiment results exist, update the evidence register and create the Outcome as DRAFT. Only freeze it when the user sends FREEZE DISCOVERY; update the control file to FROZEN. Do not auto-start another process.
