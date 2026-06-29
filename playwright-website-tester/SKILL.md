---
name: playwright-website-tester
description: Test websites and local web apps with the Playwright plugin in a fresh browser context, separate from the user's Chrome profile. Use for full website QA, mobile and desktop checks, route crawling, login-from-scratch testing, console and network error monitoring, screenshots, accessibility snapshots, forms/buttons/navigation checks, responsive layout review, and browser-visible error reports. Do not use the Chrome extension connector for this workflow.
---

# Playwright Website Tester

## Operating Rule

Use the Playwright plugin, not the Chrome extension connector. Treat the browser context as fresh and separate from the user's existing Chrome profile. If a site requires authentication, tell the user they may need to log in from scratch inside the Playwright-controlled browser; never ask them to paste passwords or 2FA codes into chat.

Skip Lighthouse by default. Focus on Playwright-observable evidence: page behavior, console messages, failed network requests, accessibility snapshots, screenshots, desktop/mobile layout, and user-flow results.

## Required References

Read `references/report-template.md` before producing a substantial QA report.

Use `scripts/website_qa_checklist.py` when planning deep or repeated QA. The path uses `${CLAUDE_SKILL_DIR}` (this skill's own directory); if that variable is not set, substitute the absolute path to this skill's `scripts/` folder.

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/website_qa_checklist.py" --depth deep --auth unknown
```

## Playwright Plugin Surface

Use these Playwright plugin tools when available.

Observation and setup:

- `browser_tabs` - create/select/close/list tabs. Use a new tab for fresh checks.
- `browser_navigate` / `browser_navigate_back` - move to the target URL and between routes.
- `browser_resize` - switch desktop and mobile viewport sizes.
- `browser_snapshot` - inspect accessible structure and interactive elements.
- `browser_take_screenshot` - capture visual evidence for findings and the report.
- `browser_console_messages` - collect console errors/warnings.
- `browser_network_requests` - list browser-visible requests and failures.
- `browser_network_request` - inspect a specific request when needed.
- `browser_wait_for` - wait for text/state to settle before re-checking console and network.

Interaction (to exercise real flows):

- `browser_click` - activate links, buttons, and controls.
- `browser_type` / `browser_fill_form` - enter text and complete forms.
- `browser_select_option` - choose values in dropdowns/selects.
- `browser_press_key` - keyboard input and focus/keyboard-navigation checks.
- `browser_hover` - reveal hover menus and tooltips.
- `browser_handle_dialog` - accept or dismiss native dialogs and confirms.

If a needed Playwright action is not exposed by the plugin, state the limitation and use the closest observable evidence. Do not pretend Lighthouse, HAR export, video recording, storage-state persistence, or tracing ran unless it actually did.

## Default Deep QA Workflow

1. Identify target URL. If missing, ask for it. If it is local, check whether a dev server is running or ask the user to start it.
2. Open a fresh Playwright tab/context through the plugin.
3. Navigate to the target URL.
4. Capture baseline state:
   - page loaded or failed
   - console errors and warnings
   - failed network requests
   - accessibility snapshot
   - obvious visual/layout issues
5. Test desktop viewport, default `1440x900`.
6. Test mobile viewport, default `390x844`.
7. Crawl obvious routes from nav links and primary CTAs. Keep scope practical; do not brute-force unrelated external links.
8. Exercise key interactions:
   - navigation
   - forms
   - buttons
   - modals/dropdowns
   - search/filter/sort controls
   - auth redirects or protected routes
9. For auth-required flows, pause and let the user type credentials directly into the Playwright browser. Do not capture secrets in screenshots or reports.
10. Re-check console and network after each key route or flow.
11. Record findings with severity, evidence, reproduction steps, and affected viewport.

## Viewports

Default viewports:

- Desktop: `1440x900`
- Mobile: `390x844`

Use other sizes when the product requires them:

- Small mobile: `360x740`
- Tablet: `768x1024`
- Wide desktop: `1920x1080`

Always report which viewport exposed an issue.

## Console And Network Policy

Treat these as findings:

- uncaught exceptions
- hydration/runtime errors
- failed fetch/XHR requests
- 4xx/5xx requests for first-party app resources or APIs
- CORS errors
- mixed-content errors
- blocked scripts that break required behavior
- infinite loading states caused by failed requests

Do not over-report expected analytics/ad-block/third-party noise unless it breaks the user flow. Mention it separately as third-party noise when useful.

## Accessibility Heuristics

Use `browser_snapshot` for accessible structure. Check:

- page has meaningful headings and landmarks
- buttons and links have accessible names
- forms expose labels or clear names
- modals/dropdowns are visible in the accessibility tree when open
- focusable controls are discoverable
- important text is not hidden behind visual-only UI

This is not a full WCAG audit. Call it an accessibility heuristic pass unless deeper tooling is actually used.

## Report Style

Lead with findings, ordered by severity:

- Critical: blocks primary flow, data loss, auth/security symptom, blank page.
- High: broken route, broken form, major layout break, important API failure.
- Medium: non-blocking runtime error, responsive issue, accessibility gap, degraded UX.
- Low: minor warning, cosmetic issue, third-party noise, polish item.

For each finding include:

- severity
- title
- affected URL/route
- viewport
- evidence
- reproduction steps
- likely area, if inferable
- suggested fix direction

If no major issues are found, say that clearly and list what was tested plus any gaps.

## Security And Privacy

- Do not ask for passwords, OTPs, session cookies, or tokens in chat.
- Let the user type credentials directly into the Playwright browser when needed.
- Avoid screenshots that expose secrets, personal data, private account data, or tokens.
- Report visible security symptoms such as mixed content, tokens in URLs, unsafe redirects, CORS failures, auth loops, and exposed stack traces.

## Final Response

End with:

- target URL
- tested viewports/routes/flows
- findings by severity
- console/network summary
- screenshots or snapshots captured, if any
- limitations and checks not run
- recommended next step
