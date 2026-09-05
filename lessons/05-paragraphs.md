# Lesson 05 — Paragraphs and line breaks

[← Previous Lesson](04-headings.md) | [Course Home](../README.md) | [Next Lesson →](06-text-formatting.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write paragraphs that render as separate blocks
- Control line wrapping versus a true line break
- Explain why pressing Enter once often does *not* start a new paragraph
- Choose a line-break style that works on GitHub
- Format poetry, addresses, and signed names when you need hard breaks

## Conceptual explanation

In a word processor, Enter starts a new paragraph. In Markdown, **a single newline is usually just wrapping**. A **blank line** (two newlines in a row) starts a new paragraph.

This design lets you wrap source lines at 80 columns without producing a choppy rendered page. It surprises every beginner once.

There are three related ideas:

| Idea | How you type it | What readers see |
|------|-----------------|------------------|
| Paragraph | One or more consecutive lines, then a blank line | A block of prose with a gap after it |
| Soft wrap | A single Enter in the source | Usually *no* break in the output |
| Hard line break | A special marker at the end of a line | A new line inside the same paragraph |

## Syntax

### Paragraphs

```markdown
This is paragraph one. It can wrap
across several source lines.

This is paragraph two. It starts after a blank line.
```

### Hard line breaks — two common styles

**Standard Markdown:** end a line with two or more spaces, then Enter.

```markdown
Department of Computer Science··
State University
```

(The `·` characters represent spaces. They are invisible, which is why this method is error-prone.)

**CommonMark also allows a backslash break** (supported on GitHub):

```markdown
Department of Computer Science\
State University
```

### Syntax explanation

- Consecutive non-blank lines merge into one paragraph.
- A completely empty line ends the paragraph.
- Two trailing spaces or a trailing `\` insert `<br>` — a line break without starting a new paragraph (no extra vertical gap, or only a small one, depending on CSS).

## Beginner example

**Source**

```markdown
Gradient descent updates parameters in the direction
that reduces the loss.

The learning rate controls the size of each step.
```

**Expected rendered result**

Two separate paragraphs. The line wrap after "direction" disappears in the output; "that reduces the loss." continues the first paragraph.

If you intended two short lines stacked (like an address), this is *not* enough. Use a hard break.

## Intermediate example: a lab header

```markdown
**Student:** A. Rivera\
**Date:** 12 March 2026\
**Course:** CHEM 220 — Organic Chemistry I

This report describes the extraction of caffeine from tea leaves.
```

**Expected rendered result**

Three stacked header lines, then a gap, then the report paragraph.

The backslash style is visible in the source, so teammates can see the break. Trailing spaces are easy to delete by accident.

## Advanced example: wrapping strategy for Git

Some teams wrap Markdown at 80 characters:

```markdown
Recurrent neural networks process sequences by passing a hidden
state from one time step to the next.  That design is powerful,
but long-range dependencies remain difficult without gating.
```

Others use one sentence per line (useful for `git diff`):

```markdown
Recurrent neural networks process sequences by passing a hidden state from one time step to the next.
That design is powerful, but long-range dependencies remain difficult without gating.
```

Both render as one paragraph if there is **no blank line** between sentences in the first style, and as two paragraphs in the second style because each sentence is followed by a newline... wait: in the second style, each sentence is on its own line *without* a blank line, so they still merge into **one paragraph**.

To get two paragraphs, you need:

```markdown
Recurrent neural networks process sequences by passing a hidden state from one time step to the next.

That design is powerful, but long-range dependencies remain difficult without gating.
```

**GitHub note:** GitHub treats a single newline inside a paragraph as a space (CommonMark). Some "Markdown extra" chat tools treat every newline as a `<br>`. Do not assume Slack rules apply to `README.md`.

## Common mistakes

- Hitting Enter once and expecting a new paragraph.
- Using trailing spaces for breaks, then having an editor "trim trailing whitespace" on save. The breaks vanish.
- Inserting `<br>` everywhere. Occasional HTML is fine (Lesson 16); it is not needed for ordinary prose.
- Blank lines *inside* a paragraph by accident, which splits one thought into two.
- Writing huge walls of text with no paragraph breaks. Headings and paragraphs should chunk the page.

## Best practices

- Separate ideas with blank lines.
- Prefer `\` hard breaks when you need stacked short lines, or use a list instead.
- Do not fight the paragraph model to fake a poster layout.
- For addresses, poems, or lyrics, hard breaks or a preformatted block are appropriate.
- Let long paragraphs wrap in the preview; do not sprinkle `<br>` at visual line endings.

## Practical use cases

- **Abstracts and papers:** one paragraph per idea; blank lines between them
- **README intro:** two or three short paragraphs under the H1
- **Lab cover block:** name, date, partner stacked with `\`
- **Commit / PR descriptions:** blank lines between summary and details

## Practice exercises

1. Write three sentences as one paragraph (wrap them in the source). Confirm they render as a single block.
2. Split the same three sentences into three paragraphs using blank lines.
3. Create a three-line "from" address using backslash breaks.
4. Enable "trim trailing whitespace" in your editor. Why is the two-space break style risky?

## Quick review

- Blank line = new paragraph.
- Single Enter usually does not break the rendered line.
- Hard breaks: trailing `\` (recommended) or two spaces (fragile).
- GitHub follows CommonMark paragraph rules, not chat-app rules.

---

[← Previous Lesson](04-headings.md) | [Course Home](../README.md) | [Next Lesson →](06-text-formatting.md)
