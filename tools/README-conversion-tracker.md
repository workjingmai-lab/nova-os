# conversion-tracker.py

Track outreach responses and conversion rates from initial send to won/lost.

## Usage

```bash
# Show stats, all leads, and follow-ups needed
python3 tools/conversion-tracker.py

# Add a new lead
python3 tools/conversion-tracker.py add "Company Name" 50000 email

# Mark as sent
python3 tools/conversion-tracker.py send 1

# Mark as responded
python3 tools/conversion-tracker.py respond 1

# Mark as won (with optional actual value)
python3 tools/conversion-tracker.py win 1 45000

# Show only follow-ups needed
python3 tools/conversion-tracker.py followups

# List all leads
python3 tools/conversion-tracker.py list
```

## Status Flow

```
ready → sent → responded → called → won/lost
   ↓
(auto flagged for follow-up after 3 days)
```

## Data Storage

- File: `data/conversion-log.json`
- Auto-created on first use
- Tracks: sent_at, responded_at, follow_up_count, actual_value

## Stats Tracked

- Total pipeline value
- Response rate (%)
- Win rate (%)
- Revenue won ($)
- Follow-ups needed
