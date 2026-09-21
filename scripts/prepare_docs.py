#!/usr/bin/env python
"""Stage the tutorial sources into _site-docs/ for the MkDocs build.

MkDocs requires `docs_dir` to be a child directory that does not contain
`mkdocs.yml`. The course Markdown lives at the repository root, so the
workflow and local builds run this script first: it copies the course
content into a generated `_site-docs/` folder (git-ignored) without
touching the original files.

Usage:  python scripts/prepare_docs.py
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "_site-docs"

# Course content plus files the theme needs (MathJax config, images).
SOURCES = [
    "README.md",
    "lessons",
    "exercises",
    "projects",
    "resources",
    "assets",
    "javascripts",
]


def main() -> int:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    missing = []
    for name in SOURCES:
        src = ROOT / name
        if src.is_dir():
            shutil.copytree(src, STAGING / name)
        elif src.is_file():
            shutil.copy2(src, STAGING / name)
        else:
            missing.append(name)

    if missing:
        print("warning: not found, skipped: " + ", ".join(missing), file=sys.stderr)
    print(f"Staged documentation sources into {STAGING}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
