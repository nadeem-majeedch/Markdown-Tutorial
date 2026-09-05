# Lesson 18 — Footnotes and definition lists

[← Previous Lesson](17-internal-links.md) | [Course Home](../README.md) | [Next Lesson →](19-emojis.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write footnotes in GitHub-Flavored Markdown
- Place footnote definitions at the bottom of a file
- Recognize definition-list syntax where it is supported
- Choose footnotes versus parenthetical citations versus a bibliography
- Label both features as renderer-dependent where needed

## Conceptual explanation

Academic and technical writing often needs **asides**: a citation, a caveat, a URL that would clutter the sentence.

A **footnote** puts a marker in the sentence and the extra text at the bottom of the page (or the end of the article).

A **definition list** is a glossary structure: a term, then its definition. HTML has `<dl>`, `<dt>`, `<dd>`. Markdown support is uneven.

| Feature | GitHub | Pandoc | Original Markdown |
|---------|--------|--------|-------------------|
| Footnotes | Yes (GFM) | Yes | No |
| Definition lists | No (use HTML) | Yes | No |

**This course target:** footnotes work in GitHub Markdown. Definition lists on GitHub should be written as HTML or as ordinary headings plus paragraphs.

## Syntax: footnotes (GFM)

Inline marker:

```markdown
Markdown was proposed in 2004.[^gruber]
```

Definition (usually at the end of the file):

```markdown
[^gruber]: John Gruber, *Markdown*, 2004. https://daringfireball.net/projects/markdown/
```

Named, readable labels (`gruber`, `1`, `note-bias`) are all allowed. Numbers are not assigned by you in the output; GitHub orders them by appearance.

Multi-paragraph footnote: indent continuation lines.

```markdown
[^long]: First paragraph of the note.

    Second paragraph, indented.
```

### Syntax explanation

- `[^label]` is the reference.
- `[^label]:` starts the definition.
- Labels can be words or numbers.
- Reuse the same label to point at the same note twice.
- GitHub renders a superscript link and a footnote section near the bottom of the container.

## Syntax: definition lists (Pandoc / some processors — not GitHub)

```markdown
Term
: Definition

Markdown
: A lightweight markup language.
```

**GitHub will not turn this into a `<dl>`.** It will look like a paragraph with a colon.

Portable GitHub glossary:

```markdown
**Markdown**
: Not used.

**Markdown.** A lightweight markup language.

**GFM.** GitHub-Flavored Markdown, including tables and task lists.
```

Or HTML:

```html
<dl>
  <dt>Markdown</dt>
  <dd>A lightweight markup language.</dd>
  <dt>GFM</dt>
  <dd>GitHub-Flavored Markdown.</dd>
</dl>
```

Test HTML definition lists on GitHub; simple `dl/dt/dd` is often allowed.

## Beginner example

**Source**

```markdown
We use accuracy as the primary metric.[^acc]

[^acc]: Accuracy is (TP + TN) / (TP + TN + FP + FN).
```

**Expected rendered result on GitHub**

A superscript after "metric." Clicking it jumps to the footnote. A small back-link returns you to the text.

## Intermediate example: lab report citations

```markdown
Caffeine was extracted with dichloromethane.[^sop] The procedure
follows the department SOP with one change: we used 80 °C water
instead of boiling water.[^temp]

## References

[^sop]: CHEM 220 Standard Operating Procedure 4: Liquid–liquid extraction.
[^temp]: Boiling water scorched the leaves in a pilot run (12 March 2026).
```

**Expected rendered result**

Two superscripts in the paragraph. Definitions collected at the bottom. This is lighter than a full BibTeX file and appropriate for short labs. For a thesis, use a real bibliography tool (Pandoc citeproc, Zotero, LaTeX).

## Advanced example: what not to put in a footnote

Poor use: hiding a required safety warning in a footnote.

Better: a visible **Warning:** paragraph or GitHub alert.

Poor use: twenty footnotes on every sentence of a README. Readers of software docs want links and a reference list, not academic apparatus.

Good use in expert docs: a compatibility caveat.

```markdown
The CLI supports Node 20 and 22.[^node]

[^node]: Node 18 was dropped in v3.0. See the changelog.
```

### Combining with links

Footnotes can contain Markdown:

```markdown
[^vaswani]: Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
```

You can also skip footnotes and use a **References** heading with a numbered list. Many students find that more portable across PDF export tools.

## Common mistakes

- Writing `[^1]` without a matching `[^1]:` definition. The marker may render broken.
- Putting the definition in a code fence by accident.
- Assuming definition-list colon syntax works on GitHub. It does not.
- Using footnotes for all citations in a paper that must follow APA/IEEE visually. Check your department's rules.
- Nested footnotes. Keep them flat.

## Best practices

- Use meaningful labels: `[^bias]` not only `[^1]`, so the source stays readable.
- Put all definitions at the end under a comment or heading.
- Prefer a visible References section when exporting to PDF via tools that mishandle GFM footnotes.
- On GitHub READMEs, prefer inline links over footnotes for documentation.
- For glossaries on GitHub, use bold terms or HTML `<dl>`.

## Practical use cases

- **Essays and lab reports** on GitHub or in GFM preview
- **Design docs:** extra rationale without bloating a paragraph
- **Specs:** edge-case notes
- **Glossaries:** HTML `<dl>` or simple bold-term lists

## Practice exercises

1. Write a paragraph with one footnote citing a website.
2. Add a second reference to the same footnote label.
3. Write a three-term glossary as bold terms plus sentences (GitHub-portable).
4. If you have Pandoc, optionally try the colon definition-list syntax and compare with GitHub.

## Quick review

- GFM footnotes: `[^label]` and `[^label]: text`
- GitHub supports footnotes; original Markdown does not
- Pandoc definition lists (`Term` / `: Definition`) are not GFM
- On GitHub, glossaries should use HTML or ordinary formatting
- Footnotes are asides, not a substitute for a bibliography in formal papers

---

[← Previous Lesson](17-internal-links.md) | [Course Home](../README.md) | [Next Lesson →](19-emojis.md)
