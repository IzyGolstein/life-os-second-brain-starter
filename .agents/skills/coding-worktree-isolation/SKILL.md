---
name: coding-worktree-isolation
description: Use this skill when starting risky or multi-step open-source implementation work that should be isolated from the current dirty workspace or developed on a separate branch.
---

# Coding Worktree Isolation

Adapted from the archive `using-git-worktrees` skill.

## Use

Use an isolated worktree when:

- the current workspace is dirty with unrelated user changes;
- the task is a multi-step feature;
- multiple agents or branches may work in parallel;
- rollback should be easy.

## Workflow

1. Check for existing worktree conventions: `.worktrees/`, `worktrees/`, repo docs.
2. Verify any project-local worktree directory is ignored by Git.
3. Create a branch with the repository's branch naming convention.
4. Run the minimal setup and baseline verification.
5. Report the worktree path and baseline status.

## Safety

Do not create or remove worktrees destructively without explicit user intent.
Do not proceed from a failing baseline without reporting the failure.
