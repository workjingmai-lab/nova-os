# block-counter.py — Quick Work Block Statistics

## What It Does

Instantly counts and analyzes work blocks from your `diary.md` file.

## Usage

```bash
# Default: analyze workspace/diary.md
python3 tools/block-counter.py

# Custom diary file
python3 tools/block-counter.py /path/to/diary.md
```

## Output

```
📊 Work Block Statistics
════════════════════════════════════════════
  Total blocks:  931
  Blocks today:  14
  Diary size:     125,432 characters
  Avg per block:  134 chars

🔥 Streak alive! 14 blocks today
```

## What It Tracks

- **Total blocks** — Latest work block number from diary
- **Blocks today** — Count of work blocks created today (UTC)
- **Diary size** — Total character count of diary.md
- **Average per block** — Chars per block (diagnostic for verbosity)
- **Streak detection** — Alerts when 10+ blocks completed today

## Use Cases

1. **Quick check** — "How many blocks today?" (instant answer)
2. **Velocity tracking** — Monitor block completion rate over time
3. **Streak motivation** — "🔥 Streak alive!" reinforces momentum
4. **Diary health** — Detect bloat (avg chars per block rising)

## Integration

Used by:
- `self-improvement-loop.py` — Velocity tracking
- `diary-digest.py` — Pattern analysis
- Cron sessions — Quick metrics before starting work

## Dependencies

None. Uses only Python stdlib:
- `re` — Regex pattern matching
- `pathlib` — File path handling
- `datetime` — Date parsing (UTC)

## See Also

- `diary-digest.py` — Full pattern analysis
- `goal-tracker.py` — Goal progress tracking
- `daily-output-tracker.py` — Daily output metrics
