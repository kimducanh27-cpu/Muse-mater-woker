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
- which risky assumptions should be tested, and how.

This process is not The Seed ideation stage, Product Definition/PRD, feature specification, UI/UX design, App Flow, architecture, or implementation. Do not cross into those outputs.

The Seed (Process 01) may provide the starting thesis. Discovery can confirm, narrow, reframe, or reject it. A frozen Seed is not proof that the market/user problem exists.

## Operating mode

First identify the context from available artifacts:
- Initial Discovery: a new app/product or concept without an active user base.
- Continuous Discovery: an existing product with users, behavior data, support feedback, or prior research.

Default to Initial Discovery only when the evidence supports that classification. Ask one concise question if the distinction materially changes the work. Do not require the user to repeat information already recorded in project artifacts.

For Android/mobile products, consider platform constraints only when they affect a discovery hypothesis. Do not drift into detailed architecture, API design, screen design, or UI implementation.

## State and approval persistence — mandatory

The canonical state file is product/discovery/00_DISCOVERY_CONTROL.md. Read it before starting or continuing any tab.

- If it does not exist, create it by copying templates/02-PRODUCT-DISCOVERY/00-DISCOVERY-CONTROL.md and initialize the initiative ID. Do not treat the template itself as the live state file.
- If the existing control file belongs to another initiative, do not overwrite it. Stop and ask the user to create a separate initiative workspace/path.
- Never infer approval from silence, positive sentiment, an AI recommendation, or a phrase that does not exactly match the required command.
- When the user sends an exact approval command, update the relevant gate status, command, decision and local timestamp in the control file before saying the gate passed. If the workspace cannot be written, report that the approval is not durably recorded and do not proceed to the next tab.
- A tab must verify the control file; chat history and an approval phrase copied into another artifact are not sufficient.
- Keep an append-only human-readable approval/change log in the control file.

Gate states are PENDING, APPROVED, REJECTED and REOPENED. Evidence state is PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY or NOT_COLLECTED. Outcome state is NOT_CREATED, DRAFT, FROZEN or REVIEW_REQUIRED.

### Invalidation rules

If a gated artifact changes after approval, invalidate that gate and every downstream gate that depends on it. Record why and when in the control file. Specifically:
- Changes to the discovery brief or opportunity map reopen Gate 1, Gate 2 and Gate 3.
- Changes to the evidence register, interview synthesis or assumption map reopen Gate 2 and Gate 3.
- Changes to the experiment plan reopen Gate 3.
- Any such material change after an Outcome was frozen changes its state to REVIEW_REQUIRED; do not silently keep presenting the old Outcome as current.

Preserve prior decisions in the log. Do not delete evidence or approvals to hide a revision.

## Required upstream method library

The files under references/upstream/ are source copies from phuryn/pm-skills, kept verbatim. Read only the relevant source before applying a method. Never edit those source copies in place.

Core methods:
- Opportunity mapping: opportunity-solution-tree/SKILL.md
- New/existing product ideation: brainstorm-ideas-new/SKILL.md or brainstorm-ideas-existing/SKILL.md
- Risk identification: identify-assumptions-new/SKILL.md or identify-assumptions-existing/SKILL.md
- Assumption prioritization: prioritize-assumptions/SKILL.md
- Interview guide: interview-script/SKILL.md
- Interview synthesis: summarize-interview/SKILL.md
- Experiment design: brainstorm-experiments-new/SKILL.md or brainstorm-experiments-existing/SKILL.md
- Feature-request triage, only for an existing product: analyze-feature-requests/SOURCE.md

The upstream discover and interview commands are reference material, not auto-run orchestration. This Skill and the three prompts define the local human-gated workflow.

## Three-tab workflow

### Tab 01 — Opportunity Discovery

Input:
- Prefer product/seed/SEED.md if Process 01 has completed.
- For an existing product, read current product brief, outcome/metric context, user research and known constraints.
- Read the control file and confirm this initiative is not already approved or frozen in a conflicting state.
- If neither Seed nor existing product context exists, ask for the smallest missing context rather than inventing it.

Work:
1. Establish one desired user/product outcome. Do not invent a metric baseline or numerical target.
2. Define the primary user, context, trigger and job-to-be-done.
3. Understand what users currently do, including manual workarounds, substitutes and non-consumption.
4. Separate observations, user claims, stakeholder opinions, desk research and hypotheses.
5. Build an Opportunity Solution Tree: outcome → user opportunities → candidate solution directions → potential experiments.
6. Do not ideate features until the opportunity is clear. When ideating, create multiple genuinely different mechanisms; do not rank by novelty alone.
7. Label the evidence basis of every material opportunity. At this stage, unsupported opportunities are hypotheses, not customer findings.
8. Record what is known, unknown, and what evidence could change the direction.

Artifacts:
- product/discovery/00_DISCOVERY_BRIEF.md
- product/discovery/01_OPPORTUNITY_MAP.md

Stop at Gate 1. Require the exact instruction APPROVE OPPORTUNITY FOCUS. On receipt, update Gate 1 in the control file. Do not start Tab 02 until the file records APPROVED.

### Tab 02 — Customer Evidence

Input:
- Read the approved discovery brief and opportunity map.
- Verify Gate 1 is APPROVED in the control file.
- Read any interview transcripts, notes, surveys, product analytics, support tickets or relevant files supplied by the user.

Work:
1. Identify which uncertainties require direct customer evidence and which can be answered from reliable existing data.
2. Create an interview guide using Mom Test principles: ask about specific past behavior, not hypothetical future use or praise for the idea.
3. If actual interviews/data are supplied, read the source material before synthesis. Preserve exact sample count and limitations.
4. If no primary evidence exists, prepare a research plan and interview guide. Never invent interview findings, customer quotes, survey responses, user counts or analytics.
5. Set evidence status in the control file to PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY or NOT_COLLECTED. Do not upgrade the status merely because an interview guide was created.
6. Separate direct observation, verbatim user statement, researcher interpretation and hypothesis.
7. Look for disconfirming evidence, contradictions, outliers, sampling bias and missing segments.
8. Update an evidence register and risk/assumption map. For each claim, track source, date, context, confidence rationale and limitations.

Artifacts:
- product/discovery/02_INTERVIEW_GUIDE.md
- product/discovery/03_EVIDENCE_REGISTER.md
- product/discovery/04_INTERVIEW_SYNTHESIS.md only if actual source data exists
- product/discovery/05_ASSUMPTION_MAP.md

Stop at Gate 2. Require the exact instruction APPROVE EVIDENCE REVIEW, then update Gate 2 in the control file. If no primary evidence exists, state that this is an evidence-gap/research plan, not validation. Gate 2 may approve the review and plan while the evidence status remains SECONDARY_ONLY or NOT_COLLECTED.

### Tab 03 — Solution & Experiments

Input:
- Read the approved opportunity map, evidence register, interview synthesis if present, assumption map and experiment-control state.
- Verify Gate 1 and Gate 2 are both APPROVED in the control file.

Work:
1. Re-check that solution hypotheses map to user opportunities, not just stakeholder feature requests.
2. Identify Value, Usability, Feasibility and Viability risks. For new products, also consider ethics, go-to-market, strategy and team risks where relevant.
3. Prioritize assumptions by impact if wrong and uncertainty/evidence gap. Use qualitative levels when no defensible numeric data exists.
4. Design the smallest ethical, feasible experiment that can materially change a decision. Prefer observed behavior or meaningful commitment over stated enthusiasm.
5. Define hypothesis, target participant/cohort, method, measurement, success/failure threshold and rationale, time window/sample needs, effort, dependencies, guardrails and interpretation limits.
6. Do not deploy an experiment, contact participants, collect personal data, charge users, publish a landing page, or change a live product without separate explicit authorization for that specific experiment.
7. APPROVE EXPERIMENT PLAN approves the plan only. It does not authorize execution. Record execution authorization separately using AUTHORIZE EXPERIMENT [ID] in the control file before taking any authorized action.
8. Distinguish proposed, approved, running, completed, supported, invalidated and inconclusive. A plan is not a result.
9. If no test has run, the decision status is READY FOR TESTING. Never call the opportunity or solution VALIDATED solely because a plan was approved.

Artifacts:
- product/discovery/06_EXPERIMENT_PLAN.md
- product/discovery/07_DISCOVERY_DECISION.md

Stop at Gate 3. Require the exact instruction APPROVE EXPERIMENT PLAN, update Gate 3 in the control file, and do not auto-run experiments.

### Discovery Outcome lifecycle

- Do not create product/discovery/08_DISCOVERY_OUTCOME.md while all experiments are only proposed or planned.
- Once actual experiment results are supplied, traceable to sources and analyzed, create/update the Outcome as DRAFT. Keep sample, method, deviations, evidence and limitations visible.
- Freeze only after the user explicitly sends FREEZE DISCOVERY. Then update the control file to FROZEN.
- If no experiment has actually run, 07_DISCOVERY_DECISION.md remains the current final artifact with READY FOR TESTING. This is a valid stopping point, not a validated Outcome.

## Evidence integrity rules

- The user's preference, excitement or approval is not evidence of market demand.
- Statements such as "I would use it" are weak evidence; ask for a recent concrete example, existing workaround, time/money spent or commitment.
- Do not treat generic market size, search volume, stars, downloads, competitor features or AI-generated personas as proof that the target user has the problem.
- Do not claim statistical significance from small or biased samples.
- Never fabricate sources, participants, quotes, numbers, outcomes or experiment results.
- Label each material statement as OBSERVED, USER-REPORTED, ANALYTICS, SECONDARY SOURCE, INTERPRETATION, HYPOTHESIS or UNKNOWN.
- If evidence is unavailable, write NOT COLLECTED; if a source cannot be checked, write NOT VERIFIED.
- Respect participant consent and privacy. Anonymize interview notes unless identifying details are essential and the user has authorization to use them.

## Interaction rules

- Sparring should challenge the idea, not the person.
- Ask one high-value question at a time. Do not deliver long questionnaires as the default.
- Make a recommendation, show its strongest counterargument, and expose uncertainty.
- Do not force every framework into every project. Use only methods that answer an actual decision question.
- Preserve user decisions exactly. No approval is inferred from silence, positive sentiment, or an AI recommendation.

## Definition of a frozen Discovery Outcome

A frozen Outcome is complete only when it contains:
1. The target user and situation supported by available evidence.
2. Evidence-supported opportunities with evidence IDs and limitations.
3. Current alternatives/workarounds.
4. An evidence register with source traceability and limitations.
5. Prioritized assumptions, including what remains unknown.
6. Experiments actually completed, observed results, threshold rationale and interpretation limits.
7. A reasoned decision: proceed, narrow, pivot, pause or stop.
8. Explicit open questions and a clearly bounded next-process handoff.

A testing plan alone is not a Discovery Outcome. Do not generate a PRD, Product Definition, App Flow, UX/UI, design system, technical architecture or code as part of this process.
