# Lesson 01 — Introduction to Markdown

[Course Home](../README.md) | [Next Lesson →](02-what-is-markdown.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Explain what this course covers and how it is organized
- Describe what a Markdown file is
- Open, edit, and preview a `.md` file
- Recognize the difference between *source* and *rendered* Markdown
- Know which tools you need for the rest of the course

## Why start here

Markdown is the writing format of GitHub, most software documentation, many research notebooks, and a large share of university course notes. If you can write Markdown, you can:

- Publish a project on GitHub that other people can actually understand
- Keep lecture notes that stay readable years later
- Write lab reports that mix prose, code, tables, and equations
- Contribute to open-source documentation

This first lesson is orientation. You will not memorize syntax yet. You will understand the *workflow*: write plain text, save a `.md` file, and let a renderer turn it into formatted output.

## What is a Markdown file?

A Markdown file is an ordinary text file with a `.md` or `.markdown` extension.

It looks like this in an editor:

```markdown
# Lab 3: Linear Regression

We fit a model of the form **y = mx + b**.

- Dataset: `housing.csv`
- Language: Python
```

The same file, rendered on GitHub or in a preview pane, looks like this:

---

**Rendered result**

# Lab 3: Linear Regression

We fit a model of the form **y = mx + b**.

- Dataset: `housing.csv`
- Language: Python

---

Nothing magical happened. Characters such as `#`, `**`, `` ` ``, and `-` are instructions to the renderer. If you open the file in Notepad, you still see the source. If you open it on GitHub, you see the formatted page.

That dual nature is the whole idea:

| You write | The renderer shows |
|-----------|--------------------|
| Plain text with a few symbols | Headings, lists, links, code, tables |
| A file you can `git diff` | A page humans can read |

## How this course is structured

The course moves in four stages:

1. **Beginner** — headings, paragraphs, emphasis, lists, links, images, code
2. **Intermediate** — tables, task lists, HTML, footnotes, math, diagrams
3. **Advanced** — GitHub-Flavored Markdown, READMEs, docs, academic writing
4. **Expert** — portability, accessibility, professional patterns, a final project

Every lesson uses the same pattern:

- A short explanation of the *idea*
- The *syntax*
- Why that syntax exists
- A beginner example, then a harder one
- Mistakes students actually make
- A few practice exercises
- Links to the previous and next page

Do not skip the early lessons even if they look simple. Later GitHub and documentation pages assume you already understand headings, links, and code fences.

## Source versus rendered output

Keep this distinction in mind for every later lesson.

**Source** is what you type:

```markdown
Visit the [course home](../README.md).
```

**Rendered output** is what readers see:

Visit the course home (as a clickable link).

When this course shows an example, it will usually present:

1. A fenced code block containing the Markdown source
2. A short description or recreation of the rendered result

You are expected to type the source yourself and preview it.

## Tools you can use

You only need a text editor. These options all work:

| Tool | Best for | Notes |
|------|----------|--------|
| GitHub web editor | Editing files in a repository | Preview tab is built in |
| Visual Studio Code | Daily coursework | Install the Markdown preview |
| Obsidian / Typora | Notes and long writing | Live preview |
| Jupyter / Quarto | Data science notebooks | Mixes Markdown and code |
| Any plain-text editor | Learning the syntax | Preview elsewhere |

For this course, VS Code or the GitHub web editor is enough.

### Minimal workflow

1. Create a file named `notes.md`
2. Type a heading: `# Week 1 Notes`
3. Save the file
4. Preview it (VS Code: open the preview pane; GitHub: open the file in the repo)

If you see a large title that says "Week 1 Notes", Markdown is working.

## Beginner example

Create `hello.md` with this source:

```markdown
# Hello, Markdown

This is my first Markdown file.

I am taking a course on **technical writing with Markdown**.
```

**Expected rendered result**

- A top-level heading: Hello, Markdown
- A normal paragraph
- The phrase "technical writing with Markdown" in bold

## Intermediate example

A short course-note fragment:

```markdown
# CS 101 — Week 2

## Agenda

1. Recap of variables
2. Functions
3. Homework Q&A

Read the [Python tutorial](https://docs.python.org/3/tutorial/) before lab.
```

**Expected rendered result**

- A main title and a second-level heading
- A numbered list with three items
- A blue, clickable link labeled "Python tutorial"

You do not need to understand every symbol yet. Notice that the file is still readable even *before* it is rendered. That is one of Markdown's design goals.

## Common mistakes

- Saving the file as `.txt` and wondering why GitHub does not format it. Use `.md`.
- Writing in Microsoft Word and exporting to Markdown without checking the result. Word adds extra markup. Start in a plain-text editor.
- Confusing Markdown with HTML or LaTeX. Markdown is simpler. You will learn how it can *include* HTML and math later.
- Trying to learn every flavor on day one. Stick to CommonMark basics first.

## Best practices

- One idea per lesson file while you are learning; one topic per heading later.
- Preview often. Markdown errors are usually missing blank lines or unclosed fences.
- Keep source readable. If the raw file is ugly, the rendered page will be hard to maintain.
- Put course files in a Git repository from the start if you can. Markdown and Git work well together.

## Practical use cases

| Context | Typical file |
|---------|----------------|
| GitHub project | `README.md` |
| Lab notebook | `lab-04-sorting.md` |
| Lecture notes | `week-07-trees.md` |
| Assignment write-up | `homework-2.md` |
| Team wiki | `docs/onboarding.md` |

## Practice exercises

1. Create a file named `about-me.md` with your name as a heading and two sentences about your major.
2. Preview the file in your editor or on GitHub. Confirm the heading is larger than the paragraph.
3. Add a second heading called `Goals` and list (in ordinary sentences, not a list yet) one thing you want to learn from this course.
4. Open this lesson's source on GitHub or in your clone and find the navigation links at the top and bottom. Click **Next Lesson** when you are ready.

## Quick review

- Markdown is plain text with lightweight formatting marks.
- Files usually end in `.md`.
- You always work with *source*; readers usually see *rendered* output.
- This course is page-by-page. Follow the next-lesson links.
- You do not need special software beyond a text editor and a preview.

---

[Course Home](../README.md) | [Next Lesson →](02-what-is-markdown.md)
