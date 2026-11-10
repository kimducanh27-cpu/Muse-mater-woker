# Process 02 — Product Discovery Kit

This is the second process in the seven-process product-building workflow. It starts from a frozen Seed (Process 01) or a documented existing product context and turns it into an evidence-backed discovery decision.

**It is not Product Definition/PRD, Product Design, App Flow, UX/UI, or engineering implementation.**

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
- `.agents/skills/product-discovery/SKILL.md`

Three independent Antigravity conversations, same workspace:
1. [Tab 01 — Opportunity Discovery](../prompts/02-PRODUCT-DISCOVERY/01-OPPORTUNITY-DISCOVERY.md)
2. [Tab 02 — Customer Evidence](../prompts/02-PRODUCT-DISCOVERY/02-CUSTOMER-EVIDENCE.md)
3. [Tab 03 — Solution & Experiments](../prompts/02-PRODUCT-DISCOVERY/03-SOLUTION-EXPERIMENTS.md)

The upstream Product Discovery methods are preserved verbatim inside the skill's `references/upstream/` folder. See [UPSTREAMS.md](UPSTREAMS.md) and [LICENSES](LICENSES/PM-SKILLS-MIT-LICENSE.txt).

## Inputs

Preferred:
- `product/seed/SEED.md` from Process 01.
- Existing product context if working on an app that already has users.
- User interview notes/transcripts, analytics, support feedback, surveys, product metrics, constraints and decisions, if available.

Do not fabricate missing inputs. If no customer evidence exists, generate a research plan and clearly mark validation as pending.

## Three tabs and gates

| Tab | Purpose | Main artifacts | Gate |
|---|---|---|---|
| 01 Opportunity Discovery | Define outcome, user/job and opportunity map; avoid premature feature ideas | `00_DISCOVERY_BRIEF.md`, `01_OPPORTUNITY_MAP.md` | `APPROVE OPPORTUNITY FOCUS` |
| 02 Customer Evidence | Interview planning, evidence synthesis, assumptions and counter-evidence | `02_INTERVIEW_GUIDE.md`, `03_EVIDENCE_REGISTER.md`, `04_INTERVIEW_SYNTHESIS.md`, `05_ASSUMPTION_MAP.md` | `APPROVE EVIDENCE SYNTHESIS` |
| 03 Solution & Experiments | Generate solution hypotheses, prioritize risks, design experiments and decisions | `06_EXPERIMENT_PLAN.md`, `07_DISCOVERY_DECISION.md` | `APPROVE EXPERIMENT PLAN` |

After experiments are actually run and results are supplied, update the record and create `08_DISCOVERY_OUTCOME.md`. The plan itself is never called validation.

## Quality gates

- Evidence from behavior outweighs stated enthusiasm.
- Interview questions ask about recent, concrete past behavior; they do not pitch the idea.
- Separate observation, user-reported statement, analytics, secondary source, interpretation and hypothesis.
- Sample size, recruitment bias, date, data gaps and limits must stay visible.
- A high-level experiment needs hypothesis, cohort, method, success/failure criteria, timeframe, effort and guardrails.
- No fake precision, fabricated interviews, invented customer quotes or claimed experiment results.
- Never deploy an experiment, collect personal data or change a live product without explicit authorization.
- Do not generate PRD, App Flow, UX/UI, architecture or code.

## How to start

Open a fresh Antigravity tab in the same workspace, read the active skill, then paste the matching prompt. One tab does not automatically start the next. Transfer work through files, not chat history.

For each idea, the process artifacts live in `product/discovery/`. Keep private participant data out of a public Git repository; anonymize or store sensitive research outside the repository.
