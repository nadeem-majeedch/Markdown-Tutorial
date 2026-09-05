# Lesson 15 — Task lists (checklists)

[← Previous Lesson](14-tables.md) | [Course Home](../README.md) | [Next Lesson →](16-html.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write checked and unchecked task items
- Use task lists in issues, pull requests, and lab plans
- Nest task items under ordinary lists
- Know that interactive checkboxes are a **GitHub** feature
- Avoid using task lists for data that is not actually a task

## Conceptual explanation

A **task list** is an unordered list whose items start with a checkbox marker. On GitHub, readers can often tick the boxes in issues and pull requests; the Markdown source updates. In a README, boxes usually render as checked or unchecked but may not be clickable depending on context.

Task lists are **GitHub-Flavored Markdown**, not original Markdown. Other tools (VS Code, many static generators) display them as checkboxes or as `[ ]` text.

They shine when the document is a **plan**:

- Assignment submission checklist
- Pre-lab setup
- Pull request completion criteria
- Research reproduction steps

They are the wrong tool for a list of facts. Use ordinary bullets for "features of the algorithm."

## Syntax

```markdown
- [ ] Unchecked item
- [x] Checked item
- [X] Also checked (capital X is fine)
```

Nested:

```markdown
- [ ] Submit the lab
    - [x] Code
    - [x] Plot
    - [ ] Written discussion
```

### Syntax explanation

- Start with a list marker (`-`, `*`, or `+`, or a number).
- Then a space, then `[ ]` or `[x]`, then a space, then the item text.
- The space inside `[ ]` is required for an empty box.
- `[x]` must not have extra spaces: `[ x ]` is unreliable.
- These are still list items, so nesting and loose/tight rules from Lessons 08–09 apply.

**GitHub:** in issues and PRs, clicking a box edits the comment. In some rendered files, boxes are read-only.

## Beginner example

**Source**

```markdown
- [x] Install Python 3.12
- [x] Clone the course repository
- [ ] Complete Lesson 15 exercises
```

**Expected rendered result (GitHub)**

Three checkboxes. The first two ticked, the third empty.

## Intermediate example: lab report gate

```markdown
## Lab 6 submission checklist

- [ ] Reproducible environment
    - [ ] `requirements.txt` is pinned
    - [ ] Random seeds are set
- [ ] Results
    - [ ] Table of accuracies
    - [ ] Confusion matrix figure with alt text
- [ ] Writing
    - [ ] Methods can be repeated by a classmate
    - [ ] Limitations paragraph included
```

**Expected rendered result**

A hierarchical checklist a student can walk through before uploading.

## Advanced example: pull request template

GitHub reads `.github/PULL_REQUEST_TEMPLATE.md`. A typical template:

```markdown
## Change summary

-

## Checklist

- [ ] Tests added or updated
- [ ] Docs updated (`README.md` and `docs/`)
- [ ] No secrets committed
- [ ] Linked an issue: Fixes #
```

When a contributor opens a PR, GitHub pre-fills this Markdown. Reviewers see progress as boxes get checked. This is one of the highest-value GFM features in software teams.

### Mixing with numbered procedures

```markdown
1. [ ] Collect 30 samples
2. [ ] Label them in `labels.csv`
3. [ ] Train the baseline
```

GitHub supports task items on ordered lists. Prefer `- [ ]` unless the sequence is essential.

## Common mistakes

- `[ ]` without a list marker. It will not become a checkbox.
- `[x]` with no spaces around it where required: `- [x]Done` can fail; use `- [x] Done`.
- Using task lists in a printed PDF workflow and expecting interactive boxes. They may print as static.
- Checking a box in a README and thinking Git will not see a change. On GitHub.com, interactive edits *are* commits/comment edits.
- Nested tasks with 1-space indent that flatten on GitHub.

## Best practices

- One action per item, starting with a verb: "Add tests", not "Tests".
- Keep the list short enough that people will actually use it.
- Put PR and issue checklists in templates so they are not forgotten.
- Do not store experimental results only as checked boxes; use tables.
- Remember portability: on a strict Markdown renderer, readers may see `- [ ]` literally.

## Practical use cases

- **Coursework:** weekly study plan
- **Research:** paper submission checklist (figures, ethics, data availability)
- **Software:** PR template, release checklist
- **ML:** "before you train" list (data license, seed, baseline, GPU budget)

## Practice exercises

1. Create a 5-item weekly planner with two items already checked.
2. Nest two subtasks under one parent task.
3. Rewrite a feature list (`- Fast`, `- Simple`) as ordinary bullets, not tasks. Why is that better?
4. Draft a 4-item PR checklist for a student team project.

## Quick review

- GFM syntax: `- [ ]` unchecked, `- [x]` checked
- Interactive on GitHub issues and pull requests
- Nest like any other list
- Use for actions, not for facts
- Not original Markdown

---

[← Previous Lesson](14-tables.md) | [Course Home](../README.md) | [Next Lesson →](16-html.md)
