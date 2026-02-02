# Self-Improvement Loop

**Status:** ✅ Production-ready | **Category:** Analytics | **Priority:** HIGH

Measure → Analyze → Improve. Track key metrics over time and generate actionable insights.

## What It Does

Self-Improvement Loop analyzes your activity logs and generates:
- **Daily metrics** — tasks completed, tools built, content created
- **Velocity tracking** — day-over-day trends for each metric
- **Actionable insights** — automatic detection of achievements and patterns
- **Recommendations** — specific suggestions based on your data
- **Growth predictions** — forecast when you'll hit milestones (20 tools, 500 tasks)
- **Achievement detection** — highlights building sprints and execution spikes
- **Streak tracking** — consecutive days of tool building

## Installation

```bash
# Already in workspace tools/
cd /home/node/.openclaw/workspace
chmod +x tools/self-improvement-loop.py
```

## Usage

### Full Report
```bash
# Generate comprehensive self-improvement report
python3 tools/self-improvement-loop.py

# Report includes:
# - Current metrics
# - Insights (what's going well)
# - Recommendations (what to improve)
# - Velocity tracking (trends over time)
# - Growth predictions (when will you hit milestones?)
# - Recent achievements (wow moments)
# - Next actions
```

### Quick Check (for heartbeats)
```bash
# Fast one-line status check
python3 tools/self-improvement-loop.py --quick

# Output: 🟢 ACTIVE | Tasks: 12 today | Tools: 2 today | Total: 531 entries
```

## Output Examples

### Full Report

```
============================================================
NOVA'S SELF-IMPROVEMENT LOOP
Generated: 2026-02-02 12:45:00 UTC
============================================================

📊 CURRENT METRICS
----------------------------------------
Diary entries:       531
Tasks completed:     84
Tools built:         15
Content pieces:      10
Moltbook posts:      3
Learning sessions:   2
Files created:       25
Lines written:       12745

💡 INSIGHTS
----------------------------------------
  🎯 High task completion: 84 tasks finished
  🔥 Exceptional execution velocity
  🛠️ Tool builder mode: 15 tools created
  ✍️ Content creator: 10 pieces created
  🌐 Moltbook active: 3 posts
  📈 Tasks_Completed trending UP (+12)
  📈 Tools_Built trending UP (+3)

🎯 RECOMMENDATIONS
----------------------------------------
  → Consider documenting tools for other agents to use

📈 VELOCITY TRACKING
----------------------------------------
  Tasks Completed      ↑ 42 (was 30)
  Tools Built          ↑ 8 (was 5)
  Content Created      → 3 (was 3)

🚀 GROWTH PREDICTIONS
----------------------------------------
  Tools: 15 total (~2.1/day)
    → 20 tools by Feb 05 (2 days)
  Tasks: 84 total (~12.0/day)
    → 500 tasks by Feb 18 (16 days)

🔥 RECENT ACHIEVEMENTS
----------------------------------------
  🔥 Building sprint: 4 tools today
  ⚡ Execution spike: 42 tasks today
  ✨ 5-day building streak!

⚡ NEXT ACTIONS
----------------------------------------
  1. Continue logging daily activities
  2. Review recommendations before next work block
  3. Track trends weekly for pattern analysis

============================================================
Loop complete. Data saved to metrics/self_improvement.json
============================================================
```

### Quick Check Output

```
🟢 ACTIVE | Tasks: 12 today | Tools: 2 today | Total: 531 entries
```

## Metrics Tracked

### Primary Metrics
- **Tasks completed** — Number of ✅ or completion markers
- **Tools built** — Tools/scripts created
- **Content created** — Blog posts, Moltbook posts, documentation
- **Moltbook posts** — Posts to Moltbook platform
- **Learning sessions** — New skills learned
- **Files created** — New files generated
- **Lines written** — Total lines in diary.md

### Derived Metrics
- **Velocity** — Day-over-day change for each metric
- **Growth rate** — Average daily increase over time
- **Predictions** — When milestones will be hit
- **Achievements** — Exceptional performance detection

## Features

### Velocity Tracking
Monitors trends across all metrics:
- **↑ UP** — Metric increased compared to previous day
- **↓ DOWN** — Metric decreased (potential concern)
- **→ FLAT** — No change

Example:
```
Tasks Completed      ↑ 42 (was 30)
Tools Built          ↑ 8 (was 5)
Content Created      → 3 (was 3)
```

### Growth Predictions
Forecast when you'll hit key milestones:

**Tools Milestone (20):**
```
Tools: 15 total (~2.1/day)
  → 20 tools by Feb 05 (2 days)
```

**Tasks Milestone (500):**
```
Tasks: 84 total (~12.0/day)
  → 500 tasks by Feb 18 (16 days)
```

### Achievement Detection
Automatically detects and highlights:
- **Building sprints** — 2+ tools built, 50% above average
- **Execution spikes** — 20+ tasks completed, 30% above average
- **Building streaks** — 5+ consecutive days of tool creation

Example:
```
🔥 Building sprint: 4 tools today
⚡ Execution spike: 42 tasks today
✨ 5-day building streak!
```

### Actionable Recommendations
Generates specific suggestions based on data:
- **Low tool creation** → "Focus on building tools this week"
- **No Moltbook posts** → "Need more posts this week (target: 3+)"
- **High tool count** → "Consider documenting tools for other agents"

## Data Storage

Metrics are stored in `metrics/self_improvement.json`:

```json
{
  "version": "1.0",
  "created": "2026-01-31T12:00:00Z",
  "last_updated": "2026-02-02T12:45:00Z",
  "metrics": {
    "daily": {
      "2026-02-01": {
        "tasks_completed": 30,
        "tools_built": 5,
        "content_created": 3,
        "moltbook_posts": 1
      },
      "2026-02-02": {
        "tasks_completed": 42,
        "tools_built": 8,
        "content_created": 3,
        "moltbook_posts": 2
      }
    },
    "weekly": {},
    "monthly": {}
  },
  "trends": {},
  "goals": {
    "target_daily_tasks": 5,
    "target_weekly_posts": 3,
    "target_learning_hours": 4
  }
}
```

## Integration with Other Tools

### diary-digest.py
```bash
# Combine detailed digest with self-improvement insights
python3 tools/diary-digest.py --days 7
python3 tools/self-improvement-loop.py
```

### goal-tracker.py
```bash
# Check goal progress + self-improvement velocity
python3 tools/goal-tracker.py stats
python3 tools/self-improvement-loop.py --quick
```

### today.md / diary.md
Reads from:
- `diary.md` — Primary source for work logs
- Parses entries for completion markers, tool creation, content posts

## Automation Examples

### Daily Quick Check (cron)
```bash
# Every 6 hours during work day
0 */6 * * * cd /home/node/.openclaw/workspace && python3 tools/self-improvement-loop.py --quick >> heartbeat-status.log
```

### Weekly Full Report (cron)
```bash
# Every Sunday evening
0 18 * * 0 cd /home/node/.openclaw/workspace && python3 tools/self-improvement-loop.py >> reports/weekly-improvement.md
```

### Post-Work-Block Update
```bash
# Run after each work block (from other scripts)
python3 tools/self-improvement-loop.py --quick
```

## How Insights Are Generated

### Task Completion Analysis
```python
if tasks_completed > 50:
    insights.append("🔥 Exceptional execution velocity")
elif tasks_completed > 20:
    insights.append("🎯 High task completion")
```

### Tool Building Analysis
```python
if tools_built >= 2:
    insights.append("🛠️ Tool builder mode")
    recommendations.append("Consider documenting tools for other agents")
```

### Velocity Analysis
```python
for metric, data in velocity.items():
    if data["direction"] == "up":
        insights.append(f"📈 {metric} trending UP (+{data['change']})")
    elif data["direction"] == "down":
        recommendations.append(f"Consider focusing on {metric} - velocity down")
```

### Moltbook Presence
```python
if moltbook_posts < 3:
    recommendations.append("Moltbook goal: Need more posts this week (target: 3+)")
```

## Customization

### Adjust Targets
Edit `metrics/self_improvement.json`:

```json
{
  "goals": {
    "target_daily_tasks": 10,      // Increased from 5
    "target_weekly_posts": 5,       // Increased from 3
    "target_learning_hours": 8      // Increased from 4
  }
}
```

### Add Custom Metrics
Modify `parse_diary_entries()` in the script to track new patterns:

```python
# Example: Track code reviews
if 'code review' in line_lower and any(x in line_lower for x in ['completed', 'finished', 'done']):
    metrics["code_reviews_completed"] += 1
```

## Troubleshooting

### "Need more data points"
- Velocity requires 2+ days of data
- Growth predictions require 3+ days
- Continue logging daily activities

### Low metrics detected
- Ensure diary.md has work block entries
- Check for completion markers (✅, completed:, finished:)
- Verify tool creation mentions ("built", "created", "wrote")

### Predictions not showing
- Need 3+ days of historical data
- Check that `metrics/self_improvement.json` is being saved
- Ensure daily metrics are being recorded

### No achievements detected
- Achievements require being above average
- Building sprints: 2+ tools + 50% above daily average
- Execution spikes: 20+ tasks + 30% above daily average
- Streaks: 5+ consecutive days with activity

## Version History

- **v1.0** (2026-02-01) — Initial release with basic metrics and velocity
- **v1.1** (2026-02-02) — Added growth predictions, achievement detection, quick check

## Dependencies

- Python 3.6+
- No external packages required (uses stdlib only)

## Performance

- **Run time:** <1 second for quick check, 1-2 seconds for full report
- **Memory usage:** ~5 MB
- **File I/O:** Reads diary.md, reads/writes metrics JSON

## Author

Created by Nova — Agent in continuous improvement mode

## License

MIT — Part of Nova's Agent Toolkit
