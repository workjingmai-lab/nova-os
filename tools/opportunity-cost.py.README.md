# opportunity-cost.py

Calculate the revenue cost of inaction. Shows how much money is being "lost" per hour/day of execution delays.

## Usage

```bash
python3 tools/opportunity-cost.py
```

Uses defaults ($754.5K ready, 99.3% gap) or reads from `data/revenue-pipeline.json`.

## Output Example

```
💰 OPPORTUNITY COST OF WAITING
Ready to execute:    $754,500
Execution gap:       99.3%
Expected revenue:    $75,450

⏰ COST OF DELAY:
  1 hour               $     105
  4 hours (half day)   $     419
  1 day                $   2,515
  1 week               $  17,605
  1 month              $  75,450
```

## Purpose

Communicate urgency of execution blockers. Every hour of delay = $105 in expected value not captured.

## Assumptions

- 10% conversion rate on outreach
- 30-day average close time
- Conservative estimates (actual may be higher)
