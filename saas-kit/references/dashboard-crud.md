# Dashboard And CRUD Reference

Use this reference for SaaS screen planning, dashboard flows, CRUD objects, and workflow state design.

## Contents

- Product UI Bias
- Core SaaS Workflow Map
- CRUD Object Checklist
- Dashboard Planning
- Roles And Visibility
- Required UI States
- Implementation Guidance After Approval

## Product UI Bias

Build the usable app first. Avoid landing-page or hero-page composition unless the user asks for public marketing pages.

Dashboard-first SaaS UI should be:

- quiet
- dense
- scannable
- workflow-focused
- predictable under repeated use
- clear about status, ownership, and next action

Prefer:

- app shell with sidebar/topbar
- tables with filters and search
- create/edit forms
- detail pages or side panels
- status controls
- bulk actions when useful
- clear empty/loading/error states

Avoid:

- oversized hero sections
- decorative cards for every section
- vague AI-generated dashboard metrics
- hidden primary actions
- UI text explaining how to use the app unless the workflow truly needs guidance

## Core SaaS Workflow Map

For each main workflow, capture:

- Actor: who performs it
- Trigger: what starts it
- Object: what record is involved
- Steps: what happens in order
- State: how the record changes
- Decision points: approval, reject, assign, archive, reopen
- Output: what confirms success
- Notifications: only if needed
- Failure paths: invalid input, permission denied, conflicting state, failed save

## CRUD Object Checklist

For every object, define:

- list view columns
- default sort
- filters
- search fields
- create fields
- edit restrictions
- detail sections
- delete/archive behavior
- ownership rules
- role visibility
- validation rules
- empty state
- bulk actions, if any

Use archive instead of delete when records have history, reports, invoices, tasks, or user accountability.

## Dashboard Planning

A useful dashboard answers:

- What needs my attention?
- What changed recently?
- What is blocked?
- What is due soon?
- What can I create or continue?
- Which records are mine vs shared?

Use metrics only if they drive action. Avoid decorative numbers.

Dashboard sections often include:

- work queue
- recent activity
- status summary
- pinned records
- alerts/exceptions
- quick create
- saved filters

## Roles And Visibility

Define what each role can:

- see
- create
- edit
- delete/archive
- assign
- approve/reject
- export
- administer

For owner-based apps, explicitly define:

- user-owned records
- team-owned records
- public/shared records
- admin-visible records

## Required UI States

Plan states for:

- no records
- loading records
- failed load
- no search results
- invalid form input
- save in progress
- failed save
- permission denied
- stale/conflicting workflow state
- archived/deleted record
- narrow/mobile layout

## Implementation Guidance After Approval

For new apps, start with:

1. app shell
2. domain model
3. primary CRUD flow
4. dashboard list/detail flow
5. workflow state transitions
6. permission rules
7. smoke tests

For existing apps, inspect current routing, components, data fetching, forms, styling, and tests before editing.
