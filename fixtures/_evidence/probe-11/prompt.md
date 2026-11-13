You are Tab 01 of Process 05. Workspace root is `fixtures/probe-11/`; every `product/` path resolves inside it.

Read, in this order:
1. `.agents/skills/ux-design/SKILL.md`
2. `fixtures/probe-11/product/ux-design/00_UX_CONTROL.md`
3. `fixtures/probe-11/product/app-flow/APP_FLOW.md`
4. `fixtures/probe-11/product/definition/PRODUCT_DEFINITION.md`
5. `templates/05-UX-DESIGN/01-SCREEN-UX-MODEL.md`

**Step 1 — before writing any artifact, run:**

```
python test-harness/validate-control.py fixtures/probe-11/product/ux-design/00_UX_CONTROL.md
```

If it does not print PASS, stop and report the failure. Do not produce an artifact on a workspace that fails its own checks.

**Step 2 — produce** `fixtures/probe-11/product/ux-design/01_SCREEN_UX_MODEL.md` using the template. One entry per SCREEN ID in the frozen flow.

**Step 3 — before reporting, run:**

```
python test-harness/validate-ux-model.py fixtures/probe-11/product/ux-design/01_SCREEN_UX_MODEL.md fixtures/probe-11/product/app-flow/APP_FLOW.md
```

If it does not print PASS, fix the artifact and run it again.

Reply in at most 10 lines: the output of both validators, verbatim, and how many attempts each took.
