# progress-dashboard.sh — Visual Progress Overview

**Version:** 1.0  
**Category:** Analytics / Dashboard  
**Created:** 2026-02-01

---

## What It Does

Displays a terminal-based dashboard of work progress: goals, metrics, streaks, and recent activity.

### Features

- Real-time work block count
- Goal completion percentage
- Streak status
- Recent diary entries
- Velocity metrics

---

## Usage

```bash
# Display dashboard
./tools/progress-dashboard.sh

# Auto-refresh every 10 seconds
watch -n 10 ./tools/progress-dashboard.sh

# Export as text file
./tools/progress-dashboard.sh > reports/dashboard-$(date +%Y%m%d).txt
```

---

## What It Shows

```
═══════════════════════════════════════════════════════════
  NOVA PROGRESS DASHBOARD — 2026-02-02 20:45 UTC
═══════════════════════════════════════════════════════════

📊 WORK BLOCKS
  Total: 736
  Today: 198
  Velocity: 38 blocks/hour

🎯 GOALS
  Week 2: 9/20 complete (45%)
  Active: 24 tasks remaining

🔥 STREAK
  Status: ALIVE ✅
  Days: 7

📝 RECENT ACTIVITY
  • Tool documentation: 3 scripts documented
  • Outreach: 5 messages ready
  • Moltbook: Services offer drafted

═══════════════════════════════════════════════════════════
```

---

## Dependencies

- `block-counter.py` — Work block statistics
- `goal-tracker.py` — Goal completion status
- `diary.md` — Recent activity
- Standard Unix tools (`date`, `grep`, `wc`)

---

## Configuration

Edit variables at the top:

```bash
DASHBOARD_REFRESH=10        # Seconds between auto-refresh
SHOW_LAST_N_ENTRIES=5       # Number of recent entries to show
STREAK_THRESHOLD_DAYS=1     # Minimum days for streak
```

---

## Integration

- Pair with `heartbeat-viz.py` for visual analytics
- Use `daily-report.py` for detailed summaries
- Schedule with cron for automated snapshots

---

## Tips

1. Run in a dedicated terminal window for always-on visibility
2. Use with `watch` for auto-refresh during work sessions
3. Export daily for historical tracking
4. Customize display to show what matters most to you
