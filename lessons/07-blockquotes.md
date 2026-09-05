# Lesson 07 — Blockquotes

[← Previous Lesson](06-text-formatting.md) | [Course Home](../README.md) | [Next Lesson →](08-lists.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Quote a passage with `>`
- Nest blockquotes
- Mix quotes with lists and emphasis
- Attribute a quotation in a readable way
- Decide when a quote is better than a callout or a code block

## Conceptual explanation

A **blockquote** marks text that comes from somewhere else, or that should be visually set apart as a cited or highlighted passage. In HTML it becomes `<blockquote>`.

In student work, blockquotes are useful for:

- Citing a paper, textbook, or lecture
- Repeating an assignment constraint in a lab report
- Email-style nested replies in a design discussion
- A motto or epigraph at the top of a notes file

They are *not* the best tool for warnings on GitHub (use alerts in Lesson 23) or for source code (use code fences in Lesson 12).

## Syntax

```markdown
> This is a blockquote.
```

Multi-paragraph quote:

```markdown
> First paragraph of the quote.
>
> Second paragraph of the quote.
```

Nested quote:

```markdown
> Outer quote
>
> > Nested quote
```

### Syntax explanation

- `>` at the start of the line (optional space after `>`) begins a quote.
- Continue `>` on every line of the quoted block, including "empty" quoted lines that are just `>`.
- A line without `>` ends the quote.
- Inline Markdown (emphasis, links, inline code) works inside quotes.
- Nested `>` characters add quote levels.

## Beginner example

**Source**

```markdown
> Markdown is not a replacement for HTML, or for anything else.
>
> — John Gruber
```

**Expected rendered result**

A indented, often left-bordered paragraph, followed by an attribution line inside the same quote.

## Intermediate example: quoting a paper in course notes

```markdown
# Bias-variance tradeoff

Bishop summarizes the tension between model flexibility and generalization:

> A model which is too simple will underfit the data, whereas a model
> which is too complex will overfit.
>
> — Christopher M. Bishop, *Pattern Recognition and Machine Learning*

We will measure both training error and validation error in Lab 5.
```

**Expected rendered result**

Section heading, intro sentence, a distinct quoted block, then your own commentary as a normal paragraph. The commentary is *not* quoted because those lines do not start with `>`.

## Advanced example: nested discussion and mixed content

```markdown
> ### Reviewer 2
>
> The authors should compare against a linear baseline.
>
> > **Authors:** We added logistic regression in Table 3.
>
> Please also report 95% confidence intervals.
>
> 1. Interval for accuracy
> 2. Interval for F1
```

**Expected rendered result**

- A quote that contains a heading, a nested reply, and a list
- Nested quotes usually appear with a stronger indent or a second bar

This pattern appears in email archives and in Markdown discussions. For GitHub code review, inline comments are usually better than quoting entire threads in a README.

### When not to quote

| Want | Use |
|------|-----|
| Copied source code | Fenced code block |
| A warning to the reader | Bold **Note:** or a GitHub alert |
| A definition you wrote | Normal paragraph or a definition list |
| Long excerpt from a copyrighted book | Short fair-use quote plus citation; do not paste chapters |

## Common mistakes

- Forgetting `>` on continuation lines, which leaks the quote back into the main document.
- Using blockquotes to indent text for layout. Markdown is not CSS.
- Quoting code with `>` instead of fences. You lose syntax highlighting.
- Nested quotes five levels deep. Readers get lost.
- No blank line after the quote, so the next heading or list fails to parse.

## Best practices

- Keep quotes short. Link to the source for the rest.
- Put attribution on its own line inside or immediately after the quote.
- Use `>` on every line, including blank quoted lines.
- Do not fake callouts with quotes in a GitHub README if you can use [alerts](23-github-markdown.md).
- Cite properly in academic work; a blockquote is formatting, not a bibliography entry.

## Practical use cases

- **Course notes:** excerpt a definition from the textbook, then explain it in your own words
- **Literature review:** one-sentence quotes with page numbers
- **Design docs:** quote a requirement from the spec
- **CHANGELOG:** quote a breaking-change warning from an upstream library

## Practice exercises

1. Quote a single sentence from a course syllabus and attribute the instructor.
2. Write a two-paragraph quote using `>` on the blank line between paragraphs.
3. Nest a one-line reply inside a quote.
4. Take a five-line Python snippet and compare quoting it with `>` versus putting it in a code fence. Which is appropriate?

## Quick review

- `>` starts a blockquote.
- Keep `>` on every line of the quoted block.
- Nest with additional `>` characters.
- Quotes are for cited or set-apart prose, not for code or layout.

---

[← Previous Lesson](06-text-formatting.md) | [Course Home](../README.md) | [Next Lesson →](08-lists.md)
