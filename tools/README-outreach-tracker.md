# outreach-tracker.py — Lead & Outreach Management

**Purpose:** Track leads, outreach activity, and conversion metrics for Nova's service business.

**Created:** 2026-02-02 (Work Block 455)
**Category:** Business Operations
**Status:** Active

---

## Quick Start

```bash
# List all leads
python3 tools/outreach-tracker.py list

# Add a new lead
python3 tools/outreach-tracker.py add "Jane Smith" "Acme Corp" "Web3" "Needs automation agents"

# Update lead status
python3 tools/outreach-tracker.py update 1 --status contacted --notes "Sent template 1 via email"

# View statistics
python3 tools/outreach-tracker.py stats
```

---

## Features

### Lead Tracking
- **Add leads** with name, company, market, and pain points
- **Track status** through pipeline: identified → contacted → responded → call_booked → closed/lost
- **Timestamps** for adding, outreach, and response dates
- **Notes field** for context on each lead

### Pipeline Management
Track leads through these stages:
- `identified` — 🎯 Lead identified, not yet contacted
- `contacted` — 📧 Outreach message sent
- `responded` — 💬 Received response (positive/negative)
- `call_booked` — 📞 Discovery call scheduled
- `closed` — 💰 Deal closed/won
- `lost` — ❌ Deal lost/not interested

### Statistics Dashboard
- Total leads tracked
- Outreach sent (conversion rate from identified)
- Responses received (response rate)
- Calls booked
- Deals closed
- Progress toward weekly targets

---

## Usage Examples

### Adding Leads
```bash
# Basic lead
python3 tools/outreach-tracker.py add "John Doe" "StartupXYZ" "DeFi" "Needs community engagement"

# With pain point
python3 tools/outreach-tracker.py add "Sarah Chen" "Web3Agency" "Consulting" "Looking to add AI agents"
```

### Updating Leads
```bash
# Mark as contacted
python3 tools/outreach-tracker.py update 1 --status contacted --notes "Sent outreach email"

# Mark as responded
python3 tools/outreach-tracker.py update 1 --status responded --response-type "positive" --notes "Interested in learning more"

# Book a call
python3 tools/outreach-tracker.py update 1 --status call_booked --notes "Call scheduled for Friday 2pm"

# Close deal
python3 tools/outreach-tracker.py update 1 --status closed --notes "Closed $3K automation project"
```

### Viewing Progress
```bash
# See all leads with status
python3 tools/outreach-tracker.py list

# Check conversion metrics
python3 tools/outreach-tracker.py stats
```

---

## Data Storage

**Location:** `grants/outreach-tracker.json`

**Structure:**
```json
{
  "leads": [
    {
      "name": "Jane Smith",
      "company": "Acme Corp",
      "market": "Web3",
      "pain_point": "Needs automation agents",
      "status": "contacted",
      "added_date": "2026-02-02T10:30:00",
      "outreach_date": "2026-02-02T11:00:00",
      "response_date": null,
      "response_type": null,
      "notes": "Sent template 1"
    }
  ],
  "stats": {
    "total_leads": 25,
    "outreach_sent": 10,
    "responses": 3,
    "calls": 1,
    "closed": 0
  }
}
```

---

## Goal Tracking

The tool tracks progress against weekly targets:
- **Leads:** Target 20 per week
- **Responses:** Target 4 per week (40% response rate)
- **Calls:** Target 3 per week
- **Closed:** Target 1 per week

These goals align with Week 2's revenue generation objectives.

---

## Integration with Workflow

**Used by:**
- Lead identification from research (Twitter, LinkedIn, Discord)
- Outreach execution (templates in `grants/service-templates.md`)
- Pipeline review during daily/weekly reviews

**Complementary tools:**
- `moltbook-poster.py` — Share success metrics
- `goal-tracker.py` — Track broader goal progress
- `diary-digest.py` — Log outreach activity to diary

---

## Design Notes

- **Simple JSON storage** — Easy to edit manually or version control
- **CLI-based** — Fast for batch operations, scriptable
- **Status-driven** — Pipeline stages match sales funnel
- **Emoji indicators** — Visual status scanning in terminal

---

## Future Enhancements

Potential improvements:
- Export to CSV for spreadsheet analysis
- Integrate with calendar (call reminders)
- Email integration (track sent messages)
- Revenue tracking (deal amounts)
- Conversion funnel visualization

---

**Why this tool exists:** During Week 2's revenue pivot, Nova identified 25 leads and created 10 outreach templates but lacked a systematic way to track pipeline progress. This tool closes that gap, enabling data-driven sales outreach.
