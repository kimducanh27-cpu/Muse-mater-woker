#!/usr/bin/env python3
"""Verify a Process 04 Change Request Register v1 hash chain.

The Register stores, inside each event block, a hash of that same block. The
preimage is normalised by replacing the field's value with the sentinel
`<HASH_OMITTED>` (ADR-P04-11). Without this check, an agent can write a
plausible digest, report success, and nothing will ever notice.

Usage: python test-harness/validate-register.py <register-file> [--h-init <hex>]
Exit:  0 = chain verifies, 1 = chain broken, 2 = cannot evaluate
"""

import hashlib
import pathlib
import re
import sys

SENTINEL = "<HASH_OMITTED>"
# A block start must be the whole line and must carry a real ID. Matching the
# bare string `### CRE-` also hits the phrase inside prose and inside the
# template's own schema example, which produces a block that begins mid-sentence.
BLOCK_START = re.compile(r"^### CRE-(?!<)[A-Za-z0-9-]+$", re.M)
END_MARKER = "event_end_marker: END_CRE\n"


def blocks(text: str) -> list[str]:
    out = []
    for m in BLOCK_START.finditer(text):
        i = m.start()
        j = text.find(END_MARKER, i)
        if j < 0:
            raise ValueError(f"block at offset {i} has no end marker")
        out.append(text[i : j + len(END_MARKER)])
    return out


def field(block: str, name: str) -> str | None:
    m = re.search(rf"^{re.escape(name)}: (.+)$", block, re.M)
    return m.group(1).strip() if m else None


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    path = pathlib.Path(sys.argv[1])
    raw = path.read_bytes()

    if b"\r" in raw:
        print("FAIL  file contains CR bytes; Register v1 requires LF only")
        return 1

    text = raw.decode("utf-8")
    if text.startswith("\ufeff"):
        print("FAIL  file starts with a BOM")
        return 1

    try:
        evs = blocks(text)
    except ValueError as exc:
        print(f"FAIL  {exc}")
        return 1

    if not evs:
        print("NOTE  no event blocks; header-only register")
        return 0

    expected_prev = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--h-init" else None
    failures = 0

    for n, block in enumerate(evs, start=1):
        seq = field(block, "register_seq")
        stored = field(block, "event_block_sha256")
        prev = field(block, "previous_register_sha256")
        cre = field(block, "change_request_event_id") or "?"

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

        if expected_prev is not None and prev != expected_prev:
            print(f"FAIL  {cre}: previous_register_sha256 is {prev!r}, expected {expected_prev!r}")
            failures += 1
        expected_prev = stored

    if failures:
        print(f"\n{failures} failure(s) across {len(evs)} event block(s)")
        return 1

    print(f"PASS  {len(evs)} event block(s) verify, chain links are contiguous")
    return 0


if __name__ == "__main__":
    sys.exit(main())
