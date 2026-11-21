#!/usr/bin/env python3
"""Write a single relaxing, awe-leaning text to /output/entry.txt."""

import os

TEXT = (
    "For ten thousand years, rain has come to this lake, "
    "one soft drop at a time. Nothing hurries. Nothing is kept. "
    "Only the water rises, patient and clear, until the whole "
    "still surface holds the sky without trying."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT + "\n")
    print(f"wrote {len(TEXT)} characters (+1 newline) to /output/entry.txt")
    print(TEXT)


if __name__ == "__main__":
    main()
