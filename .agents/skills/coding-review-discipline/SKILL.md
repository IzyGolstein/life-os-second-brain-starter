---
name: coding-review-discipline
description: Use this skill when requesting, receiving, or acting on code review feedback for open-source development, especially when feedback may be incomplete, overbroad, or technically questionable.
---

# Coding Review Discipline

Adapted from the archive `requesting-code-review` and `receiving-code-review` skills.

## Requesting Review

When a change is non-trivial:

1. Summarize what changed and why.
2. Provide exact files, diff range, or branch comparison.
3. State requirements and verification already run.
4. Ask for bugs, regressions, missing tests, security issues, and overengineering.

Do not ask a reviewer to infer the task from chat history.

## Receiving Review

For each review item:

1. Restate the technical requirement.
2. Verify it against the current codebase.
3. Decide whether it is correct, unnecessary, or conflicting.
4. Fix one item at a time and verify.
5. Push back with evidence when the suggestion is wrong or YAGNI.

Avoid performative agreement. Technical correctness decides.
