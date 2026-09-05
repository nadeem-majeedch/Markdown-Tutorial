# Lesson 26 — Academic notes, labs, and reports

[← Previous Lesson](25-documentation.md) | [Course Home](../README.md) | [Next Lesson →](27-project-documentation.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Structure course notes in Markdown
- Write a lab report that mixes prose, figures, code, and tables
- Use math, citations, and captions appropriately
- Keep notes searchable and versioned in Git
- Distinguish informal notes from a submission-quality report

## Conceptual explanation

University STEM work is mostly **prose + evidence**: claims, methods, data, code, plots, equations, references. Markdown is strong at that mix if you stay disciplined.

Use different templates for different stakes:

| Artifact | Tone | Typical extras |
|----------|------|----------------|
| Lecture notes | Informal, incomplete OK | Headings, lists, snippets |
| Lab notebook | Dated log | Checklists, raw output in fences |
| Lab report | Formal IMRaD | Figures, tables, math, references |
| Paper notes | Bibliographic | Footnotes or a reference list |

**IMRaD** = Introduction, Methods, Results, and Discussion. It maps cleanly onto H2 headings.

## Syntax patterns for academic files

Title block:

```markdown
# Extraction of caffeine from tea

**Course:** CHEM 220\
**Date:** 12 March 2026\
**Authors:** A. Rivera, B. Chen
```

Figure with caption (portable):

```markdown
![Thin-layer chromatogram of extract and caffeine standard](figures/tlc.png)

**Figure 1.** TLC plate under UV light. Spot A is the extract; spot B is the standard.
```

Equation in methods (where math is supported):

```markdown
$$
R_f = \frac{\text{distance of spot}}{\text{distance of solvent front}}
$$
```

## Beginner example: weekly notes

```markdown
# Week 8 — Hash tables

## Load factor

The average number of elements per bucket is $n / m$.

## Operations

- Insert
- Lookup
- Delete

## Exam prompt idea

Why does chaining still degrade when the hash is biased?
```

**Expected rendered result**

A scannable outline you can review before a quiz. Incomplete sentences are acceptable in *notes*. They are not acceptable in a *report*.

## Intermediate example: lab report skeleton

```markdown
# Lab 4: Linear regression on housing data

## Abstract

We fit a linear model to 506 Boston-area housing records and report
test RMSE.

## Introduction

## Methods

### Data

### Model

### Evaluation

## Results

| Split | RMSE |
| ----: | ---: |
| Train | 4.21 |
| Test  | 5.08 |

![Residuals versus fitted values](figures/residuals.png)

**Figure 1.** Residuals show mild heteroscedasticity at high fitted values.

## Discussion

## Limitations

## References

1. Harrison & Rubinfeld, 1978.
```

**Expected rendered result**

A report a TA can grade without opening your notebook. The table and figure carry the results; the discussion interprets them.

## Advanced example: from notebook to report

Jupyter and Quarto let you mix Markdown cells and code cells. Expert workflow:

1. Experiment in a notebook
2. Export or copy *cleaned* figures to `figures/`
3. Write `REPORT.md` in complete sentences
4. Put only the essential snippets in fences — not every cell
5. State seeds, versions, and commands to reproduce

Bad: submitting a 40-cell notebook with `print(df)` everywhere and no narrative.

Good: a Markdown report plus `analysis.ipynb` in an appendix folder.

### Citations

- Short lab: numbered list under References, or GFM footnotes (Lesson 18)
- Paper: BibTeX via Quarto/Pandoc, or a journal template in LaTeX
- Always include enough information to find the source (title, authors, year, URL/DOI)

Do not paste copyrighted textbook chapters into your notes repository if the repo is public.

## Common mistakes

- Methods that cannot be repeated ("we cleaned the data")
- Figures without alt text or captions
- Tables of 2,000 rows in Markdown
- Math that only renders in the author's notebook
- Informal emoji in a graded report
- File named `final_final_v3.md` instead of Git history

## Best practices

- One report file per assignment, plus `figures/`
- Write Methods so a classmate could repeat them
- Put units in table headers
- Caption every figure
- Separate notes (messy, fast) from submissions (clean, structured)
- Use Git commits as your lab timeline

## Practical use cases

- Every STEM lab with a write-up
- Reading notes for a seminar
- Capstone weekly logs
- Supplementary material for a preprint (if the journal allows Markdown/PDF)

## Practice exercises

1. Convert your last lecture into H1/H2 notes with three bullet lists.
2. Draft an IMRaD skeleton for a fictional chemistry or ML lab.
3. Add one GFM table of results and one figure caption.
4. Write a Methods paragraph that includes a `bash` or `python` command a reviewer could run.

## Quick review

- Notes can be messy; reports cannot
- IMRaD maps to headings
- Figures need alt text and captions
- Show small tables, snippets, and reproducible commands
- Match formality to the audience (you vs the grader vs the public)

---

[← Previous Lesson](25-documentation.md) | [Course Home](../README.md) | [Next Lesson →](27-project-documentation.md)
