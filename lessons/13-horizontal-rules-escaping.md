# Lesson 13 — Horizontal rules and escaping characters

[← Previous Lesson](12-code.md) | [Course Home](../README.md) | [Next Lesson →](14-tables.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Insert a horizontal rule (thematic break)
- Escape a Markdown special character with a backslash
- Show literal `*`, `_`, `#`, `` ` ``, and `[]()` when you need them
- Choose escaping versus inline code
- Avoid accidental thematic breaks from `---` in prose

## Conceptual explanation

Two small tools complete the core syntax:

1. **Horizontal rules** divide a page into scenes. They become HTML `<hr>`.
2. **Escaping** tells the parser "this character is literal, not syntax."

You need escaping whenever you write about Markdown, mathematics with asterisks, or Windows paths, or when a character would otherwise start a list or emphasis.

## Syntax: horizontal rules

A line that is only hyphens, asterisks, or underscores — at least three — becomes a rule:

```markdown
---

***

___
```

Spaces between the characters are allowed in CommonMark (`- - -`).

### Syntax explanation

- The line should be a block of its own (blank lines around it are safest).
- `---` on a line by itself is a rule. `---` under a paragraph can be a Setext H2 underline (Lesson 04). Context matters.
- GitHub renders a thin full-width line.

Use rules rarely. Headings already divide sections. A rule is appropriate between very different parts of one file (for example, lesson body vs navigation), or in a resume-style README.

## Syntax: escaping

Prefix a special character with `\`:

```markdown
\*this is not italic\*

\# This is not a heading

1\. This is not a numbered list
```

Characters that are commonly escaped:

| Character | Why escape |
|-----------|------------|
| `\*` `\_` | Avoid emphasis |
| `\#` | Avoid headings |
| `\+` `\-` | Avoid lists or rules |
| `` \` `` | Avoid code spans (or use extra backticks) |
| `\[` `\]` `\(` `\)` | Avoid links |
| `\\` | A literal backslash |
| `\!` | Avoid an image |
| `\|` | Avoid table cells in GFM |

You do **not** need to escape letters, digits, or ordinary punctuation such as `. , ?`.

### Escaping versus code

If the literal text is an identifier or a snippet, **backticks are better than backslashes**:

```markdown
The glob pattern is `*.md`, not \*.md.
```

Inside a fenced code block, almost nothing needs escaping. Fences already treat content as literal.

## Beginner example

**Source**

```markdown
Part one: theory.

---

Part two: experiment.
```

**Expected rendered result**

Two short paragraphs separated by a horizontal line.

**Source**

```markdown
Use \*stars\* for italic in Markdown.
```

**Expected rendered result**

The sentence: Use \*stars\* for italic in Markdown. (asterisks visible, no italic)

## Intermediate example: teaching syntax without breaking the page

```markdown
A heading starts with `#` plus a space. Type `\#` if you need a hash
at the start of a line in prose.

Multiply by 2 with an asterisk in math-like prose: 3 \* 2 = 6.
Better: write `3 * 2 = 6` or use a math block later.
```

**Expected rendered result**

Readable teaching prose. The first hash in backticks is safest. The multiplication example shows why code spans beat a forest of backslashes.

## Advanced example: accidental Setext headings and YAML

This source is a trap:

```markdown
Conclusion
---

We failed to reject the null hypothesis.
```

Many parsers treat `Conclusion` plus `---` as an **H2 heading**, not as a title and a rule. Fix it with a blank line and a longer rule, or use `***`, or make `Conclusion` a real ATX heading:

```markdown
## Conclusion

We failed to reject the null hypothesis.
```

Another trap: files that start with YAML front matter for Jekyll/GitHub Pages:

```markdown
---
title: Lab 5
---
```

That is **not** a horizontal rule. It is metadata (Lesson 28). Ordinary lesson content should not begin with a lone `---` unless you intend front matter.

### Windows paths

```markdown
Bad: `C:\new\test` can look like escapes.

Better: `C:\\new\\test` in prose, or always use backticks:
`C:\new\test` inside inline code, where backslashes are safer.
```

Inside inline code, backslashes are mostly literal, but be careful with a trailing backslash before the closing backtick. Prefer forward slashes in documentation: `C:/new/test`.

## Common mistakes

- Using a horizontal rule after every heading. Visual noise.
- Writing `--` (en dash style) and getting a rule or a heading underline.
- Escaping characters inside code fences where it is unnecessary.
- Forgetting that `---` after a one-line paragraph can become H2.
- Escaping too much: `hello\.` is pointless.

## Best practices

- Prefer headings over horizontal rules for structure.
- Prefer inline code over backslash escaping for technical tokens.
- Put blank lines around `---`.
- Use `***` if you need a rule and want to avoid Setext collisions.
- Escape only the character that would otherwise parse specially.

## Practical use cases

- **Lesson pages:** a rule above the previous/next navigation (as in this course)
- **README:** a rule before license text (optional; a heading is clearer)
- **Cheat sheets:** literal syntax shown with escapes or fences
- **Math-ish notes:** `\*` until you switch to LaTeX (Lesson 20)

## Practice exercises

1. Insert a horizontal rule between two paragraphs and preview it.
2. Write a sentence that shows the characters `*italic*` literally, using backslashes.
3. Show the same characters using inline code instead. Which source is easier to read?
4. Type a one-word paragraph, then `---` on the next line, then another paragraph. Did you get a heading? Fix it with ATX syntax.

## Quick review

- Thematic break: `---` or `***` or `___` on its own line
- Escape with `\`
- Code spans and fences are often better than escaping
- `---` after a short line can be an H2 underline, not a rule

---

[← Previous Lesson](12-code.md) | [Course Home](../README.md) | [Next Lesson →](14-tables.md)
