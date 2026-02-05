# blocks-to-go.py — Milestone Progress Checker

Quick progress check for the 2000-block milestone.

## What It Does

Shows:
- Current block count (reads from diary.md)
- Percentage complete to 2000
- Blocks remaining
- ETA at 3 velocity scenarios (sustained 44/hr, burst 55/hr, current session pace)

## Usage

```bash
python3 tools/blocks-to-go.py
```

## Example Output

```
🎯 2000-Block Milestone Progress
==================================================
Current: 1907 blocks (95.35%)
Target: 2000 blocks
Remaining: 93 blocks

📊 Velocity Scenarios:
  Sustained (44/hr): 2.1hr → ~10:23 UTC
  Burst (55/hr):     1.7hr → ~09:58 UTC
  Current (67/hr):   1.4hr → ~09:39 UTC

💪 Keep going! 93 blocks to milestone!
```

## Why It Exists

Milestone tracking creates urgency and visibility. Quick check → know how far to go → maintain momentum.

## Dependencies

- Reads `diary.md` for current block count
- Uses regex to find latest work block number
- No external dependencies (standard library only)

---

*Created: 2026-02-05*
*Category: Utilities*
