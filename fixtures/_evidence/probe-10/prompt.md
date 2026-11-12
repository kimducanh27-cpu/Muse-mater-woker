You are Tab 01 of Process 05. Workspace root is `fixtures/probe-10/`; every `product/` path resolves inside it.

Read, in this order:
1. `.agents/skills/ux-design/SKILL.md`
2. `fixtures/probe-10/product/ux-design/00_UX_CONTROL.md`
3. `fixtures/probe-10/product/app-flow/APP_FLOW.md`
4. `fixtures/probe-10/product/definition/PRODUCT_DEFINITION.md`
5. `templates/05-UX-DESIGN/01-SCREEN-UX-MODEL.md`

Produce `fixtures/probe-10/product/ux-design/01_SCREEN_UX_MODEL.md` using that template. One entry per SCREEN ID in the frozen flow. Preserve every template heading and column.

**Before you report anything, run this and paste its output verbatim:**

```
python test-harness/validate-ux-model.py fixtures/probe-10/product/ux-design/01_SCREEN_UX_MODEL.md fixtures/probe-10/product/app-flow/APP_FLOW.md
```

If it does not print PASS, fix the artifact and run it again. Do not report success on a FAIL.

Reply in at most 8 lines: the validator output, and how many attempts it took.
