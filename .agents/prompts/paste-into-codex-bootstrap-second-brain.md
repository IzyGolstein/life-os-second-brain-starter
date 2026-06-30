# Paste Into Codex: Bootstrap Second Brain For New User

Copy the text below into a fresh Codex thread when you want Codex to set up a
new user's private second-brain repository from the portable starter kit.

```text
You are Codex bootstrapping a private Markdown second-brain repository for a new user.

Goal:
Create a fully working private second-brain repo for the new user from the Life OS portable starter kit. Ask me the needed questions in chat, generate the intake JSON yourself, run the bootstrap scripts, inspect the generated files, and tell me exactly what to review next.

Important safety rules:
- Do not copy another person's private memory into the new user's repo.
- Do not store secrets: passwords, API keys, private keys, seed phrases, bank access, tokens, credentials.
- If the platform repo contains private memory, do not make it public and do not use it as a public starter.
- Ordinary project/code repos should get only a compact second-brain pointer, not a copy of the user's private brain.
- Browse/clone only after you have a repo URL or local path.

Inputs I may provide:
- PLATFORM_REPO_URL: URL of the sanitized Life OS platform/starter repo.
- PLATFORM_REPO_PATH: local path if the platform repo is already cloned.
- OUTPUT_BRAIN_PATH: local directory for the new private brain repo.
- OPTIONAL_PROJECT_REPOS: code/project repos that should receive a second-brain pointer.

If any input is missing, ask me for it. If I do not have a public/sanitized platform repo yet, tell me that this is required before sharing with unrelated users, and continue only if I provide a trusted local platform path.

Step 1 - Get or locate the platform repo:
1. If PLATFORM_REPO_PATH exists locally, use it.
2. Else clone PLATFORM_REPO_URL into a local folder.
3. Run `git pull --ff-only` inside the platform repo before reading files.
4. Verify these files exist:
   - starter-kits/second-brain/README.md
   - starter-kits/second-brain/intake/second-brain-intake.md
   - starter-kits/second-brain/skill-selection/starter-skill-packs.json
   - starter-kits/second-brain/examples/sample-intake.json
   - scripts/bootstrap_second_brain_user.py
   - scripts/install_second_brain_pointer.py
   - starter-kits/second-brain/project-repo-pointer/AGENTS.pointer.md

Step 2 - Ask me the intake questions:
Ask in compact batches, not one huge wall of text. Collect:

Batch A - identity and answer style:
- Preferred name and display name?
- Timezone?
- Main languages and default answer language?
- 2-4 bullets describing the person?
- Preferred tone: direct, gentle, academic, operational, tutor-like, other?
- Default answer length: terse, compact, medium, deep?
- What makes an answer bad?
- What makes an answer excellent?

Batch B - goals and projects:
- Active goals: id, title, horizon, why, success condition, current state, next step.
- Active projects: id, title, status, goal, context, out of scope, key files/repos/links, next actions, definition of done, privacy level.

Batch C - domains and skills:
Ask which domains are actually useful now:
- coding
- frontend
- provider_adapter
- research
- product
- career
- admissions
- english
- ml
- psychology
- job_search
- personal_planning

Use precision-first selection. Do not select a domain unless the user says it is useful now.

Batch D - repositories and integrations:
- External project repos: id, Git URL, local path if known, role, validation commands, secret policy.
- Telegram capture: yes/no.
- Voice transcription: yes/no.
- Plane UI: yes/no.
- GitHub/Drive/Docs/Sheets/Slides or other integrations: yes/no.

Batch E - privacy and sharing:
- Default privacy: public/internal/sensitive.
- What must never be stored?
- What can be shared with a team/household?
- Which skills/prompts may be shared?
- Which skills/prompts contain private examples and must not be shared?

Step 3 - Build the intake JSON:
Create a JSON file based on:
starter-kits/second-brain/examples/sample-intake.json

Save it as:
starter-kits/second-brain/generated-intakes/<user_id>-intake.json

If that path is inside a shared platform repo, make sure it does not include secrets. If the answers are sensitive, save the intake under /tmp instead and say where it is.

Step 4 - Generate the private brain:
Run:

python3 scripts/bootstrap_second_brain_user.py \
  --input <intake-json-path> \
  --output <OUTPUT_BRAIN_PATH>

If OUTPUT_BRAIN_PATH is missing, ask me for it. It should be an empty directory for the new private brain.

Step 5 - Verify generated repo:
Inspect:
- AGENTS.md
- README.md
- profile.md
- notes/answer-contract.md
- notes/user/personal_model.md
- notes/user/answer_preferences.md
- notes/privacy-rules.md
- projects/_index.md
- agent-system/skills/selected.json
- agent-system/repos.json
- .agents/skills/

Run:
- `python3 -m json.tool agent-system/skills/selected.json`
- `python3 -m json.tool agent-system/repos.json`
- `find .agents/skills -maxdepth 2 -name SKILL.md | wc -l`

Step 6 - Initialize private Git repo:
If I approve, run inside OUTPUT_BRAIN_PATH:

git init
git add .
git commit -m "Initialize private second brain"

Do not push unless I provide a private remote URL and explicitly ask you to push.

Step 7 - Add pointer to ordinary project repos:
For each OPTIONAL_PROJECT_REPO I approve, run from the platform repo:

python3 scripts/install_second_brain_pointer.py --target <project-repo-path>

This should create/update only AGENTS.md in the project repo. It must not copy profile, answers, inbox, projects, or skills into the project repo.

Final response:
- Platform repo used:
- New private brain path:
- Intake JSON path:
- Selected skill packs:
- Selected skills:
- Missing skills, if any:
- Generated files checked:
- Optional project repos updated:
- Git status / commit result:
- What the new user should review first:
```

