---
name: frontend-implementation-qa
description: Use this skill when building, modifying, or reviewing UI, CSS, components, layouts, graph views, task boards, markdown readers, forms, or local frontend prototypes.
---

# Frontend Implementation QA

## Purpose

Make UI changes that are usable, visually stable, accessible, responsive, and verified in a browser.

## Workflow

1. Follow the existing product surface and design system before inventing a new visual language.
2. Implement real workflows, states, empty/error/loading cases, and keyboard interactions when relevant.
3. Use stable dimensions for boards, panels, graph areas, toolbars, and buttons.
4. Avoid generic AI UI: excessive gradients, purple-heavy palettes, oversized cards, random shadows, stock hero layouts.
5. Verify with the local browser target when available: desktop and narrow viewport, console errors, text overflow, interaction, and screenshot.
6. When sending the user a local URL, open that exact URL yourself after the latest server restart and confirm the rendered page is the intended screen.
7. For Plane/Life OS UI, do not accept an HTTP 200 alone; check that the page is not the Plane startup/maintenance screen, a blank shell, or an error boundary.
8. For canvas/graph/UI visual work, inspect the screenshot yourself and iterate until it is readable.

## Output

```text
Changed UI:
Interaction verified:
Responsive/overflow check:
Browser/screenshot evidence:
Remaining visual risk:
```

## Provenance

Local Life OS adaptation inspired by Addy Osmani frontend UI engineering, Vercel web-agent skills, Microsoft frontend design review, and UI/UX subagent taxonomies.
