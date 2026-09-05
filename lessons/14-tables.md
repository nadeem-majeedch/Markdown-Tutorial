# Lesson 14 — Tables

[← Previous Lesson](13-horizontal-rules-escaping.md) | [Course Home](../README.md) | [Next Lesson →](15-task-lists.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write a GitHub-Flavored Markdown table
- Align columns left, right, or center
- Put inline code, links, and emphasis inside cells
- Know the limits: no merged cells, awkward wrapping, wide data
- Choose a table versus a list versus a CSV file

## Conceptual explanation

Tables display rectangular data: columns with names, rows with values. They are perfect for hyperparameters, grading rubrics, command cheat sheets, and small experimental results.

**Important:** tables are **not** in original Markdown. They are part of **GitHub-Flavored Markdown (GFM)** and many other modern flavors (Pandoc, most static-site generators). A strict CommonMark parser may show the raw pipes.

On GitHub, tables render as HTML `<table>` elements with header styling.

Markdown tables cannot:

- Merge cells
- Set column widths precisely
- Nested tables
- Multi-paragraph cells comfortably

For a large dataset, keep a `.csv` and show only a summary table in Markdown.

## Syntax

```markdown
| Column A | Column B | Column C |
| -------- | -------- | -------- |
| a1       | b1       | c1       |
| a2       | b2       | c2       |
```

Alignment colons in the separator row:

```markdown
| Left     | Center   | Right |
| :------- | :------: | ----: |
| text     | text     |  12.0 |
```

### Syntax explanation

- Row 1 is the header.
- Row 2 is the **separator**. It must contain hyphens. Colons control alignment.
- Later rows are data.
- Leading and trailing `|` are conventional and recommended.
- Extra spaces inside cells are ignored (they pad the source for readability).
- Inline Markdown works in cells: `` `code` ``, `**bold**`, `[links](url)`.
- A pipe character inside a cell must be escaped: `\|`

GFM does not require the source columns to line up, but aligned source is easier to edit.

## Beginner example

**Source**

```markdown
| Language | Extension |
| -------- | --------- |
| Python   | `.py`     |
| R        | `.R`      |
| Julia    | `.jl`     |
```

**Expected rendered result (GFM)**

A two-column table with a header row. Language names on the left, file extensions in code style.

Without GFM, the reader would see the pipe characters as text.

## Intermediate example: experiment log

```markdown
| Run | Model              | Accuracy | Notes                    |
| --: | :----------------- | -------: | :----------------------- |
|   1 | logistic regression|    0.812 | baseline                 |
|   2 | random forest      |    0.874 | `n_estimators=200`       |
|   3 | SVM, RBF kernel    |    0.861 | slow to train            |
```

**Expected rendered result**

Numeric columns right-aligned, text left-aligned. The header stays visible while you scan numbers.

This is the standard way to report a small student experiment in a README or lab notebook.

## Advanced example: mixed inline content and limits

```markdown
| Topic        | Resource | Status |
| ------------ | -------- | :----: |
| Gradient descent | [Lecture 4](../lectures/04.md) | done |
| Regularization   | [Bishop ch. 3](https://www.microsoft.com/en-us/research/people/cmbishop/) | reading |
| Backprop         | `notebooks/backprop.ipynb` | todo |
```

**What you cannot do portably**

```markdown
<!-- Not GFM: rowspan/colspan in pure Markdown pipes -->
```

If you need merged headers, use HTML `<table>` (Lesson 16) and accept that some Markdown linters will complain, or split into two tables.

### Wide tables

GitHub scrolls wide tables horizontally on small screens. Still:

- Keep 4–7 columns when you can
- Abbreviate header names
- Move extra fields into a nested list under the table
- For 50+ rows, link to CSV or a notebook instead of pasting them all

### Lists versus tables

| Use a list | Use a table |
|------------|-------------|
| Sequence of steps | Several attributes per item |
| Uneven item length | Comparable rows |
| Hierarchy (nesting) | A matrix of values |

## Common mistakes

- Forgetting the separator row. Then GitHub does not make a table.
- Separator without enough hyphens. Use at least three `---` per column.
- Unescaped `|` inside a cell.
- Inconsistent column counts across rows.
- Assuming alignment works in every tool. It is GFM.
- Pasting Excel cells and getting tabs instead of pipes. Convert properly.
- Putting block elements (fences, lists) inside a cell. GFM cells are inline-oriented.

## Best practices

- Always include a header and a separator.
- Align the *source* for your future self, even if the parser does not require it.
- Right-align numbers; left-align text.
- Use inline code for identifiers in cells.
- Label units in the header: `Accuracy (%)`, `Time (s)`.
- Mark tables as GFM in your mind: they may not render on an old forum.

## Practical use cases

- **README:** compatibility matrix (OS × Python version)
- **ML:** hyperparameter grid, ablation results
- **Course:** grading rubric
- **Lab:** measured volumes and yields
- **API docs:** status codes and meanings

## Practice exercises

1. Make a 3×3 table of your weekly timetable (day, task, hours).
2. Right-align a column of numbers.
3. Add a column that contains inline code.
4. Add a column that contains a link.
5. Export three rows from a spreadsheet mentally into pipe syntax. Check that every row has the same number of cells.

## Quick review

- GFM tables: header, hyphen separator, data rows
- Colons in the separator set alignment
- Inline Markdown is allowed in cells
- No merged cells in pure GFM
- Not original Markdown — GitHub and other GFM tools only (plus similar flavors)

---

[← Previous Lesson](13-horizontal-rules-escaping.md) | [Course Home](../README.md) | [Next Lesson →](15-task-lists.md)
