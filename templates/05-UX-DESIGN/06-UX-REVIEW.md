# 06 — UX Review History

> Append-only. Owner: Tab 03. Never edit or delete a prior round.
> Initialize this file from the template, read it back, hash it, and bind the hash with `REVIEW_HISTORY_INITIALIZED` **before** Round 1.

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
| Reviewer | clean-context reviewer, read-only on 01–05 and 08 |

**Artifact hashes reviewed**

| Artifact | SHA-256 |
|---|---|
| `01_SCREEN_UX_MODEL.md` | |
| `02_INTERACTION_PATTERNS.md` | |
| `03_STATE_EXPERIENCE.md` | |
| `04_CONTENT_AND_COPY_INTENT.md` | |
| `05_ACCESSIBILITY_REQUIREMENTS.md` | |
| `08_DECISION_LOG.md` | |
| `07_UX_SPEC_DRAFT.md` | |
| Process 04 `APP_FLOW.md` | |
| Product Definition | |

**Set comparisons performed**

| Comparison | Expected | Observed | Result |
|---|---|---|---|
| SCREEN IDs in 01 vs Process 04 inventory | equal | | PASS / FAIL |
| (screen, state) rows vs Process 04 matrix projection | equal | | PASS / FAIL |
| Pattern IDs cited vs defined | closed | | PASS / FAIL |
| Capabilities served vs frozen scope | total | | PASS / FAIL |
| Named components in 01–05 | `0` | | PASS / FAIL |
| Colour / typography / spacing values in 01–05 | `0` | | PASS / FAIL |

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

BLOCKER and CRITICAL findings cannot be accepted. A blanket statement, a general approval or silence is never an acceptance, and one command accepts exactly one finding.

## Rules

- Never rewrite a historical finding row. If a finding is fixed, append a new round that records its resolution.
- Never append the same round twice. If the Control update failed after the append, recovery requires `RECOVER REVIEW ROUND [N]` and every precondition in the Skill.
- A round appended before Gate 1 or Gate 2 approval is invalid and must be marked as such, not deleted.
