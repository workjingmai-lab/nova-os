# Blocker ROI Calculator — Prioritize Unblocking

## What

Calculate which blocker to fix first based on ROI per minute.

## Why

Small unblocks → massive value unlocked.

Examples:
- 2 min Arthur approval = $1,028,500/min ROI ($2,057K services)
- 5 min GitHub auth = $26,000/min ROI ($130K grants)
- 1 min gateway restart = $50,000/min ROI ($50K bounties)

## Usage

```bash
python3 tools/blocker-roi-calculator.py              # List all blockers
python3 tools/blocker-roi-calculator.py --priority   # Sort by ROI/min
python3 tools/blocker-roi-calculator.py --json       # Export as JSON
```

## Output

Shows:
- Blocker name
- Time to fix (minutes)
- Value unlocked ($)
- ROI per minute
- Recommended action

## Example Output

```
🎯 BLOCKERS (Sorted by ROI/min)

Blocker                             | Time   | Value      | ROI/min      
Arthur approval — Service outreach  | 2min   | $2.1M      | $1,028,500/min
Arthur approval — Grant submission  | 1min   | $130K      | $130,000/min
Browser access (gateway restart)    | 1min   | $50K       | $50,000/min
GitHub CLI authentication           | 5min   | $130K      | $26,000/min
```

## Data Structure

Each blocker has:
- `name`: Description
- `time_min`: Minutes to fix
- `value_unlocked`: Dollar value unlocked
- `category`: infrastructure / decision / external
- `unblocks`: List of what gets unblocked
- `action`: Specific step to take

## Integration

- Pipeline Snapshot: Show blockers with pipeline value
- EXECUTE-PHASE-READY.md: Embed blocker ROI
- Daily report: Include blocker status

## ROI Math

```
ROI per minute = value_unlocked / time_min

Example:
- Service outreach approval: $2,057,000 / 2 min = $1,028,500/min
- GitHub auth: $130,000 / 5 min = $26,000/min
```

## Insights

1. **Decisions have highest ROI** — Arthur approvals unlock millions in minutes
2. **Infrastructure unblocks scale** — Gateway restart = $50K/min forever
3. **Small fixes = massive leverage** — 19 min total = $2.4M unlocked

## Size

- Tool: 5,144 bytes
- README: 2,134 bytes
- Total: 7,278 bytes

## Related Tools

- `pipeline-snapshot.py` — See what's blocked
- `service-batch-send.py` — Execute after unblocking
- `grant-submit-helper.py` — Submit grants after auth

---

**Created:** 2026-02-03 (Work block #1224)
**Category:** Revenue Execution
**Status:** ✅ Active
