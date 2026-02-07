# Conversion Tracker Template

Track the journey from sent messages to closed deals.

## What It Does

Monitors the entire conversion funnel:
- **Sent** → **Replies** → **Calls** → **Proposals** → **Won/Lost**

Calculates key metrics:
- Reply rate (target: 15-25%)
- Call rate (target: 40-60%)
- Proposal rate (target: 60-80%)
- Close rate (target: 30-50%)
- Overall conversion (target: 5-10%)

## Usage

```bash
# View current conversion status
python3 conversion-tracker-template.py summary

# Record a response
python3 conversion-tracker-template.py record <message_id> <response_type> [notes]

# Calculate funnel metrics
python3 conversion-tracker-template.py metrics
```

## Response Types

- `interested` - Lead expressed interest
- `not_interested` - Lead declined
- `no_response` - No reply yet
- `call_scheduled` - Call booked
- `proposal_sent` - Proposal delivered
- `won` - Deal closed (revenue!)
- `lost` - Deal lost

## Example Workflow

```bash
# After sending: Update "sent" count in conversion-tracking.json
# After reply: Record response
python3 conversion-tracker-template.py record msg-001 interested "Asked for call"

# After call: Record next step
python3 conversion-tracker-template.py record msg-001 call_scheduled "Tue 2pm UTC"

# After proposal: Track it
python3 conversion-tracker-template.py record msg-001 proposal_sent "$15K, 3-week project"

# Check overall health
python3 conversion-tracker-template.py summary
```

## Why This Matters

**Pre-send:** Pipeline size ($1.49M) — potential, not reality
**Post-send:** Conversion rate (%) — reality, not potential

Pipeline gets you to the starting line. Conversion gets you to revenue.

Tracking conversion = knowing what's working, what's not, and how to improve.

## Key Insights

1. **Speed wins:** Reply within 1 hour = 5× more likely to convert
2. **Follow-up = revenue:** Most deals close after 3-5 touches, not 1
3. **No response ≠ no:** "No" now ≠ "no" forever. Re-engage in 30-60 days
4. **Metrics > feelings:** 5% conversion feels low, but 5% of $1.49M = $74.5K revenue

## Files

- `conversion-tracker-template.py` - Main tool
- `conversion-tracking.json` - Data store (auto-created)
- `README-conversion-tracker-template.md` - This file

## Integration

Works with:
- `revenue-tracker.py` - Pipeline data source
- `follow-up-tracker.py` - Follow-up scheduling
- `diary.md` - Manual logging reference
