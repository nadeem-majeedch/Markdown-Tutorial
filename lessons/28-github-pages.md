# Lesson 28 — Markdown with GitHub Pages

[← Previous Lesson](27-project-documentation.md) | [Course Home](../README.md) | [Next Lesson →](29-limitations.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Explain what GitHub Pages is
- Publish a Markdown repository as a website
- Configure a basic Jekyll `_config.yml`
- Understand differences between github.com file view and Pages
- Troubleshoot missing pages and broken relative links

## Conceptual explanation

**GitHub Pages** builds a static website from files in your repository. For a course like this one, each `.md` file can become an HTML page.

Two mental models:

1. **github.com file rendering** — you browse `README.md` inside the repo UI (GFM).
2. **Pages site** — visitors open `https://USERNAME.github.io/REPO/` and see a themed site.

This repository includes `_config.yml` so Pages can use the Cayman theme:

```yaml
title: Markdown Language Tutorial
theme: jekyll-theme-cayman
markdown: GFM
```

Jekyll is the default Pages generator. It treats Markdown files as pages. A file `/lessons/01-introduction.md` becomes a URL path like `/lessons/01-introduction.html` (pretty URLs may drop `.html`).

## Syntax and configuration

### Enable Pages (manual steps on GitHub)

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Source: **Deploy from a branch**.
4. Branch: `main` or `master`, folder `/ (root)` or `/docs`.
5. Save and wait for the Actions build.

You cannot finish the click-ops from this lesson file; you do it in the GitHub UI.

### Front matter (Jekyll)

Optional YAML at the top of a page:

```markdown
---
title: Introduction
---

# Introduction to Markdown
```

Without front matter, Jekyll still converts many `.md` files, depending on theme and version. Lesson files in this course omit front matter so they also read cleanly on github.com.

### Relative links

On GitHub file view, `[Next](02-what-is-markdown.md)` works.

On Pages, the same relative link usually still works if both files are built. Prefer extension-inclusive links that exist as real files (this course uses `.md` links, which GitHub file view needs). Some themes rewrite `.md` to `.html`. If a link 404s on Pages but works in the repo, check whether the theme expects `.html` or extensionless URLs.

This course uses `.md` targets so **repository navigation never breaks**. That is the correct default for a GitHub curriculum. If you customize a theme, test both surfaces.

## Beginner example

A minimal user site in `docs/`:

```text
docs/index.md
docs/about.md
```

`docs/index.md`:

```markdown
# My notes

- [About](about.md)
```

Set Pages source to `/docs`.

**Expected result**

A public URL serving those pages with the chosen theme.

## Intermediate example: this course

```text
README.md          → site home if published from root
lessons/*.md       → lesson pages
_config.yml        → theme and GFM
```

Cayman provides a header from `title` in `_config.yml`. Content is your Markdown.

**kramdown vs GFM:** `_config.yml` in this repo sets `markdown: GFM` when the Pages environment supports it. If a feature fails on Pages (alerts, mermaid), it may still work in the repo view. Lesson 29 discusses that gap.

## Advanced example: project documentation site

Many libraries use Pages for `docs/`:

```text
docs/index.md
docs/api.md
docs/assets/logo.svg
```

Add a `docs/_config.yml` if the site root is `docs/`.

Quarto and MkDocs can also deploy to Pages via GitHub Actions. Those tools are outside the Markdown syntax course, but they still start from `.md` (or `.qmd`) files.

### Custom domains and HTTPS

Pages supports custom domains in the repository settings. Students do not need that for class. Use the default `*.github.io` URL.

## Common mistakes

- Enabling Pages on the wrong branch
- Linking to `/workspace/...` absolute paths that only exist on your machine
- Expecting Jekyll to run Python or a database — Pages is static
- Committing a broken `_config.yml` (tabs, invalid YAML)
- Using `url: localhost` in config
- Forgetting that private-repo Pages may require a paid plan (org/policy dependent)

## Best practices

- Test links in the repo UI first, then on the Pages URL
- Keep `_config.yml` small
- Do not put secrets in Pages files — the site is public
- Prefer relative links
- Document the Pages URL in the README once it exists
- For class submissions, the repo view is enough even if Pages is off

## Practical use cases

- Publishing this tutorial
- Student portfolio of Markdown notes
- Project documentation
- Course mini-site (syllabus + schedule as Markdown)

## Practice exercises

1. Read `_config.yml` at the repository root. What theme is set?
2. Write the GitHub UI steps to publish from `master` or `main` at `/ (root)`.
3. Predict the Pages path for `lessons/12-code.md`.
4. Find one feature from Lesson 23 that might look different on Pages than on github.com file view.

## Quick review

- Pages turns Markdown into a static website
- Configure under Settings → Pages
- `_config.yml` selects a Jekyll theme
- Relative `.md` links are required for repo study; test them on Pages too
- Pages is public static hosting, not a full web app platform

---

[← Previous Lesson](27-project-documentation.md) | [Course Home](../README.md) | [Next Lesson →](29-limitations.md)
