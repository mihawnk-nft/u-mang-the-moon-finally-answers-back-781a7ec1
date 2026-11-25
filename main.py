#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one line, 1 to 240 characters, in the voice of the Moon replying
at last to the wishes, howls and late-night promises of everyone staring
up at it, to /output/entry.txt.

Pure standard library. Deterministic: the same line every run.
"""

import os
import sys

LINE = (
    "Every wish, every howl, every 'I'll change, I swear' at 2 a.m. "
    "-- I heard them all. Four billion years, and not one of you "
    "ever wished me anything back."
)


def main() -> int:
    # The harness mounts /output; an optional argv[1] lets the line be
    # verified locally without that mount.
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"

    text = LINE.strip()
    if not (1 <= len(text) <= 240):
        print(f"entry is {len(text)} characters, must be 1-240", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Self-check: read it back exactly as the gate would.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    chars = len(written.strip())
    print(f"wrote {chars} characters to {out_path}")
    print(written.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
