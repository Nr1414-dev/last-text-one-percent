#!/usr/bin/env python3
"""Last Text at One Percent — writes the dying phone's final text.

The entry is one short final text message, under 200 characters, in the
voice of a phone at one percent battery. The program writes exactly that
one line to /output/entry.txt and nothing else.
"""

import os

TEXT = "I died mid-swipe. He was a 6. You can do better. Goodbye."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate guard: the entry must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: what was written must be byte-identical to TEXT.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "read-back mismatch"


if __name__ == "__main__":
    main()
