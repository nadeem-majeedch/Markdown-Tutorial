# Lesson 24 — Markdown for README files

[← Previous Lesson](23-github-markdown.md) | [Course Home](../README.md) | [Next Lesson →](25-documentation.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Explain what a README is for
- Structure a student or open-source README
- Write install, usage, and citation sections
- Avoid the common README anti-patterns
- Use GFM features that help first-time visitors

## Conceptual explanation

`README.md` is the front door of a GitHub repository. GitHub renders it on the repo home page. People decide in a few seconds whether they can use your project.

A good README answers, in order:

1. What is this?
2. Why should I care?
3. How do I get it running?
4. How do I use it?
5. Where do I go next (docs, issues, license, citation)?

It is **not** your entire documentation, your lab notebook, or a private diary. Link to those.

## Syntax and structure

There is no special README syntax — only conventions.

Recommended skeleton:

```markdown
# project-name

One sentence pitch.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

## Requirements

## Installation

## Quick start

## Usage

## Project structure

## Tests

## Contributing

## Citation

## License
```

Use only the sections you need. A four-file homework repo does not need a contributing guide if the course forbids collaboration — but it still needs **what**, **how to run**, and **how it was evaluated**.

## Beginner example: homework repository

````markdown
# CS201 Homework 4 — Dijkstra

Implementation of Dijkstra's algorithm on an adjacency list.

## Run

```bash
python dijkstra.py --input graphs/small.txt
```

## Files

- `dijkstra.py` — algorithm
- `graphs/` — sample inputs
- `REPORT.md` — write-up
````

**Expected rendered result**

A title, a pitch, a copyable command, a file map. A grader can run it without guessing.

## Intermediate example: data-science project

````markdown
# whale-song-classifier

CNN baseline for classifying whale calls in hydrophone clips.

## Dataset

Place `clips/` in this directory. The data are **not** stored in Git.
See `data/README.md` for license and download steps.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Train

```bash
python train.py --epochs 10 --seed 0
```

Expected baseline accuracy is about 0.84 on the held-out test split.

## Reproducibility

- Python 3.12
- Seed `0` for the reported run
- GPU optional
````

**Expected rendered result**

A stranger (or your future self during finals) can reproduce the experiment.

## Advanced example: open-source library README

Include:

- Badges (CI, license, version)
- TOC for long pages (Lesson 17)
- A 10-line usage snippet that actually works
- Link to full docs
- Citation bib snippet for academic software

````markdown
# tinyknn

A tiny k-nearest-neighbors classifier for teaching.

## Table of contents

- [Install](#install)
- [Quick start](#quick-start)
- [Citation](#citation)

## Install

```bash
pip install tinyknn
```

## Quick start

```python
from tinyknn import KNN
model = KNN(k=3)
model.fit(X_train, y_train)
y_hat = model.predict(X_test)
```

## Citation

If you use this in coursework, cite the repository URL and version tag.
````

### What not to put in README

- Passwords, tokens, private data
- 200 lines of raw logs (use `<details>` or `docs/`)
- Broken relative links to files you never committed
- "TODO: write this" as the entire install section
- Screenshots of code instead of fences

## Common mistakes

- Project named `untitled` with an empty README (GitHub's default text).
- Install commands that only work on the author's laptop (`C:\Users\Sam\...`).
- No example input, so the program errors immediately.
- Features list that does not match the code.
- License section that contradicts the `LICENSE` file.

## Best practices

- Write the README on the same day you create the repo.
- Put a working command in **Quick start** and run it when you change the CLI.
- Use relative links to `LICENSE`, `docs/`, `CONTRIBUTING.md`.
- Keep the first screenful useful without scrolling past a huge badge wall.
- Update the README in the same PR as behavior changes.
- For academic work, say how to reproduce tables and figures.

## Practical use cases

- Every GitHub repo you submit for a course
- Capstone and internship projects
- Internal team tools
- Dataset repositories (`data/README.md` explaining columns)

## Practice exercises

1. Write a README skeleton for a fictional Python package `csvcut`.
2. Add a `bash` install block and a 5-line usage block.
3. Add a Features bullet list of three items.
4. Link `LICENSE` and a `docs/usage.md` page (create the links even if you will add files in the final project).
5. Cut any sentence that does not help a first-time visitor.

## Quick review

- README = what, why, how to run, where next
- GFM is welcome: tables, tasks, badges, alerts
- Show copyable commands and honest requirements
- Keep secrets and giant logs out
- Update the README when the project changes

---

[← Previous Lesson](23-github-markdown.md) | [Course Home](../README.md) | [Next Lesson →](25-documentation.md)
