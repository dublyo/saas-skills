# Implementation And Convergence

Use this reference after the user approves a SaaS spec.

## Contents

- Task Generation
- Scoped Implementation
- Parallel Work
- Progress Tracking
- Convergence
- Completion Report

## Task Generation

Tasks must be specific enough for an agent to execute without guessing.

Group tasks as:

1. Setup
2. Foundational infrastructure
3. User Story 1 MVP
4. Later user stories
5. Polish and verification

Every task should include:

- checkbox
- stable task ID
- parallel marker only when safe
- user-story label when applicable
- exact file path or artifact path
- clear dependency when needed

Example:

```markdown
- [ ] T014 [US1] Implement lead status transition validation in src/features/leads/actions.ts
```

Avoid vague tasks:

- "Improve dashboard"
- "Add backend"
- "Make CRUD work"

## Scoped Implementation

For complex SaaS work, do not implement all tasks in one run.

Use scoped passes:

- only setup
- only T001-T010
- only US1
- only provider rules
- only dashboard shell
- only verification and fixes

After each pass:

- mark completed tasks
- run relevant checks
- report remaining tasks
- stop if a blocker changes the spec or plan

## Parallel Work

Parallel tasks are safe only when they touch different files or independent artifacts.

Good parallel candidates:

- independent model files
- independent UI components
- checklist generation
- docs updates
- tests for different endpoints

Poor parallel candidates:

- same form component
- same migration
- same provider rules file
- same routing file
- shared auth or permission logic

If subagents are available, use them only for isolated tasks with clear inputs and expected outputs.

## Progress Tracking

Use `tasks.md` as the work ledger.

- Mark completed work as `[X]`.
- Leave incomplete work as `[ ]`.
- Add notes for blocked tasks.
- Do not mark a task complete unless code and verification for that task are done.
- Do not silently skip required checks.

## Convergence

Convergence compares current code to intent. It is not a git diff and not a rewrite pass.

Inputs:

- `spec.md`
- `plan.md`
- `tasks.md`
- constitution
- current code

Classify gaps:

- missing: required work is absent
- partial: present but incomplete
- contradicts: code conflicts with intent
- unrequested: code adds behavior not requested

If gaps remain, append a new convergence phase at the bottom of `tasks.md`:

```markdown
## Phase N: Convergence

- [ ] T042 Add owner-based update rule for invoices per FR-006 (missing)
- [ ] T043 Remove or justify unrequested export action per US1/AC3 (unrequested)
```

Never rewrite, renumber, reorder, or delete prior tasks during convergence.

If no gaps remain, report that implementation satisfies the spec, plan, and tasks.

## Completion Report

Final reports should state:

- what was implemented
- files changed
- task IDs completed
- checks run
- checks not run
- convergence result
- remaining risks or gaps
