#!/usr/bin/env python3
"""Prepare a Life OS + Telegram + Plane workspace for a new user."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_STARTER_REPO = "https://github.com/IzyGolstein/life-os-second-brain-starter.git"
DEFAULT_TELEGRAM_REPO = "https://github.com/IzyGolstein/life-os-telegram-inbox-bot.git"
DEFAULT_PLANE_REPO = "https://github.com/IzyGolstein/life-os-plane.git"


def run(cmd: list[str], cwd: Path | None = None, *, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd, text=True, check=False)
    if check and result.returncode != 0:
        raise SystemExit(result.returncode)
    return result


def clone_or_pull(url: str, path: Path) -> None:
    if (path / ".git").is_dir():
        run(["git", "pull", "--ff-only"], cwd=path)
        return
    if path.exists() and any(path.iterdir()):
        raise SystemExit(f"Refusing to clone into non-empty directory: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    run(["git", "clone", url, str(path)])


def write_default_intake(path: Path, user_id: str) -> None:
    if path.exists():
        return
    intake = {
        "user": {
            "id": user_id,
            "preferred_name": user_id,
            "display_name": user_id,
            "timezone": "UTC",
            "languages": ["en"],
            "default_answer_language": "en",
            "short_profile": ["Replace this with 2-4 concrete bullets."],
        },
        "answer_preferences": {
            "tone": "direct, operational",
            "default_length": "compact",
            "depth_rule": "Use deep analysis only for important decisions.",
            "browse_policy": "Browse for current or high-stakes facts.",
            "citation_policy": "Cite external factual sources when used.",
            "save_policy": "Ask before changing core memory.",
            "bad_answer_patterns": ["Generic advice", "Invented context"],
            "excellent_answer_patterns": ["Clear judgment", "Concrete next step"],
        },
        "goals": [],
        "domains": ["coding", "research", "product"],
        "skill_packs": ["core"],
        "projects": [],
        "repos": [],
        "integrations": {
            "telegram": {"enabled": False},
            "voice_transcription": {"enabled": False},
            "plane": {"enabled": False},
        },
        "privacy": {
            "default": "sensitive",
            "never_store": ["passwords", "API keys", "private keys", "bank access"],
            "shareable_with_team": ["generic prompts", "skills without private examples"],
            "private": ["profile", "raw inbox", "personal strategy", "private project notes"],
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(intake, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True, help="Directory that will contain all cloned/generated repos.")
    parser.add_argument("--user-id", required=True, help="Slug for the new user's private brain.")
    parser.add_argument("--intake", default="", help="Path to completed intake JSON. If omitted, a draft is created.")
    parser.add_argument("--starter-repo", default=DEFAULT_STARTER_REPO)
    parser.add_argument("--telegram-repo", default=DEFAULT_TELEGRAM_REPO)
    parser.add_argument("--plane-repo", default=DEFAULT_PLANE_REPO)
    parser.add_argument("--with-telegram", action="store_true")
    parser.add_argument("--with-plane", action="store_true")
    parser.add_argument("--generate", action="store_true", help="Generate the private brain from the intake JSON.")
    args = parser.parse_args(argv)

    workspace = Path(args.workspace).expanduser().resolve()
    workspace.mkdir(parents=True, exist_ok=True)

    starter_path = workspace / "life-os-second-brain-starter"
    brain_path = workspace / f"{args.user_id}-brain"
    intake_path = Path(args.intake).expanduser().resolve() if args.intake else workspace / f"{args.user_id}-intake.json"

    clone_or_pull(args.starter_repo, starter_path)
    write_default_intake(intake_path, args.user_id)

    if args.generate:
        run(
            [
                sys.executable,
                "scripts/bootstrap_second_brain_user.py",
                "--input",
                str(intake_path),
                "--output",
                str(brain_path),
                "--force",
            ],
            cwd=starter_path,
        )
    else:
        print(f"Draft intake created at: {intake_path}")
        print("Edit the intake JSON, then rerun with --generate.")

    if args.with_telegram:
        telegram_path = workspace / "life-os-telegram-inbox-bot"
        clone_or_pull(args.telegram_repo, telegram_path)
        env_example = telegram_path / ".env.example"
        env_file = telegram_path / ".env"
        if env_example.exists() and not env_file.exists():
            env_file.write_text(env_example.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Telegram bot repo: {telegram_path}")
        print("Edit .env locally. Do not paste BOT_TOKEN into chat.")

    if args.with_plane:
        plane_path = workspace / "plane"
        clone_or_pull(args.plane_repo, plane_path)
        print(f"Plane repo: {plane_path}")
        print("Use LIFE_OS_SETUP.md in the Plane repo to run the Life OS Plane UI. Private brain remains canonical Markdown.")

    print("\nSummary")
    print(f"- Workspace: {workspace}")
    print(f"- Starter: {starter_path}")
    print(f"- Intake: {intake_path}")
    print(f"- Private brain target: {brain_path}")
    print(f"- Telegram: {'enabled' if args.with_telegram else 'skipped'}")
    print(f"- Plane: {'enabled' if args.with_plane else 'skipped'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
