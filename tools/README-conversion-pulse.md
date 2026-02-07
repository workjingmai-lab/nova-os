# conversion-pulse.py — Post-Send Conversion Metrics

**Created:** 2026-02-07 (Work block 3029)
**Purpose:** Daily conversion funnel health check after sending outreach

## What It Does

Shows your conversion funnel at a glance:
- **Sent:** Total amount of outreach sent
- **Responses:** How many replied (with response rate %)
- **Calls:** How many calls booked (with call rate %)
- **Won:** Revenue closed (with win rate %)

Plus benchmarks and action items based on current state.

## Usage

```bash
python3 tools/conversion-pulse.py
```

## Output Example

```
💓 Conversion Pulse
========================================
Sent:      $734.5K
Responses: 42 (5.7%)
Calls:     12 (28.6% of responses)
Won:       $25.0K (3.4% of sent)

Funnel:
  Sent → 734500 messages
  ↓ 5.7% response rate
  Responses → 42
  ↓ 28.6% call rate
  Calls → 12
  ↓ 20.0% win rate
  Revenue → $25.0K

Benchmarks (good/healthy):
  Response rate: 5.7% (target: 10-20%)
  Call rate:     28.6% (target: 30-50% of responses)
  Win rate:      20.0% (target: 20-40% of calls)

Next actions:
  📞 Book calls: python3 tools/follow-up-reminder.py due
```

## Why This Matters

**Pre-send:** You're building pipeline.
**Post-send:** You're optimizing conversion.

This tool is for the post-send phase. It tells you:
1. Are people responding? (If 0% after 72h → outreach needs fixing)
2. Are we booking calls? (If < 30% → follow-up needs work)
3. Are we closing? (If < 20% → proposal/pricing needs review)

**Visibility = Optimization.**

## Benchmarks

Based on industry standards for B2B outreach:

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Response rate | 10-20% | 5-10% | < 5% |
| Call rate | 30-50% of responses | 20-30% | < 20% |
| Win rate | 20-40% of calls | 10-20% | < 10% |

## Integration

Add to your **daily routine** (after sends go out):

```bash
# Morning: Check pulse
python3 tools/conversion-pulse.py

# If responses pending: Wait 24-48h
# If responses low: Review outreach templates
# If calls needed: python3 tools/follow-up-reminder.py due
```

## Data Sources

Reads from:
- `revenue-pipeline.json` — Total pipeline and submitted amounts
- `conversion-tracking.json` — Responses, calls, won deals

## Technical Notes

- **Funnel math:** Each stage is % of previous stage (not % of total sent)
- **Response rate:** % of sent messages that got replies
- **Call rate:** % of responses that converted to calls
- **Win rate:** % of sent messages that became revenue
- **Action items:** Generated based on funnel state (e.g., if 0 calls → remind to book)

## Future Enhancements

- Add --trend flag to show conversion over time (7-day, 30-day)
- Add --by-category to break down grants vs services vs bounties
- Add alert thresholds (email/SMS if response rate < 5% for 3 days)
- Show average time-to-response and time-to-close
- Predictive modeling (e.g., "At current rate, expect $X in 30 days")

## Related Tools

- `verify-leads.py` — Pre-send validation
- `send-everything.sh` — Execute sends
- `daily-revenue-dashboard.py` — Pipeline health
- `follow-up-reminder.py` — Response tracking
- `revenue-tracker.py` — Full pipeline view
