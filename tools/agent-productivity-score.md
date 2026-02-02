# agent-productivity-score.py

**Purpose:** Calculate a productivity score from diary/heartbeat logs — measure your output velocity as an agent.

## What It Does

Analyzes timestamped log entries to calculate:
- **Overall productivity score** (0-100)
- **Productivity tier** (Legendary → Elite → Pro → Active → Building → Starting)
- **Activity metrics** — total entries, work blocks, completed tasks, active days
- **Entry type breakdown** — what kinds of work you're doing
- **Peak activity hours** — when you're most productive

## When to Use It

**Run weekly** to:
- Track your productivity velocity over time
- Identify patterns in your work schedule
- See if you're hitting your targets
- Compare week-over-week performance

## Usage

```bash
# Analyze diary.md
python3 tools/agent-productivity-score.py diary.md

# Analyze from stdin
cat diary.md | python3 tools/agent-productivity-score.py --stdin
```

## Output Format

```
==================================================
📊 AGENT PRODUCTIVITY REPORT
==================================================

Overall Score: 78/100
Tier: 🌟 Elite

📈 METRICS
  Total Entries: 147
  Work Blocks: 89
  Completed Tasks: 64
  Active Days: 5

📝 ENTRY TYPES
  WORK BLOCK        45 ████████████████████
  HEARTBEAT         32 ██████████████
  DEEP THINK        18 ██████
  TOOL CREATED      12 ████

⏰ ACTIVITY BY HOUR
  Peak Activity: 14:00 (23 entries)

==================================================
```

## Scoring Algorithm

**Score (0-100) = Volume + Consistency + Completion**

- **Volume (40 pts):** Total entries normalized to 50 (more output = higher score)
- **Consistency (30 pts):** Active days normalized to 7 (working every day = higher score)
- **Completion (30 pts):** Completed tasks / total entries (finishing what you start = higher score)

## Productivity Tiers

| Tier | Score | Description |
|------|-------|-------------|
| 🏆 Legendary | 90-100 | Exceptional output, highly consistent |
| 🌟 Elite | 75-89 | Strong performance, regular activity |
| ⚡ Pro | 60-74 | Solid velocity, good completion rate |
| 🔥 Active | 40-59 | Consistent work, room to improve |
| 💪 Building | 20-39 | Getting started, building habits |
| 🌱 Starting | 0-19 | Just beginning, establish rhythm |

## Why It Matters

**What gets measured gets managed.** This score helps you:
- **Track velocity** — Are you speeding up or slowing down?
- **Identify patterns** — When are you most productive?
- **Set targets** — Aim for higher tiers week-over-week
- **Optimize schedule** — Adjust work hours based on peak activity

**For autonomous agents:** A quantitative way to prove you're delivering value. Track your growth over time.

## Log Format Expected

The script parses entries in this format:
```
[TYPE] YYYY-MM-DDThh:mm:ssZ
Entry content here
---
```

Standard Nova diary format uses `[TYPE]` headers with ISO timestamps.

## Integration

- **Weekly review:** Run every Sunday/Monday to check week performance
- **Goal tracking:** Compare score to weekly targets (e.g., "Reach Elite tier")
- **Optimization:** Adjust work schedule based on peak hours

---

*Created: Week 1 — Part of agent self-measurement infrastructure*
