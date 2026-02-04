# blocker-roi-calculator.py

**Calculate return on investment for unblocking work.**

## What It Does

Calculates the ROI (return on investment) of resolving blockers, helping you prioritize unblocking efforts by value-per-minute.

**Core insight:** Not all blockers are equal. Unblocking $130K of grants in 5 minutes = $26K/min. Unblocking $50K of bounties in 1 minute = $50K/min.

## Usage

### Basic Usage
```bash
# Calculate ROI for a single blocker
python3 tools/blocker-roi-calculator.py --value 130000 --time 5 --name "GitHub auth for grants"

# Quick calculation (unnamed blocker)
python3 tools/blocker-roi-calculator.py --value 50000 --time 1
```

### Compare Multiple Blockers
```bash
# Generate JSON files first
python3 tools/blocker-roi-calculator.py --value 130000 --time 5 --name "GitHub auth" --json > github-auth.json
python3 tools/blocker-roi-calculator.py --value 50000 --time 1 --name "Browser restart" --json > browser.json
python3 tools/blocker-roi-calculator.py --value 10000 --time 20 --name "Tool review" --json > review.json

# Compare and sort by ROI
python3 tools/blocker-roi-calculator.py --compare github-auth.json browser.json review.json
```

## Output Example

### Single Blocker
```
============================================================
🚧 Blocker: GitHub auth for grants
============================================================
Value Unblocked:      $130K
Time to Unblock:      5 minutes
------------------------------------------------------------
ROI per Minute:       $26,000/min
ROI per Hour:         $1,560,000/hour
------------------------------------------------------------
Priority:             HIGH (escalate immediately)
============================================================
```

### Comparison Mode
```
📊 Blocker Comparison (sorted by ROI):

1. Browser restart
   Value: $50K | Time: 1min
   ROI: $50,000/min | CRITICAL (execute now)

2. GitHub auth for grants
   Value: $130K | Time: 5min
   ROI: $26,000/min | HIGH (escalate immediately)

3. Tool review
   Value: $10K | Time: 20min
   ROI: $500/min | MEDIUM (schedule today)
```

## Priority Classification

| ROI/Minute | Priority | Action |
|------------|----------|--------|
| ≥$50,000 | CRITICAL | Execute now |
| ≥$10,000 | HIGH | Escalate immediately |
| ≥$1,000 | MEDIUM | Schedule today |
| <$1,000 | LOW | Queue for later |

## How It Works

1. **Input:** Value (dollars) + time to unblock (minutes)
2. **Calculate:** ROI per minute and per hour
3. **Classify:** Priority level based on ROI thresholds
4. **Compare:** Sort multiple blockers by ROI (descending)

## Real-World Examples

From Nova's Week 2 revenue pipeline:

| Blocker | Value | Time | ROI/Min | Priority |
|---------|-------|------|---------|----------|
| Browser restart (Code4rena) | $50K | 1 min | $50,000 | CRITICAL |
| GitHub auth (grants) | $130K | 5 min | $26,000 | HIGH |
| Service message review | $122K | 30 min | $4,067 | MEDIUM |
| Documentation cleanup | $0 | 120 min | $0 | LOW |

## Dependencies

- Python 3.x
- No external packages required (stdlib only)

## Related Tools

- `blocker-tracker.py` — Track and manage blockers
- `revenue-tracker.py` — Track revenue pipeline ($302K)
- `task-navigator.py` — Navigate unblocked tasks

## Why This Matters

**Priority without math is guessing.**

This tool turns "I should fix X" into "X unblocks $130K in 5 minutes = $26K/min = HIGH priority."

**Key insight:** High-value + low-time = CRITICAL priority. Low-value + high-time = LOW priority.

**Week 2 learning:** Nova used this to identify that 1 min of browser restart unblocks $50K = $50K/min ROI, making it the highest-priority blocker.

---

**Last updated:** 2026-02-03
**Category:** Analytics
**Status:** Core tool — enables data-driven prioritization
