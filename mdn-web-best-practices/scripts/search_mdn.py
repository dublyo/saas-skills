#!/usr/bin/env python3
"""Rank local MDN Web Docs Markdown files for a query."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_ROOT = Path("/Users/dribrahimm/skills/mozilla/content/files/en-us/web")


def title_for(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"')
    return path.parent.name.replace("_", " ")


def snippet_for(text: str, terms: list[str]) -> str:
    compact = re.sub(r"\s+", " ", text)
    lower = compact.lower()
    positions = [lower.find(term) for term in terms if lower.find(term) >= 0]
    if not positions:
        return compact[:220].strip()
    start = max(min(positions) - 80, 0)
    end = min(start + 260, len(compact))
    return compact[start:end].strip()


def score_file(path: Path, query: str, terms: list[str], root: Path) -> tuple[int, str, str] | None:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None

    rel = path.relative_to(root)
    path_text = str(rel).replace("_", " ").replace("-", " ").lower()
    title = title_for(text, path)
    title_text = title.lower()
    content = text.lower()
    query_l = query.lower()

    score = 0
    if query_l in path_text:
        score += 40
    if query_l in title_text:
        score += 30
    if query_l in content:
        score += 12

    for term in terms:
        if term in path_text:
            score += 10
        if term in title_text:
            score += 8
        count = content.count(term)
        if count:
            score += min(count, 8)

    if score == 0:
        return None

    return score, title, snippet_for(text, terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search local MDN Web Docs Markdown files.")
    parser.add_argument("query", nargs="+", help="Topic to search, for example: form validation")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="MDN web root directory")
    parser.add_argument("--limit", type=int, default=12, help="Maximum results to print")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    query = " ".join(args.query).strip()
    terms = [term.lower() for term in re.findall(r"[a-zA-Z0-9_:-]+", query) if len(term) > 1]

    if not root.exists():
        raise SystemExit(f"MDN root not found: {root}")
    if not terms:
        raise SystemExit("Provide a more specific query.")

    results: list[tuple[int, Path, str, str]] = []
    for path in root.rglob("*.md"):
        scored = score_file(path, query, terms, root)
        if scored:
            score, title, snippet = scored
            results.append((score, path, title, snippet))

    results.sort(key=lambda item: (-item[0], len(str(item[1]))))

    if not results:
        print(f"No Markdown results found under {root} for: {query}")
        return 1

    for index, (score, path, title, snippet) in enumerate(results[: args.limit], start=1):
        rel = path.relative_to(root)
        print(f"{index}. {title}")
        print(f"   score: {score}")
        print(f"   path: {path}")
        print(f"   relative: {rel}")
        print(f"   snippet: {snippet}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
