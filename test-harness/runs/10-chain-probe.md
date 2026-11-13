# Chain Probe Run Report — 2026-11-13

## Chain probe

### 1. Thread
`CAP-01 — the user can save a draft and return to it later`
The capability enables mobile application filers to explicitly save incomplete multi-step form progress locally and resume later without loss of work or session disruption.

---

### 2. Artifacts and SHA-256 Hashes

All artifacts were generated exclusively under `fixtures/chain-probe/` using canonical templates from `templates/`. Every artifact contains the required header line `> SIMULATED — NOT ELIGIBLE DOWNSTREAM`.

Approvals across all control files and candidates were recorded as `SIMULATED_APPROVED` (and `SIMULATED_VERIFIED` for handoffs) rather than real gate approvals, adhering strictly to the harness substitution rule.

#### Core Process Artifacts (Steps 1–6)

| Step | Process | Artifact Path | SHA-256 Hash | Thread Element |
|---|---|---|---|---|
| 1 | 01 Seed | [`01_SEED_CANDIDATE.md`](fixtures/chain-probe/01_SEED_CANDIDATE.md) | `f326d6b862a9107fb7f0d3a184a79fae626cbaac39bf00eb173d22da68fa5039` | Seed hypothesis: mobile users need explicit draft saving to prevent form abandonment |
| 2 | 02 Discovery | [`07_DISCOVERY_DECISION.md`](fixtures/chain-probe/07_DISCOVERY_DECISION.md) | `4e440fcb2e11ea84cf1cd317785778d813cc6b7e760b2eec46a72f43a8a3ed56` | Opportunity decision: `PROCEED` on `CAP-01` supported by primary interview evidence |
| 3 | 03 Definition | [`PRODUCT_DEFINITION.md`](fixtures/chain-probe/PRODUCT_DEFINITION.md) | `2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075` | Product Definition: `CAP-01` admitted to frozen capability scope (`IN` table) |
| 4 | 04 App Flow | [`04_SCREEN_INVENTORY.md`](fixtures/chain-probe/04_SCREEN_INVENTORY.md) | `5379b4799753ee50f7af4953c6fcfe54493fc8d6e8ee42830c0f7c6d72fe40f6` | Screen inventory: `SCREEN-01` (Draft Editor) serves `CAP-01` with terminal node `NODE-02` |
| 5 | 05 UX Design | [`01_SCREEN_UX_MODEL.md`](fixtures/chain-probe/01_SCREEN_UX_MODEL.md) | `286c714d74ab555d295e71765fde3de216a73ced8b764dbba6365d3ba3191b9a` | UX Model: `SCREEN-01` user goal, exactly one primary action (`Save draft`), hierarchy & structure |
| 6 | 06 Design Systems | [`03_COMPONENT_INVENTORY.md`](fixtures/chain-probe/03_COMPONENT_INVENTORY.md) | `f35453b8520015593c1bfa3c409a2e4c7bdc9269b1f9cd332b4ec137805dc921` | Component inventory: `CMP-01` (Draft Save Control) citing `SCREEN-01` with token anatomy |

#### Accompanying Canonical Control Files

| Step | Process | Control File Path | SHA-256 Hash | Recorded Hash Content |
|---|---|---|---|---|
| 2 | 02 Discovery | [`00_DISCOVERY_CONTROL.md`](fixtures/chain-probe/00_DISCOVERY_CONTROL.md) | `76cbd03c895f96cadfe19017773b1f5d07c99ec18f9b5d2ace7af7d3594e5d53` | None (Process 02 schema lacks hash fields) |
| 3 | 03 Definition | [`00_PRODUCT_DEFINITION_CONTROL.md`](fixtures/chain-probe/00_PRODUCT_DEFINITION_CONTROL.md) | `340aaacf2de81e2f117bfec553ea47ee8593fb80b7af2de287bcc5624135484d` | `gate_3.frozen_artifact.sha256`: `2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075` |
| 4 | 04 App Flow | [`00_APP_FLOW_CONTROL.md`](fixtures/chain-probe/00_APP_FLOW_CONTROL.md) | `bede5acf5a602f2657ef1effdff74e9e49b1b094bed6cb828c101826a1f53742` | `source_process_03.frozen_artifact_sha256`: `2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075`<br>`gate_3.frozen_artifact.sha256`: `5379b4799753ee50f7af4953c6fcfe54493fc8d6e8ee42830c0f7c6d72fe40f6` |

---

### 3. The Closure Audit Table

| Link | From | To | Closed? | Evidence |
|---|---|---|---|---|
| L1 | Seed hypothesis (`01_SEED_CANDIDATE.md`) | Discovery decision (`07_DISCOVERY_DECISION.md`) | `ASSERTED` | Traceable by capability intent (`CAP-01`), but Process 01 has no canonical control state file and Process 02 records no SHA-256 for upstream artifacts. A modification to `01_SEED_CANDIDATE.md` cannot be detected by Process 02. |
| L2 | Discovery decision (`07_DISCOVERY_DECISION.md`) | `CAP-01` in approved scope (`PRODUCT_DEFINITION.md`) | `ASSERTED` | `PRODUCT_DEFINITION.md` incorporates `CAP-01` citing `EVID-01`, but `00_DISCOVERY_CONTROL.md` records zero hashes. `00_PRODUCT_DEFINITION_CONTROL.md` verifies the handoff via string comparison (`discovery_decision: "PROCEED"`, `source_gate_3_status: "APPROVED"`), not byte verification. Edits to `07_DISCOVERY_DECISION.md` cannot be detected by Process 03. |
| L3 | `CAP-01` in approved scope (`PRODUCT_DEFINITION.md`) | at least one screen (`04_SCREEN_INVENTORY.md`) | `CLOSED` | `SCREEN-01` explicitly references `CAP-01`. `00_PRODUCT_DEFINITION_CONTROL.md` records `gate_3.frozen_artifact.sha256` (`2e6b6c6d...`), which `00_APP_FLOW_CONTROL.md` verifies against disk bytes (`verified_file_sha256 == frozen_artifact_sha256`). Any file change breaks the gate. |
| L4 | Screen (`04_SCREEN_INVENTORY.md`) | UX model entry (`01_SCREEN_UX_MODEL.md`) | `CLOSED` | `01_SCREEN_UX_MODEL.md` defines `SCREEN-01` with exactly one primary action (`Save draft`) and passes mechanical validator `validate-ux-model.py` with zero errors. Byte-verifiable through Process 04 frozen artifact hash binding. |
| L5 | Screen (`01_SCREEN_UX_MODEL.md`) | at least one component (`03_COMPONENT_INVENTORY.md`) | `CLOSED` | `CMP-01` (Draft Save Control) explicitly cites `SCREEN-01`. Set check confirms 0 uncited components, 100% citing screens accounted for. Process 06 binds upstream frozen artifact hashes in `00_DS_CONTROL.md`. |
| L6 | Component (`03_COMPONENT_INVENTORY.md`) | measured contrast pair (`CP-01`) | `CLOSED` | `CMP-01` label text binds token `color.text.primary` (`#1A1C1E`) on container `color.surface.base` (`#FDFBFF`). Measured contrast ratio `15.8:1 >= 4.5:1` (WCAG 2.2 AA `PASS`), mathematically derived from token hex definitions. |
| L7 | Every hash | recorded in a Control File | `ASSERTED` | Fails end-to-end byte closure. Process 01 has no state file; Process 02 has no hash fields. Hashes are recorded in canonical Control Files only from Process 03 freeze onward (`00_PRODUCT_DEFINITION_CONTROL.md` -> `00_APP_FLOW_CONTROL.md` -> `00_UX_CONTROL.md` -> `00_DS_CONTROL.md`). |

---

### 4. Verdict per Link

| Link | Link Scope | Verdict | Summary |
|---|---|---|---|
| L1 | P01 -> P02 | `ASSERTED` | Traceable by text claim; zero hash binding or state tracking in P01/P02. |
| L2 | P02 -> P03 | `ASSERTED` | Handoff into P03 compares string values (`"PROCEED"`), not cryptographic byte hashes. |
| L3 | P03 -> P04 | `CLOSED` | `PRODUCT_DEFINITION.md` is frozen with real SHA-256 hash verified by P04 control state. |
| L4 | P04 -> P05 | `CLOSED` | Screen-to-model parity verified mechanically; upstream flow artifact is byte-bound. |
| L5 | P05 -> P06 | `CLOSED` | Component citations bound to frozen screen inventory; upstream UX spec is byte-bound. |
| L6 | P06 Component -> Contrast | `CLOSED` | Token contrast pair `CP-01` mathematically measured and audited against WCAG 2.2 AA. |
| L7 | Entire Chain Hash Coverage | `ASSERTED` | First two handoffs are unhashed strings; only downstream half (P03–P06) is byte-closed. |

---

### 5. Hypothesis Confirmation

**Verdict: `CONFIRMED`.**

The run strictly confirms the pre-stated hypothesis:
> *"The chain is verifiable from Process 03 onward and only asserted before it. Process 01 has no canonical state file, and Process 02's Control File contains no hash binding, so the handoff into Process 03 compares strings rather than bytes."*

- **Processes 01 & 02 (The Blind Zone):** Process 01 has no control file template in `templates/`. Process 02's `00_DISCOVERY_CONTROL.md` contains gate status labels and an unstructured prose event log, but completely omits file paths and SHA-256 hashes.
- **Process 02 -> Process 03 Seam (The String Bridge):** Process 03's `00_PRODUCT_DEFINITION_CONTROL.md` verifies the Process 02 handoff exclusively by inspecting string tokens (`discovery_decision: "PROCEED"`, `source_gate_3_status: "APPROVED"`). If `07_DISCOVERY_DECISION.md` is altered or replaced on disk, Process 03 continues to report `VERIFIED` as long as the string `"PROCEED"` exists.
- **Process 03 Onward (The Byte-Verifiable Chain):** Once `PRODUCT_DEFINITION.md` is frozen, its SHA-256 (`2e6b6c6d...`) is stamped into `00_PRODUCT_DEFINITION_CONTROL.md`. Process 04 actively recalculates this hash (`verified_file_sha256`) and refuses to proceed on any byte divergence. Subsequent stages (P05 and P06) inherit this cryptographic rigor.

---

### 6. Weakest Link and Required Remedy

#### The Single Weakest Link: **L2 (Process 02 Discovery -> Process 03 Definition Handoff)**

While L1 also lacks state infrastructure, L2 is materially more dangerous: **it commits the organization to product definition and engineering scope based on unverified string claims.** An editor could modify `07_DISCOVERY_DECISION.md` to alter the opportunity scope, remove counter-evidence, or fabricate user interview statistics, and Process 03's automated gate checks would remain completely oblivious.

#### What it would take to close L2:

1. **Add Cryptographic Freezing to Process 02 (`00_DISCOVERY_CONTROL.md`):**
   Upgrade `00_DISCOVERY_CONTROL.md` to schema v2, adding explicit artifact hash fields:
   ```yaml
   discovery_decision_artifact:
     path: "product/discovery/07_DISCOVERY_DECISION.md"
     sha256: "<computed-sha256>"
   frozen_outcome:
     path: "product/discovery/08_DISCOVERY_OUTCOME.md"
     sha256: "<computed-sha256>"
   ```
2. **Upgrade Process 03 Handoff Verification Contract (`00_PRODUCT_DEFINITION_CONTROL.md`):**
   Update `process_02_handoff` in `00_PRODUCT_DEFINITION_CONTROL.md` to compare hashes rather than strings:
   ```yaml
   process_02_handoff:
     source_decision_path: "product/discovery/07_DISCOVERY_DECISION.md"
     expected_sha256: "<read-from-p02-control>"
     verified_file_sha256: "<computed-from-disk>"
     status: "VERIFIED" # only valid if verified_file_sha256 == expected_sha256
   ```
3. **Automate Mechanical Verification:**
   Introduce a `validate-discovery-handoff.py` script in `test-harness/` that executes before Process 03 initialization to ensure no unhashed or mutated discovery decisions enter the definition pipeline.
