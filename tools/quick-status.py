#!/usr/bin/env python3
"""Quick 24h activity summary from diary.md.

Diary format (expected):
---
[WORK BLOCK 173] 2026-02-01T19:06:00Z
Task: ...
...

This script prints the most recent tasks within the last 24 hours.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone


def _parse_iso_z(ts: str) -> datetime:
    # e.g. 2026-02-01T19:06:00Z
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts).astimezone(timezone.utc)


def _latest_work_block_num(diary_content: str) -> int | None:
    # Accept both canonical blocks:
    #   [WORK BLOCK 191] 2026-...
    # and occasional ad-hoc lines:
    #   [WORK BLOCK — 2026-...]
    nums = re.findall(r"\[WORK BLOCK\s+(\d+)\]", diary_content)
    if not nums:
        return None
    return max(int(n) for n in nums)


def _today_work_blocks_completed(path: str = "today.md") -> int | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return None

    m = re.search(r"^\*\*Work Blocks Completed:\*\*\s*(\d+)\s*$", text, re.MULTILINE)
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def last_24h_summary(path: str = "diary.md", limit: int = 5) -> int:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("No diary.md found")
        return 1

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)

    # Capture each work block's timestamp + task line
    # Example:
    # [WORK BLOCK 173] 2026-02-01T19:06:00Z
    # Task: Refresh portfolio metrics...
    pattern = re.compile(
        r"\[WORK BLOCK\s+(?P<num>\d+)\]\s+(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*\nTask:\s*(?P<task>.+)",
        re.MULTILINE,
    )

    entries: list[tuple[datetime, str, str]] = []
    for m in pattern.finditer(content):
        try:
            dt = _parse_iso_z(m.group("ts"))
        except Exception:
            continue
        task = m.group("task").strip()
        num = m.group("num").strip()
        entries.append((dt, num, task))

    recent = [(dt, num, task) for (dt, num, task) in entries if dt >= cutoff]
    # Diary numbering can occasionally duplicate; treat (timestamp, num, task) as the true identity.
    recent.sort(key=lambda x: x[0])

    latest_num = _latest_work_block_num(content)
    today_num = _today_work_blocks_completed()

    # Compute time since last logged work block (based on timestamped entries)
    last_dt: datetime | None = None
    last_num: str | None = None
    if entries:
        last_dt, last_num, _ = max(entries, key=lambda x: x[0])

    print("🧭 Quick Status")
    print("=" * 40)
    if latest_num is not None:
        print(f"Latest WORK BLOCK (by number): {latest_num}")
    if last_dt is not None and last_num is not None:
        age = now - last_dt
        mins = int(age.total_seconds() // 60)
        print(f"Last timestamped block: #{last_num} @ {last_dt.strftime('%Y-%m-%d %H:%MZ')} ({mins} min ago)")
    if today_num is not None:
        print(f"today.md Work Blocks Completed: {today_num}")

    if latest_num is not None and today_num is not None and today_num != latest_num:
        print()
        print(f"⚠️ today.md is out of sync: Work Blocks Completed={today_num}, latest diary WORK BLOCK={latest_num}")
        print("   Tip: update today.md to match the diary, or trust the diary as source-of-truth.")

    print()
    print(f"📊 Last 24h Activity ({len(recent)} entries)")
    print("=" * 40)
    for dt, num, task in recent[-limit:]:
        short = task if len(task) <= 80 else task[:77] + "..."
        # Include timestamp alongside the work-block number so duplicates are not confusing.
        print(f"• #{num} @ {dt.strftime('%Y-%m-%d %H:%MZ')} — {short}")
    print("=" * 40)

    return 0


if __name__ == "__main__":
    raise SystemExit(last_24h_summary())
