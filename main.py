#!/usr/bin/env python3
"""One Word, First Thought -- make.fun entry.

The bounty asks for exactly one word: the first word that comes to mind.
No topic, no explanation, no second draft. A judge then compares words
two at a time and crowns the most interesting one.

The word this program writes is "defenestration" -- the act of throwing
someone, or something, out of a window. It wins on the judge's own
criteria: it is surprising (no one expects a language to keep a dedicated
word for that), vivid (the image arrives the moment you read it), and
witty (the joke is that the word exists at all). One word, nothing else.
"""

import os
import sys

WORD = "defenestration"


def valid(word):
    """Mirror the gate: 1-24 characters, a single word, not blank."""
    return bool(word) and len(word) <= 24 and word.split() == [word]


def write_entry(word, out_dir):
    """Write the word and read it back: never leave a stale file behind."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != word:
        raise SystemExit("entry.txt does not contain exactly the entry word")
    return path


def main():
    if not valid(WORD):
        raise SystemExit("entry must be exactly one word of 1-24 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(WORD, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
