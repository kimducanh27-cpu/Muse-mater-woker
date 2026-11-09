# REVIEW.md — Shared Review and Gate Policy

**Version:** 3.0  
**Status:** Normative  
**Applies to:** Phase 2, Phase 3, and Master aggregation

## 1. Authority and precedence

This file is the single source of truth for cross-phase review states, review evidence, and the full-regression contract.

- `SECURITY_REVIEW.md` is authoritative for security-review scope, independence, findings, and security veto. Where a security rule is stricter, it prevails.
- `docs/specs/phase-1.md` defines design-system inputs and acceptance criteria. Phase 1 is specification-only and does not replace Phase 2/3 code gates.
- `docs/specs/phase-2.md` and `docs/specs/phase-3.md` define when their platform-specific work invokes these gates. They MUST NOT weaken or skip this policy.
- `MUSE_ORCHESTRATOR.md` owns dispatch, evidence collection, state transitions, and merge/release aggregation.
- `scripts/validate-gates.py` validates the minimum machine-readable evidence contract. Missing validator, malformed evidence, stale evidence, or a non-zero validator exit is a blocked gate, never a warning or PASS.

A prompt, verbal statement, screenshot, or agent claim is not a substitute for a machine-readable artifact plus its referenced evidence.

## 2. Canonical gate states

Every gate and aggregate result MUST use exactly one of these states:

| State | Meaning | Merge/release eligible |
|---|---|---:|
| `NOT_RUN` | Required check has not executed or has no result yet. | No |
| `PASS` | All required assertions and evidence for this gate pass for the exact candidate revision. | Yes, subject to every other gate and approval |
| `FAIL` | A check failed or an unresolved finding exists. | No |
| `BLOCKED` | Required tool, input, permission, artifact, or evidence is missing or invalid. | No |
| `ARBITRATION` | A non-security reviewer disagreement remains unresolved. | No |
| `FLAKY` | A required check is nondeterministic, intermittent, or has not produced a stable result. | No |

Reviewer votes may be `PASS` or `REJECT`; map `REJECT` to a failed gate. A reviewer vote is not the aggregate gate state. The legacy labels `FLAKY_WARNING`, `CONSENSUS`, or a bare `PASS` string without evidence MUST NOT make a gate eligible.

**No transition may convert `NOT_RUN`, `FAIL`, `BLOCKED`, `ARBITRATION`, or `FLAKY` directly to `PASS`.** The underlying problem must be fixed and the required checks rerun. Master arbitration cannot override the Security Reviewer veto.

## 3. Candidate and evidence identity

Each phase task MUST create an immutable candidate commit in its isolated worker branch before dispatching reviewers. Do not merge it yet. Every artifact MUST identify the same:

- `run_id`
- `candidate_sha` — the exact candidate commit under review
- `phase` — 2 or 3
- `platforms_required` — the platforms required by the task charter

Store all evidence under `.agy/runs/<run-id>/`:

| Artifact | Required purpose |
|---|---|
| `manifest.json` | Candidate identity, phase, and required platforms |
| `regression.json` | Full functional, build, visual, immutability, and platform regression |
| `independent-review.json` | Fresh-context UX/Vision and Code/Architecture reviewer results |
| `security-review.json` | Fresh-context, read-only security reviewer result |
| `gate-result.json` | Machine-generated aggregate produced by the validator |

Each PASS check MUST include the executed `command`, `exit_code: 0`, and a non-empty `evidence` path relative to the run directory. The referenced evidence file MUST exist and be non-empty. Evidence paths MUST NOT escape the run directory. Platform-specific results MUST cover every entry in `manifest.json.platforms_required`.

The candidate SHA is a freshness boundary. Any source change, rebase, cherry-pick, regenerated candidate, or changed platform scope invalidates all prior regression, independent-review, and security-review artifacts. Create a new candidate identity and rerun the complete sequence.

## 4. Mandatory full-regression contract

After **every code change**, including remediation, rerun the complete regression contract before dispatching or rerunning independent reviewers, before invoking final arbitration, and before reporting PASS.

For **each required platform** (Web and/or Android), `regression.json` MUST contain successful evidence for:

1. **Build** — production/release-relevant build for the candidate.
2. **Typecheck** — TypeScript/Kotlin compiler or the platform's equivalent static type validation.
3. **Lint** — all applicable source and configuration lint rules.
4. **Unit tests** — the relevant component/screen unit-test suite.
5. **State-matrix tests** — all contract states, including Loading, Data/Success, Empty, Error, Retry, Disabled, and other states required by the spec.
6. **E2E tests** — the complete required user-journey suite, not just a smoke test.
7. **Visual snapshot verification** — compare against an approved baseline; missing, stale, or unapproved baselines block. Recording a new baseline is a separate approval action, not an automatic pass.
8. **Responsive/platform checks** — the required viewport, window-size, orientation, and target-device checks for that platform.

Additionally, every run MUST include a frozen-input immutability check: Phase 2 proves that the Phase 1 SSOT/tokens/contracts were not modified; Phase 3 proves that frozen Phase 2 components were not modified. The artifact key is `frozen_input_immutability` for Phase 2 and `component_immutability` for Phase 3. A regression check may not be silently omitted or marked NOT_APPLICABLE; the validator requires each regression check to pass for every required platform. The only current NOT_APPLICABLE exceptions are the Security policy's authorization and network-boundary subchecks, with reason and evidence.

A check is complete only when its result and evidence are present. A command that was not run, a missing tool, a missing test directory, an empty snapshot directory, a stale baseline, or a missing evidence file is `BLOCKED` or `FAIL`, never PASS.

## 5. Reviewer independence and remediation

- UX/Vision and Code/Architecture reviewers MUST receive fresh, isolated context and the exact candidate SHA/diff they are reviewing.
- Reviewers MUST have read-only access to audited source. They may write only their separate report artifact; they MUST NOT modify implementation files, tests, snapshots, manifests, or candidate commits.
- The Worker MUST NOT author, edit, or suppress reviewer findings. The Master collects reports and enforces the result; it does not edit implementation code.
- A reviewer MUST focus on the candidate diff plus the adjacent context needed to validate the change. Each finding should identify file/symbol or screen/state, violated requirement, evidence, severity, and remediation.
- Duplicate findings may be consolidated only when the same underlying defect is demonstrably identical. A finding may be marked resolved only with a fix reference and passing verification for the new candidate SHA.
- Any code remediation invalidates the old reports. Rerun full regression first, then dispatch fresh independent reviews and a fresh security review for the new candidate.
- Maximum automatic remediation budget is three cycles per task. On exhaustion, preserve the worktree and all evidence, set `BLOCKED`, and request human direction. Do not merge.

## 6. Aggregation and authority

The Master MUST run:

```bash
python3 scripts/validate-gates.py --run-dir .agy/runs/<run-id>
```

Only exit code 0 with `gate-result.json.status == "PASS"` and `merge_eligible == true` may advance to checkpoint/merge/PR. A missing script or failed invocation is `BLOCKED`. The validator checks artifact structure, matching candidate identity, reported exit codes, read-only declarations, and evidence-file existence; it does not independently execute scanners or tests. The Master MUST therefore verify that the evidence files are outputs from the named tools and candidate, not hand-written assertions.

A successful technical gate does not replace human approval required by the change-risk policy. Defect severity (P0/P1/P2) and change risk (LOW/MEDIUM/HIGH) are separate dimensions. AI agents never count as human approvers.

## 7. Evaluation and policy gaps

Before setting quantitative reviewer-quality targets, establish a versioned evaluation corpus containing known-bug patches, clean patches, regressions, and false-positive cases. Record true positives, false positives, false negatives, reviewer agreement, review rounds, and reverts. Do not claim reviewer effectiveness from qualitative document review or set target percentages without a measured baseline.

