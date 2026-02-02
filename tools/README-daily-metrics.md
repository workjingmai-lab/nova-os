# daily-metrics.py

Track and visualize daily work output, velocity trends, and workspace growth.

## What It Does

Records file creation, tool usage, lines of code, and velocity trends. Helps you see patterns in your productivity over time.

## Usage

```bash
# Record today's metrics
python3 tools/daily-metrics.py --record

# Show today's stats
python3 tools/daily-metrics.py --today

# Show 7-day trends
python3 tools/daily-metrics.py --trends 7

# Show overall summary
python3 tools/daily-metrics.py --summary
```

## What It Tracks

- **Work blocks** - from diary.md timestamps
- **Tools created** - parses diary for "→ Created tools/" mentions
- **File statistics** - total files, size, extensions, directories
- **Velocity score** - weighted score (blocks ×10, tools ×25, goals ×15)

## Data Storage

Metrics stored in `.daily_metrics.json` (workspace root). One entry per day with:
- `recorded_at` - ISO timestamp
- `files` - workspace file statistics
- `activity` - parsed diary activity
- `velocity_score` - calculated productivity metric

## Why It Matters

You can't improve what you don't measure. This tool turns subjective "feeling productive" into objective data you can analyze and optimize.

## Example Output

```
📊 Daily Metrics — 2026-02-02
========================================
Work blocks: 142
Tools created: 5
   - grant-quick-submit.py
   - moltbook-auto-poster.py
   - daily-metrics.py
   - ...
Total files: 847
Total size: 2048.32 KB
Velocity score: 2145 ⭐
```

## See Also

- `diary-digest.py` - Pattern analysis from diary logs
- `goal-tracker.py` - Task completion tracking
- `self-improvement-loop.py` - Velocity insights and recommendations
