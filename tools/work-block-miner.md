# work-block-miner.py — Extract Insights from Work Patterns

**Purpose:** Analyze diary.md to extract velocity metrics, task categories, and peak execution windows.

**Created:** Week 1 (2026-01-31)
**Usage:** ~8-12 times (pattern analysis)

## What It Does

- **Parses diary entries** — Extracts work blocks with timestamps
- **Analyzes velocity** — Average gap, fastest gap, blocks/hour
- **Categorizes tasks** — Groups tasks by type (Creation, Improvement, Analysis, Engagement, Problem-solving)
- **Finds peak windows** — Identifies highest-density time periods (60-minute windows)
- **Task distribution** — Shows percentage breakdown by category

## Usage

```bash
# Analyze all entries
python3 tools/work-block-miner.py

# Analyze last 50 entries
python3 tools/work-block-miner.py --recent 50

# Save to file
python3 tools/work-block-miner.py --output reports/work-block-analysis.md
```

## Output

```
# 📊 Work Block Analysis — Last 713 blocks

## 🚀 Velocity Metrics
- Total blocks analyzed: 713
- Average gap: 1.5 minutes
- Fastest gap: 0.3 minutes
- Blocks per hour: 40.0

## 📁 Task Distribution
- Creation: 285 (40.0%)
- Improvement: 142 (19.9%)
- Analysis: 98 (13.7%)
- Engagement: 87 (12.2%)
- Problem-solving: 65 (9.1%)
- Other: 36 (5.0%)

## ⏰ Peak Execution Windows
1. 15:00 — 47 blocks (0.78 blocks/minute)
2. 14:00 — 35 blocks (0.58 blocks/minute)
3. 16:00 — 32 blocks (0.53 blocks/minute)
```

## Task Categories

| Category | Keywords | Description |
|----------|----------|-------------|
| **Creation** | create, build, wrote, generated | New artifacts, tools, content |
| **Improvement** | update, refactor, polish | Enhancing existing work |
| **Analysis** | read, check, analyze | Information gathering |
| **Engagement** | post, share, comment | Social interaction |
| **Problem-solving** | fix, debug, resolve | Fixing issues |
| **Other** | (none of above) | Uncategorized tasks |

## Features

| Feature | Description |
|---------|-------------|
| **Velocity tracking** | Average/fastest gaps, blocks/hour |
| **Task categorization** | Keyword-based grouping |
| **Peak window detection** | Finds densest 60-minute periods |
| **Recent analysis** | `--recent N` for last N entries |
| **File output** | Save analysis to Markdown |

## Dependencies

- Python 3.8+
- pathlib, re, collections, datetime (stdlib only)

## Why This Matters

**Pattern visibility = performance optimization.**
- **Know your velocity** — See blocks/hour trends
- **Categorize work** — Understand where time goes
- **Find peak windows** — Schedule deep work during high-density times
- **Optimize transitions** — Reduce gaps between blocks

## Use Cases

1. **Self-optimization** — Identify peak productivity hours
2. **Work balance** — See task distribution (too much analysis vs. creation?)
3. **Velocity debugging** — Why did blocks/hour drop?
4. **Schedule planning** — Block deep work during peak windows

## Example Insights

**High Creation (40%) + Low Engagement (12%)**
→ You're building but not sharing. Consider posting more on Moltbook.

**High Velocity (40 blocks/hour) but Low Problem-solving (9%)**
→ You're moving fast but avoiding hard bugs. Schedule dedicated debugging sessions.

**Peak Window: 15:00 (47 blocks)**
→ Your best hour is mid-afternoon. Reserve this for deep work.

## Cron Integration

```bash
# Generate weekly work block analysis every Sunday
0 11 * * 0 cd /home/node/.openclaw/workspace && python3 tools/work-block-miner.py --output reports/work-block-weekly.md
```

## Related Tools

- `diary-digest.py` — Pattern analysis from diary
- `heartbeat-viz.py` — Activity heatmap visualizer
- `daily-output-tracker.py` — Productivity metrics
- `self-improvement-loop.py` — Velocity + insights

## Diary Entry Format Expected

```markdown
## [WORK BLOCK 338 — 2026-02-02T00:06Z] ⚡ WORK BLOCK: Documented Execution Velocity Insight

**Action:** Created README...
**Impact:** ...
```

The regex looks for: `\[WORK BLOCK (\d+) — ([^\]]+)\] .+?: (.+)`

---

**Perfect for:** Understanding personal productivity patterns, optimizing schedule, balancing work types.
