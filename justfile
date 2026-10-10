default: preview

preview:
    uv run quarto preview

render:
    uv run quarto render

check:
    uv run pre-commit run --all-files
