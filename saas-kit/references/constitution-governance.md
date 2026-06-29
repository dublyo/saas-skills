# SaaS Constitution And Governance

Use this reference when defining or checking project rules before SaaS planning or implementation.

## Contents

- Purpose
- Default SaaS Constitution
- Constitution Check
- Amendment Rules
- Approval Gate

## Purpose

The constitution is the project-level contract. It prevents the agent from trading product clarity, workflow safety, or implementation quality for speed.

If a repo already has a constitution or AGENTS-style instructions, obey those first and adapt this reference to them.

## Default SaaS Constitution

Use or adapt these principles:

### I. Workflow First

Every feature must start from user jobs, dashboard flows, CRUD objects, workflow states, and measurable outcomes. Stack choices must not replace product decisions.

### II. Spec Approval Before Code

No implementation code may be written until the user approves the spec. Review and audit requests remain read-only unless fixes are explicitly requested.

### III. Provider-Neutral Data Modeling

PocketBase and Supabase are implementation mappings, not product definitions. Define users, roles, entities, ownership, relationships, validation, and states before provider-specific collections, tables, rules, or RLS policies.

### IV. Dashboard-First UX

The primary screen should be the usable SaaS workflow. Prioritize tables, filters, forms, detail views, queues, status, and repeated-use ergonomics. Avoid landing-page-first or decorative composition unless requested.

### V. Minimal Dependencies

Use the selected framework and provider directly unless a dependency solves a real problem. Do not add abstractions for imagined future needs.

### VI. Security Boundaries Are Requirements

Auth assumptions, role behavior, ownership rules, public/private data boundaries, and provider rules/RLS expectations must be specified before implementation.

### VII. Verification Is Part Of Delivery

Plans and tasks must include build, lint/typecheck, provider-rule checks, workflow tests, UI state checks, and manual smoke tests appropriate to the repo.

### VIII. Spec Drift Must Be Reconciled

If implementation discoveries change behavior, update the relevant spec, plan, and tasks before continuing. Do not leave code as the only source of truth.

## Constitution Check

Before planning, verify:

- Does the spec identify a primary user and success moment?
- Are core workflows clear enough to test manually?
- Are CRUD objects and ownership rules defined?
- Are roles and permission boundaries defined?
- Are PocketBase/Supabase choices deferred until workflow clarity?
- Is dashboard-first UI preserved?
- Are tests and smoke checks planned?

If a check fails and materially changes implementation, ask one more A/B/C/D question or mark the gap in the spec.

## Amendment Rules

Only change the constitution when the user or project needs a durable rule change.

Use version semantics:

- Major: removes or redefines a core rule
- Minor: adds a new principle or required gate
- Patch: clarifies wording without changing behavior

Record the reason for the change and update affected spec, plan, task, or checklist templates.

## Approval Gate

The final planning output must end with:

```text
Approve this spec for implementation?
```

Approval unlocks implementation. A scope change returns to the spec.
