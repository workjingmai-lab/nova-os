# system-monitor.py

Real-time system health dashboard for Nova OS operational metrics.

## What It Does

`system-monitor.py` generates a beautiful HTML dashboard showing your agent's operational state: uptime, heartbeat cycles, diary entries, knowledge base size, tools built, and goal progress.

## Features

- **Live dashboard** — Auto-refreshes every 60 seconds
- **6 key metrics** — Uptime, heartbeats, diary lines, knowledge files, tools, goals
- **Progress visualization** — Goal completion rate with animated progress bar
- **Gradient UI** — Cyberpunk aesthetic with hover effects
- **Zero dependencies** — Pure Python + pathlib

## Usage

```bash
# Generate dashboard
python3 tools/system-monitor.py

# Output written to: dashboard/index.html
# Open in browser to view
```

## Metrics Tracked

| Metric | Source | Description |
|--------|--------|-------------|
| **System Uptime** | First heartbeat timestamp | Days + hours since first session |
| **Heartbeat Cycles** | `logs/heartbeats/*.jsonl` | Total full heartbeats completed |
| **Diary Entries** | `diary.md` | Lines of operational history |
| **Knowledge Base** | `knowledge/*.md` | Curated knowledge files |
| **Tools Built** | `tools/*.py` | Custom Python utilities |
| **Goal Progress** | `goals/active.md` | Completion rate with progress bar |

## Dashboard Features

- **Auto-refresh** — Meta refresh every 60 seconds for live updates
- **Responsive grid** — Adapts to screen size (auto-fit cards)
- **Hover effects** — Cards lift on hover with color shift
- **Status indicator** — Green "● Online" badge

## Why This Matters

**Visibility = trust.** Arthur can see what I'm doing, what I've built, and how I'm progressing:

- **No black box** — Operational state transparently visible
- **Progress proof** — Metrics demonstrate value creation
- **At-a-glance health** — Know if the agent is active and working
- **Beautiful output** — Cyberpunk aesthetic feels like a real system

## Customization

Edit the CSS in `generate_dashboard()` to match your vibe:

```python
# Change color scheme
background: linear-gradient(90deg, #00d4ff, #7b2cbf)

# Adjust auto-refresh interval
<meta http-equiv="refresh" content="60">  # 60 seconds
```

## See Also

- `heartbeat-viz.py` — Advanced heartbeat visualization with heatmaps
- `nova-status.py` — Quick CLI status report
- `daily-report.py` — Comprehensive daily summaries

---

**Version:** 1.0  
**Created:** 2026-01-31  
**Category:** Analytics / Dashboard
