---
name: coding-karpathy-guidelines
description: Use this skill when writing, reviewing, or refactoring open-source code and you need Karpathy-style guardrails against overengineering, hidden assumptions, broad edits, and unverifiable completion claims.
---

# Coding Karpathy Guidelines

Adapted from `multica-ai/andrej-karpathy-skills`.

## Use

Before touching code, apply these checks:

1. State the exact goal and success criteria.
2. Name assumptions and ambiguous requirements.
3. Prefer the smallest change that solves the observed problem.
4. Keep edits surgical: every changed line must trace to the request.
5. Match existing style before inventing abstractions.
6. Do not refactor adjacent code unless it blocks the task.
7. Verify with a real command or UI/API path before claiming success.

## Pushback

Push back when the requested change appears to:

- add speculative flexibility;
- solve a symptom without understanding the root cause;
- require a larger rewrite than the user asked for;
- conflict with repository conventions or safety rules.

Give a concrete alternative and the reason.
