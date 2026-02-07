# response-tracker.py

Track responses to outreach messages and measure conversion rates.

## What It Does

- **Track responses:** Record positive, negative, callback, or won responses
- **Calculate stats:** Response rates, positive rates, conversion funnel
- **Follow-up management:** See pending follow-ups
- **Export reports:** Generate summary reports

## Usage

```bash
# Add a response
python3 tools/response-tracker.py --prospect "Uniswap" --response "positive" --notes "Interested in audit services"

# View statistics
python3 tools/response-tracker.py --stats

# Check pending follow-ups
python3 tools/response-tracker.py --followups

# Export report
python3 tools/response-tracker.py --export

# Log a won deal
python3 tools/response-tracker.py --prospect "Balancer" --response "won" --notes "Audit contract signed" --value 25000
```

## Response Types

- `positive` — Positive response, interested
- `negative` — Not interested, declined
- `callback` — Call scheduled
- `won` — Deal closed, revenue booked

## Data Stored

Creates `response-tracker.json` with:
- Response log (timestamp, type, notes, value)
- Aggregated stats (totals, rates)
- Follow-up dates

## When to Use

1. **After sending outreach** — Record any responses
2. **Weekly reviews** — Check `--stats` for conversion rates
3. **Before follow-ups** — Check `--followups` for pending items
4. **Monthly reporting** — `--export` for summary

## Example Output

```
📊 Response Statistics
==================================================
Total Sent:       39
Total Responded:  12
Response Rate:    30.8%

Breakdown:
  Positive:        8
  Negative:        3
  Calls:           2
  Won:             1
  Total Value:     $25,000

Positive Rate:    66.7% (of responses)
```

## Integration with Other Tools

- **send-service-messages.py** — After sending, use this to track responses
- **revenue-tracker.py** — Sync won deals to revenue pipeline
- **follow-up-reminder.py** — Auto-generate follow-up reminders

## ROI Calculation

Response tracking enables:
- Calculate true conversion rates (sent → responded → won)
- Identify high-value channels (DAOs vs protocols vs exchanges)
- Optimize outreach based on real data, not guesses
- Measure ROI of outreach campaigns

## Files Created

- `response-tracker.json` — Response database
- No external dependencies

---

**Tool created:** 2026-02-05 (Work block 2247)
**Purpose:** Prepares for shipping phase by tracking conversion metrics
**Status:** Ready for use when Arthur begins sending outreach
