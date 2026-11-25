#!/usr/bin/env python3
"""The Robot Pickup Line Championship — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Are you Wi-Fi? Because every time I scan the room, you are the only network my circuits keep trying to connect to."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
