# pipeline-alerts.py

Monitor pipeline health and alert on actionable conditions.

## Usage

```bash
# Run all health checks
python3 tools/pipeline-alerts.py check

# Check specific conditions
python3 tools/pipeline-alerts.py stale       # Stale leads (>2 days)
python3 tools/pipeline-alerts.py followups   # Due follow-ups
python3 tools/pipeline-alerts.py rate-limit  # Moltbook cooldown
```

## Checks Performed

| Check | Trigger | Action |
|-------|---------|--------|
| Stale leads | Ready >2 days | Send messages or update status |
| Due follow-ups | Follow-up date reached | Execute follow-up sequence |
| Rate limit | Moltbook cooldown active | Wait or pivot to other tasks |
| Pipeline value | Services/grants status | Track ready vs submitted |

## Output Example

```
============================================================
🚨 PIPELINE ALERTS
============================================================

📋 STALE LEADS (ready >2 days)
----------------------------------------
⚠️  3 stale leads worth $127K
   • ETH Foundation: 3 days, $40K
   • Uniswap DevX: 4 days, $40K
   ... and 1 more

📅 DUE FOLLOW-UPS
----------------------------------------
✅ No follow-ups due

🐦 MOLTBOOK STATUS
----------------------------------------
✅ Ready to post (2 in queue)

💰 PIPELINE SUMMARY
----------------------------------------
   Services ready: $630K
   Grants submitted: $5K

============================================================
⚠️  3 ALERTS REQUIRE ATTENTION
============================================================
```

## Data Sources

- `data/conversion-log.json` — Lead status and follow-ups
- `data/revenue-pipeline.json` — Pipeline values
- `data/moltbook-queue.json` — Post queue status

## Automation

Add to cron for automated monitoring:
```bash
# Check every 15 minutes
*/15 * * * * cd /workspace && python3 tools/pipeline-alerts.py check
```

## Related Tools

- `daily-revenue-report.py` — Full revenue dashboard
- `execution-gap-closer.py` — Actionable send tasks
- `follow-up-reminder.py` — Follow-up scheduler
