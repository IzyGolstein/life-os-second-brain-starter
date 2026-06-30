#!/usr/bin/env python3
"""Generate a private Markdown second-brain repository from an intake JSON."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKS = ROOT / "starter-kits/second-brain/skill-selection/starter-skill-packs.json"
DEFAULT_SKILL_SOURCE = ROOT / ".agents/skills"


def slugify(value: str, fallback: str = "item") -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or fallback


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def text(value: Any, fallback: str = "") -> str:
    if value is None:
        return fallback
    return str(value)


def bullet_list(items: list[Any], empty: str = "- Not specified.") -> str:
    clean = [str(item).strip() for item in items if str(item).strip()]
    if not clean:
        return empty
    return "\n".join(f"- {item}" for item in clean)


def numbered_list(items: list[Any], empty: str = "1. Not specified.") -> str:
    clean = [str(item).strip() for item in items if str(item).strip()]
    if not clean:
        return empty
    return "\n".join(f"{idx}. {item}" for idx, item in enumerate(clean, 1))


def frontmatter(
    record_id: str,
    record_type: str,
    *,
    privacy: str = "sensitive",
    status: str = "active",
    updated: str,
    project: str | None = None,
    role: str | None = None,
) -> str:
    lines = [
        "---",
        f"id: {record_id}",
        f"type: {record_type}",
        f"status: {status}",
        f"privacy: {privacy}",
        f"updated: {updated}",
    ]
    if project:
        lines.append(f"project: {project}")
    if role:
        lines.append(f"role: {role}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_file(path: Path, content: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def select_skills(
    intake: dict[str, Any],
    pack_config: dict[str, Any],
) -> tuple[list[str], list[str]]:
    packs_cfg = pack_config.get("packs", {})
    domain_to_packs = pack_config.get("domain_to_packs", {})

    selected_packs: list[str] = []
    if not intake.get("disable_default_skill_packs"):
        for pack_id, pack in packs_cfg.items():
            if pack.get("default"):
                selected_packs.append(pack_id)

    for domain in as_list(intake.get("domains")):
        selected_packs.extend(domain_to_packs.get(str(domain), []))

    selected_packs.extend(str(pack) for pack in as_list(intake.get("skill_packs")))

    deduped_packs: list[str] = []
    for pack in selected_packs:
        if pack in packs_cfg and pack not in deduped_packs:
            deduped_packs.append(pack)

    skills: list[str] = []
    for pack in deduped_packs:
        for skill in packs_cfg[pack].get("skills", []):
            if skill not in skills:
                skills.append(skill)

    explicit_skills = [str(skill) for skill in as_list(intake.get("skills"))]
    for skill in explicit_skills:
        if skill not in skills:
            skills.append(skill)

    return deduped_packs, skills


def copy_selected_skills(
    skills: list[str],
    source: Path,
    target: Path,
    *,
    force: bool,
) -> tuple[list[str], list[str]]:
    copied: list[str] = []
    missing: list[str] = []
    target.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        src = source / skill
        dest = target / skill
        if not src.is_dir():
            missing.append(skill)
            continue
        if dest.exists() and force:
            shutil.rmtree(dest)
        if dest.exists() and not force:
            raise FileExistsError(f"Refusing to overwrite existing skill: {dest}")
        shutil.copytree(src, dest)
        copied.append(skill)

    return copied, missing


def render_readme(data: dict[str, Any], selected_skills: list[str]) -> str:
    user = data.get("user", {})
    name = text(user.get("display_name") or user.get("preferred_name"), "New user")
    return f"""# {name} Second Brain

This is a private Markdown second-brain repository generated from an intake
form. It stores user profile, answer preferences, goals, project context,
answers, inbox source packets, and selected runtime skills.

Default context load:

1. `AGENTS.md`
2. `profile.md`
3. `notes/answer-contract.md`
4. one relevant skill under `.agents/skills/`
5. one relevant project/note/answer/inbox source only when needed

Selected skills:

{bullet_list(selected_skills)}

Do not store secrets in this repository.
"""


def render_agents(data: dict[str, Any], selected_skills: list[str], today: str) -> str:
    user = data.get("user", {})
    default_language = text(user.get("default_answer_language"), "user preference")
    return frontmatter("agents", "context", privacy="internal", updated=today) + f"""# Agent Map

This repo is a private, auditable second brain. Markdown is durable memory; chat
memory is cache.

## Rules

- Do not store secrets: passwords, tokens, API keys, private keys, seed phrases,
  bank access, or credentials.
- Load the smallest useful context. Default preload is `profile.md` plus
  `notes/answer-contract.md`.
- Do not read the whole repository unless the task requires it.
- Answer first, then save when saving is appropriate.
- Preserve traceability for substantive answers:
  source/original -> reconstructed question -> answer/result -> conclusion.
- Ask before changing core memory: `AGENTS.md`, `profile.md`,
  `notes/answer-contract.md`, `notes/user/*`, or `.agents/skills/*`.
- Use `archive/` instead of deletion when unsure.
- For external project repos, add only a small second-brain pointer to the
  target `AGENTS.md`; do not copy private context into the project.

## Active Layout

```text
profile.md
inbox.md
tasks.md
inbox/
answers/
notes/
projects/
agent-system/
.agents/
generated/
archive/
```

## Answer Workflow

1. Read `profile.md`.
2. Read `notes/answer-contract.md`.
3. Use one relevant skill from `.agents/skills/` when applicable.
4. Search `projects/`, `answers/`, `notes/`, and `inbox/` only as needed.
5. Browse current or high-stakes facts when they may have changed.
6. Respond in `{default_language}` unless the user asks otherwise.
7. Save a pointer or answer case only when the result has durable value.

## Installed Skills

{bullet_list(selected_skills)}
"""


def render_profile(data: dict[str, Any], today: str) -> str:
    user = data.get("user", {})
    privacy = data.get("privacy", {}).get("default", "sensitive")
    name = text(user.get("preferred_name") or user.get("display_name"), "User")
    languages = ", ".join(str(item) for item in as_list(user.get("languages"))) or "Not specified"
    return frontmatter("profile", "profile", privacy=privacy, updated=today) + f"""# Profile

## Short Preload

- Preferred name: {name}
- Display name: {text(user.get("display_name"), name)}
- Timezone: {text(user.get("timezone"), "Not specified")}
- Languages: {languages}
- Default answer language: {text(user.get("default_answer_language"), "Not specified")}

## User Snapshot

{bullet_list(as_list(user.get("short_profile")))}

## Context Rule

Use this file as the compact preload profile. Load `notes/user/personal_model.md`
only for personal, strategic, career, planning, or preference-sensitive work.
"""


def render_answer_contract(data: dict[str, Any], skills: list[str], today: str) -> str:
    prefs = data.get("answer_preferences", {})
    privacy = data.get("privacy", {}).get("default", "sensitive")
    return frontmatter("answer_contract", "note", privacy=privacy, updated=today, role="answer_contract") + f"""# Answer Contract

## Load Order

1. `profile.md`
2. `notes/answer-contract.md`
3. one relevant `.agents/skills/<skill>/SKILL.md`
4. `answers/question-ledger.md` for recurring questions
5. relevant `projects/`, `answers/`, `notes/`, or `inbox/` files found by search

Default context budget is small. Do not load raw inbox, archive, long answer
cases, or project folders unless the question needs them.

## Answer Preferences

- Tone: {text(prefs.get("tone"), "Not specified")}
- Default length: {text(prefs.get("default_length"), "compact")}
- Depth rule: {text(prefs.get("depth_rule"), "Use deeper analysis only when the decision requires it.")}
- Browse policy: {text(prefs.get("browse_policy"), "Browse for current or high-stakes facts.")}
- Citation policy: {text(prefs.get("citation_policy"), "Cite external factual sources when used.")}
- Save policy: {text(prefs.get("save_policy"), "Ask before changing core memory.")}

## Bad Answer Patterns

{bullet_list(as_list(prefs.get("bad_answer_patterns")))}

## Excellent Answer Patterns

{bullet_list(as_list(prefs.get("excellent_answer_patterns")))}

## Skill Routing

Installed skills:

{bullet_list(skills)}

Use a skill only when it fits the user's intent. Do not stack many skills by
default.

## Substantive Answer Shape

Make clear:

```text
Question I am answering
Context I am using
Short judgment
Analysis
Uncertainty / what would change the answer
Next concrete step
Where saved, if saved
```

For long substantive answers, ask for brief feedback and identify any memory
candidate that needs approval before changing core memory.
"""


def render_personal_model(data: dict[str, Any], today: str) -> str:
    user = data.get("user", {})
    goals = data.get("goals", [])
    privacy = data.get("privacy", {}).get("default", "sensitive")
    goal_lines: list[str] = []
    for goal in goals:
        goal_lines.append(
            f"- {text(goal.get('title'), text(goal.get('id'), 'Goal'))}: "
            f"{text(goal.get('success'), 'success not specified')}"
        )
    return frontmatter("personal_model", "note", privacy=privacy, updated=today, role="personal_model") + f"""# Personal Model

## Stable Facts

{bullet_list(as_list(user.get("short_profile")))}

## Active Goals

{bullet_list(goal_lines)}

## Working Assumptions

- Treat this file as a hypothesis, not a complete identity.
- Prefer explicit user corrections over inferred patterns.
- Update only after user approval when a change would affect future behavior.

## Unknowns To Resolve

- Decision style under stress.
- Preferred cadence for reviews.
- Boundaries between personal, work, and shared team context.
"""


def render_answer_preferences(data: dict[str, Any], today: str) -> str:
    prefs = data.get("answer_preferences", {})
    privacy = data.get("privacy", {}).get("default", "sensitive")
    return frontmatter("answer_preferences", "note", privacy=privacy, updated=today, role="answer_preferences") + f"""# Answer Preferences

- Tone: {text(prefs.get("tone"), "Not specified")}
- Default length: {text(prefs.get("default_length"), "compact")}
- Depth rule: {text(prefs.get("depth_rule"), "Not specified")}
- Browse policy: {text(prefs.get("browse_policy"), "Not specified")}
- Citation policy: {text(prefs.get("citation_policy"), "Not specified")}
- Save policy: {text(prefs.get("save_policy"), "Not specified")}

## Avoid

{bullet_list(as_list(prefs.get("bad_answer_patterns")))}

## Prefer

{bullet_list(as_list(prefs.get("excellent_answer_patterns")))}
"""


def render_privacy_rules(data: dict[str, Any], today: str) -> str:
    privacy = data.get("privacy", {})
    default = privacy.get("default", "sensitive")
    return frontmatter("privacy_rules", "note", privacy="internal", updated=today, role="privacy_rules") + f"""# Privacy Rules

Default privacy: `{default}`

## Never Store

{bullet_list(as_list(privacy.get("never_store")))}

## Shareable With Team

{bullet_list(as_list(privacy.get("shareable_with_team")))}

## Private By Default

{bullet_list(as_list(privacy.get("private")))}

## Rule

When unsure, mark records as `sensitive` and ask before sharing or publishing.
"""


def render_repository_contract(today: str) -> str:
    return frontmatter("repository_contract", "note", privacy="internal", updated=today, role="repository_contract") + """# Repository Contract

## Purpose

This repository is a private, searchable, auditable second brain. It stores
profile, preferences, goals, project context, source packets, answers, decisions,
tasks, and selected skills.

## Traceability

Every serious question or inbox item should be traceable:

```text
source path -> original text/transcript -> reconstructed question -> answer/result -> conclusion -> destination
```

## Layout

```text
profile.md
inbox.md
tasks.md
inbox/
answers/
notes/
projects/
agent-system/
.agents/
generated/
archive/
```

## Project Folder Contract

Each substantial project should have:

- `projects/<slug>.md`: compact project hub.
- `projects/<slug>/_index.md`: detailed map and current state.
- `projects/<slug>/tasks.md`: project tasks.
- `projects/<slug>/decisions.md`: decision log.
- optional `cases/`, `evidence/`, `notes/`, `artifacts/`, and `tickets/`.

## Big File Policy

Do not copy large binary files by default. Store paths, manifests, summaries,
checksums, and privacy boundaries.

## Source Safety

Never store secrets or credentials. Do not copy client raw data, participant
rows, private exports, or access tokens unless the user has explicitly approved
safe redaction.
"""


def render_projects_index(data: dict[str, Any], today: str) -> str:
    projects = data.get("projects", [])
    lines = []
    for project in projects:
        pid = slugify(text(project.get("id") or project.get("title")), "project")
        title = text(project.get("title"), pid)
        status = text(project.get("status"), "active")
        lines.append(f"[{title}]({pid}.md): {status}")
    return frontmatter("projects_index", "index", privacy="sensitive", updated=today) + f"""# Projects Index

{bullet_list(lines)}
"""


def render_project_hub(project: dict[str, Any], today: str) -> str:
    pid = slugify(text(project.get("id") or project.get("title")), "project")
    title = text(project.get("title"), pid)
    privacy = text(project.get("privacy"), "sensitive")
    status = text(project.get("status"), "active")
    repos = []
    for repo in as_list(project.get("repos")):
        if isinstance(repo, dict):
            repos.append(f"{text(repo.get('id'), 'repo')}: {text(repo.get('url'), 'no url')}")
        else:
            repos.append(str(repo))
    return frontmatter(pid, "project", privacy=privacy, status=status, updated=today) + f"""# {title}

## Goal

{text(project.get("goal"), "Not specified.")}

## Current Context

{text(project.get("context"), "Not specified.")}

## Out Of Scope

{text(project.get("out_of_scope"), "Not specified.")}

## Repositories And Sources

{bullet_list(repos)}

## Next Actions

{numbered_list(as_list(project.get("next_actions")))}

## Done Means

{text(project.get("done"), "Not specified.")}
"""


def render_project_detail(project: dict[str, Any], today: str, kind: str) -> str:
    pid = slugify(text(project.get("id") or project.get("title")), "project")
    title = text(project.get("title"), pid)
    if kind == "index":
        body = f"""# {title} Detail Index

## Map

- Hub: `../{pid}.md`
- Tasks: `tasks.md`
- Decisions: `decisions.md`
- Cases: `cases/`
- Evidence: `evidence/`
- Notes: `notes/`

## Current State

{text(project.get("context"), "Not specified.")}
"""
        role = "project_index"
    elif kind == "tasks":
        body = f"""# {title} Tasks

## Active

{numbered_list(as_list(project.get("next_actions")))}

## Waiting

1. Not specified.

## Someday

1. Not specified.
"""
        role = "task_log"
    else:
        body = f"""# {title} Decisions

No decisions recorded yet.
"""
        role = "decision_log"
    return frontmatter(f"{pid}_{kind}", "note", privacy=text(project.get("privacy"), "sensitive"), updated=today, project=pid, role=role) + body


def render_tasks(data: dict[str, Any], today: str) -> str:
    goals = data.get("goals", [])
    lines = []
    for goal in goals:
        title = text(goal.get("title"), text(goal.get("id"), "Goal"))
        next_step = text(goal.get("next_step"), "Next step not specified")
        lines.append(f"{title}: {next_step}")
    return frontmatter("tasks", "task", privacy="sensitive", updated=today) + f"""# Tasks

## Active

{numbered_list(lines)}

## Waiting

1. Not specified.

## Someday

1. Not specified.
"""


def render_goal_notes(data: dict[str, Any], today: str) -> str:
    goals = data.get("goals", [])
    chunks = []
    for goal in goals:
        chunks.append(
            f"## {text(goal.get('title'), text(goal.get('id'), 'Goal'))}\n\n"
            f"- Horizon: {text(goal.get('horizon'), 'Not specified')}\n"
            f"- Why: {text(goal.get('why'), 'Not specified')}\n"
            f"- Success: {text(goal.get('success'), 'Not specified')}\n"
            f"- Current state: {text(goal.get('current_state'), 'Not specified')}\n"
            f"- Next step: {text(goal.get('next_step'), 'Not specified')}\n"
        )
    body = "\n".join(chunks) if chunks else "No goals recorded yet."
    return frontmatter("goals", "note", privacy="sensitive", updated=today, role="goals") + "# Goals\n\n" + body


def render_prompt_loader(today: str) -> str:
    return f"""# Load Second Brain Context

Use this prompt when a project or chat needs private second-brain context.

Load order:

1. `AGENTS.md`
2. `profile.md`
3. `notes/answer-contract.md`
4. one relevant `.agents/skills/<skill>/SKILL.md`
5. targeted search in `projects/`, `answers/`, `notes/`, or `inbox/`

Do not load `archive/`, raw inbox, generated files, or all projects unless the
task explicitly needs them.

Updated: {today}
"""


def render_repos(data: dict[str, Any]) -> dict[str, Any]:
    repos: dict[str, Any] = {}
    for repo in as_list(data.get("repos")):
        if not isinstance(repo, dict):
            continue
        rid = slugify(text(repo.get("id") or repo.get("url")), "repo")
        repos[rid] = {
            "url": repo.get("url", ""),
            "local_path": repo.get("local_path", ""),
            "role": repo.get("role", "external_project"),
            "description": repo.get("description", ""),
            "validation": as_list(repo.get("validation")),
            "secret_policy": repo.get("secret_policy", "No secrets in git."),
        }
    return {"version": 1, "repos": repos}


def render_skill_manifest(
    packs: list[str],
    selected: list[str],
    copied: list[str],
    missing: list[str],
) -> dict[str, Any]:
    return {
        "version": 1,
        "selection_mode": "precision_first",
        "selected_packs": packs,
        "selected_skills": selected,
        "copied_skills": copied,
        "missing_skills": missing,
    }


def create_brain(args: argparse.Namespace) -> int:
    intake = load_json(Path(args.input).resolve())
    pack_config = load_json(Path(args.packs).resolve())
    output = Path(args.output).resolve()
    today = args.date or date.today().isoformat()

    if output.exists() and any(output.iterdir()) and not args.force:
        print(f"Output directory is not empty: {output}", file=sys.stderr)
        print("Use --force to overwrite generated files.", file=sys.stderr)
        return 2

    output.mkdir(parents=True, exist_ok=True)

    selected_packs, selected_skills = select_skills(intake, pack_config)
    copied, missing = copy_selected_skills(
        selected_skills,
        Path(args.skill_source).resolve(),
        output / ".agents/skills",
        force=args.force,
    )

    year_month = today[:7]
    files: dict[Path, str] = {
        output / "README.md": render_readme(intake, selected_skills),
        output / "AGENTS.md": render_agents(intake, selected_skills, today),
        output / "profile.md": render_profile(intake, today),
        output / "notes/answer-contract.md": render_answer_contract(intake, selected_skills, today),
        output / "notes/repository-contract.md": render_repository_contract(today),
        output / "notes/privacy-rules.md": render_privacy_rules(intake, today),
        output / "notes/user/personal_model.md": render_personal_model(intake, today),
        output / "notes/user/answer_preferences.md": render_answer_preferences(intake, today),
        output / "notes/goals.md": render_goal_notes(intake, today),
        output / "notes/prompts/README.md": "# Prompt Library\n\nUser-specific prompt patterns go here.\n",
        output / "projects/_index.md": render_projects_index(intake, today),
        output / "tasks.md": render_tasks(intake, today),
        output / "inbox.md": frontmatter("inbox", "inbox", privacy="sensitive", updated=today) + "# Inbox\n\nUnprocessed notes and source snippets go here.\n",
        output / "inbox/README.md": "# Inbox\n\nRaw source packets and temporary captures go here.\n",
        output / "inbox/telegram-raw/README.md": "# Telegram Raw Inbox\n\nRaw Telegram queue, media pointers, transcripts, review sessions, and processed markers live here.\n",
        output / f"answers/{year_month}.md": frontmatter(f"answers_{year_month}", "index", privacy="sensitive", updated=today) + f"# Answers {year_month}\n\nNo answers saved yet.\n",
        output / "answers/question-ledger.md": frontmatter("question_ledger", "index", privacy="sensitive", updated=today) + "# Question Ledger\n\nRecurring questions go here.\n",
        output / ".agents/prompts/load-second-brain-context.md": render_prompt_loader(today),
        output / ".agents/skills/README.md": "# Selected Skills\n\nThis folder contains only selected runtime skills copied from the platform source.\n",
        output / "archive/README.md": "# Archive\n\nFrozen old context goes here. Archive instead of deleting when unsure.\n",
        output / "generated/indexes/.gitkeep": "# generated indexes placeholder\n",
        output / ".gitignore": ".DS_Store\n.env\n.env.*\n__pycache__/\n.pytest_cache/\n.mypy_cache/\n.ruff_cache/\n*.key\n*.pem\n*.p12\n*.pfx\n*.sqlite\n*.sqlite3\n*.db\n*.duckdb\ninbox/telegram-raw/raw/\ngenerated/indexes/*.jsonl\n",
    }

    for subdir in [
        "inbox/telegram-raw/queue",
        "inbox/telegram-raw/raw",
        "inbox/telegram-raw/review_sessions",
        "inbox/telegram-raw/processed",
    ]:
        files[output / subdir / ".gitkeep"] = "# placeholder\n"

    for project in as_list(intake.get("projects")):
        if not isinstance(project, dict):
            continue
        pid = slugify(text(project.get("id") or project.get("title")), "project")
        files[output / f"projects/{pid}.md"] = render_project_hub(project, today)
        files[output / f"projects/{pid}/_index.md"] = render_project_detail(project, today, "index")
        files[output / f"projects/{pid}/tasks.md"] = render_project_detail(project, today, "tasks")
        files[output / f"projects/{pid}/decisions.md"] = render_project_detail(project, today, "decisions")
        for subdir in ["cases", "evidence", "notes", "artifacts", "tickets"]:
            files[output / f"projects/{pid}/{subdir}/.gitkeep"] = "# placeholder\n"

    for path, content in files.items():
        write_file(path, content, force=args.force)

    write_file(
        output / "agent-system/repos.json",
        json.dumps(render_repos(intake), indent=2, ensure_ascii=False),
        force=args.force,
    )
    write_file(
        output / "agent-system/skills/selected.json",
        json.dumps(render_skill_manifest(selected_packs, selected_skills, copied, missing), indent=2, ensure_ascii=False),
        force=args.force,
    )

    print(f"Created second brain at {output}")
    print(f"Selected packs: {', '.join(selected_packs) if selected_packs else 'none'}")
    print(f"Copied skills: {', '.join(copied) if copied else 'none'}")
    if missing:
        print(f"Missing skills: {', '.join(missing)}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to intake JSON.")
    parser.add_argument("--output", required=True, help="Output directory for the new private brain.")
    parser.add_argument("--packs", default=str(DEFAULT_PACKS), help="Skill pack configuration JSON.")
    parser.add_argument("--skill-source", default=str(DEFAULT_SKILL_SOURCE), help="Directory containing local skill folders.")
    parser.add_argument("--date", default="", help="Override updated date, YYYY-MM-DD.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated files and copied skills.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    return create_brain(args)


if __name__ == "__main__":
    raise SystemExit(main())
