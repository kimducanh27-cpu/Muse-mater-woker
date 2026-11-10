# Process 02 — Product Discovery Kit

This is the second process in the seven-process product-building workflow. It starts from a frozen Seed (Process 01) or a documented existing product context and turns it into an evidence-backed discovery decision.

It is not Product Definition/PRD, Product Design, App Flow, UX/UI, or engineering implementation.

## What Product Discovery must answer
- Who experiences the problem, in what context, and how do we know?
- What job, unmet need or opportunity is important enough to pursue?
- What do people currently do instead?
- Which solution hypotheses could address the opportunity?
- Which assumptions are most dangerous?
- What experiment would produce credible learning at the lowest responsible cost?
- What do the findings support, reject or leave unknown?

## Architecture: one active skill, three tabs
Active skill: .agents/skills/product-discovery/SKILL.md

Three independent Antigravity conversations, same workspace:
1. Tab 01 — Opportunity Discovery: ../prompts/02-PRODUCT-DISCOVERY/01-OPPORTUNITY-DISCOVERY.md
2. Tab 02 — Customer Evidence: ../prompts/02-PRODUCT-DISCOVERY/02-CUSTOMER-EVIDENCE.md
3. Tab 03 — Solution & Experiments: ../prompts/02-PRODUCT-DISCOVERY/03-SOLUTION-EXPERIMENTS.md

The upstream Product Discovery methods are preserved verbatim inside the Skill's references/upstream/ folder. See UPSTREAMS.md and LICENSES/PM-SKILLS-MIT-LICENSE.txt.

## Inputs
Preferred: product/seed/SEED.md; existing product context for continuous discovery; interviews, analytics, support feedback, surveys and other authorized evidence.
Do not fabricate missing inputs. Mark evidence NOT_COLLECTED or SECONDARY_ONLY when applicable.

## Canonical state file
Every initiative must have product/discovery/00_DISCOVERY_CONTROL.md, copied from templates/02-PRODUCT-DISCOVERY/00-DISCOVERY-CONTROL.md at startup. This is the single source of truth for gates, evidence status, experiment authorizations and Outcome freeze state. Never infer approval from chat history.

## Three tabs and gates
| Tab | Purpose | Main artifacts | Required gate |
|---|---|---|---|
| 01 Opportunity Discovery | Define outcome, user/job and evidence-labeled opportunity map | 00_DISCOVERY_BRIEF.md, 01_OPPORTUNITY_MAP.md | APPROVE OPPORTUNITY FOCUS |
| 02 Customer Evidence | Interview planning, synthesis, counter-evidence and assumptions | 02_INTERVIEW_GUIDE.md, 03_EVIDENCE_REGISTER.md, 04_INTERVIEW_SYNTHESIS.md when real data exists, 05_ASSUMPTION_MAP.md | APPROVE EVIDENCE REVIEW |
| 03 Solution & Experiments | Prioritize risks, design tests and decisions | 06_EXPERIMENT_PLAN.md, 07_DISCOVERY_DECISION.md | APPROVE EXPERIMENT PLAN |

Gate 2 approves evidence review and documented gaps; it does not validate the opportunity. Gate 3 approves the plan, not execution. Each experiment needs separate AUTHORIZE EXPERIMENT [ID].

## Outcome lifecycle
Create 08_DISCOVERY_OUTCOME.md only after actual experiment results are supplied, traceable and analyzed. Freeze with FREEZE DISCOVERY. If no experiment has run, keep 07_DISCOVERY_DECISION.md as READY FOR TESTING; do not create an Outcome based only on a testing plan.

## Handoff to Process 03 — Product Definition
Process 03 consumes an eligible Process 02 handoff: either a frozen Discovery Outcome, or an approved Decision Brief in READY FOR TESTING state with the user's explicit acceptance of residual uncertainty. Process 03 defines product intent and capability scope; it does not redo discovery or create App Flow. See ../product-definition-kit/README.md.

## Quality gates
- Evidence from behavior outweighs stated enthusiasm.
- Interview questions ask about recent, concrete past behavior.
- Separate observation, user report, analytics, secondary source, interpretation and hypothesis.
- Keep sample size, recruitment bias, date, data gaps and limitations visible.
- No fabricated interviews, quotes, metrics or experiment results.
- Never deploy an experiment or collect personal data without separate explicit authorization.
- Do not generate Product Definition, App Flow, UX/UI, architecture or code.

## How to start
Open a fresh Antigravity tab in the same workspace, read the Skill, then paste the matching prompt. Transfer context through files, not chat history. Keep private participant data out of a public repository.
