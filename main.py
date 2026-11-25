#!/usr/bin/env python3
"""The One-Liner Groan-Off — write one original dad joke to /output/entry.txt.

Gate: /output/entry.txt, UTF-8, 1-140 characters, not only whitespace, one line.
"""
import os

ENTRY = "I asked my wife what she wanted for dinner. She said, 'Surprise me.' So I hid the leftovers."
MAX_CHARS = 140


def validate(text):
    """Check the entry against the gate before writing it."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return text


def describe():
    """One line about the joke, for the README and the build log."""
    return "One original dad joke: a dinner-table setup whose punchline takes 'surprise me' literally."


def write_entry(path):
    text = validate(ENTRY)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    text = write_entry(path)
    print("Wrote %d chars to %s — %s" % (len(text), path, describe()))


if __name__ == "__main__":
    main()
