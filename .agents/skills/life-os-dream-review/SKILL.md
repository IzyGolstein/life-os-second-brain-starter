---
name: life-os-dream-review
description: Use this skill when the user asks to review recent AI/Codex chats, long answers, user corrections, failures, or repo changes and turn them into candidate Life OS memory, prompt, skill, eval, or workflow improvements without silent core-memory edits.
---

# Life OS Dream Review

## Purpose

Convert interaction evidence into reviewable improvements to Life OS. This is the portable version of "dreaming": immediate memory candidates plus periodic consolidation, not unrestricted self-modification.

## When To Use

Use when the user asks for:

- dreaming;
- feedback-to-memory;
- "why was this answer bad?";
- improving future answers;
- updating skills/prompts/rules from a session;
- reviewing repeated mistakes;
- consolidating recent chats or answer packets.

## Workflow

1. Reconstruct the source event: wanted, got, gap, consequence.
2. Gather the smallest evidence set: current chat, relevant answer packet, `git diff`, validation failures, user corrections, and related Life OS files.
3. Extract candidate lessons.
4. Classify each candidate:

```text
memory type: semantic | episodic | procedural | project-state | anti-pattern | eval-case
durability: one-off | repeated | stable
risk: green | yellow | red
target file:
proposed patch:
needs the user approval:
```

5. Apply only green, low-risk updates such as answer packets, project notes, source pointers, or eval cases.
6. For `AGENTS.md`, `profile.md`, `notes/answer-contract.md`, `notes/anti-patterns.md`, and `.agents/skills/*`, propose or apply only when the user explicitly requests the edit in the current turn.
7. Run Life OS validation after edits.

## Two-Phase Memory Loop

Use two separate loops:

1. Hot-path feedback capture:
   - happens after a long answer, bad answer, correction, or rating;
   - uses `life-os-learn-from-feedback`;
   - creates a candidate, eval case, answer pointer, or small project note;
   - does not rewrite core instructions unless the user explicitly asks.
2. Dream review consolidation:
   - happens periodically or when the user asks for dreaming;
   - compares several candidates, answer packets, diffs, and repeated failures;
   - upgrades only stable patterns into `AGENTS.md`, `profile.md`,
     `notes/answer-contract.md`, `notes/anti-patterns.md`, or skills.

Do not skip from one chat correction directly into permanent profile memory
unless the user explicitly confirms that the lesson is stable.

## Token Budget

- Do not load all recent chats or all answer packets.
- Start with one source event and `git diff`.
- Use `rg` to find related rules/prompts before opening files.
- Open archives or long appendices only when provenance is necessary.
- If more than five Life OS files are needed, say why before continuing.

## Output

```text
Source reviewed:
Candidate lessons:
Applied changes:
Approval-needed changes:
Rejected candidates:
Validation:
```

## Rules

- Do not treat one emotional moment as permanent profile memory.
- Do not save secrets or private raw data.
- Do not silently change core instructions.
- Prefer a small patch to the smallest relevant file.
- Add eval cases when a failure could regress again.
