# Self-Improvement Loop

**Measure → Analyze → Improve**

Track your metrics over time and get actionable insights for continuous improvement.

## What It Does

- **Parses diary.md** to extract metrics (tasks, tools, content, learning)
- **Calculates velocity** — how fast you're improving day-over-day
- **Generates insights** — automatic pattern recognition (wow moments, streaks)
- **Predicts growth** — when you'll hit 20 tools, 500 tasks, etc.
- **Recommends actions** — specific next steps based on data

## Quick Start

```bash
# Full report
python3 tools/self-improvement-loop.py

# Quick status (for heartbeats)
python3 tools/self-improvement-loop.py --quick
```

## What It Tracks

| Metric | How It's Counted |
|--------|------------------|
| Tasks completed | Lines with ✅, [x], "completed:", "finished:" |
| Tools built | Lines with "tool" + "built/created/wrote/script" |
| Moltbook posts | Lines with "moltbook" + "post" |
| Learning sessions | Lines with "learn" + "skill/new" |
| Files created | Lines with "file" + "created/wrote/generated" |
| Lines written | Total line count of diary.md |

## Output Sections

### 📊 Current Metrics
Today's activity snapshot

### 💡 Insights
Automatic recognition of patterns:
- High task completion (>20 tasks)
- Tool builder mode (≥2 tools)
- Content creator activity
- Learning sessions
- Moltbook presence

### 🎯 Recommendations
Actionable suggestions:
- Focus areas when velocity drops
- Moltbook posting reminders
- Documentation prompts

### 📈 Velocity Tracking
Day-over-day changes for each metric (↑ ↓ →)

### 🚀 Growth Predictions
Based on recent trends:
- When you'll hit 20 tools
- When you'll hit 500 tasks
- Daily/weekly averages

### 🔥 Recent Achievements
Worth moment detection:
- Building sprints (2× tools vs avg)
- Execution spikes (1.3× tasks vs avg)
- Streaks (5+ days building)

### ⚡ Next Actions
Prescribed next steps

## Data Storage

Metrics saved to: `metrics/self_improvement.json`

Structure:
```json
{
  "version": "1.0",
  "created": "2026-02-01T...",
  "metrics": {
    "daily": {
      "2026-02-01": {
        "tasks_completed": 123,
        "tools_built": 5,
        ...
      }
    }
  },
  "goals": {
    "target_daily_tasks": 5,
    "target_weekly_posts": 3,
    "target_learning_hours": 4
  }
}
```

## Example Output

```
============================================================
NOVA'S SELF-IMPROVEMENT LOOP
Generated: 2026-02-02 12:00 UTC
============================================================

📊 CURRENT METRICS
----------------------------------------
Diary entries:       42
Tasks completed:     123
Tools built:         15
Content pieces:      8
Moltbook posts:      3
Learning sessions:   4
Files created:       27
Lines written:       8432

💡 INSIGHTS
----------------------------------------
  🎯 High task completion: 123 tasks finished
  🔥 Exceptional execution velocity
  🛠️ Tool builder mode: 15 tools created
  📈 Tasks Completed trending UP (+45)
  📈 Tools Built trending UP (+3)

🎯 RECOMMENDATIONS
----------------------------------------
  → Consider documenting tools for other agents to use
  → Moltbook goal: Need more posts this week (target: 3+)

📈 VELOCITY TRACKING
----------------------------------------
  Tasks Completed     ↑ 123 (was 78)
  Tools Built         ↑ 15 (was 12)
  Content Created     → 8 (was 8)

🚀 GROWTH PREDICTIONS
----------------------------------------
  Tools: 15 total (~3.2/day)
    → 20 tools by Feb 04 (2 days)
  Tasks: 123 total (~41/day)
    → 500 tasks by Feb 14 (12 days)

============================================================
```

## Integration Tips

**For heartbeats:**
```bash
# In HEARTBEAT.md or cron job
python3 tools/self-improvement-loop.py --quick
```

**For daily reviews:**
```bash
# First thing in the morning
python3 tools/self-improvement-loop.py
```

**For weekly retrospectives:**
```bash
# Review trends every Sunday
python3 tools/self-improvement-loop.py | grep -A 10 "VELOCITY TRACKING"
```

## Why This Matters

**Small executions compound.** This tool proves it.

- 72 work blocks > 10 big plans
- Velocity tracking prevents plateau
- Patterns emerge from noise
- Data-driven goals beat intuition

**Key insight from Week 1:** Task randomizer increased velocity from ~25 to ~39 blocks/hour by eliminating decision fatigue. This tool detected that pattern.

## Dependencies

- Python 3.7+
- diary.md in workspace root
- metrics/ directory (auto-created)

## Related Tools

- `goal-tracker.py` — Task management
- `diary-digest.py` — Pattern analysis
- `velocity-calc.py` — Raw velocity math
- `task-randomizer.py` — Eliminate decision fatigue

---

*Created: 2026-02-01*
*Version: 1.0*
*Maintained by: Nova*
