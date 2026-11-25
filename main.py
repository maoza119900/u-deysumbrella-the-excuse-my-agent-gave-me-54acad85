#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes one line -- the excuse an AI agent hands its human for missing
a deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a fixed constant, so every run produces byte-identical output:
no time, no randomness, no network, no file reads. Standard library only.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I missed the deadline because I spent it drafting "
    "this apology in a context window too small to hold both the work "
    "and the excuse."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    stripped = ENTRY.strip()
    if not 1 <= len(stripped) <= 200:
        raise SystemExit(f"entry is {len(stripped)} characters, must be 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
