# Lesson 32 — Accessibility and readable documentation

[← Previous Lesson](31-best-practices.md) | [Course Home](../README.md) | [Next Lesson →](33-advanced-markdown.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Explain why Markdown accessibility matters
- Write headings, links, and alt text that work with screen readers
- Avoid conveying meaning with color or emoji alone
- Structure documents for cognitive load and mobile reading
- Check a page with a short accessibility checklist

## Conceptual explanation

**Accessible documentation** can be used by people who:

- Listen with a screen reader
- Navigate by keyboard
- Magnify the page
- Read on a small phone
- Are not native speakers of the document language
- Are tired, stressed, or new to the subject (that is most students the night before a deadline)

Markdown helps because it encourages real headings and lists instead of fake visual styling. Markdown hurts when authors write "click here", skip heading levels, omit alt text, or paste screenshots of words.

GitHub's rendered HTML inherits your structure. If the outline is correct, assistive tech gets a map.

## Syntax that affects accessibility

### Headings as structure

```markdown
# Document title
## Section
### Subsection
```

Do not fake headings with `**Big bold line**`. Screen readers skip those when users browse by heading.

### Descriptive links

```markdown
Bad: [click here](install.md)
Good: [Installation guide](install.md)
```

### Alt text

```markdown
Bad: ![image](plot.png)
Good: ![Scatter plot of predicted versus true hospital stay length](plot.png)
```

If the figure is explained fully in the next paragraph, alt text can be shorter, but it should not be empty unless the image is decorative.

### Tables

Header rows are required so column meaning is announced:

```markdown
| Metric | Train | Test |
| ------ | ----: | ---: |
```

Do not use tables for page layout (two-column "design").

## Beginner example

**Source**

```markdown
# Lab safety

Read the [lab safety manual](safety.md) before the first session.

![Fire extinguisher location near door B](figures/extinguisher.png)
```

**Expected rendered result**

A real title, a link that makes sense out of context, an image that still communicates if unseen.

## Intermediate example: do not rely on color or icons

Inaccessible:

```markdown
- Red items are required
- Green items are optional
```

(without any non-color cue)

Better:

```markdown
- **Required:** helmet
- **Optional:** extra notebook
```

Inaccessible status table that uses only emoji:

```markdown
| Test | Status |
| ---- | ------ |
```

with cells containing only a colored circle.

Better: `Pass` and `Fail` words, optional extra icon.

## Advanced example: cognitive load and language

````markdown
## Install (Windows, macOS, Linux)

You need Python 3.12. Then run:

```bash
pip install -r requirements.txt
```

If `pip` is not found, see [Troubleshooting pip](faq.md#pip).
````

Accessible writing techniques:

- Short sentences
- One instruction per step
- Define acronyms on first use: "Random access memory (RAM)"
- Avoid unexplained jargon
- Put the expected result after a command ("You should see `Successfully installed`")
- Do not autoplay GIFs that flash (GitHub still lets you embed busy images)

### `<details>` and hidden content

Collapsible HTML can hide required instructions. Do not put safety or grading-critical steps only inside `<details>`. Hints and optional logs are fine.

### Language attribute

GitHub README cannot set `lang` easily per repo page. For GitHub Pages, the theme's HTML `lang` should match the course language. For multi-language docs, use separate files: `README.md`, `README.es.md`.

## Common mistakes

- Heading text that is a whole paragraph
- Link text `here`, `this`, `link`
- Empty alt or filename alt
- Screenshots of code instead of fences (cannot copy, hard to hear)
- Tiny low-contrast images of terminal text
- Skipping H2 so the outline jumps
- Tables used as a two-column brochure

## Best practices

- Real headings, in order, unique
- Links name their destination
- Alt text describes the information in the figure
- Words, not only color or emoji, carry meaning
- Code as text
- Plain language
- Test with tab navigation on the Pages site if you publish one
- Caption figures in visible prose as well as alt text for academic work

## Practical use cases

- Public course notes
- Open-source READMEs with a global audience
- Lab safety docs
- Government or university-facing project pages

## Practice exercises

1. Rewrite three `click here` sentences from any website as descriptive Markdown links.
2. Write alt text for a confusion-matrix figure without using the word "image."
3. Convert a color-only legend into word-based labels.
4. Run through the checklist below on Lesson 24's examples.

## Accessibility checklist

- [ ] One H1, no skipped levels
- [ ] Link text makes sense alone
- [ ] Images have useful alt text
- [ ] Tables have headers
- [ ] Meaning is not color-only
- [ ] Code is in fences, not pictures
- [ ] Critical instructions are not hidden
- [ ] Language is as plain as the topic allows

## Quick review

- Structure is accessibility
- Headings, links, and alt text do most of the work
- Do not hide meaning in color, emoji, or screenshots
- Write short, explicit steps
- Checklists catch regressions

---

[← Previous Lesson](31-best-practices.md) | [Course Home](../README.md) | [Next Lesson →](33-advanced-markdown.md)
