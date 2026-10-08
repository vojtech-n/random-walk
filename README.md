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
- Preview the site: `uv run quarto preview`
- Run checks: `uv run pre-commit run --all-files`

## License

Code: [MIT](LICENSE). Notes: [CC BY 4.0](LICENSE-CONTENT).

Built with help from [Claude Code](https://claude.com/claude-code).
