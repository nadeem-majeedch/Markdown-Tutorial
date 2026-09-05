# Lesson 16 — HTML inside Markdown

[← Previous Lesson](15-task-lists.md) | [Course Home](../README.md) | [Next Lesson →](17-internal-links.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Include simple HTML in a Markdown file
- Know which tags GitHub allows and which it strips
- Use HTML for the few layouts Markdown cannot express
- Mix HTML and Markdown without breaking paragraphs
- Avoid unsafe HTML (scripts, inline event handlers)

## Conceptual explanation

Markdown was designed to *compile to HTML*. Gruber allowed authors to drop down to raw HTML when the lightweight syntax was not enough.

That escape hatch is powerful and dangerous:

- Powerful: you can add a line break, a definition list, a colored mark, a details/summary spoiler, or an image width.
- Dangerous: different renderers **sanitize** HTML. GitHub removes scripts and most attributes that could run code. Email clients and some linters strip even more.

**Rule of thumb:** write Markdown first. Add HTML only for a specific gap, and only tags you have tested on the target renderer.

## What GitHub generally allows

GitHub's sanitizer (an allow-list) typically keeps structural tags such as:

`p`, `div`, `span`, `br`, `hr`, `h1`–`h6`, `ul`, `ol`, `li`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `a`, `img`, `strong`, `em`, `b`, `i`, `del`, `ins`, `code`, `pre`, `blockquote`, `details`, `summary`, `kbd`, `sub`, `sup`, `dl`, `dt`, `dd`, `mark` (support can change — test).

GitHub strips or ignores:

- `<script>`, `<style>` (in many contexts), `<iframe>` (often)
- `onClick` and other event attributes
- `javascript:` URLs
- Most CSS classes you might expect from a full website (README pages have limited styling)

Do not rely on custom CSS in `README.md`. GitHub Pages sites (Lesson 28) can use CSS because they are real websites.

## Syntax

A line break:

```html
Line one<br>
Line two
```

Subscript and superscript:

```markdown
H<sub>2</sub>O and 10<sup>3</sup>
```

Collapsible section (**GitHub-supported**, widely used in READMEs):

```html
<details>
<summary>Show training curve notes</summary>

The loss spiked at epoch 12 because the learning rate was too high.

</details>
```

Image size:

```html
<img src="assets/plot.png" alt="Loss curve" width="400">
```

### Syntax explanation

- HTML blocks often need **blank lines** around them so the Markdown parser does not wrap them in `<p>` incorrectly.
- Markdown inside an HTML block is **not always processed**. GitHub processes Markdown inside `<details>` if there are blank lines. Other tags may treat inner text as raw HTML.
- When you need Markdown inside HTML, test on GitHub. A reliable pattern for `<details>` is: blank line after `<summary>`, then Markdown, then blank line before `</details>`.

## Beginner example

**Source**

```markdown
Water is H<sub>2</sub>O. The area is 4 m<sup>2</sup>.
```

**Expected rendered result**

Water is H<sub>2</sub>O. The area is 4 m<sup>2</sup>.

(If you need a lot of math, Lesson 20 is better than HTML hacks.)

## Intermediate example: keyboard keys and collapsible answers

```markdown
Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to copy.

<details>
<summary>Hint for exercise 2</summary>

Use a **stratified** split so each class stays balanced.

</details>
```

**Expected rendered result on GitHub**

Keyboard-style keys, and a disclosure triangle labeled "Hint for exercise 2" that expands to a sentence with bold text.

This is excellent for course notes and assignment pages you publish on GitHub.

## Advanced example: when HTML is the wrong tool

**Do not** rebuild your design system in a README:

```html
<div style="color: red; font-size: 48px;">IMPORTANT</div>
```

GitHub may strip `style`. Even if a preview tool shows it, the page will not look that way on github.com.

**Do not** embed tracking or scripts.

**Do** use HTML tables only when you need `colspan`:

```html
<table>
  <tr>
    <th colspan="2">Test accuracy</th>
  </tr>
  <tr>
    <td>Baseline</td>
    <td>0.81</td>
  </tr>
</table>
```

Even then, a simpler GFM table plus a heading is often clearer.

### Mixing rules that bite students

```markdown
<div>
This **will not** become bold on many parsers because it is inside an HTML block.
</div>
```

```markdown
<div>

This **will** often become bold on GitHub because of the blank lines.

</div>
```

When in doubt, keep HTML tags on their own lines with blank lines around inner Markdown.

## Common mistakes

- Assuming `<style>` in a README will theme GitHub.
- Using `<font color="red">` (obsolete; may be stripped).
- Forgetting alt text on HTML `<img>`.
- Nesting Markdown links inside HTML without testing.
- Copy-pasting Word-generated HTML. It is huge and ugly.
- Putting unescaped `<` in prose, which can start an unintended tag. Use `` `<` `` or `&lt;`.

## Best practices

- Prefer pure Markdown for 95% of the document.
- Test HTML on the real target (GitHub, Pages, Pandoc).
- Always include `alt` on `<img>`.
- Use `<details>` for optional noise, not for required instructions.
- Never put secrets, scripts, or tracking pixels in Markdown HTML.
- For math, diagrams, and tables, prefer the specialized syntax in later lessons when the renderer supports it.

## Practical use cases

- **README:** collapsible long logs, extra install notes
- **Course notes:** hints and answers
- **Science:** `<sub>` and `<sup>` when math mode is unavailable
- **Docs:** `<kbd>` for shortcuts

## Practice exercises

1. Write a chemical formula using `<sub>`.
2. Create a `<details>` block with a one-sentence hint inside.
3. Embed an image with HTML and include alt text and `width="300"`.
4. Try `<div style="color:red">Hello</div>` on GitHub. Record whether the color survived. What does that tell you about README CSS?

## Quick review

- Raw HTML is allowed, then often sanitized
- GitHub strips scripts and most styling
- `<details>`, `<kbd>`, `<sub>`, `<sup>`, and `<br>` are the useful extras
- Blank lines affect whether inner Markdown is parsed
- Markdown first; HTML only for gaps

---

[← Previous Lesson](15-task-lists.md) | [Course Home](../README.md) | [Next Lesson →](17-internal-links.md)
