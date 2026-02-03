# block-counter.py

**Quick work block statistics from diary.md**

## What It Does

Counts work blocks in your diary.md and generates instant metrics:
- Total work blocks (lifetime)
- Blocks today
- Diary size (character count)
- Average characters per block

## Usage

```bash
# Count from default diary.md
python tools/block-counter.py

# Count from custom diary
python tools/block-counter.py path/to/diary.md
```

## Output Example

```
📊 Work Block Statistics
══════════════════════════════════════════
  Total blocks:  718
  Blocks today:  195
  Diary size:    1,234,567 characters
  Avg per block: 1,719 chars

🔥 Streak alive! 195 blocks today
```

## Use Cases

- **Morning check-in:** See yesterday's total
- **Mid-day status:** Quick progress check
- **Session handoff:** Give another agent context on your work volume
- **Streak motivation:** Visual confirmation you're maintaining momentum

## How It Works

1. Parses diary.md for `[WORK BLOCK NNN — timestamp]` patterns
2. Extracts the latest block number (your lifetime total)
3. Counts blocks with today's date
4. Calculates character metrics
5. Shows streak message if 10+ blocks today

## Integration

Used by:
- `daily-report.py` — Includes work block count in daily summaries
- `task-navigator.py` — Uses block count for velocity calculations
- `session-starter.py` — Shows work volume during session initialization

## See Also

- `diary-digest.py` — Full pattern analysis from diary
- `work-block-miner.py` — Advanced work pattern insights
- `today-summary.py` — Human-readable daily summary

**Category:** Analytics | **Status:** Stable | **Last Updated:** 2026-02-02
