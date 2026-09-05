# Final project — Professional GitHub documentation set

[Course Home](../README.md) | [Exercises](../exercises/README.md) | [Cheat sheet](../resources/cheat-sheet.md)

---

## Overview

Build a **complete, realistic GitHub repository documentation set** for a small software, data-science, or research project. The project may be fictional, but every command, path, and claim must be internally consistent — as if a classmate might clone it.

This is the capstone for the Markdown Language Tutorial. It is a writing and structure project, not a large coding project. A few stub files are enough.

## Learning goals

- Ship a README that answers what, why, and how in the first screen
- Connect multiple Markdown pages with working relative links
- Use GFM where it helps and stay honest about GitHub-only features
- Include an academic or technical write-up with a figure caption and a table
- Meet an accessibility minimum (headings, alt text, descriptive links)

## Time estimate

4–8 hours.

## Deliverable structure

Create a folder `projects/student-project/` (or a new GitHub repository). Required files:

```text
student-project/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── index.md
│   ├── install.md
│   └── usage.md
├── reports/
│   └── lab-or-technical-note.md
└── assets/
    └── README.md
```

You may add `SECURITY.md`, an ADR, issue templates, or extra docs pages. Do not add empty files that you do not write.

## Product constraint

Choose **one** of these briefs (or an equivalent of similar size):

1. **Teaching library** — a tiny Python/R/Java helper used in a course
2. **Data pipeline** — a script that cleans a CSV and writes a summary table
3. **ML baseline** — train a simple model and report a metric
4. **Research companion** — code and notes that accompany a short paper
5. **Course toolkit** — a documented set of lab scripts for a teaching assistant

Invent names, but keep the scope small.

## Requirements (rubric)

### A. README (25%)

Must include:

- One H1 product name
- One-sentence pitch
- Features (bullets)
- Requirements
- Installation with a language-tagged fence
- Quick start with a fence that a reader could copy
- Link to docs, contributing, changelog, license
- Optional: one badge row, one GitHub alert, a short TOC if the README is long

Must not include:

- Secrets
- "Click here"
- Unclosed fences
- Broken relative links

### B. Multi-page docs (20%)

- `docs/index.md` explains the docs map
- `docs/install.md` and `docs/usage.md` use Goal / Steps / Expected result
- Previous / Home / Next style navigation on each docs page
- All relative links resolve

### C. Project community files (15%)

- `CONTRIBUTING.md` with actual steps
- `CHANGELOG.md` with at least two versions (e.g. 0.1.0 and 0.2.0)
- `LICENSE` — MIT text is acceptable (you may copy this course's license and change the copyright line)

### D. Academic or technical note (20%)

`reports/lab-or-technical-note.md` must include:

- Title block (course or project, date, author)
- At least three heading levels used correctly (no skipped levels)
- One GFM table
- One image tag with **meaningful alt text** (a placeholder path is allowed if you describe the missing file in `assets/README.md`)
- A visible figure caption paragraph
- One blockquote or citation
- One code fence relevant to the domain
- A Limitations or Discussion heading

Math, Mermaid, and footnotes are optional. If you use them, add a one-line note that they need GitHub or another capable renderer.

### E. Accessibility and quality (10%)

- Descriptive link text
- Alt text
- Parallel list items
- No heading-level skips
- English (or your course language) in complete sentences in the report

### F. Reflection (10%)

Add `reports/reflection.md` (about 300–500 words) answering:

1. Which features are CommonMark vs GFM vs GitHub-only in your deliverable?
2. What would break if this were pasted into a CommonMark-only LMS?
3. One accessibility choice you made on purpose
4. What you would still improve

## Process

1. Sketch the outline on paper (headings only).
2. Create files empty except for H1s and navigation links. **Click every link.**
3. Fill README install/quick start first.
4. Write the technical note as if it will be graded by a TA who will not run your code blindly.
5. Run the quality checklist below.
6. Optional: enable GitHub Pages as in [Lesson 28](../lessons/28-github-pages.md).

## Quality checklist

- [ ] Every relative link points to a real file
- [ ] Every code fence is closed and has a language tag when the language is known
- [ ] README quick start matches docs/install (no contradictory commands)
- [ ] Changelog versions are dated
- [ ] Images have alt text
- [ ] No skipped heading levels
- [ ] GitHub-only syntax is optional, not required to understand the project
- [ ] No `TODO` left in rendered text
- [ ] License and README license section agree

## Stretch challenges

- Add a Mermaid architecture diagram with quoted labels and a PNG fallback sentence
- Add `.github/PULL_REQUEST_TEMPLATE.md` with a task list
- Add `adr/0001-language-choice.md`
- Publish with GitHub Pages and paste the URL into the README
- Write `README` and `docs/install.md` so a classmate reproduces a dummy result in under 10 minutes

## What "done" looks like

A stranger who completed this course can clone (or browse) your folder and:

1. Understand the project in 30 seconds
2. See how to install and run it
3. Navigate docs without 404s
4. Read a technical note with a table and a figure caption
5. Know how to contribute and what changed between versions

When you finish, return to the [course home](../README.md) or keep the [cheat sheet](../resources/cheat-sheet.md) open while you maintain the project.

---

[Course Home](../README.md) | [Exercises](../exercises/README.md) | [Cheat sheet](../resources/cheat-sheet.md)
