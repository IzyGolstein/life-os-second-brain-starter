#!/usr/bin/env python3
"""Install a compact second-brain pointer into a project AGENTS.md."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POINTER = ROOT / "starter-kits/second-brain/project-repo-pointer/AGENTS.pointer.md"
MARKER = "Optional Second Brain Context"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Target project directory.")
    parser.add_argument("--pointer", default=str(DEFAULT_POINTER), help="Pointer markdown file.")
    parser.add_argument("--force", action="store_true", help="Rewrite an existing pointer block if present.")
    return parser.parse_args(argv)


def install_pointer(target: Path, pointer_path: Path, *, force: bool) -> int:
    if not target.is_dir():
        print(f"Target is not a directory: {target}", file=sys.stderr)
        return 2
    pointer = pointer_path.read_text(encoding="utf-8").rstrip() + "\n"
    agents = target / "AGENTS.md"

    if not agents.exists():
        agents.write_text(pointer, encoding="utf-8")
        print(f"Created {agents}")
        return 0

    current = agents.read_text(encoding="utf-8")
    if MARKER in current and not force:
        print(f"Pointer already present in {agents}")
        return 0

    if MARKER in current and force:
        before = current.split(f"# {MARKER}", 1)[0].rstrip()
        current = before + "\n\n"

    updated = current.rstrip() + "\n\n" + pointer
    agents.write_text(updated, encoding="utf-8")
    print(f"Updated {agents}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    return install_pointer(Path(args.target).resolve(), Path(args.pointer).resolve(), force=args.force)


if __name__ == "__main__":
    raise SystemExit(main())

