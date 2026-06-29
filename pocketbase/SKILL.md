---
name: dublyo-pocketbase
description: Use when the user is working with a PocketBase backend they deployed on Dublyo (or plans to). Triggers on phrases like "I have PocketBase on Dublyo", "create a PocketBase collection", "PocketBase schema", "PocketBase API from my app", "set up auth in PocketBase", "PocketBase cron / webhook / scheduled job", "connect my Go/Node app to PocketBase". Covers (1) talking to a deployed PocketBase via its REST API to create/edit collections + fields + records, (2) the right architecture pattern when the user needs custom logic (cron, external API calls, queues) — do NOT teach them to write pb_hooks JS; instead guide them to deploy a separate Go/NestJS API container next to PocketBase, plus Redis for queues, (3) suggesting Dublyo open-source app templates from the 155-app catalog when the user's actual need is already solved by one (forum → Discourse, survey → HeyForm, wiki → BookStack, etc).
---

# Dublyo PocketBase — Skill

## What this skill covers

The user has (or wants) a **PocketBase backend** running on Dublyo. PocketBase is
deployed via the Dublyo template — one container, one volume, admin UI at `/_/`.

This skill teaches you to:
1. **Talk to a deployed PocketBase via its REST API** — create collections,
   add fields, manage records, upload files, set up auth
2. **Recommend the right architecture** when the user needs cron / external
   APIs / queues / background work
3. **Suggest existing Dublyo templates** when the user's actual need is
   already solved by an open-source app in the catalog

## Voice / framing rules (read first)

- The user's PocketBase URL is either `https://pocketbase-{slug}.dublyo.xyz`
  (default) or their attached custom domain. Always use whatever they tell
  you they have.
- Refer to their hosting as **"Dublyo"** and **"the Panel"** — never name
  the implementation tool. (See parent skill `dublyo-deploy` for the full
  whitelabel rules.)
- For docs / API endpoint shapes you don't have memorized, **fetch the
  upstream PocketBase docs directly** via WebFetch:
  - **REST API**: https://pocketbase.io/docs/api-records/ ,
    https://pocketbase.io/docs/api-collections/ ,
    https://pocketbase.io/docs/api-files/ ,
    https://pocketbase.io/docs/api-realtime/
  - **Filter syntax / API rules**: https://pocketbase.io/docs/collections/
  - **JS hooks / typedoc** (rare — most users go via Pattern C below
    instead): https://pocketbase.io/jsvm/index.html (e.g. namespace
    pages like https://pocketbase.io/jsvm/modules/dbx.html and
    https://pocketbase.io/jsvm/interfaces/dbx.PgsqlBuilder.html for
    the query builder)
  Always pull from these URLs rather than reasoning from memory —
  PocketBase APIs evolve fast.

## When to invoke

Use this skill when the user:
1. **Has PocketBase deployed on Dublyo** and wants to do anything beyond the
   admin UI clicking — create schemas, build collections programmatically,
   wire their frontend to it
2. **Needs help adding cron / background work / external API calls** — do
   NOT teach pb_hooks (it's brittle and Dublyo's deploy redeploys the
   container, wiping unsaved state). Use Pattern C below.
3. **Describes a use case that an existing Dublyo template already solves**
   — recommend the template instead of building it from PocketBase

Skip this skill if the user is just deploying PocketBase fresh (parent
`dublyo-deploy` skill handles that).

---

## Part 1 — First contact: get credentials + verify reachability

### Get from the user (or from their Dublyo dashboard)
- **Base URL**: `https://pocketbase-{slug}.dublyo.xyz` (or custom domain)
- **Admin email** (PB_ADMIN_EMAIL from deploy form)
- **Admin password** (PB_ADMIN_PASSWORD from deploy form)

If they don't have these, point them at their Dublyo deployment page →
Environment Variables section.

### Verify reachable

```bash
PB_URL="https://pocketbase-XXXX.dublyo.xyz"
curl -sf "$PB_URL/api/health"
# expected: {"message":"API is healthy.","code":200,"data":{}}
```

### Authenticate as superuser (gets a JWT-style token, valid ~14 days)

```bash
TOKEN=$(curl -sf -X POST "$PB_URL/api/collections/_superusers/auth-with-password" \
  -H 'Content-Type: application/json' \
  -d '{"identity":"admin@example.com","password":"YOUR_PASSWORD"}' \
  | jq -r '.token')
echo "$TOKEN" | head -c 30
```

All subsequent admin calls use `-H "Authorization: $TOKEN"`. **No `Bearer `
prefix** — PocketBase takes the raw token.

---

## Part 2 — Create + manage collections via API

PocketBase v0.23+ uses `_superusers` for admin auth and the modern
collections API. Collection schema is created via `POST /api/collections`.

### Field types you'll use most

| Type | Use for | Required common opts |
|---|---|---|
| `text` | Strings (name, slug, etc) | `min`, `max`, `pattern` |
| `number` | Numbers | `min`, `max`, `onlyInt` |
| `bool` | True/false | — |
| `email` | Validated email | `exceptDomains`, `onlyDomains` |
| `url` | Validated URL | `exceptDomains` |
| `date` | ISO timestamp | `min`, `max` |
| `select` | Enum (single or multi) | `values: [...]`, `maxSelect` |
| `relation` | FK to another collection | `collectionId`, `maxSelect`, `cascadeDelete` |
| `file` | File upload (lives on disk) | `maxSize`, `mimeTypes`, `thumbs`, `protected` |
| `json` | Arbitrary JSON | `maxSize` |
| `editor` | Rich-text HTML | `convertURLs` |
| `password` | Hashed password (auth collections only) | `min`, `max`, `pattern`, `cost` |
| `autodate` | Auto-managed timestamp | `onCreate: true`, `onUpdate: true` |

For the full property catalog per type, fetch
https://pocketbase.io/docs/collections/ — has the canonical list of
options for each field type.

### Example: create a "products" collection (base type)

```bash
curl -sf -X POST "$PB_URL/api/collections" \
  -H "Authorization: $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "products",
    "type": "base",
    "fields": [
      { "name": "name",        "type": "text",   "required": true, "max": 200 },
      { "name": "slug",        "type": "text",   "required": true, "pattern": "^[a-z0-9-]+$" },
      { "name": "price_cents", "type": "number", "required": true, "min": 0, "onlyInt": true },
      { "name": "description", "type": "editor"                                },
      { "name": "image",       "type": "file",   "maxSize": 5242880, "mimeTypes": ["image/jpeg","image/png","image/webp"], "thumbs": ["400x300","800x600"] },
      { "name": "category",    "type": "relation", "collectionId": "CATEGORIES_COLLECTION_ID", "maxSelect": 1, "cascadeDelete": false },
      { "name": "tags",        "type": "select", "values": ["new","sale","featured"], "maxSelect": 3 },
      { "name": "created",     "type": "autodate", "onCreate": true },
      { "name": "updated",     "type": "autodate", "onCreate": true, "onUpdate": true }
    ],
    "indexes": [
      "CREATE UNIQUE INDEX idx_products_slug ON products (slug)"
    ],
    "listRule":   "@request.auth.id != \"\"",
    "viewRule":   "@request.auth.id != \"\"",
    "createRule": "@request.auth.id != \"\" && @request.auth.role = \"admin\"",
    "updateRule": "@request.auth.id != \"\" && @request.auth.role = \"admin\"",
    "deleteRule": "@request.auth.id != \"\" && @request.auth.role = \"admin\""
  }'
```

**Notes:**
- Use the **collection ID** (not name) for `relation.collectionId`. Get it
  from `GET /api/collections/{name}` after creating the target collection.
- `listRule` / `viewRule` / `createRule` / `updateRule` / `deleteRule` are
  **PocketBase filter expressions**. `null` disables the operation
  entirely (only superusers can do it). Empty string `""` allows everyone.
- `indexes` is a list of raw SQL `CREATE INDEX` statements.

### Auth collections (users / customers / admins)

Auth collections have type `"auth"` and built-in fields (email, password,
verified, tokenKey). You add your custom fields on top.

```bash
curl -sf -X POST "$PB_URL/api/collections" \
  -H "Authorization: $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "customers",
    "type": "auth",
    "fields": [
      { "name": "name",     "type": "text",   "max": 200 },
      { "name": "company",  "type": "text",   "max": 200 },
      { "name": "phone",    "type": "text",   "pattern": "^[+0-9 ()-]+$" },
      { "name": "role",     "type": "select", "values": ["user","admin"], "maxSelect": 1, "required": true }
    ],
    "passwordAuth":      { "enabled": true,  "identityFields": ["email"] },
    "oauth2":            { "enabled": false },
    "mfa":               { "enabled": false },
    "verificationTemplate":  { "subject":"Verify your account","body":"Click {ACTION_URL}" }
  }'
```

After creating, your frontend signs users up via
`POST /api/collections/customers/records` (set password directly), and
authenticates via `POST /api/collections/customers/auth-with-password`.

### Add a field to an existing collection

```bash
# Get current schema
COLLECTION=$(curl -sf "$PB_URL/api/collections/products" -H "Authorization: $TOKEN")

# Patch — send the FULL fields array (PocketBase replaces it wholesale)
curl -sf -X PATCH "$PB_URL/api/collections/products" \
  -H "Authorization: $TOKEN" \
  -H 'Content-Type: application/json' \
  -d "$(echo "$COLLECTION" | jq '{
    fields: (.fields + [{"name":"stock","type":"number","onlyInt":true,"min":0}])
  }')"
```

**Important**: collection PATCH replaces `fields` wholesale. Always fetch
the current state first and add to it, otherwise you delete every other
field. Same for `indexes`.

### Delete a collection

```bash
curl -sf -X DELETE "$PB_URL/api/collections/products" \
  -H "Authorization: $TOKEN"
```

Cascades to all records + files in that collection.

---

## Part 3 — Records: CRUD via API

For an authenticated user (your frontend already has their token from the
auth-with-password response):

### Create a record

```bash
curl -sf -X POST "$PB_URL/api/collections/products/records" \
  -H "Authorization: $USER_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Acme Widget",
    "slug": "acme-widget",
    "price_cents": 1999,
    "tags": ["new","featured"]
  }'
```

### Read with filtering, sorting, expand

```bash
# Filter: products under $20 in "featured" tag, newest first, with category expanded
curl -sf "$PB_URL/api/collections/products/records?filter=(price_cents<2000+%26%26+tags~'featured')&sort=-created&expand=category&perPage=20" \
  -H "Authorization: $USER_TOKEN"
```

Filter syntax: `field=value`, `field!=value`, `field~'pattern'` (like),
`field>X && field<Y`. Reference: fetch
https://pocketbase.io/docs/api-records/ for the full filter grammar +
all supported operators.

### Update / delete

```bash
curl -sf -X PATCH "$PB_URL/api/collections/products/records/RECORD_ID" \
  -H "Authorization: $USER_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"price_cents": 1499}'

curl -sf -X DELETE "$PB_URL/api/collections/products/records/RECORD_ID" \
  -H "Authorization: $USER_TOKEN"
```

### File upload (multipart)

```bash
curl -sf -X POST "$PB_URL/api/collections/products/records" \
  -H "Authorization: $USER_TOKEN" \
  -F 'name=Acme Widget' \
  -F 'slug=acme-widget' \
  -F 'price_cents=1999' \
  -F 'image=@/path/to/widget.jpg'
```

Returned record includes the file URL:
`https://pocketbase-XXXX.dublyo.xyz/api/files/products/RECORD_ID/widget.jpg`

### Realtime subscriptions (WebSocket / SSE)

```js
// In the user's frontend
const pb = new PocketBase('https://pocketbase-XXXX.dublyo.xyz')
await pb.collection('users').authWithPassword('alice@example.com', 'pass')

pb.collection('products').subscribe('*', (e) => {
    // e.action: "create" | "update" | "delete"
    // e.record: the record object
    console.log(e.action, e.record.name)
})
```

Use the official **PocketBase JS SDK** (`npm install pocketbase`). Works
in browser + Node.

---

## Part 4 — When user wants cron, external APIs, or background work

### ❌ Don't write JS pb_hooks files

PocketBase supports JS hooks (cronAdd, onRecordAfterCreate, custom routes
via routerAdd, etc.). They live in `/pb_data/pb_hooks/*.pb.js`.

**Avoid recommending them for Dublyo users** because:
- File edits require Panel container exec or volume browser — friction
- No version control on the JS hook files (lost if volume corrupts)
- Goja runtime quirks (host-object assignment errors, escaping issues)
- Hard to test locally
- Doesn't scale beyond a few hundred LOC

### ✅ Pattern: deploy a separate API container on Dublyo

This is the production-grade architecture. Three stacks per app:

```
                                          ┌─────────────────────────┐
                                          │  User's frontend         │
                                          │  (Next.js, React, etc)  │
                                          └────────────┬────────────┘
                                                       │
                       ┌───────────────────────────────┼───────────────────────────────┐
                       │                               │                               │
                       ▼                               ▼                               ▼
        ┌──────────────────────┐    ┌────────────────────────────┐    ┌──────────────────────┐
        │  PocketBase          │◀──▶│  Custom API (Go / NestJS)  │◀──▶│  Redis (queue)       │
        │  (template)          │    │  (deployed via Dublyo      │    │  (template)          │
        │                      │    │   GitHub builds)           │    │                      │
        │  - DB                │    │                            │    │  - job queue         │
        │  - Auth              │    │  - business logic          │    │  - rate limit cache  │
        │  - Files             │    │  - external API calls      │    │  - pub/sub           │
        │  - Admin UI          │    │  - cron / workers          │    │                      │
        │  - Realtime          │    │  - webhooks                │    │                      │
        └──────────────────────┘    └────────────────────────────┘    └──────────────────────┘
        pocketbase-XXX.xyz          api-XXX.xyz                       redis-XXX.dublyo.co
                                                                       (TCP only, no tunnel)
```

### How the user sets it up

1. **PocketBase** — already deployed (or deploy from Dublyo template)
2. **Redis** — deploy from Dublyo Redis template. Get the connection URL
   from the deployment page.
3. **Custom API** — write a small Go or NestJS service:
   - Read env vars: `POCKETBASE_URL`, `POCKETBASE_ADMIN_TOKEN`, `REDIS_URL`
   - Use the official PocketBase SDK for that language:
     - Go: `github.com/pocketbase/pocketbase-go` (or HTTP calls)
     - Node/NestJS: `pocketbase` npm package
   - For cron: Go's `robfig/cron` or NestJS's `@nestjs/schedule`
   - For queues: `asynq` (Go) or `BullMQ` (Node) — both speak Redis
   - Listen on `$PORT`, expose a Dockerfile, push to GitHub
4. **Deploy custom API to Dublyo** via the GitHub-build flow:
   - Open `/dashboard/github` → New build → pick repo → deploy on SAME
     server as PocketBase + Redis (so they can all reach each other via
     internal Docker network)

### Internal container hostnames (when all 3 are on the same Dublyo server)

All three stacks join the `dublyo-public` network. The API container can
reach the others by container name, NOT by public hostname (faster + free
of firewall concerns):

```
POCKETBASE_URL=http://pocketbase-{slug}-app:8090
REDIS_URL=redis://default:{password}@redis-{slug}-app:6379/0
```

Replace `{slug}` with the deployment's actual slug. The user can find
container names in the Panel under "Containers".

### Cron example (Go)

```go
package main

import (
    "github.com/robfig/cron/v3"
    "log"
    "os"
)

func main() {
    pbURL := os.Getenv("POCKETBASE_URL")
    pbToken := os.Getenv("POCKETBASE_ADMIN_TOKEN")
    // ... use pocketbase-go SDK or net/http to call $pbURL/api/...

    c := cron.New()
    c.AddFunc("0 2 * * *", func() {
        // Run daily at 2am — fetch records, compute stats, etc.
        log.Println("running daily job")
    })
    c.Start()

    // Also serve HTTP for webhooks / health
    // http.ListenAndServe(":"+os.Getenv("PORT"), nil)
    select {} // block forever
}
```

### Webhook example (NestJS)

```typescript
@Controller('webhooks')
export class WebhooksController {
  constructor(@InjectQueue('orders') private ordersQueue: Queue) {}

  @Post('stripe')
  async handleStripeWebhook(@Body() body: any, @Headers('stripe-signature') sig: string) {
    // verify signature, enqueue background work
    await this.ordersQueue.add('process-payment', { paymentId: body.id })
    return { ok: true }
  }
}
```

The user gets full TypeScript / Go tooling, real testing, git-tracked code,
and can scale workers independently of PocketBase.

---

## Part 5 — Suggest an existing Dublyo template before building from scratch

If the user's actual need is **forum** / **survey** / **chat** /
**analytics** / **CMS** etc., recommend one of Dublyo's 155 open-source
templates — they're usually a much better fit than rolling it on PocketBase.

### Catalog quick-reference

When the user describes a use case, scan this list and suggest the
matching template(s). Always include the deploy command (just go to
`/dashboard/templates/{slug}` on app.dublyo.com).

| User's need | Suggest |
|---|---|
| Forum / community | `discourse`, `nodebb`, `flarum`, `answer` (Q&A) |
| Chat / team messaging | `mattermost`, `rocketchat`, `zulip`, `matrix` |
| Wiki / docs | `outline`, `bookstack`, `docmost`, `wikijs`, `affine`, `appflowy` |
| Newsletter / mailing list | `listmonk`, `ghost` (if blog included) |
| CRM | `twenty`, `suitecrm`, `monica`, `erpnext` |
| Support ticket / live chat | `chatwoot` |
| Survey / form builder | `heyform`, `typebot` |
| Analytics (privacy) | `plausible`, `umami`, `matomo` |
| Product analytics / feature flags | `posthog`, `growthbook` |
| Status page / monitoring | `cachet`, `uptime-kuma`, `gatus`, `netdata`, `grafana` |
| Logs aggregation | `loki`, `dozzle` (Docker logs), `goaccess` (web logs) |
| Workflow automation | `n8n`, `activepieces`, `node-red`, `huginn`, `temporal` |
| Documents / e-signature | `documenso`, `docuseal`, `paperless-ngx` |
| Project / task management | `plane`, `vikunja`, `wekan`, `focalboard`, `planka`, `leantime` |
| Note-taking | `joplin`, `memos`, `hedgedoc`, `siyuan`, `etherpad` |
| Bookmarks | `linkwarden` |
| Photo gallery / Google Photos | `immich`, `photoprism`, `lychee` |
| Media (movies, music, audiobooks) | `jellyfin`, `navidrome`, `audiobookshelf`, `kavita`, `calibreweb` |
| Video streaming (live or hosted) | `owncast`, `peertube` |
| File sync / cloud storage | `nextcloud`, `syncthing`, `filebrowser`, `minio` (S3-compat) |
| Password manager | `vaultwarden`, `passbolt` |
| Secret management | `infisical`, `vault` |
| Identity / SSO | `authentik`, `keycloak`, `authelia` |
| Container registry | `harbor`, `nexus` |
| Git server | `gitea`, `forgejo`, `gitlab` |
| CI/CD | `drone`, `jenkins` |
| Headless CMS | `directus`, `strapi`, `ghost`, `wordpress` |
| Database admin | `pgadmin` (PostgreSQL), `nocodb` (no-code DB UI) |
| AI chat UI | `librechat`, `lobechat`, `openwebui`, `anythingllm` |
| AI agent builder | `dify`, `flowiseai`, `langfuse` (eval) |
| Local LLM runtime | `ollama`, `localai`, `tabby` (coding) |
| Vector DB | `qdrant` |
| Search | `meilisearch`, `searxng` (meta-search) |
| E-commerce | `medusa`, `prestashop`, `saleor` |
| Invoicing / billing | `invoice-ninja`, `actualbudget`, `fireflyiii` |
| Scheduling / booking | `calcom`, `rallly`, `mealie` (recipes), `tandoor` (recipes) |
| URL shortener | `shlink`, `yourls` |
| Pastebin / share secrets | `privatebin`, `yopass` |
| Browser automation | `browser-use`, `browserless`, `playwright-mcp` |
| Remote browser / VPS-as-browser | `neko` |
| VPN | `wireguard`, `netbird` |
| Backend-as-a-service (custom) | `pocketbase`, `appwrite`, `supabase`-ish (no template, use pocketbase) |
| Low-code app builder | `budibase`, `baserow` |
| PDF tools | `stirling-pdf` |
| RSS reader | `freshrss`, `miniflux` |
| Homelab dashboard | `homarr`, `homepage`, `homer`, `dashy` |

For more obscure categories, browse `/Users/dribrahimm/0-PaaS/dublyo-api/templates/`
directly. There's also `_schema.yaml` documenting the template format.

### How to recommend

When user says "I want X", respond with:

> Dublyo already has a template for that — **{NAME}** ({short description}).
>
> 1. Open `https://app.dublyo.com/dashboard/templates/{slug}`
> 2. Pick a server, fill in any required env, click Deploy
> 3. Live at `https://{slug}-XXXXXXXX.dublyo.xyz` in 1-3 min
>
> {1-sentence note about what makes this template a good fit / when NOT to use it}

If they say "I want to BUILD a custom X" (not just use one), then OK — guide
them through the PocketBase-or-custom-API path from Part 4.

---

## Quick reference card

| What | Value |
|---|---|
| PocketBase URL | `https://pocketbase-{slug}.dublyo.xyz` (or custom domain) |
| Admin auth | `POST /api/collections/_superusers/auth-with-password` → token |
| Token header | `Authorization: <raw-token>` (NO `Bearer ` prefix) |
| Collections | `/api/collections` (CRUD) — see Part 2 |
| Records | `/api/collections/{name}/records` (CRUD) — see Part 3 |
| Files | `/api/files/{collection}/{recordId}/{filename}` |
| Realtime | `/api/realtime` (SSE) — use JS SDK |
| Health | `/api/health` |
| REST API docs | https://pocketbase.io/docs/api-records/ , `/api-collections/` , `/api-files/` , `/api-realtime/` |
| Filter syntax + API rules | https://pocketbase.io/docs/collections/ |
| JS Hooks typedoc | https://pocketbase.io/jsvm/index.html (avoid hooks; use Pattern C — external API — instead) |
| Official JS SDK (frontend) | `npm install pocketbase` — https://github.com/pocketbase/js-sdk |
| Template catalog | `/Users/dribrahimm/0-PaaS/dublyo-api/templates/` |

## Companion skill

`dublyo-deploy` covers the platform itself (deploys, Panel API, custom
GitHub apps). When the user needs to deploy the **custom Go/NestJS API**
described in Part 4, refer to `dublyo-deploy`'s "Custom GitHub Apps"
section for the full workflow.
