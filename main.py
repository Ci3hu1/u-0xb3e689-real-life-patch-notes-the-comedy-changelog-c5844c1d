#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog entry.

Writes one patch-note line to /output/entry.txt: a software changelog
entry for a bug in real life -- the brain replaying your most embarrassing
memory from 2009 every night at 3 a.m.

Pure standard library. Deterministic: the same line every run.
The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space.
"""

import os
import sys

LINE = "v3.0.0: fixed a bug where the brain replayed your most embarrassing memory from 2009 every night at 3 a.m."


def main() -> None:
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise SystemExit(
            f"line is {len(LINE)} characters, outside the 1-160 gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
