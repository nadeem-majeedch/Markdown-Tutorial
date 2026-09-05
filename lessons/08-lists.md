# Lesson 08 — Ordered and unordered lists

[← Previous Lesson](07-blockquotes.md) | [Course Home](../README.md) | [Next Lesson →](09-nested-lists.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write bullet (unordered) lists
- Write numbered (ordered) lists
- Choose markers that render consistently
- Control tight versus loose lists
- Use lists for procedures, inventories, and ranking

## Conceptual explanation

Lists turn a sequence of items into a structure readers can scan. Markdown supports:

- **Unordered lists** — items where order is not essential (dependencies, features, materials)
- **Ordered lists** — items where order *is* essential (install steps, experimental procedure, ranked results)

The parser looks for a **list marker**, a space, and then the item text. Consecutive item lines form one list. A blank line between items can make the list "loose" (each item wrapped in a paragraph, with extra spacing).

## Syntax

### Unordered lists

```markdown
- alpha
- beta
- gamma
```

Equivalent markers:

```markdown
* alpha
* beta

+ alpha
+ beta
```

### Ordered lists

```markdown
1. Clone the repository
2. Create a virtual environment
3. Install requirements
```

CommonMark also accepts:

```markdown
1. First
1. Second
1. Third
```

and

```markdown
3. Starts at three
4. Continues
```

GitHub numbers ordered lists from the first number you write. Starting at `1.` is the usual style.

### Syntax explanation

- Put a space after `-`, `*`, `+`, or `1.`.
- `-item` is not a list item.
- You may indent wrapped lines of a long item so the text aligns with the text above it.
- Markers `-`, `*`, and `+` are interchangeable; pick one style per document. This course uses `-`.
- Ordered-list markers are digits plus `.` (or `)` in CommonMark: `1)`). Prefer `1.` for GitHub.

## Beginner example

**Source**

```markdown
Shopping list for the electronics lab:

- jumper wires
- breadboard
- 220 Ω resistors
```

**Expected rendered result**

A sentence, then three bullets with a disc (or similar) marker.

**Source**

```markdown
1. Open the notebook
2. Restart the kernel
3. Run all cells
```

**Expected rendered result**

A numbered list 1, 2, 3.

## Intermediate example: tight vs loose

**Tight list** (no blank lines between items):

```markdown
- Train set: 70%
- Validation set: 15%
- Test set: 15%
```

Renders compactly.

**Loose list** (blank lines between items):

```markdown
- Train set: 70%

- Validation set: 15%

- Test set: 15%
```

Renders with extra vertical space. Use loose lists when items contain multiple paragraphs.

**Multi-paragraph item:**

```markdown
- **Preprocessing.** Normalize pixel values to the range [0, 1].

  Do this before augmentation so noise is on the same scale.

- **Augmentation.** Apply random flips and small rotations.
```

The continuation line is indented so it stays in the same item.

## Advanced example: procedures in a lab report

```markdown
## Procedure

1. Weigh 2.0 g of tea leaves.
2. Add 20 mL of hot water at 80 °C.
3. Steep for 10 minutes.
4. Extract with 10 mL of dichloromethane.
5. Dry the organic layer over sodium sulfate.

Materials used:

- tea leaves (Lipton, black)
- dichloromethane (ACS grade)
- sodium sulfate, anhydrous
```

**Expected rendered result**

A numbered procedure (order matters) and a bullet inventory (order does not). Mixing both types on one page is normal and useful.

### Numbering strategy for Git

If you write:

```markdown
1. Install Python
1. Install Git
1. Clone the repo
```

GitHub still shows 1, 2, 3. The advantage: inserting a step does not force you to renumber every later item in the source. Many documentation teams use all `1.` markers for that reason. Other teams prefer true 1, 2, 3 in the source so the raw file reads well. Both are valid GFM/CommonMark.

## Common mistakes

- Missing space after the marker.
- Mixing `-` and `*` randomly in the same list (works, looks sloppy).
- Using `1)` in a document that will be rendered by an older tool that only accepts `1.`.
- Putting a heading immediately after a list without a blank line.
- Writing a 20-item ordered list when the order does not matter. Use bullets.
- Using lists for entire paragraphs of narrative. If items are long essays, consider headings.

## Best practices

- Use `-` for bullets and `1.` for numbered steps, consistently.
- Tight lists for short items; loose lists for multi-paragraph items.
- Start ordered lists at 1 unless you are continuing a truncated sequence on purpose.
- Indent wrapped text to the text column, not to column 0.
- Prefer lists over a comma-separated blob when there are three or more items a reader might scan.

## Practical use cases

- **README install section:** ordered list of commands
- **Machine-learning paper notes:** bullet list of hyperparameters
- **Course syllabus:** numbered weekly topics
- **Bug report:** numbered reproduction steps (GitHub issues love this)

## Practice exercises

1. Convert this sentence into a bullet list: "The stack includes Python, FastAPI, PostgreSQL, and Docker."
2. Write a 4-step ordered list for making tea or compiling a program.
3. Create a loose list where each item has a bold title and a second sentence.
4. Rewrite a numbered list using only `1.` markers. Confirm GitHub still shows 1, 2, 3.

## Quick review

- Unordered: `- item` (or `*` / `+`)
- Ordered: `1. item`
- Space after the marker is required
- Blank lines between items make a loose list
- Use numbered lists only when sequence matters

---

[← Previous Lesson](07-blockquotes.md) | [Course Home](../README.md) | [Next Lesson →](09-nested-lists.md)
