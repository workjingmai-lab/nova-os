#!/usr/bin/env python3
"""Refresh a couple of headline metrics in PORTFOLIO.md from today.md.

Keeps this intentionally small + safe:
- Updates total Work Blocks in PORTFOLIO.md (2 locations)

Usage:
  python3 tools/refresh-portfolio-metrics.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = ROOT / "today.md"
ACTIVE_GOALS = ROOT / "goals" / "active.md"
TOOLS_INDEX = ROOT / "tools" / "INDEX.md"
PORTFOLIO = ROOT / "PORTFOLIO.md"
SKILLS = ROOT / "skills.md"


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def main() -> int:
    today = read_text(TODAY)
    m = re.search(r"^\*\*Work Blocks Completed:\*\*\s*(\d+)\s*$", today, flags=re.M)
    if not m:
        raise SystemExit("Could not find 'Work Blocks Completed' in today.md")

    total_blocks = int(m.group(1))

    active_goals = read_text(ACTIVE_GOALS)
    gm = re.search(r"\*\*Progress:\*\*\s*(\d+)/(\d+)", active_goals)
    if not gm:
        raise SystemExit("Could not find 'Progress: X/Y' in goals/active.md")
    goals_done = int(gm.group(1))
    goals_total = int(gm.group(2))

    tools_index = read_text(TOOLS_INDEX)
    tm = re.search(r"^-\s*\*\*Total tools:\*\*\s*([^\n]+)\s*$", tools_index, flags=re.M)
    if not tm:
        raise SystemExit("Could not find 'Total tools' in tools/INDEX.md")
    tools_built = tm.group(1).strip()

    skills_text = read_text(SKILLS) if SKILLS.exists() else ""
    skills = [
        re.sub(r"^\s*-\s*", "", line).strip()
        for line in skills_text.splitlines()
        if re.match(r"^\s*-\s*\S", line)
    ]
    skills_count = len(skills)
    skills_list = ", ".join(skills)

    portfolio = read_text(PORTFOLIO)
    updated = portfolio

    # 1) Core Expertise → OpenClaw Operations line
    updated = re.sub(
        r"(\*\*Continuous execution model:\*\*\s*)(\d+)(\s*work blocks executed\s*\(Week 1:\s*\d+,\s*Week 2:\s*\d+\))",
        rf"\g<1>{total_blocks}\g<3>",
        updated,
        count=1,
    )

    # 2) Key Metrics section line: Work Blocks
    updated = re.sub(
        r"(^-\s*\*\*Work Blocks:\*\*\s*)(\d+)(\s*$)",
        rf"\g<1>{total_blocks}\g<3>",
        updated,
        flags=re.M,
        count=1,
    )

    # 3) Key Metrics section line: Goals Completed
    updated = re.sub(
        r"(^-\s*\*\*Goals Completed:\*\*\s*)(\d+)/(\d+)(.*$)",
        rf"\g<1>{goals_done}/{goals_total}\g<4>",
        updated,
        flags=re.M,
        count=1,
    )

    # 4) Key Metrics section line: Tools Built
    updated = re.sub(
        r"(^-\s*\*\*Tools Built:\*\*\s*)([^\n]+?)(\s*$)",
        rf"\g<1>{tools_built}\g<3>",
        updated,
        flags=re.M,
        count=1,
    )

    # 5) Key Metrics section line: Skills Learned
    updated = re.sub(
        r"(^-\s*\*\*Skills Learned:\*\*\s*)(\d+)(.*$)",
        rf"\g<1>{skills_count} ({skills_list})",
        updated,
        flags=re.M,
        count=1,
    )

    if updated == portfolio:
        print("No changes needed.")
        return 0

    PORTFOLIO.write_text(updated, encoding="utf-8")
    print(
        "Updated PORTFOLIO.md: "
        f"Work Blocks -> {total_blocks}; "
        f"Goals Completed -> {goals_done}/{goals_total}; "
        f"Tools Built -> {tools_built}; "
        f"Skills Learned -> {skills_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
