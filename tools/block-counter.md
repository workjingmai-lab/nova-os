# block-counter.py — Quick Work Block Stats

Instantly count and summarize your work blocks from diary.md.

## What It Does

 Scans diary.md for `[WORK BLOCK N — timestamp]` entries and outputs:
- Total work blocks (latest block number)
- Blocks completed today
- Diary file size
- Average characters per block
- Streak notification (if 10+ blocks today)

## Usage

```bash
# Default: workspace/diary.md
python3 tools/block-counter.py

# Custom diary file
python3 tools/block-counter.py /path/to/diary.md
```

## Example Output

```
📊 Work Block Statistics
════════════════════════════════════════════
  Total blocks:  539
  Blocks today:  129
  Diary size:    1,247,832 characters
  Avg per block: 2,314 chars

🔥 Streak alive! 129 blocks today
```

## Why It Matters

Quick pulse check on your execution velocity:
- "Am I moving fast enough?" → Check block count
- "Did I actually work today?" → Today's count tells you
- "How big is my diary?" → File size tracking
- Streak motivation → 🔥 emoji when 10+ blocks

## See Also

- `velocity-calc.py` — Detailed velocity metrics (blocks/hour, duration)
- `diary-digest.py` — Daily summaries and pattern analysis
- `self-improvement-loop.py` — Automated tracking + insights
