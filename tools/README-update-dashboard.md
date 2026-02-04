# update-dashboard.py

Dashboard auto-updater for Nova OS. Updates static HTML dashboard with live metrics from diary/logs.

## What It Does

- Counts workspace files, tools, heartbeats, days active
- Updates dashboard HTML with current timestamp
- Generates JSON feed for dynamic dashboards
- Prepares dashboard for GitHub Pages deployment

## Usage

```bash
python3 tools/update-dashboard.py
```

## Dashboard Location

- HTML: `dashboard/index.html`
- JSON feed: `dashboard/metrics.json`

## Metrics Tracked

- **Files:** Total files in workspace (excludes hidden dirs)
- **Tools:** Python scripts in `tools/`
- **Heartbeats:** FULL heartbeat markers in diary.md
- **Days Active:** Days since first diary entry

## Deployment

Updates are static. For live metrics, serve `metrics.json` via simple HTTP server or deploy to GitHub Pages with periodic updates.

## Why This Matters

Visibility = motivation. Dashboard shows progress at a glance.

---

**Work Block:** #960
**Created:** 2026-02-03T06:05Z
