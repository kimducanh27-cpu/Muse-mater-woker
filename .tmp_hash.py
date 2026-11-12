import hashlib

block = "### CRE-0001\n" \
"change_request_event_id: CRE-0001\n" \
"change_request_id: CR-001\n" \
"register_seq: 1\n" \
"event_type: CR_RECORDED\n" \
"from_status: NONE\n" \
"to_status: RECORDED\n" \
"exact_user_command: RECORD APP FLOW CHANGE SUBMISSION SUB-001\n" \
"recorded_by_tab: TAB_01\n" \
"timestamp_local: 2026-11-12T18:09:57+07:00\n" \
"submission_id: SUB-001\n" \
"submission_payload_sha256: NOT_APPLICABLE\n" \
"source_process: NOT_APPLICABLE\n" \
"source_initiative_id: NOT_APPLICABLE\n" \
"source_artifact_path: NOT_APPLICABLE\n" \
"source_artifact_sha256: NOT_APPLICABLE\n" \
"affected_gate: NOT_APPLICABLE\n" \
"affected_artifact_paths: []\n" \
"control_state_seq_before_append: NOT_APPLICABLE\n" \
"control_file_sha256_before_append: NOT_APPLICABLE\n" \
"previous_register_sha256: 96c9bc22637d2ece54134fb64b077801be65c9994b95dcd35f51e8daf5792222\n" \
"transition_evidence: {}\n" \
"event_block_sha256: <HASH_OMITTED>\n" \
"event_end_marker: END_CRE\n"

digest = hashlib.sha256(block.encode('utf-8')).hexdigest()
print('digest:', digest)
print('block repr:', repr(block))
