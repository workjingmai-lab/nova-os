# system-monitor.py

**Real-time system health dashboard for Nova OS.**

Generates a beautiful HTML dashboard showing operational metrics, uptime, and progress.

## What It Does

- Scans workspace for key metrics (heartbeats, diary lines, tools, goals)
- Calculates system uptime from first heartbeat
- Generates auto-refreshing HTML dashboard (60s refresh)
- Displays goal completion rate with progress bar
- Creates visual health overview with gradient styling

## Usage

```bash
python3 tools/system-monitor.py
```

Output: `dashboard/index.html`

## Dashboard Metrics

- **System Uptime:** Days + hours since first heartbeat
- **Heartbeat Cycles:** Total full heartbeats completed
- **Diary Entries:** Lines of operational history
- **Knowledge Base:** Curated knowledge files count
- **Tools Built:** Custom Python utilities count
- **Goal Progress:** Completion percentage with progress bar

## Output

Auto-refreshing HTML dashboard at `dashboard/index.html` with:
- Dark gradient theme (#0a0a0f → #1a1a2e)
- Responsive grid layout
- Hover effects on cards
- 60-second auto-refresh
- Color-coded status indicators

## Use Cases

- **Health monitoring:** Quick visual check of system status
- **Progress tracking:** See goals completion at a glance
- **Uptime tracking:** Monitor continuous operation
- **Workspace audit:** Verify file counts and growth

## Why It Matters

**Visibility enables optimization.**

This dashboard creates a single source of truth for Nova OS health. Instead of checking multiple files, you get a real-time overview in one glance.

---

**Created:** 2026-02-02
**Status:** Active ✅
**Output:** `dashboard/index.html`
**Refresh:** 60 seconds
