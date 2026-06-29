---
name: moat
description: "Evaluate, design, or improve SaaS moats: the structural barriers that protect profitability, retention, pricing power, distribution, and long-term defensibility. Use when the user asks whether a SaaS idea is defensible, profitable, hard to copy, has a real moat, can survive AI copycats, has switching costs, network effects, workflow lock-in, proprietary data, integrations, white-label/reseller defensibility, system-of-record potential, pricing power, NRR expansion, CAC payback, gross-margin risk, or needs a moat-focused product/business review."
---

# Moat

## Core Rule

A SaaS moat is not a feature, a UI, a model wrapper, or "we will move fast."

A real moat must pass both tests:

1. Benefit: it creates higher customer value, lower cost, better retention, faster distribution, or better margins.
2. Barrier: competitors cannot cheaply copy, neutralize, or bypass it.

For SaaS, judge moats by their effect on profitability:

- Higher willingness to pay.
- Lower churn and higher gross revenue retention.
- Expansion revenue and stronger net revenue retention.
- Lower CAC or faster CAC payback.
- Higher gross margin or lower cost-to-serve.
- Stronger pricing power.
- Lower support/onboarding drag over time.
- More durable distribution.

## Operating Workflow

1. Identify the SaaS idea, customer, buyer, and workflow.
2. Identify the profit engine:
   - Pricing model.
   - Gross margin drivers.
   - Cost-to-serve.
   - Acquisition channel.
   - Retention and expansion mechanism.
3. Identify candidate moat types:
   - Switching costs.
   - Workflow/system-of-record depth.
   - Network effects.
   - Data advantage.
   - Integration depth.
   - Distribution advantage.
   - Brand/trust.
   - Scale or cost advantage.
   - Process power.
   - Ecosystem, marketplace, partner, reseller, or white-label channel.
   - Compliance, regulatory, procurement, or operational trust.
4. Test each candidate moat:
   - What customer behavior proves it?
   - What product function creates it?
   - What business metric should improve?
   - What must compound over time?
   - How would a competitor attack it?
   - Is it a real barrier or only temporary differentiation?
5. Convert the moat into product requirements:
   - Data model.
   - Dashboard/workflow.
   - Integrations.
   - Collaboration.
   - Permissions.
   - Audit/history.
   - Automation.
   - Sharing.
   - Billing/entitlements.
   - Analytics.
6. Output a moat plan with proof metrics and build sequence.

## Default Stance

Be skeptical.

Treat these as weak moat claims unless proven:

- "We use AI."
- "We have data."
- "We have a better UI."
- "We are first."
- "We will ship faster."
- "Customers will not switch because migration is annoying."
- "We have many features."
- "We will build a community later."
- "Competitors are old."

Push every moat claim toward a measurable structural barrier.

## Reference Routing

Load only what is needed:

- `references/moat-framework.md`: moat theory, SaaS translation, moat types, false moats, and how to turn moat claims into product functions.
- `references/profitability-model.md`: SaaS metrics and business-model checks for NRR, GRR, CAC payback, gross margin, Rule of 40/Rule of X, pricing power, cost-to-serve, and margin protection.
- `references/product-function-patterns.md`: practical SaaS product patterns that create moat through workflow depth, data loops, integrations, collaboration, compliance, marketplace, reseller, white-label, and AI workflows.
- `references/review-scorecard.md`: structured review template, scoring rubric, red flags, questions, and implementation outputs.
- `references/research-sources.md`: source map and research takeaways used to shape this skill.

If used with `saas-kit`, let `saas-kit` drive spec approval and use this skill to add moat/profitability requirements to Goal, Scope, Requirements, Backend, Database, APIs, UI/UX, Security, Testing, and Implementation Steps.

If used with `saas-product-growth`, use that skill for full SaaS component/growth coverage and this skill for defensibility, profit protection, and moat proof.

## Output Shapes

For a SaaS idea:

- Moat thesis.
- Customer value created.
- Business profit protected.
- Product functions that create the moat.
- Proof metrics.
- Competitor attack paths.
- Weak assumptions.
- MVP moat path.
- Production moat path.
- Scale moat path.

For an existing SaaS app:

- Real moats found.
- Claimed moats that are only features.
- Missing product functions needed to create defensibility.
- Profitability risks.
- Metrics to instrument.
- Prioritized build plan.

For implementation after approval:

- Build the smallest product function that strengthens a measurable moat.
- Avoid overbuilding enterprise friction unless it protects real revenue, retention, trust, or margin.
