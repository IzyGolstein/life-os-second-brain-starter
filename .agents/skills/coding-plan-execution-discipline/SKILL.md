---
name: coding-plan-execution-discipline
description: Use this skill when turning a product or engineering goal into implementation groups, sequencing work, executing a written plan, or deciding when a development slice is ready to integrate.
---

# Coding Plan Execution Discipline

Adapted from the archive `writing-plans`, `executing-plans`, and `finishing-a-development-branch` skills, rewritten for Life OS/Codex.

## Planning

For multi-step implementation, group work into independently verifiable slices:

1. Product/user workflow.
2. Data/storage contract.
3. Backend/API behavior.
4. Provider/runtime behavior.
5. UI integration.
6. Observability and evals.
7. Migration/import.
8. Deployment/ops.

For each slice define:

- files or modules likely involved;
- exact success criteria;
- test/smoke check;
- dependencies and blockers;
- whether it can ship independently.

## Execution

1. Read the plan critically before editing.
2. Work one slice at a time.
3. Keep a visible checklist.
4. Verify each slice before moving on.
5. Stop on unclear requirements or failing verification.

## Finishing

Before integration:

- rerun relevant verification;
- summarize changed behavior and residual risks;
- list migrations or operational steps;
- do not merge, push, or delete branches without explicit user intent.
