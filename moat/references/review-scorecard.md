# Review Scorecard

Use this reference to review a SaaS idea, spec, or codebase for moat quality.

## Table Of Contents

- Review Inputs
- Fast Moat Triage
- Scorecard
- Questions To Ask
- Red Flags
- Output Template
- Implementation Plan Template
- Test Cases

## Review Inputs

Ask for or infer:

- SaaS idea.
- Target customer.
- Buyer and user.
- Core recurring workflow.
- Current product functions.
- Pricing model.
- Acquisition channel.
- Main cost drivers.
- Current metrics if available.
- Competitors and substitutes.
- Stage: idea, MVP, production, scale, enterprise.

## Fast Moat Triage

Use this quick classification:

```text
No moat:
- Feature can be copied quickly.
- No workflow ownership.
- No retention/expansion logic.
- No channel advantage.
- No cost or pricing protection.

Weak moat:
- Useful product but moat depends on execution speed, UI, generic AI, or basic data.
- Some switching cost, but mostly inconvenience.

Emerging moat:
- Product owns recurring workflow, has clear expansion path, collects useful proprietary data, or has repeatable distribution.

Strong moat:
- Product becomes system of record or workflow infrastructure, compounds data/network/distribution, protects margins, and shows retention/expansion proof.
```

## Scorecard

Score each from 0 to 5.

| Area | 0 | 3 | 5 |
| --- | --- | --- | --- |
| Customer value | Nice-to-have | Clear efficiency/value | Critical recurring outcome |
| Barrier | Easy copy | Some migration/process friction | Structural workflow/data/network/channel barrier |
| Profit impact | No link | Indirect link | Clear retention, expansion, CAC, margin, or pricing power |
| Compounding | Static feature | Gets stickier with setup | Gets stronger with usage, data, users, partners, or scale |
| Workflow depth | Single task | Multi-step process | System of record or operating layer |
| Switching cost | None | Data/process migration | History, integrations, training, compliance, team process |
| Data advantage | Generic | Some proprietary data | Fresh, permissioned, outcome-improving data loop |
| Distribution | Paid/founder only | Some organic/partner path | Repeatable low-CAC channel or embedded virality |
| Cost control | Unknown | Basic usage limits | Strong margin instrumentation and controls |
| Defensibility proof | Assumptions | Early behavior | Metrics prove retention, expansion, or lower CAC |

Interpretation:

- 0-15: no real moat yet.
- 16-30: useful product, weak defensibility.
- 31-40: emerging moat, build proof.
- 41-50: strong moat candidate.

Do not average away a fatal flaw. A product with no customer value or no profit link should not be called strong even if some categories score well.

## Questions To Ask

Customer value:

- What recurring pain does this own?
- What does the customer stop doing manually?
- What business outcome improves?

Barrier:

- What gets harder to replace after 30, 90, and 365 days?
- What would a competitor need besides code?
- Which data, process, integrations, or relationships compound?

Profit:

- Why can this charge more over time?
- Why will churn fall with usage?
- Where does expansion revenue come from?
- What lowers CAC?
- What protects gross margin?

Product:

- Which function creates the moat?
- Which database entity stores the compounding asset?
- Which workflow creates switching cost?
- Which event proves activation?
- Which integration makes the product operationally embedded?

AI:

- What proprietary context does AI use?
- What feedback improves outputs?
- What action does AI complete?
- What controls make customers trust it?
- What prevents a generic AI tool from replacing it?

## Red Flags

High-risk claims:

- "Our moat is AI."
- "Our moat is data" without outcome improvement.
- "Our moat is better UI."
- "Our moat is all-in-one" without workflow ownership.
- "Our moat is cheaper price."
- "Our moat is first mover."
- "Our moat is we know the niche" without distribution or workflow proof.
- "Our moat is integrations" but no integration is critical.
- "Our moat is community" before a community exists.
- "Our moat is enterprise" before enterprise controls or buyers.

Profit red flags:

- Unlimited usage on costly AI/scraping/storage/API features.
- No usage metering.
- No churn reason tracking.
- No expansion path.
- Paid acquisition before activation is measured.
- High-support onboarding for low ACV.
- Manual services hidden inside "SaaS."
- Heavy reseller discounts without usage limits.

## Output Template

```text
Moat review:
- Stage:
- Current moat strength:
- Main moat thesis:
- Strongest structural barrier:
- Weakest assumption:

Customer value:
- Core recurring workflow:
- Business outcome:
- Buyer reason to pay:

Profit protection:
- Retention mechanism:
- Expansion mechanism:
- Pricing power:
- CAC/distribution advantage:
- Gross margin protection:

Product functions required:
- Must build now:
- Should build before paid launch:
- Later/scale:

Competitor attack:
- Fast-copy risk:
- Platform risk:
- AI-copy risk:
- Low-price risk:

Metrics:
- Activation:
- Retention:
- Expansion:
- CAC/payback:
- Margin/cost:

Verdict:
- No moat / weak moat / emerging moat / strong moat candidate
- Why:
```

## Implementation Plan Template

```text
1. Instrument the moat:
   - Events:
   - Entities:
   - Metrics:

2. Build the first structural barrier:
   - Workflow:
   - Data:
   - Integration:
   - Permission:

3. Protect the profit engine:
   - Entitlements:
   - Usage limits:
   - Cost tracking:
   - Pricing trigger:

4. Add proof loop:
   - Activation proof:
   - Retention proof:
   - Expansion proof:
   - Distribution proof:

5. Test competitor attack:
   - Copycat:
   - Low-price:
   - Platform:
   - AI generic tool:
```

## Test Cases

Add tests based on the moat claim:

- Tenant/user cannot access another tenant's moat data.
- Export includes customer-owned data without leaking internal scoring or other tenants.
- Usage limit prevents negative-margin overuse.
- Plan entitlement blocks premium moat features server-side.
- Shared report exposes only approved fields.
- Integration sync failure is logged and recoverable.
- Audit history survives edits.
- AI output stores human feedback and approval state.
- Referral/affiliate attribution cannot be trivially forged.
- White-label client cannot see platform owner internals.
- Data deletion removes personal data without corrupting aggregate permitted analytics.
