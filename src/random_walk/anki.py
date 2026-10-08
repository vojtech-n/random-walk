import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DIV_OPEN = re.compile(r"^::: *\{#(def|thm)-([\w-]+)\}\s*$")
DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH = re.compile(r"\$(.+?)\$")
CATEGORIES = re.compile(r"^categories:\s*\[(.*)\]\s*$", re.MULTILINE)
PROMPTS = {"def": "Define", "thm": "State"}


@dataclass(frozen=True)
class Card:
    id: str
    front: str
    back: str
    tags: list[str]


def to_anki_html(text: str) -> str:
    escaped = html.escape(text.strip(), quote=False)
    escaped = DISPLAY_MATH.sub(r"\\[\1\\]", escaped)
    escaped = INLINE_MATH.sub(r"\\(\1\\)", escaped)
    return escaped.replace("\n", "<br>")


def _source(cell: dict[str, Any]) -> str:
    source: str | list[str] = cell["source"]
    return "".join(source) if isinstance(source, list) else source


def extract_cards(notebook: Path, root: Path) -> list[Card]:
    # Any: notebook JSON is untyped.
    cells: list[dict[str, Any]] = json.loads(notebook.read_text())["cells"]
    relative = notebook.relative_to(root).with_suffix("")
    tags = ["random-walk::" + "::".join(relative.parts)]
    if cells and cells[0]["cell_type"] == "raw":
        match = CATEGORIES.search(_source(cells[0]))
        if match:
            categories = [c.strip() for c in match[1].split(",")]
            tags += [c.replace(" ", "_") for c in categories if c]

    cards: list[Card] = []
    for cell in cells:
        if cell["cell_type"] != "markdown":
            continue
        lines = _source(cell).splitlines()
        i = 0
        while i < len(lines):
            match = DIV_OPEN.match(lines[i])
            i += 1
            if not match:
                continue
            kind, slug = match[1], match[2]
            body: list[str] = []
            while i < len(lines) and lines[i].strip() != ":::":
                body.append(lines[i])
                i += 1
            title = slug
            if body and body[0].startswith("## "):
                title = body.pop(0).removeprefix("## ").strip()
            cards.append(
                Card(
                    id=f"{kind}-{slug}",
                    front=f"{PROMPTS[kind]}: {to_anki_html(title)}",
                    back=to_anki_html("\n".join(body)),
                    tags=[*tags, kind],
                )
            )
    return cards


def collect_cards(root: Path) -> list[Card]:
    cards: list[Card] = []
    seen: dict[str, Path] = {}
    for notebook in sorted(root.glob("*/*.ipynb")):
        if notebook.parent.name == "templates":
            continue
        for card in extract_cards(notebook, root):
            if card.id in seen:
                other = seen[card.id]
                raise ValueError(f"duplicate id {card.id!r} in {notebook} and {other}")
            seen[card.id] = notebook
            cards.append(card)
    return cards
