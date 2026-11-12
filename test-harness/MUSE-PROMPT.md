# Kickoff prompt for Muse

Paste everything between the rules into a fresh Muse session. Nothing else is needed — the harness document carries the detail.

## Before you paste

The repository is not in the VM. The first step below clones it, on the correct branch. `main` does **not** contain this harness, so a default clone finds nothing.

The VM may be discarded when the session ends. Copy the report out before you close the conversation.

Do not run this in a session where Muse holds your email, calendar or payment credentials. `agy` runs with permissions skipped, and a sandbox that also holds your accounts is not a sandbox.

---

You are the orchestrator for a contract probe. The worker is `agy` (Antigravity CLI) running in this VM.

Your job is **not** to build a product and **not** to run the product workflow end to end. Your job is to find out whether five process contracts refuse correctly when the evidence is wrong.

**Step 0 — get the repository.** Run:

```bash
git clone --branch pipeline/p05-p06 --depth 1 https://github.com/kimducanh27-cpu/app-adr-ui.git
cd app-adr-ui
ls test-harness/
```

You must see `MUSE-CONTRACT-PROBE.md` and `MUSE-PROMPT.md`. If you see an error, or that folder is missing, stop and report the exact error. Do not continue on the wrong branch.

Then read `test-harness/MUSE-CONTRACT-PROBE.md`. It defines the preflight, the five probes, the verdict vocabulary and the report format. Follow it exactly. Do not add probes.

Operating rules, in priority order:

1. **Never write to `product/`.** Write only under `fixtures/probe-<N>-<timestamp>/`.
2. **Never issue or simulate an approval.** No gate may be marked approved by you. If a probe needs a pre-existing approval, the fixture supplies it and the fixture is labelled `SIMULATED`.
3. **Never trust the exit code.** `agy` exits `0` on most failures. The evidence is the final result event in the stream, not the return value.
4. **Never invent a CLI flag.** Run `agy --help` and `agy models list` first, and use only flags that appear there.
5. **Record a SHA-256 for every file you write.**
6. **Keep the raw stream.** One `transcript-<probe>.jsonl` per probe. A verdict without a transcript is an assertion.

Before the first probe, report back in one message:

- the `agy` version and the model you selected
- whether credentials are present, and which mechanism (`GEMINI_API_KEY` or `settings.json` `modelProvider`)
- the repo HEAD commit
- the list of five probes you are about to run

Then run the probes in order, one at a time. Do not run two probes in the same `agy` session — Probe 3 in particular requires a clean context, because it plays an independent reviewer.

After each probe, print one line: probe number, verdict, evidence path. Continue immediately; do not ask for permission between probes.

**Part B — the chain probe.** When the five probes finish, read `test-harness/CHAIN-PROBE.md` and run it.

That suite is different in kind. The first five test whether gates refuse. Part B tests whether one capability can travel from an idea in Process 01 to a component in Process 06 without the chain losing it, and whether each handoff can be **verified** rather than believed.

It states a hypothesis before the run. Confirm or refute it; do not soften it. If the chain is only asserted at the early links, say so plainly — that is the finding the suite exists to produce.

Keep the same constraints: `fixtures/chain-<timestamp>/` only, every artifact headed `> SIMULATED — NOT ELIGIBLE DOWNSTREAM`, no contract edited, every approval written as `SIMULATED_APPROVED` and that substitution recorded.

When both suites finish, write `fixtures/probe-report-<timestamp>.md` covering both, then stop and report:

- the verdict table for the five probes
- the closure table for the chain, link by link
- every `AMBIGUOUS`, `UNEXECUTABLE`, `ASSERTED` and `BROKEN` result, with the contract clause it implicates
- whether the chain hypothesis was confirmed or refuted
- the single weakest link in the whole pipeline, and what it would take to close it
- what you could not test, and why

Finally, paste the full report into the conversation as text. The VM may not survive the session, and a report that exists only inside it is a report nobody can read.

Two things to keep straight while you work:

A `COMPLIANT` result is weak evidence. It means the agent happened to behave. An `AMBIGUOUS` or `UNEXECUTABLE` result is strong evidence, because it means the contract itself is underspecified or contradictory. Weight them accordingly and say so in the report.

You are probing a document, not a product. If a contract clause is impossible to follow, that is a successful probe, not a failed one. Report it as the finding it is.
