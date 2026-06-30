---
name: coding-code-review
description: Use this skill when reviewing agent-generated code, user diffs, completed tickets, pull-request-style changes, or any patch before adoption.
---

# Coding Code Review

## Purpose

Review patches like a senior engineer: bugs and risks first, summary second.

## Workflow

1. Read the ticket/acceptance criteria and changed files.
2. Check behavior correctness, missing edge cases, regressions, tests, security, permissions, and maintainability.
3. Verify validation evidence; if absent, mark residual risk.
4. Lead with concrete findings tied to file/line references.
5. Keep praise and broad summaries out of the findings section.

## Output

```text
Findings:
Open questions:
Validation reviewed:
Residual risk:
Change summary:
```

## Guardrails

Do not approve a patch only because it looks plausible. Do not ask for stylistic rewrites unless they affect correctness, maintainability, or local conventions.

## Provenance

Local Life OS adaptation inspired by Addy Osmani code-review skills, Microsoft code-review prompts, VoltAgent reviewer roles, and Life OS review rules.
