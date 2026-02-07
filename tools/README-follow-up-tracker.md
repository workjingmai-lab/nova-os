# follow-up-tracker.py

Track sent outreach messages and their follow-up schedules.

## Why This Tool

**Problem:** Sending 29 messages ($714.5K pipeline) creates a tracking nightmare. When do I follow up? Which messages got responses? What's overdue?

**Solution:** Simple CLI tracker for sent messages with automatic follow-up scheduling.

## Quick Start

```bash
# List all sent messages
python3 tools/follow-up-tracker.py

# Add a sent message (after sending)
python3 tools/follow-up-tracker.py add "Company Name" 25000 "HIGH"

# Check follow-ups due now
python3 tools/follow-up-tracker.py due

# Mark follow-up complete
python3 tools/follow-up-tracker.py done "Company Name" 3

# Get detailed status
python3 tools/follow-up-tracker.py status "Company Name"
```

## Workflow

1. **After sending a message:** `python3 tools/follow-up-tracker.py add <company> <value> <priority>`
2. **Daily:** Run `python3 tools/follow-up-tracker.py due` to see what needs attention
3. **After follow-up:** Mark it done: `python3 tools/follow-up-tracker.py done <company> <day>`

## Data Structure

Stored in `follow-up-tracker.json`:

```json
{
  "sent": [
    {
      "company": "Example Corp",
      "value": 25000,
      "sent_date": "2026-02-06T12:32:00",
      "priority": "HIGH",
      "followups": [
        {"day": 0, "done": false, "date": null},
        {"day": 3, "done": false, "date": null},
        ...
      ],
      "responses": [],
      "status": "SENT"
    }
  ],
  "last_updated": "2026-02-06T12:32:00"
}
```

## Integration

Can be integrated with `service-batch-send.py` to auto-add messages when sent.

## Created

Work block #2676 — 2026-02-06
