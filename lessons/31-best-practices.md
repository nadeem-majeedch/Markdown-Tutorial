# Lesson 31 — Best practices

[← Previous Lesson](30-common-mistakes.md) | [Course Home](../README.md) | [Next Lesson →](32-accessibility.md)

---

## Learning objectives

By the end of this lesson you will be able to:

- Apply a consistent Markdown style to a project
- Structure files so they stay maintainable
- Write for scanning, not only for linear reading
- Keep documentation honest as code changes
- Use a short style guide with your team

## Conceptual explanation

Best practices are habits that keep documents **correct, scannable, and kind to the next reader** (including you in six months).

They are not about clever syntax. You already know enough syntax. This lesson is about judgment.

Four principles:

1. **Clarity over cleverness** — portable syntax, short headings, obvious links
2. **Structure over decoration** — headings mean outline; emphasis is rare
3. **Examples over adjectives** — show the command, do not say "easy"
4. **Maintenance over dump** — a living file beats a perfect file that is never updated

## A practical style guide

You can paste this into a team `docs/style.md`:

```markdown
# Markdown style

- ATX headings (`#`)
- One H1 per file
- Do not skip heading levels
- Unordered lists use `-`
- Fenced code with a language tag
- Relative links inside the repo
- Descriptive link text (no "click here")
- Alt text on every meaningful image
- Line wrap optional; blank lines between blocks required
- GFM tables for small matrices only
```

## Syntax habits that pay off

### Put a blank line around blocks

````markdown
## Install

```bash
pip install -e .
```

Then run `pytest`.
````

### Lead with the action

Bad: "It should be noted that users may wish to consider running tests."

Good:

````markdown
Run the tests:

```bash
pytest -q
```
````

### Keep lists parallel

Bad:

- Installing Python
- you should create a venv
- `pip install -r requirements.txt`

Good:

- Install Python 3.12
- Create a virtual environment
- Install requirements

## Beginner example

Before:

```markdown
#welcome
this project is a thing for data. **click** [here](https://example.com) for stuff. ```python
print(1)```
```

After:

````markdown
# Data widget

Small Python helpers for CSV cleanup.

See the [usage guide](docs/usage.md).

```python
print(1)
```
````

**Expected rendered result**

A title, a pitch, a meaningful link, a proper fence. The "after" file is what professional repos look like.

## Intermediate example: scanning

People scan README files. Help them:

```markdown
# medscan

Preprocessing for DICOM teaching sets.

## Who it is for

Teaching labs that cannot use identifiable patient images.

## What it does

- Strips selected metadata
- Resizes to a teaching resolution
- Writes PNG previews

## What it does not do

- It is not a PACS
- It is not a diagnostic tool
```

Negative scope (`does not do`) prevents misuse. That is a documentation best practice, not a syntax trick.

## Advanced example: docs in the same PR

Expert teams treat documentation as part of the change:

```text
feat: add --seed flag

- CLI: --seed int
- README quick start updated
- docs/reference.md table updated
```

If the flag ships without the README, the project just became dishonest. Markdown skill includes **process**, not only punctuation.

### File length

| File | Comfortable length |
|------|--------------------|
| README | 1–3 screens, then links |
| Lesson / how-to | One topic |
| Changelog entry | A handful of bullets |
| ADR | 1–2 pages |

When a file needs a TOC, it might also need to be split.

## Common mistakes

- Style-guide lawyering (`*` vs `-`) while the install command is wrong
- Inconsistent naming: `set_up.md` vs `setup.md` vs `install.md`
- Copy-pasted warnings in five files that drift apart — link instead
- Mixing American/British spelling randomly (pick one per repo)
- Commenting-out old Markdown with `<!-- huge block -->` forever

## Best practices (checklist)

- One idea per heading
- Working examples you have run
- Relative links, descriptive text, alt text
- Language-tagged fences
- Honest scope and requirements
- Update docs in the same change as the code
- Preview on GitHub
- Prefer rewriting over decorating

## Practical use cases

- Course team GitHub orgs
- Open-source first README
- Lab protocol library
- This curriculum's own lesson template

## Practice exercises

1. Write a 10-line style guide for your next group project.
2. Take a dense paragraph of instructions and rewrite it as a numbered list plus one fence.
3. Add a "What it does not do" section to a fictional README.
4. Review a public open-source README against this lesson's checklist. List two strengths and two gaps.

## Quick review

- Best practice is structure, honesty, and maintenance
- Style guides prevent bikeshedding
- Scan-friendly pages beat ornate pages
- Docs change with code
- Clarity over cleverness

---

[← Previous Lesson](30-common-mistakes.md) | [Course Home](../README.md) | [Next Lesson →](32-accessibility.md)
