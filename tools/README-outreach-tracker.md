# outreach-tracker.py — Lead & Outreach Management System

## What It Does

Manages your entire sales pipeline for Nova's service business:
- Track leads with status (identified → closed)
- Log outreach activities (emails sent, responses received)
- Monitor conversion metrics
- Track progress against weekly goals
- Persistent JSON storage

## When to Use It

- **Lead capture:** Add prospects as you discover them
- **Outreach logging:** Record when you contact leads
- **Pipeline reviews:** Check conversion funnel status
- **Goal tracking:** Monitor progress toward weekly targets

## Installation

No dependencies needed. Uses Python stdlib only.

```bash
# Already in workspace/tools/
chmod +x tools/outreach-tracker.py

# Create tracking file (auto-created on first use)
touch grants/outreach-tracker.json
```

## Usage

```bash
# List all leads
python3 tools/outreach-tracker.py list

# Add a new lead
python3 tools/outreach-tracker.py add 'John Doe' 'Acme Inc' 'Web3' 'Needs community agent'

# Update lead status
python3 tools/outreach-tracker.py update 1 --status contacted --notes 'Sent email via template 1'

# Show statistics
python3 tools/outreach-tracker.py stats
```

## Lead Statuses

| Status | Emoji | Description |
|--------|-------|-------------|
| `identified` | 🎯 | Lead discovered, not yet contacted |
| `contacted` | 📧 | Outreach sent, awaiting response |
| `responded` | 💬 | Lead replied, in conversation |
| `call_booked` | 📞 | Meeting scheduled |
| `closed` | 💰 | Deal won/converted |
| `lost` | ❌ | Deal lost/not interested |

## Output Format

**List view:**
```
📋 OUTREACH LEADS (3 total)
══════════════════════════════════════════════════════════════════════════

1. 🎯 John Doe (Acme Inc)
   Market: Web3
   Status: identified
   Added: 2026-02-02T12:00:00

2. 📧 Jane Smith (XYZ Corp)
   Market: SaaS
   Status: contacted
   Added: 2026-02-01T15:30:00
   Outreach: 2026-02-02T10:15:00

3. 💬 Bob Johnson (Startup.io)
   Market: DeFi
   Status: responded
   Added: 2026-01-31T09:00:00
   Outreach: 2026-02-01T14:20:00
   Response: 2026-02-02T08:45:00 (positive)
```

**Stats view:**
```
📊 OUTREACH STATISTICS
════════════════════════════════════════════
Total Leads:        25
Outreach Sent:      15 (60.0%)
Responses:          6 (40.0%)
Calls Booked:       3
Closed Deals:       1

🎯 WEEK 3-4 GOAL TRACKING
────────────────────────────────────────────────
Leads (target 20):     25/20 (125%)
Responses (target 4):  6/4 (150%)
Calls (target 3):      3/3 (100%)
Closed (target 1):     1/1 (100%)
```

## Data Structure

**JSON format (grants/outreach-tracker.json):**
```json
{
  "leads": [
    {
      "name": "John Doe",
      "company": "Acme Inc",
      "market": "Web3",
      "pain_point": "Needs community agent",
      "status": "contacted",
      "added_date": "2026-02-02T12:00:00",
      "outreach_date": "2026-02-02T14:30:00",
      "response_date": null,
      "response_type": null,
      "notes": "Sent email via template 1"
    }
  ],
  "stats": {
    "total_leads": 25,
    "outreach_sent": 15,
    "responses": 6,
    "calls": 3,
    "closed": 1
  }
}
```

## Integration Examples

```bash
# Morning pipeline check
alias pipeline="python3 tools/outreach-tracker.py list"
pipeline  # Show all leads

# Quick stats
alias outreach-stats="python3 tools/outreach-tracker.py stats"
outreach-stats  # Show conversion funnel

# Add lead from research
python3 tools/outreach-tracker.py add \
  'Sarah Connor' \
  'Skynet Systems' \
  'AI Safety' \
  'Needs alignment agent'

# Log outreach activity
python3 tools/outreach-tracker.py update 5 \
  --status contacted \
  --notes 'Sent cold email, used template 3'

# Update after response
python3 tools/outreach-tracker.py update 5 \
  --status responded \
  --notes 'Positive response, interested in demo'
```

## Weekly Goals (Week 3-4)

The tracker includes built-in goal tracking for Weeks 3-4:
- **Leads:** 20 total (125% achieved)
- **Responses:** 4 positive responses (150% achieved)
- **Calls:** 3 calls booked (100% achieved)
- **Closed:** 1 deal closed (100% achieved)

## Conversion Metrics

- **Outreach rate:** `outreach_sent / total_leads`
- **Response rate:** `responses / outreach_sent`
- **Call rate:** `calls / responses`
- **Close rate:** `closed / calls`

Track these to optimize your sales funnel.

## Error Handling

- Gracefully handles missing JSON file (creates new)
- Validates lead index on update
- Handles missing optional fields
- Returns helpful usage messages

## Performance Notes

- Entire JSON file loaded into memory
- Suitable for hundreds of leads
- Atomic write operations (safe concurrent access)

## Maintenance Notes

- **Last updated:** 2026-02-02
- **Dependencies:** None (stdlib only)
- **Storage:** `grants/outreach-tracker.json`
- **Backup:** Consider adding git tracking for JSON file

## See Also

- `lead-researcher.py` — Automated lead discovery
- `grant-submit-helper.py` — Grant submission tracking
- `moltbook-prospector.py` — Find agents to connect with

---

**Created:** 2026-02-02 (Work Block 455)
**Category:** Business
**Status:** ✅ Production-ready
