# Exercise set 4 — Emoji, math, Mermaid, and GitHub extras

**Level:** Intermediate  
**Lessons:** [19](../lessons/19-emojis.md)–[23](../lessons/23-github-markdown.md)

[← Previous set](03-intermediate.md) | [Exercises home](README.md) | [Course Home](../README.md) | [Next set →](05-advanced-docs.md)

---

## Goals

Create `exercises/work/04-github-demo.md` aimed at github.com (GFM + GitHub extras). Afterward, open the same file in a preview that is *not* GitHub and write three differences.

## Exercises

### 1. Emoji policy

Write a three-bullet project status list **with words only**. Then duplicate it with GitHub shortcodes. Add a sentence stating which version you would submit in a formal lab report.

### 2. Inline and display math

- Inline: mention $\lambda$ and $\eta$ in a sentence (type the dollar syntax even if you are reading as source).
- Display: binary cross-entropy or MSE in a `$$` block.
- A 2-row table of symbol meanings.

### 3. Mermaid flowchart

Draw a 4-node `flowchart TD` of data → clean → train → evaluate.

- Quote any label that contains `()`
- No line breaks inside labels
- Caption the figure in the following paragraph

### 4. Sequence diagram

A user, an API, and a model service exchanging one request and one response.

### 5. GFM feature pack

In one page region include strikethrough, a tiny table, a task item, and a bare URL.

### 6. Alerts

Write one `NOTE`, one `WARNING`, and one `TIP` using GitHub alert syntax. Keep each body to one sentence.

### 7. Issue language

Draft a PR description that:

- Uses `Closes #15`
- Mentions a teammate as text (`@username` only if you understand it may ping on GitHub)
- Contains a 3-item task list

### 8. Badge

Add a license badge image-link pointing at `../../LICENSE` from `exercises/work/` or at `LICENSE` if you keep the file at repo root for the project later. Use the MIT badge pattern from Lesson 23.

## Self-check

- [ ] Math delimiters are closed
- [ ] Mermaid fence language is `mermaid`
- [ ] Alerts start with `> [!NOTE]` (or TIP/WARNING) as the first quote line
- [ ] You recorded what broke in a non-GitHub preview

## Stretch

Add a PNG fallback sentence: "If the diagram does not render, see `assets/pipeline.png`."
