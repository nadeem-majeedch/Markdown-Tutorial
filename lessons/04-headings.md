# Lesson 04 — Headings

[← Previous Lesson](03-basic-syntax.md) | [Course Home](../README.md) | [Next Lesson →](05-paragraphs.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write headings at levels 1 through 6
- Use ATX (`#`) headings confidently
- Recognize Setext headings
- Build a sensible document outline
- Avoid heading mistakes that break navigation and accessibility

## Conceptual explanation

Headings create the **outline** of a document. They are not just large, bold text. Screen readers, GitHub's outline panel, and tables of contents all use heading levels to understand structure.

HTML has six heading levels: `h1` through `h6`. Markdown maps onto those levels.

A good mental model is a book:

| Level | Role | Example |
|-------|------|---------|
| `#` H1 | Document title | A Course in Machine Learning |
| `##` H2 | Chapter or major section | Supervised Learning |
| `###` H3 | Subsection | k-Nearest Neighbors |
| `####` H4 | Minor subsection | Choosing k |
| `#####` / `######` | Rarely needed | Notes inside a nested subsection |

Most student documents need H1–H3. If you reach H6, the outline is probably too deep.

**There should usually be one H1 per page:** the title of that file.

## Syntax

### ATX headings (preferred)

```markdown
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
```

### Syntax explanation

- Start the line with 1–6 hash characters.
- Put a space after the hashes. `#Title` is not reliable; `# Title` is correct.
- The rest of the line is the heading text. Inline formatting such as `**bold**` is allowed but usually unnecessary.
- Closing hashes are optional and uncommon in modern style: `## Methods ##`

### Setext headings (legacy, levels 1–2 only)

```markdown
Heading level 1
===============

Heading level 2
---------------
```

Underline with `=` for H1 and `-` for H2. Setext headings cannot express H3–H6. This course uses ATX headings everywhere.

## Beginner example

**Source**

```markdown
# Biology 210 Lab Report

## Introduction

## Methods

## Results

## Discussion
```

**Expected rendered result**

A title in large type, then four smaller section titles in order. GitHub will list those sections in the outline menu (the icon near the top of a file view).

## Intermediate example

A lecture-note outline with three levels:

```markdown
# Week 9: Recursion

## 1. Motivation

Why repeat work with a stack of calls?

## 2. The pattern

### Base case

The smallest input you can answer immediately.

### Recursive case

A smaller call plus a combination step.

## 3. Classic problems

### Factorial

### Binary search

### Merge sort
```

**Expected rendered result**

A nested outline. Do not skip levels: do not jump from `#` to `###` just to change visual size. Use CSS or bold text if you only want emphasis. Headings mean *structure*.

## Advanced example: headings in a GitHub README

```markdown
# medscan

Lightweight preprocessing for medical image datasets.

## Features

## Installation

## Quick start

## Documentation

## Citing

## License
```

This H1 + H2 pattern is the standard first impression of an open-source repository. Lesson 24 develops it into a full README.

### Heading IDs (preview)

On GitHub, `## Quick start` becomes an anchor such as `#quick-start`. You can link to it with `[Quick start](#quick-start)`. Full details are in Lesson 17. You already need clean, unique heading text so those anchors stay stable.

## Common mistakes

- No space after hashes: `#Title` may render as a paragraph.
- Using headings only to make text big. That confuses the outline and accessibility tools.
- Multiple H1s on one page. Allowed by the parser; confusing for readers and some generators.
- Skipping levels (`#` then `####`) to get a "look."
- Putting links or `code` in every heading. Occasional inline code is fine (`## Using numpy.mean`); long headings are not.
- Ending a heading with punctuation soup. `## Results (final)!!!` makes ugly anchors.
- Forgetting a blank line before the heading when it follows a paragraph.

## Best practices

- One H1: the document title.
- Walk levels in order: H1 → H2 → H3.
- Keep headings short, unique, and descriptive. Prefer `## Training the model` over `## Part 2`.
- Use sentence case or title case consistently in a project. This course uses sentence case after the lesson title.
- Put a blank line before and after headings.
- Prefer ATX (`#`) over Setext.

## Practical use cases

- **Course notes:** H1 = week, H2 = topic, H3 = example
- **Lab report:** IMRaD sections as H2
- **README:** product name as H1, user tasks as H2
- **Thesis notes:** one file per chapter, H1 = chapter title

## Practice exercises

1. Create `essay-outline.md` with one H1 and four H2s for a short paper (introduction, argument, evidence, conclusion).
2. Add H3s under **Evidence** for two sources.
3. Preview the GitHub or VS Code outline. Does it match your intended structure?
4. Rewrite this bad outline so levels are not skipped:

   ```markdown
   # Project
   #### Setup
   ## Usage
   ```

## Quick review

- Headings are structure, not decoration.
- ATX syntax: `#` through `######`, plus a space.
- One H1 per page; do not skip levels.
- GitHub builds anchors and an outline from your headings.

---

[← Previous Lesson](03-basic-syntax.md) | [Course Home](../README.md) | [Next Lesson →](05-paragraphs.md)
