# blocker-dashboard.py

One-command view of all blockers with ROI ranking.

## Usage

```bash
# Show blocker dashboard
python3 tools/blocker-dashboard.py

# Show unblocked/ready actions
python3 tools/blocker-dashboard.py ready
```

## Output

```
=================================================================
🔒 BLOCKER DASHBOARD
=================================================================

📊 SUMMARY
-----------------------------------------------------------------
   Blockers: 2
   Total value blocked: $175K
   Time to unblock: 6 minutes
   Average ROI: $29K/min

🎯 BY PRIORITY (ROI/min)
-----------------------------------------------------------------

1. Code4rena Bounties
   Value: $50K | ROI: $50K/min
   Blocker: Browser automation blocked
   Action: Gateway restart required
   Owner: Arthur | Time: 1 min

2. Grant Submissions
   Value: $125K | ROI: $25K/min
   Blocker: GitHub repo push needed
   Action: gh auth login + git push
   Owner: Arthur | Time: 5 min

=================================================================
⚡ EXECUTE TOP BLOCKER FIRST
=================================================================
```

## Priority Logic

Blockers sorted by ROI/min:
1. Highest value per minute = top priority
2. Execute in order until all unblocked
3. Then switch to `execution-gap-closer.py`

## Related Tools

- `execution-gap-closer.py` — Actions for unblocked leads
- `daily-revenue-report.py` — Full pipeline status
- `pipeline-alerts.py` — Automated monitoring
