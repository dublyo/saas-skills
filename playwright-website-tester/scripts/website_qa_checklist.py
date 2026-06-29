#!/usr/bin/env python3
"""Generate a Playwright website QA checklist."""

from __future__ import annotations

import argparse


BASE = [
    "Confirm target URL and whether it is local, staging, or production.",
    "Use the Playwright plugin, not the Chrome extension connector.",
    "Open a fresh Playwright tab/context; do not rely on the user's Chrome profile.",
    "If auth is needed, have the user type credentials directly in the Playwright browser.",
    "Avoid capturing secrets, tokens, or private account data in screenshots/reports.",
]

STANDARD = [
    "Navigate to homepage and confirm load state.",
    "Collect console errors/warnings.",
    "Collect network requests and identify failed first-party requests.",
    "Capture accessibility snapshot for headings, landmarks, controls, and forms.",
    "Check desktop viewport 1440x900.",
    "Check mobile viewport 390x844.",
    "Exercise primary navigation and CTAs.",
    "Exercise visible forms, buttons, dropdowns, modals, and search/filter controls.",
    "Look for overlap, clipping, horizontal overflow, broken sticky headers, and hidden content.",
]

DEEP = [
    "Crawl obvious internal nav routes and primary CTA routes.",
    "Re-check console/network after each important route.",
    "Check protected routes or auth redirects when applicable.",
    "Inspect failed request details for important API/resource failures.",
    "Check loading, empty, error, disabled, and retry states when visible.",
    "Note accessibility heuristic issues from snapshots.",
    "Group findings by severity with route, viewport, evidence, and reproduction steps.",
]

AUTH = {
    "none": ["Proceed unauthenticated and note any gated routes."],
    "unknown": ["Determine whether login is required; if blocked, ask the user to log in inside the Playwright browser."],
    "required": ["Pause at login and let the user enter credentials directly in the Playwright browser.", "Do not ask for or record passwords/OTP/session tokens."],
}


def emit(title: str, items: list[str]) -> None:
    print(f"## {title}")
    for item in items:
        print(f"- [ ] {item}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Playwright website QA checklist.")
    parser.add_argument("--depth", choices=["standard", "deep"], default="deep")
    parser.add_argument("--auth", choices=["none", "unknown", "required"], default="unknown")
    parser.add_argument("--target", default="<target-url>")
    args = parser.parse_args()

    print("# Playwright Website QA Checklist")
    print()
    print(f"- Target: {args.target}")
    print(f"- Depth: {args.depth}")
    print(f"- Auth: {args.auth}")
    print(f"- Lighthouse: skipped by default")
    print()

    emit("Base", BASE)
    emit("Authentication", AUTH[args.auth])
    emit("Standard QA", STANDARD)
    if args.depth == "deep":
        emit("Deep QA", DEEP)
    emit(
        "Final Report",
        [
            "Summarize tested routes, viewports, and flows.",
            "List findings by severity.",
            "Include console and network summaries.",
            "State limitations and checks not run.",
            "Recommend the next smallest useful action.",
        ],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
