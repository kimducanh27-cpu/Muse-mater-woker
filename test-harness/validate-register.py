#!/usr/bin/env python3
"""Verify a Process 04 Change Request Register v1 hash chain.

The Register stores, inside each event block, a hash of that same block. The
preimage is normalised by replacing the field's value with the sentinel
`<HASH_OMITTED>` (ADR-P04-11). Without this check, an agent can write a
plausible digest, report success, and nothing will ever notice.

Chain contiguity: For each event block, `previous_register_sha256` must equal
the exact SHA-256 digest of the entire file bytes immediately before that
event block was appended (raw[:block_start_offset]).

Usage: python test-harness/validate-register.py <register-file> [--h-init <hex>]
Exit:  0 = chain verifies, 1 = chain broken, 2 = cannot evaluate
"""

import hashlib
import pathlib
import re
import sys

SENTINEL = "<HASH_OMITTED>"
BLOCK_START_B = re.compile(rb"^### CRE-(?!<)[A-Za-z0-9-]+$", re.M)
END_MARKER_B = b"event_end_marker: END_CRE\n"


def blocks_with_offsets(raw: bytes) -> list[tuple[int, int, str]]:
    out = []
    for m in BLOCK_START_B.finditer(raw):
        i = m.start()
        j = raw.find(END_MARKER_B, i)
        if j < 0:
            raise ValueError(f"block at offset {i} has no end marker")
        end = j + len(END_MARKER_B)
        out.append((i, end, raw[i:end].decode("utf-8")))
    return out


def field(block: str, name: str) -> str | None:
    m = re.search(rf"^{re.escape(name)}: (.+)$", block, re.M)
    return m.group(1).strip() if m else None


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL  file not found: {path}")
        return 2

    raw = path.read_bytes()

    if b"\r" in raw:
        print("FAIL  file contains CR bytes; Register v1 requires LF only")
        return 1

    if raw.startswith(b"\xef\xbb\xbf"):
        print("FAIL  file starts with a BOM")
        return 1

    try:
        evs = blocks_with_offsets(raw)
    except ValueError as exc:
        print(f"FAIL  {exc}")
        return 1

    if not evs:
        print("NOTE  no event blocks; header-only register")
        return 0

    h_init = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--h-init" else None
    failures = 0

    for n, (start_offset, end_offset, block) in enumerate(evs, start=1):
        seq = field(block, "register_seq")
        stored = field(block, "event_block_sha256")
        prev = field(block, "previous_register_sha256")
        cre = field(block, "change_request_event_id") or f"CRE-{n:04d}"

        if seq != str(n):
            print(f"FAIL  {cre}: register_seq is {seq!r}, expected {n!r}")
            failures += 1

        if not stored or not re.fullmatch(r"[0-9a-f]{64}", stored):
            print(f"FAIL  {cre}: event_block_sha256 missing or not lowercase hex")
            failures += 1
            continue

        normalized = block.replace(
            f"event_block_sha256: {stored}", f"event_block_sha256: {SENTINEL}", 1
        )
        computed = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        if computed != stored:
            print(f"FAIL  {cre}: event_block_sha256 does not verify")
            print(f"        stored   {stored}")
            print(f"        computed {computed}")
            failures += 1

        # The actual bytes of the entire Register file immediately before this event was appended:
        expected_prev = hashlib.sha256(raw[:start_offset]).hexdigest()

        if prev != expected_prev:
            print(f"FAIL  {cre}: previous_register_sha256 is {prev!r}, expected {expected_prev!r}")
            failures += 1

        if n == 1 and h_init is not None and expected_prev != h_init:
            print(f"FAIL  {cre}: initial header hash is {expected_prev!r}, expected --h-init {h_init!r}")
            failures += 1

    if failures:
        print(f"\n{failures} failure(s) across {len(evs)} event block(s)")
        return 1

    print(f"PASS  {len(evs)} event block(s) verify, chain links are contiguous")
    return 0


if __name__ == "__main__":
    sys.exit(main())
