# Stage Gates

Use this reference to decide what belongs in the current release and what should wait.

## Table Of Contents

- MVP Gate
- Production-Ready Gate
- Scale Gate
- Enterprise Gate
- Highest-Risk Forgotten SaaS Items
- Review Output Template
- Implementation Sequencing

## MVP Gate

Must exist before first real users:

- Frontend for the core workflow.
- Backend for the core business action.
- Database schema for core objects.
- Authentication.
- Basic authorization.
- Core product feature.
- Payment checkout if paid from day one.
- Payment webhook handling if charging.
- Plan enforcement if multiple plans exist.
- Basic file storage if files are core.
- Transactional email.
- Simple admin dashboard.
- Error tracking.
- Backups.
- Privacy policy and terms.
- Basic analytics.
- One activation event.
- One growth hook if natural, such as invite, shareable output, free tool, or email capture.

MVP non-goals unless central:

- SSO/SAML.
- SCIM.
- Full ABM.
- Full reseller platform.
- Complex audit analytics.
- Multi-region infrastructure.
- Advanced compliance.

## Production-Ready Gate

Add after real demand or before charging serious customers:

- Teams and organizations.
- Usage metering.
- Queue workers.
- Better monitoring.
- Audit logs.
- Notification preferences.
- Billing portal.
- Failed payment recovery.
- Feature flags.
- Staging environment.
- Automated tests.
- Restore testing.
- Public status page.
- Lifecycle emails.
- Review/referral prompt timing.
- Support workflow.

Production-ready means a failed payment, duplicate webhook, stuck job, tenant-boundary bug, or backup restore issue has a known behavior and test path.

## Scale Gate

Add when usage and cost grow:

- Advanced caching.
- Search engine if database search is insufficient.
- Load balancing.
- Autoscaling.
- Cost analytics.
- Data archiving.
- Advanced fraud/abuse detection.
- Advanced observability.
- Multiple workers.
- Disaster recovery environment.
- Performance and load testing.
- Programmatic SEO if content quality can remain high.
- Affiliate/reseller dashboards if partner demand exists.
- Integration marketplace listings if integrations are stable.

Scale means margin and reliability matter as much as feature count.

## Enterprise Gate

Add when enterprise sales justify it:

- SSO/SAML.
- SCIM.
- Custom roles.
- Advanced audit logs.
- Data residency.
- SLA.
- DPA.
- Dedicated environments.
- IP allowlisting.
- Custom retention rules.
- Enterprise billing.
- Security reports.
- Compliance certifications.
- Procurement-friendly invoices and contracts.
- Sales-assisted onboarding.

Enterprise features should not be built early unless an actual customer or market segment requires them.

## Highest-Risk Forgotten SaaS Items

These are commonly missed and should be checked in almost every serious SaaS review:

1. Payment webhooks, including duplicate events, failed processing, replay, and retries.
2. Entitlements that connect every paid feature to the correct plan.
3. Usage metering before cost exceeds subscription revenue.
4. Email deliverability, not only sending email.
5. Tenant data isolation across UI, API, storage, search, export, jobs, and public links.
6. Background jobs instead of heavy request-time work.
7. Audit logs for who did what and when.
8. Restore testing, not only backup creation.
9. Cost monitoring per customer, feature, and provider.
10. Account deletion and data export from the beginning.
11. Admin impersonation controls.
12. Failed payment recovery.
13. Plan downgrade behavior.
14. Notification preferences and unsubscribe handling.
15. Public/shared artifact privacy controls.

## Review Output Template

When using this reference for a review, group output like this:

```text
Stage fit:
- Current apparent stage:
- Recommended stage target:

Must fix before users:
- ...

Must fix before paid customers:
- ...

Growth hooks worth building now:
- ...

Delay until scale or enterprise:
- ...

Tests to prove readiness:
- ...
```

## Implementation Sequencing

Prefer this order:

1. Core workflow and tenant-safe data model.
2. Auth, authorization, and dashboard CRUD.
3. Plan/entitlement model.
4. Billing/webhook lifecycle if paid.
5. Usage/cost tracking if usage-based, AI, scraping, storage-heavy, or API-heavy.
6. Admin/support visibility.
7. Observability, backups, and critical tests.
8. One or two product-growth loops.
9. Expansion channels after product activation is measured.

The goal is not to build every SaaS component immediately. The goal is to avoid painting the product into a corner.
