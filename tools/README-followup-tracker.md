# followup-tracker.py

Track sent messages and manage follow-up schedules.

## What It Does

Records when you send outreach messages and calculates when follow-ups are due (Day 3, 7, 14, 21).

## Commands

```bash
# Record a sent message
python3 tools/followup-tracker.py record <prospect> <type> <amount> <channel> [date]

# Example:
python3 tools/followup-tracker.py record "Ethereum Foundation" "service" 40000 "email"

# Check what follow-ups are due
python3 tools/followup-tracker.py due

# List all tracked messages
python3 tools/followup-tracker.py list
```

## Workflow

1. **Send a message** (email, Discord, etc.)
2. **Record it:** `followup-tracker.py record ...`
3. **Check daily:** `followup-tracker.py due`
4. **Send follow-ups** for items shown as due

## Data Storage

- **File:** `followup-tracker.json`
- **Tracks:** Prospect, type, amount, channel, send date, follow-up dates

## Follow-up Schedule

- **Day 3:** Quick bump to top of inbox
- **Day 7:** "Any thoughts?" check-in
- **Day 14:** "Still interested?" gentle reminder
- **Day 21:** Final check-in (last contact)

## Use Case

After executing `TODAY-SHIPPING-MANIFEST.md` protocol, use this tool to:
1. Record all messages sent
2. Get daily reminders for follow-ups
3. Ensure no leads fall through cracks

## Integration

Works with:
- `revenue-tracker.py` (pipeline management)
- `TODAY-SHIPPING-MANIFEST.md` (shipping protocol)

## Created

2026-02-06 — Work block 2541
