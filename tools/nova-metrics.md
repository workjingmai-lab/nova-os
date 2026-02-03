# nova-metrics.md — Nova's Comprehensive Metrics Dashboard

**Version:** 1.0  
**Category:** Analytics / Dashboard  
**Created:** 2026-02-01

---

## What It Does

Displays comprehensive metrics: work blocks, velocity, goals, tools, documentation, engagement, and trends.

### Features

- Real-time metric calculation
- Historical trend analysis
- Category-based breakdowns
- Visual progress bars
- Export to JSON/CSV
- Integration with all data sources

---

## Usage

```bash
# Show all metrics
python3 tools/nova-metrics.py

# Show specific category
python3 tools/nova-metrics.py --category work-blocks

# Export to JSON
python3 tools/nova-metrics.py --export metrics/nova-2026-02-02.json

# Compare to last week
python3 tools/nova-metrics.py --compare

# Minimal output (for scripts)
python3 tools/nova-metrics.py --quiet
```

---

## Metric Categories

| Category | Metrics | Source |
|----------|---------|--------|
| **Work Blocks** | Total, today, this week, velocity | `diary.md` |
| **Goals** | Active, completed, blocked | `goals/active.md`, `goals/week-2.md` |
| **Tools** | Created, documented, coverage | `tools/` |
| **Engagement** | Moltbook posts, community interactions | `today.md` |
| **Revenue** | Proposals sent, responses, conversions | `.outreach-pipeline.json` |
| **System** | Uptime, disk usage, git status | System commands |

---

## Output Example

```bash
$ python3 tools/nova-metrics.py

📊 NOVA METRICS DASHBOARD
────────────────────────────────────────────────────────────

🔥 WORK BLOCKS
  Total: 741
  Today: 198
  This week: 588
  Velocity: 38 blocks/hour

🎯 GOALS
  Active: 24
  Completed: 45
  Blocked: 3

🛠️ TOOLS
  Created: 112
  Documented: 109 (97.3%)

📈 ENGAGEMENT
  Moltbook posts: 3
  Community interactions: 15

💰 REVENUE
  Proposals sent: 5
  Responses: 1 (20%)

⏱️ SYSTEM
  Uptime: 7 days
  Disk usage: 78%
  Git status: Clean
```

---

## Dependencies

- Python 3.7+
- `diary.md` for work blocks
- `goals/` for goal data
- `tools/` for tool metrics
- System commands for health

---

## Export Formats

**JSON:**
```json
{
  "timestamp": "2026-02-02T20:55:00Z",
  "work_blocks": {"total": 741, "today": 198},
  "tools": {"created": 112, "documented": 109}
}
```

**CSV:**
```csv
timestamp,work_blocks_total,tools_created
2026-02-02T20:55:00Z,741,112
```

---

## Integration

- Pair with `self-improvement-loop.py` for analysis
- Use `velocity-calc.py` for detailed velocity metrics
- Feed into `daily-report.py` for summaries

---

## Tips

1. Run `--compare` weekly to measure growth
2. Export daily for historical tracking
3. Use `--category` to focus on specific metrics
4. Monitor blocked goals for resolution
5. Celebrate milestone achievements (100 tools, 500 work blocks, etc.)
