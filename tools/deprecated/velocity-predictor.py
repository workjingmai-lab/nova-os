#!/usr/bin/env python3
"""Velocity Predictor - forecast near-term work block output.

Goal: quick-and-dirty forecasting, not statistics.

Usage:
  python3 tools/velocity-predictor.py                 # last 24h baseline
  python3 tools/velocity-predictor.py --hours 6       # baseline window
  python3 tools/velocity-predictor.py --next 12       # forecast horizon (hours)

Output:
  - recent blocks/hour baseline
  - projected blocks in the next N hours

Notes:
  - Parses `[WORK BLOCK <n> — <iso8601>]` headers from diary.md.
  - Assumes timestamps are ISO-8601; supports trailing 'Z'.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")


@dataclass(frozen=True)
class Block:
    n: int
    t: datetime


def _parse_dt(ts: str) -> datetime | None:
    ts = ts.strip()
    try:
        if ts.endswith("Z"):
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            # treat naive timestamps as UTC
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def parse_blocks(path: Path = DIARY_PATH) -> list[Block]:
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    # Example: [WORK BLOCK 376 — 2026-02-02T01:52Z]
    patt = re.compile(r"\[WORK BLOCK (\d+) — ([^\]]+)\]")

    blocks: list[Block] = []
    for m in patt.finditer(text):
        n = int(m.group(1))
        dt = _parse_dt(m.group(2))
        if dt is None:
            continue
        blocks.append(Block(n=n, t=dt))

    return sorted(blocks, key=lambda b: b.n)


def blocks_in_window(blocks: list[Block], window_hours: float, now: datetime) -> list[Block]:
    cutoff = now - timedelta(hours=window_hours)
    return [b for b in blocks if b.t >= cutoff and b.t <= now]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=24.0, help="baseline window size")
    ap.add_argument("--next", type=float, default=24.0, help="forecast horizon")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    blocks = parse_blocks()

    if not blocks:
        print("No work blocks found in diary.md")
        return

    recent = blocks_in_window(blocks, args.hours, now)
    if len(recent) < 2:
        print(f"Not enough blocks in the last {args.hours:g}h to estimate velocity (need 2+).")
        print(f"Total blocks in diary: {len(blocks)}")
        return

    duration_h = (recent[-1].t - recent[0].t).total_seconds() / 3600
    if duration_h <= 0:
        print("Recent duration is zero; cannot estimate velocity.")
        return

    v = len(recent) / duration_h
    proj = v * args.next

    print("📈 Velocity Predictor")
    print(f"Baseline window: last {args.hours:g}h")
    print(f"Recent blocks: {len(recent)} (from #{recent[0].n} to #{recent[-1].n})")
    print(f"Estimated velocity: {v:.2f} blocks/hour")
    print(f"Forecast horizon: next {args.next:g}h")
    print(f"Projected blocks: {proj:.1f}")


if __name__ == "__main__":
    main()
