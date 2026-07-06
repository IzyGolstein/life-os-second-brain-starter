# Full Stack Setup For Codex

Use this when a new Codex thread should bootstrap the whole second-brain setup
for a new user.

## Public Repositories

Starter repo:

```bash
git clone https://github.com/IzyGolstein/life-os-second-brain-starter.git
```

Life OS Core backend:

```bash
git clone https://github.com/IzyGolstein/life-os-core.git
```

Life OS Plane UI fork:

```bash
git clone https://github.com/IzyGolstein/life-os-plane.git
```

Telegram bot public repo target:

```bash
git clone https://github.com/IzyGolstein/life-os-telegram-inbox-bot.git
```

If the Telegram bot clone returns 404, the public repo has not been published
yet. Ask Alex to explicitly approve publishing the sanitized bot code, then run:

```bash
cd "/Users/alex/Documents/New project/telegram-inbox-bot"
gh repo create IzyGolstein/life-os-telegram-inbox-bot --public --source=. --remote=public --push
```

Do not publish private repositories without explicit approval.

## What Codex Should Do

Fast path:

```bash
git clone https://github.com/IzyGolstein/life-os-second-brain-starter.git
cd life-os-second-brain-starter
python3 scripts/setup_full_stack.py \
  --workspace ~/second-brain-stack \
  --user-id new-user \
  --with-telegram \
  --with-core \
  --with-plane
```

This creates a draft intake at:

```text
~/second-brain-stack/new-user-intake.json
```

Edit it, then generate the private brain:

```bash
python3 scripts/setup_full_stack.py \
  --workspace ~/second-brain-stack \
  --user-id new-user \
  --intake ~/second-brain-stack/new-user-intake.json \
  --with-telegram \
  --with-core \
  --with-plane \
  --generate
```

Manual Codex flow:

Paste this into Codex:

```text
You are Codex setting up a new user's second-brain stack.

Use these public repos:
- starter: https://github.com/IzyGolstein/life-os-second-brain-starter
- Life OS Core backend: https://github.com/IzyGolstein/life-os-core
- Life OS Plane UI fork: https://github.com/IzyGolstein/life-os-plane
- Telegram bot: https://github.com/IzyGolstein/life-os-telegram-inbox-bot

Goal:
Clone the starter repo, ask me the intake questions, generate a private brain
repo, optionally configure Telegram capture, and optionally clone Life OS Core
plus the Life OS Plane UI as the work-surface stack.

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
- INBOX_REPO_SSH_URL
- INBOX_REPO_BRANCH
- TIMEZONE

Do not ask me to paste the bot token into chat. Tell me to edit `.env` locally.

The current Telegram bot writes to a Git inbox repository through
`INBOX_REPO_SSH_URL`. For the Life OS target layout, that inbox repo should be
the new user's private brain repo or a dedicated private raw inbox repo that is
later migrated into `<user>-brain/inbox/telegram-raw/`.

Step 5 - Optional Life OS Core:

If Plane UI is enabled, Life OS Core is required. It serves the local Life OS
API used by chat, wiki, project pages, project files, task bridge endpoints,
and lightweight Plane-compatible API routes.

git clone https://github.com/IzyGolstein/life-os-core.git
cd life-os-core
python3 run_backend.py --host 127.0.0.1 --port 8765

Verify:
- http://127.0.0.1:8765/health returns ok.

Step 6 - Optional Plane:

If Plane UI is enabled:

git clone https://github.com/IzyGolstein/life-os-plane.git
cd life-os-plane
npm exec --yes pnpm@11.3.0 -- install --frozen-lockfile
npm exec --yes pnpm@11.3.0 -- turbo run build --filter=web^...

Run the Life OS Plane UI against Life OS Core:

env VITE_LIFE_OS_PLANE_MODE=1 \
  VITE_LIFE_OS_BRIDGE_TARGET=http://127.0.0.1:8765 \
  VITE_API_PROXY_TARGET=http://127.0.0.1:8765 \
  npm exec --yes pnpm@11.3.0 -- --filter=web dev

Verify:
- http://127.0.0.1:3000/life-os/chat
- http://127.0.0.1:3000/life-os/wiki
- http://127.0.0.1:3000/life-os/projects/life-os-plane/issues

The private brain remains canonical Markdown. Do not store private profile,
answers, or raw inbox inside Plane-only storage.

Step 7 - Optional project repos:

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
