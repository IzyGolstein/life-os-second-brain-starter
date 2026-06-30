# AGENTS.md

This repository is a clean public starter for generating private second-brain
repositories.

## Rules

- Do not add private user memory to this repo.
- Do not add secrets, tokens, credentials, raw inbox exports, or attachments.
- Keep starter files generic and portable.
- Use `starter-kits/second-brain/intake/second-brain-intake.md` for user
  questions.
- Use `scripts/bootstrap_second_brain_user.py` to generate private user brains.
- Use precision-first skill selection from
  `starter-kits/second-brain/skill-selection/starter-skill-packs.json`.
- Ordinary project repos receive only the compact pointer from
  `starter-kits/second-brain/project-repo-pointer/AGENTS.pointer.md`.

## Validation

```bash
python3 -m py_compile scripts/bootstrap_second_brain_user.py scripts/install_second_brain_pointer.py
python3 -m json.tool starter-kits/second-brain/examples/sample-intake.json
python3 -m json.tool starter-kits/second-brain/skill-selection/starter-skill-packs.json
python3 scripts/bootstrap_second_brain_user.py --input starter-kits/second-brain/examples/sample-intake.json --output /tmp/life-os-starter-smoke --force
```
