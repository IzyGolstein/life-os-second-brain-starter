---
name: coding-verification-gate
description: Use this skill before saying a coding, UI, backend, provider, or integration task is fixed, complete, ready, passing, or production-ready.
---

# Coding Verification Gate

Adapted from the archive `verification-before-completion` skill.

## Rule

Evidence before completion claims.

## Gate

Before reporting success:

1. Identify the command, browser path, API call, or artifact that proves the claim.
2. Run it fresh in the current workspace.
3. Read the full output and exit code.
4. Check the user-facing behavior when the change touches UI, Plane, bridge, local execution, or providers.
5. If you give the user a local URL, open that exact URL yourself after the last restart/edit and verify the rendered page, not just HTTP status.
6. For Plane/Life OS UI, explicitly check that the page is not showing the Plane startup/maintenance screen or an error boundary.
7. Report exact verification and any remaining warnings or blockers.

## Not Enough

Do not claim success from:

- static code inspection only;
- a previous run before the latest edit;
- "should work";
- provider or subagent self-report;
- tests passing when the bug was in a browser/API path not covered by tests;
- `200 OK` from HTML when the user-facing page can still render a startup, maintenance, or client-side error screen.
