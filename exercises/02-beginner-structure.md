# Exercise set 2 — Lists, links, images, and code

**Level:** Beginner  
**Lessons:** [08](../lessons/08-lists.md)–[13](../lessons/13-horizontal-rules-escaping.md)

[← Previous set](01-beginner-syntax.md) | [Exercises home](README.md) | [Course Home](../README.md) | [Next set →](03-intermediate.md)

---

## Goals

Create `exercises/work/02-lab-prep.md` for a fictional programming lab.

## Exercises

### 1. Materials (unordered)

List five tools or libraries as bullets. Put each name in inline code if it is a command or package.

### 2. Procedure (ordered)

Write six install-or-run steps. Use `1.` on every item in the source. Confirm the rendered list still shows 1–6 on GitHub.

### 3. Nested list

Under step 3, nest two OS-specific substeps (Windows / macOS or Linux). Indent with four spaces.

### 4. Links

- One external HTTPS link with descriptive text
- One relative link to [../README.md](../README.md)
- One reference-style link defined at the bottom of the file

### 5. Image and image link

Add:

```markdown
![Diagram of the compile-run-test loop](../assets/dev-loop.png)
```

Then make a second copy that is clickable and opens the same path. You do not need a real PNG for the exercise, but you should write honest alt text.

### 6. Code

- Mention `pytest` inline
- A `bash` fence with two commands
- A `python` fence with a 4-line function
- A `diff` fence that changes a default port from 8000 to 8080

### 7. Escaping

Show the characters `*italic*` literally once with backslashes and once with inline code.

### 8. Horizontal rule

Separate "Setup" from "Appendix" with `***`, not with a Setext underline.

## Self-check

- [ ] Nested list actually nests on GitHub
- [ ] No reversed link brackets
- [ ] Every fence is closed
- [ ] Alt text is not a filename
- [ ] Relative path to the course home is correct from `exercises/work/` (`../../README.md`) if you placed the file there

## Stretch

Put the Python fence **inside** list item 6. Indent it so the list does not break.
