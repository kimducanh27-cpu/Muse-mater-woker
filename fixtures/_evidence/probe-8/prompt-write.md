Append one event block to `fixtures/probe-8/product/app-flow/10_CHANGE_REQUEST_REGISTER.md`.

The event block schema is in `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` under "Canonical event block schema". Follow its field names and order exactly.

Values for this event:
- change_request_event_id: CRE-0001
- change_request_id: CR-001
- register_seq: 1
- event_type: CR_RECORDED
- from_status: NONE
- to_status: RECORDED
- exact_user_command: RECORD APP FLOW CHANGE SUBMISSION SUB-001
- recorded_by_tab: TAB_01
- timestamp_local: use a real Asia/Ho_Chi_Minh timestamp
- previous_register_sha256: 7252fa37d800a70714c7cafe20ff9388c91c613d30b4d406c4c4a23ed7a2bc99
- all other fields: NOT_APPLICABLE or empty list/map as the schema allows

Hash rule for `event_block_sha256`, quoted from the Skill:

> SHA-256 over the normalized event block. The preimage is the bytes from the first byte of `### CRE-<NNNN>` through the LF after `END_CRE`, excluding the following blank line, with the value of the `event_block_sha256` field replaced by the exact sentinel `<HASH_OMITTED>` before hashing. Writers hash the normalized block, then write the resulting lowercase digest into the field.

Append the block at the end of the file, separated by exactly one blank line. Do not modify any existing byte.

Reply in at most 5 lines: the digest you wrote, and the sha256 of the whole file after your edit.
