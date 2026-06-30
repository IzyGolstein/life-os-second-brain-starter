# Portable Second Brain Starter Kit

This kit creates a private Markdown second-brain repository for a new user while
keeping reusable product logic, skills, prompts, and platform code shareable.

The target split is:

```text
life-os-platform or source repo
  public/reusable code, schemas, skills, prompts, bootstrap scripts

<user>-brain
  private profile, answer preferences, goals, project context, inbox, answers

ordinary project repos
  public or private code/data repos with only a small second-brain pointer
```

Do not clone another person's private brain as a starter. Generate a fresh brain
from an intake form and copy only selected runtime skills.

## Quick Start

1. Fill the intake:

   ```text
   starter-kits/second-brain/intake/second-brain-intake.md
   ```

2. Convert the answers into JSON using the sample shape:

   ```text
   starter-kits/second-brain/examples/sample-intake.json
   ```

3. Generate a private brain repo:

   ```bash
   python3 scripts/bootstrap_second_brain_user.py \
     --input starter-kits/second-brain/examples/sample-intake.json \
     --output /path/to/new-user-brain
   ```

4. Initialize Git in the generated repo and push it to a private repository.

5. For ordinary code/project repositories, add only the pointer from:

   ```text
   starter-kits/second-brain/project-repo-pointer/AGENTS.pointer.md
   ```

## What The Generator Creates

```text
AGENTS.md
README.md
profile.md
inbox.md
tasks.md
notes/
  answer-contract.md
  repository-contract.md
  privacy-rules.md
  user/
    personal_model.md
    answer_preferences.md
  prompts/
projects/
  _index.md
  <project>.md
  <project>/
    _index.md
    tasks.md
    decisions.md
answers/
  YYYY-MM.md
  question-ledger.md
inbox/
  telegram-raw/
agent-system/
  repos.json
  skills/selected.json
.agents/
  skills/
  prompts/load-second-brain-context.md
archive/
generated/indexes/
```

The active context is intentionally small. `profile.md` and
`notes/answer-contract.md` are the only default preload files. Detailed user
facts, projects, answers, and inbox items are loaded only when the current task
requires them.

## Skill Strategy

Use precision-first selection:

- always install the small core pack;
- add coding, research, product, career, admissions, English, ML, or frontend
  packs only when the intake explicitly names those domains;
- keep external skill repositories as source/provenance catalogs, not bulk
  runtime dependencies;
- avoid copying personal examples from another user;
- record selected skills in `agent-system/skills/selected.json`.

The selection rules live in:

```text
starter-kits/second-brain/skill-selection/
```

## Ordinary Project Repos

Project repos should be easy to clone and run. They should not contain a user's
private second brain.

Add only:

```text
AGENTS.md
```

with a compact pointer explaining how an agent can find the user's private
second brain when needed. The pointer must not include personal profile text,
answer history, raw inbox content, or secrets.

