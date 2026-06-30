# Full Stack Setup For Codex

Use this when a new Codex thread should bootstrap the whole second-brain setup
for a new user.

## Public Repositories

Starter repo:

```bash
git clone https://github.com/IzyGolstein/life-os-second-brain-starter.git
```

Plane upstream:

```bash
git clone https://github.com/makeplane/plane.git
```

Telegram bot public repo target:

```bash
git clone https://github.com/IzyGolstein/life-os-telegram-inbox-bot.git
```

If the Telegram bot clone returns 404, the public repo has not been published
yet. Ask the user to explicitly approve publishing the sanitized bot code, then run:

```bash
cd "/Users/user/Documents/New project/telegram-inbox-bot"
gh repo create IzyGolstein/life-os-telegram-inbox-bot --public --source=. --remote=public --push
```

Do not publish private repositories without explicit approval.

## What Codex Should Do

Paste this into Codex:

```text
You are Codex setting up a new user's second-brain stack.

Use these public repos:
- starter: https://github.com/IzyGolstein/life-os-second-brain-starter
- Plane upstream: https://github.com/makeplane/plane
- Telegram bot: https://github.com/IzyGolstein/life-os-telegram-inbox-bot

Goal:
Clone the starter repo, ask me the intake questions, generate a private brain
repo, optionally configure Telegram capture, and optionally clone Plane as the
work-surface base.

Step 1 - Clone starter:

git clone https://github.com/IzyGolstein/life-os-second-brain-starter.git
cd life-os-second-brain-starter

Read:
- README.md
- AGENTS.md
- starter-kits/second-brain/README.md
- starter-kits/second-brain/intake/second-brain-intake.md
- starter-kits/second-brain/skill-selection/starter-skill-packs.json

Step 2 - Ask intake questions in compact batches:

Batch A:
- Preferred name and display name?
- Timezone?
- Main languages and default answer language?
- 2-4 bullets describing the person?
- Preferred tone?
- Default answer length?
- What makes an answer bad?
- What makes an answer excellent?

Batch B:
- Active goals: id, title, horizon, why, success condition, current state, next step.
- Active projects: id, title, status, goal, context, out of scope, key files/repos/links, next actions, definition of done, privacy.

Batch C:
Which domains are useful now?
coding, frontend, provider_adapter, research, product, career, admissions,
english, ml, psychology, job_search, personal_planning.

Batch D:
- External project repos: id, Git URL, local path, role, validation commands, secret policy.
- Telegram capture: yes/no?
- Voice transcription: yes/no?
- Plane UI: yes/no?
- GitHub/Drive/Docs/Sheets/Slides: yes/no?

Batch E:
- Default privacy: public/internal/sensitive?
- What must never be stored?
- What can be shared with team/household?
- Which skills/prompts may be shared?
- Which skills/prompts contain private examples and must not be shared?

Step 3 - Generate private brain:

Create intake JSON under /tmp/<user_id>-second-brain-intake.json.
Ask me for OUTPUT_BRAIN_PATH.

Run:

python3 scripts/bootstrap_second_brain_user.py \
  --input /tmp/<user_id>-second-brain-intake.json \
  --output <OUTPUT_BRAIN_PATH>

Verify:
- AGENTS.md
- profile.md
- notes/answer-contract.md
- notes/user/personal_model.md
- notes/privacy-rules.md
- projects/_index.md
- agent-system/skills/selected.json
- agent-system/repos.json

Run:
- python3 -m json.tool agent-system/skills/selected.json
- python3 -m json.tool agent-system/repos.json
- find .agents/skills -maxdepth 2 -name SKILL.md | wc -l

Step 4 - Optional Telegram:

If Telegram capture is enabled:

git clone https://github.com/IzyGolstein/life-os-telegram-inbox-bot.git
cd life-os-telegram-inbox-bot
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -e .
cp .env.example .env

Tell me to fill `.env` with:
- BOT_TOKEN
- ALLOWED_TELEGRAM_IDS
- INBOX_REPO_SSH_URL or local raw inbox path, depending on deployment
- INBOX_REPO_BRANCH
- TIMEZONE

Do not ask me to paste the bot token into chat. Tell me to edit `.env` locally.

Step 5 - Optional Plane:

If Plane UI is enabled:

git clone https://github.com/makeplane/plane.git

Use Plane as the work surface. The private brain remains canonical Markdown.
Do not store private profile, answers, or raw inbox inside Plane-only storage.
If a Life OS Plane fork URL is provided later, use that fork instead of upstream.

Step 6 - Optional project repos:

For each ordinary project repo I approve, run from the starter repo:

python3 scripts/install_second_brain_pointer.py --target <project-repo-path>

Final response:
- Starter repo path
- Private brain path
- Selected skill packs
- Selected skills
- Telegram configured or skipped
- Plane cloned/configured or skipped
- Project repos updated
- Commands run
- Remaining blockers
```

