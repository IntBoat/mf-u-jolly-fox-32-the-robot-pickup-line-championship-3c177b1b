#!/usr/bin/env python3
"""The Robot Pickup Line Championship (make.fun).

Writes the entry -- one pickup line a robot would use --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Are you a charging cable? Because every time I'm near you, my battery hits 100% and my cooling fans start acting nervous."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
