---
name: coding-debugging
description: Use this skill when fixing a failing command, UI bug, broken endpoint, parsing problem, flaky behavior, provider failure, or agent run failure.
---

# Coding Debugging

## Purpose

Fix bugs by reproducing and isolating the cause before changing code.

## Workflow

1. Reconstruct the reported failure and expected behavior.
2. Reproduce with the smallest command, browser action, API call, or fixture available.
3. Identify the failing contract: parser, state transition, UI event, data shape, permission, provider transport, or validation command.
4. Make one causal fix with minimal blast radius.
5. Add or update a regression check when practical.
6. Rerun the failing check and any nearby validation.

## Output

```text
Failure:
Root cause:
Fix:
Regression check:
Validation:
Remaining risk:
```

## Guardrails

Do not paper over the symptom with broad exception handling unless the ticket is explicitly about resilience.

## Provenance

Local Life OS adaptation inspired by debugging/recovery patterns in production engineering skill packs and QA/debugger subagent taxonomies.
