# PocketBase And Supabase Reference

Use this reference when mapping a provider-neutral SaaS spec to PocketBase or Supabase.

## Contents

- Provider-Neutral First
- When PocketBase Fits
- When Supabase Fits
- Mapping Questions
- Auth And Roles
- Provider Output Format

## Provider-Neutral First

Do not let the backend provider define the product. First define:

- users
- roles
- domain entities
- ownership
- relationships
- workflow states
- validation rules
- list/filter/search needs
- realtime needs, if any
- file upload needs, if any

Then map those decisions to PocketBase or Supabase.

## When PocketBase Fits

Prefer PocketBase when the app is:

- small to medium SaaS or internal tool
- fast MVP
- CRUD-heavy
- simple role model
- single binary/self-hosted deployment
- admin-managed collections are useful
- realtime is useful but not complex

Plan PocketBase mapping as:

- collections for entities
- auth collection for users
- relation fields for ownership and joins
- collection API rules for access control
- hooks/custom code only when provider rules are not enough
- file fields only when uploads are part of the workflow

Always specify collection rules for:

- list
- view
- create
- update
- delete

## When Supabase Fits

Prefer Supabase when the app needs:

- hosted PostgreSQL
- SQL flexibility
- relational complexity
- Row Level Security
- reporting queries
- edge functions
- larger team or production scaling expectations
- direct SQL migrations

Plan Supabase mapping as:

- tables for entities
- foreign keys for relationships
- enum/check constraints or lookup tables for states
- RLS policies for ownership and role access
- RPC/functions only when needed
- storage buckets and policies for files
- migrations for all schema changes

Always specify RLS behavior for:

- select
- insert
- update
- delete

## Mapping Questions

Ask only after workflows are clear:

- Are records owned by users, teams, organizations, or globally shared?
- Are roles global or per workspace/project?
- Do users need realtime collaboration or just updated lists?
- Does the app need reports across many records?
- Are file uploads central or incidental?
- Does data need SQL-level reporting/export?
- Is self-hosting preferred?

## Auth And Roles

Keep auth simple unless the product needs more.

Common role levels:

- owner/admin
- manager
- member
- viewer

Common ownership models:

- user-owned
- workspace-owned
- organization-owned
- assigned-to user
- created-by user

Do not add multi-tenant complexity unless the workflow needs workspaces, teams, client accounts, or separate customer data spaces.

## Provider Output Format

When provider is selected, include:

```markdown
## Provider Mapping

### PocketBase
- Collections:
- Fields:
- Relations:
- API rules:
- Hooks:

### Supabase
- Tables:
- Constraints:
- RLS policies:
- Storage:
- Functions:
```

Include only the chosen provider in the final implementation plan unless the user wants a comparison.
