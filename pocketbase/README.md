# dublyo-pocketbase skill

Helps an AI assist users who deployed PocketBase on Dublyo.

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | The skill itself (loaded by the AI). Covers: collection/field CRUD via API, record operations, files, realtime, and the recommended pattern for cron / external APIs (deploy a separate Go/NestJS API container, do NOT teach pb_hooks). Also includes the full Dublyo template catalog so the AI can suggest an existing template when one fits the user's need. |

## No bundled reference file

This skill points the AI at the **upstream PocketBase docs directly** —
WebFetch from the canonical URLs instead of shipping a cached copy:

| What | URL |
|---|---|
| Records API | https://pocketbase.io/docs/api-records/ |
| Collections API | https://pocketbase.io/docs/api-collections/ |
| Files API | https://pocketbase.io/docs/api-files/ |
| Realtime API | https://pocketbase.io/docs/api-realtime/ |
| Filter syntax + API rules | https://pocketbase.io/docs/collections/ |
| JS hooks typedoc | https://pocketbase.io/jsvm/index.html |

PocketBase ships fast — fetching live avoids staleness from a cached
`llms.txt` that drifts on every minor release.

## Companion skill

`dublyo-deploy` (sibling folder) handles the platform layer (deploying any
app, calling the Panel API). The two skills cross-reference each other —
when the user needs to deploy the recommended "custom Go/NestJS API"
container described in Part 4 of the PocketBase skill, they fall through
to dublyo-deploy.
