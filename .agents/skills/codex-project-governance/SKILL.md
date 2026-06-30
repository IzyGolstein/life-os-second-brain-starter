---
name: "codex-project-governance"
description: "Use this skill when the user wants Codex to work in an arbitrary software repository using Life OS rules: configure AGENTS.md, define development constraints, split work into reviewable slices, review agent-generated code, or set up a safe Codex collaboration process for a project."
---

# Codex Project Governance

## Purpose

Make Codex useful in software projects without letting it become an unsupervised project owner.

Use this skill when the task is about project setup, coding workflow, code review, AGENTS.md rules, AI-generated diffs, validation commands, or safe collaboration in an arbitrary repo.

## Load

1. Read target repo instructions first: `AGENTS.md`, `CLAUDE.md`, README, package/config files, test/build docs.
2. If Life OS is available, read `notes/codex-development-protocol.md`.
3. If doing detailed review or setup, read `references/review-protocol.md`.

## Core Rule

```text
Codex executes inside a bounded slice.
the user owns architecture, scope, acceptance criteria, validation standards, and merge/adoption decisions.
```

## Workflow

1. Start in exploration mode: inspect repo shape, stack, commands, git status, and existing instructions. Do not edit yet.
2. Produce a project contract: goal, non-goals, constraints, relevant files, allowed write areas, validation commands, and stop condition.
3. For adding new code, produce a new-code plan before edits: behavior contract, exact file plan, risk class, code budget, test/spec plan, review hotspots, and non-goals.
4. For ambiguous work, propose a 2-4 step plan and ask for approval of the first slice.
5. During implementation, change only the approved slice and prefer existing project patterns.
6. Run available validation: tests, lint, type checks, build, notebook/script execution, screenshot/render, or source-to-output check.
7. Stop with a checkpoint packet: changed files, behavior contract, diff summary, validation result, evidence, review hotspots, risks, and next suggested slice.

## Hard Limits

- Do not create whole-project skeletons, broad refactors, new frameworks, services, or large generated structures without explicit approval.
- Do not touch secrets, `.env`, credentials, auth, deployment, CI, or security-sensitive files unless the task explicitly requires it.
- Do not run destructive commands, reset user changes, or overwrite unrelated diffs.
- Do not install dependencies, call external services, or run migrations without approval.
- For one new-code slice, default to <= 300 net production LOC and <= 5 touched files; for unfamiliar backend, default to <= 150 net production LOC and <= 3 production files.
- If the slice exceeds the approved code budget or needs unexpected files, stop before editing further.
- If validation cannot be run, say why and mark the residual risk.

## Setup Output

When asked to configure a project for Codex, create or update a short project-local `AGENTS.md` containing:

- project goal and non-goals;
- commands for run/test/lint/type/build/format;
- source/generated/vendor boundaries;
- allowed and forbidden write areas;
- Codex working rules;
- checkpoint packet format;
- review checklist.

Do not copy the whole Life OS protocol into every project. Put only the project-specific operating rules there.

## Final Response

For implementation or setup work, report:

```text
Changed files:
Validation:
What is now enforced:
Remaining risk:
Next slice:
```
