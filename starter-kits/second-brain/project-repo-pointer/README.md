# Project Repo Pointer

Ordinary project repositories should stay ordinary: easy to clone, run, test,
and review. They should not contain a user's private second brain.

Install the compact pointer:

```bash
python3 /path/to/life-os/scripts/install_second_brain_pointer.py \
  --target /path/to/project-repo
```

The installer creates or updates:

```text
AGENTS.md
```

The pointer tells agents how to resolve `SECOND_BRAIN_PATH` only when private
context is actually needed. It does not copy profile, answers, inbox, projects,
or secrets into the code repo.

