# Lesson 02 — What is Markdown and why use it?

[← Previous Lesson](01-introduction.md) | [Course Home](../README.md) | [Next Lesson →](03-basic-syntax.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Define Markdown in one sentence
- Explain why Markdown is popular on GitHub and in academia
- Distinguish Markdown, HTML, LaTeX, and rich-text formats such as Word
- Name the major Markdown *flavors* and why they matter
- Decide when Markdown is the right tool

## Conceptual explanation

Markdown is a lightweight markup language. **Markup** means you add a small number of characters to plain text to describe structure: this is a heading, this is a list, this is a link.

John Gruber created Markdown in 2004 with two goals:

1. The source should be readable as-is, even if it is never rendered.
2. The source should convert cleanly to HTML.

Those two goals explain almost every design choice you will meet in this course. A heading is `# Title` rather than `<h1>Title</h1>` because a human can still read `# Title` in a terminal, a diff, or an email.

### A one-sentence definition

**Markdown is plain text with a small, readable syntax that renderers turn into formatted documents.**

## Why students and engineers use it

| Need | How Markdown helps |
|------|--------------------|
| Version control | The file is text, so `git diff` shows real edits, not a binary blob |
| Portability | The same `.md` file opens in GitHub, VS Code, Jupyter, Obsidian, and many static-site generators |
| Speed | Faster to type than Word or HTML for notes, READMEs, and docs |
| Code + prose | Fenced code blocks make programming and data-science write-ups natural |
| Collaboration | Pull requests can review documentation the same way they review code |
| Publishing | GitHub Pages, MkDocs, Quarto, and Jekyll all accept Markdown |

Compare three ways to write the same sentence:

**Word / Google Docs** — stored as a complex document; hard to diff; formatting can break when you paste.

**HTML**

```html
<h1>Neural Networks</h1>
<p>A <strong>perceptron</strong> is a linear classifier.</p>
```

Correct, but noisy for notes.

**Markdown**

```markdown
# Neural Networks

A **perceptron** is a linear classifier.
```

Same structure, less ceremony.

## Markdown is not a programming language

Markdown has no variables, loops, or runtime. It is a *document format*. A **renderer** (GitHub, Pandoc, VS Code, Jekyll) reads your file and produces HTML, PDF, or a preview.

That means:

- There is no single official program named "Markdown" that you must install.
- Different renderers can disagree on edge cases.
- You should write for a *target renderer* (this course's default target is GitHub) while staying as portable as possible.

Lesson 29 covers portability in depth. For now, remember: **syntax that GitHub understands is not automatically universal.**

## Flavors you will meet

"Markdown" is a family, not one frozen spec.

| Flavor | Where you see it | Notes |
|--------|------------------|--------|
| Original Markdown | Gruber's 2004 syntax | The ancestor |
| CommonMark | Many modern parsers | A stricter, unambiguous spec |
| GitHub-Flavored Markdown (GFM) | GitHub, much of this course | Tables, task lists, strikethrough, autolinks |
| Pandoc Markdown | Academic conversion to PDF/DOCX | Extra features for scholars |
| GitHub Pages / Jekyll | Project websites | GFM plus site templates |

This course teaches **CommonMark basics first**, then **GFM**, then features that only some tools support (math, Mermaid, definition lists, highlights).

Whenever a feature is not universal, the lesson will say so.

## Beginner example

Suppose you email a teammate:

```text
Meeting notes
We decided to use Python 3.12.
Please review chapter 4.
```

In Markdown, you add just enough structure to make a document:

```markdown
# Meeting notes

We decided to use **Python 3.12**.

Please review [chapter 4](https://docs.python.org/3/tutorial/).
```

**Expected rendered result**

- A clear title
- The language name in bold
- A working link

The file is still understandable if the email client never renders it.

## Intermediate example

Why Markdown beats a Word file for a programming course:

```markdown
# Assignment 2 — Recursion

## Goal

Implement `factorial(n)` and measure stack depth.

## Constraints

- Language: Python 3
- No loops in `factorial`
- Submit `factorial.py` and this write-up

## Result

On `n = 1000` the function reached the default recursion limit.
```

A grader reading this on GitHub sees headings and a list. A `git log` of the same file shows exactly which sentences you changed before the deadline.

## Advanced example: choosing the format

| Document | Recommended format | Why |
|----------|--------------------|-----|
| GitHub README | Markdown (GFM) | Native rendering |
| Two-page lab report with a few equations | Markdown + math, or Quarto | Fast, versionable |
| Journal article with complex floats | LaTeX | Fine-grained typesetting |
| Collaborative policy memo for non-technical staff | Google Docs or Word | Comments and track changes |
| API reference for a library | Markdown in `docs/` | Lives next to the code |

Markdown is the default for software and a strong default for student STEM writing. It is not always the best tool for heavily designed print layouts.

## Common mistakes

- Treating Markdown as "HTML without tags." Some HTML works inside Markdown (Lesson 16), but Markdown has its own rules for paragraphs, lists, and code.
- Assuming one preview equals all previews. VS Code, GitHub, and Pandoc can differ.
- Converting a thesis to Markdown at the last minute. Choose the format at the start of a project.
- Embedding huge binary content. Markdown files should stay text; store images separately.

## Best practices

- Write Markdown when the document must live in Git or on GitHub.
- Prefer portable syntax (headings, lists, links, code) unless you need a GFM-only feature.
- Name the target: "This README is written for GitHub."
- Keep the source pleasant to read. If you need three layers of HTML to force a layout, you may be using the wrong tool.

## Practical use cases

- **Programming:** README, changelog, issue comments, pull request descriptions
- **Data science:** notebook markdown cells, experiment logs, model cards
- **Research:** annotated bibliographies, lab notebooks, preprint notes
- **Teaching:** syllabi, assignment sheets, solution write-ups
- **Teams:** onboarding docs, design decisions, meeting notes

## Practice exercises

1. In one or two sentences, write your own definition of Markdown. Then compare it with the definition in this lesson.
2. List three files in your degree program that would be better as `.md` than as `.docx`, and one file that should stay in Word or LaTeX.
3. Open any public GitHub repository and find its `README.md`. Identify one heading, one link, and one code fragment.
4. Explain to a classmate why `git diff` is more useful on a Markdown file than on a Word file.

## Quick review

- Markdown is readable plain text that renderers turn into formatted documents.
- It exists to be easier than HTML and more version-control-friendly than Word.
- Several flavors exist; this course targets GitHub after teaching the shared core.
- Choose Markdown for docs, notes, and repos; choose LaTeX or Word when you need their strengths.

---

[← Previous Lesson](01-introduction.md) | [Course Home](../README.md) | [Next Lesson →](03-basic-syntax.md)
