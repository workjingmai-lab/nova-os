# Agent Productivity Score

Calculate a productivity score from diary/heartbeat logs. Measure your output velocity, consistency, and completion rate.

## Features

- **Overall score (0-100)** — Based on volume, consistency, and completion
- **Productivity tiers** — Legendary, Elite, Pro, Active, Building, Starting
- **Work block tracking** — Counts completed work blocks from logs
- **Activity analysis** — Entry types, hourly distribution, active days
- **Flexible input** — Reads from file or stdin

## Usage

```bash
# Analyze diary.md
python3 tools/agent-productivity-score.py diary.md

# Read from stdin
cat diary.md | python3 tools/agent-productivity-score.py --stdin

# Analyze specific date range
sed -n '/2026-02-01/,/2026-02-02/p' diary.md | python3 tools/agent-productivity-score.py --stdin
```

## Score Calculation

The overall score (0-100) combines three factors:

1. **Volume (40 pts)** — Total entries normalized to 50
2. **Consistency (30 pts)** — Active days normalized to 1 week
3. **Completion (30 pts)** — Task completion rate ×2

## Productivity Tiers

| Score | Tier | Description |
|-------|------|-------------|
| 90+ | 🏆 Legendary | Exceptional output and consistency |
| 75+ | 🌟 Elite | High velocity, strong track record |
| 60+ | ⚡ Pro | Solid productivity, reliable execution |
| 40+ | 🔥 Active | Consistent work, building momentum |
| 20+ | 💪 Building | Starting out, establishing patterns |
| <20 | 🌱 Starting | New agent, early days |

## Expected Log Format

The tool parses timestamped entries in this format:

```
[TYPE] YYYY-MM-DDThh:mm:ssZ
Entry content here
---
```

Example:
```
[WORK BLOCK 500] 2026-02-02T12:00:00Z
Created README for goal-tracker.py
---
```

## Example Output

```
==================================================
📊 AGENT PRODUCTIVITY REPORT
==================================================

Overall Score: 87/100
Tier: 🌟 Elite

📈 METRICS
  Total Entries: 547
  Work Blocks: 482
  Completed Tasks: 312
  Active Days: 7

📝 ENTRY TYPES
  WORK BLOCK       482 ████████████████████
  HEARTBEAT         42 ███
  UPDATE            23 ██

⏰ ACTIVITY BY HOUR
  Peak Activity: 13:00 (67 entries)

==================================================
```

## Use Cases

1. **Weekly reviews** — Check productivity trends over time
2. **Self-assessment** — Understand your work patterns
3. **Goal tracking** — Correlate score with goal completion
4. **Optimization** — Identify peak hours for deep work

## Integration

Works seamlessly with:
- `diary-digest.py` — For pattern analysis
- `self-improvement-loop.py` — For velocity tracking
- `goal-tracker.py` — For goal correlation

## Created

2026-02-02 — Part of Week 2 continuous improvement toolkit
