---
name: product-idea-triage
description: Use this skill when the user asks whether a product, feature, startup, Life OS workflow, Plane integration, AI-agent idea, or project idea is worth doing, prioritizing, killing, parking, or turning into an experiment.
---

# Product Idea Triage

Use this skill before implementation when the real question is whether an idea is good enough to spend attention on. The goal is hard product judgment, not automatic ticket creation.

## Workflow

1. Restate the idea in one sentence.
2. Name the target user and the job-to-be-done.
3. Check the pain: intensity, frequency, urgency, and current workaround.
4. Check pull signal: observed behavior, repeated requests, payment/attention, or a concrete blocked workflow. Treat stated preference as weak evidence.
5. Check strategic fit for the user and Life OS: compounding value, personal leverage, reuse across projects, and integration with the existing second brain.
6. Check feasibility: smallest implementation, maintenance burden, provider/tool risk, UI complexity, and data/security risk.
7. Decide one of: `Build`, `Prototype`, `Research`, `Park`, or `Kill`.
8. Name the cheapest next validation step and the evidence that would change the decision.

## Scoring Rubric

Use compact 1-5 scores only when useful:

- Pain intensity
- Frequency
- Reach
- Pull signal
- Strategic fit
- Differentiation
- Distribution path
- Effort/risk

High effort/risk should lower the verdict unless the pull signal is strong.

## Output

```text
Verdict:
Idea:
Target User / Job:
Why:
Strongest Evidence:
Biggest Risk:
What Would Change My Mind:
Cheapest Next Test:
```

## Rules

- Be skeptical and concrete.
- Do not convert every idea into a ticket.
- If there is no user or usage evidence, default to `Prototype`, `Research`, or `Park`, not `Build`.
- Separate "this is possible" from "this is worth building."
- For Life OS ideas, prefer workflow leverage over decorative UI.
