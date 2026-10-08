# random-walk

Vojtěch's personal math & statistics notes, written as Jupyter notebooks.

## Setup

```sh
brew install quarto
uv sync
uv run pre-commit install
uv tool install nbdime nbstripout
nbdime config-git --enable
nbstripout --install
```

## Use

- Plan and progress: [ROADMAP.md](ROADMAP.md).
- Symbols and LaTeX: `reference/symbols.qmd`.
- New note: copy `templates/note.ipynb` into a topic folder.
- Site: https://vojtech-n.github.io/random-walk/ (deployed on push to `main`).
- Preview the site: `uv run quarto preview`
- Run checks: `uv run pre-commit run --all-files`
- Anki deck from def/thm divs: `uv run scripts/anki_export.py`. Div ids must be unique across notes.

## License

Code: [MIT](LICENSE). Notes: [CC BY 4.0](LICENSE-CONTENT).

Built with help from [Claude Code](https://claude.com/claude-code).
