# SECURITY_REVIEW — Independent Security Gate (v3.0)

## 1. Authority and independence

This document is the single source of truth for the mandatory security review gate.
It applies to every Phase 2 component and Phase 3 screen task, and to any task changing
authentication, authorization, data handling, dependencies, secrets, network boundaries,
build/release configuration, or deployment behavior.

The Security Reviewer is an independent, fresh-context, read-only auditor. It MUST NOT
edit source code, tests, configuration, lockfiles, snapshots, baselines, or evidence.
Grant read-only repository access and only the tools required to inspect the diff and
run non-mutating checks. If a check would mutate the worktree, use a disposable copy
or report BLOCKED.

The Security Reviewer has an independent veto. Master, Worker, and other reviewers
cannot waive or reinterpret a security FAIL. Only a named human owner can adjudicate
a finding after remediation and a new independent review. Confirmed critical
vulnerabilities and exposed credentials cannot be waived by an ordinary exception.

## 2. Dispatch point and required inputs

Dispatch after implementation and before final arbitration in both Phase 2 and Phase 3.
Dispatch again after every remediation that changes the audited head.

Inputs: task identifier and phase; base SHA and exact head SHA; complete changed-path
list and diff; relevant design/component/screen contracts; this policy; risk
classification; available scan configuration and prior finding identifiers.

The dispatch itself is mandatory. If the environment cannot dispatch an independent
reviewer, record BLOCKED and stop; do not simulate a reviewer result.

## 3. Mandatory review domains

Review all applicable domains and explicitly mark each PASS, FAIL, or BLOCKED:

1. Secrets: committed credentials, API keys, access tokens, private keys, certificates,
   sensitive environment files, and secret-bearing logs.
2. Dependencies: known vulnerable direct/transitive dependencies, untrusted sources,
   lockfile integrity, unsupported packages.
3. Static/code security: injection, unsafe deserialization, path traversal, command
   execution, insecure cryptography, unsafe storage/logging, data exposure.
4. Authentication/authorization: server/API enforcement, role and tenant boundaries,
   object/resource-level authorization, privilege escalation. UI route guards alone
   are not authorization.
5. Network/mock boundaries: production code must not silently rely on test mocks;
   mock endpoints/credentials must not ship; validate trust boundaries and transport.
6. Build/release configuration: debug flags, signing material, artifact provenance,
   workflow permissions, untrusted workflow inputs, unsafe deployment permissions.

A domain may be NOT_APPLICABLE only with an evidence-backed rationale. A missing
scanner/configuration, skipped check, unavailable required tool, or untested applicable
domain is BLOCKED, never PASS. Pattern matching alone does not prove security.

## 4. Required machine-readable evidence

Write `.agy/security-review.json` and a human-readable report. The JSON minimum
contract is:

```json
{
  "schema_version": "1.0",
  "task_id": "string",
  "phase": 2,
  "base_sha": "40-hex-commit",
  "head_sha": "40-hex-commit",
  "changed_paths": ["path"],
  "reviewer_id": "independent-reviewer",
  "reviewed_at": "RFC3339 timestamp",
  "status": "PASS|FAIL|BLOCKED",
  "checks": [
    {
      "domain": "secrets|dependencies|static-code|authorization|network-mock|build-release",
      "status": "PASS|FAIL|BLOCKED|NOT_APPLICABLE",
      "tool": "tool and version",
      "command": "exact command or procedure",
      "exit_code": 0,
      "evidence": "path or report reference",
      "rationale": "short explanation"
    }
  ],
  "findings": [
    {
      "id": "stable finding id",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW|INFO",
      "path": "repository path",
      "location": "line or symbol",
      "description": "evidence-backed description",
      "recommendation": "remediation",
      "status": "OPEN|RESOLVED|ACCEPTED"
    }
  ],
  "report_path": ".agy/security-review.md"
}
```

These values are schema guidance, not evidence. The artifact is valid only if head_sha
matches the current audited commit, all required checks are present, and every result
has supporting evidence. Never include secret values in reports.

## 5. Decision and veto rules

- PASS: every applicable mandatory domain passed, evidence is complete/current, and
  no unresolved finding remains.
- FAIL: one or more checks failed or an unresolved security finding exists.
- BLOCKED: dispatch, tool, input, configuration, evidence, or domain coverage is
  missing, stale, malformed, or incomplete.
- Security FAIL/BLOCKED blocks integration, merge, release, and final PASS.
- Remediation invalidates the prior report. Dispatch a new reviewer against the new
  exact head SHA; do not edit the previous report to manufacture a PASS.
- A resolved finding requires a linked remediation commit and verification evidence.
- Security veto is independent of defect severity and ordinary Master arbitration.

## 6. Risk classification is separate from defect severity

Classify change risk separately using changed paths, data sensitivity, privilege
boundaries, blast radius, and release impact. A small authentication change can be
HIGH risk; a large isolated visual change can be LOW risk. Recompute after scope
expansion. LOW changes may complete autonomously only after all gates pass. MEDIUM
requires at least one human approval. HIGH requires explicit owner approval and the
project's stricter approval rule. AI agents never count as human approvers.

## 7. Evidence retention

Keep the machine-readable result, human-readable report, exact diff reference,
base/head SHAs, scan logs, and finding/remediation links as durable task artifacts.
Do not store raw credentials, personal data, or secret-bearing scanner output.
