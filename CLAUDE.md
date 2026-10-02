# random-walk

Personal math & statistics notes. Each note is one `.ipynb`, rendered with Quarto.

## Notes

- Location: `<topic>/NN-slug.ipynb`, e.g. `probability/03-bayes-theorem.ipynb`. Topics: `calculus`, `linear-algebra`, `probability`, `statistics`. Add a topic folder when needed.
- Start every note from `templates/note.ipynb`. Keep its first raw cell: Quarto front matter with `title`, `source`, `date`, `categories`.
- Math: LaTeX in markdown cells.
- Definitions and theorems: Quarto cross-ref divs `::: {#def-slug}` and `::: {#thm-slug}`. Intuition: `.callout-tip`.
- Exercises: an `## Exercises` section at the end. Each solution sits in a `.callout-note` with `collapse="true"`.
- Commit notebooks without outputs. The `nbstripout` pre-commit hook strips them.

## Code

- Logic used by more than one note goes in `src/random_walk/`, with a test in `tests/`. Notebooks import it: `from random_walk import ...`.
- Add a library with `uv add <pkg>` only when a note needs it.
- Done means `uv run pre-commit run --all-files` and `uv run quarto render` both pass.
