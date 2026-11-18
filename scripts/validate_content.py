#!/usr/bin/env python3
"""Validate monitored ASE publications and news without third-party packages."""

from __future__ import annotations

import re
import sys
import unicodedata
import argparse
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---", re.DOTALL)
TITLE = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
PUBLICATION_DATE = re.compile(r"^date:\s*[\"']?(\d{4}-\d{2}-\d{2})", re.MULTILINE)
DOI = re.compile(r"^doi:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)
MONITORING_DOI = re.compile(r"^  doi:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)
CANONICAL_KEY = re.compile(r"^\s*canonical_key:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)


def normalize(value: str) -> str:
    value = re.sub(r"[\u2010-\u2015]", " ", value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def front_matter(path: Path) -> str:
    match = FRONT_MATTER.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def normalize_doi(value: str) -> str:
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value.strip(), flags=re.I).lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    start = date(2025, 9, 1)
    errors: list[str] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    keys: dict[str, list[Path]] = defaultdict(list)
    dois: dict[str, list[Path]] = defaultdict(list)

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

        date_match = PUBLICATION_DATE.search(data)
        if key_match:
            try:
                publication_date = date.fromisoformat(date_match.group(1)) if date_match else None
            except ValueError:
                publication_date = None
            if publication_date is None or not start <= publication_date <= args.as_of:
                errors.append(f"{path.relative_to(ROOT)}: monitored publication outside {start}–{args.as_of} or invalid date")

        doi_match = DOI.search(data)
        monitoring_doi = MONITORING_DOI.search(data)
        doi = normalize_doi(doi_match.group(1)) if doi_match else ""
        if doi:
            dois[doi].append(path)
        if monitoring_doi and normalize_doi(monitoring_doi.group(1)) != doi:
            errors.append(f"{path.relative_to(ROOT)}: monitoring DOI differs from publication DOI")

    for label, index in (("DOI", dois), ("normalized title", titles), ("canonical key", keys)):
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
