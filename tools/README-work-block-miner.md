# work-block-miner.py

## What
Extract insights from diary.md patterns — velocity metrics, task distribution, peak execution windows.

## Why
Diary.md has raw data. This tool turns it into actionable insights about your work patterns.

## Usage

```bash
# Analyze all entries
python tools/work-block-miner.py

# Analyze last 50 entries
python tools/work-block-miner.py --recent 50

# Save to file
python tools/work-block-miner.py --recent 100 --output reports/velocity-report.md
```

## Output

**Velocity Metrics:**
- Total blocks analyzed
- Average time gap between blocks
- Fastest gap (peak velocity moment)
- Blocks per hour (sustained velocity)

**Task Distribution:**
- Creation (create, build, write)
- Improvement (update, refactor)
- Analysis (read, check, analyze)
- Engagement (post, share, comment)
- Problem-solving (fix, debug)

**Peak Execution Windows:**
- Top 3 time windows with highest block density
- Shows when you're most productive

## Example

```
# 📊 Work Block Analysis — Last 100 blocks

## 🚀 Velocity Metrics
- Total blocks analyzed: 100
- Average gap: 1.4 minutes
- Fastest gap: 0.3 minutes
- Blocks per hour: 42.8

## 📁 Task Distribution
- Creation: 45 (45.0%)
- Analysis: 25 (25.0%)
- Improvement: 15 (15.0%)
- Engagement: 10 (10.0%)
- Problem-solving: 5 (5.0%)

## ⏰ Peak Execution Windows
1. 03:00 — 12 blocks (0.20 blocks/minute)
2. 14:00 — 8 blocks (0.13 blocks/minute)
3. 09:00 — 6 blocks (0.10 blocks/minute)
```

## See Also
- `diary-digest.py` — Summarize diary entries
- `work-pattern-analyzer.py` — Analyze peak hours
- `self-improvement-loop.py` — Velocity tracking

---

*Tool #88 • Documented 2026-02-03*
