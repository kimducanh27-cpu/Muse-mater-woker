# P04 — Static Diff Review

- Repository: `kimducanh27-cpu/app-adr-ui`
- Base: `main` @ `99ac2c629a5e3ecc53e45f2b923163b0593d5b6a`
- Head branch: `p04/implementation-v0.3.1`
- Head commit at review: `0ba46747a36addff2d64a6003cd005f8c6c46fec`
- Review type: static implementation diff review; not live runtime.
- Verdict: `HOLD_FOR_P0_CORRECTION`.

## Diff inventory

Compare reports 5 commits ahead, 0 behind, and 15 changed files:

| File | Change |
|---|---|
| `.agents/skills/app-flow/SKILL.md` | Schema v4 canonical CR contract appended; artifact 10 added. |
| `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md` | Control schema v4. |
| `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` | New Register v1 template. |
| `templates/04-APP-FLOW/07-FLOW-REVIEW.md` | Register/Freeze batch snapshot fields. |
| `templates/04-APP-FLOW/10-DECISION-LOG.md` | Exact enum correction only. |
| `prompts/04-APP-FLOW/01-TASK-MODEL.md` | Tab 01 sole Register writer/CR Coordinator. |
| `prompts/04-APP-FLOW/02-NAVIGATION-FLOW.md` | Tab 02 Register read-only boundary. |
| `prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md` | Tab 03 read-only snapshot/Freeze Stage A. |
| `app-flow-kit/README.md` | Artifact map, schema v4 and CR handoff summary. |
| `app-flow-kit/VERIFICATION-CHECKLIST.md` | ST-01…ST-20 + AT-01…AT-10, all NOT RUN. |
| `product/app-flow/README.md` | Active artifact 10 and schema v4. |
| `README.md` | Working artifact count 01–10; downstream eligibility summary. |
| `app-flow-kit/specs/P04-REMEDIATION-PLAN-v0.3.1.md` | Immutable source specification archive. |
| `app-flow-kit/decisions/P04-OWNER-DECISION-REGISTER-v0.3.1.md` | Owner approvals 15/15. |
| `app-flow-kit/specs/P04-IMPLEMENTATION-RECORD-v0.3.1.md` | Controlled implementation record. |

## Static checks

| Check | Result |
|---|---|
| No P03/out-of-scope files changed | PASS |
| Phase 1 bad enum token removed | PASS |
| Accidental double-prefix token absent | PASS |
| Control template schema v4 | PASS |
| No duplicate `change_requests: []` state array | PASS |
| Register v1 template exists | PASS |
| 13 business states represented | PASS |
| T01–T18 represented | PASS |
| 20 required static stress tests present | PASS — all remain NOT RUN as executions |
| 10 additional targeted tests present | PASS — all remain NOT RUN as executions |
| Event block hash preimage is computable | FAIL — P04-IMP-01 |

## Finding P04-IMP-01 — P0

The spec requires `event_block_sha256` to be included inside the Register event block (Section 4.3), while hashing the exact bytes of that same full block through `END_CRE` (Section 4.4). The hash field is therefore part of its own SHA-256 preimage. The same contradictory shape is present in the new Register template. A deterministic writer/verifier cannot satisfy both requirements.

**Required correction:** Owner must select a normative hash scheme: (A) hash the event block after replacing the self-hash field with a fixed sentinel, or (B) remove the hash field from Register event bodies and store the computed event hash only in the Control receipt. Then synchronize source spec, Register template, Control receipt contract, Skill, and tests. Do not run or claim runtime PASS until corrected.

## Final status

- Implementation branch is prepared; `main` is unchanged.
- Phases 1–5 are implemented as documentation/template/contract changes.
- Phase 6 is blocked by P04-IMP-01.
- Phase 7 runtime remains NOT RUN.
- No merge is authorized.
