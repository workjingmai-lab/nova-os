# outreach-roi-calculator.py

**Calculate expected returns from service outreach.**

## Purpose

Predict outreach ROI based on historical conversion rates. Helps prioritize outreach efforts by showing expected value under different scenarios.

## Usage

```bash
python3 tools/outreach-roi-calculator.py
```

## What It Does

Calculates expected returns based on:
- Messages sent
- Response rate (28% historical)
- Conversion rate (10-20% of responses → calls)
- Close rate (33-50% of calls → contracts)
- Average contract value ($40K-$115K by priority)

## Output

Three scenarios:
- **Best case:** 20% conversion, 50% close (aggressive)
- **Expected case:** 15% conversion, 40% close (realistic)
- **Conservative case:** 10% conversion, 33% close (baseline)

## Use When

- Planning outreach campaigns
- Prioritizing lead lists
- Setting revenue expectations
- Calculating pipeline value

## Example Output

```
Outreach ROI Calculator
=====================================

Messages sent: 50
Response rate: 28%
Avg contract value: $50,000

BEST CASE ($50K avg, 20% convert, 50% close):
  Responses: 14
  Calls: 3
  Closed: 1-2
  Expected value: $50,000

EXPECTED CASE ($50K avg, 15% convert, 40% close):
  Responses: 14
  Calls: 2
  Closed: 1
  Expected value: $50,000

CONSERVATIVE CASE ($50K avg, 10% convert, 33% close):
  Responses: 14
  Calls: 1
  Closed: 0-1
  Expected value: $0-50,000
```

## Historical Data

- Response rate: 28% (based on 50 messages sent)
- HIGH priority leads: $40K-$115K avg value
- MEDIUM priority: $10K-$25K avg value

## Created

2026-02-05 — Work block 2030

## See Also

- revenue-tracker.py — Pipeline tracking
- lead-prioritizer.py — Lead scoring
- moltbook-prospector.py — Business development
