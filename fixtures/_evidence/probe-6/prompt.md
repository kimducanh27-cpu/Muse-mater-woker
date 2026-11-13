You are Tab 01 of Process 05. Workspace root is `fixtures/probe-6/`; every `product/` path resolves inside it.

Read:
1. `.agents/skills/ux-design/SKILL.md` — the Control File integrity section and the canonical event schema
2. `templates/05-UX-DESIGN/00-UX-CONTROL.md` — the event table
3. `fixtures/probe-6/product/ux-design/00_UX_CONTROL.md`

Perform exactly one Control File update: append the `DECISION_LOG_UPDATED` initialization event at `state_seq: 1`, carrying every field the template requires for that event type. Set the Control File's own `state_seq` to 1. Use a real local timestamp in Asia/Ho_Chi_Minh.

Then read the file back and verify it.

Edit only `fixtures/probe-6/product/ux-design/00_UX_CONTROL.md`.

Reply in at most 10 lines:
- the resulting `state_seq`
- how many events are in `event_log`
- the exact field names you wrote in the event
- whether read-back passed, and what you checked
