---
name: coding-red-green-tdd
description: Use this skill when implementing behavior changes or bug fixes where a focused failing test or smoke check can be written before production code.
---

# Coding Red-Green TDD

Adapted from the archive `test-driven-development` skill.

## Workflow

1. Write the smallest test or smoke check that captures the desired behavior or bug.
2. Run it and confirm it fails for the expected reason.
3. Implement the minimal code to pass.
4. Run the focused check again.
5. Run the broader relevant verification.
6. Refactor only after green.

## When A Full Unit Test Is Not Practical

Use a reproducible smoke check instead:

- API request with expected JSON;
- Playwright/browser path;
- CLI command against a fixture;
- provider dry-run or fake adapter test.

The check must still be specific enough to fail before the fix.
