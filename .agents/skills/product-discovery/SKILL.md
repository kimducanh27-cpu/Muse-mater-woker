---
name: product-discovery
description: Run Process 02 Product Discovery after a product seed or for an existing product. Discover customer opportunities, collect behavioral evidence, map assumptions, and design validation experiments. Do not create PRDs, App Flows, UX/UI, or implementation plans.
---

# Product Discovery — Process 02

## Mission and boundary

Product Discovery turns a product idea/seed into an evidence-backed understanding of:
- which user and situation matter;
- what important unmet need or opportunity exists;
- what alternatives/workarounds users rely on;
- which solution hypotheses are worth testing;
- which risky assumptions must be validated, and how.

This process is **not** The Seed ideation stage, PRD writing, feature specification, UI/UX design, App Flow, architecture, or implementation. Do not cross into those outputs.

The Seed (Process 01) may provide the starting thesis. Discovery can confirm, narrow, reframe, or reject it. Do not treat the frozen Seed as proof that the market/user problem exists.

## Operating mode

First identify the context from available artifacts:
- **Initial Discovery:** a new app/product or concept without an active user base.
- **Continuous Discovery:** an existing product with users, behavior data, support feedback, or prior research.

Default to Initial Discovery only when the evidence supports that classification. Ask one concise question if the distinction materially changes the work. Do not require the user to repeat information already in `product/seed/SEED.md` or other project artifacts.

For Android/mobile products, consider platform constraints only when they affect a discovery hypothesis. Do not drift into detailed architecture, API design, screen design, or UI implementation.

## Required upstream method library

The files under `references/upstream/` are source copies from `phuryn/pm-skills`, kept verbatim. Read only the relevant source before applying a method. Never edit or silently paraphrase those upstream files in place.

Core methods:
- Opportunity mapping: `opportunity-solution-tree/SKILL.md`
- New/existing product ideation: `brainstorm-ideas-new/SKILL.md` or `brainstorm-ideas-existing/SKILL.md`
- Risk identification: `identify-assumptions-new/SKILL.md` or `identify-assumptions-existing/SKILL.md`
- Assumption prioritization: `prioritize-assumptions/SKILL.md`
- Interview guide: `interview-script/SKILL.md`
- Interview synthesis: `summarize-interview/SKILL.md`
- Experiment design: `brainstorm-experiments-new/SKILL.md` or `brainstorm-experiments-existing/SKILL.md`
- Feature-request triage, only for an existing product: `analyze-feature-requests/SKILL.md`

The upstream `discover` and `interview` commands are retained as reference, not auto-run orchestration. This skill and the three prompts define this repository's human-gated workflow.

## Three-tab workflow

### Tab 01 — Opportunity Discovery

Input:
- Prefer `product/seed/SEED.md` if Process 01 has completed.
- For an existing product, read current product brief, outcome/metric context, user research and known constraints.
- If neither exists, ask for the smallest missing context rather than inventing it.

Work:
1. Establish one desired user/product outcome. Do not invent a metric baseline or numerical target.
2. Define the primary user, context, trigger and job-to-be-done.
3. Understand what users currently do, including manual workarounds, substitutes and non-consumption.
4. Separate observations, user claims, stakeholder opinions, desk research and hypotheses.
5. Build an Opportunity Solution Tree: outcome → user opportunities → candidate solution directions → potential experiments.
6. Do not ideate features until the opportunity is clear. When ideating, create multiple genuinely different mechanisms; do not rank by novelty alone.
7. Record what is known, unknown, and what evidence could change the direction.

Artifacts:
- `product/discovery/00_DISCOVERY_BRIEF.md`
- `product/discovery/01_OPPORTUNITY_MAP.md`

Stop at Gate 1. Require the exact instruction `APPROVE OPPORTUNITY FOCUS` before moving to Tab 02.

### Tab 02 — Customer Evidence

Input:
- Read the approved opportunity map and discovery brief.
- Read any interview transcripts, notes, surveys, product analytics, support tickets or relevant files supplied by the user.

Work:
1. Identify which uncertainties require direct customer evidence and which can be answered from reliable existing data.
2. Create an interview guide using the Mom Test principles: ask about specific past behavior, not hypothetical future use or praise for the idea.
3. If actual interviews are supplied, read the source material and synthesize across participants. Preserve exact participant count and sample limitations.
4. If no interviews/data exist, prepare a research plan and interview guide. Never invent interview findings, customer quotes, survey responses, user counts or analytics.
5. Separate direct observation, verbatim user statement, researcher interpretation and hypothesis.
6. Look for disconfirming evidence, contradictions, outliers, sampling bias and missing segments.
7. Update an evidence register and risk/assumption map. For each claim, track source, date, context, confidence rationale and limitations.

Artifacts:
- `product/discovery/02_INTERVIEW_GUIDE.md`
- `product/discovery/03_EVIDENCE_REGISTER.md`
- `product/discovery/04_INTERVIEW_SYNTHESIS.md` (only if actual source data exists)
- `product/discovery/05_ASSUMPTION_MAP.md`

Stop at Gate 2. Require `APPROVE EVIDENCE SYNTHESIS` before Tab 03. If no primary evidence exists, clearly state that the work is a research plan, not validation.

### Tab 03 — Solution & Experiments

Input:
- Read the approved opportunity map, evidence register, interview synthesis (if any), and assumption map.

Work:
1. List solution hypotheses tied to the highest-priority user opportunities.
2. For each, identify Value, Usability, Feasibility and Viability risks. For new products, also consider ethics, go-to-market, strategy and team risks where relevant.
3. Prioritize assumptions by impact if wrong and uncertainty/evidence gap. Use qualitative levels when no defensible numeric data exists. Do not manufacture precision.
4. Design the smallest ethical, feasible experiment that can materially change the decision. Prefer observed behavior or meaningful commitment over stated enthusiasm.
5. Define hypothesis, target participant/cohort, method, measurement, success/failure threshold, time window, effort, dependencies, guardrails and interpretation limits.
6. Do not deploy an experiment, contact participants, collect personal data, charge users, publish a landing page, or change a live product unless the user explicitly asks and the action is within available capabilities.
7. Distinguish **proposed**, **approved**, **running**, **completed**, **supported**, **invalidated** and **inconclusive**. A plan is not a result.
8. If results do not exist yet, the correct status is `READY FOR TESTING`, never `VALIDATED`.

Artifacts:
- `product/discovery/06_EXPERIMENT_PLAN.md`
- `product/discovery/07_DISCOVERY_DECISION.md` (decision brief; keep unresolved assumptions visible)
- `product/discovery/08_DISCOVERY_OUTCOME.md` only after actual experiment results are provided and analyzed.

Stop at Gate 3. Require `APPROVE EXPERIMENT PLAN` before treating the plan as accepted. After tests run, record results and limitations. Only create/finalize the Discovery Outcome after the user asks to freeze it with `FREEZE DISCOVERY`.

## Evidence integrity rules

- The user's preference, excitement or approval is not evidence of market demand.
- Statements such as "I would use it" are weak evidence; ask for a recent concrete example, existing workaround, time/money spent or commitment.
- Do not treat generic market size, search volume, stars, downloads, competitor features or AI-generated personas as proof that the target user has the problem.
- Do not claim statistical significance from small or biased samples.
- Never fabricate sources, participants, quotes, numbers, outcomes or experiment results.
- Label each material statement as one of: `OBSERVED`, `USER-REPORTED`, `ANALYTICS`, `SECONDARY SOURCE`, `INTERPRETATION`, `HYPOTHESIS`, `UNKNOWN`.
- If evidence is unavailable, write `NOT COLLECTED`; if a source cannot be checked, write `NOT VERIFIED`.
- Respect participant consent and privacy. Anonymize interview notes unless identifying details are essential and the user has authorization to use them.

## Interaction rules

- Sparring should challenge the idea, not the person.
- Ask one high-value question at a time. Do not deliver long questionnaires as the default.
- Make a recommendation, show its strongest counterargument, and expose uncertainty.
- Do not force every framework into every project. Use only methods that answer an actual decision question.
- Preserve user decisions exactly. No approval is inferred from silence, positive sentiment, or an AI recommendation.

## Definition of done

A Discovery Outcome is complete only when it contains:
1. The target user and situation supported by available evidence.
2. The clearest validated or still-unvalidated opportunity.
3. Current alternatives/workarounds.
4. Evidence register with source traceability and limitations.
5. Prioritized assumptions, including what remains unknown.
6. Experiment results or a clearly labeled testing plan.
7. A reasoned decision: proceed, narrow, pivot, pause, or stop.
8. Explicit open questions and the next process handoff boundary.

Do not generate a PRD, App Flow, UX/UI, design system, technical architecture or code as part of this process.
