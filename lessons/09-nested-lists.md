# Lesson 09 — Nested lists

[← Previous Lesson](08-lists.md) | [Course Home](../README.md) | [Next Lesson →](10-links.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Nest lists two or three levels deep
- Mix ordered and unordered lists
- Include paragraphs, code, and quotes inside a list item
- Indent consistently so GitHub parses the nest
- Avoid the indentation bugs that break student READMEs

## Conceptual explanation

A **nested list** is a list that lives inside another list item. You create it by indenting the inner markers so the parser sees them as children, not as a new top-level list.

Nesting is how you express hierarchy:

```text
Week 4
  ├── Lecture
  │     ├── Trees
  │     └── Heaps
  └── Lab
        └── Implement a binary heap
```

Markdown does not use tree-drawing characters. It uses indentation.

### How much to indent?

CommonMark's rule is subtle: the inner list should be indented to align with the content of the parent item (often 2 or 4 spaces). **On GitHub, two or more spaces usually work; four spaces is the safest habit.**

This course recommends:

- 2 spaces if your team already uses that style and previews on GitHub
- **4 spaces** when you want maximum compatibility and clearer nesting

Never mix tabs and spaces.

## Syntax

```markdown
- Parent
    - Child
    - Child
- Next parent
```

Mixed types:

```markdown
1. First major step
    - detail A
    - detail B
2. Second major step
    1. sub-step
    2. sub-step
```

### Syntax explanation

- The child line starts with whitespace, then a list marker, then a space, then text.
- The child belongs to the nearest parent item above it at a smaller indent.
- You can nest ordered inside unordered and the reverse.
- A list item can contain other blocks if those blocks are indented to the item's content column.

## Beginner example

**Source**

```markdown
- Fruit
    - apple
    - banana
- Vegetables
    - carrot
    - spinach
```

**Expected rendered result**

Two top-level bullets. Under Fruit, two inner bullets. Under Vegetables, two inner bullets.

If the inner items do not indent far enough, GitHub may show one flat list of six items.

## Intermediate example: a lab checklist outline

```markdown
1. Data preparation
    1. Download `iris.csv`
    2. Check for missing values
    3. Stratified split
        - train: 60%
        - validation: 20%
        - test: 20%
2. Baseline model
    - logistic regression
    - dummy classifier
3. Report
    - confusion matrix
    - F1 score
```

**Expected rendered result**

A numbered spine with mixed inner bullets and a third-level split under step 1.3.

## Advanced example: content inside items

A list item can hold a paragraph, a code block, and a nested list if indentation is consistent.

````markdown
1. Create the environment

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install packages

    - `numpy`
    - `pandas`
    - `scikit-learn`

    Pin versions in `requirements.txt`.

3. Run the tests

    ```bash
    pytest -q
    ```
````

**Expected rendered result**

Three numbered steps. Step 1 contains a highlighted shell block. Step 2 contains bullets and a following sentence still inside item 2. Step 3 contains another code block.

The fenced code is indented so it belongs to the list item. If you start the fence at column 0, you may break the list.

**GitHub indentation tip:** indent the contents of a list item by at least 4 spaces (or one tab) relative to the marker. Indent nested fences with the item.

### How deep should you go?

Two levels are easy to read. Three is acceptable. Four or more usually means you need headings instead of lists.

## Common mistakes

- Indenting with 1 space. GitHub may not nest the list.
- Mixing tabs on one line and spaces on the next.
- Outdenting too early, which "closes" the parent list.
- Putting a code fence at column 0 in the middle of a list.
- Nested lists without a parent item (orphan children).
- Using nested lists to draw an organizational chart. Consider a Mermaid diagram (Lesson 21) for true graphs.

## Best practices

- Prefer 4-space indent per nested level while you are learning.
- Preview on GitHub, not only in a chat app.
- Keep nested items short.
- Promote a nested list to headings if it becomes a mini-document.
- When a list item contains a fence, indent the entire fence.

## Practical use cases

- **Syllabus:** week → topics → readings
- **ML experiments:** model → hyperparameters → values tried
- **Software README:** install step → OS-specific substeps
- **Research protocol:** phase → tasks → responsible person

## Practice exercises

1. Recreate a two-level campus map list: campuses as parents, buildings as children.
2. Write an ordered procedure with unordered materials nested under step 1.
3. Put a one-line `code` fence inside a list item and preview it. If the list breaks, increase indent.
4. Take a four-level nested list and rewrite it using headings plus two-level lists. Which is easier to read?

## Quick review

- Nest by indenting child markers (4 spaces is a safe default).
- Ordered and unordered lists can mix.
- Other blocks can live in an item if they are indented.
- If nesting fails, the indent is usually too small or inconsistent.

---

[← Previous Lesson](08-lists.md) | [Course Home](../README.md) | [Next Lesson →](10-links.md)
