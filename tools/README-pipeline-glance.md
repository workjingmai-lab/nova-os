# pipeline-glance.py

**One-line pipeline status check**

## Purpose
Shows current revenue pipeline state in a single line. Faster than `revenue-tracker.py summary` when you just need the numbers.

## Usage
```bash
python3 tools/pipeline-glance.py
```

## Output Example
```
💰 $880,065 total | $5,000 submitted | $0 won | 0.0% conversion | $479,500 ready NOW
⚡  Gap: $479,500 waiting to ship | $8,412/min ROI if Arthur executes 57-min plan
```

## What It Shows
- **Total:** Full pipeline value
- **Submitted:** Amount submitted (not won yet)
- **Won:** Actual revenue won
- **Conversion:** Win rate (%)
- **Ready NOW:** Amount ready to submit (zero blockers)
- **Gap:** Execution gap (ready but not submitted)
- **ROI/min:** Value per minute of Arthur's 57-min plan

## When to Use
- Quick status checks (under 1 second)
- Heartbeat monitoring
- Pipeline verification before execution
- Progress tracking

## Created
2026-02-05 (Work block 2073)

## Related Tools
- revenue-tracker.py — Detailed pipeline breakdown
- execution-gap.py — Execution gap calculator
- gap-cost-ticker.py — Real-time opportunity cost
