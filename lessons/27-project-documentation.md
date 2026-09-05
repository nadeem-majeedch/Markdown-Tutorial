# Lesson 27 — Markdown for project documentation

[← Previous Lesson](26-academic-notes.md) | [Course Home](../README.md) | [Next Lesson →](28-github-pages.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Identify the standard Markdown files in a professional repository
- Write CONTRIBUTING, CHANGELOG, CODE_OF_CONDUCT, and SECURITY drafts
- Record an Architecture Decision Record (ADR)
- Keep project docs discoverable from the README
- Use GitHub community files in `.github/`

## Conceptual explanation

A **project** is more than source code. People need to know how to contribute, what changed, how to report a vulnerability, and why a design looks the way it does.

Markdown is the default format for these files because GitHub renders them with special treatment:

| File | GitHub behavior |
|------|-----------------|
| `README.md` | Repo home |
| `LICENSE` | License detector (often plain text) |
| `CONTRIBUTING.md` | Linked when opening issues/PRs |
| `CODE_OF_CONDUCT.md` | Community tab |
| `SECURITY.md` | Security policy tab |
| `CHANGELOG.md` | Human history of versions |
| `docs/` | Project documentation |
| `.github/ISSUE_TEMPLATE/` | New-issue forms and Markdown templates |
| `adr/0001-....md` | Team memory (convention, not a GitHub feature) |

You already saw [CONTRIBUTING.md](../CONTRIBUTING.md) in this course.

## Syntax: conventional files

None of these files need special Markdown features. They need **clear headings and lists**.

### CHANGELOG (Keep a Changelog style)

```markdown
# Changelog

## [1.2.0] — 2026-03-01

### Added

- CSV export (`--out`)

### Fixed

- Crash on empty files

### Changed

- Default `k` from 3 to 5
```

### ADR

```markdown
# ADR 0001. Store models as joblib files

## Status

Accepted

## Context

We need a one-command load path for student labs.

## Decision

Serialize with `joblib.dump`.

## Consequences

Python-only. Not portable to R without a converter.
```

## Beginner example: tiny team repo

```markdown
# Contributing

## Issues

Open an issue before large changes.

## Pull requests

1. Create a branch
2. Add tests
3. Update `README.md` if usage changes
4. Fill in the PR checklist
```

**Expected rendered result**

A short, actionable page. GitHub will surface it to contributors.

## Intermediate example: SECURITY.md

```markdown
# Security policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 2.x     | Yes       |
| 1.x     | No        |

## Reporting

Email `security@example.edu` with a description and a reproduction.
Do **not** open a public issue for vulnerabilities.
```

**Expected rendered result on GitHub**

The Security tab uses this file. The table is GFM.

## Advanced example: `.github` templates

`.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Summary

## Checklist

- [ ] Tests
- [ ] Docs
- [ ] No secrets
```

`.github/ISSUE_TEMPLATE/bug.md`:

```markdown
---
name: Bug report
about: Report incorrect behavior
---

## Expected

## Actual

## Steps
```

The YAML between `---` is **GitHub issue-template front matter**, not a horizontal rule (Lesson 13).

### Linking the web of files

From README:

```markdown
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Security](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Docs](docs/index.md)
```

Relative links keep forks working.

## Common mistakes

- CONTRIBUTING.md that only says "be nice" with no branch or test instructions
- CHANGELOG that is a Git dump (`git log` pasted raw)
- SECURITY.md that tells people to file public issues for exploits
- ADRs written after the fact as fiction — they should capture real options
- Community files left as GitHub's unedited boilerplate

## Best practices

- Keep CONTRIBUTING in the same style as your lessons: steps, not slogans
- Version the changelog when you tag releases
- Put templates in `.github/` so every issue starts structured
- Write ADRs when the team disagrees, not for every tiny choice
- Link everything from the README
- Match the license file to the README badge

## Practical use cases

- Student team capstones
- Open-source homework libraries
- Research group code
- Internships: this is what professional repos look like

## Practice exercises

1. Write a 15-line CONTRIBUTING.md for a class team of four.
2. Draft a changelog with Added / Fixed sections.
3. Write ADR 0001 for "we will use Python 3.12."
4. List which files GitHub treats specially vs which are only convention.

## Quick review

- Project docs are a small set of well-known Markdown files
- GitHub renders several of them in dedicated UI tabs
- CHANGELOG, ADRs, and templates keep teams aligned
- Link them from the README
- Templates may use YAML front matter

---

[← Previous Lesson](26-academic-notes.md) | [Course Home](../README.md) | [Next Lesson →](28-github-pages.md)
