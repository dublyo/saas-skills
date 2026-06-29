# Design And Validation

Load this for UI quality, product fit, and final verification expectations.

## Design Standard

Design for the actual product surface:

- Operational SaaS: dense, quiet, structured, fast to scan.
- Landing page: strong product signal in the first viewport, clear offer, credible proof, strong mobile layout.
- Dashboard: filters, comparison, table density, empty states, errors, and repeated actions.
- Editor/tool: persistent controls, clear state, undo/redo or recovery where relevant, keyboard flow.
- Content site: hierarchy, reading rhythm, navigation, search, related content, and accessible typography.

Avoid default-looking placeholder UI. Avoid decorative visual systems that fight the task. Do not create a marketing landing page when the user asked for an app or tool.

## Required States

Consider these before finishing UI work:

- Loading.
- Empty.
- Error.
- Success.
- Disabled.
- Long text.
- Small viewport.
- Large viewport.
- Keyboard-only.
- Reduced motion.
- Slow network.
- Partial data.

## Browser QA

For meaningful UI work, open the app in a browser when possible and check:

- Primary flow works.
- No obvious console errors.
- Desktop and mobile layouts do not overlap or overflow.
- Text fits buttons, tabs, cards, sidebars, and tables.
- Focus is visible and follows the workflow.
- Interactive controls have clear labels and states.
- Images/media render and have stable dimensions.
- Important content is not hidden under sticky headers or overlays.

## Reporting

End with:

- Changed files.
- Validation commands and results.
- Browser checks performed.
- Accessibility/performance/security checks performed.
- Remaining risks or checks not run.
