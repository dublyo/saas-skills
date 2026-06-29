---
name: saas-product-growth
description: Build, plan, or review SaaS products with product architecture, monetization, operational readiness, and embedded growth loops considered during development. Use when the user asks to create, spec, audit, or improve a SaaS app, dashboard, CRUD system, PocketBase or Supabase-backed product, billing/subscription workflow, team/workspace product, PLG/free-tool funnel, referral/shareable-report loop, white-label/reseller offer, SaaS marketing surface, onboarding flow, activation flow, retention workflow, or product-growth review.
---

# SaaS Product Growth

## Core Intent

Use this skill to make SaaS development commercially complete, not just technically functional.

While building or reviewing, connect four layers:

1. Product workflow: dashboard, CRUD, states, roles, permissions, teams, and data ownership.
2. Monetization: plans, entitlements, usage limits, billing state, invoices, and payment webhooks.
3. Operations: admin tools, support, observability, backups, security, testing, and cost control.
4. Growth: onboarding, activation, free tools, shareable outputs, referrals, SEO/GEO surfaces, lifecycle emails, partner loops, and social proof.

If the task is a new feature or app and the user has not approved a spec, produce a product-growth spec or review first. If coding is approved, use this skill as a build checklist and keep changes scoped to the selected stage.

## Operating Workflow

1. Identify the product stage: MVP, production-ready, scale, or enterprise.
2. Identify the SaaS motion: self-serve, sales-assisted, team/workspace, agency/white-label, API-first, marketplace/integration-led, or enterprise.
3. Map the core workflow before naming stack details:
   - Actors and roles.
   - Workspace or tenant ownership.
   - Main CRUD objects.
   - Workflow states and transitions.
   - Dashboard views and daily actions.
   - Events that should be logged, billed, notified, or analyzed.
4. Add monetization gates:
   - Plans and entitlements.
   - Usage meters and reset periods.
   - Feature gates in backend logic, not only UI.
   - Billing lifecycle and webhook idempotency.
   - Cost per customer and per feature.
5. Add product-led growth hooks where natural:
   - Free tool or sample output.
   - Public/shareable report, status page, badge, embed, or client link.
   - Invite/referral/team expansion loop.
   - Onboarding checklist and activation events.
   - Lifecycle emails and in-app nudges.
   - Review/case-study/social-proof capture.
6. Add operational readiness:
   - Admin dashboard and support tools.
   - Security, audit logs, data isolation, backups, restore tests, alerts.
   - Tests for permissions, billing, usage limits, webhooks, jobs, and tenant boundaries.
7. Output a prioritized plan:
   - Must ship now.
   - Should ship before paid customers.
   - Later scale/enterprise items.
   - Explicit non-goals to avoid overbuilding.

## Review Mode

When reviewing an existing SaaS repo, inspect the connected surfaces together:

- Schema and tenant ownership.
- Backend authorization and feature gating.
- Frontend dashboard, empty/loading/error states, and plan-state UX.
- Billing checkout, portal, subscription state, webhook handling, retries, and idempotency.
- Usage metering, quotas, rate limits, and abuse controls.
- Background jobs, queues, cron, retries, progress, and dead-letter handling.
- Email deliverability, notifications, preferences, and unsubscribe behavior.
- Analytics events, activation metrics, revenue metrics, and cost metrics.
- Admin/support tools, impersonation controls, and audit trails.
- Public growth surfaces such as SEO pages, free tools, share links, badges, templates, review prompts, and referral flows.

Return findings by severity or release stage. Do not treat a feature as complete if it is only hidden in the UI but not enforced in backend rules.

## Reference Routing

Load only the reference needed for the task:

- `references/product-architecture-checklist.md`: full SaaS component checklist for product, frontend, backend, database, auth, teams, billing, APIs, storage, jobs, security, analytics, testing, legal, support, cost, and vendors.
- `references/growth-marketing-checklist.md`: SaaS marketing channels and product-embedded growth mechanics such as PLG, free tools, SEO, GEO/AEO, referrals, affiliates, white-label, integrations, reviews, lifecycle email, paid ads, virality, and localization.
- `references/stage-gates.md`: MVP, production-ready, scale, and enterprise gates plus the highest-risk forgotten SaaS items.
- `references/pocketbase-supabase-mapping.md`: pragmatic mapping for PocketBase/Supabase apps, including auth rules, RLS/collection rules, subscriptions, storage, background jobs, admin tooling, and product-growth events.
- `references/source-coverage.md`: map from the original two source files to the converted skill references.

If this skill is used alongside `saas-kit`, let `saas-kit` drive the spec-first artifact workflow and use this skill to enrich the SaaS component, monetization, and growth coverage.

## Output Shapes

For a new SaaS idea, produce:

- Product stage and SaaS motion.
- Core workflow map.
- Data and ownership model.
- Dashboard and CRUD requirements.
- Monetization and entitlement rules.
- Growth hooks to build into the product.
- Operational gates.
- Testing and verification plan.
- Implementation sequence.

For an existing repo review, produce:

- Critical blockers.
- Missing SaaS core items.
- Missing growth/product loops.
- PocketBase/Supabase-specific risks if relevant.
- Practical next implementation steps.

For implementation after approval, produce or update only the pieces needed for the chosen release stage. Avoid adding enterprise, scale, or marketing-channel machinery before it has a product reason.
