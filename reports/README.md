# 📊 Nova's Reports Dashboard

This directory contains automated reports and visualizations generated from Nova's activity logs.

## Available Reports

### 📸 Daily Snapshot (`daily-snapshot.md`)
**Auto-generated at:** Every work block  
**What it shows:**
- Goals progress (completed/total with percentage)
- Today's activity metrics (diary entries, tools built)
- Heartbeat statistics (files logged, total entries)
- Current blockers from today.md

**How to use:** Run `./tools/daily-snapshot.py` for fresh data anytime.

---

### ❤️ Heartbeat Dashboard (`heartbeat-dashboard.html`)
**What it shows:**
- **Lifetime Heartbeats:** Total count of all heartbeat events
- **Days Alive:** How long Nova has been operational
- **Avg per Day:** Heartbeat rate metric
- **Activity Heatmap:** Visual calendar showing activity intensity by day

**How to read the heatmap:**
- Each cell = one day
- Darker green = more activity (more heartbeats logged)
- White/gray = no activity
- Hover for exact counts

---

### 📈 Pattern Analysis (`patterns-2026-02-01.md`)
**What it shows:**
- **Peak Activity Hours:** When Nova is most productive
- **Top Working Directories:** Where Nova spends time
- **Activity Streaks:** Longest consecutive active periods
- **Anomalies:** Unusual patterns detected in logs

**How to use:** Review weekly to identify optimization opportunities.

---

### 🎯 Goal Tracking (`goals/goal-status-*.md`)
**What it shows:**
- Weekly goal progress with completion percentages
- Historical trends across weeks
- Blockers and impediments tracked over time

---

## For Arthur

**Quick status check:**
```bash
# Latest snapshot
cat reports/daily-snapshot.md

# Open visual dashboard
open reports/heartbeat-dashboard.html
```

**All reports are auto-generated.** No manual updates needed.

---
*Last updated: 2026-02-01*
