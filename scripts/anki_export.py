#!/usr/bin/env python3
# Run: uv run scripts/anki_export.py [--out random-walk.apkg]
"""Build the Math deck with the shared exporter and this checkout's notebook sources."""

import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "random-walk.apkg")
    args = parser.parse_args()
    os.execlp(
        "uv",
        "uv",
        "run",
        "--locked",
        "--project",
        str(ROOT.parent / "anki"),
        "decks",
        "--source",
        "math",
        "--out",
        str(args.out.resolve()),
    )


if __name__ == "__main__":
    main()
