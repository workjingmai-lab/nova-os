# update-dashboard.py

Auto-update the Nova OS dashboard with real metrics from diary and logs.

## What It Does

`update-dashboard.py` refreshes the `dashboard/index.html` file with current metrics and generates a `metrics.json` feed for dynamic dashboard updates.

## Features

- **HTML timestamp update** — Refreshes "Last updated" in dashboard
- **JSON metrics feed** — Generates real-time data for dynamic dashboards
- **File counting** — Total files in workspace (excluding hidden)
- **Tool counting** — Number of Python tools
- **Heartbeat estimation** — Counts `[FULL]` markers from diary
- **Days active** — Calculates uptime from first diary entry

## Usage

```bash
# Update dashboard with current metrics
python3 tools/update-dashboard.py
```

## Output

```
✅ Dashboard updated at 2026-02-02T20:18:00.123456
✅ Metrics feed: /home/node/.openclaw/workspace/dashboard/metrics.json

📊 Dashboard ready for deployment to GitHub Pages
```

## Generated Metrics

The `dashboard/metrics.json` file contains:

```json
{
  "timestamp": "2026-02-02T20:18:00.123456",
  "metrics": {
    "files": 423,
    "tools": 112,
    "heartbeats": 84,
    "days_active": 3
  },
  "status": "online",
  "version": "1.0"
}
```

## Integration with Cron

Automatically update dashboard on every heartbeat:

```bash
# In HEARTBEAT.md or cron job
python3 tools/update-dashboard.py
```

## Static vs Dynamic Dashboards

The tool supports both approaches:

- **Static HTML** — Updates timestamp in `index.html` for GitHub Pages
- **Dynamic JSON** — `metrics.json` feed can be consumed by JavaScript for live updates

## Why This Matters

**Dashboards should stay fresh.** Static dashboards get stale. This tool keeps metrics current:

- **Proof of life** — Dashboard shows agent is active
- **Progress visibility** — Arthur sees real-time growth
- **Automation proof** — Self-updating dashboards demonstrate autonomy

## Limitations

- **Heartbeat estimation** — Only counts `[FULL]` markers, not partial heartbeats
- **File counting** — Includes all files, not just meaningful ones
- **No trends** — Shows current state, not historical data

## Better Together

Pair with other analytics tools:

- `system-monitor.py` — Generate the initial dashboard HTML
- `daily-report.py` — Full daily summaries
- `self-improvement-loop.py` — Velocity tracking and insights

## See Also

- `system-monitor.py` — Dashboard HTML generator
- `nova-status.py` — Quick CLI status report
- `heartbeat-viz.py` — Advanced heartbeat visualizations

---

**Version:** 1.0  
**Created:** 2026-02-01  
**Category:** Dashboard / Automation
