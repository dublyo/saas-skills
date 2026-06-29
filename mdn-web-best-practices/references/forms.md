# Forms Reference

Load this for inputs, labels, validation, autocomplete, mobile keyboards, file uploads, search/filter forms, auth forms, and checkout/contact flows.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/elements/form/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/elements/input/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/elements/label/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/api/validitystate/`

## Rules

- Use native labels connected to controls.
- Choose input types for meaning and mobile keyboard fit, not only for validation.
- Use `autocomplete`, `inputmode`, `required`, `min`, `max`, `pattern`, and validation attributes intentionally.
- Keep server validation authoritative and client validation helpful.
- Put errors near fields, make them specific, and expose them to assistive technology.
- Preserve entered values after validation errors.
- Use fieldsets and legends for grouped choices.
- Avoid placeholder-only instructions.
- Design loading, disabled, success, error, and retry states.
- Treat file upload previews, MIME checks, size limits, progress, and cancel states as first-class behavior.

## Audit Triggers

- Missing labels.
- Generic "Invalid input" errors.
- Client-only validation for security or business rules.
- Password, OTP, phone, address, payment, and file fields without autofill/mobile behavior considered.
- Submit buttons that do not communicate progress or duplicate submission behavior.
