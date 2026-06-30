# Optional Second Brain Context

This project may use an external private second-brain repository for durable
context, answer preferences, project memory, prompts, and skills.

Do not load the second brain by default. Use it only when the task needs
user-specific context, prior decisions, cross-project memory, selected skills,
or a saved result.

Resolve the second brain in this order:

1. `SECOND_BRAIN_PATH` environment variable.
2. An explicitly provided local path.
3. A sibling checkout such as `../<user>-brain`.
4. Ask the user for a path or private repo URL.

When second-brain context is needed, load the smallest useful set:

1. `<brain>/AGENTS.md`
2. `<brain>/profile.md`
3. `<brain>/notes/answer-contract.md`
4. one relevant `<brain>/.agents/skills/<skill>/SKILL.md`
5. one matching project, note, answer, or inbox source found with search

Never copy private second-brain files into this project. Never read secrets.
Never edit the second brain unless the user explicitly asks to save or sync a
result.

For coding tasks in this repo, follow this project's own run/test/lint/build
commands first. The second brain provides context and preferences, not hidden
source code ownership.

