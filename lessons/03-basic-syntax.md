# Lesson 03 — Markdown syntax and basic rules

[← Previous Lesson](02-what-is-markdown.md) | [Course Home](../README.md) | [Next Lesson →](04-headings.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Describe how a Markdown parser divides a file into blocks and inlines
- Use blank lines to separate block elements
- Recognize characters that have special meaning
- Write a valid minimal Markdown document
- Predict why a line did or did not format

## Conceptual explanation

Markdown parsers read your file in two layers:

1. **Block elements** — headings, paragraphs, lists, code blocks, quotes, tables, thematic breaks. These are the large pieces of a page.
2. **Inline elements** — emphasis, links, images, inline code, and plain text. These live *inside* blocks.

This is why a blank line matters. A blank line tells the parser, "the previous block is finished." If you forget it, two things that should be separate may glue together.

Think of Markdown as a very small grammar:

```text
document  →  one or more blocks
block     →  heading | paragraph | list | code | quote | ...
paragraph →  inlines (text, emphasis, links, code spans, ...)
```

You do not need to memorize a spec. You do need this habit: **when something fails to format, look at blank lines, indentation, and special characters first.**

## Special characters

These characters are structurally important in Markdown. You will learn each one in later lessons. For now, recognize them.

| Character | Typical meaning |
|-----------|-----------------|
| `#` | Heading |
| `*` `_` | Emphasis or list marker |
| `-` `+` | List marker or thematic break |
| `` ` `` | Code |
| `[]()` | Links and images |
| `>` | Blockquote |
| `\` | Escape the next character |
| `\|` | Table cell (GFM) |
| `~` | Strikethrough (GFM, when doubled) |

If you want to *show* one of these characters as itself, you often prefix it with a backslash. Lesson 13 covers escaping in full.

## Whitespace rules

Markdown is more sensitive to blank lines than to extra spaces in ordinary sentences.

| Rule | Why it matters |
|------|----------------|
| Separate blocks with a blank line | Headings, lists, and code fences parse reliably |
| Do not indent ordinary paragraphs with four spaces | Four spaces can start an indented code block in some parsers |
| One space after list markers (`- item`) | `-item` may not be a list |
| Trailing two spaces can force a line break | Easy to miss; prefer a blank line or a trailing backslash where supported |
| Tabs vs spaces in nested lists | Mixed indentation is a leading cause of broken lists |

**Standard Markdown / CommonMark:** a line indented by four spaces or a tab can be treated as a code block. That surprise bites students who paste from Word or from indented email.

## Syntax: a minimal document

```markdown
# Title

A paragraph of one or more sentences.

Another paragraph after a blank line.
```

### Syntax explanation

- `# Title` is a block: an ATX heading.
- The blank line ends the heading block.
- The next non-blank lines form a paragraph.
- Another blank line starts a new paragraph.

## Beginner example

**Source**

```markdown
# Experiment log

Today I installed Python.

Tomorrow I will run the sample notebook.
```

**Expected rendered result**

- Heading: Experiment log
- Two separate paragraphs

If you delete the blank lines:

```markdown
# Experiment log
Today I installed Python.
Tomorrow I will run the sample notebook.
```

Many renderers still show a heading plus one paragraph, but lists, quotes, and code are far more likely to break without blank lines. Form the habit now.

## Intermediate example

Mixing several block types correctly:

```markdown
# Dataset notes

The file `patients.csv` has 1,204 rows.

## Columns

- `id` — anonymous patient id
- `age` — age in years
- `label` — `0` or `1`

See the codebook before you clean missing values.
```

**Expected rendered result**

- H1, paragraph, H2, bullet list, paragraph
- Inline code for column names

Each block is separated by a blank line (the list items themselves are not separated; they belong to one list block).

## Advanced example: how parsers can disagree

This line is a classic edge case:

```markdown
- item
  continuation
```

Most CommonMark parsers treat `continuation` as part of the list item.

This one is different:

```markdown
    print("hello")
```

Four leading spaces: original Markdown and CommonMark treat it as a code block. GFM on GitHub still supports indented code, but fenced code (Lesson 12) is the modern style and avoids accidental indentation bugs.

**Write as if blank lines and fences are your friends.** Do not rely on clever indentation.

## Common mistakes

- No blank line before a list or heading. The list may become part of the previous paragraph.
- Indenting paragraphs to "look nested" in the editor. You may create a code block by accident.
- Copy-pasting from Slack or Word, which can insert special Unicode bullets and non-breaking spaces.
- Leaving a code fence unclosed. The rest of the file becomes a code block.
- Mixing tabs and spaces when nesting lists.

## Best practices

- Always put a blank line before and after headings, lists, quotes, tables, and code fences.
- Start lines at column 0 unless you are nesting inside a list.
- Prefer fenced code blocks over indented ones.
- When debugging, look at the raw file with whitespace visible in your editor.
- Keep lines reasonably short (wrap around 80–100 characters if you like), but wrapping is optional; GitHub wraps long lines.

## Practical use cases

- **Course notes:** blank lines between topics keep the outline clear.
- **Lab reports:** headings and paragraphs stay distinct when you paste command output.
- **READMEs:** install instructions fail to render as lists if you skip blank lines after a paragraph.
- **Pull requests:** a missing fence in a comment can swallow the rest of the description.

## Practice exercises

1. Write a file with a heading and two paragraphs. Preview it. Then remove the blank lines and preview again. What changed?
2. Type a paragraph, then indent the next paragraph by four spaces. What does your preview do?
3. Create a heading, a short paragraph, and a three-item list, using blank lines in the recommended places.
4. In your editor, enable "render whitespace" and inspect a Markdown file you pasted from a web page. Do you see unusual spaces?

## Quick review

- Markdown documents are blocks; blocks contain inlines.
- Blank lines separate blocks.
- `# * _ - ` []() > \\` and friends are special.
- Four-space indentation can mean "code."
- When formatting fails, check whitespace and unclosed fences first.

---

[← Previous Lesson](02-what-is-markdown.md) | [Course Home](../README.md) | [Next Lesson →](04-headings.md)
