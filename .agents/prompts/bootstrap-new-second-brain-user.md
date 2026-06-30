# Bootstrap New Second Brain User

Use this prompt when creating a private second-brain repository for a new user
from the portable Life OS starter kit.

```text
You are Codex bootstrapping a new private second-brain repository.

Goal:
Generate a clean Markdown brain for a new user without copying another user's
private memory.

Inputs:
- PLATFORM_REPO_PATH: this Life OS/platform checkout.
- INTAKE_JSON: path to the completed intake JSON.
- OUTPUT_BRAIN_PATH: empty target directory for the new private brain.

Workflow:
1. Read:
   - starter-kits/second-brain/README.md
   - starter-kits/second-brain/skill-selection/README.md
   - starter-kits/second-brain/skill-selection/starter-skill-packs.json
2. Validate that INTAKE_JSON contains:
   - user;
   - answer_preferences;
   - at least one goal or project;
   - domains or explicit skill_packs;
   - privacy.never_store.
3. Run:

   python3 scripts/bootstrap_second_brain_user.py \
     --input INTAKE_JSON \
     --output OUTPUT_BRAIN_PATH

4. Inspect generated:
   - AGENTS.md
   - profile.md
   - notes/answer-contract.md
   - agent-system/skills/selected.json
   - projects/_index.md
5. Do not push or publish the generated repo unless the user explicitly asks.
6. For ordinary code repos, install only the compact pointer from:
   starter-kits/second-brain/project-repo-pointer/AGENTS.pointer.md

Final response:
- Generated brain path:
- Selected skill packs:
- Selected skills:
- Missing skills, if any:
- Files to review first:
- Next command to initialize private Git repo:
```

