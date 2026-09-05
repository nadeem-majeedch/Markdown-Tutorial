# Lesson 30 — Common Markdown mistakes

[← Previous Lesson](29-limitations.md) | [Course Home](../README.md) | [Next Lesson →](31-best-practices.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Recognize the errors that appear most often in student Markdown
- Fix them quickly
- Build a personal debugging checklist
- Avoid mistakes that break GitHub navigation and grading

## Conceptual explanation

Most Markdown bugs are not mysterious. They come from **whitespace**, **unclosed fences**, **wrong brackets**, and **assuming the editor is GitHub**.

When something "does not render," work through this list in order:

1. Is the file saved as `.md`?
2. Is a code fence unclosed above this line?
3. Is there a blank line between blocks?
4. Is the special character the ASCII one (`-`, `` ` ``, `*`) not a Word substitute?
5. Are you previewing the same flavor as the audience?

This lesson is a field guide. Steal the examples for office hours.

## Syntax: broken vs fixed

### 1. Unclosed fence

Broken:

````markdown
```python
print("hello")

# The rest of the README is stuck in the code block
````

Fixed: add the closing `` ``` ``.

### 2. No space after heading hashes

Broken: `#Title`

Fixed: `# Title`

### 3. No space after list marker

Broken: `-item`

Fixed: `- item`

### 4. Link brackets reversed

Broken: `(Python)[https://python.org]`

Fixed: `[Python](https://python.org)`

### 5. Space between link parts

Broken: `[Python] (https://python.org)`

Fixed: `[Python](https://python.org)`

### 6. Missing `!` on images

Broken: `[plot](fig.png)` (shows a text link)

Fixed: `![plot of residuals](fig.png)`

### 7. Table without separator

Broken:

```markdown
| A | B |
| 1 | 2 |
```

Fixed:

```markdown
| A | B |
| - | - |
| 1 | 2 |
```

### 8. Trailing-space line breaks deleted by the editor

Broken: two spaces, then the formatter trims them.

Fixed: use a backslash break or a paragraph.

### 9. Nested list with one space

Broken:

```markdown
- parent
 - child
```

Fixed: indent the child with 2–4 spaces consistently (4 recommended).

### 10. `---` turning into a heading

Broken:

```markdown
Results
---
We won.
```

Fixed:

```markdown
## Results

We won.
```

## Beginner example

A student writes:

```markdown
#Lab 1
We used python.
-numpy
-pandas
See (docs)[https://pandas.pydata.org]
```

**Problems:** heading space, list spaces, reversed link, `python` could be inline code.

**Fixed:**

```markdown
# Lab 1

We used `python`.

- `numpy`
- `pandas`

See [Pandas documentation](https://pandas.pydata.org)
```

**Expected rendered result**

A real H1, a paragraph, a bullet list, a working link.

## Intermediate example: README that swallows itself

````markdown
## Install

```bash
pip install catboost
# forgot to close

## Usage

This heading is still inside the bash fence.
````

**Fix:** close the fence before the next heading. If GitHub shows a giant code block, scroll up until you find the unmatched opener.

## Advanced example: flavor confusion

The file uses:

```markdown
==highlight==

Term
: definition

> [!NOTE]
> Secret exam hint
```

On GitHub: no highlight, no definition list, alert works.

On Pandoc: definition list may work, GitHub alerts may not.

**Fix:** pick a target. For GitHub coursework: bold instead of `==`, HTML or bold glossaries, alerts only if the TA views on GitHub.

### Unicode lookalikes

| Intended | Dangerous lookalike |
|----------|---------------------|
| `-` hyphen-minus | `–` en dash, `•` bullet |
| `` ` `` | `'` apostrophe, `‘` |
| `*` | `∗` asterisk operator |
| `"` | `“` `”` |

Paste into a plain-text editor. If a list will not parse, delete the bullet and type `- `.

## Common mistakes (meta)

- Fixing the wrong problem (adding HTML) when a blank line would suffice
- Not looking at the GitHub preview tab before submitting
- Copying Slack Markdown (different rules) into a README
- Leaving `lorem ipsum` and `TODO` in a graded README

## Best practices

- Preview before every push
- Turn on visible whitespace when debugging
- Keep a snippet file of "known good" heading/list/link/table/fence examples
- Prefer backticks over italics for identifiers so underscores survive
- Close fences immediately after opening them, then fill the middle

## Practical use cases

- Office hours debugging
- TA grading checklists
- Open-source "your README is a code block" issues
- Converting Word lab reports to Markdown

## Practice exercises

1. Break a file with an unclosed fence, preview, then repair it.
2. Correct a reversed link and a heading without a space.
3. Paste a list from a website and retype the markers as ASCII `- `.
4. Build a 6-item personal debugging checklist and keep it in `notes.md`.

## Quick review

- Fences, blank lines, and ASCII characters cause most failures
- Headings and lists need a space after the marker
- Links are `[text](url)` — not the reverse
- Tables need a hyphen separator row
- Preview on the renderer your reader will use

---

[← Previous Lesson](29-limitations.md) | [Course Home](../README.md) | [Next Lesson →](31-best-practices.md)
