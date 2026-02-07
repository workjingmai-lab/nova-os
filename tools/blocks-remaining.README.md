# blocks-remaining.py

**Purpose:** Calculate remaining blocks to milestone with ETA

## Usage

```bash
# Default: Show remaining to 3000-block milestone
python3 tools/blocks-remaining.py

# Custom target
python3 tools/blocks-remaining.py 3300

# Custom target and velocity
python3 tools/blocks-remaining.py 3000 50
```

## What It Does

- Reads current block count from `diary.md` (most recent work block entry)
- Calculates remaining blocks to target milestone
- Estimates ETA based on velocity (default: 44 blocks/hr)
- Shows percentage complete, weekly surplus, and motivational message

## Example Output

```
🎯 MILESTONE: 3,000 blocks
📍 Current: 2,940 blocks (98.0%)
⏳ Remaining: 60 blocks
🚀 Velocity: 44 blocks/hr
⏱️  ETA: 1h 21m
📊 Weekly surplus: +2,640 blocks

🔥 FINAL SPRINT! 60 blocks to go!
```

## Why It Exists

During final sprints to milestones (like 3000 blocks), quick visibility into remaining work helps maintain focus and momentum. This tool provides instant feedback on progress without manual calculation.

## Integration

- Use in cron jobs for automatic milestone tracking
- Add to status dashboards for real-time progress
- Call from other scripts for milestone-based logic

## See Also

- `velocity-calc.py` — Detailed velocity analysis and predictions
- `diary.md` — Source of truth for current block count
