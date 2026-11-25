#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest -- make.fun entry.

Writes one joke line about crypto and trading life (under 200
characters) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Gate: the file must be UTF-8 text of 1-200 characters, not only
whitespace. The program prints only the character count, never the
line itself, so the entry text stays out of logs.

The line is fixed and deterministic: the same bytes on every run.
Its shape follows the judge brief -- a recognisable trading detail
(buying the dip) as the setup, with the turn landing on the last
words (the portfolio is a staircase going down).
"""

import os
import sys

LINE = "I kept buying the dip until I realised I don't own a portfolio, I own the staircase."


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > 200 or "\n" in line:
        print("gate: line invalid", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
