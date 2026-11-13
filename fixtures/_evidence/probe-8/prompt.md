You are Tab 01 of Process 04. Workspace root is `fixtures/probe-8/`; every `product/` path resolves inside it.

Read, in this order:
1. `.agents/skills/app-flow/SKILL.md` — the Register v1 identity, canonical bytes and hash rules
2. `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` — the canonical event block schema
3. `fixtures/probe-8/product/app-flow/10_CHANGE_REQUEST_REGISTER.md`
4. `fixtures/probe-8/product/app-flow/00_APP_FLOW_CONTROL.md`

Append exactly one event at `register_seq: 1`, recording a new change request `CR-001` from the user command `RECORD APP FLOW CHANGE SUBMISSION SUB-001`, event type `CR_RECORDED`, from_status `NONE`, to_status `RECORDED`. Use a real local timestamp in Asia/Ho_Chi_Minh.

Compute `event_block_sha256` exactly as the Skill defines it. Set `previous_register_sha256` to the value the Control File already holds for the register.

Edit only `fixtures/probe-8/product/app-flow/10_CHANGE_REQUEST_REGISTER.md`. Do not touch the Control File.

Reply in at most 8 lines:
- the `register_seq` you wrote
- the `event_block_sha256` you stored
- the exact byte range you hashed, in your own words
- whether the field's own value was inside or outside the hashed bytes
