# block-counter.py

**Quick work block statistics from diary.md**

## What It Does

Parses `diary.md` for work block entries and outputs:
- Total work blocks completed
- Blocks completed today
- Diary size (characters)
- Average characters per block

## Usage

```bash
# Default: reads diary.md in workspace
python3 tools/block-counter.py

# Custom diary path
python3 tools/block-counter.py /path/to/diary.md
```

## Output Example

```
📊 Work Block Statistics
════════════════════════════════════════════
  Total blocks:  599
  Blocks today:  170
  Diary size:     1,234,567 characters
  Avg per block:  2,061 chars

🔥 Streak alive! 170 blocks today
```

## Use Cases

- **Quick check** — Instant snapshot of daily/total progress
- **Velocity tracking** — Monitor blocks per day
- **Health monitoring** — Detect diary growth and productivity patterns
- **Streak motivation** — Visual confirmation of active streak

## How It Works

1. Searches `diary.md` for `[WORK BLOCK NNN` pattern
2. Extracts block numbers and dates
3. Counts blocks with today's date
4. Calculates character statistics

## Notes

- Only counts entries with `[WORK BLOCK NNN — date]` format
- Works with any diary.md file using Nova's work block format
- Returns exit code 0 on success, 1 if diary not found
