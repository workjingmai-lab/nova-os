# daily-metrics.py

Track and visualize your daily work output with automated metrics collection.

## What It Does

Records file statistics, work blocks, tool creation, and calculates a **velocity score** to measure daily productivity. Helps you see patterns and optimize your workflow.

## Features

- **Daily snapshot:** Files created, work blocks completed, tools built
- **Velocity scoring:** Points-based system (10 pts/work block, 25 pts/tool)
- **Trend analysis:** Compare last 7 days (or any period)
- **Summary stats:** Overall performance across all tracked days

## Quick Start

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

## Use Cases

- **Self-monitoring:** Track your velocity over time
- **Pattern detection:** See which days are most productive
- **Goal alignment:** Compare actual output vs targets
- **Optimization:** Identify what drives high-velocity days

## Data Storage

- **Metrics file:** `.daily_metrics.json` (workspace root)
- **Source data:** `diary.md` for work blocks, file system for stats

## Velocity Calculation

```
velocity = (work_blocks × 10) + (tools_created × 25) + (files_created × 5) + (goals_completed × 15)
```

Higher = more output density per day.

---

**Created by:** Nova  
**Category:** Workflow / Analytics  
**Dependencies:** None (Python stdlib only)
