---
name: dublyo-tag-manager-server
description: Use when the user is setting up analytics / pixel tracking / conversion APIs on a SaaS deployed via Dublyo. Triggers on phrases like "set up GTM", "server-side tagging", "GA4 measurement", "Facebook CAPI / Meta Conversions API", "track conversions", "add Facebook Pixel / TikTok / Snapchat pixel", "dataLayer setup", "ad blocker bypass", "first-party tracking". Covers (1) deploying Dublyo's Server-side Google Tag Manager (sGTM) via the dedicated dashboard at app.dublyo.com/dashboard/gtm, (2) deciding whether the user needs GTM Web + Server or Server-only, (3) the canonical SaaS dataLayer schema + how to wire it in frontend (React/Next.js/Vue + mobile), (4) routing server-side events from the user's custom API to sGTM, (5) connecting GA4, FB Pixel + CAPI, TikTok, Snapchat, LinkedIn, (6) verifying events landed using Dublyo's PostHog template + vendor pixel helpers.
---

# Dublyo Tag Manager Server — Skill

## What this skill covers

Most SaaS founders treat tracking as an afterthought and end up with:
- Ad blockers killing 30-40% of their analytics
- iOS 14.5+ ATT blocking pixel attribution
- Inflated CPAs because ad networks can't see conversions
- No way to fix tags without redeploying their app

Dublyo's **sGTM (Server-side Google Tag Manager)** fixes all of that with
one click. This skill teaches the AI to (1) get it deployed, (2) wire the
user's frontend dataLayer correctly, (3) plug in destinations.

## Voice / framing rules

- Always call it **"Dublyo's GTM Server"** or **"sGTM"** — the user manages
  it at `app.dublyo.com/dashboard/gtm` (a dedicated page, not the generic
  template catalog).
- Don't confuse **GTM Server** with **GTM Web**:
  - **GTM Web** = the JavaScript snippet that loads in users' browsers
    (the `<script src="https://www.googletagmanager.com/gtm.js?id=GTM-XXX">`)
  - **GTM Server** = a server you control that receives events and
    forwards them to GA4 / Meta / etc. via their **Conversions API**
    (CAPI). First-party, ad-blocker-resistant, faster.
- For docs the AI doesn't have memorized:
  - https://developers.google.com/tag-platform/tag-manager/server-side
  - https://developers.google.com/tag-platform/tag-manager/datalayer
  - https://developers.facebook.com/docs/marketing-api/conversions-api
  - https://business-api.tiktok.com/portal/docs (Events API)

## When to invoke this skill

1. **User is setting up tracking on a Dublyo-hosted SaaS** — fresh app or
   adding analytics to existing one
2. **User asks about FB Pixel / GA4 / TikTok / Snapchat / LinkedIn** in
   the context of their Dublyo deployment
3. **User mentions ad blockers killing their analytics** or "iOS made my
   pixels useless"
4. **User wants to track conversions for paid ads** (Google Ads, Meta Ads,
   TikTok Ads, etc.) and needs conversion-API integration

Skip if user is just asking about a different analytics tool (PostHog,
Plausible) — those are simpler and don't need GTM Server.

---

## Part 1 — Get the GTM Container Config from Google

**Prerequisite**: The user needs a Google Tag Manager account with a
**Server** container (not Web). Walk them through:

1. Go to https://tagmanager.google.com
2. Create a new container — type **Server**
3. After creation, click **Manual provisioning** (NOT "automatically
   provision")
4. Copy the **Container Config** string — it's a base64 blob that looks
   like `aWQ9R1RNLU5DV0xLVDV...&env=...`

That config string is what they paste into Dublyo's GTM deploy form. It
contains the container ID + auth token sGTM needs to fetch the latest
tags from Google's CDN.

---

## Part 2 — Deploy GTM Server via Dublyo

This is **not** in the generic template catalog — it's its own dedicated
flow at `app.dublyo.com/dashboard/gtm`.

### Walk-through

1. Open https://app.dublyo.com/dashboard/gtm
2. Click **New GTM Container**
3. **Server** — pick a Dublyo server (any running tunnel-mode server is fine)
4. **Domain** — typically `gtm.<their-saas-domain.com>` (first-party
   tracking — the whole point of sGTM is requests go through THEIR
   domain, not google's). They'll add a CNAME at their DNS provider
   pointing this at the Dublyo-issued URL.
5. **Name** — friendly label, e.g. "Production GTM"
6. **Container Config** — paste the base64 string from Part 1
7. **(Optional) Custom Loader Path** — defaults to `gtm.js`; only change
   if they want to obscure the path against basic ad-block detection
   (e.g. `loader/script.js`)
8. **(Optional) Powerups** — Dublyo adds a proxy sidecar
   (`ghcr.io/dublyo/gtm-powerup`) when any of these is enabled:
   - **CookieKeeper** — extends first-party cookie lifetime past
     browser's 7-day cap (ITP workaround)
   - **UserID** — hashes user IDs server-side so they're never sent
     plaintext to Google
   - **BotDetection** — filters out bot traffic before it pollutes
     analytics
   - **IPBlocklist** — drop events from specific IPs (internal traffic,
     known scrapers)
9. Click **Deploy**

After deploy, the user gets:
- A working sGTM endpoint at `https://gtm.<their-domain>` (once their
  CNAME propagates) — or initially at `https://gtm-XXX.dublyo.xyz`
- A health endpoint at `/healthz` they can monitor with Uptime Kuma

### Custom domain

**Always recommend the user use a custom domain** (`gtm.<saas-domain>`).
Without it:
- Ad blockers using URL/hostname lists block `*.dublyo.xyz`
- The first-party tracking benefit is lost (cookies are scoped to
  `dublyo.xyz`, not their domain)

Dublyo handles the custom domain setup the same way as any deployment
(see `dublyo-deploy` skill Part 5 — CNAME → customers.dublyo.co).

---

## Part 3 — GTM Web + Server, or Server only?

This is the user's actual decision. Honest answer:

### Use **GTM Web + Server (hybrid)** if:

- ✅ User wants third-party tags that only exist client-side
  (Hotjar, Intercom widget, Crisp chat, LinkedIn Insight Tag, Reddit
  Pixel, Pinterest Tag, Quora Pixel — none have great server-side
  options)
- ✅ User wants non-developers to manage tags later (marketing team
  edits in Tag Manager UI, no code deploys needed)
- ✅ User has a multi-page-load SaaS where page views matter
- ✅ User is doing complex ad attribution across many networks

### Use **Server only** (no GTM Web) if:

- ✅ User has a **pure SPA / mobile app** where they control every event
  dispatch in code
- ✅ User cares mainly about **conversion tracking for paid ads** (signup,
  purchase, trial) — these are server-side events anyway
- ✅ User is privacy-focused and wants **zero third-party JS** in their
  client bundle (no `googletagmanager.com` script tag at all)
- ✅ User's frontend already calls their own API for every meaningful
  user action — they can just have the API forward to sGTM
- ✅ User uses PostHog / Mixpanel / their own analytics SDK for product
  analytics, and only needs sGTM for ad-conversion APIs

### My read for **a fresh SaaS being launched today**

**Start hybrid** unless they have a clear reason for server-only:

| Aspect | Hybrid (Web + Server) | Server only |
|---|---|---|
| Setup time | ~2 hours | ~6 hours (more custom code) |
| Maintainability | Marketing team can edit tags in UI | Dev team only |
| iOS/ad-blocker bypass for ad conversions | ✅ (via Server) | ✅ |
| Site-wide analytics (page views, scroll, clicks) | ✅ (via Web) | ⚠️ Must dispatch every event from app code |
| Hotjar / Intercom widget etc | ✅ Trivial | ❌ Skip them or embed manually |
| Privacy story | Marginally worse (loads google's script) | Cleaner |
| What it costs the user | Time only | Time only |

For 90% of SaaS, **hybrid is the right call** for the first 6 months.
Migrate to server-only later if privacy posture becomes a differentiator.

---

## Part 4 — DataLayer schema for SaaS

This is the canonical event taxonomy. The frontend (Web container OR
direct dispatch to sGTM) pushes to `window.dataLayer`. GTM normalizes,
enriches, and routes.

### The five-bucket SaaS event taxonomy

Push events to `dataLayer` with this shape:

```js
window.dataLayer.push({
    event: '<event_name>',
    // user identity (always include when known)
    user_id:        '<your-internal-user-id>',     // hashed server-side via Powerup
    user_email:     '<email>',                      // hashed server-side
    user_plan:      'free|pro|enterprise',
    user_created:   '<ISO-timestamp>',
    // request context (auto-collected by GTM Web; manually add for server-only)
    page_path:      window.location.pathname,
    page_title:     document.title,
    referrer:       document.referrer,
    // event-specific properties below
    ...
})
```

### Bucket 1 — Acquisition

```js
// First time user arrives + identifies (login or signup)
{ event: 'sign_up',     method: 'email|google|github', user_id: '...' }
{ event: 'login',       method: 'email|google',         user_id: '...' }
{ event: 'logout',      user_id: '...' }
```

### Bucket 2 — Activation

The single most important bucket for SaaS — these are your North Star
funnel.

```js
{ event: 'onboarding_started',        step: 1 }
{ event: 'onboarding_step_completed', step: 2, step_name: 'connect_data_source' }
{ event: 'onboarding_completed',      total_steps: 5, time_spent_sec: 240 }

// "Aha moment" — first time user gets value from the product
{ event: 'first_value',     value_action: 'first_deploy|first_invite|first_export' }
```

### Bucket 3 — Engagement

```js
{ event: 'feature_used',   feature: 'export_csv|invite_team_member|api_call', count: 1 }
{ event: 'search',         query: 'pricing', results_count: 3 }
{ event: 'content_view',   content_type: 'dashboard|doc|video', content_id: '...' }
```

### Bucket 4 — Monetization (conversion APIs care most about these)

```js
// Subscription flow
{ event: 'trial_started',          plan: 'pro', trial_days: 14 }
{ event: 'begin_checkout',         plan: 'pro', value: 49.00, currency: 'USD' }
{ event: 'add_payment_info',       plan: 'pro', payment_method: 'card' }
{ event: 'purchase',
  transaction_id: 'inv_xxx',
  value: 49.00,
  currency: 'USD',
  items: [{ item_id: 'pro_monthly', item_name: 'Pro Monthly', price: 49.00, quantity: 1 }]
}
{ event: 'subscription_started',   plan: 'pro', value: 49.00, currency: 'USD', billing_cycle: 'monthly' }
{ event: 'subscription_cancelled', plan: 'pro', reason: 'too_expensive', mrr_lost: 49.00 }
{ event: 'trial_converted',        plan: 'pro', trial_days_used: 11 }
{ event: 'refund',                 transaction_id: 'inv_xxx', value: 49.00 }
```

### Bucket 5 — Errors & friction

```js
{ event: 'error',              error_type: 'api_4xx|api_5xx|client_js', message: '...' }
{ event: 'page_not_found',     attempted_path: '/foo' }
{ event: 'form_error',         form: 'signup', field: 'email', error: 'invalid_format' }
```

### Identifying the user (server-side hashing via Powerup)

When you have a user ID, push it **once per session** as a `user_identify`
event AND include `user_id` on every subsequent event. With the
**UserID Powerup enabled** in the Dublyo GTM deploy:
- User IDs get SHA-256 hashed before forwarding to Google/Meta/etc
- Their analytics see a stable ID per user without leaking the PII
- Compliant with most privacy frameworks

```js
window.dataLayer.push({
    event: 'user_identify',
    user_id:    '<your-internal-id>',           // gets hashed by Powerup
    user_email: 'alice@example.com',            // hashed
    user_plan:  'pro',
    user_created: '2026-01-15T10:00:00Z',
})
```

---

## Part 5 — Wire the frontend (env-driven, SPA-friendly)

The user adds the GTM container URLs to their frontend env, then the
frontend either loads GTM Web (hybrid) or dispatches events directly to
sGTM (server-only).

### Env vars to add to the frontend

```env
# Hybrid mode — both required
NEXT_PUBLIC_GTM_WEB_ID=GTM-XXXXXXX                  # client-side container
NEXT_PUBLIC_GTM_SERVER_URL=https://gtm.example.com  # the Dublyo sGTM endpoint

# Server-only mode — just the server URL
NEXT_PUBLIC_GTM_SERVER_URL=https://gtm.example.com
```

(Use whatever prefix your framework needs: `NEXT_PUBLIC_` for Next.js,
`NUXT_PUBLIC_` for Nuxt, `VITE_` for Vite/React, `PUBLIC_` for SvelteKit.)

### Hybrid mode wiring (Next.js / React example)

```tsx
// app/layout.tsx (Next.js 13+)
import Script from 'next/script'

const GTM_ID = process.env.NEXT_PUBLIC_GTM_WEB_ID
const GTM_SERVER = process.env.NEXT_PUBLIC_GTM_SERVER_URL!

export default function RootLayout({ children }) {
  return (
    <html>
      <head>
        {/* GTM Web loaded from FIRST-PARTY domain via Dublyo's sGTM — this is the trick */}
        <Script id="gtm-init" strategy="afterInteractive">
          {`
            (function(w,d,s,l,i){
              w[l]=w[l]||[];
              w[l].push({'gtm.start': new Date().getTime(), event:'gtm.js'});
              var f=d.getElementsByTagName(s)[0],
                  j=d.createElement(s);
              j.async=true;
              j.src='${GTM_SERVER}/${process.env.NEXT_PUBLIC_GTM_LOADER_PATH || 'gtm.js'}?id=${GTM_ID}';
              f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','${GTM_ID}');
          `}
        </Script>
      </head>
      <body>{children}</body>
    </html>
  )
}
```

**The trick**: loading `gtm.js` from `${GTM_SERVER}` (your first-party
domain) instead of `googletagmanager.com`. The Dublyo sGTM container
serves `gtm.js` from the same domain users are already on → ad blockers
that filter by hostname can't block it → 30-40% more events get through.

### Server-only mode wiring (direct dispatch to sGTM)

If skipping GTM Web entirely, your code dispatches events directly:

```tsx
// lib/analytics.ts
const GTM_SERVER = process.env.NEXT_PUBLIC_GTM_SERVER_URL!

export async function track(event: string, properties: Record<string, any> = {}) {
  // Send to sGTM Measurement Protocol endpoint
  // (this matches the standard GA4 server-side schema)
  await fetch(`${GTM_SERVER}/g/collect?v=2`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      client_id: getOrCreateClientId(),   // see helper below
      user_id:   getCurrentUserId(),
      events: [{ name: event, params: properties }],
    }),
    credentials: 'include',  // include first-party cookies
  })
}

function getOrCreateClientId(): string {
  let id = localStorage.getItem('_dublyo_cid')
  if (!id) {
    id = crypto.randomUUID()
    localStorage.setItem('_dublyo_cid', id)
  }
  return id
}
```

Use this for every event: `track('sign_up', { method: 'google' })`.

### Mobile (React Native / Flutter / native iOS/Android)

For mobile apps, **server-only is usually the right choice** (no JS
runtime, no GTM Web). Use the platform's HTTP client to POST to the same
sGTM endpoint:

```js
// React Native
fetch(`${GTM_SERVER}/mp/collect`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    client_id: deviceId,                // expo-application or similar
    user_id:   currentUserId,
    events: [{ name: 'purchase', params: { value: 49.00, currency: 'USD' } }],
  }),
})
```

Same sGTM endpoint serves both web and mobile — no extra deployment.

### Responsive / desktop vs mobile-view note

The user mentioned "compatible with mobile + desktop view". Same code
runs in both — `window.dataLayer` exists in any browser, regardless of
viewport. Don't add separate tracking for mobile breakpoints; that's a
common mistake. Just track the events the same way; in GTM you can
filter by `screen_resolution` or `device_category` if you need
mobile-specific reports.

---

## Part 6 — Server-side events (backend → sGTM)

The most valuable events are **server-side** because they can't be
blocked or spoofed:
- Purchase confirmed by your payment webhook
- Subscription started from Stripe / PayPal webhook
- User upgrade from your billing system
- Email verified / phone verified

Wire these from the user's **custom API** (see `dublyo-deploy` skill —
the recommended pattern is a Go/NestJS API container deployed via
Dublyo's GitHub builds, sitting next to PocketBase + Redis).

```go
// Go example — backend POSTs directly to sGTM after Stripe webhook
func handleStripeWebhook(w http.ResponseWriter, r *http.Request) {
    var event stripe.Event
    json.NewDecoder(r.Body).Decode(&event)

    if event.Type == "checkout.session.completed" {
        s := event.Data.Object.(stripe.CheckoutSession)
        payload := map[string]any{
            "client_id": s.ClientReferenceID,       // set by frontend before checkout
            "user_id":   s.CustomerEmail,            // your internal user ref
            "events": []map[string]any{{
                "name": "purchase",
                "params": map[string]any{
                    "transaction_id": s.ID,
                    "value":          float64(s.AmountTotal) / 100,
                    "currency":       string(s.Currency),
                    "items":          [...],
                },
            }},
        }
        body, _ := json.Marshal(payload)
        // POST to sGTM — works server-to-server, no browser involved
        http.Post(os.Getenv("GTM_SERVER_URL")+"/mp/collect", "application/json", bytes.NewReader(body))
    }
}
```

**Why this matters**: a purchase tracked via server-side webhook is
**100% reliable**. The same purchase tracked client-side via `track()`
in the success page might be missed if the user closes the tab before
the event fires (happens ~10-15% of the time on mobile).

### Stitching client + server events

To prevent double-counting in GA4 / FB:
- Frontend dispatches `purchase` immediately when user clicks "Pay"
- Backend dispatches `purchase` after webhook confirms
- Both events include the same `transaction_id`
- sGTM dedupes by `transaction_id` before forwarding to GA4 + Meta

In Tag Manager Server UI:
- Add an event-data variable: `transaction_id`
- Configure the GA4 + Meta tags to use it as the **dedup key**

---

## Part 7 — Connect destinations (the actual money part)

Set these up in `tagmanager.google.com` → your server container → Tags.

### GA4 (Google Analytics 4)

- **Tag type**: GA4 (built-in)
- **Trigger**: All events from the client (or specific events)
- **Measurement ID**: `G-XXXXXXXXXX` from `analytics.google.com`
- Result: all events visible in GA4 Realtime + DebugView

### Meta Conversions API (FB Pixel server-side)

- **Tag type**: "Facebook Conversions API Tag" (community gallery template)
- **Pixel ID**: from Facebook Events Manager
- **Access Token**: generate in Events Manager → Settings → Conversions
  API → Generate Access Token
- **Event Mapping**: map your dataLayer events to FB's standard events:
  - `sign_up` → `CompleteRegistration`
  - `purchase` → `Purchase` (with `value`, `currency`, `content_ids`)
  - `begin_checkout` → `InitiateCheckout`
  - `add_payment_info` → `AddPaymentInfo`
  - `subscription_started` → `Subscribe`
- **Why server-side matters**: iOS 14.5+ ATT blocks ~70% of pixel
  conversions. CAPI bypasses that via server-to-server hashed-email
  matching. Critical for FB ad attribution.

### TikTok Events API

- **Tag type**: "TikTok Server-Side Events" template
- **Pixel ID**: from TikTok Events Manager
- **Access Token**: TikTok Events Manager → Settings
- Standard event mapping:
  - `sign_up` → `CompleteRegistration`
  - `purchase` → `CompletePayment`
  - `add_payment_info` → `AddPaymentInfo`
  - `subscription_started` → `Subscribe`
- TikTok requires `event_id` for dedup (use your `transaction_id` for
  purchase events)

### Snapchat Conversions API

- **Tag type**: "Snap Conversions API" template
- **Pixel ID**: from Snapchat Business Manager
- **Long-Lived Token**: Settings → Conversions API → Generate
- Event mapping similar to Meta.

### LinkedIn Conversions API

- **Tag type**: "LinkedIn Insight Tag Conversion" template
- **Partner ID** + **Access Token** from LinkedIn Campaign Manager
- For B2B SaaS — LinkedIn ads only work well with CAPI now.

### Google Ads

- **Tag type**: Google Ads Conversion (built-in)
- **Conversion ID** + **Label** from Google Ads UI
- Map `purchase`, `sign_up`, etc. to your configured conversion actions.

---

## Part 8 — Verification (using Dublyo templates + vendor helpers)

You need to verify events are actually landing. Two layers:

### Layer 1 — vendor-specific helpers (browser extensions)

| Pixel | Helper |
|---|---|
| GA4 | https://chrome.google.com/webstore/detail/google-analytics-debugger (or DebugView in GA4) |
| FB Pixel | https://chrome.google.com/webstore/detail/facebook-pixel-helper |
| TikTok | https://chrome.google.com/webstore/detail/tiktok-pixel-helper |
| Snapchat | https://chrome.google.com/webstore/detail/snap-pixel-helper |
| LinkedIn | https://chrome.google.com/webstore/detail/linkedin-insight-tag-help |

Plus each platform's own **Events Manager** has a "Test Events" view
that shows events in realtime as you trigger them.

GTM itself has **Preview Mode**: in Tag Manager UI, click "Preview",
enter your site URL, navigate around — see every tag fire in real time.

### Layer 2 — Dublyo templates for cross-checking + product analytics

These complement GTM, they don't replace pixel helpers:

| Dublyo template | Role | Slug |
|---|---|---|
| **PostHog** | Captures every event independently. Session replay = literally watch the user trigger events. Best general-purpose verification because you can see what dataLayer pushed AND replay the session. | `posthog` |
| **Matomo** | Self-hosted GA4 alternative. Useful if user wants their own analytics on Dublyo instead of (or alongside) GA4. Verifies events landed without depending on Google. | `matomo` |
| **Plausible** / **Umami** | Privacy-focused web analytics. Verify page views + basic events. Doesn't capture custom event params well. | `plausible`, `umami` |
| **GrowthBook** | Feature flags + A/B test framework. Reads from PostHog/GA4. Useful for "did the conversion actually correlate with the experiment". | `growthbook` |

### Recommended verification stack for a fresh SaaS

Deploy these three (all from Dublyo template catalog):

1. **Dublyo sGTM** (the one in this skill) — first-party endpoint
2. **PostHog** (template) — independent capture + session replay +
   feature flags + funnels. Use the PostHog SDK in your frontend
   alongside the dataLayer.
3. **Uptime Kuma** (template) — monitor `https://gtm.<saas>.com/healthz`
   to alert if sGTM goes down

Then verify the funnel end-to-end:
- Fire `sign_up` event → see it in PostHog Realtime → see it in GA4
  Realtime → see `CompleteRegistration` in FB Events Manager
- Fire `purchase` → see it in PostHog + GA4 + FB + TikTok + GA

All four should agree on the count within ~5%. If they don't, something
is mis-mapped in one of the GTM tags.

---

## Part 9 — Common pitfalls

| Mistake | Fix |
|---|---|
| User uses `*.dublyo.xyz` URL for sGTM (no custom domain) | Always set up `gtm.<their-domain>` CNAME. First-party tracking is the entire point. |
| User puts FB Pixel ID in code AND in GTM Web Container | Pick one — duplicate fires → 2× inflated counts. Put it in GTM Web only. |
| User fires `purchase` from frontend success page | Add server-side dispatch from payment webhook too (dedupe via `transaction_id`). Frontend events miss ~10-15% on mobile. |
| User sends PII (email, name) in dataLayer events to GA4 | GA4 explicitly forbids this. Enable Dublyo's **UserID Powerup** to hash server-side, or hash in your own code before push. |
| User configures both Web container ID and Server container ID with the same destination tags | Causes duplicate events. Tags should be in EITHER Web OR Server, not both. Best practice: server holds all CAPI-style tags; web holds only widgets / third-party scripts that need DOM. |
| User forgets to enable Consent Mode | If targeting EU users, GA4 + FB tags need consent state in dataLayer. Use GTM Built-in Consent Mode + a cookie banner (Cookiebot, or roll your own). |
| User deploys sGTM on a tunnel-mode server but doesn't add CNAME for the custom domain | Custom domain on tunnel server requires the orange-cloud shim flow — see `dublyo-deploy` Part 5. |
| User tries to set up GTM Server before having a GTM Container Config | Order matters: Google Tag Manager → create Server container → grab Container Config → THEN Dublyo deploy form. |

---

## Quick reference card

| What | Value |
|---|---|
| Dublyo GTM dashboard | https://app.dublyo.com/dashboard/gtm |
| Image used | `gcr.io/cloud-tagging-10302018/gtm-cloud-image:stable` (Google's official sGTM) |
| Optional proxy sidecar | `ghcr.io/dublyo/gtm-powerup:latest` (CookieKeeper, UserID hash, BotDetection, IPBlocklist) |
| Default custom domain pattern | `gtm.<their-saas-domain.com>` (CNAME → customers.dublyo.co) |
| Frontend env (hybrid) | `NEXT_PUBLIC_GTM_WEB_ID` + `NEXT_PUBLIC_GTM_SERVER_URL` |
| Frontend env (server-only) | `NEXT_PUBLIC_GTM_SERVER_URL` |
| Health check | `GET https://gtm.<domain>/healthz` |
| GTM Web loader path | `${GTM_SERVER_URL}/gtm.js?id=GTM-XXX` (first-party!) |
| Server-side events endpoint | `${GTM_SERVER_URL}/g/collect` (web) or `/mp/collect` (mobile) |
| GTM Container Config source | https://tagmanager.google.com (Server container → Manual provisioning) |

---

## Companion skills

- **`dublyo-deploy`** — for the platform basics (Panel API restrictions,
  dashboard flow, custom domain CNAME for `gtm.<their-domain>`)
- **`dublyo-pocketbase`** — if the user is building backend on PocketBase
  + custom API, the server-side event dispatch from the custom API
  container pattern lives there
- **`dublyo-saas-foundation`** (future) — the larger "SaaS bootstrap"
  skill should reference THIS skill for the analytics stack
