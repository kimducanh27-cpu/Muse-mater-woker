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

Active skill:
- .agents/skills/product-discovery/SKILL.md

Three independent Antigravity conversations, same workspace:
1. Tab 01 — Opportunity Discovery: ../prompts/02-PRODUCT-DISCOVERY/01-OPPORTUNITY-DISCOVERY.md
2. Tab 02 — Customer Evidence: ../prompts/02-PRODUCT-DISCOVERY/02-CUSTOMER-EVIDENCE.md
3. Tab 03 — Solution & Experiments: ../prompts/02-PRODUCT-DISCOVERY/03-SOLUTION-EXPERIMENTS.md

The upstream Product Discovery methods are preserved verbatim inside the Skill's references/upstream/ folder. See UPSTREAMS.md and LICENSES/PM-SKILLS-MIT-LICENSE.txt.

## Inputs

Preferred:
- product/seed/SEED.md from Process 01.
- Existing product context if working on an app that already has users.
- User interview notes/transcripts, analytics, support feedback, surveys, product metrics, constraints and decisions, if available.

Do not fabricate missing inputs. If no customer evidence exists, generate a research plan and clearly mark evidence as NOT_COLLECTED or SECONDARY_ONLY.

## Canonical state file

Every initiative must have product/discovery/00_DISCOVERY_CONTROL.md, copied from templates/02-PRODUCT-DISCOVERY/00-DISCOVERY-CONTROL.md at startup.

This file is the only source of truth for Gate 1, Gate 2, Gate 3, evidence status, experiment execution authorizations and Outcome freeze state. A gate is not passed until its exact user command and timestamp are saved successfully in this file. Never infer approval from chat history.

If the control file belongs to another initiative, do not overwrite it; create a separate initiative directory/control file.

## Three tabs and gates

| Tab | Purpose | Main artifacts | Required gate |
|---|---|---|---|
| 01 Opportunity Discovery | Define outcome, user/job and opportunity map; label evidence basis and hypotheses | 00_DISCOVERY_BRIEF.md, 01_OPPORTUNITY_MAP.md | APPROVE OPPORTUNITY FOCUS |
| 02 Customer Evidence | Interview planning, evidence synthesis, counter-evidence and assumptions | 02_INTERVIEW_GUIDE.md, 03_EVIDENCE_REGISTER.md, 04_INTERVIEW_SYNTHESIS.md when real data exists, 05_ASSUMPTION_MAP.md | APPROVE EVIDENCE REVIEW |
| 03 Solution & Experiments | Generate solution hypotheses, prioritize risks, design tests and decisions | 06_EXPERIMENT_PLAN.md, 07_DISCOVERY_DECISION.md | APPROVE EXPERIMENT PLAN |

Approving Gate 2 approves the evidence review and documented gaps; it does not validate the opportunity. Evidence status remains PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY or NOT_COLLECTED.

Approving Gate 3 approves the experiment plan only. It does not authorize execution. Each experiment requires separate explicit authorization using AUTHORIZE EXPERIMENT [ID], recorded in the control file.

## Outcome lifecycle

After experiments are actually run and their results are supplied, traceable and analyzed, create 08_DISCOVERY_OUTCOME.md as DRAFT. Freeze it only after the exact command FREEZE DISCOVERY and record that state in the control file.

If no experiment has run, keep 07_DISCOVERY_DECISION.md as the current artifact with status READY FOR TESTING. Do not create an Outcome containing only a testing plan.

## Quality gates

- Evidence from behavior outweighs stated enthusiasm.
- Interview questions ask about recent, concrete past behavior; they do not pitch the idea.
- Separate observation, user-reported statement, analytics, secondary source, interpretation and hypothesis.
- Sample size, recruitment bias, date, data gaps and limits must stay visible.
- A high-level experiment needs hypothesis, cohort, method, success/failure criteria, timeframe, effort and guardrails.
- No fake precision, fabricated interviews, invented customer quotes or claimed experiment results.
- Never deploy an experiment, collect personal data or change a live product without separate explicit authorization.
- Do not generate Product Definition/PRD, App Flow, UX/UI, architecture or code.

## How to start

Open a fresh Antigravity tab in the same workspace, read the active Skill, then paste the matching prompt. One tab does not automatically start the next. Transfer work through files, not chat history.

For each idea, the process artifacts live in product/discovery/. The control state is canonical. Keep private participant data out of a public Git repository; anonymize or store sensitive research outside the repository.
