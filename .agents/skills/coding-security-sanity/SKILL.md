---
name: coding-security-sanity
description: Use this skill when touching command execution, provider adapters, repo whitelists, path handling, file attachments, network access, browser-to-bridge APIs, secrets, permissions, or auth-like behavior.
---

# Coding Security Sanity

## Purpose

Keep agent execution and file handling fail-closed.

## Workflow

1. Identify the trust boundary: browser, bridge, provider adapter, repo path, attachment, shell command, network, or credential.
2. Reject arbitrary paths, parent traversal, `.git` paths, home shortcuts, unknown repo ids, and unknown providers.
3. Keep browser JavaScript away from direct shell execution.
4. Never store secrets in Life OS Markdown.
5. Prefer explicit allowlists and named permission profiles over ad hoc checks.
6. Log what happened without leaking sensitive values.

## Verification

Check at least one negative case when feasible: unknown repo, bad path, unsupported provider, too-large attachment, or disabled network/browser setting.

## Provenance

Local Life OS adaptation inspired by security/hardening skills, Microsoft MCP/permission patterns, safety-hook tooling, and Life OS bridge rules.
