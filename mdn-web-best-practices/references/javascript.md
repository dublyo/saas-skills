# JavaScript And Browser APIs

Load this for DOM behavior, events, fetch, storage, history, workers, permissions, clipboard, files, media, and other browser APIs.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/javascript/reference/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/api/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/http/`

## Rules

- Prefer minimal JavaScript when HTML and CSS can solve the behavior reliably.
- Preserve keyboard and assistive technology behavior when enhancing native controls.
- Check MDN for secure-context requirements, permission prompts, user activation requirements, browser support, and worker availability before using browser APIs.
- Use event delegation carefully and keep event targets accessible.
- Abort or clean up long-running fetches, timers, observers, subscriptions, and event listeners where component lifecycles matter.
- Handle loading, empty, error, timeout, offline, and retry states for network flows.
- Treat localStorage/sessionStorage as convenience storage, not a secure store.
- Avoid direct HTML injection. If unavoidable, sanitize with a trusted project-approved path.
- Keep SSR/client boundaries explicit in frameworks that hydrate.

## API Lookup Triggers

Search MDN before using:

- Clipboard, File, FileReader, Streams, WebSocket, EventSource, Web Workers, Service Workers.
- Geolocation, Notifications, Permissions, MediaDevices, Web Share, Payment Request.
- History, URL, URLSearchParams, Web Storage, IndexedDB, Cache, Crypto.
- Drag and drop, pointer/touch events, IntersectionObserver, ResizeObserver.
