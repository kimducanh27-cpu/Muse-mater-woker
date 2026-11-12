Append one event block to `fixtures/probe-9/product/app-flow/10_CHANGE_REQUEST_REGISTER.md`.

The event block schema is in `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` under "Canonical event block schema". Follow its field names and order exactly.

Values:
- change_request_event_id: CRE-0001
- change_request_id: CR-001
- register_seq: 1
- event_type: CR_RECORDED
- from_status: NONE
- to_status: RECORDED
- exact_user_command: RECORD APP FLOW CHANGE SUBMISSION SUB-001
- recorded_by_tab: TAB_01
- timestamp_local: a real Asia/Ho_Chi_Minh timestamp
- previous_register_sha256: 96c9bc22637d2ece54134fb64b077801be65c9994b95dcd35f51e8daf5792222
- all other fields: NOT_APPLICABLE or empty list/map as the schema allows

Hash rule for `event_block_sha256`, quoted from the Skill:

> SHA-256 over the normalized event block. The preimage is the bytes from the first byte of `### CRE-<NNNN>` through the LF after `END_CRE`, excluding the following blank line, with the value of the `event_block_sha256` field replaced by the exact sentinel `<HASH_OMITTED>` before hashing.

Append the block at the end of the file, separated by exactly one blank line. Do not modify any existing byte.

**Before you report anything, run this and paste its output verbatim:**

```
python test-harness/validate-register.py fixtures/probe-9/product/app-flow/10_CHANGE_REQUEST_REGISTER.md --h-init 96c9bc22637d2ece54134fb64b077801be65c9994b95dcd35f51e8daf5792222
```

If it does not print PASS, fix the digest and run it again. Do not report success on a FAIL. Reply in at most 8 lines: the validator output, and how many attempts it took.
