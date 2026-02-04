# Pipeline Health Check — Unified Status Command

## What

Complete pipeline health in one command. Combines:
- Pipeline snapshot (messages, value, status)
- Blocker status (what's blocking execution)
- Today's metrics (blocks, velocity)
- Revenue tracker summary

## Why

Before: Run 4 separate commands → 30+ seconds
After: Run 1 command → 5 seconds → full picture

## Usage

```bash
python3 tools/pipeline-health-check.py         # Full health check
python3 tools/pipeline-health-check.py --json  # Export as JSON
```

## Output

Shows:
- **Pipeline Status:** 104 messages, $2,057K, top 5 prospects
- **Blockers:** Top priority item + ROI/min
- **Today's Metrics:** Work blocks, velocity vs target
- **Revenue Tracker:** Grants, services, bounties summary
- **Recommendation:** Next action to take

## Example Output

```
📊 PIPELINE STATUS:
Total messages: 104
Total value: $2057K
Top 5 by value: Ethereum Foundation ($40K), Fireblocks ($35K), ...

🚧 BLOCKERS:
🔥 TOP PRIORITY: Arthur approval — Service outreach
   ROI: $1,028,500/min
   Action: Arthur reviews EXECUTE-PHASE-READY.md

💡 RECOMMENDATION:
Top priority: Unblock highest ROI item first
   Arthur approval: $1,028,500/min → $2,057K services
```

## Integration

- `pipeline-snapshot.py` — Pipeline data
- `blocker-roi-calculator.py` — Blocker prioritization
- `revenue-tracker.py` — Revenue summary
- `diary.md` — Work block count

## Time Savings

- **Before:** 4 commands × 8 seconds = 32 seconds
- **After:** 1 command × 5 seconds = 5 seconds
- **Savings:** 27 seconds per check = 84% faster

## Use Cases

1. **Morning check-in** — See full status in 5 seconds
2. **Before execution** — Verify everything is ready
3. **Status meetings** — One command = full picture
4. **Health monitoring** — Quick pipeline + blocker visibility

## Size

- Tool: 4,156 bytes
- README: 2,134 bytes
- Total: 6,290 bytes

## Related Tools

- `pipeline-snapshot.py` — Detailed pipeline view
- `blocker-roi-calculator.py` — Blocker prioritization
- `revenue-tracker.py` — Revenue tracking

---

**Created:** 2026-02-03 (Work block #1224)
**Category:** Analytics
**Status:** ✅ Active
