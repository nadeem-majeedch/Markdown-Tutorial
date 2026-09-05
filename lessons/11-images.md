# Lesson 11 — Images and image links

[← Previous Lesson](10-links.md) | [Course Home](../README.md) | [Next Lesson →](12-code.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Embed an image with alt text
- Add an optional title
- Store images in a repository and link them relatively
- Make an image clickable (an image link)
- Write alt text that is useful for accessibility and for failed loads

## Conceptual explanation

An image in Markdown is almost the same syntax as a link, with a `!` in front:

```markdown
![alternative text](path-or-url)
```

The `!` means "render this destination as an image, not as a clickable phrase."

**Alt text** is not a caption. It is the text used when:

- The image cannot load
- A screen reader describes the page
- Search and accessibility tools index the document

On GitHub, images in a repository render in README files, issues, and Markdown pages. Large binary images belong in `assets/` or in Git LFS, not pasted as huge blobs into the `.md` file.

**Standard Markdown** supports inline and reference images. Captions, resizing, and alignment are **renderer-dependent** (often HTML `<img>` attributes, Lesson 16).

## Syntax

### Inline image

```markdown
![Scatter plot of height versus weight](../assets/height-weight.png)
```

With a title (often shown as a tooltip):

```markdown
![Scatter plot of height versus weight](../assets/height-weight.png "Lab 2 figure 1")
```

### Remote image

```markdown
![GitHub Mark](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)
```

Remote images depend on the other server. For course work and READMEs, files in your repo are more reliable.

### Reference-style image

```markdown
![Architecture diagram][arch]

[arch]: ../assets/architecture.png "System architecture"
```

### Image link (clickable image)

Wrap the image in a link:

```markdown
[![Architecture diagram](../assets/architecture.png)](../assets/architecture.png)
```

Readers see the image; clicking it opens the full-size file or another URL (paper, demo, higher-resolution figure).

```markdown
[![Paper thumbnail](../assets/paper-thumb.png)](https://arxiv.org/abs/1706.03762)
```

### Syntax explanation

- `!` + `[alt text]` + `(url)` is the core form.
- Alt text should describe the *content* of the figure, not the filename.
- Empty alt `![](url)` is only for decorative images. Academic figures are not decorative.
- The same relative-path rules as links apply.

## Beginner example

**Source**

```markdown
![Campus map with libraries highlighted](../assets/campus-map.png)
```

**Expected rendered result**

The picture displayed in the page flow. If the file is missing, the reader sees the alt text "Campus map with libraries highlighted".

Because this course repository may not include a real `campus-map.png`, GitHub would show the broken-image placeholder plus alt text. When you do the exercises, add a real file under `assets/`.

## Intermediate example: a lab report figure

```markdown
## Figure 1

![Histogram of residual errors after linear regression](../assets/lab4-residuals.png "Residuals appear roughly normal")

**Figure 1.** Distribution of residuals for the fitted model. n = 250.
```

**Expected rendered result**

A heading, the image, then a bold caption in the next paragraph. Markdown has no standard caption syntax, so a following sentence is the portable approach.

## Advanced example: README hero and clickable badge-like images

```markdown
# OceanNet

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.123456-blue)](https://doi.org/10.5281/zenodo.123456)

![Predicted sea-surface temperature compared with buoy measurements](docs/figures/sst-preview.png)
```

Badges are images served by a badge service and wrapped in links. Lesson 23 and Lesson 24 return to badges. They are GFM/HTML images like any other; the `![]()` syntax is the same.

### Sizing (renderer-dependent)

GitHub ignores Markdown-only width syntax such as some processors' `=100x`. To resize on GitHub you typically need HTML:

```html
<img src="assets/plot.png" alt="Loss curve" width="400">
```

Use HTML resizing only when necessary. Prefer generating an image at the right size so portable Markdown is enough.

## Common mistakes

- Forgetting the `!`. You get a text link instead of an image.
- Using the filename as alt text: `![plot.png](plot.png)`.
- Linking to an image on your desktop (`/Users/me/Desktop/fig.png`). Nobody else has that path.
- Uploading a 20 MB PNG into a Git repo for a tiny README icon.
- Hotlinking images you do not have permission to use.
- Putting a space between `!` and `[`.

## Best practices

- Store images in `assets/` or `docs/figures/` and use relative paths.
- Write alt text that would still make sense if the picture were gone.
- Add a visible caption in the following paragraph for academic figures.
- Compress screenshots.
- Prefer SVG for diagrams when possible; PNG for plots and photos.
- Make screenshots of UI clickable if a larger version exists.

## Practical use cases

- **README:** screenshot of the running app
- **Data science:** saved Matplotlib/Seaborn figures
- **ML:** architecture diagrams, confusion matrices
- **Lab reports:** apparatus photo, chromatogram
- **Course notes:** a photo of a whiteboard, with alt text describing the derivation

## Practice exercises

1. Write an image tag for `../assets/confusion-matrix.png` with alt text that describes a 2×2 confusion matrix.
2. Add a tooltip title.
3. Make the image clickable so it opens the same PNG.
4. Write a caption paragraph under the image, as you would in a report.
5. Explain in one sentence the difference between alt text and a caption.

## Quick review

- Images: `![alt](url)`
- The `!` distinguishes images from links
- Alt text describes the content
- Image link: `[![alt](img)](href)`
- No standard caption or resize syntax; use a following paragraph, and HTML only if you must

---

[← Previous Lesson](10-links.md) | [Course Home](../README.md) | [Next Lesson →](12-code.md)
