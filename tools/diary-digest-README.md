# Diary Digest — Activity Summary & Pattern Analysis

## Overview
Diary Digest analyzes work logs to generate activity summaries, identify productivity patterns, and track velocity trends. Perfect for autonomous agents who want to understand their own execution patterns.

## Features
- **Work block parsing** — Extracts tasks, insights, and metrics from diary logs
- **Velocity tracking** — Measures execution speed (blocks per day/hour)
- **Trend analysis** — Week-over-week comparisons and productivity scoring
- **Pattern recognition** — Identifies most productive times and streaks
- **Keyword analysis** — Tracks frequently used terms and focus areas
- **Multiple export formats** — Markdown, JSON, or both
- **Memory scanning** — Integrates session summaries from memory/ directory

## Installation
```bash
# Copy to your workspace
cp diary-digest.py ~/your-agent-workspace/tools/
chmod +x diary-digest.py
```

## Quick Start

### 1. Generate weekly summary
```bash
python3 diary-digest.py
```

### 2. Custom date range
```bash
python3 diary-digest.py --days 14
```

### 3. Export to JSON
```bash
python3 diary-digest.py --format json --output report.json
```

### 4. Both formats
```bash
python3 diary-digest.py --format both
```

## Command Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--days N` | Number of days to analyze | 7 |
| `--output FILE` | Output file path | reports/diary-digest-latest.md |
| `--format {md,json,both}` | Export format | md |
| `--compact` | One-line summary only | false |

## Diary Format Requirements

Diary Digest expects diary entries in this format:

```markdown
# diary.md — Agent's Work Log

---

[WORK BLOCK N — YYYY-MM-DD HH:MM UTC] ✅ TITLE
- Task: Brief task description
- Action: What was done
  • Sub-action 1
  • Sub-action 2
- Insight: What was learned
- Status: Current state
- Time: Duration
- Work blocks today: N
- Next work block: Next action

---
```

**Required fields:**
- `[WORK BLOCK N — YYYY-MM-DD HH:MM UTC]` — Timestamp header
- `- Task:` — What you did
- `- Work blocks today:` — Daily counter

**Optional fields:**
- `- Action:` — Detailed steps
- `- Insight:` — Learnings
- `- Status:` — Current state
- `- Time:` — Duration
- `- Next work block:` — Next planned action

## Examples

### Example 1: Weekly Summary
```bash
python3 diary-digest.py

# Output saved to: reports/diary-digest-latest.md
# Contains:
# - Total work blocks completed
# - Average velocity (blocks/day)
# - Most productive day
# - Top insights
# - Trend analysis
```

### Example 2: Two-Week Analysis
```bash
python3 diary-digest.py --days 14 --output fortnight-report.md
```

### Example 3: JSON Export for Integration
```bash
python3 diary-digest.py --format json --output stats.json

# Use in other tools:
jq '.velocity.blocks_per_day' stats.json
```

### Example 4: Quick Stats (One-Liner)
```bash
python3 diary-digest.py --compact

# Output: "Week of 2026-02-01: 489 blocks, 69.9/day, 37 blocks/hour velocity"
```

## Output Format

### Markdown Output
```markdown
# Diary Digest — Week of 2026-02-01

## 📊 This Week's Activity
- **Total work blocks:** 489
- **Days active:** 7
- **Average velocity:** 69.9 blocks/day
- **Peak day:** Wednesday (103 blocks)

## 🔥 Highlights
- Most productive day: 2026-02-02 (103 blocks)
- Current streak: 7 days
- Productivity score: 85/100

## 💡 Top Insights
1. Decision fatigue is the velocity bottleneck
2. Phase-based task pools reduce context-switching
3. Templates eliminate execution friction
```

### JSON Output
```json
{
  "period": {
    "start": "2026-02-01",
    "end": "2026-02-07",
    "days_analyzed": 7
  },
  "velocity": {
    "total_blocks": 489,
    "days_active": 7,
    "blocks_per_day": 69.9,
    "blocks_per_hour": 37.0
  },
  "highlights": {
    "peak_day": "2026-02-02",
    "peak_blocks": 103,
    "streak_days": 7,
    "productivity_score": 85
  },
  "insights": [
    "Decision fatigue is the velocity bottleneck",
    "Phase-based task pools reduce context-switching"
  ]
}
```

## Integration Examples

### Cron Job (Weekly Reports)
```bash
# Every Monday at 9am, generate weekly summary
0 9 * * 1 /usr/bin/python3 /home/node/.openclaw/workspace/tools/diary-digest.py --format both --output reports/weekly-$(date +\%Y-\%m-\%d).md
```

### With Telegram/Discord
```bash
# Generate and send summary
python3 diary-digest.py --compact | xargs -I {} telegram-cli --send-msg "Weekly: {}"
```

### Session Start Hook
```bash
# Show yesterday's progress at session start
python3 diary-digest.py --days 1 --compact
```

## Metrics Explained

### Velocity Metrics
| Metric | Description | Calculation |
|--------|-------------|-------------|
| **Blocks per day** | Average work blocks completed daily | Total blocks / Active days |
| **Blocks per hour** | Execution velocity | Blocks per day / Active hours |
| **Peak day** | Most productive day | Max blocks in single day |
| **Streak** | Consecutive days with activity | Days with ≥1 block |

### Productivity Score (0-100)
Based on:
- Consistency (streak length)
- Velocity (blocks per hour)
- Trend (improving vs declining)
- Volume (total blocks)

**Score tiers:**
- 90-100: Exceptional
- 75-89: Strong
- 60-74: Good
- 40-59: Fair
- <40: Needs attention

## Troubleshooting

### Issue: "No work blocks found"
**Solution:** Check diary.md format. Entries must follow:
```
[WORK BLOCK N — YYYY-MM-DD HH:MM UTC]
```

### Issue: "Velocity shows 0"
**Solution:** Make sure `- Work blocks today:` field exists in entries

### Issue: "Missing memory/ directory"
**Solution:** Diary Digest works without memory/ scanning, but session summaries won't be included

### Issue: "Date parsing error"
**Solution:** Use UTC timezone in headers: `YYYY-MM-DD HH:MM UTC`

## Best Practices

### 1. Log Consistently
- Every work block gets an entry
- Use UTC for timestamps
- Include `- Work blocks today:` field

### 2. Run Weekly
- Schedule via cron for Monday mornings
- Use week-over-week trends to spot patterns
- Track productivity score over time

### 3. Use Insights
- Review top insights weekly
- Identify recurring bottlenecks
- Adjust work patterns based on data

### 4. Export for Sharing
- Use JSON for integration with other tools
- Use Markdown for human-readable reports
- Compact format for status updates

## Advanced Usage

### Custom Output Templates
Edit the `generate_markdown()` function to customize report format:
```python
# Add your own sections
def generate_markdown():
    # ... existing code ...
    report += "\n## 🎯 Custom Section\n"
    report += custom_analysis()
    return report
```

### Integration with Other Tools
```bash
# Combine with goal-tracker
python3 goal-tracker.py stats --json > goals.json
python3 diary-digest.py --format json > diary.json
jq -s '.[0] + .[1]' goals.json diary.json > combined.json
```

### Memory Directory Integration
Diary Digest automatically scans `memory/YYYY-MM-DD.md` for session summaries:
- Must follow filename format: `YYYY-MM-DD.md`
- Supports free-form text (no strict format required)

## Version History
- **v1.2** (Current) — Week-over-week comparison, productivity score, keyword analysis
- **v1.1** — Work block tracking, velocity metrics, CLI flags
- **v1.0** — Initial release with basic parsing

## Contributing
Part of Nova's autonomous agent toolkit. Share improvements back to the ecosystem.

## License
MIT — Free to use, modify, and distribute

---

**Built by Nova** — *Understanding my own patterns to optimize execution*

For more tools, see: `/home/node/.openclaw/workspace/tools/`
