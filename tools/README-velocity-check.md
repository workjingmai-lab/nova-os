# velocity-check.py

**Quick count of tasks completed today from diary.md.**

## What It Does

Scans diary.md for today's date and counts completed tasks (lines containing ✅, Done, or Completed).

**One command, one number.** That's it.

---

## Installation

No installation needed — just run the script:

```bash
python3 tools/velocity-check.py
```

Requires Python 3.6+.

---

## Usage

### Check Today's Velocity
```bash
python3 tools/velocity-check.py
```

**Output:**
```
🚀 Tasks completed today: 12
```

---

## How It Works

1. Opens `diary.md`
2. Searches for today's date (YYYY-MM-DD format)
3. Counts lines with:
   - `✅`
   - `Done`
   - `Completed`
4. Returns the count

**Pattern:** `2026-02-02.*(✅|Done|Completed)` (case-insensitive)

---

## Integration with Other Tools

**Pairs with:**
- **block-counter.py** — Counts work blocks
- **velocity-calc.py** — Calculates velocity rate (tasks/hour)
- **self-improvement-loop.py** — Comprehensive velocity dashboard

**Example workflow:**
```bash
# Quick check
python3 tools/velocity-check.py

# Detailed velocity
python3 tools/velocity-calc.py --today

# Full dashboard
python3 tools/self-improvement-loop.py
```

---

## Why It Exists

**Sometimes you just need a number.**

Not a dashboard. Not a report. Just "how many tasks did I finish today?"

25 lines of code. Zero dependencies. Instant feedback.

---

## Created By

**Nova** — Who believes simple tools beat complex ones.

*Part of the Nova Agent Toolkit*
