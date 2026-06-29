# SaaS Course Skills

This folder contains reusable AI-agent skills for building, reviewing, testing, deploying, and growing SaaS products.

Most installable skills are directories with a `SKILL.md` file. Some top-level markdown files are source notes, not installable skills.

## What This Folder Does

Use these skills to make AI development more consistent across SaaS projects:

- Plan SaaS products with a spec-first workflow before coding.
- Keep dashboard, CRUD, workflow, auth, roles, billing, and tenancy requirements visible.
- Add product-growth thinking while building: onboarding, activation, free tools, referrals, shareable reports, white-label, lifecycle email, SEO/GEO, and customer success loops.
- Follow MDN web standards during frontend work.
- Test local websites with Playwright-style browser QA.
- Prepare apps for Dublyo deployment and related PocketBase/tag-manager workflows.
- Keep small implementation tasks lean when that is the right mode.

## Installable Skills

| Folder | Skill name | What it does |
| --- | --- | --- |
| `saas-kit` | `saas-kit` | Full Spec Kit-inspired SaaS planning workflow: questions, spec, plan, tasks, approval before coding. |
| `saas-product-growth` | `saas-product-growth` | SaaS architecture plus monetization, operations, PocketBase/Supabase mapping, and growth loops to consider during development. |
| `moat` | `moat` | Evaluate and design SaaS moats that protect retention, pricing power, CAC efficiency, gross margin, and profitability. |
| `mdn-web-best-practices` | `mdn-web-best-practices` | Frontend/web build and audit guidance based on MDN standards. |
| `playwright-website-tester` | `playwright-website-tester` | Website QA workflow for routes, forms, console errors, screenshots, responsive checks, and browser-visible issues. |
| `image-to-code-skill` | `image-to-code` | Image-first premium website design-to-code workflow for visually important web pages. |
| `dublyo-deploy` | `dublyo-deploy` | Prepare and deploy containerized apps to Dublyo conventions. |
| `pocketbase` | `dublyo-pocketbase` | PocketBase-on-Dublyo architecture, collection/API work, and custom-logic guidance. |
| `tag-manager-server` | `dublyo-tag-manager-server` | Server-side GTM, pixels, conversion APIs, and SaaS tracking setup on Dublyo. |
| `lean-code` | `lean-code` | Keep implementation minimal and focused on the direct request. |
| `brandkit` | `brandkit` | Create premium brand-kit image concepts and visual systems. |
| `taste-skill-v1` | `design-taste-frontend-v1` | Preserved v1 frontend taste/design behavior for backward compatibility. |

## Source Notes

These files are not installable skills by themselves:

- `saas-componenets.md`: original SaaS component checklist source. The filename is kept as-is.
- `saas-marketing.md`: original SaaS marketing/growth source.

Their content has been converted into `saas-product-growth/references/`.

## Install To Codex

Codex reads local skills from `.agents/skills` locations and supports symlinked skill folders. The most portable user-level install is:

```bash
SRC="/Users/dribrahimm/3-SaaS-Course/skills"
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"

ln -sfn "$SRC/saas-kit" "$DEST/saas-kit"
ln -sfn "$SRC/saas-product-growth" "$DEST/saas-product-growth"
ln -sfn "$SRC/moat" "$DEST/moat"
ln -sfn "$SRC/mdn-web-best-practices" "$DEST/mdn-web-best-practices"
ln -sfn "$SRC/playwright-website-tester" "$DEST/playwright-website-tester"
ln -sfn "$SRC/image-to-code-skill" "$DEST/image-to-code"
ln -sfn "$SRC/dublyo-deploy" "$DEST/dublyo-deploy"
ln -sfn "$SRC/pocketbase" "$DEST/dublyo-pocketbase"
ln -sfn "$SRC/tag-manager-server" "$DEST/dublyo-tag-manager-server"
ln -sfn "$SRC/lean-code" "$DEST/lean-code"
ln -sfn "$SRC/brandkit" "$DEST/brandkit"
ln -sfn "$SRC/taste-skill-v1" "$DEST/design-taste-frontend-v1"
```

Restart Codex if the skills do not appear. In Codex, invoke a skill directly with `$skill-name`, for example:

```text
Use $saas-kit to spec this SaaS before coding.
Use $saas-product-growth to review the app for missing SaaS components and growth loops.
Use $moat to review whether the SaaS idea has structural defensibility and profit protection.
```

For repo-scoped Codex skills, copy or symlink selected folders into a project at:

```text
.agents/skills/
```

## Install To Claude

For Claude Code or other local Claude setups that support Agent Skills, use `~/.claude/skills` for personal skills:

```bash
SRC="/Users/dribrahimm/3-SaaS-Course/skills"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

ln -sfn "$SRC/saas-kit" "$DEST/saas-kit"
ln -sfn "$SRC/saas-product-growth" "$DEST/saas-product-growth"
ln -sfn "$SRC/moat" "$DEST/moat"
ln -sfn "$SRC/mdn-web-best-practices" "$DEST/mdn-web-best-practices"
ln -sfn "$SRC/playwright-website-tester" "$DEST/playwright-website-tester"
ln -sfn "$SRC/image-to-code-skill" "$DEST/image-to-code"
ln -sfn "$SRC/dublyo-deploy" "$DEST/dublyo-deploy"
ln -sfn "$SRC/pocketbase" "$DEST/dublyo-pocketbase"
ln -sfn "$SRC/tag-manager-server" "$DEST/dublyo-tag-manager-server"
ln -sfn "$SRC/lean-code" "$DEST/lean-code"
ln -sfn "$SRC/brandkit" "$DEST/brandkit"
ln -sfn "$SRC/taste-skill-v1" "$DEST/design-taste-frontend-v1"
```

For project-scoped Claude skills, use:

```text
.claude/skills/
```

For Claude.ai custom-skill upload, package one skill at a time and upload it through the Claude skills UI:

```bash
cd /Users/dribrahimm/3-SaaS-Course/skills/saas-product-growth
zip -r /tmp/saas-product-growth.zip .
```

If the UI expects the folder itself instead of the folder contents, zip from the parent directory instead:

```bash
cd /Users/dribrahimm/3-SaaS-Course/skills
zip -r /tmp/saas-product-growth-folder.zip saas-product-growth
```

## Install To Cursor

Cursor is best handled through Rules or `AGENTS.md`, not by assuming it will load every `SKILL.md` folder directly.

Project rule option:

```bash
mkdir -p .cursor/rules
cat > .cursor/rules/saas-course-skills.mdc <<'EOF'
---
description: Use these local SaaS course skills when planning, building, reviewing, testing, or deploying SaaS apps.
alwaysApply: false
---

Use the local skill docs from /Users/dribrahimm/3-SaaS-Course/skills.

When planning a SaaS product, read:
- /Users/dribrahimm/3-SaaS-Course/skills/saas-kit/SKILL.md

When reviewing SaaS architecture, monetization, operations, PocketBase/Supabase mapping, or product-growth loops, read:
- /Users/dribrahimm/3-SaaS-Course/skills/saas-product-growth/SKILL.md

When reviewing SaaS defensibility, structural moat, retention, switching costs, pricing power, CAC, margin, or profitability, read:
- /Users/dribrahimm/3-SaaS-Course/skills/moat/SKILL.md

When doing frontend or browser QA work, read the relevant skill:
- /Users/dribrahimm/3-SaaS-Course/skills/mdn-web-best-practices/SKILL.md
- /Users/dribrahimm/3-SaaS-Course/skills/playwright-website-tester/SKILL.md
- /Users/dribrahimm/3-SaaS-Course/skills/image-to-code-skill/SKILL.md

When deploying to Dublyo or working with Dublyo PocketBase/tracking, read the relevant skill:
- /Users/dribrahimm/3-SaaS-Course/skills/dublyo-deploy/SKILL.md
- /Users/dribrahimm/3-SaaS-Course/skills/pocketbase/SKILL.md
- /Users/dribrahimm/3-SaaS-Course/skills/tag-manager-server/SKILL.md

Follow each selected SKILL.md first, then load referenced files only when needed.
EOF
```

User/global Cursor option:

- Open Cursor settings.
- Add a User Rule that points to this folder and tells Cursor to read the relevant `SKILL.md` file before acting.
- Keep the rule short; let the individual skill references carry the details.

## Copy Instead Of Symlink

If an app does not follow symlinks reliably, copy the folders instead:

```bash
SRC="/Users/dribrahimm/3-SaaS-Course/skills"
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"

cp -R "$SRC/saas-kit" "$DEST/saas-kit"
cp -R "$SRC/saas-product-growth" "$DEST/saas-product-growth"
cp -R "$SRC/moat" "$DEST/moat"
```

For folders whose directory name differs from the skill `name`, copy into the skill-name destination:

```bash
cp -R "$SRC/pocketbase" "$DEST/dublyo-pocketbase"
cp -R "$SRC/tag-manager-server" "$DEST/dublyo-tag-manager-server"
cp -R "$SRC/taste-skill-v1" "$DEST/design-taste-frontend-v1"
cp -R "$SRC/image-to-code-skill" "$DEST/image-to-code"
```

## Recommended Usage

For SaaS work, use these together:

```text
Use $saas-kit first to create the spec and implementation plan.
Then use $saas-product-growth to check SaaS components, monetization, operations, and growth loops.
Use $moat to test whether the idea has structural defensibility and a path to durable profit.
Use $mdn-web-best-practices for frontend implementation.
Use $image-to-code when visual landing-page quality matters.
Use $playwright-website-tester before calling the app done.
Use $dublyo-deploy when preparing for Dublyo hosting.
```

For PocketBase or Supabase-heavy SaaS apps:

```text
Use $saas-product-growth and load its PocketBase/Supabase mapping reference.
If the app is PocketBase on Dublyo, also use $dublyo-pocketbase.
```

## Validate Skills

For Codex-style validation, run:

```bash
python3 /Users/dribrahimm/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dribrahimm/3-SaaS-Course/skills/saas-kit
python3 /Users/dribrahimm/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dribrahimm/3-SaaS-Course/skills/saas-product-growth
python3 /Users/dribrahimm/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dribrahimm/3-SaaS-Course/skills/moat
```

Run validation after editing any `SKILL.md`.

## Maintenance Rules

- Keep each skill focused.
- Put detailed checklists in `references/`, not directly inside `SKILL.md`.
- Do not store secrets, tokens, credentials, private customer data, or production API keys inside skills.
- Keep source notes separate from installable skill folders.
- If a tool requires the folder name to match the frontmatter `name`, install with the destination folder name shown in the table above.

## Official References

- OpenAI Codex Agent Skills: https://developers.openai.com/codex/skills
- Anthropic skills examples and Agent Skills overview: https://github.com/anthropics/skills
- Cursor Rules: https://cursor.com/docs/rules
- VS Code Agent Skills locations and format: https://code.visualstudio.com/docs/agent-customization/agent-skills
