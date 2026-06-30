---
name: product-experiment-design
description: Use this skill when the user has a product idea or feature and needs a minimal experiment, prototype, smoke test, landing page, concierge flow, Plane workflow, or validation plan with stop/go criteria.
---

# Product Experiment Design

Use this skill to turn a product idea into the smallest decisive test. The default is not "build an MVP"; the default is "learn enough to decide."

## Workflow

1. State the decision the experiment must inform.
2. Pick the riskiest assumption.
3. Choose the cheapest valid experiment:
   - manual or concierge workflow;
   - fake-door UI;
   - clickable prototype;
   - interview with concrete artifact;
   - workflow simulation inside Plane/Markdown;
   - small technical spike only when feasibility is the riskiest assumption.
4. Define target audience and recruitment/channel.
5. Define the task flow the user will attempt.
6. Define success metric, failure threshold, and what result changes the decision.
7. Set a short timebox and the next action after the result.

## Output

```text
Decision:
Riskiest Assumption:
Experiment:
Audience / Channel:
Test Script Or Flow:
Success Metric:
Stop / Go Threshold:
Timebox:
Follow-Up Decision:
```

## Rules

- A metric must change the decision; otherwise it is vanity.
- Use small manual tests before automation.
- Prefer testing behavior over asking whether the user "would use it."
- For Life OS and Plane features, use one real task/wiki/project first before migrating bulk data.
- If the experiment cannot fail, redesign it.
