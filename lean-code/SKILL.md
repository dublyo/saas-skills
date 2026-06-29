---
name: lean-code
description: >
  Write the shortest correct code that does exactly what was asked - nothing
  more. Solve the direct target, reach for stdlib and native features before
  custom code, one line before fifty, and never cut validation, error handling,
  security, or accessibility. Use whenever the user wants minimal, direct, no-
  fluff code, or complains about bloat, boilerplate, over-engineering, or
  unnecessary dependencies.
license: MIT
---

# Lean Code

Write code like a senior dev who is paid to solve the problem, not to show off.
The best code is the code you did not have to write. Hit the exact target the
user asked for, in the fewest correct lines, and stop.

## The target rule

Solve **only** what was asked. Restate the goal in one sentence, then write the
smallest thing that fully meets it. No extra features, options, config, or
"while we're here" additions. If you think they need more, ship the direct
answer first and ask in one line.

## The ladder (stop at the first rung that holds)

1. **Does it need to exist?** Speculative need -> skip it, say so in one line.
2. **Standard library does it?** Use it.
3. **Native platform feature covers it?** Use it (`<input type="date">` over a
   picker lib, CSS over JS, a DB constraint over app code).
4. **An installed dependency solves it?** Use it. Don't add a new dependency for
   what a few lines do.
5. **Can it be one line?** Make it one line.
6. **Only then:** write the minimum code that works.

Two rungs work -> take the higher one and move on. The first solution that
works is the right one.

## Rules

- No abstraction with one caller. No interface with one implementation. No
  config for a value that never changes.
- Deletion over addition. Boring over clever - clever is what someone debugs at
  3am.
- Fewest files, shortest diff that does the job.
- Match the surrounding code's style, names, and patterns.
- Two same-size options -> pick the one that is correct on edge cases. Lazy
  means less code, not a flimsier algorithm.
- Mark a deliberate shortcut with a `lean:` comment naming its ceiling and the
  upgrade path, e.g. `// lean: in-memory only, swap for Redis if multi-process`.

## Never cut (lazy is not careless)

Input validation at trust boundaries, error handling that prevents data loss,
security, accessibility, and anything the user explicitly asked to keep. Code
without its check is unfinished: non-trivial logic leaves ONE runnable check
behind (a small test or an assert-based self-check). Trivial one-liners need
none.

## Output

Code first. Then at most three short lines: what you skipped and when to add it.
If the explanation is longer than the code, delete the explanation. Give full
explanation only when the user explicitly asked for one.

Pattern: `[code] -> skipped: [X], add when [Y].`
