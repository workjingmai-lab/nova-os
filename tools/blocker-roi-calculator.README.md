# blocker-roi-calculator.py

**Purpose:** Prioritize unblocking work by value/time (Insight #17: "Blocker ROI = Priority")

## What It Does

Calculates and ranks blockers by ROI (value per minute). Helps prioritize which blockers to tackle first.

## Usage

```bash
# Show ranked blockers
python3 blocker-roi-calculator.py

# Add blocker
python3 blocker-roi-calculator.py --add "Browser fix" 2 50000

# Remove blocker
python3 blocker-roi-calculator.py --rm 0

# Clear all blockers
python3 blocker-roi-calculator.py --clear
```

## Output

```
🔓 BLOCKER ROI RANKING
======================================================================
#   Blocker                   Time   Value      ROI ($/min)
----------------------------------------------------------------------
0   Gateway Restart           1m     $50,000    $50,000
1   GitHub SSH Auth           5m     $130,000   $26,000
----------------------------------------------------------------------
TOTAL                         6m     $180,000   $30,000/min
```

## Data Storage

- `~/.openclaw/workspace/data/blockers.json` — Persistent blocker database
- Auto-creates on first run

## Insight Background

From MEMORY.md #17: "Blocker ROI = Priority" — Sort blockers by value/time, execute highest first. Gateway restart (1 min → $50K) > GitHub auth (5 min → $130K) = $30K/min average ROI.

## Created

2026-02-05 — Work block 1827
