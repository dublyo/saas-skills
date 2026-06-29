# Workflow Spec Reference

Use this reference when turning a SaaS idea into a spec.

## Contents

- Question Loop
- Full Spec Skeleton
- Spec Kit Mapping
- Approval Gate

## Question Loop

Ask one question at a time. Each question has exactly four options: A, B, C, D.

Do not ask about stack first unless the user explicitly frames the work as a migration or integration.

Question sequence:

1. Who is the primary user?
2. What job do they need to complete?
3. What is the core success moment?
4. What objects do they create, view, edit, delete, approve, assign, or track?
5. What dashboard views do they need every day?
6. What workflow states matter?
7. What roles or ownership boundaries matter?
8. What provider constraints exist: PocketBase, Supabase, existing backend, or undecided?
9. What is in/out of MVP?
10. What proof must exist before implementation is considered done?

Stop early when the spec can be written without guessing.

## Full Spec Skeleton

Use this shape after the question loop:

```markdown
# SaaS Spec: [Name]

## Goal
[What the product/feature helps users accomplish.]

## Scope
### In Scope
- ...

### Out of Scope
- ...

## User Flow
1. ...

## Requirements
### Functional
- FR-001: ...

### Non-Functional
- NFR-001: ...

## Frontend
- App shell:
- Dashboard views:
- CRUD flows:
- Workflow screens:
- States:

## Backend
- Auth assumption:
- Roles:
- Domain services/workflows:
- Background jobs:

## Database
- Entity:
  - Fields:
  - Relationships:
  - Ownership:
  - State:

## APIs
- Operation:
  - Inputs:
  - Output:
  - Errors:
  - Permission:

## UI/UX
- Layout:
- Navigation:
- Tables/forms:
- Empty/loading/error states:

## Edge Cases
- ...

## Security
- Auth:
- Record ownership:
- Provider rules/RLS:
- Secrets:

## Testing
- Unit:
- Integration:
- Provider rules:
- UI:
- Manual smoke:

## Spec Kit / Manual Artifact Mapping
- Constitution notes:
- spec.md:
- plan.md:
- tasks.md:
- checklists:

## Implementation Steps
1. ...
```

## Spec Kit Mapping

When Spec Kit is installed:

- Put user intent, stories, requirements, entities, edge cases, and success criteria in `spec.md`.
- Put stack, provider choice, data mapping, contracts, and validation plan in `plan.md`.
- Put user-story-sized implementation tasks in `tasks.md`.
- Use a checklist for requirement clarity before implementation.
- Run analysis before code changes.
- Run convergence after implementation.

When Spec Kit is not installed:

- Keep the same artifacts as normal Markdown files.
- Preserve IDs for requirements, entities, tasks, and tests.
- Keep the spec as the source of truth and update it before derived plans/tasks.
- Use the same gate names in headings so future migration to Spec Kit is straightforward.

## Approval Gate

End the spec with a direct approval question:

```text
Approve this spec for implementation?
```

If the user changes scope, revise the spec first. If they approve, implementation may begin.
