# Codex Review Protocol

Use this reference when reviewing or configuring AI-generated code changes.

## Project Contract

Before implementation:

```text
Goal:
Non-goals:
Relevant files:
Allowed write areas:
Forbidden write areas:
Acceptance criteria:
Validation command/evidence:
Stop condition:
```

## Review Gates

Reject or stop for clarification when any gate fails.

1. The task is vague and Codex is about to create architecture.
2. The diff touches unexpected files or broad file groups.
3. The change introduces a framework, service, data copy, schema, migration, workflow, auth, or secrets-related edit without approval.
4. There is no validation command and no alternative evidence.
5. The generated code is harder to review than writing a smaller slice.
6. Codex cannot explain why each touched file was necessary.
7. Existing user changes would need to be reverted or overwritten.
8. The implementation exceeded the approved file/LOC budget without stopping.
9. Codex did not identify review hotspots for the user.

## New Code Plan

Before adding new code, Codex should produce this plan and wait:

```text
Behavior contract:
Expected changed files:
Risk class:
Code budget:
Test/spec plan:
Review hotspots:
Non-goals:
Stop condition:
```

Default code budget:

```text
normal slice: <= 300 net production LOC and <= 5 touched files
unfamiliar backend slice: <= 150 net production LOC and <= 3 production files
```

Risk classes:

| Risk | Examples | Review depth |
|---|---|---|
| Green | docs, tests, small UI copy, isolated helper | Summary and validation. |
| Yellow | normal app logic, endpoint, data transform | Contract, tests, changed functions, hotspots. |
| Red | auth, permissions, payments, migrations, production data, security, CI/deploy | Stop for explicit approval and stronger review. |

## Checkpoint Packet

Every implementation slice must end with:

```text
Changed files:
Why these files:
Diff summary:
Behavior contract:
Validation command(s):
Validation result:
Evidence:
Review hotspots:
Boilerplate/skimmable areas:
Risks / uncertainty:
Unreviewed or generated areas:
Next suggested slice:
```

## Safe Default Commands

Infer from the target repo. Prefer existing scripts over invented commands.

Common examples:

```text
npm test / npm run test
npm run lint
npm run typecheck
npm run build
pytest
ruff check
mypy
cargo test
go test ./...
python3 scripts/validate_*.py
```

If dependencies are missing or network access is required, ask before installing or downloading.

## Target `AGENTS.md` Minimum

```markdown
# AGENTS.md

## Project Contract

- Goal:
- Non-goals:
- Stack:
- Main entry points:
- Source of truth:
- Generated/vendor files:

## Commands

- Install:
- Run:
- Test:
- Lint/type:
- Format:
- Build:

## Codex Rules

- Inspect and plan before ambiguous work.
- Implement one reviewable slice at a time.
- Preserve user changes.
- Prefer existing patterns.
- Avoid new frameworks, services, generated structures, broad refactors, migrations, CI/deploy/auth/security edits, and external calls unless approved.
- Run validation and stop with a checkpoint packet.

## Checkpoint Packet

- Changed files:
- Diff summary:
- Validation:
- Evidence:
- Risks:
- Next slice:
```
