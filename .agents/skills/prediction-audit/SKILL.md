---
name: prediction-audit
description: Use this skill when the user wants to evaluate a book, article, public intellectual, expert, podcast, or forecast by extracting factual or predictive claims and checking them against evidence. Trigger for Movchan-style book audits, expert accuracy ratings, open-access texts, claim extraction, forecast scoring, and "who predicted X correctly" questions.
---

# Prediction Audit

## Overview

Turn texts into a reproducible audit of checkable claims. Do not block on copyright boilerplate when the user provides a legal/open source; do not republish large text chunks.

## Required Output

1. Reconstructed audit question.
2. Access/source status: open access, provided text, purchased copy, or unavailable.
3. Claim extraction scope: chapter/article/time window.
4. Claim schema and score rubric.
5. Evidence-source plan.
6. Baseline for comparison.
7. Pilot plan and uncertainty.

## Workflow

1. Verify access status before discussing blockers.
2. Extract only scoreable claims: factual, causal, forecast, conditional forecast, comparative, institutional.
3. Exclude rhetoric, metaphors, and value judgments from accuracy score.
4. Keep only short quote anchors; store paraphrase, location, evidence links, and score.
5. Compare against primary/institutional sources and a baseline.
6. Start with a 20-40 claim pilot from one chapter or section.

## Quality Gates

- Did we check whether the text is actually open/provided?
- Did we avoid large copyrighted reproduction?
- Did we define baseline, resolution criteria, and score?
- Did we separate factual accuracy from forecast skill?
- Did we produce a pilot before scaling?

## References

- `references/claim-schema.md`
