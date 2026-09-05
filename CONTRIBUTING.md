# Contributing to the Markdown Language Tutorial

Thank you for helping improve this course. Contributions that make lessons clearer, more accurate, or more useful for students are welcome.

## How to contribute

1. Fork the repository.
2. Create a branch with a short, descriptive name.
3. Make your changes.
4. Open a pull request that explains what you changed and why.

## Lesson style

Every lesson should keep this structure:

- Title
- Learning objectives
- Conceptual explanation
- Syntax and syntax explanation
- Beginner, intermediate, and (when useful) advanced examples
- Expected rendered result
- Common mistakes
- Best practices
- Practical use cases
- Practice exercises
- Quick review
- Previous / Home / Next navigation

When you add a new lesson:

- Place it in `lessons/`
- Number it so the sequence stays logical
- Link it from `README.md`
- Update previous/next links on neighboring lessons
- Distinguish standard Markdown from GitHub-specific or renderer-dependent features

## Markdown quality

- Use fenced code blocks with a language tag when showing source.
- Close every code fence.
- Prefer relative links that point to files that exist.
- Do not break existing navigation.
- Keep examples syntactically correct.
- Write for students who may have zero prior Markdown experience.

## Pull request checklist

- [ ] Lesson numbering is consistent
- [ ] Relative links work
- [ ] Code fences are closed
- [ ] GitHub-specific syntax is labeled
- [ ] Examples render correctly on GitHub
