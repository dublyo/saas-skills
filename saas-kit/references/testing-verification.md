# Testing And Verification Reference

Use this reference before implementation and during final verification.

## Contents

- Planning Gate Checklist
- Requirements Checklists
- Test Categories
- PocketBase Verification
- Supabase Verification
- Frontend Verification
- Implementation Verification
- Final Report

## Planning Gate Checklist

Before coding, ensure the spec has:

- primary user
- core workflow
- MVP boundary
- main entities
- CRUD behavior
- dashboard views
- ownership and roles
- workflow states
- provider assumptions
- edge cases
- security boundaries
- test plan

If any item materially affects implementation and is unknown, ask one more A/B/C/D question before coding.

## Requirements Checklists

Use checklists as "unit tests for English." They validate requirement quality, not implementation behavior.

Good checklist items ask:

- Are dashboard empty states specified for each main record list?
- Is record ownership defined for create, read, update, and archive actions?
- Are workflow state transitions named and bounded?
- Are permission-denied states distinct from empty states?
- Are provider rules or RLS expectations documented?

Avoid checklist items that ask the agent to click, render, test, or verify code behavior. Those belong in implementation tests, not requirement checklists.

## Test Categories

For SaaS apps, plan tests around workflows, not only components.

Recommended test coverage:

- model/schema validation
- CRUD happy path
- CRUD validation failures
- list/filter/search behavior
- permission/ownership checks
- workflow state transitions
- dashboard data loading
- empty/loading/error UI states
- provider rules/RLS
- manual smoke path

## PocketBase Verification

Verify:

- collections exist with expected fields
- required fields are enforced
- relations point to expected collections
- list/view/create/update/delete rules match ownership
- user cannot access another user's private records
- admin-only records/actions are not available to normal users
- file fields and file rules are correct if uploads exist

## Supabase Verification

Verify:

- migrations apply cleanly
- tables, constraints, and indexes exist
- RLS is enabled for protected tables
- select/insert/update/delete policies match roles and ownership
- anonymous access is impossible unless explicitly intended
- storage policies match file visibility
- queries used by dashboard screens are covered by indexes when scale requires it

## Frontend Verification

Verify:

- dashboard first screen loads real or seeded data
- primary CRUD flow works end-to-end
- forms show validation errors
- failed saves are visible
- empty states are useful
- permission-denied states do not look like missing data
- tables fit common and narrow viewports
- navigation reflects user role
- destructive actions require clear confirmation

## Implementation Verification

After coding, run the repo's existing checks first. Typical commands:

- package manager install/check command
- lint
- typecheck
- unit tests
- integration tests
- build
- app smoke run

Do not claim release-ready from compile-only proof. Report which checks were run and which were not.

## Final Report

Close with:

- spec approved: yes/no
- implementation completed: yes/no
- files changed
- checks run
- known gaps
- next concrete step
