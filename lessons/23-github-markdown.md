# Lesson 23 — GitHub-specific Markdown features

[← Previous Lesson](22-gfm.md) | [Course Home](../README.md) | [Next Lesson →](24-readme-files.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Mention people and teams with `@`
- Reference issues, pull requests, and commits
- Use GitHub alerts
- Add badges to a README
- Use collapsible sections, footnotes, and other GitHub extras together

## Conceptual explanation

Beyond GFM, **github.com** rewrites certain patterns into rich UI:

| Pattern | Result |
|---------|--------|
| `@username` | Profile mention, often notifies the user in issues/PRs |
| `#123` or `owner/repo#123` | Link to an issue or pull request |
| `a1b2c3d` (commit SHA) | Link to a commit |
| `> [!NOTE]` etc. | Colored alert box |
| User/org/repo shorthand | Link to a repository in some contexts |

These **do not work** on a generic CommonMark website unless that site reimplements them. Never rely on `@mention` in a PDF.

## Syntax

### Mentions

```markdown
Thanks @ada for the review.
```

In issues and PRs, this may notify `ada`. In a README, it usually still links but may not notify.

### Issues, PRs, discussions

```markdown
Fixed in #42.
See also octocat/Hello-World#12.
```

### Commits

```markdown
Introduced in 6dcb09b5b57875f334f61aebed695e2e4193db5e
```

GitHub shortens and links SHAs it recognizes.

### Alerts (GitHub Markdown)

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

The `> [!TYPE]` line must be the first line of the blockquote. The type is one of `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`.

### Badges

Badges are images (often from shields.io) wrapped in links:

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions)
```

They are ordinary image-links (Lesson 11), not a separate Markdown syntax.

### Syntax explanation

- Mentions and issue numbers are *textual conventions* GitHub parses after Markdown.
- Alerts are blockquotes with a special first line. On non-GitHub renderers they look like a quote starting with `[!NOTE]`.
- Do not indent the `[!NOTE]` marker oddly or it may not parse.

## Beginner example

**Source**

```markdown
> [!WARNING]
> Do not commit `.env` files. They contain secrets.

Questions? Open an issue on this repository.
```

**Expected rendered result on GitHub**

A colored warning callout. Elsewhere: a blockquote.

## Intermediate example: PR description

```markdown
Closes #88.

This PR adds stratified splits. Reviewers: @ml-staff.

> [!NOTE]
> Training time increases by about 10%.
```

**Expected rendered result**

Issue 88 linked and possibly auto-closed on merge (`Closes #88` is a GitHub keyword). The note renders as an alert.

Auto-close keywords include `Fixes`, `Closes`, `Resolves` plus an issue number. That is GitHub issue-tracker behavior, not Markdown.

## Advanced example: professional README header

```markdown
# forest-tools

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/forest-tools.svg)](https://pypi.org/project/forest-tools/)

Utilities for forestry plot data.

> [!TIP]
> New users should start at [Quick start](#quick-start).
```

**Expected rendered result**

Title, two badges, pitch sentence, tip alert, internal link.

### Wiki, discussions, and comments

The same GFM works in issue comments. Mentions are most useful there. READMEs should not `@` people just to decorate; it is noisy and can ping them on edits depending on context.

### HTML extras that pair well

`<details>` (Lesson 16) for long logs, plus alerts for the short warning, is a common GitHub docs pattern.

## Common mistakes

- Using alerts in a document that must look identical on GitHub Pages with an old processor. Test Pages separately (Lesson 28).
- Badge URLs pointing at a private CI that always shows "failing" to anonymous readers.
- `@everyone` style spam in issues.
- Writing `#1` when you meant a heading or a numbered point — in issues, `#1` is issue 1.
- Assuming Mermaid `click` can open GitHub issues. Restricted.

## Best practices

- Alerts for true notes, tips, and dangers — not for every paragraph.
- Badges: license, CI, docs, version — keep to a short row.
- Reference issues by number in PRs; use full `owner/repo#n` across repos.
- Do not mention users in a README without a reason.
- Provide a non-GitHub fallback sentence if the file is also a course PDF.

## Practical use cases

- PR and issue templates
- README warnings about breaking changes
- Changelog entries that cite PRs
- Org-internal wikis on GitHub

## Practice exercises

1. Write one of each alert type with a single-sentence body.
2. Draft a PR body that uses `Closes #12` and a task list.
3. Add a license badge that links to `LICENSE`.
4. Preview the same file in a non-GitHub editor. Record how alerts look.

## Quick review

- `@user`, `#123`, commit SHAs are GitHub linkification
- Alerts: `> [!NOTE]` (and TIP, IMPORTANT, WARNING, CAUTION)
- Badges are image links
- `Closes #n` is tracker syntax, not Markdown
- None of this is portable CommonMark

---

[← Previous Lesson](22-gfm.md) | [Course Home](../README.md) | [Next Lesson →](24-readme-files.md)
