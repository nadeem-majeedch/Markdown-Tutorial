# Lesson 06 — Text formatting

[← Previous Lesson](05-paragraphs.md) | [Course Home](../README.md) | [Next Lesson →](07-blockquotes.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write italic, bold, and bold-italic text
- Strike through text using GitHub-Flavored Markdown
- Know when highlighting is available (and when it is not)
- Combine emphasis with code, lists, and headings correctly
- Avoid nested-asterisk bugs

## Conceptual explanation

Emphasis tells the reader what is important. In Markdown you mark a *span* of text with delimiter characters. The parser turns those spans into HTML `<em>`, `<strong>`, or (in GFM) `<del>`.

Use emphasis the way a careful journal uses it: **sparingly**. If everything is bold, nothing is.

| Style | Meaning in technical writing |
|-------|------------------------------|
| Italic | Terms on first use, book titles, mild emphasis |
| Bold | UI labels, critical warnings, vector-like stress on a word |
| Bold italic | Rare; nested emphasis |
| Strikethrough | Obsolete API names, tracked changes, "we no longer do X" |
| Highlight | Not standard Markdown; only some editors |

## Syntax

### Italic

```markdown
*italic* or _italic_
```

### Bold

```markdown
**bold** or __bold__
```

### Bold italic

```markdown
***bold italic*** or **_bold italic_**
```

### Strikethrough — GitHub-Flavored Markdown

```markdown
~~strikethrough~~
```

**Not standard Markdown.** Works on GitHub, many previewers, and GFM parsers. May not work in strict CommonMark tools.

### Highlight — renderer-dependent

Some tools (Typora, certain wikis) support:

```markdown
==highlighted text==
```

**GitHub does not render `==highlight==` as a mark.** On GitHub, use bold, an alert (Lesson 23), or HTML `<mark>` if HTML is allowed (Lesson 16). Prefer portable bold unless you control the renderer.

### Syntax explanation

- Opening and closing markers must match.
- Do not put a space after the opening marker: `** bold **` often fails; `**bold**` works.
- Word-internal underscores can fail: `long_variable_name` may be parsed as emphasis. Prefer asterisks, or wrap code in backticks.
- Emphasis is inline: it lives inside a paragraph, heading, or list item.

## Beginner example

**Source**

```markdown
A *tensor* is a multi-dimensional array. In this lab you must submit
**both** the notebook and the PDF export.
```

**Expected rendered result**

- "tensor" in italic
- "both" in bold
- The rest of the sentences in regular type

## Intermediate example

```markdown
Install **Python 3.12** and the `numpy` package.

The old function `fit_model()` is ~~deprecated~~. Use `Model.fit()` instead.

Read _Pattern Recognition and Machine Learning_ (Bishop) before the quiz.
```

**Expected rendered result**

- Product names in bold
- Deprecated phrase struck through (on GitHub)
- Book title in italic
- Identifiers in `code` style, which you will study in Lesson 12. Backticks protect underscores in names like `fit_model`.

## Advanced example: nested and mixed markers

```markdown
Use ***very strong* caution** when deleting the `main` branch.

This is **bold with an *italic* word inside**.

The formula is not ** * n **, it is `n * n`.
```

Tips:

- Asterisks are easier to nest than underscores.
- If a literal asterisk is part of the sentence, escape it (`\*`) or put the math in code or a math block (Lesson 20).
- Do not emphasize entire paragraphs. Use a heading, a blockquote, or a list.

### Programming and data-science style

| Do this | Avoid this |
|---------|------------|
| Set `learning_rate` to **0.01** | Set *learning_rate* to 0.01 |
| Click **File → Save** | Click File → Save in bold-italic |
| The *loss* increased | The **loss** **increased** **again** |

Code identifiers belong in backticks, not italics. Italics are for language, not for `function_names`.

## Common mistakes

- Mismatched markers: `**bold*` renders incorrectly.
- Spaces inside markers: `** bold**` fails in CommonMark.
- Underscores inside `snake_case` words without backticks.
- Using strikethrough as decoration. It means "removed."
- Assuming `==highlight==` works on GitHub. It does not.
- Bolding every heading's text *and* using `#`. Redundant.
- Overusing ALL CAPS plus bold for warnings.

## Best practices

- Prefer `*` and `**` over `_` and `__` in technical documents so identifiers stay safe.
- Emphasize a word or a short phrase, not a paragraph.
- Put code in backticks; put UI labels in bold.
- Use strikethrough only for deletions or superseded text.
- Stay portable: do not depend on `==highlight==` for GitHub READMEs.

## Practical use cases

- **README:** **Note:** and **Warning:** labels (or GitHub alerts, Lesson 23)
- **Lab report:** italicize a new term on first definition
- **API docs:** `~~oldEndpoint~~` next to the replacement
- **Course notes:** bold the exam-critical clause in a policy paragraph

## Practice exercises

1. Write a sentence with one italic term and one bold warning.
2. Write a changelog line that strikes through an old flag and bolds the new flag: ~~`--fast`~~ **`--threads`**.
3. Type `this_is_important` without backticks and with `*this_is_important*`. Compare. Then wrap it in backticks.
4. Check whether `==highlight==` works in your preview. Record whether your tool is GitHub-like or Typora-like.

## Quick review

- `*italic*` and `**bold**` are standard.
- `~~strike~~` is GFM (GitHub).
- `==highlight==` is not GitHub Markdown.
- No spaces inside the markers; prefer asterisks in code-heavy text.
- Emphasis is for meaning, not decoration.

---

[← Previous Lesson](05-paragraphs.md) | [Course Home](../README.md) | [Next Lesson →](07-blockquotes.md)
