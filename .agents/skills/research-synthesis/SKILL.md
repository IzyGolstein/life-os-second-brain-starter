---
name: research-synthesis
description: Use this skill when doing source-backed research, market research, literature review, competitor analysis, policy research, source comparison, evidence tables, citations, and uncertainty-aware synthesis.
---

# Research Synthesis

## Purpose

Use sources to improve a research answer: inspect them, rank them, extract what
changes the mechanism or judgment, and keep uncertainty visible.

## Workflow

1. Clarify the research question and scope.
2. Find prior art first for research/product/modeling ideas.
3. Open and inspect sources; rank by substantive relevance.
4. Build the mechanism/model, alternatives, measurements, and failure modes,
   preserving the user's own framing or hypothesis when one was given.
5. Search narrowly for any missing evidence.
6. Extract claims, limits, conflicts, and dates; separate evidence from interpretation.
7. Stop when the answer has mechanism, strongest prior art, alternatives,
   concrete test/work product, uncertainty/falsifier, and next action.
8. Save useful source notes in `answers/`, `notes/sources.md`, or the relevant
   `projects/*.md`; use appendices only for long audit trails.

## Output

Default: compact source-backed findings integrated into the answer.

For saved memos/appendices only: evidence table, source notes, conflicts/gaps,
and recommended next research steps.

## Empirical Prior-Art Standard

- When the user asks for literature, papers, or hypothesis support, summarize each
  main empirical paper with dataset/sample, observation unit, exposure/treatment,
  outcome measurement, design/model, main numerical or directional result, and
  the main limitation.
- Do not cite a paper merely as a name-drop. If a paper is included, report at
  least one concrete method detail and one concrete result that helps the user
  believe more or less in the hypothesis.
- Prefer compact evidence tables for multi-paper answers. Put "not causal" or
  the identifying assumption directly in the limitation column when relevant.
- When exact coefficients are unavailable from accessible sources, say so and
  report only the result level that can be verified from the source.

## Rules

- Cite external sources when browsing or reading documents.
- Do not cite a page unless it clearly supports the claim and contains useful
  information for the user.
- Do not overstate certainty.
- Mark stale sources and access dates.
- For scholarly questions, prefer papers, books, working papers, datasets,
  official statistics, or field surveys over generic web summaries.
- Named authorities are not enough. Explain the mechanism, why that literature
  is relevant, where it disagrees, and what evidence would falsify the answer.
