#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-register.py.

Tests:
  1. Valid single-event sample (fixtures/probe-9) with --h-init -> PASS (exit 0)
  2. Valid multi-event sample (2 contiguous blocks) -> PASS (exit 0)
  3. Planted failure 1: Modified header with --h-init mismatch -> FAIL (exit 1)
  4. Planted failure 2: Broken chain link on second event -> FAIL (exit 1)
  5. Planted failure 3: Tampered event block content -> FAIL (exit 1)
  6. CLI argument check -> exit 2
"""

import hashlib
import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-register.py"
PROBE9_REG = REPO / "fixtures" / "probe-9" / "product" / "app-flow" / "10_CHANGE_REQUEST_REGISTER.md"
PROBE9_H_INIT = "1317723c5003d26f40ab279aeeb55aa9264505e4c8a1cabbee213f634c21766f"


def run_validator(reg_path: pathlib.Path, h_init: str = None) -> tuple[int, str]:
    cmd = [sys.executable, str(VALIDATOR), str(reg_path)]
    if h_init:
        cmd.extend(["--h-init", h_init])
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, proc.stdout + proc.stderr


def run_validator_bytes(data: bytes, h_init: str = None) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile("wb", suffix=".md", delete=False) as f:
        f.write(data)
        tmp_path = pathlib.Path(f.name)
    try:
        return run_validator(tmp_path, h_init)
    finally:
        tmp_path.unlink(missing_ok=True)


def build_cre_block(event_id: str, seq: int, prev_hash: str) -> bytes:
    lines = [
        f"### {event_id}",
        f"change_request_event_id: {event_id}",
        "change_request_id: CR-001",
        f"register_seq: {seq}",
        "event_type: CR_TRIAGED",
        "from_status: RECORDED",
        "to_status: TRIAGED",
        "exact_user_command: TRIAGE APP FLOW CHANGE CR-001",
        "recorded_by_tab: TAB_01",
        "timestamp_local: 2026-11-12T18:15:00+07:00",
        "submission_id: SUB-001",
        "submission_payload_sha256: NOT_APPLICABLE",
        "source_process: NOT_APPLICABLE",
        "source_initiative_id: NOT_APPLICABLE",
        "source_artifact_path: NOT_APPLICABLE",
        "source_artifact_sha256: NOT_APPLICABLE",
        "affected_gate: NOT_APPLICABLE",
        "affected_artifact_paths: []",
        "control_state_seq_before_append: NOT_APPLICABLE",
        "control_file_sha256_before_append: NOT_APPLICABLE",
        f"previous_register_sha256: {prev_hash}",
        "transition_evidence: {}",
        "event_block_sha256: <HASH_OMITTED>",
        "event_end_marker: END_CRE\n",
    ]
    preimage = "\n".join(lines)
    digest = hashlib.sha256(preimage.encode("utf-8")).hexdigest()
    return preimage.replace("<HASH_OMITTED>", digest).encode("utf-8")


def test_suite() -> bool:
    all_ok = True
    base_raw = PROBE9_REG.read_bytes()

    # 1. Valid single-event sample
    print("--- Test 1: Valid single-event sample with --h-init ---")
    rc, out = run_validator(PROBE9_REG, PROBE9_H_INIT)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "PASS" not in out:
        print("FAIL: Expected rc=0 with PASS")
        all_ok = False
    else:
        print("OK: Valid single-event sample passed.")
    print()

    # 2. Valid multi-event sample (append CRE-0002)
    print("--- Test 2: Valid multi-event sample (2 blocks) ---")
    sep = b"\n"
    h_before_cre2 = hashlib.sha256(base_raw + sep).hexdigest()
    cre2_bytes = build_cre_block("CRE-0002", 2, h_before_cre2)
    full_2events = base_raw + sep + cre2_bytes
    rc, out = run_validator_bytes(full_2events, PROBE9_H_INIT)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "2 event block(s) verify" not in out:
        print("FAIL: Expected 2 event blocks to verify cleanly")
        all_ok = False
    else:
        print("OK: Multi-event chain verified.")
    print()

    # 3. Planted failure 1: Modified header with --h-init mismatch
    print("--- Test 3: Planted failure 1 (Modified header vs --h-init) ---")
    bad_header = base_raw.replace(
        b"# Process 04 \xe2\x80\x94 Change Request Register v1",
        b"# Process 04 \xe2\x80\x94 Tampered Header",
    )
    rc, out = run_validator_bytes(bad_header, PROBE9_H_INIT)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "initial header hash is" not in out:
        print("FAIL: Expected initial header hash mismatch error")
        all_ok = False
    else:
        print("OK: Caught header tampered error")
    print()

    # 4. Planted failure 2: Broken chain link on CRE-0002
    print("--- Test 4: Planted failure 2 (Broken chain link on CRE-0002) ---")
    broken_cre2 = build_cre_block("CRE-0002", 2, "0" * 64)
    full_broken_link = base_raw + sep + broken_cre2
    rc, out = run_validator_bytes(full_broken_link, PROBE9_H_INIT)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "previous_register_sha256 is '0000" not in out:
        print("FAIL: Expected broken previous_register_sha256 error")
        all_ok = False
    else:
        print("OK: Caught broken chain link")
    print()

    # 5. Planted failure 3: Tampered event block content
    print("--- Test 5: Planted failure 3 (Tampered event block content) ---")
    tampered_block = base_raw.replace(b"CR_RECORDED", b"CR_TAMPERED")
    rc, out = run_validator_bytes(tampered_block, PROBE9_H_INIT)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "event_block_sha256 does not verify" not in out:
        print("FAIL: Expected event_block_sha256 verification failure")
        all_ok = False
    else:
        print("OK: Caught tampered event block")
    print()

    # 6. CLI argument check
    print("--- Test 6: CLI argument check ---")
    proc = subprocess.run([sys.executable, str(VALIDATOR)], capture_output=True, text=True)
    if proc.returncode != 2:
        print(f"FAIL: Expected rc=2, got {proc.returncode}")
        all_ok = False
    else:
        print("OK: CLI argument check passed.")
    print()

    if all_ok:
        print("ALL TESTS PASSED: Two-sided verification complete.")
        return True
    else:
        print("SOME TESTS FAILED.")
        return False


if __name__ == "__main__":
    success = test_suite()
    sys.exit(0 if success else 1)
