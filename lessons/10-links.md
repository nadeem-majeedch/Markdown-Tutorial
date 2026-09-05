# Lesson 10 — Links

[← Previous Lesson](09-nested-lists.md) | [Course Home](../README.md) | [Next Lesson →](11-images.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Write inline links
- Write reference-style links
- Add optional link titles
- Use autolinks and email links
- Choose absolute versus relative URLs in a GitHub repository

## Conceptual explanation

A **link** has two parts:

1. **The visible text** — what the reader clicks
2. **The destination** — a URL or a relative path

Markdown keeps both in the source so the file remains readable:

```markdown
[visible text](destination)
```

On GitHub, destinations can be:

- External URLs: `https://docs.python.org/3/`
- Paths in the same repository: `docs/install.md`
- In-page anchors: `#installation` (Lesson 17)
- GitHub objects: issues, commits, mentions (Lesson 23)

**Standard Markdown** includes inline links, reference links, and autolinks. **GFM** also autolinks bare URLs such as `https://example.com`.

## Syntax

### Inline link

```markdown
[Python tutorial](https://docs.python.org/3/tutorial/)
```

With a title (tooltip on hover, in HTML `title=`):

```markdown
[Python tutorial](https://docs.python.org/3/tutorial/ "Official Python 3 tutorial")
```

### Relative link

```markdown
[Course home](../README.md)
[Next lesson](11-images.md)
```

### Reference-style link

```markdown
We follow the [NumPy style guide][numpy-style] in this lab.

[numpy-style]: https://numpydoc.readthedocs.io/en/latest/format.html
```

The definition can sit anywhere in the file, commonly at the bottom. Labels are not case-sensitive.

Shorthand when the label equals the text:

```markdown
See [PEP 8][].

[PEP 8]: https://peps.python.org/pep-0008/
```

### Autolinks

```markdown
<https://github.com>
<student@university.edu>
```

**GFM bare URL:**

```markdown
https://github.com
```

GitHub turns that into a link even without angle brackets.

### Syntax explanation

- Square brackets wrap the clickable text.
- Parentheses wrap the URL. Quotes inside the parentheses are the optional title.
- Spaces in URLs should be encoded (`%20`) or avoided.
- Link text can contain emphasis: `[**must read**](notes.md)`
- Empty text `[ ](url)` is a poor idea; always write meaningful text.

## Beginner example

**Source**

```markdown
Submit the report as a pull request. If you are new to Git, read
[GitHub's quickstart](https://docs.github.com/en/get-started/quickstart).
```

**Expected rendered result**

A sentence containing a blue "GitHub's quickstart" link. The raw URL is hidden from the reader.

## Intermediate example: course navigation

```markdown
# Week 6 notes

Full syllabus: [Syllabus](../syllabus.md)

## Readings

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- Course slides ([PDF](../slides/week-06.pdf))

## Internal

Return to the [table of contents](../README.md).
```

**Expected rendered result**

A mix of repo-relative links and an external arXiv link. Relative links keep working when the repository is forked or published on GitHub Pages *if* the paths stay valid.

Use relative links for files you own. Use absolute `https://` links for other sites.

## Advanced example: reference links in a paper summary

```markdown
The original transformer paper [Vaswani et al., 2017][vaswani]
replaced recurrence with self-attention. Later surveys
[compare variants][lin-survey] on long sequences.

For implementation notes see the [course home][home].

[vaswani]: https://arxiv.org/abs/1706.03762 "Attention Is All You Need"
[lin-survey]: https://arxiv.org/abs/2009.06732
[home]: ../README.md
```

**Expected rendered result**

Readable prose with short citations. URLs live in a reference block, which keeps paragraphs clean. This style scales well in literature reviews.

### Link text that is accessible

Bad: `click here`, `here`, `link`.

Better: `Python 3 tutorial`, `Lab 4 rubric`, `Vaswani et al., 2017`.

Screen readers often announce link text out of context (Lesson 32).

## Common mistakes

- Reversing the brackets: `(text)[url]` does not work.
- Spaces between `] and (`: `[text] (url)` often fails.
- Using Windows paths `C:\Users\...` as URLs.
- Linking to `localhost` in a README. Other people cannot open your machine.
- Broken relative paths (`lessons/10-links.md` from inside `lessons/` should be `10-links.md` or `./10-links.md`).
- Pasting URLs with trailing punctuation inside the parentheses by accident.
- Tiny URL shorteners that hide the destination in academic work. Prefer the canonical URL.

## Best practices

- Write descriptive link text.
- Prefer relative links for files in the same repository.
- Prefer HTTPS URLs.
- Use reference-style links when the same destination appears many times or when a paragraph is URL-heavy.
- Check links before you submit; GitHub does not verify them for you.
- Do not wrap every bare URL in a student paper if you can use a citation link instead.

## Practical use cases

- **README:** documentation, demo video, issue tracker
- **Course notes:** textbook sections, lecture recordings
- **Research:** DOI and arXiv links
- **This course:** previous / home / next navigation at the bottom of each lesson

## Practice exercises

1. Link the words `Pandas documentation` to `https://pandas.pydata.org/docs/`.
2. Add a title tooltip to that link.
3. Convert the link to reference style with label `pandas-docs`.
4. From a file in `lessons/`, write a relative link to `../README.md` and to `11-images.md`.
5. Rewrite `For the spec, click [here](https://spec.commonmark.org/).` so the link text names the spec.

## Quick review

- Inline: `[text](url)`
- Optional title: `[text](url "title")`
- Reference: `[text][id]` plus `[id]: url`
- Autolink: `<https://...>` — GFM also autolinks bare URLs
- Relative paths for in-repo files; descriptive text for humans and screen readers

---

[← Previous Lesson](09-nested-lists.md) | [Course Home](../README.md) | [Next Lesson →](11-images.md)
