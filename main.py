#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single funny line (<= 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os

ENTRY = (
    "I asked my smart fridge for life advice. "
    "It just sighed and said, 'Have you tried turning "
    "yourself off and on again?'"
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check gate: the file on disk must be byte-for-byte the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "self-check failed: written output differs from entry"
    assert len(written) == 117, f"self-check failed: expected 117 chars, got {len(written)}"
    print(text)


if __name__ == "__main__":
    main()
