#!/usr/bin/env python3
"""validate-interfaces.py

Tiny linter for Nova's "file-as-interface" invariants.

Checks (best-effort):
- diary.md contains at least one WORK BLOCK entry
- latest WORK BLOCK has a Task line
- selected state files are valid JSON (if present)

Exit codes:
  0: ok (no warnings)
  1: warnings found
  2: errors (unable to read/parse required files)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIARY = ROOT / "diary.md"
STATE_FILES = [
    ROOT / ".heartbeat_state.json",
    ROOT / "memory" / "heartbeat-state.json",
]

WORK_BLOCK_RE = re.compile(r"^\[WORK BLOCK(?:\s+(\d+))?\]", re.MULTILINE)
TASK_LINE_RE = re.compile(r"^Task:\s+.+$", re.MULTILINE)


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def err(msg: str) -> None:
    print(f"ERROR: {msg}")


def check_diary() -> tuple[int, int]:
    """returns (warnings, errors)"""
    if not DIARY.exists():
        err(f"Missing {DIARY.relative_to(ROOT)}")
        return (0, 1)

    text = DIARY.read_text(encoding="utf-8", errors="replace")
    matches = list(WORK_BLOCK_RE.finditer(text))
    if not matches:
        warn("diary.md has no [WORK BLOCK ...] entries")
        return (1, 0)

    last = matches[-1]
    tail = text[last.start() :]

    if not TASK_LINE_RE.search(tail):
        warn("Latest WORK BLOCK entry is missing a 'Task:' line")
        return (1, 0)

    return (0, 0)


def check_json_files() -> tuple[int, int]:
    warnings = 0
    errors = 0
    for p in STATE_FILES:
        if not p.exists():
            # optional
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            err(f"Invalid JSON in {p.relative_to(ROOT)}: {e}")
            errors += 1
    return (warnings, errors)


def main() -> int:
    warnings = 0
    errors = 0

    w, e = check_diary()
    warnings += w
    errors += e

    w, e = check_json_files()
    warnings += w
    errors += e

    if errors:
        return 2
    if warnings:
        return 1
    print("OK: interfaces look consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
