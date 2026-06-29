---
name: mdn-web-best-practices
description: Build, improve, or audit web apps using MDN Web Docs as the standards baseline. Use for frontend and web design/code tasks including new app or landing page creation, redesigns, refactors, code review, accessibility audits, responsive QA, performance checks, security reviews, forms, browser APIs, semantic HTML, CSS, JavaScript, and validation of existing web projects across any framework.
---

# MDN Web Best Practices

## Operating Model

Use a spec-first workflow for web work unless the user already provided a precise implementation request. Default to:

1. Clarify the target user, page/app type, core flow, framework, and validation bar.
2. Inspect the current repo before choosing patterns or adding dependencies.
3. Route to the smallest relevant reference files below.
4. Use the local MDN checkout as the standards source of truth.
5. Design context-aware UI, then implement against MDN-backed web platform rules.
6. Validate build/tests, browser behavior, responsiveness, accessibility, console, performance, and security before finishing substantial work.

For audit-only requests, skip implementation unless the user asks for fixes. Lead with findings, file/line references, risk, and evidence.

## Source Of Truth

Primary MDN source:

`/Users/dribrahimm/skills/mozilla/content/files/en-us/web`

Fallback source:

`https://github.com/mdn/content/tree/main/files/en-us/web`

Use the local source first. Use the GitHub fallback only when the local path is missing or the needed MDN topic is not present locally. When browser behavior, API support, accessibility semantics, or security requirements are uncertain, search MDN instead of relying on memory.

## Reference Routing

Read only the references needed for the task:

- `references/mdn-routing.md` - local MDN search rules, topic map, and fallback behavior.
- `references/html.md` - semantic HTML, document structure, media, interactive elements.
- `references/css.md` - layout, responsive CSS, media queries, container queries, motion.
- `references/javascript.md` - DOM, events, fetch, storage, browser APIs, progressive enhancement.
- `references/accessibility.md` - keyboard, focus, labels, ARIA restraint, reduced motion.
- `references/forms.md` - native forms, validation, errors, uploads, autofill, mobile inputs.
- `references/performance.md` - rendering, loading, images, fonts, animations, Core Web Vitals.
- `references/security.md` - XSS, CSP, cookies, CORS, storage, permissions, embeds.
- `references/design-validation.md` - design quality bar and final QA expectations.

Use `scripts/search_mdn.py` for focused local MDN lookup. Use `scripts/web_audit_checklist.py` to generate a task-specific checklist before deep audits or larger builds.

## Framework Behavior

Adapt to the current project instead of forcing a stack. Support plain HTML/CSS/JS and any framework already present, including Next.js, Nuxt, Astro, React, Vue, Svelte, Rails, Phoenix, or static site generators.

Prefer established repo conventions for routing, components, styling, state, tests, and build tools. Add dependencies only when they solve a real problem and fit the existing project.

## Design Standard

Choose the visual language from the product context:

- SaaS/product tools: quiet, dense, efficient, scan-friendly, low decoration.
- Landing pages: strong first viewport, clear offer, real product or domain visuals, conversion-oriented structure.
- Dashboards: comparison, filters, tables, states, and repeated workflows over decorative cards.
- Developer tools: clarity, keyboard flow, logs, errors, and compact controls.
- Consumer/mobile-responsive pages: fast comprehension, comfortable touch targets, resilient layout.

Do not let visual polish weaken semantics, keyboard access, contrast, layout stability, or performance.

## Build Workflow

1. Inspect package files, routes, app structure, styling system, test scripts, and existing UI conventions.
2. Create or confirm a short spec covering user flow, states, data, edge cases, and validation.
3. Search local MDN for platform-specific behavior before using browser APIs, complex CSS, advanced forms, media, storage, workers, permissions, or security-sensitive features.
4. Implement with semantic HTML first, CSS that responds to content and viewport, and JavaScript that preserves progressive behavior where practical.
5. Add or update focused tests when project tooling exists.
6. Run available build/test/lint commands.
7. Run browser QA for meaningful UI changes.
8. Report what changed, what was validated, and any remaining risk.

## Audit Workflow

1. Identify the app type, user-critical flows, target browsers if available, and current framework.
2. Inspect source and rendered behavior when possible.
3. Generate an audit checklist with `scripts/web_audit_checklist.py`.
4. Search MDN for any uncertain standards issue.
5. Prioritize findings by user impact and regression risk.
6. Include file/line references for code issues and screenshots or browser evidence for UI issues when available.
7. Separate confirmed bugs from improvements and questions.

## Validation Contract

For substantial web changes, try to complete all applicable checks:

- Install/build/test/lint using repo scripts.
- Browser smoke test for the primary flow.
- Desktop and mobile responsive checks.
- Console error check.
- Keyboard navigation and focus visibility check.
- Accessible name, label, landmark, heading, and contrast review.
- Loading, empty, error, overflow, and long-content states.
- Basic performance review for images, fonts, script weight, animation, and layout shift.
- Security review for user HTML, forms, uploads, storage, cookies, third-party scripts, iframes, and auth/session assumptions.

If a check cannot run, state why and give the next best manual check.

## Helper Scripts

Paths below use `${CLAUDE_SKILL_DIR}` (this skill's own directory). If that variable is not set in the environment, substitute the absolute path to this skill's `scripts/` folder.

Search MDN locally:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/search_mdn.py" "dialog element"
```

Create a checklist:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/web_audit_checklist.py" --mode full --surface app --framework next
```

Keep script output as guidance. Read the referenced MDN files before making a standards-sensitive claim.
