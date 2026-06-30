---
name: life-os-learn-from-feedback
description: Use this skill when the user gives feedback on an AI answer, workflow, prompt, skill, search, coding session, or Life OS behavior and wants the lesson converted into durable improvements without silently changing core memory.
---

# Life OS Learn From Feedback

## Purpose

Convert the user's feedback into reviewable improvements: answer standards, anti-patterns, skills, prompts, eval cases, project notes, or tasks. This is the lightweight "learn from review comments" loop for Life OS.

## When To Use

Use when the user:

- rates a long answer;
- says an answer was generic, shallow, wrong, too long, too short, or token-wasteful;
- corrects a repeated assistant behavior;
- asks how to make future answers better;
- wants feedback saved from Codex, Claude, ChatGPT, Cursor, Windsurf, or another agent.

## Workflow

1. Reconstruct the feedback event:
   - what the user wanted;
   - what the model did;
   - what was missing or harmful;
   - what behavior should happen next time.
2. Gather the smallest evidence set:
   - current chat or supplied transcript;
   - relevant answer packet or prompt;
   - `git diff` only if repo behavior changed;
   - the specific Life OS files that may need a patch.
3. Classify the lesson:

```text
feedback type: content | style | context | research | coding | memory | workflow | token-budget
durability: one-off | repeated | stable
target: answer-contract | profile | anti-pattern | skill | prompt | eval-case | project-note | no-change
risk: green | yellow | red
proposed change:
needs the user approval:
```

4. Apply only green low-risk changes, such as answer packets, eval cases, project notes, and source pointers.
5. For `AGENTS.md`, `profile.md`, `notes/answer-contract.md`, `notes/anti-patterns.md`, and `.agents/skills/*`, propose the exact change unless the user explicitly asked to apply it now.
6. If the feedback is weak, emotional, or ambiguous, save it as an eval/source note only when it could prevent a future regression.
7. Run validation after edits.

## Token Budget

- Do not load all feedback history.
- Read at most one source thread, one answer packet, and three candidate target files before deciding.
- Use `rg` before opening large files.
- Do not open appendices or archives unless the feedback explicitly depends on them.

## Output

```text
Feedback source:
Root cause:
Candidate lessons:
Applied changes:
Approval-needed changes:
Rejected / not durable:
Validation:
```

## Rules

- Do not turn one bad mood into permanent profile memory.
- Do not silently change core behavior rules.
- Prefer an eval case over a broad new rule when the lesson is specific.
- Prefer editing an existing prompt/skill over creating a new one.
- Keep the lesson phrased as future observable behavior.
