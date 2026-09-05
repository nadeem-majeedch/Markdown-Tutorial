# Lesson 19 — Emojis

[← Previous Lesson](18-footnotes.md) | [Course Home](../README.md) | [Next Lesson →](20-math.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Insert Unicode emoji in a Markdown file
- Use GitHub emoji shortcodes
- Decide when emoji helps and when it harms professionalism
- Keep documents accessible when emoji is present
- Know what is standard versus GitHub-specific

## Conceptual explanation

An **emoji** is a Unicode character (or sequence) that many fonts draw as a small pictogram. Because Markdown files are plain text, you can paste emoji directly:

```markdown
Shipped in v2.1
```

GitHub also supports **shortcodes**: ASCII names between colons that GitHub replaces with emoji images.

```markdown
:shipit: :tada: :warning:
```

**Standard Markdown** has no emoji syntax. Unicode characters work anywhere UTF-8 is accepted (almost everywhere). **Shortcodes are GitHub-specific** (also used in Slack, Discord, and some other tools, with *different* name lists).

## Syntax

### Unicode (portable)

```markdown
Status: done
Warning: do not train on the test set.
```

Type them with your OS picker, or paste from a character map.

### GitHub shortcodes

```markdown
:rocket: Launch notes
:bug: Known issues
:books: Documentation
```

A full list is documented by GitHub as "Emoji cheat sheet" / emoji markup. Names use lowercase and underscores: `:white_check_mark:`, `:heavy_plus_sign:`.

### Syntax explanation

- Unicode emoji is just text. No special Markdown parsing.
- Shortcodes are replaced only by renderers that know that dictionary. A PDF toolchain may print `:rocket:` literally.
- Shortcodes can sit inside headings, lists, and tables on GitHub.
- Variation selectors and skin-tone modifiers are Unicode, not Markdown.

## Beginner example

**Source**

```markdown
# Project status

- Docs: complete
- Tests: in progress
```

Or with shortcodes on GitHub:

```markdown
- Docs: :white_check_mark: complete
- Tests: :construction: in progress
```

**Expected rendered result on GitHub**

A heading and a list, with icons if shortcodes or Unicode are used.

## Intermediate example: README sections

```markdown
## Features

- Fast CSV parser
- Typed Python API
- MIT license
```

Some popular READMEs prefix every bullet with emoji. That can scan well *or* look noisy. A professional default for academic and industry course work is:

- Use emoji in informal project READMEs if the team wants a friendly tone
- Avoid emoji in lab reports, papers, and formal API references unless a style guide allows it

## Advanced example: accessibility and headings

```markdown
## :warning: Breaking changes
```

Problems:

- Screen readers may announce "warning" twice or skip the glyph
- GitHub heading IDs may include or drop the shortcode / emoji (Lesson 17)
- Search becomes harder

Better:

```markdown
## Breaking changes
```

If you want a visible warning, GitHub **alerts** (Lesson 23) are clearer than a heading emoji:

```markdown
> [!WARNING]
> Version 4 removes `fit_old()`.
```

### Emoji in tables and CI badges

Unicode in table cells is fine. Do not replace words entirely with icons:

| Bad | Better |
|-----|--------|
| :white_check_mark: | Supported |
| mix of both | Linux: supported |

Readers and parsers should still understand the cell if the image fails.

## Common mistakes

- Assuming `:smile:` works in every Markdown preview. It is not CommonMark.
- Overloading a README with a dozen icons per line.
- Using emoji as the only indicator of pass/fail in a grading table.
- Putting emoji in filenames (`notes🎉.md`). Tools and URLs suffer.
- Copying emoji from a chat app that inserts non-standard sequences.

## Best practices

- Prefer Unicode when you need an icon outside GitHub.
- Prefer words (or GitHub alerts) for warnings.
- One optional decorative emoji in a README title is enough.
- Keep formal academic Markdown emoji-free unless instructed otherwise.
- Never rely on color or icon alone to convey meaning (Lesson 32).

## Practical use cases

- Informal open-source README section markers
- Changelog: added / fixed / removed labels (or use words: Added, Fixed)
- Course Discord-to-notes paste (clean them up for the official submission)
- Issue titles on GitHub (team-dependent)

## Practice exercises

1. Write a three-item status list using only words, then a second version using GitHub shortcodes.
2. Preview both in a tool that is *not* GitHub. Which still looks right?
3. Rewrite a heading `## :bug: Bugs` without emoji.
4. Find GitHub's emoji documentation and look up `:octocat:`.

## Quick review

- Unicode emoji is portable plain text
- `:shortcode:` is GitHub (and some chat tools), not standard Markdown
- Use emoji lightly; never as the only meaning
- Formal reports should usually skip emoji

---

[← Previous Lesson](18-footnotes.md) | [Course Home](../README.md) | [Next Lesson →](20-math.md)
