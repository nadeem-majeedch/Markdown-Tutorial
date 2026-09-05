# Exercise set 5 — README and documentation

**Level:** Advanced  
**Lessons:** [24](../lessons/24-readme-files.md)–[28](../lessons/28-github-pages.md)

[← Previous set](04-intermediate-gfm.md) | [Exercises home](README.md) | [Course Home](../README.md) | [Next set →](06-expert.md)

---

## Goals

You will not yet build the full final project. You will draft the **information architecture** and two real pages.

Create:

```text
exercises/work/mini-docs/
  README.md
  docs/index.md
  docs/usage.md
  CHANGELOG.md
```

Invent a tiny tool (for example `csvcut`, `labtimer`, or `notefold`).

## Exercises

### 1. README first screen

`README.md` must include, in order:

1. H1 name
2. One-sentence pitch
3. Features (3 bullets)
4. Requirements
5. Installation fence
6. Quick start fence
7. Links to `docs/usage.md`, `CHANGELOG.md`, and the course [LICENSE](../LICENSE) or a local license note

### 2. Docs index

`docs/index.md` lists tutorial vs how-to vs reference in one short list of links. Even if some pages do not exist, **do not** add broken links: only link files you created. Extra pages can be listed as plain text "planned."

### 3. Usage how-to

`docs/usage.md` follows:

- Goal
- Steps (numbered)
- Expected result
- Next (link back to README)

Use a relative link: `[README](../README.md)`.

### 4. Changelog

One version `0.1.0` with Added and Fixed subsections.

### 5. Navigation

Add previous/home/next style links between `docs/index.md` and `docs/usage.md`.

### 6. Pages thinking

Write a comment at the bottom of README (as a Markdown paragraph, not HTML) answering:

- Would you publish this from repo root or from `/docs`?
- What is in `_config.yml` of *this course* (open the real file)?

### 7. Honesty pass

Delete any section that you cannot support with a real command. Empty "Tests" sections are worse than omitted ones.

## Self-check

- [ ] Every relative link points at a file you created
- [ ] README quick start is copyable
- [ ] Changelog uses past-tense, factual bullets
- [ ] No secrets, no `localhost` as the only URL

## Stretch

Add `CONTRIBUTING.md` with four bullets a classmate could follow.
