# MDN Routing

Use this file first when a task needs MDN-backed standards guidance.

## Local Source

Primary root:

`/Users/dribrahimm/skills/mozilla/content/files/en-us/web`

Fallback:

`https://github.com/mdn/content/tree/main/files/en-us/web`

Use local files first. Use the fallback only if the local tree is missing, incomplete, or the requested topic cannot be found locally.

## Topic Map

- HTML: `html/`, especially `html/reference/`, `html/reference/elements/`, `html/reference/global_attributes/`, `html/guides/`.
- CSS: `css/`, especially `css/reference/`, `css/guides/`, `css/how_to/`.
- JavaScript: `javascript/`, especially `javascript/reference/`, `javascript/guide/`.
- Accessibility: `accessibility/`, especially `accessibility/guides/` and `accessibility/guides/understanding_wcag/`.
- Performance: `performance/`, especially `performance/guides/`.
- Security: `security/`, especially `security/attacks/`, `security/defenses/`, `security/practical_implementation_guides/`, `security/authentication/`.
- Privacy: `privacy/`, especially `privacy/guides/`.
- HTTP: `http/`, especially `http/guides/` and `http/reference/`.
- Browser APIs: `api/`, named by API or interface, for example `api/fetch_api/`, `api/web_storage_api/`, `api/clipboard_api/`, `api/service_worker_api/`.
- Progressive web apps: `progressive_web_apps/`.
- Media: `media/`.
- SVG: `svg/`.

## Search Commands

Prefer `rg` over broad file browsing:

```bash
rg -n "query terms" /Users/dribrahimm/skills/mozilla/content/files/en-us/web
```

Find likely topic files:

```bash
rg --files /Users/dribrahimm/skills/mozilla/content/files/en-us/web | rg "html/reference/elements/dialog|api/fetch|css/reference/properties/grid"
```

Use the bundled script for ranked Markdown results:

```bash
python3 /Users/dribrahimm/.agents/skills/mdn-web-best-practices/scripts/search_mdn.py "form validation"
```

## Reading Rule

When a topic is standards-sensitive, read the specific MDN page before deciding. This applies especially to:

- Browser API permissions, secure-context requirements, and compatibility notes.
- HTML element semantics and implicit roles.
- Form behavior, validation, input types, and autofill attributes.
- CSS layout algorithms, containment, media queries, container queries, and motion.
- Storage, cookies, CORS, CSP, fetch credentials, iframes, and third-party scripts.
- Accessibility requirements for keyboard, focus, labels, names, color, and reduced motion.

Do not paste large MDN excerpts into the answer. Summarize the rule and cite the local path or web URL when useful.
