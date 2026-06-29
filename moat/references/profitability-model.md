# Profitability Model

Use this reference to connect moat design to SaaS business health and profitability.

## Table Of Contents

- Profit Protection Thesis
- Metrics To Gather
- Retention And Expansion
- CAC And Distribution
- Gross Margin And Cost-To-Serve
- Pricing Power
- Rule Of 40 And Rule Of X
- Moat-To-Metric Map
- Unit Economics Stress Tests
- Output Template

## Profit Protection Thesis

Every moat claim should explain how the SaaS makes or keeps more money.

Good moat thesis:

```text
Because the product owns [critical workflow/data/channel],
customers get [measurable value],
competitors face [hard barrier],
and the business protects [retention/pricing/margin/CAC/expansion].
```

Weak moat thesis:

```text
We have better features and AI.
```

## Metrics To Gather

Request or infer:

- ICP and buyer.
- ACV or ARPA.
- Pricing model.
- Gross margin.
- Cost-to-serve.
- CAC by channel.
- CAC payback.
- GRR.
- NRR.
- Churn by segment.
- Expansion by account age.
- Activation rate.
- Time to value.
- Usage frequency.
- Seat expansion.
- Integration adoption.
- Support tickets per account.
- Infrastructure, AI, storage, email, SMS, scraping, and API costs.

If metrics are missing, specify instrumentation needed before claiming the moat works.

## Retention And Expansion

Retention is the strongest SaaS moat proof.

GRR signals:

- Are customers staying before expansion?
- Does the product solve a recurring problem?
- Is churn concentrated in a weak segment?

NRR signals:

- Do customers buy more seats, usage, projects, modules, data, reports, API calls, or white-label capability?
- Does value grow with use?
- Does account age increase revenue?

Moat interpretation:

- High GRR with low NRR: sticky but may lack expansion.
- Low GRR with high new sales: acquisition masking weak product value.
- High NRR: strong signal of workflow, usage, or seat expansion moat.
- Falling NRR: moat may be weakening, pricing may be wrong, or expansion path may be saturated.

Product requirements:

- Track activation.
- Track account age.
- Track seats/users.
- Track expansion events.
- Track feature and integration adoption.
- Track churn reasons.
- Track downgrade reasons.

## CAC And Distribution

A distribution moat lowers CAC or improves payback.

Potential distribution moats:

- SEO/GEO content.
- Free tools.
- Product virality.
- Referrals.
- Affiliate channel.
- Marketplace listing.
- Agency/reseller channel.
- Integration partnerships.
- Founder-led trust.
- Community.
- Templates.
- Public reports.

Signals:

- Organic share of leads increases.
- CAC payback shortens.
- Referral conversion rate is high.
- Partner-sourced customers retain.
- Marketplace customers activate faster.
- Free-tool users convert to paid.

False moat:

- Paid ads work only when pricing is undercounting cost or churn.

## Gross Margin And Cost-To-Serve

A SaaS moat must survive costs.

Cost drivers:

- AI tokens.
- Model inference.
- Scraping.
- Storage.
- Bandwidth.
- Email/SMS.
- External APIs.
- Support.
- Onboarding.
- Implementation services.
- Compliance/security operations.
- Human review.

Margin protection functions:

- Usage metering.
- Quotas.
- Entitlements.
- Cost dashboards.
- Per-plan limits.
- Abuse detection.
- Model routing.
- Caching.
- Batch processing.
- Self-serve onboarding.
- Help center and support automation.
- Customer health scoring.

Moat test:

```text
Can the product deliver more customer value over time without cost rising faster than revenue?
```

## Pricing Power

Pricing power is a strong moat outcome.

Evidence:

- Customers renew after price increases.
- Price is tied to a value metric.
- Higher plans map to real operational value.
- Expansion happens naturally through seats, usage, volume, clients, storage, credits, API, compliance, or white-label.
- Competitors undercut price but customers stay.

Product requirements:

- Entitlement model.
- Usage records.
- Plan limits.
- Value metric tracking.
- Upgrade prompts tied to reached value.
- Billing lifecycle.
- Downgrade behavior.

Avoid:

- Unlimited usage for high-cost features.
- Pricing based only on internal cost instead of customer value.
- Enterprise features on cheap self-serve plans.
- Manual plan overrides without audit trail.

## Rule Of 40 And Rule Of X

Use these as business-health lenses, not absolute laws.

Rule of 40:

```text
Revenue growth rate + profit/free-cash-flow/EBITDA margin
```

Common interpretation: at scale, a healthy SaaS should balance growth and profitability around 40 or better.

Rule of X:

```text
(Growth rate * multiplier) + free cash flow margin
```

Bessemer's Rule of X emphasizes that efficient growth can compound value more than the same number of margin points. Use this lens when the company is still scaling and growth quality is strong.

Moat interpretation:

- A moat should improve the quality of growth, not only growth rate.
- High growth with poor retention is weak.
- High margin with no growth may be a niche service, not a scalable SaaS moat.
- Efficient growth with improving retention, expansion, and payback is stronger evidence.

## Moat-To-Metric Map

| Moat type | Product behavior | Profit metric |
| --- | --- | --- |
| Switching costs | Customer adds data, workflows, integrations, users, approvals | GRR, churn, renewal rate, contract length |
| Workflow/system of record | Product used daily/weekly to run core process | Retention, expansion, seat growth |
| Network effects | More users/partners/customers increase value | Organic growth, activation, engagement, CAC |
| Data advantage | Usage improves output quality or benchmarks | Conversion, retention, pricing power |
| Integration depth | Customer connects critical tools | Retention, ACV, enterprise close rate |
| Distribution | Channel compounds cheaper than paid ads | CAC, CAC payback, lead quality |
| Trust/compliance | Buyer risk is lower | ACV, win rate, sales cycle, churn |
| Cost advantage | Product delivers value cheaper at scale | Gross margin, contribution margin |
| White-label/reseller | Partners distribute and embed product | CAC, payback, partner retention, ARPA |

## Unit Economics Stress Tests

Ask:

- If support cost doubles, does the business remain profitable?
- If AI or infrastructure cost doubles, which plan becomes unprofitable?
- If paid CAC rises 50%, which channel protects growth?
- If churn rises by 3 points, which moat is failing?
- If a competitor drops price by 30%, why do customers stay?
- If a customer doubles usage, do margins improve or collapse?
- If a large customer asks for enterprise features, is ACV high enough to justify them?

## Output Template

```text
Profit engine:
- Pricing model:
- Main value metric:
- Main cost drivers:
- Retention mechanism:
- Expansion mechanism:
- Distribution mechanism:

Moat-profit link:
- Moat candidate:
- Customer value:
- Competitor barrier:
- Metric protected:
- Product functions required:

Risks:
- Gross margin risk:
- CAC risk:
- Churn risk:
- Pricing risk:

Instrumentation:
- Must track now:
- Should track before paid launch:
- Track later:
```
