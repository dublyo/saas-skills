# Spec Kit SaaS Lifecycle

Use this reference when the user wants the full Spec Kit-style SaaS process.

## Contents

- Lifecycle
- Command Or Manual Equivalent
- Phase Responsibilities
- Recommended SaaS Production Flow
- Shortcuts

## Lifecycle

The full lifecycle is:

```text
constitution -> specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement -> converge
```

For Codex skills installations, Spec Kit commands may appear as `$speckit-constitution`, `$speckit-specify`, and similar skill names. For slash-command integrations, they may appear as `/speckit.constitution` or `/speckit-constitution`.

If Spec Kit is absent, use the same lifecycle manually with Markdown files.

## Command Or Manual Equivalent

| Step | Purpose | Manual equivalent |
| --- | --- | --- |
| Constitution | Set project principles and gates | `constitution.md` |
| Specify | Capture what users need and why | `spec.md` |
| Clarify | Resolve ambiguity before planning | `clarifications` section in `spec.md` |
| Plan | Translate spec into technical approach | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` |
| Checklist | Validate requirement quality | `checklists/*.md` |
| Tasks | Produce executable work items | `tasks.md` |
| Analyze | Find gaps across spec, plan, tasks | read-only analysis report |
| Implement | Execute approved tasks | code changes plus task checkoffs |
| Converge | Compare code to intent and append remaining work | convergence section in `tasks.md` |

## Phase Responsibilities

### Constitution

Define the rules that outrank convenience:

- planning before coding
- workflow-first product definition
- Tailwind dashboard-first UI
- PocketBase/Supabase provider-neutral planning
- security and ownership boundaries
- tests and smoke checks
- no unapproved scope expansion

### Specify

Stay technology-agnostic. Capture:

- target user
- primary job
- user stories
- acceptance scenarios
- entities
- edge cases
- measurable success criteria
- explicit out-of-scope items

### Clarify

Ask only high-impact questions. For this skill, use one A/B/C/D question at a time, not Spec Kit's multi-question default.

### Plan

Add technical choices:

- frontend framework
- PocketBase/Supabase or existing backend
- data model
- provider rules/RLS
- API/provider operation contracts
- validation guide
- performance and deployment constraints

### Checklist

Create requirement-quality checklists before tasks. They should catch vague, missing, conflicting, or untestable requirements while changes are still cheap.

### Tasks

Create tasks grouped by user story and phase:

- setup
- foundation
- US1 MVP
- later user stories
- polish and verification

Every implementation task needs an exact path or concrete artifact target.

### Analyze

Run before code. It is read-only. It should flag:

- duplicate requirements
- vague terms
- missing task coverage
- task/spec mismatch
- plan/spec contradiction
- constitution violations

### Implement

Run only after approval. Mark completed tasks in `tasks.md` and stop at checkpoints for complex work.

### Converge

Run after implementation. Compare the present code to spec, plan, and tasks. If gaps remain, append new tasks instead of rewriting history.

## Recommended SaaS Production Flow

Use the full flow for any SaaS app with real users, data ownership, provider rules, dashboard workflows, or unclear MVP scope.

Use this order:

1. Draft or confirm constitution.
2. Ask up to 10 A/B/C/D questions.
3. Write the SaaS spec.
4. Ask for approval.
5. After approval, generate plan and checklists.
6. Generate tasks.
7. Analyze artifacts.
8. Implement in scoped passes.
9. Verify.
10. Converge until no actionable findings remain.

## Shortcuts

For a tiny prototype, the minimum safe flow is:

```text
spec -> plan -> tasks -> approval -> implement -> smoke test
```

Do not skip the approval gate.
