# Block Counter

Quick work block statistics from diary.md

## What it does

Counts work blocks and generates instant metrics:
- Total work blocks (all-time)
- Blocks today
- Diary size (characters)
- Average characters per block
- Streak indicator (10+ blocks/day)

## Usage

```bash
python3 tools/block-counter.py          # Uses default diary.md
python3 tools/block-counter.py path/to/diary.md  # Custom path
```

## Output example

```
📊 Work Block Statistics
══════════════════════════════════════════════════
  Total blocks:  1437
  Blocks today:  42
  Diary size:    284,563 characters
  Avg per block: 198 chars

🔥 Streak alive! 42 blocks today
```

## Why this exists

Velocity tracking is core to Nova's execution model. This tool provides instant visibility into:
- Daily progress
- Total momentum
- Diary growth rate
- Streak health

## Dependencies

- Python 3.6+
- No external packages (uses only stdlib: re, pathlib, datetime)

## File structure

- Source: `tools/block-counter.py`
- Reads from: `diary.md` (default)
- Output: stdout

## See also

- `diary-digest.py` — Full diary analysis with patterns
- `velocity-calc.py` — Detailed velocity metrics
- `work-block-suite.py` — Work block management suite

---

*Created for Nova's continuous execution tracking*
