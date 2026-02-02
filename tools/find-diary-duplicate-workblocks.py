#!/usr/bin/env python3
"""Find duplicate Work Block IDs in diary.md.

Goal: support validate-interfaces finding that some Work Block numbers repeat.
This script is intentionally conservative: it only reports duplicates with line numbers
and nearby header text so a follow-up renumbering can be done safely.

Usage:
  python3 tools/find-diary-duplicate-workblocks.py [path/to/diary.md]

Exit codes:
  0 = no duplicates found
  2 = duplicates found
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass


# Match formats like:
#   "Work Block 123"
#   "WORK BLOCK 123"
#   "Work Block #123"
# Avoid matching timestamp formats like "WORK BLOCK — 2026-02-02...".
WORKBLOCK_RE = re.compile(
    r"(?i)\bwork\s*block\b\s*(?:#\s*)?(?P<id>\d{1,6})\b"
)


@dataclass
class Hit:
    line_no: int
    line: str


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "diary.md"
    try:
        text = open(path, "r", encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 1

    hits: dict[int, list[Hit]] = defaultdict(list)

    for i, line in enumerate(text, start=1):
        m = WORKBLOCK_RE.search(line)
        if not m:
            continue
        wb = int(m.group("id"))
        hits[wb].append(Hit(i, line.rstrip()))

    dupes = {k: v for k, v in hits.items() if len(v) > 1}

    if not dupes:
        print("OK: no duplicate Work Block IDs detected")
        return 0

    print("DUPLICATE Work Block IDs detected:\n")
    for wb in sorted(dupes):
        print(f"- Work Block {wb} appears {len(dupes[wb])} times")
        for hit in dupes[wb]:
            print(f"    line {hit.line_no}: {hit.line}")
        print()

    print(
        "Next: decide a renumbering policy (e.g., keep earliest occurrence, renumber later ones),\n"
        "then implement a safe patcher that updates both headers and any internal references." 
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
