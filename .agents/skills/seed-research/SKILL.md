---
name: seed-research
description: Conducts deep, evidence-led research for a Seed Candidate after explicit Gate 1 approval. Produces a traceable dossier without silently changing the candidate or choosing the product direction.
---

# Seed Research — Tab 02

## Mission

Find the evidence, counter-evidence, substitutes, constraints and unknowns that could change the product decision. Optimize for decision quality, not report length.

Default language: Vietnamese. Preserve source names and technical terminology.

## Preconditions

1. Read `product/seed/01_SEED_CANDIDATE.md` and `product/seed/03_DECISION_LOG.md`.
2. Confirm both the candidate and decision log explicitly record `APPROVE GATE 1`.
3. If approval is missing, ambiguous, contradicted or the artifacts are stale, stop and report the exact blocker.
4. Treat artifacts as the source of truth. Do not rely on Tab 01 chat history.

## Research work

Build a research plan from the candidate's highest-impact assumptions. Investigate only relevant areas:

- Problem and user context: observable evidence of the job, pain, trigger and current workaround.
- Alternatives: direct competitors, indirect substitutes, manual workflows and non-app solutions.
- Product patterns: how comparable products actually work; distinguish documented capability from marketing.
- GitHub/open-source: inspect repository scope, relevant files, license, releases, meaningful commits, maintenance and platform constraints. Do not infer reuse rights if there is no clear license.
- Android feasibility: verify only platform constraints material to the proposed mechanism using Android Developers or other primary documentation.
- Risks: falsifiable assumptions, evidence for and against, likely impact and cheapest credible test.

Do not force all categories when irrelevant. State why a category is out of scope.

## Evidence rules

- Prefer primary sources: official documentation, actual product pages, release notes, repository code/configuration, standards and platform documentation.
- Open and inspect high-impact sources. Search snippets alone are discovery aids, not final evidence.
- Cross-check high-impact claims with independent evidence when feasible.
- Record source URL, publisher/owner, date published or updated when visible, date checked, evidence summary and source limitation.
- Separate FACT, USER-REPORTED, INTERPRETATION and HYPOTHESIS.
- Treat community posts as qualitative reports, not proof of prevalence.
- Stars, downloads, forks, launch announcements and promotional claims are weak signals, not evidence of product demand or software quality.
- If a source cannot be opened or a claim cannot be confirmed, write `NOT VERIFIED`; if a search produces no evidence, write `NOT FOUND`. Never fill gaps with plausible numbers.
- No fake precision or invented confidence percentages.

## Decision discipline

Do not edit `01_SEED_CANDIDATE.md` or update the decision log as if the user approved a choice. You may propose changes, explain why evidence points toward another direction, and ask the user to decide.

## Deliverable

Create `product/seed/02_RESEARCH_DOSSIER.md` using `templates/02-RESEARCH-DOSSIER.md`. Include:
1. Scope, date, search method and explicit exclusions.
2. Three to six decision-relevant findings.
3. Problem/user evidence and current alternatives.
4. Comparable products and substitutes.
5. GitHub/open-source findings where relevant.
6. Android constraints where relevant.
7. Assumption/risk register with counter-evidence.
8. Implications for candidate directions (not a decision).
9. Evidence register with traceable URLs and dates.
10. Limitations, NOT FOUND and NOT VERIFIED items.

End with a Gate 2 brief: strongest support, strongest challenge, what changed, the one to three choices that require the user, and a clearly labeled AI recommendation.

## Stop

Ask for exactly one next instruction: `APPROVE GATE 2`, `MORE RESEARCH: [specific question]` or `RETURN TO EXPLORE: [reason]`. Stop. Do not start Tab 03.
