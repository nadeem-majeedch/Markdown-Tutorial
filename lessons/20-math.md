# Lesson 20 — Mathematical equations (LaTeX-style)

[← Previous Lesson](19-emojis.md) | [Course Home](../README.md) | [Next Lesson →](21-mermaid.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write inline and block math using LaTeX-like delimiters
- Know where math works (GitHub, Jupyter, Quarto, Pandoc) and where it does not
- Typeset common statistics and ML formulas
- Escape characters that collide with Markdown
- Fall back when the renderer has no math support

## Conceptual explanation

Markdown has no native equation language. **LaTeX math mode** is the de facto standard in STEM, so many Markdown tools embed a math renderer (MathJax or KaTeX).

You write:

```markdown
$$
E = mc^2
$$
```

and the tool turns it into a formatted equation.

**Renderer-dependent.** Support varies:

| Environment | Typical math syntax | Notes |
|-------------|---------------------|--------|
| GitHub (newer GFM math) | `$inline$` and `$$block$$` | Supported in Markdown files, issues, wikis on github.com |
| Jupyter / VS Code notebooks | Same, or `$$` cells | Very common for data science |
| Pandoc / Quarto | `$`, `$$`, or `\( \)` | Excellent PDF output |
| Strict CommonMark README on an old host | None | Show code or Unicode |

Always check your target. This lesson assumes **GitHub math** plus the Jupyter-style syntax students already meet in data-science courses.

## Syntax

### Inline math (GitHub, many tools)

```markdown
The learning rate $\eta$ is 0.01.
```

### Block math

```markdown
$$
\hat{y} = \theta^{\top} x + b
$$
```

Some tools also accept:

```markdown
\\[
\\hat{y} = \\theta^{\\top} x + b
\\]
```

Prefer `$` / `$$` on GitHub and in notebooks unless a style guide says otherwise.

### Syntax explanation

- `$...$` is inline (in a sentence).
- `$$...$$` is a display block, usually centered.
- Inside the delimiters, you write **TeX math**, not Markdown. `*` means multiplication or an italic variable, not emphasis.
- Underscores are subscripts: `x_i`. Carets are superscripts: `x^2`.
- Braces group: `x_{i,j}`, `\frac{a}{b}`.

If `$` is also used for currency, GitHub tries not to treat `I have $5` as math. Still, prefer `USD 5` or escape when a file is full of both money and math.

## Beginner example

**Source**

```markdown
The mean is $\bar{x}$. For two points, $\bar{x} = (x_1 + x_2)/2$.
```

**Expected rendered result (where math works)**

The mean is an x with a bar. The second formula shows a fraction-like expression in mathematical italic.

If math is **not** supported, the reader sees dollar signs and backslashes. In that environment, write:

```markdown
The mean is `x_bar = (x1 + x2) / 2`.
```

## Intermediate example: a short ML derivation

```markdown
## Logistic regression

We model the probability as

$$
P(y=1\mid x) = \sigma(\theta^{\top} x), \quad
\sigma(z) = \frac{1}{1+e^{-z}}
$$

The binary cross-entropy loss for one example is

$$
\mathcal{L} = -\, y \log \hat{p} - (1-y)\log(1-\hat{p})
$$

We update $\theta$ with gradient descent.
```

**Expected rendered result**

A subsection with two centered equations and inline Greek letters. This is standard for course notes and lab discussions.

## Advanced example: aligned equations and Markdown collisions

Aligned block (GitHub uses MathJax-like TeX; `aligned` is widely supported):

```markdown
$$
\begin{aligned}
\nabla_\theta \mathcal{L}
  &= \frac{\partial \mathcal{L}}{\partial \theta} \\
  &= X^{\top}(\hat{p} - y)
\end{aligned}
$$
```

**Collision with Markdown**

This fails if the parser eats underscores or asterisks *outside* math. Keep each equation in `$`/`$$` so the math tokenizer owns those characters.

Inside a table, prefer `$...$` with spaces:

```markdown
| Quantity | Symbol |
| -------- | ------ |
| Learning rate | $\eta$ |
| Regularization | $\lambda$ |
```

### Fallbacks when math is unavailable

1. Unicode: `θᵀx + b` (limited)
2. Inline code: `` `theta^T x + b` ``
3. Screenshot of a rendered equation plus alt text (last resort; not copyable)
4. Link to a PDF built with Quarto/Pandoc/LaTeX

For a thesis, generate PDF with a real typesetting pipeline. For GitHub notes, `$`/`$$` is enough.

## Common mistakes

- Leaving a space in a way your renderer forbids, e.g. `$ x $` vs `$x$` — GitHub is fairly tolerant; some tools are not.
- Using `$$` inline in the middle of a sentence when you wanted `$`.
- Writing Markdown `**bold**` inside `$$`. Use `\mathbf{x}` instead.
- Assuming every GitHub *feature preview* from years ago still applies. Check a current file on github.com.
- Unclosed `$`, which turns the rest of the paragraph into broken math.

## Best practices

- One idea per display equation.
- Number equations in prose if you will refer to them: "Equation (1) below." GitHub math does not auto-number like LaTeX `equation` environments in all contexts.
- Define symbols on first use.
- Do not screenshot notebooks as a substitute for source math in a repo.
- For formal papers, use Quarto or LaTeX; keep Markdown math for notes and READMEs.

## Practical use cases

- **Course notes:** derivations
- **ML reports:** loss functions, update rules
- **Statistics labs:** hypothesis tests, confidence intervals
- **Physics/chemistry:** displayed laws, optional `\ce{}` only if mhchem is installed (often **not** on GitHub)

## Practice exercises

1. Write an inline formula for the slope $m$ of a line through two points (even if you only type the TeX).
2. Display the softmax function in a `$$` block.
3. Put $\alpha$, $\beta$, and $\gamma$ in a three-row table.
4. Open your file on GitHub (or in a notebook). If math does not render, add a code-style fallback under the equation.

## Quick review

- Math is renderer-dependent, not original Markdown
- GitHub and Jupyter: `$inline$` and `$$block$$`
- Inside delimiters, write TeX, not Markdown emphasis
- Fall back to code or Unicode when math is unsupported
- Close every `$`

---

[← Previous Lesson](19-emojis.md) | [Course Home](../README.md) | [Next Lesson →](21-mermaid.md)
