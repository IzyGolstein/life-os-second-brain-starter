---
name: coding-provider-adapter
description: Use this skill when adding or changing a Life OS execution provider adapter such as Codex CLI, Claude Code, OpenHands, OpenClaw, LiteLLM/OpenRouter, Plane mirror, Langfuse tracing, MCP, or external repo execution.
---

# Coding Provider Adapter

## Purpose

Add provider integrations behind stable Life OS contracts instead of coupling them to UI state.

## Workflow

1. Treat `TicketEnvelope` as the task contract and `PromptPacket` as the provider input.
2. Resolve `repo_id` through the whitelist; never accept arbitrary execution paths from UI.
3. Keep provider-specific transport isolated: command, API call, worktree/sandbox, timeout, logs, artifacts.
4. Write run logs and patches/artifacts back under the Life OS project.
5. Keep provider output reviewable before source repo adoption.
6. Add dry-run behavior before real execution when possible.

## Adapter Checklist

- Input contract is provider-neutral.
- Permission profile and sandbox are enforced.
- Errors are captured as run logs, not lost in chat.
- Provider can be replaced without changing the frontend.
- Validation and residual risk are returned to the ticket.

## Provenance

Local Life OS adaptation inspired by OpenAI/Anthropic skill portability, wshobson multi-harness adapters, Microsoft MCP/agent patterns, and awesome-claude-code orchestration catalogs.
