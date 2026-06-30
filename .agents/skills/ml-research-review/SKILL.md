---
name: ml-research-review
description: Use this skill when answering the user's technical ML, causal inference, uplift modeling, recommender, policy-learning, experiment, metric, or modeling-idea questions when he wants professional research judgment rather than implementation. Especially use for domain-specific business problems, sigmoid/minimum-rate, off-policy evaluation, treatment effects, calibration, and "is this idea worth trying" questions.
---

# ML Research Review

## Overview

Evaluate ML ideas as research claims: formalize the estimand, criticize assumptions, connect to methods/literature, and propose the smallest falsification experiment.

## Required Output

1. Reconstructed question with the original hypothesis preserved.
2. Directional judgment: reasonable / weak / not worth doing.
3. Hard criticism: assumptions, identifiability, leakage, metric mismatch.
4. Formalization: target, loss, estimand, decision rule.
5. Related methods and search keywords.
6. Smallest experiment and stop/go criterion.
7. Implementation and evaluation sketch.
8. Saved appendix if the answer is nontrivial.

## Workflow

1. Read local project notes first: project context, tasks, source prompts, modeling contracts, experiment ladders.
2. Do not stop at "code/data missing" when the user asked for research.
3. Separate conceptual validity from executable validation.
4. Prefer simple baselines and diagnostic gates before architecture changes.
5. Use external literature for unstable or method-specific claims.
6. Judge by the business/policy metric, not only model loss.

## Causal ML Standard

- For DML, R-learners, T-learners, causal forests, orthogonal learners, and
  related methods, separate identification from estimation. These methods can
  reduce adjustment and regularization bias under stated assumptions, but they
  do not create exogenous treatment variation.
- State the unit, treatment, outcome, timing, estimand, identifying assumption,
  overlap/positivity requirement, nuisance models, cross-fitting scheme, and
  whether controls are measured before treatment.
- Say what the method can defensibly support, what remains observational, and
  what design element would be needed for a stronger causal claim.

## Quality Gates

- Did the proposed loss estimate the user's actual target?
- Are observed labels enough to identify the claimed latent quantity?
- Is there an off-policy / causal / selection issue?
- Is there a calibration or monotonicity requirement?
- Is the suggested experiment cheap and falsifiable?
- Does the recommendation say whether to do the work now?

## References

- `references/ml-review-checklist.md`
