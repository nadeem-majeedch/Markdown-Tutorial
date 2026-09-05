# Lesson 29 — Limitations and portability

[← Previous Lesson](28-github-pages.md) | [Course Home](../README.md) | [Next Lesson →](30-common-mistakes.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- List things Markdown cannot do well
- Rank features from portable to GitHub-only
- Write a portability policy for a project
- Convert or fall back when a renderer is weaker
- Avoid lock-in to a single preview tool

## Conceptual explanation

Markdown's strength is simplicity. That is also its ceiling.

It will not give you:

- Precise print layout (margins, running headers, float placement like LaTeX)
- Full application UI (forms, authenticated dashboards)
- Guaranteed identical rendering everywhere
- Built-in bibliography management as strong as BibTeX
- Spreadsheet formulas
- Comments/suggestion mode like Google Docs (unless a tool adds it)

**Portability** means a file still makes sense when opened in another program. The more GFM and GitHub extras you use, the better it looks on GitHub and the worse it may look in a strict parser, an LMS, or a printed handout.

## A portability ladder

| Level | Features | Survivability |
|-------|----------|----------------|
| 1 | Headings, paragraphs, emphasis, lists, links, images, fenced code | Almost everywhere |
| 2 | GFM tables, strikethrough, task lists, autolinks | GitHub, many modern tools |
| 3 | Footnotes, HTML subset | GFM / HTML-friendly tools |
| 4 | Math, Mermaid, alerts, mentions, wiki syntax | Specific products |
| 5 | MDX, shortcodes, embed widgets | One generator only |

This course taught levels 1–4. For a syllabus PDF that must print, stay near level 1–2 and export with Pandoc.

## Syntax: documenting your target

Put a note in CONTRIBUTING or README:

```markdown
## Markdown dialect

Documentation is GitHub-Flavored Markdown, rendered on github.com.
Mermaid diagrams require GitHub or a Mermaid-capable preview.
```

That single section prevents "it looks broken in Word" bug reports.

## Beginner example: portable versus pretty

Portable:

```markdown
**Warning:** Do not train on the test set.
```

Pretty on GitHub only:

```markdown
> [!WARNING]
> Do not train on the test set.
```

Both are valid. If the file is also pasted into an LMS, the first one is safer.

## Intermediate example: a conversion workflow

```text
notes.md  →  Pandoc  →  notes.pdf
README.md →  GitHub  →  HTML
```

Pandoc command (for you to run locally when needed):

```bash
pandoc REPORT.md -o REPORT.pdf
```

GFM tables often survive. Mermaid usually does not unless you add a filter. Plan figure exports for PDF.

## Advanced example: feature budget

An expert README might allow:

- Tables, badges, relative links, fences (yes)
- One Mermaid architecture diagram (yes, with a PNG fallback in `assets/`)
- Alerts (optional)
- `@mentions` (no, except CHANGELOG credits)

An expert journal supplement might allow:

- Math and tables (yes)
- Task lists (no)
- HTML `<details>` (no — poor in print)

### What Markdown is bad at, with alternatives

| Need | Instead of stretching Markdown |
|------|--------------------------------|
| Complex equations + cross-refs | LaTeX or Quarto |
| Collaborative comments | Google Docs, then export |
| Huge tables | CSV + notebook |
| Designed slides | Marp, reveal.js, or PowerPoint |
| Legal contracts with numbering schemes | Dedicated tools or DOCX templates |

## Common mistakes

- Building a course website that only works in Typora
- Using four flavors in four folders with no note
- Assuming "it previewed in VS Code" equals "the TA's GitHub view matches"
- Embedding binary Office documents in Git "just in case" *instead of* Markdown, then never updating the Markdown
- Unicode look-alike characters (`*` vs `∗`) that break parsing

## Best practices

- Default to CommonMark + GFM tables
- Isolate non-portable features (math, mermaid) in files whose audience is GitHub
- Provide fallbacks (PNG, Unicode, extra sentence)
- Test at least two renderers for anything graded or published
- Never require a paid editor to read student submissions

## Practical use cases

- Multi-institution course notes
- Open-source docs read on GitHub, GitLab, and the web
- Exporting labs to PDF for archival
- Sending README content to a non-technical manager in email

## Practice exercises

1. Classify ten features from this course onto the portability ladder.
2. Rewrite a GitHub alert as portable bold **Warning:** text.
3. Export a small Markdown file to HTML using your editor and compare tables.
4. Write a three-line dialect statement for a capstone repo.

## Quick review

- Markdown is limited on purpose
- Portability drops as flavor-specific features rise
- State your dialect
- Give fallbacks for math, diagrams, and alerts
- Test more than one renderer

---

[← Previous Lesson](28-github-pages.md) | [Course Home](../README.md) | [Next Lesson →](30-common-mistakes.md)
