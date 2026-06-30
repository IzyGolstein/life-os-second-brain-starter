---
name: chat-feedback-extractor
description: Use this skill when the user asks to extract, audit, or save his feedback on an assistant answer from a chat thread, especially when prior summaries were too shallow, too broad, or mixed exact remarks with invented rules.
---

# Chat Feedback Extractor

## Purpose

Extract the user's feedback with high precision. The goal is not to collect many
phrases. The goal is to preserve the feedback that can actually improve future
answers.

## What Counts As Feedback

Include only items where the chat provides enough local context to answer all
of these:

1. What did the assistant do wrong or miss?
2. What exactly did the user say or rewrite?
3. What was the local context where the correction mattered?
4. What should the assistant do differently next time in that same kind of
   context?

If any answer is missing, do not create a durable feedback item. Put it in
"discarded / too local" only if useful.

## Required Item Format

Each saved item must use this shape:

```text
ID:
Context:
Assistant failure:
the user feedback:
Concrete example:
Future rule:
Scope:
```

Definitions:

- `Context`: the section/task where the problem happened, not a vague label.
- `Assistant failure`: behavior, not just a bad word.
- `the user feedback`: quote or close paraphrase of the user's actual feedback.
- `Concrete example`: a before/after phrase, accepted rewrite pattern, table/plot
  requirement, or chapter placement.
- `Future rule`: narrow enough that it will not misfire elsewhere.
- `Scope`: where this rule applies; avoid global word bans.

## Precision Rules

- Do not save naked word substitutions unless the local context is included.
  Example: "назначить -> назначать" is not a global grammar rule; it only matters
  where the text describes an ongoing system capability.
- Do not save ordinary task instructions as style feedback unless the user criticized
  the assistant's prior answer.
- Do not turn the user's rough spoken dictation into exact prose unless he explicitly
  says to use the exact text.
- Do not invent the assistant's bad text if the chat only contains the user's
  correction. Say "assistant context not fully visible" and anchor the item on
  the correction that is visible.
- Prefer 15-30 high-signal items over 100+ low-signal rows.
- Separate exact feedback from interpretation.

## Output Structure

When producing a feedback file:

1. `Scope And Method`
2. `High-Precision Feedback Items`
3. `Accepted Style Anchors`
4. `Discarded Or Too-Local Remarks`
5. `Checklist Before Next Draft`

## Review Gate

Before finalizing, remove any item that:

- only repeats the user's phrase without explaining context;
- would make the assistant mechanically avoid a word everywhere;
- is really a project requirement, not feedback on writing or reasoning;
- lacks a concrete example.
