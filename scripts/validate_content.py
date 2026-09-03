#!/usr/bin/env python3
"""Validate monitored ASE publications and news without third-party packages."""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---", re.DOTALL)
TITLE = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
YEAR = re.compile(r"^date:\s*[\"']?(\d{4})", re.MULTILINE)
CANONICAL_KEY = re.compile(r"^\s*canonical_key:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)


def normalize(value: str) -> str:
    value = re.sub(r"[\u2010-\u2015]", " ", value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def front_matter(path: Path) -> str:
    match = FRONT_MATTER.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def main() -> int:
    errors: list[str] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    keys: dict[str, list[Path]] = defaultdict(list)

    for path in sorted((ROOT / "content" / "publications").glob("*/index.md")):
        data = front_matter(path)
        if not data:
            errors.append(f"{path.relative_to(ROOT)}: missing front matter")
            continue
        title_match = TITLE.search(data)
        if not title_match:
            errors.append(f"{path.relative_to(ROOT)}: missing title")
            continue
        titles[normalize(title_match.group(1))].append(path)

        key_match = CANONICAL_KEY.search(data)
        if key_match:
            key = normalize(key_match.group(1))
            keys[key].append(path)
            if key != normalize(title_match.group(1)):
                errors.append(f"{path.relative_to(ROOT)}: canonical_key does not match title")

        year_match = YEAR.search(data)
        if key_match and (not year_match or int(year_match.group(1)) not in range(2026, 2029)):
            errors.append(f"{path.relative_to(ROOT)}: monitored publication outside 2026-2028")

    for label, index in (("normalized title", titles), ("canonical key", keys)):
        for value, paths in index.items():
            if value and len(paths) > 1:
                joined = ", ".join(str(path.relative_to(ROOT)) for path in paths)
                errors.append(f"duplicate {label} '{value}': {joined}")

    if errors:
        print("Content validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Content validation passed: {len(titles)} publication pages checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
