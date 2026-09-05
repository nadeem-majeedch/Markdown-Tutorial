# Lesson 12 — Code: inline, fences, and highlighting

[← Previous Lesson](11-images.md) | [Course Home](../README.md) | [Next Lesson →](13-horizontal-rules-escaping.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Mark inline code with backticks
- Write fenced code blocks
- Add a language tag for syntax highlighting
- Show a backtick inside inline code
- Choose code versus emphasis, quotes, or screenshots

## Conceptual explanation

Technical documents constantly mention identifiers, commands, and snippets. Markdown gives them a **monospaced, unformatted** style so readers can copy them accurately.

There are two layers:

| Form | Use | HTML |
|------|-----|------|
| Inline code | A name inside a sentence: `pandas.read_csv` | `<code>` |
| Fenced code block | Multiple lines the reader might copy | `<pre><code>` |

**Syntax highlighting** is extra: if you label the fence with a language (`python`, `bash`, `json`), GitHub colors the tokens. Highlighting is **GFM / renderer-dependent**. The fence itself is widely supported (CommonMark).

Indented code blocks (four spaces) are the original Markdown form. Prefer fences. They are clearer and do not collide with nested lists as often.

## Syntax

### Inline code

```markdown
Install the `scikit-learn` package.
```

A backtick inside inline code: wrap with more backticks and spaces:

```markdown
The fence looks like `` ` `` in this sentence.
```

### Fenced code block

````markdown
```
plain text, no highlighting
```
````

With a language tag:

````markdown
```python
def area(radius):
    return 3.14159 * radius ** 2
```
````

### Syntax explanation

- One backtick starts and ends an inline span.
- Three (or more) backticks start a fence. The closing fence must be at least as long.
- The language tag is a short name on the opening fence line: `python`, `py`, `javascript`, `js`, `ts`, `bash`, `sh`, `json`, `yaml`, `html`, `css`, `sql`, `r`, `cpp`, `java`, `go`, `rust`, `markdown`, `diff`, `text`.
- Content inside a fence is **not** interpreted as Markdown. `**bold**` inside a fence stays literal.
- Tilde fences `~~~` also work in CommonMark; GitHub accepts them. Backticks are the usual choice.

## Beginner example

**Source**

```markdown
Run `python --version` in a terminal.
```

**Expected rendered result**

The command appears in a distinct typeface, typically with a light background.

**Source**

````markdown
```bash
python --version
```
````

**Expected rendered result**

A block, copyable as a whole, with shell coloring on GitHub.

## Intermediate example: a data-science snippet

````markdown
Load the CSV with pandas and drop empty rows:

```python
import pandas as pd

df = pd.read_csv("patients.csv")
df = df.dropna(subset=["age", "label"])
print(df.shape)
```

The important function is `dropna`, not the print statement.
````

**Expected rendered result**

An intro sentence, a highlighted Python block, then a follow-up sentence with inline code. Students should see why the language tag matters: `import` and `print` are colored as keywords on GitHub.

### Why highlighting works

GitHub uses a highlighter (currently based on Linguist language detection plus a highlighting library). It maps the fence tag to a grammar. Unknown tags still show a monospaced block; they just lack color. Spelling the language correctly is enough. You do not install anything.

## Advanced example: nested fences and diffs

To *document Markdown itself*, open with a longer fence:

`````markdown
````markdown
```python
print("hello")
```
````
`````

A `diff` block is excellent in code reviews and lab write-ups:

````markdown
```diff
- learning_rate = 0.1
+ learning_rate = 0.01
```
````

**Expected rendered result on GitHub**

Removed lines in red, added lines in green, when the language is `diff` and lines start with `-` or `+`.

### Commands versus output

````markdown
```bash
pytest -q
```

```text
12 passed in 3.04s
```
````

Use `bash` (or `sh`) for commands the reader should run. Use `text` or no tag for program output so nobody thinks the output is a command.

## Common mistakes

- Unclosed fence: the rest of the file becomes code. Always count opening and closing fences.
- Using a word processor quote character `` “ `` instead of `` ` ``.
- Putting a language tag on the *closing* fence. It belongs on the opening line.
- Highlighting fake languages (`phyton`). The block still works; colors do not.
- Using inline code for long snippets. Use a fence.
- Using a screenshot of code instead of a fence. Screenshots are not copyable or accessible.
- Four-space indent by accident, creating a code block from a normal paragraph.

## Best practices

- Inline code for identifiers, file names, flags, and short commands.
- Fences for anything a reader might copy as a block.
- Always add a language tag when you know the language.
- Keep snippets complete enough to understand, small enough to read.
- Do not paste secrets (API keys, tokens) into code blocks.
- Indent fences inside list items (Lesson 09).

## Practical use cases

- **README:** install commands in `bash` fences
- **Labs:** the function the student must write
- **ML papers notes:** a PyTorch training loop excerpt
- **This course:** every example you have been reading

## Practice exercises

1. Mention the filename `train.py` inline in a sentence.
2. Write a fenced Python function `accuracy(y_true, y_pred)` with a language tag.
3. Write a `bash` block with two commands to create and activate a virtual environment.
4. Create a `diff` block that changes `epochs = 3` to `epochs = 10`.
5. Deliberately omit a closing fence in a scratch file, preview it, then fix it. Remember that feeling.

## Quick review

- Inline: `` `code` ``
- Fence: three backticks, optional language tag, matching close
- Language tags enable highlighting on GitHub
- Content in fences is literal, not Markdown
- Never leave a fence unclosed

---

[← Previous Lesson](11-images.md) | [Course Home](../README.md) | [Next Lesson →](13-horizontal-rules-escaping.md)
