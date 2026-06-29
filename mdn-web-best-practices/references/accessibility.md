# Accessibility Reference

Load this for keyboard navigation, focus, accessible names, landmarks, forms, color contrast, reduced motion, ARIA, and WCAG-oriented checks.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/accessibility/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/accessibility/guides/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/accessibility/guides/understanding_wcag/`

## Rules

- Use semantic HTML first. Add ARIA only when native semantics cannot express the UI.
- Every interactive control needs an accessible name, visible focus, and keyboard operation.
- Maintain logical tab order that follows the visual and task flow.
- Do not trap focus except in real modal contexts, and always provide a way out.
- Label forms clearly and connect errors to fields.
- Provide non-color cues for status, validation, charts, badges, and destructive states.
- Respect reduced motion and avoid flashing or seizure-risk patterns.
- Keep touch targets comfortable and separated on mobile.
- Test empty, loading, error, disabled, and success states with accessibility in mind.

## Audit Triggers

- Click-only controls.
- Icon-only buttons without names.
- Custom selects, menus, tabs, dialogs, tooltips, sliders, comboboxes, and drag/drop.
- Toasts or async updates that screen reader users may miss.
- Placeholder-only labels.
- Focus hidden by sticky headers, overlays, or scroll containers.
