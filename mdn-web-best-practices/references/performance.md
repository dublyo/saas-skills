# Performance Reference

Load this for page speed, rendering, image delivery, fonts, JavaScript weight, animation, layout shift, startup, and perceived responsiveness.

Primary MDN paths:

- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/performance/index.md`
- `/Users/dribrahimm/skills/mozilla/content/files/en-us/web/performance/guides/`

## Rules

- Optimize the critical path for the user's first meaningful task.
- Avoid render-blocking work where possible.
- Give images dimensions or aspect ratios and serve reasonable sizes.
- Lazy-load non-critical media without delaying important content.
- Keep font loading deliberate and avoid invisible text delays.
- Split heavy JavaScript only when the framework and route behavior benefit from it.
- Avoid hydration or client-side work for static content when SSR/SSG can serve it.
- Use transform/opacity for animation and keep animation work off the layout path when possible.
- Reduce layout shift from late content, ads, banners, images, fonts, toolbars, and validation messages.
- Prefer measurement over guesswork when the repo has tooling or a browser profiler is available.

## Audit Triggers

- Large hero media with no size strategy.
- Heavy client bundles on mostly static pages.
- Layout shift from unloaded images or dynamic UI.
- Animations that jank scroll or ignore reduced motion.
- Third-party scripts in the critical path.
- Data fetching that blocks basic page shell rendering without need.
