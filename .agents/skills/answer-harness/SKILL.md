---
name: answer-harness
description: Use this skill when answering the user's substantive questions from Telegram, Life OS, or chat and the answer needs research, local context, hard judgment, a compact main response, and a saved appendix. Triggers include research questions, technical ML ideas, science/psychology claims, career/geopolitics decisions, book/expert audits, and complaints that previous answers were too generic.
---

# Answer Harness

## Overview

Produce answers that feel like a strong GPT response backed by agents and research, not like a task-board summary. Use progressive disclosure: a compact chat answer plus a saved appendix when needed.

## Answer Core

Choose only the blocks needed: `question`, `judgment`, `prior_art`,
`mechanism/evidence`, `decision/test`, `save/feedback`.

Default chat answer: reconstructed question, short judgment, 2-4 non-obvious
insights, one uncertainty/falsifier, next concrete step, save pointer when
relevant.

When the user offers his own analogy, hypothesis, or partial model, carry it into
the answer and evaluate it directly. Do not silently swap it for a generic
literature frame.

## Workflow

1. Reconstruct the real question in one sentence and preserve important original wording.
2. Load `profile.md`.
3. Load `notes/playbooks.md` only if the answer shape is unclear.
4. Search active Life OS context first: `projects/`, `answers/`, `notes/`, `tasks.md`, `inbox.md`.
5. Browse current/high-stakes/unstable facts; include non-official news/community sources when the user asks about lived access, blocks, or trends.
6. Use repo skills/workflows first. Use subagents only when the runtime allows it and the user explicitly asked for delegation or parallel agents. Do not show raw logs by default.
7. Write a compact high-density answer with inline links near claims.
8. Save a pointer in `answers/YYYY-MM.md`; save a long appendix under `answers/appendices/` only when needed.
9. For long substantive answers, ask for brief feedback and flag any memory candidate that should be saved only with the user's approval.
10. Run the quality gates below before finalizing.

## Research Loop

Use one compact loop for research-grade work:

```text
question/context -> prior art -> mechanism/model -> missing evidence ->
targeted search -> completion check
```

Completion criterion: mechanism, strongest prior art, alternatives, concrete
test/work product, uncertainty/falsifier, next action. Modeling answers need the
model object, assumptions, objective or estimand, inputs, validation, and failure
modes. For agent-based, RL, or simulation proposals, also specify entities,
state, actions, interactions, and calibration targets.

## Research-Grade Escalation

Escalate from compact answer to research-grade memo when the user asks about
science, economics, ML/RL, forecasting, technological change, historical
analogies, or why a system works the way it does, or when he says a previous
answer was shallow.

For research-grade answers:

- Use `research-synthesis` and the relevant domain skill.
- Search external scholarly/current sources when the answer depends on the state
  of research.
- Give the mechanisms, competing hypotheses, evidence, uncertainty, and failure
  modes that change the answer.
- For empirical prior art, extract data, measurement, method, result, and
  limitation for each main paper; do not only list paper names.
- If the user says a prior answer lacked results, switch to result-extraction mode:
  prioritize verified sample sizes, exposure/outcome measures, coefficients,
  correlations, effect sizes, and directional findings over broad coverage.
- Save an answer case or appendix if the result would otherwise be too shallow
  in chat.
- Do not turn the item into only project context, tasks, or a routing note.
- Do not satisfy depth by listing sources or mechanisms. The chat answer should
  contain the strongest few insights; the saved memo can carry the audit trail.
- If several packet items belong to the same project or nearby source thread,
  treat them as mutually informative context and say when grouping changes the
  interpretation. Still preserve each source question and answer explicitly.

## Reader Calibration

the user understands ML, economics, statistics, and data analysis; skip basics there
and focus on mechanisms, caveats, and falsification. Explain biology, physics,
chemistry, and other weaker-background mechanisms more explicitly.

## Skill Routing

- Technical ML idea: use `ml-research-review`.
- Psychology, science, environment, performance, or study-audit question: use `evidence-context-effects`.
- career, migration, AI-tool access, jobs, PhD, salaries: use `career-risk-strategy`.
- Book, public intellectual, prediction, factual audit: use `prediction-audit`.
- General multi-source research: combine with `research-synthesis`.

## Output Shape

```text
Reconstructed question:
Short answer:
Key insights:
Concrete next step:
Uncertainty:
Appendix:
```

Do not write a giant answer unless the user explicitly asks for the full appendix inline.

## References

- `profile.md`
- `notes/playbooks.md`
- archived old harness, if provenance is needed: `archive/2026-05-life-os-v1/08_llm_context/answer_harness/`

## Quality Gates

- Did we recover the user's real question and key wording?
- Did we check active local context before external sources?
- Did we use current sources for current/high-stakes claims?
- Did we give numbers/ranges when asked?
- If papers/tools are mentioned, is there enough result and method detail for
  the user to reuse them in a thesis?
- Did we provide concrete options and hard judgment?
- Did we include a falsification test for ML/science claims?
- Did we save a compact pointer or appendix without bloating active storage?
- For long answers, did we request feedback and identify any durable memory candidate?
