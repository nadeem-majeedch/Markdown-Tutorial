# Lesson 22 — GitHub-Flavored Markdown (GFM)

[← Previous Lesson](21-mermaid.md) | [Course Home](../README.md) | [Next Lesson →](23-github-markdown.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Define GFM relative to CommonMark
- List the GFM extensions you already learned
- Write a document that uses GFM on purpose
- Avoid mixing "works on GitHub" with "works everywhere"
- Find the official GFM specification

## Conceptual explanation

**GitHub-Flavored Markdown** is CommonMark plus a documented set of extensions that GitHub uses for user content.

Think of three concentric circles:

1. **Original Markdown (2004)** — Gruber's syntax, some ambiguities
2. **CommonMark** — a strict specification many parsers implement
3. **GFM** — CommonMark + tables, task lists, strikethrough, autolinks, and other extensions

When you write a `README.md` on GitHub, you are writing **GFM** (plus some GitHub-only extras in Lesson 23 that are *not* all in the GFM spec, such as `@mentions` and alerts).

That split matters:

| In the GFM spec | GitHub extra (next lesson) |
|-----------------|----------------------------|
| Tables | `@user` mentions |
| Task list items | `#123` issue references |
| Strikethrough | Alerts `> [!NOTE]` |
| URL autolinks | Geolocation? no — commit SHAs, etc. |
| Disallowed raw HTML (sanitization notes) | Mermaid, math (product features) |

Math and Mermaid are GitHub *product* features layered on Markdown. They may not appear in the GFM spec even though they work on github.com. Always distinguish **spec GFM** from **what the website currently renders**.

## Syntax you already know, now labeled

### Strikethrough

```markdown
~~removed API~~
```

### Tables

```markdown
| A | B |
| - | - |
| 1 | 2 |
```

### Task lists

```markdown
- [x] Draft
- [ ] Review
```

### Autolinks

```markdown
Visit https://spec.commonmark.org/ without angle brackets.
```

CommonMark autolinks need `<https://...>`. GFM also linkifies many bare URLs.

### Syntax explanation

GFM parsers first apply CommonMark block and inline rules, then extra rules for pipes, tildes, and checkboxes. If a construct is ambiguous, the [GFM spec](https://github.github.com/gfm/) is the authority for GFM, not a random blog.

## Beginner example

A fully portable-plus-GFM note:

```markdown
# Office hours

Bring your laptop. We will **not** debug ~~Windows 7~~ unsupported OS versions.

- [ ] Update Git
- [ ] Clone https://github.com/example/lab

| Slot | Room |
| ---- | ---- |
| 10:00 | 2.14 |
```

**Expected rendered result on GitHub**

Heading, strikethrough, task list, autolinked URL, table.

On a strict CommonMark CLI, tables and tasks may show as literal text.

## Intermediate example: writing to the spec on purpose

When you publish a library, decide a policy and state it:

```markdown
This document is written in GitHub-Flavored Markdown.
Tables and task lists require a GFM renderer.
```

Then use GFM freely in that repository. When you write a file that must compile with a picky static generator, stick to CommonMark: headings, lists, links, emphasis, fenced code.

## Advanced example: GFM vs GitHub product Markdown

```markdown
~~GFM strikethrough~~

- [ ] GFM task

https://example.com

> [!NOTE]
> This alert is GitHub UI, not necessarily GFM spec.

@octocat mentioned — GitHub extra.

See #1 — GitHub extra.
```

**Expert habit:** if you need a feature, ask:

1. Is it CommonMark?
2. If not, is it GFM spec?
3. If not, is it a GitHub website feature?
4. If not, is it a third-party tool (Typora highlight, Pandoc definition lists)?

Document the answer in your project if multiple renderers are in play (README vs PDF vs course LMS).

## Common mistakes

- Calling everything "Markdown" when you mean GFM or GitHub.
- Copying a README into an LMS that strips tables.
- Using GFM tables in an email client that is not GFM.
- Treating the GFM spec as covering Mermaid, math, and alerts. Check current GitHub docs too.

## Best practices

- Default student target: **GFM on GitHub**.
- For maximum portability, avoid tables/tasks or also ship HTML/PDF.
- Link the spec in contributor docs: https://github.github.com/gfm/
- Keep a cheat sheet of "allowed in this repo."
- Test paste into the real destination (GitHub preview tab).

## Practical use cases

- All GitHub READMEs, issues, pull requests, wiki pages
- Many static site generators with a `gfm` option
- VS Code preview (largely GFM-like)

## Practice exercises

1. List five features from this course that are CommonMark and five that are GFM or GitHub-only.
2. Rewrite a GFM table as a bullet list so it survives a CommonMark-only tool.
3. Open the GFM spec in a browser and find the section on tables.
4. Preview `~~a~~` and `- [x] b` in your editor. Does it match GitHub?

## Quick review

- GFM = CommonMark + extensions (tables, tasks, strikethrough, autolinks, …)
- GitHub the product adds still more (mentions, alerts, mermaid, math)
- Know your renderer
- The GFM spec is the reference for GFM, not for every GitHub feature

---

[← Previous Lesson](21-mermaid.md) | [Course Home](../README.md) | [Next Lesson →](23-github-markdown.md)
