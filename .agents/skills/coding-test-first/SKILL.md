---
name: coding-test-first
description: Use this skill when changing behavior, fixing bugs, touching shared code, editing provider/bridge logic, or adding functionality that can be checked with tests or executable smoke checks.
---

# Coding Test First

## Purpose

Prefer an executable check before implementation and keep the fix minimal.

## Workflow

1. State the behavior being protected.
2. Choose the cheapest check: unit test, integration test, API smoke, CLI smoke, browser action, screenshot, or validation script.
3. If feasible, run or create a failing check before editing.
4. Implement only what is needed to pass the check.
5. Rerun the check and the repo's relevant validation.
6. If no executable check is feasible, write the manual verification steps and residual risk.

## Guardrails

- Do not claim behavior is fixed without evidence.
- Do not overbuild beyond the failing check.
- Do not weaken tests to make the change pass.

## Provenance

Local Life OS adaptation inspired by TDD skills, `tdd-guard` hook patterns, Microsoft skill test scenarios, and Addy Osmani's test-driven workflows.
