# Customization And Integration

Use this reference when adapting SaaS Kit to a repo, Spec Kit installation, or AI agent setup.

## Contents

- Spec Kit Detection
- Project-Local Overrides
- Presets
- Extensions
- Bundles
- Git Workflow
- Agent Integrations

## Spec Kit Detection

Before using Spec Kit commands, check for:

- `.specify/`
- `.agents/skills/speckit-*`
- agent command folders such as `.claude/commands`, `.gemini/commands`, `.windsurf/workflows`
- `specs/`
- `specify` CLI availability

If present, follow the installed invocation style. If absent, use manual Markdown artifacts.

## Project-Local Overrides

Use project-local overrides when only this SaaS app needs adjusted templates.

Typical override targets:

- spec template requiring SaaS workflow sections
- plan template requiring PocketBase/Supabase mapping
- tasks template requiring provider-rule verification
- checklist prompt requiring dashboard/CRUD requirement tests

Prefer overrides when:

- one project needs the rule
- the rule is not reusable yet
- speed matters

## Presets

Use a preset when you want to customize how Spec Kit works across multiple SaaS projects.

Good SaaS preset candidates:

- dashboard-first spec template
- PocketBase/Supabase plan sections
- mandatory ownership and provider-rule checklists
- task groups for CRUD, workflow states, and smoke tests
- no-code-before-approval language

Presets change existing workflows; they do not add brand-new commands.

## Extensions

Use an extension when adding new capabilities beyond the core flow.

Good SaaS extension candidates:

- provider rule audit command
- seed-data generation command
- smoke-test checklist command
- deployment readiness command
- bug triage workflow

Extensions add commands, hooks, or new phases.

## Bundles

Use a bundle when a complete role or team setup should be installable in one step.

Good SaaS bundle candidates:

- founder planning bundle
- developer implementation bundle
- QA/release verification bundle
- PocketBase MVP bundle
- Supabase production bundle

Bundles should be transparent: users should be able to inspect exactly which presets, extensions, workflows, and steps they install.

## Git Workflow

When a Git extension or manual git workflow is used:

- create a feature branch before specification
- keep generated spec/plan/tasks reviewable
- commit after major artifacts when useful
- never use destructive git commands unless explicitly requested
- preserve user-modified generated files

Feature branch naming should include a short product/workflow slug, such as:

```text
feat/001-lead-pipeline
feat/002-client-portal
fix/invoice-status-rules
```

## Agent Integrations

Spec Kit can install into different agents with different invocation styles.

For this skill, do not assume one style. Detect or infer from project files:

- Codex skills: `.agents/skills`, usually `$speckit-*`
- Claude skills/commands: `.claude/...`
- Gemini commands: `.gemini/commands`
- Windsurf workflows: `.windsurf/workflows`
- Generic integration: custom command directory

If invocation is uncertain, describe the artifact workflow manually instead of fabricating commands.

For team portability, keep artifacts agent-neutral whenever possible.
