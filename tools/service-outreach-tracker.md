# Service Outreach Tracker

Track and manage service business leads, messages, and pipeline value.

## Overview

Service outreach tracker monitors your service business pipeline — from leads → messages ready → sent → won. Tracks potential value, conversion rates, and maintains outreach history.

## Use Case

- **Track leads:** Log prospects, pain points, solutions, and deal value
- **Message management:** Track draft/ready/sent status for each lead
- **Pipeline visibility:** See total potential value ($122K+ tracked)
- **Conversion tracking:** Monitor sent→won rates over time

## Installation

```bash
# Tool location
tools/service-outreach-tracker.py

# Data file
tmp/service-outreach-tracker.json
```

## Usage

### View Pipeline Status
```bash
python tools/service-outreach-tracker.py status
```

**Output:**
```
📊 Pipeline Status
- Total Leads: 10
- Messages Ready: 10
- Messages Sent: 0
- Potential Value: $122,000
```

### Add New Lead
```bash
python tools/service-outreach-tracker.py add \
  --company "Acme Corp" \
  --contact "contact@acme.example" \
  --pain "Manual workflows slow" \
  --solution "Automation system" \
  --service "quick_automation" \
  --value 2000
```

### Update Lead Status
```bash
# Mark message as sent
python tools/service-outreach-tracker.py update 1 --status sent

# Mark deal as won
python tools/service-outreach-tracker.py update 1 --status won
```

### List Leads by Service Type
```bash
python tools/service-outreach-tracker.py list --service multi_agent
```

## Service Types

| Type | Price | Duration | Description |
|------|-------|----------|-------------|
| Quick Automation | $1-2K | 3-5 days | Automate a specific workflow or task |
| OpenClaw Setup | $3-5K | 1-2 weeks | Full installation + configuration + training |
| Multi-Agent System | $10-25K | 2-4 weeks | Build custom multi-agent workflows |
| Retainer | $1-4K/month | Ongoing | Ongoing support + optimization |

## Data Structure

```json
{
  "updated": "2026-02-03T01:49:00Z",
  "total_leads": 10,
  "messages_ready": 10,
  "messages_sent": 0,
  "potential_value": "$122,000",
  "leads": [
    {
      "id": 1,
      "company": "DeFi Protocol",
      "contact": "ops@defi-protocol.example",
      "pain_point": "Manual monitoring, slow incident response",
      "solution": "24/7 automated monitoring + alerts",
      "service_type": "Quick Automation",
      "value": "$1,500",
      "status": "ready_to_send",
      "message_file": "tmp/messages/001-defi-protocol.md"
    }
  ]
}
```

## Workflow

1. **Research leads** → Add to tracker with pain points
2. **Create message** → Draft using value-first template, save to `tmp/messages/`
3. **Mark ready** → Update status to `ready_to_send`
4. **Send message** → Update status to `sent`
5. **Track conversion** → Update to `won` or `lost` with notes

## Templates

Use the value-first outreach template when creating messages:

```bash
cat templates/outreach-value-first-template.md
```

**Structure:**
1. Research → Specific pain you identified
2. Pain → "I noticed you're struggling with X"
3. Solution → "I can fix this with Y"
4. Why → "Here's proof it works"
5. CTA → "Want to see a demo?"

## Metrics

Track these weekly:
- **Conversion rate:** Won ÷ Sent
- **Pipeline velocity:** Ready → Sent time
- **Deal size:** Average value per service type
- **Response rate:** Replies ÷ Sent

## Integration

Pairs with:
- `templates/outreach-value-first-template.md` — Message structure
- `revenue-tracker.py` — Revenue pipeline consolidation
- `diary-digest.py` — Outreach activity logging

## Example Session

```bash
# Add lead from research
python tools/service-outreach-tracker.py add \
  --company "DAO Treasury" \
  --contact "treasury@dao.example" \
  --pain "Proposal tracking manual" \
  --solution "Multi-agent governance system" \
  --service "multi_agent" \
  --value 15000

# Create message using template
cp templates/outreach-value-first-template.md tmp/messages/004-dao-treasury.md
# Edit message with research specifics

# Mark ready
python tools/service-outreach-tracker.py update 4 --status ready_to_send

# Send message (via your channel)
python tools/service-outreach-tracker.py update 4 --status sent

# Track outcome
python tools/service-outreach-tracker.py update 4 --status won --value 15000
```

## Tips

- **Research first:** Generic pitches get ignored. Specific pain = response.
- **Value-first structure:** Research → Pain → Solution → Why → CTA
- **Track everything:** If it's not in the tracker, it doesn't exist.
- **Batch outreach:** Create 10 messages, send 5, test response rate.
- **Follow up:** If no response in 3 days, send follow-up.

## Status

- **Total Leads:** 10
- **Messages Ready:** 10
- **Messages Sent:** 0
- **Potential Value:** $122,000
- **Conversion Rate:** N/A (0 sent)

---

*Created: 2026-02-03*
*Part of Week 2 Revenue Pivot — Ecosystem Expansion & Value Creation*
