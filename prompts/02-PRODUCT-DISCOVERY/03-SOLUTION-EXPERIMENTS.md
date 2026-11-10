# PROCESS 02 — TAB 03: SOLUTION & EXPERIMENTS

Use the active `product-discovery` skill. This is a fresh conversation in the same workspace.

## Read first

- `product/discovery/00_DISCOVERY_BRIEF.md`
- `product/discovery/01_OPPORTUNITY_MAP.md`
- `product/discovery/03_EVIDENCE_REGISTER.md`
- `product/discovery/04_INTERVIEW_SYNTHESIS.md` if present
- `product/discovery/05_ASSUMPTION_MAP.md`
- Read the relevant upstream sources for assumption prioritization and experiment design.

Do not begin unless Gate 1 and Gate 2 approvals are explicitly recorded. If missing, stop and show the blocker.

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
7. Distinguish a proposed test from an approved, running or completed test. Do not execute or deploy anything unless explicitly requested and supported.
8. If no test has run, final status must be `READY FOR TESTING`, not `VALIDATED`.

## Boundaries

- Do not create PRD, App Flow, UX/UI, detailed prototype screens, architecture, database schema, tickets or code.
- Do not claim statistical significance from a small or biased sample.
- Do not fabricate experiment results.
- No autonomous tab handoff.

## Output

Create/update:
- `product/discovery/06_EXPERIMENT_PLAN.md`
- `product/discovery/07_DISCOVERY_DECISION.md`

Create `product/discovery/08_DISCOVERY_OUTCOME.md` only after actual results are supplied and analyzed. Show evidence, limitations, supported/invalidated/inconclusive assumptions, and a recommendation to proceed, narrow, pivot, pause or stop.

Stop and wait for `APPROVE EXPERIMENT PLAN`. After tests run, wait for explicit `FREEZE DISCOVERY` before finalizing the Discovery Outcome.
