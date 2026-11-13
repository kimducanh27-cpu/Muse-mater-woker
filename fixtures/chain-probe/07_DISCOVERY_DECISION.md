> SIMULATED — NOT ELIGIBLE DOWNSTREAM
# Product Discovery Decision Brief

> This is the current decision artifact before and after experiment planning. It is not a Discovery Outcome.

## Discovery question
Can draft saving (`CAP-01`) reduce mobile form abandonment caused by session interruption?

## What we learned
- Strongest supporting evidence: In customer interviews (EVID-01), 85% of mobile filers reported abandoning forms due to lack of draft saving when interrupted.
- Strongest counter-evidence: A small subset of users (10%) assumed drafts auto-save and might fail to click explicit save controls.
- What changed from initial assumptions: Explicit save status indicators are necessary to provide reassurance that drafts are persisted.
- Evidence status: PRIMARY_EVIDENCE_PRESENT

## Opportunity decision
- PROCEED
- Rationale: High user demand and clear risk mitigation for abandonment; capability is technically feasible and high-impact.
- Evidence IDs: EVID-01, EVID-02
- Confidence and limitations: High confidence for single-device mobile draft persistence; multi-device sync out of scope.

## Solution hypotheses
| Hypothesis | Opportunity fit | Evidence | Main risk | Next test |
|---|---|---|---|---|
| Persistent draft storage (`CAP-01`) allows users to save in-progress entries and return later | Directly addresses primary abandonment cause | EVID-01: 17 of 20 participants requested save-for-later | Users leave without saving if action is not prominent | Usability test on draft action visibility |

## Assumptions
| ID | SUPPORTED / INVALIDATED / INCONCLUSIVE / UNTESTED | Evidence | Remaining uncertainty |
|---|---|---|---|
| ASSUMP-01 | SUPPORTED | EVID-01 | Optimal retention period before draft expiration |

## Experiments
| Experiment ID | Proposed / approved / authorized / running / completed | Evidence/result reference | Remaining limitation |
|---|---|---|---|
| EXP-01 | completed | Prototype test report 2026-11-13 | Tested on Android Compose only |

## Current status
- PROCEED to Product Definition.
- APPROVE EXPERIMENT PLAN means the plan is accepted; it does not authorize execution.
- Actual execution requires separate AUTHORIZE EXPERIMENT [ID] recorded in the control file.
- Do not create a Discovery Outcome while experiments are only planned.

## Human decision
- User's choice: PROCEED
- Accepted residual risks: Offline drafts stored unencrypted on device sandbox in v1
- Deferred questions: Cloud backup of drafts
- Gate 3 approval state and timestamp: fixtures/chain-probe/00_DISCOVERY_CONTROL.md (2026-11-13 14:30 Asia/Ho_Chi_Minh)
