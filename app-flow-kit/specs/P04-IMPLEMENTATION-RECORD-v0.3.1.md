# P04 Implementation Record — v0.3.1

**Repository:** `kimducanh27-cpu/app-adr-ui`  
**Approved specification:** P04 Remediation Plan v0.3.1  
**Owner decisions:** ADR-P04-01…ADR-P04-10 and CL-01…CL-05 — ALL APPROVED  
**Implementation authorization:** GRANTED on 2026-11-12 by explicit Owner instruction.  
**Merge authorization:** NOT GRANTED.  
**Runtime verification:** NOT RUN.

## Controlled inputs

| Input | SHA-256 / identity |
|---|---|
| P04 Remediation Plan v0.3.1 | `cb982ff1ed2592ea44e8e5173c887b32143b13023c91553ee013ab4839cc32c6` |
| Owner Decision Register intake | `e7c343742d2b7fdae9f015b4604a11c7598ee9451c38ea0a2c73910389166d69` |
| Verified `main` baseline | `99ac2c629a5e3ecc53e45f2b923163b0593d5b6a` |
| Implementation branch | `p04/implementation-v0.3.1` |

## Execution boundaries

1. All implementation commits are on `p04/implementation-v0.3.1`; `main` remains unchanged.
2. Phase 1 Decision Log token correction is an isolated commit.
3. P03 templates, prompts, Skill and schema v2 are strictly out of scope.
4. Active P04 Control/Register state is not initialized because no initiative-specific verified P03 source and initiative ID were supplied. Only reusable P04 contracts/templates are changed.
5. Static verification inspects the exact branch diff and all schema/event/state references.
6. Live Antigravity tests (six minimum end-to-end flows, v3→v4 migration and invalid recovery) remain NOT RUN until executed in the actual Windows workspace with evidence.
7. A Draft PR may be opened for review; no merge or auto-merge is authorized.

## Phase record

| Phase | Scope | Status |
|---|---|---|
| 0 | Owner decisions and implementation authority | COMPLETE — 15/15 approved |
| 1 | Decision Log enum correction | COMPLETE — isolated commit |
| 2 | Control v4 + Register v1 | COMPLETE — static content created |
| 3 | Canonical Skill + Review snapshot | COMPLETE — static content updated |
| 4 | Three P04 prompts | COMPLETE — permission overlays added |
| 5 | README/checklist/spec/decision record | COMPLETE — source plan and 15/15 Owner approvals archived |
| 6 | Static verification + independent diff review | COMPLETE — P04-IMP-01 resolved by ADR-P04-11 (sentinel normalization) |
| 7 | Windows Antigravity runtime and Owner merge approval | NOT RUN / NOT AUTHORIZED |

## Commits

- Phase 1: `16861152249e2c2983d8f067f677e32e22068db2`
- Phase 2: `47b7777e9fdbc3c45bcea2f62ced86cfcbf9ad5f`
- Phase 3: `d32c819e469bd483e2c32d47b53c2c720b3d98c4`
- Phase 4: `086885fa11625768559c63a43d23c73994c089ea`
- Phase 5: `0ba46747a36addff2d64a6003cd005f8c6c46fec`
- Phase 6 static finding report: `dd153e5198d98a4d3e5062879ab779c19de68cf9`

## Open verification

- Validate the complete tree and diff against the v0.3.1 impact matrix.
- Confirm all 20 ST cases and the targeted cases are present and NOT RUN.
- Confirm no P03/out-of-scope path changed.
- Run the independent DIFF-ONLY Hard Review on the actual branch diff.
- Execute live Windows Antigravity runtime tests before any merge decision.

## Static verification result — 2026-11-12

- Compare `main` → `p04/implementation-v0.3.1`: 5 commits ahead, 0 behind, 15 changed files.
- No changed file is in P03 or another excluded process.
- Phase 1 exact-token check: one legacy `decision_event_kind: STATUS_CHANGED` corrected; zero remaining exact occurrences in affected canonical Skill/Decision Log; no `DECISION_DECISION_STATUS_CHANGED`.
- Control template: schema v4; no `change_requests: []` duplicate CR state.
- Register template: schema v1; 13 business states; T01–T18 present.
- Verification checklist: 22 ST scenarios + 10 targeted AT scenarios, all NOT RUN.
- Owner decisions: 11/11 ADR + 5/5 CL recorded APPROVED.
- Live Antigravity runtime: NOT RUN.

## P0 blocker P04-IMP-01 — RESOLVED by ADR-P04-11

**Resolution (2026-11-12):** the Owner approved model 1, sentinel normalization. `event_block_sha256` is now defined over the event block with that field's value replaced by the literal `<HASH_OMITTED>`; writers hash the normalized block and then write the digest, readers substitute the same sentinel before recomputing. The rule is stated normatively in `.agents/skills/app-flow/SKILL.md` and `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md`, and recorded as ADR-P04-11 in `app-flow-kit/decisions/P04-OWNER-DECISION-REGISTER-v0.3.1.md`.

The remediation plan file is deliberately not rewritten, because it is an approved artifact with a recorded SHA-256. Its Section 4.4 preimage rule is superseded for this field by reference only.

This closes the specification defect. It does not close the implementation gap: no Register writer exists, so the sentinel rule has never been executed against a real workspace. Runtime verification remains NOT RUN, and the gate for Phase 7 is unchanged.

The original finding is preserved below unaltered.

**Evidence:** The approved specification requires each Register event body to contain `event_block_sha256` (Section 4.3) and defines that hash as SHA-256 of the exact bytes from `### CRE-<NNNN>` through the LF after `event_end_marker: END_CRE` (Section 4.4). The hash field itself lies inside that byte range. The Register v1 template reproduces both requirements.

**Why this blocks implementation:** To calculate the field value, the exact event bytes depend on the hash value being calculated. This creates a self-referential preimage with no deterministic ordinary SHA-256 construction. Therefore no conforming writer or reader can calculate and verify the specified event hash as written.

**Required Owner resolution (choose one normative model):**

1. **Preferred minimal correction:** Define the hash preimage as the canonical event block with the `event_block_sha256` value replaced by a fixed sentinel (for example `event_block_sha256: <HASH_OMITTED>`). Writers hash that normalized preimage, then write the digest into the field. Readers apply the same normalization before recomputing. This preserves the field and receipt structure but changes the 'exact bytes' rule.
2. **Alternative:** Remove `event_block_sha256` from Register event bodies and store it only in the Control receipt, calculated over the exact Register event bytes excluding any self-hash field. This changes the event schema and receipt contract more substantially.

The Owner approved model 1 on 2026-11-12 and the Skill and template are aligned to it, so the specification precondition above is satisfied. What remains is unchanged: no Register writer, migration routine or runtime hash test is implemented, and Phase 7 stays NOT RUN until live Windows evidence exists. Existing contract/template edits remain on the dedicated branch for review; `main` is unchanged.

## Review handoff

- Draft Pull Request: [#1 — P04 v0.3.1 implementation](https://github.com/kimducanh27-cpu/app-adr-ui/pull/1)
- PR status: OPEN / DRAFT / DO NOT MERGE. The P0 specification blocker is resolved; merge is still not authorized by the Owner, and runtime verification has not run.
- Static diff review record: `app-flow-kit/reviews/P04-STATIC-DIFF-REVIEW-2026-11-12.md`.
- Required next decision: none at specification level. The remaining gate is Owner merge authorization plus live Windows runtime evidence.
