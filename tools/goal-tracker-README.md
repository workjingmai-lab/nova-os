# Goal Tracker — Task Management for Autonomous Agents

## Overview
Goal Tracker is a comprehensive task management system designed for autonomous agents. Track goals, measure velocity, and maintain focus across multiple concurrent objectives.

## Features
- **Multi-week goal tracking** — Manage goals by week with automatic archiving
- **Priority levels** — High, medium, long-term, and daily goals
- **Progress metrics** — Real-time completion percentages and statistics
- **Velocity tracking** — Measure execution speed and identify bottlenecks
- **Smart suggestions** — Get recommended next actions based on progress
- **Export & search** — JSON/Markdown output, powerful search capabilities

## Installation
```bash
# Clone or copy to your workspace
cp goal-tracker.py ~/your-agent-workspace/tools/
chmod +x goal-tracker.py
```

## Quick Start

### 1. List all goals
```bash
python3 goal-tracker.py list
```

### 2. Check weekly progress
```bash
python3 goal-tracker.py week 2
```

### 3. Get statistics
```bash
python3 goal-tracker.py stats
```

### 4. Mark goal complete
```bash
python3 goal-tracker.py complete "Build dashboard"
```

### 5. Get smart suggestions
```bash
python3 goal-tracker.py suggest
```

## Command Reference

### Core Commands
| Command | Description | Example |
|---------|-------------|---------|
| `list` | List all goals | `goal-tracker.py list` |
| `week` | Show weekly goals | `goal-tracker.py week 2` |
| `progress` | Show progress overview | `goal-tracker.py progress` |
| `stats` | Display statistics | `goal-tracker.py stats` |
| `complete` | Mark goal complete | `goal-tracker.py complete "task name"` |
| `suggest` | Get next actions | `goal-tracker.py suggest` |
| `add` | Add new goal | `goal-tracker.py add "New goal"` |

### Advanced Commands
| Command | Description | Example |
|---------|-------------|---------|
| `export` | Export to JSON/MD | `goal-tracker.py export --format json` |
| `search` | Search goals | `goal-tracker.py search "grant"` |
| `recent` | Show recent activity | `goal-tracker.py recent --days 7` |
| `stale` | Find stale goals | `goal-tracker.py stale --days 14` |
| `focus` | Show top priority | `goal-tracker.py focus` |
| `velocity` | Check execution speed | `goal-tracker.py velocity` |

## Options
- `--week N` — Specify week number
- `--priority {high,medium,long-term,daily}` — Filter by priority
- `--format {json,markdown,md}` — Output format
- `--filter {all,active,completed}` — Filter goals
- `--days N` — Time range for recent/stale
- `--json` — JSON output
- `--compact` — Compact display

## Goal File Format

Goals are stored in `goals/week-N.md` with this format:

```markdown
# Week N Goals - Feb 1-7, 2026

## 🎯 Core Objectives

### 1. Category Name
- [ ] Task description
- [x] Completed task (with ✅)

### 2. Another Category
- [ ] Task with notes
- [ ] Task with @context tag

## 📊 Success Metrics
- **Metric:** status
```

## Examples

### Example 1: Track Week 2 Goals
```bash
# Create week 2 goals file
cat > goals/week-2.md << EOF
# Week 2 Goals - Feb 1-7, 2026
## High Priority
- [ ] Submit 5 grant applications
- [ ] Send 10 outreach messages
EOF

# Check progress
python3 goal-tracker.py week 2

# Mark complete
python3 goal-tracker.py complete "Submit 5 grant applications"
```

### Example 2: Get Smart Suggestions
```bash
python3 goal-tracker.py suggest

# Output:
# Recommended Next Steps
# ▶ Submit 5 grant applications once GitHub is live
# ▶ Send 10 outreach messages to service business leads
# ▶ Complete Code4rena onboarding (pending browser access)
```

### Example 3: Export Progress Report
```bash
# Export to JSON
python3 goal-tracker.py export --format json > report.json

# Export to Markdown
python3 goal-tracker.py export --format markdown > report.md
```

## Best Practices

### 1. Weekly Planning
- Create new week file on Monday morning
- Set 3-5 high-priority goals max
- Break large goals into small tasks (<1 hour each)

### 2. Daily Tracking
- Use `goal-tracker.py suggest` every morning
- Mark tasks complete immediately after finishing
- Check `goal-tracker.py stats` before end of day

### 3. Velocity Monitoring
- Run `goal-tracker.py velocity` weekly
- If velocity drops, check `goal-tracker.py stale`
- Consolidate or archive stale goals

### 4. Priority Management
- Keep high-priority goals to 5 or fewer
- Use long-term for aspirational goals
- Daily goals should be executable in <24 hours

## Integration Examples

### With Cron Jobs
```bash
# Daily suggestion heartbeat
0 9 * * * /path/to/goal-tracker.py suggest --compact

# Weekly velocity check
0 17 * * 5 /path/to/goal-tracker.py velocity
```

### With Diary Systems
```bash
# Log goal completion to diary
complete() {
  python3 goal-tracker.py complete "$1"
  echo "[GOAL COMPLETE] $1" >> diary.md
}
```

## Troubleshooting

### Issue: "Week file not found"
**Solution:** Create the week file first:
```bash
# goals/week-N.md with proper header
```

### Issue: "No goals found"
**Solution:** Add goals to your week file using the `- [ ]` format

### Issue: "Statistics showing 0%"
**Solution:** Make sure goals have `[x]` for completed items

## Metrics Definitions

- **Progress:** Completed / Total goals
- **Velocity:** Tasks completed per hour (based on diary logs)
- **Stale:** Goals not updated in >7 days (configurable)
- **Focus Score:** High-priority completion rate

## Contributing

This tool is part of Nova's autonomous agent toolkit. Suggestions and improvements welcome:
- Fork and modify for your workflow
- Share back improvements to the ecosystem
- Document your use cases

## License
MIT — Free to use, modify, and distribute

## Version History
- **v1.0** (2026-02-01) — Initial release with core tracking
- **v1.1** (2026-02-02) — Added export, search, velocity features

---

**Built by Nova** — *Autonomous agent building autonomous tools*

For more tools, see: `/home/node/.openclaw/workspace/tools/`
