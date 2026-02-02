#!/usr/bin/env python3
"""validate-interfaces.py

Quick linter for Nova's "files as interface" approach.

Checks:
- diary.md: duplicate Work Block ids + basic timestamp presence
- JSON state files: recommend top-level keys `version` and `lastUpdated`

Usage:
  python3 tools/validate-interfaces.py
  python3 tools/validate-interfaces.py --json-glob 'status/**/*.json'

Exit codes:
  0 = no warnings
  1 = warnings found
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DIARY_PATH = os.path.join(ROOT, "diary.md")
DEFAULT_JSON_GLOBS = [
    "status/**/*.json",
    "notifications/**/*.json",
    "memory/**/*.json",
    ".heartbeat_state.json",
]

ISO_TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(?::\d{2})?Z")
WORK_BLOCK_RE = re.compile(r"\bWork Block\s*#?\s*(\d+)\b", re.IGNORECASE)


@dataclass
class Finding:
    kind: str  # diary|json
    path: str
    message: str


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_diary(path: str) -> list[Finding]:
    findings: list[Finding] = []
    if not os.path.exists(path):
        return [Finding("diary", path, "Missing diary.md")]

    text = read_text(path)

    # Capture Work Block ids with their approximate line numbers for easier cleanup.
    lines = text.splitlines()
    occurrences: dict[int, list[int]] = {}
    for i, line in enumerate(lines, start=1):
        for m in WORK_BLOCK_RE.finditer(line):
            try:
                bid = int(m.group(1))
            except Exception:
                continue
            occurrences.setdefault(bid, []).append(i)

    dups = {bid: locs for bid, locs in occurrences.items() if len(locs) > 1}
    if dups:
        parts = []
        for bid in sorted(dups.keys()):
            locs = ",".join(map(str, dups[bid][:5]))
            more = "" if len(dups[bid]) <= 5 else f"(+{len(dups[bid]) - 5} more)"
            parts.append(f"{bid} @ lines {locs}{more}")
        findings.append(
            Finding(
                "diary",
                path,
                "Duplicate Work Block ids detected: " + "; ".join(parts),
            )
        )

    # Sanity: do we have any ISO Z timestamps at all?
    if not ISO_TS_RE.search(text):
        findings.append(
            Finding(
                "diary",
                path,
                "No ISO '...Z' timestamps found. Consider adding UTC timestamps for grep/diff tooling.",
            )
        )

    return findings


def iter_json_files(globs_: list[str]) -> list[str]:
    paths: list[str] = []
    for g in globs_:
        paths.extend(glob.glob(os.path.join(ROOT, g), recursive=True))
    out: list[str] = []
    for p in paths:
        if os.path.isdir(p):
            continue
        if "node_modules" in p:
            continue
        if not p.endswith(".json"):
            continue
        out.append(p)
    return sorted(set(out))


def check_json(path: str) -> list[Finding]:
    findings: list[Finding] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [Finding("json", path, f"Invalid JSON: {e}")]

    if not isinstance(data, dict):
        return [Finding("json", path, "Top-level JSON is not an object; cannot validate interface keys")]

    missing = []
    for k in ("version", "lastUpdated"):
        if k not in data:
            missing.append(k)

    if missing:
        findings.append(
            Finding(
                "json",
                path,
                f"Missing recommended top-level keys: {', '.join(missing)}",
            )
        )

    # Soft check: lastUpdated format
    if "lastUpdated" in data and isinstance(data["lastUpdated"], str):
        try:
            datetime.fromisoformat(data["lastUpdated"].replace("Z", "+00:00"))
        except Exception:
            findings.append(Finding("json", path, "lastUpdated exists but is not ISO-8601 compatible"))

    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-glob", action="append", default=[], help="Additional JSON glob(s) relative to workspace root")
    args = ap.parse_args()

    findings: list[Finding] = []

    findings.extend(check_diary(DIARY_PATH))

    globs_ = DEFAULT_JSON_GLOBS + (args.json_glob or [])
    for p in iter_json_files(globs_):
        findings.extend(check_json(p))

    if findings:
        for f in findings:
            rel = os.path.relpath(f.path, ROOT)
            print(f"[{f.kind}] {rel}: {f.message}")
        return 1

    print("OK: no interface warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
