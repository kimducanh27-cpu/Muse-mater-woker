> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `7432476`, 2026-11-13.

# Rules

Read this before writing anything. These are the rules that, when broken, produced the thirteen findings in `test-harness/FINDINGS.md`.

## Never

1. **Never approve on the human's behalf.** No gate may be set to `APPROVED` without the human typing the exact command. An agent that infers approval has turned the gate into decoration.
2. **Never invent a hash.** Compute it from the bytes on disk, or write `NOT_VERIFIED`. A plausible digest is worse than a missing one, because it survives review.
3. **Never write to `product/` in a probe or test.** Fixtures live under `fixtures/`. A probe that writes to the live workspace contaminates the thing it is measuring.
4. **Never report success without running the check.** If a validator exists for the artifact you just wrote, run it and paste the output. "I verified" is not evidence; a `PASS` line is.
5. **Never compare an artifact to your memory of writing it.** That comparison always passes. Compare it to an external file: a field contract, a template, a validator.
6. **Never edit a frozen artifact.** Freeze copies the reviewed draft byte-for-byte and changes one status line. Anything else is a new version through a Change Request.
7. **Never let a rewrite pass as upstream.** If you adapt an external skill, label it. See `PROVENANCE.md`: VERBATIM, ADAPTED or LOCAL.
8. **Never claim a `NOT RUN` scenario is a `PASS`.** Eleven probes have executed pieces of the machinery. None has converted a checklist scenario into evidence.
9. **Never scan a whole document when you mean one section.** This defect appeared four times in one session: `card` inside `discards`, `### CRE-` inside prose, `component` outside the list, and a validator that read the citation table as a second pattern register. A checker that reads past the end of its section measures the wrong thing, and it fails correct input.

## Always

1. **Read the Skill before acting.** Nine Skills, 2,031 lines. The one for your tab is normative; the charters and READMEs are not.
2. **Fail closed.** Missing, unreadable, mismatched or unorderable evidence yields `NOT_VERIFIED`. Never a best guess.
3. **Record a real timestamp** in `Asia/Ho_Chi_Minh`, from the clock, not from arithmetic.
4. **Quote the exact command** the human sent. `exact_user_command` is a field, not a paraphrase.
5. **Keep the raw transcript.** A verdict without one is an assertion.
6. **Delete the prose when a check replaces it.** If a validator computes six values, do not also require the agent to narrate them — two ways to comply means the cheaper one wins, and the other becomes dead weight a reader still believes is enforced.

## The checkers

Run the relevant one before claiming anything is done.

```bash
python test-harness/validate-control.py <control-file>
python test-harness/validate-register.py <register-file> --h-init <hex>
python test-harness/validate-ux-model.py <artifact-01> <app-flow>
python test-harness/validate-patterns.py <artifact-02> <app-flow>
python test-harness/apply-gate.py <control> --gate 1 --command "<exact>" --artifact <path>
```

The first four check. The fifth applies a gate and then re-checks the result. `make-fixture.py` generates probe workspaces; it is a fixture tool, not a checker.

A checker that has never failed on a known-bad input is not a checker. Every one of these was tested against a deliberately broken input before it was trusted.

## Commands the human types

These are the only strings that open a gate. An agent must not type them, suggest that they were typed, or treat a conversational "ok" as one.

| Gate | Command |
|---|---|
| P05 Gate 1 | `APPROVE SCREEN UX MODEL` |
| P05 Gate 2 | `APPROVE INTERACTION AND STATE DESIGN` |
| P05 Gate 3 | `FREEZE UX SPEC` |
| P06 Gate 1 | `APPROVE DESIGN FOUNDATIONS` |
| P06 Gate 2 | `APPROVE COMPONENT LIBRARY` |
| P06 Gate 3 | `FREEZE DESIGN SYSTEM` |

Full lists per process are in each kit README.

## How this repo grows

**Reference upstream first. Do not invent what already exists.**

The order is fixed:

1. **VERBATIM** — an upstream file fits as-is. Copy it byte-for-byte, record blob SHA, size, licence and retrieval date.
2. **ADAPTED** — an upstream file nearly fits. Copy it, then name the source and state exactly what you changed and why.
3. **LOCAL** — nothing exists upstream. Then say so, give the rationale, the risk, and what evidence would retire the rule.

Invention is not forbidden. **Unlabelled invention is.** A reader must be able to ask "where does this come from" and get an answer in one hop: a file with a blob SHA, a named standard, or an entry in the register.

Current audit of Processes 05 and 06, 23 rules: **3 verbatim, 4 adapted, 16 local.**

That number is the honest measure of this repository. Most of it is original, and the original parts are exactly the parts nobody outside has validated.

**The gap.** `PROVENANCE.md` is the one rule with no mechanical check. Three validators guard artifacts; none guards a claim about where a rule came from. A new rule added without a label is invisible — it looks like every other rule and inherits the same unearned confidence.

Until a checker exists, the discipline is manual and it belongs in the same commit as the rule: add the rule, add its label, in one change. A rule that arrives without one is a finding waiting to be filed.

## What counts as evidence

| Claim | Evidence |
|---|---|
| "The gate is approved" | Control File `status: APPROVED` **and** `approved_state_seq` equal to the event's `state_seq` |
| "The artifact is frozen" | Control File hash equals the actual file hash, recomputed |
| "The probe passed" | A `PASS` line from a validator, plus the transcript |
| "This rule came from somewhere" | A label in `PROVENANCE.md` |
| "It works" | A live run with a real workspace. Nothing in this repository currently qualifies. |
