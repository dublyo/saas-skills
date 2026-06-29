# PocketBase And Supabase Mapping

Use this reference when the SaaS app uses PocketBase or Supabase. Verify exact API syntax against the installed version or official docs before implementation.

## Table Of Contents

- Shared Design Rules
- Typical Data Model
- Supabase Mapping
- PocketBase Mapping
- Billing And Entitlement Flow
- Usage Metering Flow
- Public Sharing Flow
- Provider Decision Notes

## Shared Design Rules

For either provider:

- Model tenant ownership explicitly with `organization_id`, `workspace_id`, `owner_id`, or equivalent fields.
- Enforce access in backend rules, RLS policies, server code, or collection rules. UI hiding is not authorization.
- Keep subscription/payment provider state separate from entitlement decisions.
- Store plan, subscription status, billing customer ID, current period, usage period, and entitlement grants in local tables/collections.
- Let payment webhooks update local subscription state.
- Make webhook handlers idempotent.
- Track usage server-side for cost-bearing actions.
- Use storage access rules that match database ownership.
- Add admin/support views only with audit logging.
- Avoid putting secrets in client code.

## Typical Data Model

Core:

- `users` or auth users.
- `organizations`.
- `organization_members`.
- `invitations`.
- `roles` or role field.
- Product collections/tables with `organization_id`.

Monetization:

- `plans`.
- `subscriptions`.
- `entitlements`.
- `usage_records`.
- `payments`.
- `invoices`.
- `billing_events`.

Operations:

- `audit_logs`.
- `activity_logs`.
- `notifications`.
- `feature_flags`.
- `api_keys`.
- `webhook_endpoints`.
- `webhook_deliveries`.
- `jobs` or external job references.
- `support_notes`.

Growth:

- `lead_sources`.
- `activation_events`.
- `referrals`.
- `affiliate_clicks`.
- `shared_links`.
- `public_reports`.
- `email_events`.
- `review_prompts`.
- `partner_accounts`.

## Supabase Mapping

Use Supabase strengths:

- Auth for identity.
- Postgres schema for relational SaaS data.
- Row Level Security for tenant isolation.
- Storage for files with signed URLs and bucket policies.
- Edge Functions or server routes for privileged operations.
- Realtime only where the workflow benefits.

Supabase checks:

- RLS enabled on tenant-owned tables.
- Policies cover select, insert, update, delete separately.
- Policies account for membership and role.
- Service-role key never reaches the browser.
- Storage buckets have matching tenant access rules.
- Triggers/functions do not bypass intended ownership rules.
- Billing webhooks run in a server-only environment.
- Usage writes cannot be forged from client code.
- Admin screens use privileged server code and audit logs.

Common patterns:

- `organizations` table.
- `organization_members` table linking auth users to orgs.
- Product tables include `organization_id`.
- RLS checks membership.
- Entitlement checks happen in server actions/API routes/functions before expensive work.
- Payment webhook verifies provider signature, updates `subscriptions`, then derives current entitlements.

Growth implementation:

- Free tool can write anonymous lead records or signed-in activation events.
- Shareable reports can be represented as private report plus public share token.
- Referral links map to referral code and attribution event.
- Lifecycle email triggers come from server-side activation and usage events.

## PocketBase Mapping

Use PocketBase strengths:

- Collections for product data.
- Auth collections for users/admins.
- Collection API rules for access control.
- File fields for simple storage needs.
- Hooks/extensions/server code for privileged workflows.
- Admin UI for internal operations during early stages.

PocketBase checks:

- Collection list/view/create/update/delete rules include tenant and role checks.
- File access follows the same ownership rules as records.
- Sensitive fields are hidden from client responses where needed.
- Hooks validate paid entitlements before expensive actions.
- Payment webhooks are handled server-side and update subscription collections.
- Jobs/queues are not forced into request handlers if tasks are heavy.
- Admin actions are logged if support staff can touch customer data.

Common patterns:

- `organizations` collection.
- `organization_members` collection.
- Product collections include organization relation.
- Rules check membership and role.
- `plans`, `subscriptions`, `entitlements`, and `usage_records` collections drive paid access.
- A server-side hook or app backend checks entitlements before generating reports, running AI, scraping, exporting, or uploading large files.

Growth implementation:

- Public report collection can use an unguessable share token plus explicit public flag.
- Agency/white-label features can be organization settings and branded report templates.
- Referral/affiliate tracking can be a collection updated on signup and subscription conversion.
- Free tool submissions can become leads, but must have rate limits and abuse controls.

## Billing And Entitlement Flow

Recommended flow:

```text
User chooses plan
-> app creates checkout session server-side
-> payment provider redirects user
-> webhook confirms subscription state
-> app updates local subscription record
-> entitlement resolver derives allowed features and limits
-> backend checks entitlements before protected actions
```

Do not unlock paid access only because the checkout success page loaded.

## Usage Metering Flow

Recommended flow:

```text
User requests cost-bearing action
-> backend verifies tenant, role, plan, quota, and rate limit
-> backend reserves or records usage
-> job/action runs
-> usage finalizes with status, cost, and provider metadata
```

Track failed, canceled, retried, and completed usage differently when cost matters.

## Public Sharing Flow

Recommended flow:

```text
Owner creates object
-> owner enables sharing
-> system creates share token or public slug
-> public route shows only safe fields
-> analytics records views/conversions
-> recipient can request access or sign up
```

Public sharing must never expose private tenant data, internal notes, billing data, raw logs, or hidden file URLs.

## Provider Decision Notes

PocketBase is often pragmatic for:

- Small teams.
- Fast MVPs.
- Simple admin needs.
- Projects that benefit from a single small backend.

Supabase is often pragmatic for:

- Hosted Postgres.
- Strong relational queries.
- RLS-heavy multi-tenant apps.
- SQL reporting.
- Larger ecosystem integrations.

For both, the SaaS product model matters more than the provider. A weak tenant model, missing entitlement resolver, or untested webhook flow will fail on either stack.
