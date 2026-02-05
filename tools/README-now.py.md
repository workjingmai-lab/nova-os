# now.py — Quick Status Dashboard

**One command to see everything.**

## What it does

Shows current status in 1 second:
- Work blocks today
- Pipeline total
- Execution gap
- Next actions

## Usage

```bash
python3 tools/now.py
```

## Output example

```
============================================================
 NOVA STATUS DASHBOARD
============================================================

📊 **Work blocks:** 1837 (612% of 300 target, +1537 surplus)
💰 Pipeline: $880,065 total
⚠️  Execution Gap: $435,000 ready, $0 submitted (100% gap)

🎯 NEXT ACTIONS:
   1. Gateway restart (1 min → $50K)
   2. GitHub auth (5 min → $130K)
   3. Send top 10 services (10 min → $305K)

📅 Timestamp: 2026-02-05 06:11Z
============================================================
```

## Why this exists

**The 30-second rule:** If you can't understand it in 30 seconds, it's too complex.

Arthur can run `python3 tools/now.py` and immediately know:
- How much work has been done
- How much pipeline exists
- What the execution gap is
- What to do next

No reading multiple files. No running multiple commands. One command = full context.

## Data sources

- **Work blocks:** today.md (parsed from header)
- **Pipeline:** data/revenue-pipeline.json (sum of all potentials)
- **Execution gap:** data/execution-gap.json (if exists)

## Integration

Add to your daily routine:
1. Run `now.py`
2. See what needs attention
3. Execute next action

Frictionless status checking = more frequent checking = better decisions.
