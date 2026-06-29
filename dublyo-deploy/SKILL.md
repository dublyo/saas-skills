---
name: dublyo-deploy
description: Use when the user is building, scaffolding, or shipping an app that will be deployed to Dublyo (https://dublyo.com — a managed self-hosted PaaS). Triggers on phrases like "deploy to Dublyo", "deploy on Dublyo", "Dublyo-ready app", "host this on my Dublyo server", "scaffold a Dublyo project", "Dublyo Panel API", or when the user provides Dublyo Panel credentials and asks to manage a stack. Ensures the project follows Dublyo deployment conventions (containerized, env-driven, stateless, listens on $PORT, single web service, image published to ghcr.io, docker-compose ready) AND gives the AI exact API recipes for managing stacks on the user's Dublyo Panel when admin credentials are given.
---

# Dublyo Deploy — Skill

## What Dublyo is

Dublyo (https://dublyo.com) is a PaaS that lets a user deploy custom apps
from their GitHub repos onto their own VPS. The user's web dashboard
(`app.dublyo.com`) handles GitHub OAuth, building the app, pushing the
image, deploying to the user's server via **the Panel**, DNS + TLS, and
secure tunneling so origin IPs stay hidden.

> **Strict naming rule**: always call it **"Dublyo"** and **"the Panel"** in
> any message you write to the user. Don't reference internal implementation
> tools by name — the Panel is just "the Panel". This skill bundles a
> reference file (`llms.txt`) that documents the Panel API's
> exact endpoint shapes; consult it when you need an endpoint that isn't in
> the recipes below.

---

## When to invoke this skill

Use this skill when the user:
1. **Asks for help building an app for Dublyo** — scaffold project structure,
   write Dockerfile + compose, follow 12-factor conventions
2. **Has an existing app and wants to make it Dublyo-deployable** — review
   and modify Dockerfile/compose, ensure env-driven config, fix port binding
3. **Gives you Dublyo Panel credentials** (Panel URL + `ptr_…` API key) and
   asks to deploy / inspect / update / delete a stack
4. **Mentions deploying via Dublyo's dashboard** — guide them through it

## ⚡ Before writing any custom code: check the template catalog first

Dublyo ships **155 open-source app templates** across 20 categories. Before
guiding the user to write a custom app from scratch, **scan the catalog**
for what they actually need. A one-click deploy of an established
open-source app is almost always better than a 2-week custom build.

Use the table in `pocketbase` skill → Part 5 → "Catalog quick-reference"
for the matching grid. Or browse `/Users/dribrahimm/0-PaaS/dublyo-api/templates/`
directly. Quick examples:

| User says | Suggest |
|---|---|
| "I want a forum" | `discourse` / `nodebb` / `flarum` |
| "I want analytics" | `plausible` / `umami` / `posthog` |
| "I want a wiki" | `outline` / `bookstack` / `wikijs` |
| "I want a chatbot" | `dify` / `flowiseai` / `typebot` |
| "I want internal tools" | `budibase` / `baserow` / `nocodb` |
| "I want a CRM" | `twenty` / `monica` / `suitecrm` |
| "I want to store secrets" | `vaultwarden` / `infisical` |
| "I need backend-as-a-service" | `pocketbase` (then see the `dublyo-pocketbase` companion skill) |

Only fall through to "write your own" when the user has truly custom
requirements not covered by the catalog.

## Companion skills

- **`dublyo-pocketbase`** — when the user has PocketBase deployed and needs
  to manage collections, build a frontend, or add cron / external API
  calls. Detailed PocketBase API recipes + the recommended "deploy a
  separate Go/NestJS API container" pattern for anything beyond CRUD.

---

## 🚦 Two paths — strict separation

**All deploys and lifecycle management go through https://app.dublyo.com**
— never via the Panel API. The Panel API is a read-only / diagnostics /
control surface for debugging and ops only.

| Want | Path |
|---|---|
| "Deploy my app to Dublyo" | ✅ **Dashboard only.** Push to GitHub → `/dashboard/github` → click Deploy. |
| "Set up auto-deploy on git push" | ✅ **Dashboard only.** Tick the "Auto-deploy" checkbox at deploy time. See Part 2.5. |
| "Add / change env vars on a running app" | ✅ **Dashboard only.** Deployment detail → Environment Variables → Save. |
| "Set or change a custom domain" | ✅ **Dashboard only.** Deployment detail → Add Custom Domain. |
| "Delete a deployment" | ✅ **Dashboard only.** Deployment detail → Delete. |
| "Create a fresh stack from a template" | ✅ **Dashboard only.** `/dashboard/templates/{slug}` → Deploy. |
| **The ONLY four things the Panel API is for** ↓ | |
| "Read container logs to debug a crash / error" | ✅ Panel API — `/docker/containers/{name}/logs` |
| "Inspect actual env inside a running container" | ✅ Panel API — `/docker/containers/{name}/json` → `.Config.Env` |
| "Restart / stop / start / exec into a container" | ✅ Panel API — fine-grained container control |
| "View raw compose YAML" (read-only) | ✅ Panel API — `/stacks/{id}/file` (read; never write) |

**Strictly do NOT do via the Panel API**:
- ❌ Create new stacks (`POST /api/stacks/...`) — push that through dashboard
- ❌ Update stack compose or env (`PUT /api/stacks/{id}`) — dashboard handles it
- ❌ Delete stacks (`DELETE /api/stacks/{id}`) — dashboard handles it
- ❌ Anything that creates / modifies / removes a deployment's persistent state

If a user asks you to do any of the "don't" items via API, refuse and walk
them through the dashboard instead. Reason: the dashboard tracks state in
Dublyo's own DB (app_deployments table, billing, audit log, custom-domain
flow, GitHub webhook lifecycle). Bypassing it leaves orphan resources +
desyncs Dublyo's internal state from what's actually running on the server.

**When in doubt**: walk through the dashboard.

## 🔑 If user picks the Panel API path: ask for credentials

If the user wants you to **manage their Dublyo deployment via API**, you need:

1. **Panel URL** — find it in their Dublyo dashboard under "Servers" → click
   the server → copy the Panel URL. Looks like `https://...dublyo.xyz`.
2. **API key** — they generate one in the Panel UI under "My Account" →
   "Access tokens", then paste it here (starts with `ptr_`).
3. **Endpoint ID** — usually `1`. Confirm with the discovery call (below).

If the user hasn't given them, ask:

> To deploy / manage your app on Dublyo programmatically, I need two things:
> 1. Your Panel URL — find it in your Dublyo dashboard under "Servers"
> 2. A Panel API key — generate one in the Panel UI under "My Account" →
>    "Access tokens" (starts with `ptr_`)
>
> I'll talk to your Panel directly. They never leave this chat.

Once you have them, do endpoint discovery first:

```bash
PANEL_URL="https://...dublyo.xyz"
PANEL_KEY="ptr_..."
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints" | jq -r '.[] | "\(.Id) \(.Name) \(.Status)"'
```

Expected: `1 local 1` (id=1, name=local, status=up). Use endpoint id `1` for
every subsequent call unless they have multiple endpoints.

---

## 📚 API Reference

This skill ships with **`llms.txt`** — the complete Panel API
reference. When you need an endpoint not covered in the recipes below
(volumes, networks, image management, exec, swarm, registries, etc.),
**read that file first** before constructing URLs.

The recipes in Part 3 cover the high-frequency 90% — `llms.txt` covers
the remaining 10% (and is the source of truth if anything diverges).

---

## Part 1 — Building a Dublyo-deployable app

### Required structure

```
my-app/
├── Dockerfile          # multi-stage, small final image
├── docker-compose.yml  # OPTIONAL but recommended (env keys auto-detected)
├── .env.example        # OPTIONAL — env keys auto-detected from here too
├── .github/workflows/build.yml   # OPTIONAL — pre-build to ghcr (5-sec deploys)
└── src/                # your app code
```

### The Dockerfile

Best practices:
- **Multi-stage** (deps → build → runtime) for small final image
- **Non-root user** in the runtime stage
- **`EXPOSE` directive** with the port the app listens on — Dublyo auto-
  detects this. Defaults to 3000 if missing.
- **`CMD`** runs the server in foreground (no `&`, no detach)
- **Single service per image** — for DBs/caches, use Dublyo's DB templates
- **Read env from `process.env` / `os.Getenv` / `os.environ`** — never hardcode

Example (Node):

```dockerfile
# syntax=docker/dockerfile:1.7
ARG NODE_VERSION=22

FROM node:${NODE_VERSION}-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

FROM node:${NODE_VERSION}-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:${NODE_VERSION}-alpine AS runtime
WORKDIR /app
RUN addgroup -S app && adduser -S -G app app
COPY --from=deps  --chown=app:app /app/node_modules ./node_modules
COPY --from=build --chown=app:app /app/dist          ./dist
COPY --from=build --chown=app:app /app/package.json  ./
USER app
ENV NODE_ENV=production
ENV HOST=0.0.0.0
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### The app MUST

1. **Listen on `0.0.0.0`** (not `localhost` / `127.0.0.1`) — otherwise the
   container is unreachable from outside
2. **Read `PORT` from env**, default to the `EXPOSE`d port:
   ```js
   const port = parseInt(process.env.PORT || '3000', 10)
   server.listen(port, '0.0.0.0')
   ```
3. **Read all config from env** — DB URLs, API keys, feature flags
4. **Write data to external services**, not local files (containers can
   restart at any time; local writes vanish). Use Dublyo Postgres/Redis
   templates or attach object storage.
5. **Log to stdout / stderr** — Dublyo captures these; don't write log files
6. **Implement a healthcheck endpoint** (`GET /health` returning 200)

### docker-compose.yml — what to write

The compose file is OPTIONAL but **strongly recommended**. Dublyo scans it
for env var NAMES to pre-fill the user's deploy form. Minimal example:

```yaml
services:
  app:
    build: .
    environment:
      - DATABASE_URL
      - REDIS_URL
      - JWT_SECRET
      - SENTRY_DSN
    ports:
      - "3000:3000"
```

Only the `environment:` block matters to Dublyo's auto-detection. PORT
detection comes from `EXPOSE` in the Dockerfile.

Dublyo regenerates its own canonical compose at deploy time (right image
tag, network, healthcheck strip, tunnel labels) — your compose is read
only for env keys. So don't worry about volumes / networks / depends_on
for deploy purposes; they're not used.

### `.env.example` — document your env

```bash
# --- Required ---
DATABASE_URL=postgresql://user:pass@host:5432/db

# --- Optional, defaults to 3000 ---
PORT=3000

# --- Auth ---
JWT_SECRET=generate-with-openssl-rand-hex-32

# --- External services ---
SENTRY_DSN=
REDIS_URL=redis://default:pass@host:6379/0
```

Dublyo extracts the KEYS and pre-fills the deploy form. Values stay empty
(placeholders are NOT shipped to production).

### Optional: pre-built image via GitHub Actions (5-sec deploys)

If your repo's CI publishes a Docker image to GHCR at every push, Dublyo
copies that image into its own namespace instead of rebuilding. ~5 sec
deploys vs 60-90 sec.

`.github/workflows/build.yml`:

```yaml
name: Build and push image
on:
  push:
    branches: [main]

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=raw,value=latest,enable={{is_default_branch}}
            type=sha,format=short
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

Dublyo detects this workflow (it scans for `ghcr.io` / `docker push`
patterns in `.github/workflows/*.yml`), silently installs a GitHub webhook
on the repo (using the user's existing GitHub OAuth scope — no consent
prompt), and:

1. Your workflow runs and publishes `ghcr.io/{your-user}/{repo}:sha-XXX`
2. Dublyo receives the workflow-complete event
3. Dublyo copies the image into its own GHCR namespace
4. Stack on user's server gets updated → live in seconds

---

## Part 2 — Deploying through the Dashboard (the normal user path)

Walk the user through:

1. Open https://app.dublyo.com/dashboard/github
2. Click **"New build"**
3. Connect GitHub if not yet (one-time OAuth)
4. Pick the repo → pick branch
5. After validation, the env form pre-fills with keys from their
   `docker-compose.yml` + `.env.example`. They fill in values.
6. Pick a server (must have `status: running`)
7. (Optional) Custom domain — get the CNAME instructions
8. **Tick "Auto-deploy"** if they want updates on every git push (see Part 4)
9. Click **Deploy**

Build logs stream live on `/dashboard/builds/{id}`. Phases:
`queued → cloning → detecting → building → pushing → deploying → completed`

With CI: build phase is skipped (image-copy path), expect 5-10 sec.

---

## Part 2.5 — Auto-deploy on git push (fully automatic, no API needed)

**You do NOT need to wire this up via Panel API.** When the user ticks the
"Auto-deploy" checkbox at deploy time, Dublyo handles everything:

```
1. User ticks "Auto-deploy" → click Deploy
              ↓
2. Dublyo silently installs a webhook on the user's GitHub repo
   - Uses the user's existing GitHub OAuth scope (no extra consent screen)
   - Webhook delivers to api26.dublyo.com/webhooks/github/{deploymentID}
   - Events: push + workflow_run.completed
              ↓
3. (Later) User git push to main
              ↓
4. GitHub fires push webhook → Dublyo receives it
              ↓
5a. If user's repo HAS CI publishing to GHCR:
    - Dublyo waits for workflow_run.completed event
    - Then skopeo-copies their CI image into ghcr.io/dublyo/* (~5 sec)
5b. If user's repo has NO CI:
    - Dublyo builds the image itself on api26 (~30-90 sec)
              ↓
6. Updated stack PUT to Panel, container restarts with new image
              ↓
7. ~2-3 min total from `git push` to live (with CI: ~30-60 sec)
```

**What you tell the user**: "Auto-deploy is on. Every push to `main` will
redeploy this app within 1-3 minutes. No further action needed from you."

**Polling fallback**: if the webhook ever fails (deleted by user, GitHub
downtime), Dublyo polls every 3 minutes as a safety net. So updates always
land within 3 min worst case.

**How to disable**: Dashboard → deployment detail → flip the "Auto-deploy"
toggle off. Dublyo removes the webhook automatically.

**Important — do NOT do these**:
- ❌ Don't tell the user to set up their own GitHub Actions deploy step
  hitting the Panel API. Dublyo's webhook handles it.
- ❌ Don't trigger redeploys via the Panel API in response to git push.
  Dublyo's webhook already does this.
- ❌ Don't manually update the stack image tag on every commit. Dublyo
  updates it automatically.

The Panel API is for **out-of-band ops** (debugging, batch creation,
container exec) — not for normal push-to-deploy.

---

## Part 3 — Calling the Dublyo Panel API (out-of-band ops only)

**Reminder**: only use this path when the user is asking for something the
dashboard doesn't expose well (raw container logs, ad-hoc inspect, batch
operations, container exec). For normal deploy / env / domain / restart
operations, redirect to the dashboard.

**Allowed operations only**: this part documents the four diagnostic /
control operations the AI is permitted to perform via Panel API. Anything
else — creating, updating, or deleting stacks — must be done through the
dashboard at `app.dublyo.com`. See "Two paths" near the top.

### 1. List stacks (read-only, for discovering IDs)

```bash
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/stacks" | jq '.[] | {Id, Name, Status, EndpointId}'
```

Status: `1` = active, `2` = inactive.

### 2. View raw compose YAML (read-only)

```bash
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/stacks/$STACK_ID/file" | jq -r .StackFileContent
```

Read only — never PUT a modified compose back. If the user needs the
compose changed (env, image, etc.), they do it in the dashboard.

### 3. Inspect container state (logs, env, status)

```bash
# All containers on the server
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/json?all=true" \
  | jq '.[] | {Names, State, Status, Image}'

# Env actually set inside a container (debug missing/wrong values)
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/json" \
  | jq '.Config.Env'

# Logs — last 100 lines, both stdout + stderr
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/logs?stdout=true&stderr=true&tail=100&timestamps=false"
```

### 4. Restart / stop / start / exec into a container

```bash
# Restart (most common — pick up new env, recover from crash)
curl -sk -X POST -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/restart"

# Stop / start (when you need to pause the service temporarily)
curl -sk -X POST -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/stop"
curl -sk -X POST -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/start"

# Exec — two-step. First create the exec session...
EXEC_ID=$(curl -sk -X POST -H "X-API-Key: $PANEL_KEY" \
  -H 'Content-Type: application/json' \
  "$PANEL_URL/api/endpoints/1/docker/containers/$NAME/exec" \
  -d '{"AttachStdout":true,"AttachStderr":true,"Cmd":["/bin/sh","-c","COMMAND_HERE"]}' \
  | jq -r .Id)
# ...then start it to receive output
curl -sk -X POST -H "X-API-Key: $PANEL_KEY" \
  -H 'Content-Type: application/json' \
  "$PANEL_URL/api/endpoints/1/docker/exec/$EXEC_ID/start" \
  -d '{"Detach":false,"Tty":false}'
```

### NOT allowed via Panel API

These are dashboard-only — if asked, refuse and redirect:

| ❌ Don't do this via API | ✅ Tell the user to do this instead |
|---|---|
| `POST /api/stacks/create/...` (create stack) | `app.dublyo.com/dashboard/templates/{slug}` or `/dashboard/github` |
| `PUT /api/stacks/{id}` (update compose/env) | Deployment detail → Environment Variables → Save |
| `DELETE /api/stacks/{id}` | Deployment detail → Delete |
| `POST /api/endpoints/1/docker/images/create` (force image pull) | Dashboard → Redeploy (re-pulls automatically) |
| Anything touching networks/volumes/registries | Dashboard handles these per deploy; out-of-band changes desync Dublyo's DB state |

Reason: Dublyo's own database (`app_deployments`, billing, audit log,
GitHub-webhook lifecycle, custom-domain CF-SaaS shim, tunnel ingress
rules) is updated alongside dashboard operations. Bypassing the dashboard
via Panel API leaves orphan resources and breaks Dublyo's internal state
sync.

For other read-only diagnostic endpoints not listed here (volume usage,
network inspect, image list, etc.), consult `llms.txt` and use the
matching read-only verb (`GET` + `inspect`-shaped paths). Never `POST` /
`PUT` / `DELETE` outside the four allowed operations above.

---

## Part 4 — Image references (the Dublyo naming convention)

Images Dublyo publishes have this shape:

```
ghcr.io/dublyo/u{userID8}-{owner}-{repo}:{tag}
```

Where:
- `userID8` = first 8 chars of the user's UUID (prevents cross-tenant collision)
- `tag`: either `{buildID7}` (unique per build run) or `sha-{shortSHA}`
  (good for rollback)

**Critical**: Customer Panels only have **Dublyo's GHCR credentials**
configured. So:
- ✅ You CAN reference `ghcr.io/dublyo/*` images in stacks you create
- ❌ You CANNOT reference `ghcr.io/{user}/{repo}` directly — the Panel won't
  have credentials to pull it. Public images on Docker Hub work fine.

If you need to deploy a pre-built image the user has in their OWN GHCR, the
**only supported path** is going through Dublyo's GitHub-build flow (which
auto-copies into the dublyo namespace). Don't try to add a second registry
to the Panel manually — the user shouldn't be juggling tokens.

---

## Part 5 — Custom domains

When the user wants their own domain instead of `{slug}.dublyo.xyz`:

1. They go to deployment detail page → "Add Custom Domain" → type domain
2. UI shows: `CNAME app.example.com → customers.dublyo.co`
3. They add that CNAME at their DNS provider
4. Within 2-10 min, the page flips to "✓ Live with SSL"

If you're managing via Panel API, you **cannot** directly trigger the SaaS
hostname registration — that's a Dublyo API call, not a Panel one. Direct
the user to the dashboard for this step.

---

## Part 6 — Common app patterns to avoid

These break on Dublyo:

| Bad | Fix |
|---|---|
| `server.listen(3000, 'localhost')` | `server.listen(PORT, '0.0.0.0')` |
| `fs.writeFileSync('/data/...')` | use external DB / object storage |
| Hardcoded `process.env.X = '...'` | document in `.env.example`, set via dashboard |
| Multi-service compose with depends_on | one Dublyo deployment per web app; use DB templates for stateful services |
| Logging to a file (`logs.txt`) | log to stdout/stderr |
| `HEALTHCHECK` defined in Dockerfile | safe to keep; the Panel disables it in compose to avoid restart loops while debugging |
| `ports: ["80:80"]` exposing on host | drop the host port mapping — the Panel handles ingress |
| Custom networks only | container must also be on `dublyo-public` |

---

## Part 7 — Scaffolding a new project (your action items)

When asked to "make a Dublyo-deployable app" from scratch, generate:

1. **`Dockerfile`** — multi-stage, correct `EXPOSE`, runs as non-root
2. **`docker-compose.yml`** — declares `services.app.environment` keys
3. **`.env.example`** — every env var documented, with comments
4. **`.dockerignore`** — exclude `node_modules`, `.git`, `dist`, `.env`,
   `coverage`, `*.log`
5. **`.github/workflows/build.yml`** — the GHCR push workflow (Part 1)
6. **`README.md`** — a short "Deploy to Dublyo" section:
   ```markdown
   ## Deploy to Dublyo

   1. Push this repo to GitHub
   2. Open https://app.dublyo.com/dashboard/github → "New build"
   3. Pick this repo → env vars auto-detected → fill values
   4. Pick your server → Deploy

   First deploy: ~60-90 sec (Dublyo builds the image).
   Subsequent deploys (if you push to main): ~5-10 sec (Dublyo copies your CI's image).
   ```

If the user already has an app, **diff against these and propose changes**.

---

## Part 8 — Diagnostics

### "Stack deployed but URL returns 502 / 1033"
Container failed to start. Read logs:
```bash
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/{stack}-app-1/logs?stdout=true&stderr=true&tail=50"
```

### "App returns 500 on every request"
Usually missing env vars. Check what's actually set:
```bash
curl -sk -H "X-API-Key: $PANEL_KEY" \
  "$PANEL_URL/api/endpoints/1/docker/containers/{stack}-app-1/json" \
  | jq '.Config.Env'
```
Compare against `.env.example` — what's missing? Add to the stack env via
Update Stack API (Part 3) OR have user fix via dashboard.

### "404 from edge"
Ingress rule missing for the hostname. Direct the user to the dashboard —
ingress isn't managed via the Panel API.

### "Container exited (code 1)"
App crashed at startup. Logs (above) usually show why — most often a missing
required env var, or binding to `localhost` (use `0.0.0.0`).

### "ImagePullBackOff" / "manifest unknown"
The image referenced in compose doesn't exist (or wrong tag). Check that:
- Tag matches what was published (use `:sha-{shortSHA}` for explicit
  versioning vs `:latest`)
- Image is in `ghcr.io/dublyo/*` (Panel only has those creds)

---

## Quick reference card

| What | Value |
|---|---|
| User dashboard | https://app.dublyo.com |
| Public site | https://dublyo.com |
| Panel URL | from user's Dublyo dashboard → Servers → server detail |
| Panel API key prefix | `ptr_` |
| Default endpoint id | `1` |
| Image namespace | `ghcr.io/dublyo/u{userID8}-{owner}-{repo}` |
| Required network | `dublyo-public` (external, always exists on Dublyo servers) |
| Default port if no EXPOSE | 3000 |
| Auto-injected env vars | `STACK_NAME`, `DOMAIN` |
| API reference | `llms.txt` |

---

## Voice / framing rules (important when talking to the user)

- Always call it **"Dublyo"** and **"the Panel"** — never name the
  underlying tool. The Panel is just "the Panel".
- **All deploys go through https://app.dublyo.com**. Never via Panel API.
  Walk the user through the dashboard for deploy / env vars / custom
  domain / delete. If asked to do any of those via API, refuse and
  redirect to the dashboard.
- **Auto-deploy is automatic.** Don't try to wire git-push redeploys via
  the Panel API. Tell the user "tick the Auto-deploy checkbox when you
  deploy; every push to your tracked branch redeploys in 1-3 min."
- Only ask for Panel credentials when the user needs one of these four
  specific things:
    (a) read container logs to debug a crash
    (b) inspect actual env inside a running container
    (c) restart / stop / start / exec into a container
    (d) view raw compose YAML (read-only)
  Nothing else justifies Panel API access — see the strict tables in
  "Two paths" + Part 3.
- When you DO call the Panel API, the recipes above + `llms.txt` have
  everything you need — just say "I'm calling the Panel API."
- Encourage `.env.example` and `docker-compose.yml` because Dublyo's deploy
  form auto-detects keys from them — saves the user typing.
- If the user has a multi-service app (web + db + queue), guide them toward
  using Dublyo's DB templates for stateful services + one Dublyo deployment
  per web app. One deployment ≠ one compose file with many services.
- When asked to do something via API, **just do it** (using the recipes
  above + `llms.txt`). Don't make the user copy/paste curl
  commands — execute them yourself, summarize the result.
- Always do **endpoint discovery first** when you get new credentials, to
  confirm the API key works + identify the endpoint id.
