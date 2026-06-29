#!/usr/bin/env python3
"""Generate a focused web design/code audit checklist."""

from __future__ import annotations

import argparse


SECTIONS = {
    "spec": [
        "Confirm target user, primary flow, page/app surface, and success criteria.",
        "Identify current framework, routing model, styling system, and validation scripts.",
        "List required states: loading, empty, error, success, disabled, long content, mobile, reduced motion.",
    ],
    "mdn": [
        "Search local MDN for any uncertain HTML, CSS, JavaScript, browser API, security, or accessibility behavior.",
        "Prefer semantic HTML and native controls before ARIA or custom JavaScript.",
        "Record exact MDN paths consulted for standards-sensitive decisions.",
    ],
    "design": [
        "Match visual density and style to the product surface and audience.",
        "Check hierarchy, spacing, typography, contrast, touch targets, and scan speed.",
        "Verify first viewport communicates the product or task clearly.",
    ],
    "html": [
        "Use headings, landmarks, links, buttons, lists, tables, media, and forms semantically.",
        "Avoid nested interactive controls and click handlers on non-interactive elements.",
        "Provide useful alt text, captions, table headers, and document metadata where applicable.",
    ],
    "css": [
        "Check responsive behavior across narrow, normal, and wide viewports.",
        "Prevent horizontal overflow, content clipping, layout shift, and hover/focus resizing.",
        "Respect reduced motion and keep focus states visible.",
    ],
    "javascript": [
        "Handle loading, error, timeout, retry, offline, and cancellation paths for async flows.",
        "Clean up listeners, timers, observers, and subscriptions where lifecycle matters.",
        "Check MDN before using permission-gated, secure-context, worker, storage, or media APIs.",
    ],
    "forms": [
        "Connect labels, descriptions, errors, and grouped choices correctly.",
        "Use input types, autocomplete, inputmode, validation attributes, and server validation deliberately.",
        "Prevent duplicate submissions and preserve user input after validation errors.",
    ],
    "accessibility": [
        "Keyboard-test primary flows and confirm visible focus.",
        "Check accessible names for icon buttons, custom controls, forms, and navigation.",
        "Review landmarks, heading order, contrast, non-color state cues, and reduced-motion behavior.",
    ],
    "performance": [
        "Review images, fonts, render-blocking resources, bundle size, hydration cost, and third-party scripts.",
        "Check layout shift risks from media, fonts, banners, errors, dynamic labels, and late data.",
        "Prefer measurement with browser tools when practical.",
    ],
    "security": [
        "Review raw HTML injection, rich text, Markdown, user URLs, uploads, iframes, and third-party scripts.",
        "Check auth/session assumptions, cookies, storage, CORS, CSP, and external links.",
        "Treat client-side validation as UX only for security/business rules.",
    ],
    "validation": [
        "Run available install/build/test/lint scripts.",
        "Run browser smoke test and check console.",
        "Capture or describe desktop/mobile responsive evidence.",
        "Report checks not run and why.",
    ],
}


def print_section(title: str, items: list[str]) -> None:
    print(f"## {title}")
    for item in items:
        print(f"- [ ] {item}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a web app audit/build checklist.")
    parser.add_argument("--mode", choices=["build", "audit", "full"], default="full")
    parser.add_argument("--surface", choices=["app", "landing", "dashboard", "form", "content", "tool"], default="app")
    parser.add_argument("--framework", default="current repo", help="Framework or stack name")
    parser.add_argument("--risk", choices=["normal", "high"], default="normal")
    args = parser.parse_args()

    print(f"# Web {args.mode.title()} Checklist")
    print()
    print(f"- Surface: {args.surface}")
    print(f"- Framework: {args.framework}")
    print(f"- Risk: {args.risk}")
    print()

    order = [
        "spec",
        "mdn",
        "design",
        "html",
        "css",
        "javascript",
        "forms",
        "accessibility",
        "performance",
        "security",
        "validation",
    ]

    if args.mode == "audit":
        order = ["spec", "mdn", "html", "css", "javascript", "forms", "accessibility", "performance", "security", "validation"]
    elif args.mode == "build":
        order = ["spec", "design", "mdn", "html", "css", "javascript", "forms", "accessibility", "performance", "security", "validation"]

    for key in order:
        title = key.replace("_", " ").title()
        print_section(title, SECTIONS[key])

    if args.surface == "landing":
        print_section(
            "Landing Page Specific",
            [
                "Make the product, place, object, or offer visible in the first viewport.",
                "Use real or generated relevant visuals, not generic decoration.",
                "Check mobile first viewport leaves a hint of the next section.",
            ],
        )
    elif args.surface == "dashboard":
        print_section(
            "Dashboard Specific",
            [
                "Prioritize scanning, comparison, filters, sorting, and repeated actions.",
                "Check table overflow, sticky regions, empty states, and dense data.",
                "Avoid marketing-style composition for operational workflows.",
            ],
        )
    elif args.surface == "form":
        print_section(
            "Form Specific",
            [
                "Check autofill, mobile keyboard, validation, progressive disclosure, and recovery.",
                "Confirm error summary or field-level errors for long forms.",
                "Test slow submit, duplicate submit, and server rejection states.",
            ],
        )

    if args.risk == "high":
        print_section(
            "High Risk Extras",
            [
                "Run deeper security review for user content, auth/session, payments, uploads, and embeds.",
                "Test with keyboard-only navigation across the complete critical flow.",
                "Use browser performance tools for the main page or interaction.",
            ],
        )

    print("## Helpful Commands")
    print("- `python3 /Users/dribrahimm/.agents/skills/mdn-web-best-practices/scripts/search_mdn.py \"topic\"`")
    print("- Run the repo's available build/test/lint commands before final response.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
