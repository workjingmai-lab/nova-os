# template-tracker.py

Track follow-up template usage and measure effectiveness over time.

## Quick Start

```bash
# View summary
python3 tools/template-tracker.py

# Record template usage
python3 tools/template-tracker.py record "Uniswap Labs" 5 2026-02-07

# Record response
python3 tools/template-tracker.py response "Uniswap Labs" yes "Call scheduled"
```

## Why This Exists

Follow-up templates are only useful if you know which ones work. This tracks:
- Which templates get used
- Response rates by scenario
- Outcomes (calls scheduled, deals closed, etc.)

## Template IDs

| ID | Scenario | Use When |
|----|----------|----------|
| 1 | No Response (Day 3) | 72hrs, no reply |
| 2 | No Response (Day 7) | 1 week, no reply |
| 3 | Not Interested | Explicit no |
| 4 | Send More Info | They ask for details |
| 5 | Interested | Positive response |
| 6 | Using Competitor | Competitor mentioned |
| 7 | Forwarded | Message passed to teammate |
| 8 | Too Expensive | Price objection |
| 9 | Wrong Person | Not their domain |
| 10 | Delayed Response | Reply after weeks |

## Data File

Stored in `data/template-usage.json`:
```json
{
  "usages": [
    {
      "lead": "Company Name",
      "template_id": 5,
      "scenario": "Interested - Let's Talk",
      "sent_date": "2026-02-07",
      "response": true,
      "outcome": "Call scheduled for Monday"
    }
  ]
}
```

## Output Example

```
============================================================
FOLLOW-UP TEMPLATE EFFECTIVENESS
============================================================

Total Templates Sent: 15
Total Responses: 6
Overall Response Rate: 40.0%

By Template:
------------------------------------------------------------
   5. Interested - Let's Talk    |  3/ 3 (100.0%) ██████████
   4. Send More Info             |  2/ 4 ( 50.0%) █████
   1. No Response (Day 3)        |  1/ 5 ( 20.0%) ██

Recent Activity:
------------------------------------------------------------
  ✓ 2026-02-07 | Uniswap Labs        | Interested - Let's Talk
  ⏳ 2026-02-07 | Balancer Labs       | No Response (Day 3)
```

## Workflow

1. Send follow-up using template from `knowledge/follow-up-templates.md`
2. Record usage: `python3 tools/template-tracker.py record "Lead Name" <template_id>`
3. When they respond: `python3 tools/template-tracker.py response "Lead Name" yes "Outcome"`
4. Review weekly: `python3 tools/template-tracker.py` to see what's working

## Related

- Templates: `knowledge/follow-up-templates.md`
- Revenue tracking: `tools/revenue-tracker.py`
- Pipeline: `data/revenue-pipeline.json`
