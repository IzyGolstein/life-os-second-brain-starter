---
name: architecture-boundary-review
description: Use this skill when reviewing or planning system architecture, especially service boundaries, multi-tenant isolation, Plane/Life OS integration, storage contracts, provider boundaries, and production rollout risks.
---

# Architecture Boundary Review

Adapted from the archive `architecture-analyzer` skill, stripped of corporate tools and mandatory artifact generation.

## Workflow

1. Identify the system boundary and actors.
2. Classify inputs: code, API contracts, schemas, docs, infra, run logs, UI paths.
3. Extract components, data stores, queues, providers, external systems, and user-facing surfaces.
4. Map critical flows end to end.
5. Mark source-of-truth decisions explicitly.
6. Check isolation, security, failure states, observability, and migration paths.
7. Separate facts from assumptions.
8. Produce a concise architecture table or Mermaid diagram only when it clarifies decisions.

## Multi-Tenant Checklist

For production systems with many users, verify:

- every record has tenant/user ownership;
- retrieval cannot cross tenant boundaries;
- files, runs, artifacts, and indexes are scoped;
- secrets are isolated;
- background jobs and provider calls carry tenant context;
- admin/debug tools cannot leak user data by default.

## Plane + Life OS Checklist

Keep the boundary explicit:

- Plane: UI/work surface, wiki, tasks, comments, attachments, activity.
- Life OS backend: context resolver, skills, provider execution, run logs, answer persistence.
- User memory: tenant-private profile, projects, answers, notes, files.
- Shared knowledge: generic skills, eval templates, public docs only.
