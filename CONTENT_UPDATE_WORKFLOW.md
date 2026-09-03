# ASE website content-update workflow

This repository publishes its Hugo source from the `gh-pages` branch. Every
content update must follow the sequence below.

## 1. Synchronize

1. Work on `gh-pages` and require a clean working tree.
2. Run `git pull --ff-only origin gh-pages` before reading sources or editing.
3. Stop if the pull cannot be completed or if unrelated local changes exist.

## 2. Collect and reconcile sources

- Prisma project page: <https://prisma.us.es/financiacion/18003>
- Google Scholar profiles: `monitoring/members.csv`
- LinkedIn hashtag: <https://www.linkedin.com/search/results/all/?keywords=%23aseproject>
- LinkedIn member profiles: `monitoring/members.csv`

Publication policy:

- Include every publication dated 2026, 2027, or 2028 from any listed Scholar
  profile, plus every publication associated with the project in Prisma.
- Prefer Prisma metadata when the same record is present in Prisma and Scholar.
- Deduplicate first by DOI, then by a canonical title obtained with Unicode
  normalization, lower-casing, punctuation removal, and whitespace collapse.
- Merge source links and the most complete author/venue metadata into one page.
- Never add a second page for capitalization, punctuation, preprint, or
  publisher-record variants without explicit human approval.

News policy:

- Consider posts using `#aseproject` and posts authored by project members.
- Include research-related talks, visits, research stays, awards, and conference
  participation.
- Deduplicate by canonical LinkedIn post URL; if unavailable, use normalized
  title, author, and event date.
- Write all website copy in English and retain the original LinkedIn source URL.

Blank profile cells in the CSV are intentionally ignored. Never guess a profile.

## 3. Edit and validate

- Publications belong in `content/publications/<slug>/index.md`.
- News belongs in `content/news/<slug>/index.md`.
- Set `featured: true` for items intended for the home page.
- Add a stable `monitoring.canonical_key` and all known source identifiers.
- Run `python3 scripts/validate_content.py` and resolve every reported error.

## 4. First approval: local preview

Build and serve the site locally with Hugo Extended 0.119.0. Show the preview
and the complete Git diff to the project owner. Do not commit or push until the
owner explicitly approves this version.

## 5. Publish

After approval, commit only the reviewed files and push `gh-pages` to `origin`.
The GitHub Pages workflow must finish successfully before production is checked.

## 6. Final approval

Open <https://isa-group.github.io/aseproject/>, verify the new pages and links,
and request final approval from the project owner. Do not silently amend an
approved production release; begin a new workflow run for follow-up changes.

Scheduled checks stop after reporting or preparing reviewable local changes.
They never commit or push without the first approval.
