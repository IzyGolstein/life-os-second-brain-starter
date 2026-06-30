---
name: coding-repo-onboarding
description: Use this skill when starting coding work in an unfamiliar repository, adding an external repo to Life OS, preparing a Codex/OpenHands/Claude Code task, or deciding the first safe implementation slice.
---

# Coding Repo Onboarding

## Purpose

Turn an unfamiliar repo into a bounded work surface before editing.

## Workflow

1. Read repo instructions first: `AGENTS.md`, `CLAUDE.md`, README, package files, test/build docs.
2. Inspect git state and avoid overwriting unrelated user changes.
3. Identify stack, app entrypoints, source/generated/vendor boundaries, and likely validation commands.
4. Find the smallest files needed for the ticket; avoid repo-wide rewrites.
5. Write a project contract: goal, non-goals, allowed paths, validation, stop condition, and residual unknowns.

## Output

Return a compact onboarding packet:

```text
Repo:
Stack:
Important instructions:
Allowed write area:
Validation:
First safe slice:
Risks/blockers:
```

## Verification

Do not edit files until the first safe slice and validation path are clear.

## Provenance

Local Life OS adaptation inspired by OpenAI skills packaging, Microsoft role/skill catalogs, wshobson multi-harness isolation, and awesome-claude-code workflow catalogs.
