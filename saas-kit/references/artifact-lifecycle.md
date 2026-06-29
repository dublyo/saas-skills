# Artifact Lifecycle

Use this reference when deciding how `spec.md`, `plan.md`, `tasks.md`, and code should evolve.

## Contents

- Artifact Roles
- Persistence Models
- Drift Rules
- Monorepo Notes
- File And Branch Hygiene

## Artifact Roles

`spec.md` is product intent:

- users
- stories
- acceptance scenarios
- requirements
- entities
- edge cases
- success criteria

`plan.md` is technical translation:

- stack
- provider mapping
- architecture
- constraints
- data model
- contracts
- quickstart validation

`tasks.md` is executable work:

- setup
- foundation
- user-story phases
- exact file paths
- tests and validation
- checkboxes that track progress

`checklists/*.md` validate requirement quality.

`quickstart.md` captures runnable manual validation scenarios.

## Persistence Models

Choose the model that fits the project. If the user did not choose, default to living spec for active SaaS MVPs.

### Flow-Back Spec

Any artifact or code can receive the first insight. Then reconcile all artifacts.

Best for:

- fast iteration
- small teams
- implementation discoveries

Risk:

- silent divergence if code or tasks change without updating `spec.md`

### Flow-Forward Spec

Completed feature directories are historical records. New requirements get a new feature directory.

Best for:

- audit trails
- explicit history
- features with clear boundaries

Risk:

- duplicated or fragmented context

### Living Spec

`spec.md` is the contract. Revise it first, then regenerate or update plan/tasks.

Best for:

- SaaS MVPs where product behavior is the source of truth
- long-lived app workflows
- teams that want future agents to trust the spec

Risk:

- losing implementation rationale if plan/task details are discarded carelessly

## Drift Rules

If spec and code disagree, do not assume code is right. Ask:

1. Did intended behavior change?
2. Did implementation reveal a constraint?
3. Is the spec missing an edge case?
4. Are tasks incomplete or too broad?

Then update the artifact closest to the truth and propagate:

- behavior change -> `spec.md`
- technical approach change -> `plan.md`
- remaining work -> `tasks.md`
- requirement quality issue -> checklist

## Monorepo Notes

Spec Kit projects are directory-scoped. The nearest `.specify/` owns the feature artifacts.

For SaaS monorepos:

- app/web may have its own `.specify/`
- api/backend may have its own `.specify/`
- shared packages may have separate specs
- branch namespace may still be shared at the git root

When operating manually, state which app/package the artifact applies to.

## File And Branch Hygiene

When Spec Kit or Git extension behavior is present:

- feature directories should be named with a number or timestamp plus short slug
- branch naming should reflect the feature
- generated artifacts should be reviewable
- never overwrite user-customized templates or prior convergence tasks without explicit approval

When no Git repo exists, keep artifacts in a clearly named `specs/<feature>/` or equivalent folder.
