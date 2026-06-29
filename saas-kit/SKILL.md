---
name: saas-kit
description: Full Spec Kit-inspired workflow for AI-assisted SaaS planning, implementation, review, and evolution. Use when the user wants to plan, spec, build, audit, or evolve a SaaS product, MVP, dashboard, CRUD app, workflow system, admin tool, PocketBase/Supabase-backed app, or Spec Kit artifact set. The skill enforces one A/B/C/D clarification question at a time, produces a detailed SaaS spec focused on product workflows before stack decisions, maps the result to constitution/spec/plan/tasks/checklists/analyze/converge artifacts, supports Spec Kit when installed or a manual equivalent when absent, and blocks coding until the user approves the spec.
---

# SaaS Kit

## Operating Rule

Do not write or edit implementation code until the user has approved a spec.

Use this order:

1. Establish or note the SaaS constitution and project rules.
2. Clarify the SaaS product with one question at a time.
3. Produce a full human-readable SaaS spec.
4. Map the spec to Spec Kit/manual artifacts.
5. Create or update a plan, checklist, and tasks only after the spec is clear.
6. Ask for explicit approval before implementation.
7. Only after approval, inspect or modify implementation files.
8. Analyze before implementation and converge after implementation.

If the user asks for a review or audit, stay read-only unless they explicitly ask for fixes.

## Question Protocol

- Ask at most 10 questions.
- Ask exactly one question per message.
- Each question must have exactly four choices: A, B, C, D.
- Each question must build on the previous answer.
- Recommend one option when helpful, but still present all four.
- Stop early when the product direction is clear enough to write a useful spec.

Prioritize questions in this order:

1. Primary SaaS job and target user
2. Core workflow and success moment
3. Dashboard views and daily user actions
4. CRUD objects and ownership rules
5. Roles and permissions
6. Workflow states and transitions
7. Data/provider constraints
8. UI density and operational needs
9. Testing and verification expectations
10. Implementation scope and first release boundary

## Planning Bias

Focus on the app's real work, not marketing copy or premature architecture.

Default assumptions:

- Product: core SaaS workflows, dashboards, CRUD, and business functions first.
- Frontend: functional dashboard-first UI, Tailwind CSS by default.
- Backend/data: provider-neutral first; map to PocketBase or Supabase after workflows are clear.
- New app defaults: Next.js, Nuxt.js, or Astro.js for frontend; PocketBase or Supabase for backend/data.
- Existing app: inspect repo conventions after spec approval and follow existing patterns.

Avoid:

- Landing-page-first planning unless requested.
- Billing, subscriptions, enterprise compliance, or SSO by default unless central to the product.
- Decorative UI that hides workflow clarity.
- New abstractions or dependencies before a real need is visible.

## Spec Output

After the question loop, write a detailed spec with these sections:

- Goal
- Scope
- User flow
- Requirements
- Frontend
- Backend
- Database
- APIs
- UI/UX
- Edge cases
- Security
- Testing
- Spec Kit/manual artifact mapping
- Implementation steps

Then ask: "Approve this spec for implementation?" Do not code until the user approves.

## Spec Kit Use

If a repo has Spec Kit installed, use its artifact model and commands where appropriate:

- Constitution/project rules
- `spec.md`
- `plan.md`
- `tasks.md`
- requirement checklists
- `analyze` before implementation
- `converge` after implementation

If Spec Kit is absent, follow the same workflow manually using Markdown specs and task lists.

Treat these artifacts as the source of intent:

- `constitution.md`: non-negotiable project principles and gates
- `spec.md`: user intent, scenarios, requirements, entities, edge cases, success criteria
- `plan.md`: technical context, provider mapping, contracts, validation guide
- `tasks.md`: user-story-sized work, exact files, dependencies, checkpoints
- `checklists/*.md`: "unit tests for English" that validate requirement quality
- `analyze`: read-only consistency report before implementation
- `converge`: append-only remaining-work discovery after implementation

## Reference Routing

Load only the reference needed for the current task:

- `references/workflow-spec.md`: question loop, spec template, and Spec Kit/manual mapping.
- `references/spec-kit-lifecycle.md`: full constitution -> specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement -> converge flow.
- `references/constitution-governance.md`: SaaS constitution principles, approval gates, and governance rules.
- `references/artifact-lifecycle.md`: spec/plan/tasks relationships, persistence models, drift handling, and monorepo notes.
- `references/dashboard-crud.md`: dashboard-first UI, CRUD, workflow states, and SaaS screen planning.
- `references/pocketbase-supabase.md`: provider-neutral mapping to PocketBase or Supabase.
- `references/testing-verification.md`: quality gates, tests, smoke checks, and approval/implementation verification.
- `references/implementation-convergence.md`: task generation, scoped implementation, subagent use, and convergence rules.
- `references/customization-integration.md`: presets, extensions, bundles, Git hooks, and agent integration guidance.

For web implementation, follow MDN Web Docs best practices and the repo's existing patterns. When library/API syntax matters, fetch current official docs before coding.
