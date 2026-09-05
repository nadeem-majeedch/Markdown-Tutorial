# Frequently asked questions

[Course Home](../README.md) | [Cheat sheet](cheat-sheet.md) | [References](references.md)

---

## Getting started

### Do I need to install Markdown?

No. Markdown is a text format. You need an editor and a renderer (GitHub, VS Code preview, Typora, Pandoc, and others).

### What file extension should I use?

`.md` is the standard. `.markdown` also works. GitHub READMEs must be named `README.md` (case may matter on some systems).

### Is Markdown a programming language?

No. There are no variables or loops. A renderer turns the text into HTML or another output format.

### Which flavor does this course teach?

Core CommonMark first, then GitHub-Flavored Markdown, then GitHub product features and other renderer-dependent extras. Each lesson labels non-portable syntax.

---

## Syntax problems

### Why did my whole file become a code block?

An opening fence `` ``` `` was never closed. Add a closing fence, or remove a stray opener.

### Why is my heading not large?

You need a space: `# Title`, not `#Title`. Also check that the line is not inside a fence or HTML block.

### Why did Enter not start a new paragraph?

Markdown merges single newlines into one paragraph. Insert a blank line.

### Why is my list not a list?

Put a space after the marker: `- item`. Use an ASCII hyphen, not a Word bullet. Put a blank line before the list if it follows a paragraph.

### Why is my nested list flat?

Indent children more (try four spaces). Do not mix tabs and spaces.

### Why is my table raw pipes?

Tables are GFM. The renderer may be strict CommonMark. Add the hyphen separator row if it is missing.

### Why does `---` make a heading?

A short line followed by `---` is a Setext H2. Use `## Heading` or put a blank line and use `***` as a rule.

### How do I show a backtick?

Use double backticks around a space-padded backtick: `` `` ` `` ``. Inside fences, backticks are easier.

### How do I write a star without italic?

Escape `\*` or wrap in code `` `*` ``.

---

## GitHub

### Does GitHub support math and Mermaid?

On github.com, Markdown files commonly support `$` / `$$` math and `mermaid` fences. This is a product feature, not original Markdown. Always preview.

### Why do `@mentions` not notify in a README?

Notifications are for issues, pull requests, and similar discussions. A README mention may still link a profile without pinging. Do not use mentions as decoration.

### Can I style my README with CSS?

Generally no. GitHub sanitizes HTML and ignores most CSS in README files. GitHub Pages sites can use theme CSS.

### Why does my Pages site differ from the repo file view?

Jekyll/kramdown and the GitHub comment renderer are not the same pipeline. Test both. Relative links and GFM extras are the usual differences.

### Should I use `main` or `master` for Pages?

Use whatever default branch the repository has. This course repository may use `master`. New GitHub repos often use `main`.

---

## Academic work

### Can I submit a Markdown lab report?

If your instructor accepts it, yes. Ask whether they want `.md`, PDF (via Pandoc/Quarto), or a notebook. Include figures as files, not only screenshots of your desktop.

### How do I cite sources?

Short labs: a References list or GFM footnotes. Papers: BibTeX/Zotero with Quarto, Pandoc, or LaTeX. Follow the department style (APA, IEEE, ACM, Nature, …).

### Is Markdown enough for a thesis?

Usually not by itself. Use Quarto or LaTeX for numbering, floats, and bibliographies. Markdown is excellent for notes and supplementary repos.

---

## Tools

### VS Code versus GitHub preview

They are close, not identical. Trust GitHub for work that will be graded or viewed there.

### Should I use Typora / Obsidian?

They are excellent for notes. They add features (`==highlight==`, wikilinks). If the submission target is GitHub, preview on GitHub before you turn in the file.

### What about Jupyter?

Notebook Markdown cells use a similar language plus math. The `.ipynb` JSON wrapper is not a plain `.md` file. For a clean repo, export important narrative to `REPORT.md`.

### How do I convert to PDF?

Pandoc and Quarto are the usual tools. Install them locally; they are not required to complete this course.

---

## Course logistics

### Do I have to complete every exercise?

The lesson-end drills are the minimum. Exercise sets 1–6 add volume. The [final project](../projects/final-project.md) is the capstone.

### Can I use this course in my class?

Yes. It is MIT licensed. See [LICENSE](../LICENSE) and [CONTRIBUTING.md](../CONTRIBUTING.md).

### Where do I go next after the cheat sheet?

Build the final project, then write README files for every repository you already have.

---

[Course Home](../README.md) | [Cheat sheet](cheat-sheet.md) | [References](references.md)
