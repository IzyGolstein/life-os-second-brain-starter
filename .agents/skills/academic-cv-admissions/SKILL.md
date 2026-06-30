---
name: academic-cv-admissions
description: Use this skill when converting a work resume, LaTeX CV, certificates, recommendation letters, program criteria, GitHub/project evidence, or admissions portfolio documents into an academic CV plan or draft for master's/PhD applications. Trigger for questions about what belongs in the CV versus attachments, how to structure an academic CV, or how to minimally edit an existing .tex CV for admission scoring.
---

# Academic CV Admissions

## Overview

Build an admissions CV as a compact evidence index, not a document dump. The CV should show the score-relevant facts clearly while transcripts, certificates, recommendation letters, full papers, and proof scans remain separate attachments.

## Workflow

1. Read the target program criteria and extract scoring hooks.
2. Read the current CV/resume and list what already maps to the criteria.
3. Extract evidence from attached documents: certificates, recommendation letters, transcripts, GitHub repos, papers, presentations.
4. Split every fact into one of three buckets:
   - `CV`: must be visible in the CV.
   - `Attachment`: proof file only; summarize briefly in CV if relevant.
   - `Ask the user`: needs verification, date, score, title, privacy check, or exact wording.
5. Preserve the existing CV format unless it blocks the admissions story. For LaTeX CVs, prefer section reorder/addition and existing macros over template replacement.
6. Draft a structure before editing:
   - header;
   - education;
   - research interests/thesis;
   - selected coursework;
   - academic training;
   - selected academic work/projects;
   - conference presentations/academic achievements;
   - professional experience;
   - skills/computer technologies;
   - languages;
   - social activities if real.
7. Rewrite work bullets through academic mechanisms: econometrics, incentives, pricing, forecasting, experiments, causal evaluation, market analysis, data construction, and policy relevance.
8. Save traceability in the project: source manifest, CV notes, and a short answer/case when the user asks for judgment.

## Editing Rules

- Do not paste recommendation-letter praise into the CV. Convert it into factual, verifiable CV entries only.
- Do not invent publications, grants, awards, or English level.
- Include conferences, seminars, summer schools, and additional education directly in the CV when the program criteria name them.
- Use exact names and dates from certificates when available.
- Keep confidential business impact numbers only if the user confirms they are safe; otherwise use method/result phrasing.
- For `.tex`, fix compile-blocking macro argument errors before substantive polish.

## HSE EEP Reference

For HSE "Экономика и экономическая политика", read `references/hse-eep.md` when working on the user's 2026 application.
