---
name: coding-refactor-simplify
description: Use this skill when simplifying duplicated code, extracting shared modules, moving prototype bridge logic into a platform boundary, or refactoring while preserving behavior.
---

# Coding Refactor Simplify

## Purpose

Reduce complexity only when it serves the current ticket and preserves behavior.

## Workflow

1. State the behavior that must not change.
2. Identify the narrow duplication or boundary problem.
3. Refactor in the smallest slice that improves the next task.
4. Avoid changing naming, formatting, architecture, and behavior at once.
5. Run before/after validation or a representative smoke check.
6. Leave follow-up tickets for broader cleanup.

## Guardrails

- Do not refactor just because code looks imperfect.
- Do not hide behavior changes inside a refactor.
- Do not move files across ownership boundaries without a clear migration reason.

## Provenance

Local Life OS adaptation inspired by production simplification/refactoring skills, multi-harness plugin isolation, and Life OS platform-boundary work.
