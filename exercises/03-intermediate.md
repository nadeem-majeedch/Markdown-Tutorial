# Exercise set 3 — Tables, tasks, HTML, and anchors

**Level:** Intermediate  
**Lessons:** [14](../lessons/14-tables.md)–[18](../lessons/18-footnotes.md)

[← Previous set](02-beginner-structure.md) | [Exercises home](README.md) | [Course Home](../README.md) | [Next set →](04-intermediate-gfm.md)

---

## Goals

Create `exercises/work/03-experiment.md` as a mini experiment log.

## Exercises

### 1. Results table

Build a GFM table with columns Run, Model, Accuracy, Notes.

- At least three data rows
- Accuracy right-aligned
- One cell containing inline code
- One cell containing a link

### 2. Alignment check

Add a second table with left, center, and right columns using colons in the separator.

### 3. Task list

A pre-registration checklist:

- [x] two completed items
- [ ] two remaining items
- one nested pair of subtasks

### 4. Table of contents

At the top, link to every H2 in the file using GitHub-style IDs. Click them after you push or preview.

### 5. Footnote

Cite a fictional paper in one sentence with `[^author2024]` and define the footnote at the bottom. Include a URL inside the footnote.

### 6. Glossary

Write three terms in a **GitHub-portable** glossary (not Pandoc colon syntax). Optionally add an HTML `<dl>` version underneath and compare.

### 7. HTML extras

- A chemical or math-ish formula using `<sub>` or `<sup>`
- A `<details>` hint block with inner Markdown (blank lines included)
- An HTML `<img>` with `alt` and `width="320"`

### 8. Limits

In a short paragraph, list two things GFM tables cannot do (merged cells, nested tables, …).

## Self-check

- [ ] Every table has a separator row
- [ ] TOC fragments match heading IDs
- [ ] Footnote definition exists
- [ ] `<details>` inner Markdown actually renders on GitHub
- [ ] Task markers are `- [ ]` / `- [x]` with spaces

## Stretch

Add a fourth table column that would require an escaped pipe `\|` inside a cell (for example a regex snippet).
