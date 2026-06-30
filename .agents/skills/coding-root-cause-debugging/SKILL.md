---
name: coding-root-cause-debugging
description: Use this skill when fixing a bug, failing test, broken UI/API path, provider failure, timeout, integration issue, or unexpected behavior where guessing would risk masking the root cause.
---

# Coding Root Cause Debugging

Adapted from the archive `systematic-debugging` skill, stripped of corporate/tool-specific assumptions.

## Rule

No fix before root cause evidence.

## Workflow

1. Reproduce the failure with exact steps or command output.
2. Read the full error, stack trace, logs, HTTP response, browser console, or run artifact.
3. Check recent diffs and the nearest working implementation.
4. Trace the data flow across boundaries: UI -> API -> backend -> provider -> persisted state.
5. Form one hypothesis: "I think X fails because Y."
6. Test the hypothesis with the smallest possible observation or change.
7. Add or update a regression check when feasible.
8. Fix the root cause, then rerun the original failure path.

## Stop Conditions

Stop and report if:

- the bug is not reproducible;
- evidence points to a missing dependency or unavailable provider;
- the fix requires destructive state changes;
- you cannot tell whether the failure is local, provider-side, or user-data-specific.
