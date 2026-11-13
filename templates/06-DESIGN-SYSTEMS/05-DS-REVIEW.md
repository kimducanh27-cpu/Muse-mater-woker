# 05 — Design System Review History

> Append-only. Owner: Tab 03. Never edit or delete a prior round.
> Initialize from this template, read back, hash, and bind with `REVIEW_HISTORY_INITIALIZED` **before** Round 1.

## Initialization record

| Field | Value |
|---|---|
| Initialized at local | `<timestamp>` |
| Template SHA-256 | `<sha256>` |
| Bound by Control event | `REVIEW_HISTORY_INITIALIZED` at `state_seq` `<n>` |
| Rounds recorded | 0 |

A file adopted as a baseline must be byte-identical to the template and contain no round and no addendum.

---

## Round template — copy exactly, append once

### Review round `<N>`

| Pre-append anchor | Value |
|---|---|
| Control File `state_seq` before append | `<n>` |
| Control File SHA-256 before append | `<sha256>` |
| Previous review history SHA-256 | `<sha256>` |
| Review round number | `<N>` |
| Reviewed at local | `<timestamp>` |
| Reviewer | clean-context reviewer, read-only on 01–04 and 07 |

**Artifact hashes reviewed**

| Artifact | SHA-256 |
|---|---|
| `01_DESIGN_FOUNDATIONS.md` | |
| `02_TOKEN_CONTRACT.md` | |
| `03_COMPONENT_INVENTORY.md` | |
| `04_COMPONENT_ACCESSIBILITY.md` | |
| `07_DECISION_LOG.md` | |
| `06_DS_DRAFT.md` | |
| Process 05 `UX_SPEC.md` | |
| Process 04 `APP_FLOW.md` | |

**Set comparisons performed**

| Comparison | Expected | Observed | Result |
|---|---|---|---|
| Components with zero citing screens | `0` | | PASS / FAIL |
| Citing SCREEN IDs absent from the frozen inventory | `0` | | PASS / FAIL |
| Screens citing at least one component | = screens in source | | PASS / FAIL |
| Component tokens referencing a reference token | `0` | | PASS / FAIL |
| System tokens without a role statement | `0` | | PASS / FAIL |
| Contrast pairs measured | = pairs required | | PASS / FAIL |
| Contrast pairs failing | `0` | | PASS / FAIL |
| Colour-only state signals | `0` | | PASS / FAIL |
| Screen layout, placement or composition present | `0` | | PASS / FAIL |
| Final copy, code or image present | `0` | | PASS / FAIL |

**Boundary audit.** The three ways this process fails:

1. **Speculative components.** A component whose only justification is "Material 3 has one". Check every entry's citing screens against the frozen inventory, not against plausibility.
2. **Declared contrast.** A ratio with no resolved hex pair behind it, or a pair marked PASS without a stated method. Treat as unmeasured.
3. **Leaked composition.** A component entry that says where it goes, how wide it is on a screen, or which screen region it occupies. That is Process 07's job and it will copy whatever it finds here.

**Findings**

| Finding ID | Severity | Artifact | Exact ID or path | Evidence | Scenario | Impact | Minimal correction | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| `F-<NN>` | BLOCKER / CRITICAL / MAJOR / MINOR | | | | | | | | OPEN |

**Verdict.** `GO` / `CONDITIONAL GO` / `HOLD`
**Review status.** `BLOCKERS_FOUND` / `READY_FOR_FREEZE`
**Open counts.** BLOCKER `<n>`, CRITICAL `<n>`, MAJOR `<n>`, MINOR `<n>`

---

## User decision addendum — append only after an explicit command

### Addendum — `<FINDING-ID>` accepted

| Field | Value |
|---|---|
| Finding ID | |
| Severity | MAJOR / MINOR only |
| Accepted by | user |
| Exact command | `ACCEPT RESIDUAL RISK <FINDING-ID>` |
| Rationale | quoted verbatim from the user's message |
| Accepted at local | `<timestamp>` |

BLOCKER and CRITICAL cannot be accepted. One command accepts exactly one finding.

## Rules

- Never rewrite a historical finding row. A fixed finding is recorded in a new round.
- Never append the same round twice. Recovery requires `RECOVER REVIEW ROUND [N]` and every precondition in the Skill.
- A round appended before Gate 1 or Gate 2 approval is invalid and must be marked as such, not deleted.
