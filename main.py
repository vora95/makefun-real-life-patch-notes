#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in real life /
human biology -- to /output/entry.txt, in the terse register of a
real release note.

The line (116 characters, under the 160-character cap):

    v2.9.1: fixed a bug where the eyes spotted a typo in someone
    else's message instantly but shipped three in your own.

Deterministic: same output on every run, no randomness, no network,
no clock, no environment-dependent behaviour. The output directory
comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
import sys

LINE = (
    "v2.9.1: fixed a bug where the eyes spotted a typo in someone "
    "else's message instantly but shipped three in your own."
)

MAX_CHARS = 160


def main() -> int:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
