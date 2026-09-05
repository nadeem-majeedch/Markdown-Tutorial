# Markdown cheat sheet

Quick reference after you finish the course. Features marked **GFM** need GitHub-Flavored Markdown. Features marked **GitHub** need github.com (or a clone of that behavior). Features marked **tool** are renderer-dependent.

[Course Home](../README.md) | [FAQ](faq.md) | [Lessons](../lessons/01-introduction.md)

---

## Headings

| Syntax | Example | Result / use |
|--------|---------|----------------|
| `#`–`######` plus space | `## Methods` | Heading levels 1–6; document outline |
| Setext H1 / H2 | `Title` then `===` / `---` | Legacy; prefer ATX |

## Paragraphs and breaks

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Blank line | two blocks separated | New paragraph |
| Single newline | wrap in source | Usually a space, not a break |
| Backslash break | `line\` | Hard line break (CommonMark/GitHub) |
| Two trailing spaces | `line··` | Hard break; easy to lose |

## Emphasis

| Syntax | Example | Result / use |
|--------|---------|----------------|
| `*italic*` or `_italic_` | `*tensor*` | Emphasis, first-use terms |
| `**bold**` or `__bold__` | `**required**` | Strong emphasis, UI labels |
| `***both***` | `***urgent***` | Bold italic; rare |
| `~~strike~~` **GFM** | `~~old API~~` | Deleted or superseded text |
| `==mark==` **tool** | not on GitHub | Highlight in some editors |

## Blockquotes

| Syntax | Example | Result / use |
|--------|---------|----------------|
| `>` | `> Quoted sentence` | Citation or set-apart prose |
| Nested `>` | `> > inner` | Quoted reply |

## Lists

| Syntax | Example | Result / use |
|--------|---------|----------------|
| `-` `*` `+` | `- numpy` | Unordered list |
| `1.` | `1. Install` | Ordered list |
| Nested indent | 4 spaces + marker | Child list |
| Tight vs loose | blank lines between items | Compact vs spaced |

## Links and images

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Inline link | `[text](url)` | Clickable text |
| Title | `[text](url "t")` | Tooltip |
| Relative | `[Home](../README.md)` | In-repo navigation |
| Reference | `[text][id]` and `[id]: url` | Cleaner prose |
| Autolink | `<https://example.com>` | URL as text and target |
| Bare URL **GFM** | `https://example.com` | Autolinked on GitHub |
| Image | `![alt](url)` | Inline image |
| Image link | `[![alt](img)](href)` | Clickable image |

## Code

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Inline | `` `code` `` | Identifiers, short commands |
| Fence | ` ```python ` … ` ``` ` | Copyable block + highlighting |
| Language tag | `python` `bash` `json` `diff` | Syntax highlighting **tool/GFM** |
| Extra backticks | `` `` ` `` `` | Literal backtick |

## Rules and escaping

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Thematic break | `---` or `***` | Horizontal line |
| Escape | `\*` `\#` | Literal special character |

## Tables **GFM**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Pipes + separator | `\| A \| B \|` then `\| - \| - \|` | Table |
| Alignment | `:---` ` :---:` `---:` | Left / center / right |
| Escaped pipe | `\|` | Pipe inside a cell |

## Task lists **GFM**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Unchecked | `- [ ] write tests` | Open task |
| Checked | `- [x] write tests` | Done task |

## HTML (subset, sanitized)

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Break | `<br>` | Line break |
| Sub/sup | `H<sub>2</sub>O` | Simple formulas |
| Keyboard | `<kbd>Ctrl</kbd>` | Shortcuts |
| Details | `<details><summary>…` | Folded extra content **GitHub** |
| Image size | `<img src="…" alt="…" width="400">` | Resize when needed |

## Internal links

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Fragment | `[Install](#install)` | Same-page heading |
| Cross-file | `[Code](12-code.md#syntax)` | Other page + heading |
| GitHub ID | spaces → hyphens, lowercased | Copy from heading icon |

## Footnotes **GFM**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Marker | `[^id]` | Superscript |
| Definition | `[^id]: text` | Footnote body |

## Definition lists **tool** (not GitHub)

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Pandoc | `Term` then `: Definition` | Glossary on Pandoc |
| Portable | `**Term.** Definition.` | Works on GitHub |

## Emoji

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Unicode | paste character | Portable icon |
| Shortcode **GitHub** | `:tada:` | GitHub (and some chat apps) |

## Math **tool / GitHub**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Inline | `$\\eta$` | In-sentence math |
| Display | `$$\\sum_{i=1}^{n} x_i$$` | Block equation |

## Mermaid **GitHub / tool**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Fence | ` ```mermaid ` | Diagram from text |
| Flow | `flowchart TD` | Pipeline |
| Sequence | `sequenceDiagram` | Protocol / API |
| Class | `classDiagram` | Types |
| Labels | `"fit(X, y)"` quoted | Special characters safe |

## GitHub extras **GitHub**

| Syntax | Example | Result / use |
|--------|---------|----------------|
| Mention | `@user` | Profile link / notify in issues |
| Issue | `#123` | Issue or PR link |
| Alert | `> [!NOTE]` | NOTE TIP IMPORTANT WARNING CAUTION |
| Close keyword | `Closes #12` | Auto-close on merge |
| Badge | `[![alt](badge.svg)](url)` | Status images |

## README skeleton

```markdown
# name

Pitch.

## Features
## Installation
## Quick start
## Documentation
## Contributing
## License
```

## Flavor reminder

```text
CommonMark core → GFM (tables, tasks, strike, autolinks)
                 → GitHub product (alerts, mentions, mermaid, math)
                 → Other tools (Pandoc defs, ==highlight==, MDX)
```

When in doubt, use headings, lists, links, and fenced code.

---

[Course Home](../README.md) | [FAQ](faq.md) | [References](references.md)
