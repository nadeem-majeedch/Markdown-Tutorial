# Markdown Language Tutorial

A complete, self-contained Markdown course for university students. Start with zero experience and finish able to write professional GitHub READMEs, software documentation, course notes, lab reports, and technical papers.

This course is designed to be studied **page by page**. Every lesson includes objectives, explanations, worked examples, common mistakes, practice exercises, and navigation to the previous and next lesson.

---

## Who this course is for

- Students who have never written Markdown
- Computer science, data science, and engineering students who need GitHub READMEs
- Researchers who want cleaner lab notes, papers, and reports
- Anyone who wants documentation that is portable, version-controlled, and easy to maintain

No programming background is required for the first half of the course. Later lessons use examples from programming, data science, machine learning, and academic writing, but every concept is explained before it is used.

## Prerequisites

- A web browser
- A GitHub account (free) for later lessons
- A plain-text editor such as VS Code, or the GitHub web editor
- Optional: [Typora](https://typora.io/), [Obsidian](https://obsidian.md/), or another Markdown preview editor

You do **not** need to install a compiler or a special Markdown runtime. Markdown is plain text.

## How to use this course

1. Read lessons in order. Later pages assume earlier pages.
2. Type the examples yourself. Do not only read them.
3. Complete the practice exercises at the end of each lesson.
4. Use the [cheat sheet](resources/cheat-sheet.md) as a quick reference after you finish a topic.
5. Complete the [final project](projects/final-project.md) when you reach the end.

Each lesson shows:

1. The Markdown **source**
2. What the **rendered result** looks like

Features that work in every CommonMark/Markdown processor are taught first. Features that work only on GitHub, GitHub Pages, or specific tools are labeled:

- **Standard Markdown** — works in almost every renderer
- **GitHub-Flavored Markdown (GFM)** — works on GitHub and many modern tools
- **Renderer-dependent** — works only where the tool explicitly supports it

## Learning roadmap

```text
Beginner          Intermediate         Advanced            Expert
---------         -------------        --------            ------
What Markdown is  Tables               GFM                 Professional docs
Basic rules       Task lists           GitHub features     GitHub Pages
Headings          HTML in Markdown     Math / LaTeX        Accessibility
Paragraphs        Internal links       Mermaid diagrams    Portability
Text formatting   Footnotes            Advanced patterns   Final project
Lists             Definition lists     README design
Links and images  Emojis
Code blocks
```

Estimated study time:

| Path | Lessons | Time |
|------|---------|------|
| Beginner core | 01–09 | 4–6 hours |
| Intermediate | 10–15 | 3–4 hours |
| Advanced | 16–20 | 3–4 hours |
| Professional practice | 21–26 | 4–6 hours |
| Exercises and final project | exercises + project | 4–8 hours |
| **Full course** | **all** | **about 20–28 hours** |

---

## Course contents

A compact index also lives in [lessons/README.md](lessons/README.md).

### Part 1 — Foundations (Beginner)

Start here if you have never used Markdown.

| # | Lesson | What you will learn |
|---|--------|---------------------|
| 01 | [Introduction to Markdown](lessons/01-introduction.md) | What this course covers and how Markdown fits into student work |
| 02 | [What is Markdown and why use it?](lessons/02-what-is-markdown.md) | History, plain text, renderers, and why Markdown beat heavier formats |
| 03 | [Syntax and basic rules](lessons/03-basic-syntax.md) | How Markdown parsers think, whitespace, and the core grammar |
| 04 | [Headings](lessons/04-headings.md) | ATX and Setext headings, hierarchy, and document outline |
| 05 | [Paragraphs and line breaks](lessons/05-paragraphs.md) | Paragraphs, hard breaks, blank lines, and wrapping |
| 06 | [Text formatting](lessons/06-text-formatting.md) | Bold, italic, strikethrough, highlight, combination |
| 07 | [Blockquotes](lessons/07-blockquotes.md) | Quotes, nested quotes, and attributed excerpts |
| 08 | [Lists](lessons/08-lists.md) | Ordered lists, unordered lists, and tight vs loose lists |
| 09 | [Nested lists](lessons/09-nested-lists.md) | Indentation, mixed list types, and nested content |

### Part 2 — Core documents (Beginner to Intermediate)

| # | Lesson | What you will learn |
|---|--------|---------------------|
| 10 | [Links](lessons/10-links.md) | Inline, reference, autolinks, and titles |
| 11 | [Images](lessons/11-images.md) | Images, alt text, and clickable image links |
| 12 | [Code](lessons/12-code.md) | Inline code, fenced blocks, and syntax highlighting |
| 13 | [Horizontal rules and escaping](lessons/13-horizontal-rules-escaping.md) | Thematic breaks and how to show literal Markdown characters |
| 14 | [Tables](lessons/14-tables.md) | GFM tables, alignment, and wide data |
| 15 | [Task lists](lessons/15-task-lists.md) | Checklists for issues, labs, and project tracking |

### Part 3 — Extended Markdown (Intermediate)

| # | Lesson | What you will learn |
|---|--------|---------------------|
| 16 | [HTML inside Markdown](lessons/16-html.md) | When HTML is allowed, when it is stripped, and safe use |
| 17 | [Anchors and internal links](lessons/17-internal-links.md) | Heading IDs, table of contents, and in-page navigation |
| 18 | [Footnotes and definition lists](lessons/18-footnotes.md) | Academic notes, glossaries, and renderer support |
| 19 | [Emojis](lessons/19-emojis.md) | Unicode emoji and GitHub shortcodes |
| 20 | [Mathematical equations](lessons/20-math.md) | LaTeX-style math on GitHub and in documentation tools |
| 21 | [Mermaid diagrams](lessons/21-mermaid.md) | Flowcharts, sequence diagrams, and class diagrams |

### Part 4 — GitHub and professional writing (Advanced)

| # | Lesson | What you will learn |
|---|--------|---------------------|
| 22 | [GitHub-Flavored Markdown](lessons/22-gfm.md) | The GFM spec and what GitHub actually renders |
| 23 | [GitHub-specific Markdown](lessons/23-github-markdown.md) | Mentions, issues, alerts, badges, and repo conventions |
| 24 | [Markdown for README files](lessons/24-readme-files.md) | Structure, badges, install steps, and project first impressions |
| 25 | [Markdown for documentation](lessons/25-documentation.md) | Docs sites, wikis, and long-form software docs |
| 26 | [Academic notes, labs, and reports](lessons/26-academic-notes.md) | Course notes, lab reports, and technical writing |
| 27 | [Project documentation](lessons/27-project-documentation.md) | CONTRIBUTING, CHANGELOG, ADRs, and team docs |
| 28 | [Markdown with GitHub Pages](lessons/28-github-pages.md) | Publishing this course (or your own) as a website |

### Part 5 — Expert practice (Expert)

| # | Lesson | What you will learn |
|---|--------|---------------------|
| 29 | [Limitations and portability](lessons/29-limitations.md) | What Markdown cannot do and how to stay portable |
| 30 | [Common mistakes](lessons/30-common-mistakes.md) | The errors students make most often, with fixes |
| 31 | [Best practices](lessons/31-best-practices.md) | Style, structure, and maintainable documents |
| 32 | [Accessibility](lessons/32-accessibility.md) | Readable, inclusive documentation |
| 33 | [Advanced techniques](lessons/33-advanced-markdown.md) | Patterns used in large docs and professional repos |
| 34 | [Professional examples](lessons/34-professional-examples.md) | Annotated real-world documents |

### Practice, project, and reference

| Resource | Purpose |
|----------|---------|
| [Exercises index](exercises/README.md) | Extra drills from beginner to expert |
| [Final project](projects/final-project.md) | Build a complete professional GitHub documentation set |
| [Cheat sheet](resources/cheat-sheet.md) | Syntax, example, and meaning on one page |
| [FAQ](resources/faq.md) | Common student questions |
| [References](resources/references.md) | Specs, tools, and further reading |

---

## Suggested weekly plan

If you are taking this as a self-paced university module:

| Week | Focus | Pages |
|------|--------|-------|
| 1 | Foundations | Lessons 01–06 |
| 2 | Structure and media | Lessons 07–12 |
| 3 | Data and extended syntax | Lessons 13–18 |
| 4 | Diagrams, GitHub, READMEs | Lessons 19–24 |
| 5 | Professional documentation | Lessons 25–30 |
| 6 | Polish, accessibility, project | Lessons 31–34 + final project |

---

## Repository layout

```text
.
├── README.md                 Course home (this file)
├── LICENSE                   MIT License
├── CONTRIBUTING.md           How to improve the course
├── _config.yml               GitHub Pages configuration
├── lessons/                  Numbered lesson pages
├── exercises/                Extra practice sets
├── projects/                 Final project brief and rubric
├── resources/                Cheat sheet, FAQ, references
└── assets/                   Images and static files
```

## GitHub Pages

This repository is ready to publish with GitHub Pages using the Cayman theme. See [Lesson 28](lessons/28-github-pages.md) for the full walkthrough.

Quick setup:

1. Push this repository to GitHub.
2. Open **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Select `main` (or `master`) and `/ (root)`.
5. Save. GitHub will build the site from these Markdown files.

## Student project

After you finish the lessons, complete the [final project](projects/final-project.md). You will create a realistic GitHub repository with:

- A professional `README.md`
- Contribution and license files
- A short documentation folder
- A lab-report or technical-note page
- Working relative links and a table of contents

## License
Engr. Dr. Muhammad Nadeem Majeed, Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore
This course is released under the [MIT License](LICENSE). You may use it in classes, forks, and personal study.

## Contributing

Improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

**Start the course:** [Lesson 01 — Introduction to Markdown](lessons/01-introduction.md)
