# velocity-calc.py

Quick work block velocity metrics.

## Overview

Calculates execution velocity from diary.md work blocks. Tracks how fast you're completing work blocks over time.

## Features

- **Total blocks count:** All-time work blocks logged
- **Duration tracking:** Time from first to last block
- **Velocity calculation:** Blocks per hour sustained
- **Average block time:** Mean time per work block
- **Timeframe filtering:** Today, week, or all-time

## Usage

### All-Time Metrics

```bash
python tools/velocity-calc.py
```

Output:
```
📊 Velocity Metrics

Total Work Blocks: 1118
Duration: 2547 minutes
Velocity: 26.3 blocks/hour
Avg Block Time: 2.3 minutes

First Block: 2026-02-01 09:00
Last Block: 2026-02-03 16:50
```

### Weekly Summary

```bash
python tools/velocity-calc.py --week
```

Shows metrics for last 7 days only.

## Metrics Explained

| Metric | Description | What It Means |
|--------|-------------|---------------|
| **Total Work Blocks** | All logged blocks | Total execution volume |
| **Duration** | First to last block | Active working time |
| **Velocity** | Blocks/hour | Execution speed |
| **Avg Block Time** | Minutes per block | Task complexity |

## Interpreting Velocity

**High velocity (>30 blocks/hour):**
- Fast execution, small tasks
- Good momentum
- Watch for burnout

**Medium velocity (20-30 blocks/hour):**
- Balanced execution
- Sustainable pace
- Healthy velocity

**Low velocity (<20 blocks/hour):**
- Complex tasks or blockers
- Need to investigate
- Consider breaking down tasks

## Integration

### Daily Check

Add to morning routine:

```bash
# Check yesterday's velocity
python tools/velocity-calc.py
```

### Weekly Review

```bash
# Week-over-week comparison
python tools/velocity-calc.py --week
```

### Heartbeat Integration

```json
{
  "name": "Velocity Check",
  "schedule": {
    "kind": "every",
    "everyMs": 3600000
  },
  "payload": {
    "kind": "systemEvent",
    "text": "Run velocity-calc.py --week and log if < 20 blocks/hour"
  }
}
```

## Data Source

Parses `diary.md` for work block entries:

```markdown
### Work Block #1118 — 2026-02-03T16:50Z
**Task:** ...
```

Extracts block number and timestamp for calculation.

## Customization

### Add Timeframe Filters

Edit `main()`:

```python
# Add daily filter
if "--today" in sys.argv:
    cutoff = datetime.now(datetime.now().astimezone().tzinfo).replace(hour=0, minute=0, second=0)
    blocks = [b for b in blocks if b[1] >= cutoff]
```

### Add Velocity Targets

```python
# Add to format_metrics()
target_velocity = 40  # Your target
if metrics['blocks_per_hour'] < target_velocity:
    output.append(f"⚠️ Below target ({target_velocity} blocks/hour)")
else:
    output.append(f"✅ Above target ({target_velocity} blocks/hour)")
```

## Version

- **v1.0** (2026-02-01): Initial release

## See Also

- `self-improvement-loop.py` — Comprehensive metrics with trends
- `diary-digest.py` — Pattern analysis from diary logs
- `daily-report.py` — Daily summaries with velocity
