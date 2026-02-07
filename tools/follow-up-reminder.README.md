# follow-up-reminder.py

**Purpose:** Check for due follow-ups and send reminders with urgency indicators.

## Usage

```bash
# All due follow-ups (overdue + today + soon)
python3 tools/follow-up-reminder.py

# Only overdue (past due date)
python3 tools/follow-up-reminder.py --urgent

# Due today or overdue
python3 tools/follow-up-reminder.py --today
```

## Output Format

```
🔴 OVERDUE | 2026-02-04 | msg-001 → Ethereum Foundation
🟡 TODAY   | 2026-02-06 | msg-002 → Optimism
🟢 SOON    | 2026-02-08 | msg-003 → Polygon
```

## Urgency Indicators

| Indicator | Meaning | Icon |
|-----------|---------|------|
| OVERDUE   | Past due date | 🔴 |
| TODAY     | Due today | 🟡 |
| SOON      | Due in 1-2 days | 🟢 |
| UPCOMING  | Due 3+ days | ⚪ |
| UNKNOWN   | No date set | gray |

## Integration

Used in heartbeat automation (HEARTBEAT.md):
```yaml
- name: "Follow-up Check"
  every: "6h"
  message: |
    Check for follow-ups due on sent messages.
    1. Run: python3 tools/follow-up-reminder.py --today
    2. If overdue follow-ups exist, flag them
    3. Optionally export checklist
```

## Related Tools

- `follow-up-tracker.py` — Track sent messages and manage follow-ups
- `follow-up-tracker.json` — Data store for all tracked messages

## Why This Matters

Follow-ups = revenue recovery. Most responses come on follow-ups (not first touch).

Automation = no leads slip through cracks. 6-hour heartbeat cadence catches same-day follow-ups.
