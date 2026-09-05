# Lesson 25 — Markdown for documentation

[← Previous Lesson](24-readme-files.md) | [Course Home](../README.md) | [Next Lesson →](26-academic-notes.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Separate README content from long-form documentation
- Structure a `docs/` folder
- Write task-oriented pages (how-to, explanation, reference)
- Use consistent headings, code fences, and cross-links
- Know how docs sites (MkDocs, Docusaurus, GitHub wiki, Pages) consume Markdown

## Conceptual explanation

A README is a landing page. **Documentation** is the set of pages that teach people to *use* and *maintain* a system over time.

Diátaxis, a widely used docs model, splits documentation into four types:

| Type | Question | Example |
|------|----------|---------|
| Tutorials | "Guide me the first time" | Getting started |
| How-to guides | "How do I do X?" | How to export CSV |
| Reference | "What does this accept?" | CLI flags, API |
| Explanation | "Why is it designed this way?" | Architecture |

Markdown is the source format for most modern docs stacks. You write `.md` files; a generator builds a website with search and navigation.

This course itself is documentation: many small pages, one topic each, previous/next links, a home index.

## Syntax and folder patterns

A simple student-project layout:

```text
docs/
  index.md
  install.md
  usage.md
  api.md
  faq.md
```

Cross-link with relative paths:

```markdown
See [Installation](install.md) before [Usage](usage.md).
```

On GitHub, `docs/` can also be the GitHub Pages root (Lesson 28).

### Page template

```markdown
# How to export predictions

## Goal

Write `predictions.csv` from a trained model.

## Steps

1. ...
2. ...

## Next

[API reference](api.md)
```

## Beginner example

**Source** (`docs/install.md`)

````markdown
# Installation

## Requirements

- Python 3.11 or 3.12
- pip

## Steps

```bash
pip install -e .
```

If the command fails, see [FAQ](faq.md#install-errors).
````

**Expected rendered result**

A focused page that does one job. The README can now say "Install: see docs/install.md" instead of growing forever.

## Intermediate example: mixing the four docs types

```markdown
# tinyknn documentation

- Tutorial: [Quick start](tutorials/quickstart.md)
- How-to: [Save and load a model](how-to/save-load.md)
- Reference: [KNN API](reference/knn.md)
- Explanation: [Why we store distances in memory](explain/memory.md)
```

Each linked file uses headings, fenced examples, and a small table of parameters. Reference pages prefer tables (GFM):

```markdown
| Parameter | Type | Default | Meaning |
| --------- | ---- | ------- | ------- |
| `k` | `int` | `5` | Number of neighbors |
| `metric` | `str` | `"euclidean"` | Distance function |
```

## Advanced example: docs that stay truthful

Documentation rot is the main failure mode. Expert teams:

- Put example commands in CI or a `scripts/check-docs.sh` that runs them
- Review docs in the same pull request as code
- Avoid duplicating the same install steps in five files — link once
- Mark version: "Applies to v2.1"

GitHub wiki is another Markdown surface. Wikis are easy to edit but harder to version with the code. For course projects, prefer `docs/` *in the repository* so the grader sees a tagged snapshot.

### Generators (overview, not setup)

| Tool | Markdown flavor | Typical use |
|------|-----------------|-------------|
| GitHub Pages + Jekyll | GFM / kramdown | Simple project sites |
| MkDocs | GFM-like | Python projects |
| Docusaurus | MDX (Markdown + JSX) | JS/TS products |
| Quarto | Pandoc Markdown | Academic and data-science sites |
| Sphinx + MyST | MyST Markdown | Scientific Python |

MDX and MyST add extra syntax. If you must stay portable, stick to GFM in `docs/` and let the generator wrap it.

## Common mistakes

- One 4,000-line `README.md` instead of pages
- Docs that say "obviously" and skip the command
- Screenshots of the CLI without the actual command
- Absolute GitHub URLs to `blob/main/docs/...` that break on forks — prefer relative links
- Mixing tutorial narrative and API reference on one page until nobody can scan it

## Best practices

- One page, one job
- Start how-to pages with a goal and a last successful command
- Use the same command syntax as the real CLI
- Link forward and backward (as this course does)
- Put docs changes in the same commit as behavior changes
- Keep examples short and copyable

## Practical use cases

- Capstone software
- Research code released with a paper
- Teaching assistants' course websites
- Internal lab protocols (`docs/lab-safety.md`)

## Practice exercises

1. Split a fictional long README into `README.md` + `docs/usage.md`. Decide what stays on the home page.
2. Write a how-to page with Goal, Steps, Next.
3. Create an API table with four parameters.
4. Add previous/next links between two docs pages.

## Quick review

- README is the door; `docs/` is the house
- Tutorials, how-tos, reference, explanation
- Relative links, small pages, working examples
- Docs must change with the code
- Generators consume Markdown; GFM is a safe baseline

---

[← Previous Lesson](24-readme-files.md) | [Course Home](../README.md) | [Next Lesson →](26-academic-notes.md)
