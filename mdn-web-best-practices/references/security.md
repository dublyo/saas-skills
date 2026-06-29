# Security Reference

Load this for user-generated content, HTML injection, forms, auth/session UI, cookies, storage, CORS, CSP, iframes, permissions, uploads, and third-party scripts.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/security/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/security/attacks/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/security/defenses/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/security/practical_implementation_guides/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/http/`

## Rules

- Treat any user-controlled HTML, Markdown, rich text, URL, file, or embedded content as risky.
- Avoid raw HTML injection. If project requirements demand it, use a sanitizer and document the trust boundary.
- Do not store secrets, tokens, or sensitive personal data in browser storage.
- Check cookie attributes and same-site behavior for auth/session flows.
- Do not assume CORS is an auth or security boundary.
- Be careful with `target="_blank"` and external links.
- Review iframe sandboxing, third-party embeds, analytics, chat widgets, and payment scripts.
- Use CSP/security headers where the deployment surface supports them.
- Keep file upload checks on the server. Client checks are UX only.
- Search MDN before using permission-gated APIs or APIs requiring secure contexts.

## Audit Triggers

- `dangerouslySetInnerHTML`, `innerHTML`, raw Markdown rendering, rich text editors.
- Tokens in localStorage/sessionStorage.
- Unsandboxed iframes.
- Broad CORS assumptions.
- Client-only file validation.
- External scripts without clear purpose or loading strategy.
