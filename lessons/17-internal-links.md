# Lesson 17 — Anchors and internal links

[← Previous Lesson](16-html.md) | [Course Home](../README.md) | [Next Lesson →](18-footnotes.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Link to a heading on the same page
- Predict GitHub's generated heading IDs
- Build a table of contents (TOC)
- Link to headings in another file
- Handle duplicate headings and punctuation in IDs

## Conceptual explanation

An **anchor** is a location in a page that a URL can point to. In HTML it looks like `id="installation"`. The full URL looks like `README.md#installation`.

Markdown does not make you write IDs by hand for ordinary headings. **GitHub generates an ID from the heading text.** You then link with:

```markdown
[Installation](#installation)
```

Internal links turn a long README or lecture note into a navigable document. They are how this course's "jump to section" idea works, and how professional READMEs offer a TOC near the top.

Anchor generation is **renderer-dependent**. GitHub's rules are the ones you should learn first if your audience is GitHub. GitHub Pages, VS Code, and Pandoc can differ slightly.

## Syntax

### Same-file heading link

```markdown
## Installation

...

See the [installation](#installation) section.
```

### Table of contents

```markdown
## Contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Citing](#citing)
```

### Link to another file's heading

```markdown
[Escaping](13-horizontal-rules-escaping.md#syntax-escaping)
```

### Manual HTML anchor (when you must)

```html
<a id="custom-id"></a>
```

```markdown
[Jump](#custom-id)
```

Use this rarely. Generated heading IDs are easier to maintain.

### Syntax explanation — GitHub heading IDs

GitHub (approximately):

1. Lowercase the heading text
2. Remove punctuation except hyphens, spaces, and underscores (most punctuation dropped)
3. Replace spaces with hyphens
4. If the ID already exists, append `-1`, `-2`, ...

Examples:

| Heading | GitHub ID |
|---------|-----------|
| `Installation` | `installation` |
| `Quick start` | `quick-start` |
| `Using numpy.mean` | `using-numpymean` (period dropped) |
| `FAQ` | `faq` |
| `FAQ` (second) | `faq-1` |

Always click the heading chain icon on GitHub to copy the real fragment if you are unsure.

## Beginner example

**Source**

```markdown
# Lab 7

Jump to [Methods](#methods).

## Methods

We used stratified 5-fold cross-validation.
```

**Expected rendered result**

"Methods" is a link. Clicking it scrolls to the H2.

## Intermediate example: course-note TOC

```markdown
# Week 11 — Clustering

## Contents

- [k-means](#k-means)
- [Hierarchical clustering](#hierarchical-clustering)
- [Choosing k](#choosing-k)
- [Lab preview](#lab-preview)

## k-means

## Hierarchical clustering

## Choosing k

## Lab preview
```

**Expected rendered result**

A clickable contents list. If you rename a heading, you must update the TOC. That is the main maintenance cost.

## Advanced example: duplicates, emoji, and code in headings

```markdown
## Setup

## Setup
```

The second becomes `#setup-1`.

```markdown
## 🎉 Release notes
```

GitHub often keeps the emoji in the ID or strips it depending on current rules — **click to verify**. For portable docs, keep headings ASCII:

```markdown
## Release notes
```

Headings with backticks:

```markdown
## The `fit` method
```

The ID may be `the-fit-method`. Copy from the UI.

### README pattern used in industry

```markdown
# Project name

Short pitch.

## Table of contents

- [Features](#features)
- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
```

Lesson 24 uses this in a full README.

### GitHub Pages difference

Jekyll / kramdown may slug headings differently (for example, keeping or dropping trailing punctuation). If you publish the same Markdown on Pages, click the rendered heading rather than guessing.

## Common mistakes

- Guessing the ID and using spaces: `#Quick start` is wrong; `#quick-start` is right.
- Forgetting the `#`.
- Linking to `#Installation` with capital letters. GitHub IDs are lowercase.
- Changing a heading and leaving a dead TOC link.
- Duplicate "Overview" headings in one file.
- Using underscores vs hyphens inconsistently when guessing.

## Best practices

- Write unique, short, ASCII headings so IDs stay obvious.
- After adding a TOC, click every item once.
- Prefer relative file links plus fragments for multi-page docs: `api.md#errors`.
- Do not pack punctuation, `:`, or `/` into headings you will link to.
- If the document is long (this course's README, a thesis chapter), a TOC is a kindness.

## Practical use cases

- **README:** table of contents
- **API docs:** jump from overview to each endpoint
- **Lecture notes:** agenda at the top
- **This course:** every "Next lesson" is a *file* link; section links are *fragment* links

## Practice exercises

1. Create a file with three H2s and a TOC that links to each.
2. Duplicate an H2 and record the two fragment IDs GitHub (or your preview) generates.
3. Link from `README.md` to `lessons/17-internal-links.md#beginner-example` in your mind: write the correct relative path from the repo root.
4. Rename one heading and update the TOC.

## Quick review

- Same-page link: `[text](#heading-id)`
- GitHub IDs: lowercase, spaces to hyphens, punctuation mostly removed
- Other files: `[text](file.md#id)`
- Duplicate headings get `-1`, `-2`
- Always verify fragments on the real renderer

---

[← Previous Lesson](16-html.md) | [Course Home](../README.md) | [Next Lesson →](18-footnotes.md)
