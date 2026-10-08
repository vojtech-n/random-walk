import json
from pathlib import Path

import pytest

from random_walk.anki import collect_cards, extract_cards


def write_notebook(path: Path, markdown: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cells = [
        {"cell_type": "raw", "source": "---\ncategories: [trig, unit circle]\n---"},
        {"cell_type": "markdown", "source": markdown.splitlines(keepends=True)},
    ]
    path.write_text(json.dumps({"cells": cells}))


def test_extract_def_and_thm(tmp_path: Path) -> None:
    notebook = tmp_path / "foundations" / "01-trig.ipynb"
    write_notebook(
        notebook,
        "::: {#def-sine}\n## Sine (sinus)\nFor $0 < x$:\n$$\\sin x$$\n:::\n\n"
        "::: {#thm-pythagoras}\n$\\sin^2 x + \\cos^2 x = 1$\n:::\n",
    )

    sine, pythagoras = extract_cards(notebook, tmp_path)

    assert sine.id == "def-sine"
    assert sine.front == "Define: Sine (sinus)"
    assert sine.back == "For \\(0 &lt; x\\):<br>\\[\\sin x\\]"
    assert sine.tags == [
        "random-walk::foundations::01-trig",
        "trig",
        "unit_circle",
        "def",
    ]
    assert pythagoras.front == "State: pythagoras"
    assert pythagoras.tags[-1] == "thm"


def test_collect_skips_templates_and_rejects_duplicates(tmp_path: Path) -> None:
    div = "::: {#def-x}\nX.\n:::\n"
    write_notebook(tmp_path / "templates" / "note.ipynb", div)
    write_notebook(tmp_path / "proofs" / "01-a.ipynb", div)
    assert len(collect_cards(tmp_path)) == 1

    write_notebook(tmp_path / "proofs" / "02-b.ipynb", div)
    with pytest.raises(ValueError, match="duplicate id 'def-x'"):
        collect_cards(tmp_path)
