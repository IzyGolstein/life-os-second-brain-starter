# Skill Selection Contract

Goal: give a new user enough skills to get high-quality answers without
installing a huge, noisy prompt pack.

## Policy

Use precision before recall.

- Install `core` for every user.
- Add a domain pack only when the intake explicitly names that domain or the
  first project requires it.
- Prefer small local adaptations under `.agents/skills/` over bulk external
  prompt packs.
- Record every selected skill and source pack in
  `agent-system/skills/selected.json`.
- Keep personal examples out of shared skills.
- Promote a user-customized skill to a shared catalog only after review or eval
  evidence.

## Source Repositories

External repositories are reference libraries and provenance sources:

- https://github.com/openai/skills
- https://github.com/anthropics/skills
- https://github.com/vercel-labs/agent-skills
- https://github.com/addyosmani/agent-skills
- https://github.com/microsoft/skills
- https://github.com/VoltAgent/awesome-claude-code-subagents
- https://github.com/wshobson/agents
- https://github.com/subinium/awesome-claude-code
- https://github.com/nizos/tdd-guard

Do not bulk-copy them into a user's runtime. Use them to improve local,
reviewed, compact skills.

## Selection Algorithm

1. Read the intake domains and explicit `skill_packs`.
2. Start with `core`.
3. Add domain packs from `domain_to_packs`.
4. Add explicit packs.
5. Remove duplicates while preserving order.
6. Copy only matching local skills into the generated `.agents/skills/`.
7. If a requested skill is missing locally, record it under `missing_skills` and
   do not fabricate it.

## Default Packs

The machine-readable pack file is:

```text
starter-kits/second-brain/skill-selection/starter-skill-packs.json
```

