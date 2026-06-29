# dublyo-tag-manager-server skill

Helps an AI assist users who want to set up analytics + ad-pixel
conversion tracking on a SaaS hosted on Dublyo.

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | The skill itself (loaded by the AI). Covers: deploying Dublyo's sGTM via the dedicated dashboard, choosing between hybrid (Web+Server) and Server-only, the canonical SaaS dataLayer schema, frontend wiring (Next.js/React/Vue + mobile), server-to-server event dispatch from the user's custom API, connecting GA4 + Meta CAPI + TikTok + Snapchat + LinkedIn + Google Ads, and verification using PostHog + vendor pixel helpers. |

## No bundled reference file

This skill points the AI at upstream docs directly via WebFetch:
- https://developers.google.com/tag-platform/tag-manager/server-side
- https://developers.google.com/tag-platform/tag-manager/datalayer
- https://developers.facebook.com/docs/marketing-api/conversions-api
- https://business-api.tiktok.com/portal/docs (Events API)
- https://businesshelp.snapchat.com/s/article/conversions-api
- https://learn.microsoft.com/en-us/linkedin/marketing/conversions/

## Why this skill exists

SaaS founders systematically under-invest in tracking and end up
unable to scale paid ads because:
- Ad blockers kill 30-40% of pixel events
- iOS 14.5+ ATT cripples mobile attribution
- Pixels can't be updated without app redeploys
- Tag fragmentation between platforms is a manual sync nightmare

Dublyo's sGTM (Google's official server-side GTM image + Dublyo's
powerup sidecar) solves all of these — but only if the user wires up
the right dataLayer events from their frontend AND the server-side
conversion APIs from their backend. This skill teaches the AI to do
both.

## Companion skills

- `dublyo-deploy` — platform basics (where the user reaches the dashboard,
  custom domain CNAME setup)
- `dublyo-pocketbase` — when the user's backend is PocketBase + custom
  API, the server-side event dispatch lives in that custom API container
