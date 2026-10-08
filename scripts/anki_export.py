#!/usr/bin/env python3
# Run: uv run scripts/anki_export.py [--out random-walk.apkg]
import argparse
from pathlib import Path
from typing import Any

import genanki as untyped_genanki  # pyright: ignore[reportMissingTypeStubs]

from random_walk.anki import collect_cards

# Any: genanki ships no type hints.
genanki: Any = untyped_genanki

ROOT = Path(__file__).resolve().parent.parent
# Fixed IDs: Anki matches decks and note types by ID on re-import.
DECK_ID = 1_726_404_118
MODEL_ID = 1_726_404_119

MODEL = genanki.Model(
    MODEL_ID,
    "random-walk",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[
        {
            "name": "Card",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }
    ],
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export def/thm divs to an Anki deck.")
    parser.add_argument("--out", type=Path, default=ROOT / "random-walk.apkg")
    args = parser.parse_args()

    deck = genanki.Deck(DECK_ID, "random-walk")
    cards = collect_cards(ROOT)
    for card in cards:
        deck.add_note(
            genanki.Note(
                model=MODEL,
                fields=[card.front, card.back],
                tags=card.tags,
                guid=genanki.guid_for(card.id),
            )
        )
    genanki.Package(deck).write_to_file(args.out)
    print(f"{len(cards)} cards -> {args.out}")


if __name__ == "__main__":
    main()
