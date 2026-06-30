---
name: vacancy-search-verification
description: Use this skill when the user asks to find, shortlist, verify, or compare current vacancies, internships, jobs, roles, or application links in Russia, big tech, international startups, or a new career domain.
---

# Vacancy Search Verification

## Search Space

Choose sources by target market:

- Named companies: company career site and official ATS first.
- local/regional: company career site, HH, Habr Career for tech roles, official ATS/job profile.
- Big tech: official careers pages, LinkedIn Jobs, company-specific talent portals.
- International startups: Wellfound, YC Work at a Startup, Otta, LinkedIn, VC portfolio job boards.
- Remote/global: company site, LinkedIn, Wellfound, RemoteOK/WeWorkRemotely only after strict validation.
- New domain/sphere: first map role synonyms and adjacent titles, then search specialist boards for that domain.

Low-trust SEO aggregators and repost farms are discovery leads only. Do not use Careerist-style pages as final proof unless no better source exists and the concrete vacancy is clearly open.

## Validation Rules

A vacancy may enter the main list only if:

1. Its concrete vacancy page was opened during the answer.
2. The page is not archived, expired, closed, unavailable, or a generic search/filter page.
3. There is an active apply path: button, form, email, ATS flow, or official open-status text.
4. The source is credible: employer site, official ATS/profile, HH/Habr/LinkedIn or a reputable board.
5. The role matches the requested profile by title, responsibilities, seniority, location, and constraints.

Search snippets, cached pages, generic filters, Telegram reposts, and aggregator summaries are not proof of актуальность.

## Output

Use this table:

```text
Company | Vacancy | Link | Source | Active evidence | Fit | Caveat
```

For `Active evidence`, say what was checked: apply button/form visible, no archive banner, publish/update date if visible, access date.

Always add `Excluded / not found` for checked leads that failed validation, with a short reason.

If live pages cannot be opened or a site blocks access, say so. Do not claim verification.
