# HTML Reference

Load this for document structure, semantic elements, media, links, buttons, dialogs, tables, landmarks, metadata, and component markup.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/elements/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/reference/global_attributes/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/html/guides/`

## Rules

- Start with native semantics. Use the correct element before adding roles, div wrappers, or custom handlers.
- Use one clear page-level heading structure. Do not choose heading levels for visual size.
- Prefer real buttons for actions and real links for navigation.
- Keep interactive elements keyboard reachable and avoid nesting interactive controls.
- Use lists, tables, figures, captions, sections, nav, main, aside, header, and footer where they communicate structure.
- Provide meaningful alternative text for informative images and empty alt text for decorative images.
- Use native dialog, details, summary, progress, meter, time, output, and form controls when they fit.
- Preserve valid nesting and document outline when composing framework components.
- Use global attributes intentionally. Check MDN before relying on `tabindex`, `inert`, `hidden`, `popover`, `contenteditable`, `autofocus`, or `draggable`.

## Audit Triggers

- Divs with click handlers.
- Buttons implemented as links or links implemented as buttons.
- Missing labels, headings, landmarks, alt text, captions, or table headers.
- `tabindex` values greater than 0.
- Modal, menu, tooltip, tab, combobox, or disclosure behavior built without native semantics or tested ARIA patterns.
