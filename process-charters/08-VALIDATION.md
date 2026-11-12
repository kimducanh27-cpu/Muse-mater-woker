# Process 08 — Validation (charter)

> Status: **CHARTER — NO CONTRACT.** Scope only. No Skill, prompts, templates, Control File or gates exist.

## 1. Why this process exists

Four processes each freeze an artifact and each verifies its own work. None of them verifies the chain. A flow can be complete, a UX spec coherent, a system consistent and a UI spec buildable — and the composition of all four can still be wrong: a capability that no screen serves, a state that no component can express, a copy string that contradicts a flow guarantee.

Process 08 produces **evidence** that the chain holds, and blocks build if it does not. It is not a taste review and not a QA pass on code. It answers one question: *is this design safe to build?*

## 2. Position in the sequence

```
04 App Flow ─┐
05 UX Design ├─▶ 08 Validation ──frozen VALIDATION_REPORT.md + hash──▶ build
06 Design Sys┤
07 UI Design ┘
```

Process 08 is the only process that reads all four frozen artifacts at once. That is why it cannot be folded into any of them: each upstream process is forbidden from judging its own output against its siblings.

## 3. Input contract

All four, frozen and hash-verified against their own Control Files:

- `product/app-flow/APP_FLOW.md`
- `product/ux-design/UX_SPEC.md`
- `product/design-system/DESIGN_SYSTEM.md`
- `product/ui-design/UI_SPEC.md`

Entry is blocked if any upstream has an open Change Request. Validating a chain with a known hole produces a report that must be thrown away.

## 4. Output contract

Proposed working artifacts (`product/validation/`):

| File | Purpose |
|---|---|
| `01_VALIDATION_PLAN.md` | What will be validated, how, by whom, and the pass criteria — written **before** any result is known |
| `02_TRACEABILITY_MATRIX.md` | capability → task → screen → state → component → composition, every link explicit |
| `03_ACCESSIBILITY_AUDIT.md` | Conformance measured per screen: contrast from token values, focus order, target size, keyboard reachability, announcement intent |
| `04_USABILITY_EVIDENCE.md` | Heuristic evaluation and/or executed user testing, each finding labelled with its evidence strength |
| `05_FINDINGS_REGISTER.md` | Append-only findings with severity, evidence, owning process and status |
| `06_VALIDATION_REPORT_DRAFT.md` | Complete reviewed candidate with verdict |
| `07_DECISION_LOG.md` | Append-only user-approved validation decisions and residual-risk acceptances |

Frozen output: `product/validation/VALIDATION_REPORT.md`.

Control schema: `v1`.

## 5. Gates and exact commands

| Tab | Gate | Exact command |
|---|---|---|
| 01 Plan and traceability | Plan approved before execution | `APPROVE VALIDATION PLAN` |
| 02 Evidence execution | Evidence approved | `APPROVE VALIDATION EVIDENCE` |
| 03 Independent verdict | Freeze authorized | `FREEZE VALIDATION REPORT` |

Gate 1 must be approved **before** any evidence is produced. A pass criterion invented after seeing the result is not a criterion.

## 6. Boundaries — what Process 08 must not do

- **No remediation.** It may not edit any upstream artifact, add a component, add a state or fix copy. Every defect is a finding addressed to its owning process.
- **No acceptance on the user's behalf.** Residual risk is accepted only by an explicit user command with a rationale, exactly as in Processes 04 and 05.
- **No product scope judgement.** A finding may say "this capability has no screen"; it may not decide whether the capability should be dropped.
- **No code review, no QA on implementation, no performance testing.** Those belong to a post-build process, which is not this one.
- **No opinion without evidence.** "Feels cluttered" is not a finding. "Primary action is below the fold at 1280×720 on SCREEN-07" is.

## 7. Evidence discipline — the rule that makes this process real

- **Not executed is not passed.** A validation report with zero executed tests is `NOT RUN`, never `PASS`. This mirrors the Discovery rule that an unrun experiment cannot produce an Outcome.
- **Heuristic evaluation is advisory, not evidence.** It may justify a `CONDITIONAL` verdict and a residual-risk acceptance, but it cannot produce `PASS` on a critical flow.
- **Every finding names an owning process** (03, 04, 05, 06 or 07). A finding with no owner is a wish.
- **Every severity is defined before execution.** BLOCKER = the design cannot be built as specified. CRITICAL = an approved capability is unreachable. MAJOR = a state or screen is inconsistent. MINOR = bounded ambiguity.

## 8. Upstream sources

| Upstream | Path | Use |
|---|---|---|
| `anthropics/knowledge-work-plugins` | `engineering/skills/testing-strategy` | Evidence planning and coverage reasoning |
| `anthropics/knowledge-work-plugins` | `design/skills/accessibility-review` | WCAG audit method |
| `anthropics/knowledge-work-plugins` | `design/skills/design-critique` | Structured critique for Tab 03 |

Apache-2.0. Copy verbatim, record source, date, blob SHA and licence in `UPSTREAMS.md`.

## 9. Open questions — must be resolved before the contract is written

1. **Is real user testing mandatory?** A solo builder may have no users. Options: (a) require at least one executed session per critical flow, blocking freeze otherwise; (b) allow heuristic-only evidence to produce `CONDITIONAL` plus an explicit user-accepted residual risk; (c) make user testing an optional post-freeze activity. Current recommendation: (b) — it keeps the gate honest without making the process unrunnable.
2. **Who reviews the reviewer?** Tab 03 is an independent reviewer of a report that is itself a review. Recursion must terminate somewhere. Recommendation: Tab 03 checks *evidence integrity only* — that every claimed test exists, every hash matches, every finding has an owner and a severity — and does not re-judge usability.
3. **Accessibility target.** WCAG 2.2 AA is the default assumption; it must be a recorded decision in the Control File, because it changes the audit checklist and the number of findings.
4. **Does this process validate the design, or the product?** If validation means "users can complete the task", it requires a built artefact and belongs after build. Recommendation: v1 validates the **design chain** only. Product validation after build is a separate process and must not be merged into this one, or the gate will silently become unreachable before build starts.
5. **Finding volume control.** A first audit can produce hundreds of MINOR findings. Recommendation: MINOR findings are recorded but do not block freeze; only BLOCKER and CRITICAL block, MAJOR requires fix or explicit acceptance.

## 10. Entry and exit in one line

**Entry:** four frozen artifacts and no open Change Requests. **Exit:** a frozen report that either clears the chain for build or names, with evidence, exactly what must change and in which process.
