# Website QA Report Template

Use this structure for substantial Playwright website tests. Keep the report concise but evidence-based.

## Summary

- Target:
- Mode: Playwright plugin, fresh browser context
- Auth state: unauthenticated / logged in by user / blocked by login / blocked by CAPTCHA or 2FA
- Desktop viewport:
- Mobile viewport:
- Routes/flows tested:

## Findings

### Critical

Use only for blockers: blank page, primary flow broken, auth/security symptom, data loss, unrecoverable crash.

```text
[Critical] Title
Route:
Viewport:
Evidence:
Steps:
Likely area:
Suggested fix:
```

### High

Use for broken routes, failed forms, major layout breakage, important first-party 4xx/5xx/API failures.

### Medium

Use for non-blocking runtime errors, responsive issues, accessibility gaps, degraded UX, flaky interactions.

### Low

Use for minor warnings, third-party noise, cosmetic issues, polish items.

## Console Summary

- Errors:
- Warnings:
- Notes:

## Network Summary

- Failed first-party requests:
- Failed third-party requests:
- CORS/mixed-content/auth redirect symptoms:
- Requests inspected in detail:

## Responsive And UI Notes

- Desktop:
- Mobile:
- Overflow/overlap/clipping:
- Forms/buttons/navigation:
- Loading/empty/error states:

## Accessibility Heuristic Notes

- Headings/landmarks:
- Button/link names:
- Form labels:
- Keyboard/focus concerns inferred from snapshot:

## Limitations

List anything not tested: login blocked, CAPTCHA/2FA, no account, no test data, plugin limitation, local server unavailable, route out of scope, Lighthouse skipped by design.

## Recommended Next Step

Give the smallest useful next step: fix a blocker, run authenticated pass, add automated Playwright tests, inspect code for failing route, or run a deeper accessibility/performance audit.
