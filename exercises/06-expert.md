# Exercise set 6 — Portability, accessibility, and polish

**Level:** Expert  
**Lessons:** [29](../lessons/29-limitations.md)–[34](../lessons/34-professional-examples.md)

[← Previous set](05-advanced-docs.md) | [Exercises home](README.md) | [Course Home](../README.md) | [Final project →](../projects/final-project.md)

---

## Goals

Take any Markdown file you already wrote (set 4 or 5 is ideal) and produce two versions:

- `exercises/work/06-github.md` — allowed to use GFM and GitHub extras
- `exercises/work/06-portable.md` — CommonMark-friendly: no tables required (convert to lists), no alerts, no Mermaid, no shortcodes, no footnotes if you want maximum safety (tables may remain if you document GFM; for this exercise **remove** tables, alerts, mermaid, and `$` math)

## Exercises

### 1. Portability ladder

Add an H2 `Dialect` to each file stating which ladder level you targeted (Lesson 29).

### 2. Rewrite alerts

Replace every `> [!WARNING]` with a portable `**Warning:**` sentence in the portable file.

### 3. Rewrite tables

Turn one table into a nested list or a sequence of paragraphs.

### 4. Accessibility pass

Run this checklist and tick it in a task list at the bottom of `06-github.md`:

- [ ] One H1, no skipped heading levels
- [ ] No "click here" links
- [ ] Images have useful alt text (or no images)
- [ ] Meaning not color-only
- [ ] Code in fences, not screenshots
- [ ] Critical steps not only inside `<details>`

### 5. Fix a broken sample

Repair this fragment and paste the fixed version:

````markdown
# Overview
#### setup
click [here](https://example.com)
![img](plot.PNG)
-item
| a | b |
| 1 | 2 |
```python
print("oops")
````

The fragment is missing a closing fence, skips a heading level, reverses nothing but uses "click here", has weak alt text, a missing list space, and a table without a separator. Produce a clean file.

### 6. Professional clone

Pick Example A or B from [Lesson 34](../lessons/34-professional-examples.md). Rewrite it for a project in *your* major in 40–60 lines. Label GitHub-only features in italics as `(GitHub)` after the line, or omit them.

### 7. Review a stranger's README

Open any public GitHub README. Write a 10-line critique covering structure, examples, accessibility, and portability. Use a blockquote for one sentence you would steal.

## Self-check

- [ ] Portable file has no Mermaid, alerts, or emoji shortcodes
- [ ] GitHub file still has a quiet first screen (not a badge wall)
- [ ] Critique is specific, not "it is nice"

## Stretch

Start [projects/final-project.md](../projects/final-project.md) and map which exercise files you will reuse.
