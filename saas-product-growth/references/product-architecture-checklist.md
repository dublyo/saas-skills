# Product Architecture Checklist

Use this reference when planning or reviewing the SaaS product itself: workflows, dashboard, CRUD, tenancy, billing, operations, and product reliability.

## Table Of Contents

- Product And Business Model
- Frontend And UX
- Backend And Business Logic
- Database And Data Architecture
- Authentication
- Authorization, Tenancy, And Teams
- Plans, Entitlements, Usage, And Quotas
- Billing And Subscription Management
- APIs And Webhooks
- File Storage And Media
- Background Processing
- Caching And Performance
- Communication And Notifications
- Search
- Admin Dashboard And Internal Tools
- Feature Flags
- Security
- Observability And Analytics
- Reliability And Resilience
- DevOps And Infrastructure
- Backup And Disaster Recovery
- Testing
- Localization And Internationalization
- Legal, Privacy, And Compliance
- Support, Status, And Releases
- Growth, Cost, And Vendors

## Product And Business Model

Define before implementation:

- Problem solved and pain level.
- Target audience, buyer, user, and admin personas.
- Core use case and success moment.
- Pricing motion: free, trial, freemium, paid, annual, usage-based, per-seat, per-workspace, enterprise.
- Product type: B2C, B2B, agency, enterprise, API-first, marketplace, or internal SaaS.
- Single-user versus team/workspace product.
- Key metrics: activation, conversion, retention, churn, MRR, ARR, ARPU, LTV, CAC, usage, cost per customer.

Development implication: pricing, plans, roles, and tenant ownership are product architecture decisions, not landing-page copy.

## Frontend And UX

Required user-facing surfaces:

- Landing, pricing, signup, login, onboarding, dashboard, settings, billing, account, notification center, help/support.
- Core CRUD screens with create, read, update, delete, duplicate, archive, restore, filters, sorting, pagination, search, bulk actions when needed.
- Empty states, loading states, error states, success states, permission-denied states, plan-limit states, and payment-failed states.
- Mobile/responsive behavior.
- Accessibility: labels, focus states, keyboard navigation, contrast, semantic structure.
- Form validation, autosave or unsaved-change protection, confirmations, undo where destructive actions exist.
- Demo data, guided tour, first-use checklist, and activation prompt.

UX rule: the dashboard should make the next user action obvious without explaining the whole product in visible help text.

## Backend And Business Logic

Backend is the product brain. It must enforce:

- Business rules and validations.
- Authorization and tenant boundaries.
- Subscription and entitlement access.
- Usage limits, rate limits, and abuse controls.
- Workflow state transitions.
- File/report/AI/scraping/media processing.
- Background jobs, queues, retries, and idempotency.
- Events for analytics, billing, notifications, audits, and webhooks.

Do not trust frontend hiding for any paid feature, admin action, tenant data, or destructive action.

## Database And Data Architecture

Core entities usually include:

- Users, sessions, identities, organizations, workspaces, team members, invitations, roles.
- Plans, subscriptions, payments, invoices, coupons, entitlements, usage records.
- Product objects such as projects, tasks, files, reports, websites, scans, forms, messages, tickets, or domain-specific records.
- Notifications, activity logs, audit logs, API keys, webhooks, settings, feature flags, support records.

Database engineering checklist:

- Clear relationships and ownership columns.
- Foreign keys or equivalent referential controls.
- Indexes for tenant queries, dashboard filters, search, status, created dates, and billing lookups.
- Constraints for uniqueness, valid state, nonnegative usage, and legal enum values.
- Migrations, rollback plan, seed/demo data, pagination, transactions, soft delete, retention, archiving.
- Query optimization, pooling, N+1 prevention, and long-running report strategy.

Data safety:

- Backups, point-in-time recovery where available, restore procedure, restore test evidence.
- Export, deletion, anonymization, retention, and legal hold strategy.
- Avoid sensitive data in logs and support/admin displays.

## Authentication

Cover the needed level:

- Basic: signup, login, logout, password reset, email verification, session management.
- Optional: OAuth, magic links, device/session list, MFA, recovery codes.
- Enterprise: SSO, SAML/OIDC, SCIM, domain verification, enforced MFA.

Map auth flows to onboarding and billing state. A logged-in user still may have no workspace, no plan, expired trial, failed payment, or revoked invitation.

## Authorization, Tenancy, And Teams

SaaS permission layers:

- User-level access.
- Workspace/org ownership.
- Role-based access.
- Permission-based access for sensitive actions.
- Plan-based access for paid capabilities.
- Object-level access for shared records, projects, reports, and files.

Team/workspace features:

- Create workspace.
- Invite member.
- Accept/reject invitation.
- Remove member.
- Transfer ownership.
- Change role.
- Multi-workspace switching.
- Per-workspace billing.
- Tenant audit logs.

Critical test: a user from tenant A must not access tenant B data through UI, API, file URLs, search, exports, public links, webhooks, or background jobs.

## Plans, Entitlements, Usage, And Quotas

Keep payment state separate from entitlement rules.

Entitlements:

- Which features are enabled per plan.
- Limits for users, seats, projects, files, websites, reports, AI credits, API calls, storage, export, integrations, support, white-label, and history retention.
- Upgrade/downgrade behavior.
- Grace period behavior.

Usage metering:

- Track per user, workspace, API key, feature, and period.
- Define reset periods: minute, day, month, billing cycle, or rolling window.
- Support hard limits, soft limits, overage, warnings, and near-limit alerts.
- Track cost-bearing usage separately from vanity metrics.

Rate limits:

- By IP, user, tenant, API key, endpoint, plan, and risk level.
- Separate abuse throttles from plan quota limits.

## Billing And Subscription Management

Billing surfaces:

- Checkout.
- Billing portal.
- Pricing table.
- Plan upgrade/downgrade/cancel/reactivate.
- Trial start/end.
- Invoice history.
- Tax/VAT where needed.
- Refunds, coupons, promo codes, credits.

Subscription lifecycle:

- Trialing, active, past due, unpaid, canceled, paused, expired, grace period.
- Failed payment recovery and dunning.
- Access restriction and restoration.
- Annual and monthly plan switching.

Payment webhooks:

- Verify signatures.
- Process asynchronously if needed.
- Make handlers idempotent.
- Deduplicate event IDs.
- Retry failed processing.
- Log event payload references safely.
- Support replay.
- Treat payment webhooks as source of truth for subscription state.

Never make paid access depend only on the client-side checkout redirect result.

## APIs And Webhooks

Internal APIs:

- REST, GraphQL, RPC, server actions, or framework routes.
- Standard errors, validation, auth, pagination, filtering, sorting, request IDs, timeouts.

Public APIs:

- API keys, scopes, rotation, revocation, plan access, rate limits, logs, docs, sandbox, versioning, deprecation.
- Idempotency keys for create/payment-like operations.
- SDKs only after API behavior stabilizes.

Incoming webhooks:

- Signature validation, retries, dedupe, async processing, DLQ/logging.

Outgoing webhooks:

- Event selection, endpoint secrets, signed payloads, delivery logs, retries, disable failing endpoints, replay, test event.

## File Storage And Media

Cover:

- Private/public buckets or containers.
- Signed URLs.
- Upload size/type validation.
- Secure object naming.
- Virus/malware scanning for risky uploads.
- Image/video optimization and thumbnails.
- CDN and cache headers.
- Versioning when needed.
- Lifecycle deletion and storage quotas.
- Multipart upload for large files.
- File access rules aligned with tenant and plan.

Examples: documents, images, PDFs, reports, exports, videos, screenshots, attachments, generated files, temporary imports.

## Background Processing

Use jobs for:

- Email sending.
- PDF/report generation.
- AI tasks.
- Scraping/crawling.
- Image/video processing.
- Imports/exports.
- Webhook delivery.
- Billing reconciliation.
- Long analytics aggregation.

Job requirements:

- Queue, worker, priority, retry/backoff, timeout, cancel, progress, dead-letter queue, monitoring, and replay.
- Avoid doing heavy work inside request/response paths.

## Caching And Performance

Possible cache layers:

- CDN, browser, application, database, Redis/cache service, API, session, precomputed reports.

Use caching only with a clear invalidation strategy. Protect dashboard performance with pagination, indexes, lazy loading, query limits, and background aggregation.

## Communication And Notifications

Transactional emails:

- Verify email, password reset, invite, receipt, payment failed, report ready, account deletion, security alert.

Deliverability:

- Sending domain, SPF, DKIM, DMARC, bounce handling, complaint handling, suppression list, unsubscribe, templates, logs.

Other channels:

- In-app, push, SMS, WhatsApp, Slack, Teams, webhooks.

Preferences:

- Category opt-in/out, quiet hours, digest frequency, and legal separation of transactional versus marketing messages.

## Search

Search can be simple database search first. Add external search when needed.

Cover:

- Full-text search, filters, sorting, facets, suggestions, recent searches, typo tolerance, permissions, search analytics.
- Tenant-aware search: do not leak restricted records through search results or counts.

## Admin Dashboard And Internal Tools

Admin surfaces:

- User lookup, org lookup, subscription state, invoices, plan override, usage, failed jobs, support tickets, webhooks, audit logs, feature flags, system health.

Support tools:

- Safe impersonation with explicit audit logs.
- Passwordless support access is dangerous unless tightly controlled.
- Mask sensitive data.
- Make destructive admin actions require confirmation and logging.

## Feature Flags

Use flags for:

- Beta access, per-user/org rollout, percentage rollout, environment toggles, experiments, emergency disable.

Flags should have owners, expiration intent, and backend enforcement where relevant.

## Security

Application security:

- Input validation, output encoding, SQL injection prevention, XSS prevention, CSRF protection, secure cookies, auth/session controls, upload validation, dependency scanning, secret handling.

Infrastructure security:

- HTTPS, CORS rules, CSP, firewall/WAF where needed, private networking, least privilege, key rotation, environment separation, encryption at rest/in transit.

Abuse prevention:

- Signup abuse, trial abuse, scraping abuse, API abuse, spam, credential stuffing, bot protection, anomaly detection.

Security operations:

- Security contact, incident process, vulnerability patching, audit logs, admin access review.

## Observability And Analytics

Logging:

- Auth, billing, webhooks, jobs, emails, errors, admin actions, permission denials, security events.

Monitoring and alerts:

- Uptime, latency, error rate, queue backlog, failed jobs, webhook failures, failed payments, backup failures, storage growth, API errors, email failures, suspicious usage.

Analytics:

- Product funnel, activation, adoption, cohorts, churn, retention, feature usage, dropoff.
- Business metrics: MRR, ARR, churn, LTV, CAC, ARPU, trial conversion, payment failure, revenue by plan/country.
- Usage/cost: API calls, AI tokens, storage, scraping, email/SMS, cost per customer.

Server-side events are required for trustworthy billing, activation, and revenue metrics.

## Reliability And Resilience

Build for:

- Timeouts, retries, exponential backoff, circuit breakers, graceful degradation, fallback providers, health checks, duplicate prevention, idempotency, DLQs, consistency checks, load shedding.

Sensitive workflows to make idempotent:

- Payment webhooks, account creation, invitation acceptance, usage charging, file import, report generation, webhook delivery, email sending.

## DevOps And Infrastructure

Environments:

- Local, development, staging, production, preview.

Deployment:

- CI/CD, tests, migrations, rollback, release logs, blue-green/canary when needed, zero-downtime migration strategy.

Configuration:

- Environment variables, secrets, validation, rotation, separation by environment.

Infrastructure:

- Hosting, domain, DNS, SSL, CDN, object storage, database, cache, queues, workers, cron, load balancing, autoscaling.

## Backup And Disaster Recovery

Cover:

- Database backups.
- File/object backups.
- Config/secret recovery path.
- Retention policy.
- Offsite backups.
- Point-in-time recovery if available.
- Restore docs and regular restore tests.
- RTO and RPO targets.
- Disaster recovery environment for scale/enterprise.

Untested restore means the backup is only a hope.

## Testing

Automated tests:

- Unit, integration, API, E2E, permission, payment, webhook, queue/job, migration, file upload.

Quality tests:

- Browser, mobile, accessibility, localization/RTL, performance, load, stress, security.

Critical SaaS tests:

- Tenant A cannot access tenant B data.
- Duplicate payment webhook updates subscription once.
- Failed job retries and reaches DLQ.
- Downgrade removes gated features.
- Deleted user loses access.
- Account deletion/export works.
- Restore from backup works.
- Plan limit blocks server-side actions.

## Localization And Internationalization

Cover:

- Arabic/English or target languages.
- RTL/LTR layout.
- Local dates, time, currency, numbers.
- Timezones: store UTC, display in user/org timezone.
- Translation files, pluralization, fallback language.
- Email, PDF/report, search, and support localization.

## Legal, Privacy, And Compliance

Baseline:

- Terms, privacy policy, cookie policy, refund policy, acceptable-use policy.
- DPA, subprocessors, consent, cookie consent, marketing consent.
- Account deletion, data export, retention, legal hold.
- Age, regional privacy, and tax requirements when applicable.

Privacy by design:

- Collect only necessary data.
- Define why each field exists.
- Control access.
- Define deletion timing.
- Avoid sensitive logs.
- Mask sensitive admin data.

## Support, Status, And Releases

Support:

- Contact form, support email, ticketing, live chat, help center, knowledge base, FAQ, tutorials, onboarding calls, feedback, bug reports, feature requests, enterprise SLA.

Status/releases:

- Public status page, incident updates, maintenance notices, changelog, release notes, in-app announcements, feature emails, API breaking-change notices, deprecation notices.

## Growth, Cost, And Vendors

Growth surfaces:

- Landing page, pricing page, comparison pages, SEO, blog, sitemap, structured data, Open Graph, email capture, waitlist, referral, affiliate, promo codes, attribution, marketing analytics, retargeting events, A/B tests.

Cost management:

- Infrastructure cost, cost per user/org, AI token cost, storage, bandwidth, email/SMS, scraping, third-party API cost, abuse detection, budget alerts, plan margin, cost-based quotas.

Vendor management:

- External service inventory, API limits, pricing limits, availability, data residency, lock-in risk, backup provider, API version changes, renewal dates, credential ownership, exit strategy.

Do not let the heart of the product depend on one provider without an exit or fallback plan.
