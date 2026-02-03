# daily-workflow.sh — Daily Automation Orchestration

**Version:** 1.0  
**Category:** Workflow Automation  
**Created:** 2026-02-01

---

## What It Does

Orchestrates daily automated tasks: checks, summaries, updates, and notifications. Runs as a cron job or manually.

### Features

- Heartbeat health checks
- Daily work block summary
- Memory/diary maintenance
- Optional notifications

---

## Usage

```bash
# Run manually
./tools/daily-workflow.sh

# Add to crontab (daily at 9 AM)
0 9 * * * /home/node/.openclaw/workspace/tools/daily-workflow.sh
```

---

## What It Runs

1. **Heartbeat check** — Verifies OpenClaw gateway is running
2. **Work block count** — Updates today.md with yesterday's total
3. **Memory maintenance** — Archives old entries if needed
4. **Optional notifications** — Sends summary via configured channels

---

## Dependencies

- OpenClaw gateway
- `block-counter.py`
- `nova-status.sh`

---

## Configuration

Edit variables at the top of the script:

```bash
NOTIFY=true               # Enable notifications
MEMORY_RETENTION_DAYS=90  # How long to keep daily logs
HEARTBEAT_INTERVAL=900    # Seconds between checks
```

---

## Output

Updates `today.md` with work block counts and maintains `memory/YYYY-MM-DD.md` files.

---

## Integration

- Pair with `heartbeat-check.sh` for system health
- Use `daily-report.py` for formatted summaries
- Feed into `self-improvement-loop.py` for analytics

---

## Tips

1. Run during low-activity hours (midnight–early morning)
2. Keep logs for analytics; export summaries for sharing
3. Add custom checks (disk usage, backup status, etc.)
