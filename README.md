# Life OS Second Brain Starter

Clean starter repository for generating private Markdown second-brain repos for
new users.

This repo contains reusable starter logic only:

- intake questions;
- private brain generator;
- precision-first skill pack selection;
- portable skills;
- ordinary project repo pointer installer.

It must not contain any user's private profile, answers, inbox, projects,
attachments, credentials, or raw media.

## Quick Start

Use a fresh Codex thread and paste:

```text
.agents/prompts/paste-into-codex-bootstrap-second-brain.md
```

Or run manually:

```bash
python3 scripts/bootstrap_second_brain_user.py   --input starter-kits/second-brain/examples/sample-intake.json   --output /tmp/example-brain
```

For ordinary project repos:

```bash
python3 scripts/install_second_brain_pointer.py --target /path/to/project
```

The generated brain repo should be private by default.
