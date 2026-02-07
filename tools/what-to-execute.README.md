# what-to-execute.py

**Arthur's Action List — What to execute next.**

Shows blocked items (technical fixes) and ready items (revenue awaiting execution).

## Usage

```bash
python3 tools/what-to-execute.py
```

## Output

- **Blockers:** Technical items Arthur can fix (e.g., gateway restart)
- **Ready items:** Revenue awaiting execution (services, grants)
- **Time + ROI:** How long each action takes, value per minute

## Example

```
🎯 WHAT TO EXECUTE — Arthur's Action List
============================================================

🚧 BLOCKERS (Technical — Arthur fixes these)

• Code4rena Setup
  Blocker: browser
  Value: $50,000
  Fix: Gateway restart (openclaw gateway restart)
  Time: 1 min
  ROI: $50,000/min

✅ READY TO EXECUTE (Revenue waiting for Arthur)

📨 Services: 5 leads ready, $700,000 total
   Execute: bash tools/send-everything.sh
   Time: ~20 min
   ROI: $35,000/min

📝 Grants: 4 ready, $125,000 total
   Execute: python3 tools/grant-submit-helper.py
   Blocker: GitHub CLI auth (run: gh auth login)
   Time: 5 min (auth) + 15 min (submit)
   ROI: $6,250/min

============================================================
TOTAL BLOCKER VALUE: $175,000
TOTAL READY VALUE: $825,000
TOTAL TIME: ~26 min (1 + 5 + 20)
TOTAL ROI: $33,654/min
```

## Why This Tool

**Problem:** Pipeline has $825K ready, but execution gap = 99.3%. Arthur needs clarity on WHAT to execute.

**Solution:** One-page summary showing:
1. What's blocked (technical fixes)
2. What's ready (revenue waiting)
3. Time + ROI for each action

**Created:** 2026-02-07 (Work block 3218)
