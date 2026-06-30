---
name: coding-feature-implementation
description: Use this skill when implementing one approved coding feature, endpoint, UI behavior, integration, or bridge/platform slice from a Life OS ticket.
---

# Coding Feature Implementation

## Purpose

Implement one bounded feature without broad refactors or speculative extras.

## Workflow

1. Treat the ticket as the behavior contract: goal, non-goals, acceptance criteria, validation, writeback target.
2. Inspect existing patterns and reuse local helpers before adding abstractions.
3. Make the smallest coherent code change that satisfies the contract.
4. Update nearby tests, fixtures, docs, or schemas when the behavior surface changes.
5. Run validation when feasible.
6. Stop with changed files, behavior summary, validation result, and residual risk.

## Guardrails

- Do not add unrelated features because they seem useful.
- Do not change architecture unless the ticket explicitly asks for it.
- Prefer a follow-up ticket over expanding scope mid-run.

## Verification

Evidence should include at least one of: test output, lint/type/build output, API smoke, browser screenshot, or manual check steps.

## Provenance

Local Life OS adaptation inspired by Addy Osmani's production engineering lifecycle, Vercel web-agent skills, Microsoft skill test scenarios, and VoltAgent specialist roles.
