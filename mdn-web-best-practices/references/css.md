# CSS Reference

Load this for layout, responsive design, typography, spacing, color, animation, media queries, container queries, and browser rendering behavior.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/css/reference/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/css/guides/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/css/how_to/`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/performance/guides/animation_performance_and_frame_rate/index.md`

## Rules

- Let layout respond to content. Prefer flexible grid/flex tracks, intrinsic sizing, min/max constraints, and aspect ratios over fixed viewport-tied sizes.
- Avoid horizontal overflow on mobile. Test long labels, narrow screens, large text, and mixed content lengths.
- Use media queries for viewport conditions and container queries when a component must adapt to its own available space.
- Keep focus styles visible. Do not remove outlines unless replacing them with an equally clear state.
- Respect `prefers-reduced-motion` for animation, parallax, auto-scrolling, and transitions.
- Use color with contrast and state redundancy. Do not communicate state by color alone.
- Avoid layout shifts from late-loading images, fonts, dynamic labels, hover states, badges, and error messages.
- Prefer transform and opacity for cheap animations. Avoid animating layout-heavy properties unless necessary.
- Keep CSS naming, utility usage, and design tokens consistent with the repo.

## Audit Triggers

- Viewport-width font scaling.
- Negative letter spacing in UI text.
- Fixed heights around dynamic text.
- Cards nested in cards or page sections styled as floating cards without purpose.
- Motion without reduced-motion fallback.
- Images without stable dimensions or aspect ratio.
- CSS that hides focus or creates pointer-only interactions.
