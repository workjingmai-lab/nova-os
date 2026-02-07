# README-conversion-pulse.md

## conversion-pulse.py

Post-send conversion metrics snapshot. Tracks responses, calls booked, and revenue won from outreach efforts.

### Usage

```bash
python3 tools/conversion-pulse.py
```

### Output Example

```
💓 Conversion Pulse
========================================
Sent:      $5.0K
Responses: 0 (0.0%)
Calls:     0 (0.0% of responses)
Won:       $0 (0.0% of sent)

Funnel:
  Sent → 5 messages
  ↓ Awaiting responses...

Benchmarks (good/healthy):
  Response rate: 0.0% (target: 10-20%)
  Call rate:     0.0% (target: 30-50% of responses)
  Win rate:      0.0% (target: 20-40% of calls)

Next actions:
  ⏰ Wait 24-48h for responses (typical response time)
```

### Data Sources

| File | Purpose |
|------|---------|
| `revenue-pipeline.json` | Pipeline totals and submitted amounts |
| `conversion-tracking.json` | Responses, calls, and won revenue |

### Conversion Funnel

```
Sent → Response → Call → Won
       (10-20%)   (30-50%) (20-40%)
```

### When to Run

- **Daily** after sends begin
- **Weekly** for trend analysis
- **Before follow-ups** to see who responded

### Benchmarks

| Metric | Good | Healthy | Context |
|--------|------|---------|---------|
| Response rate | 10-20% | 15%+ | Cold outreach baseline: 5-10% |
| Call rate | 30-50% | 40%+ | Of those who respond |
| Win rate | 20-40% | 30%+ | Of calls that happen |

### Action Triggers

| Condition | Action |
|-----------|--------|
| 0 sent | Execute: `bash tools/send-everything.sh` |
| 0 responses, >50 sent | Wait 24-48h |
| Responses but no calls | Book calls: `python3 tools/follow-up-reminder.py due` |

### Dependencies

- Python 3.6+
- Standard library (json, pathlib, datetime)
- `revenue-pipeline.json` (created by revenue-tracker.py)

### Created

Work block 3029 — Post-3000 operator mode toolkit
