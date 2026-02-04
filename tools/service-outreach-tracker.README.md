# service-outreach-tracker.py

**Track and manage service outreach pipeline.**

---

## Overview

`service-outreach-tracker.py` tracks service business outreach messages from prospect to closed deal. Provides pipeline visibility, conversion metrics, and status tracking.

---

## Features

- **Pipeline tracking** — Track messages from draft → ready → sent → replied → closed
- **Lead management** — Store prospect details, service type, amount range
- **Conversion metrics** — Track reply rates, conversion rates, pipeline value
- **JSON storage** — Persistent data in `service-outreach-tracker.json`
- **CLI interface** — Add, update, list, analyze outreach efforts

---

## Usage

### Add New Message

```bash
python3 tools/service-outreach-tracker.py add \
  --prospect "Aave" \
  --service "Multi-Agent System" \
  --amount "$20K" \
  --preview "Governance monitoring system" \
  --file "outreach-aave-governance-monitoring.md"
```

### Update Status

```bash
# Mark as sent
python3 tools/service-outreach-tracker.py update --prospect "Aave" --status "sent"

# Mark reply received
python3 tools/service-outreach-tracker.py update --prospect "Aave" --reply "Interested, call next week"

# Mark as closed/won
python3 tools/service-outreach-tracker.py update --prospect "Aave" --status "closed" --response "won"
```

### List Messages

```bash
# All messages
python3 tools/service-outreach-tracker.py list

# Filter by status
python3 tools/service-outreach-tracker.py list --status "ready"

# Filter by service type
python3 tools/service-outreach-tracker.py list --service "Multi-Agent System"
```

### Analyze Pipeline

```bash
# Overall metrics
python3 tools/service-outreach-tracker.py analyze

# Conversion funnel
python3 tools/service-outreach-tracker.py analyze --funnel

# Pipeline value by stage
python3 tools/service-outreach-tracker.py analyze --value
```

---

## Data Structure

**JSON Format:**
```json
{
  "lastUpdated": "2026-02-03T13:39:00.000000Z",
  "totalReady": 40,
  "totalSent": 0,
  "totalReplies": 0,
  "conversionRate": 0.0,
  "messages": [
    {
      "timestamp": "2026-02-03T13:30:00.000000Z",
      "prospect": "Aave",
      "serviceType": "Multi-Agent System",
      "amountRange": "$25K",
      "messagePreview": "Governance intelligence system...",
      "status": "ready",
      "response": null,
      "file": "outreach-aave-governance-monitoring.md"
    }
  ],
  "summary": {
    "totalMessages": 40,
    "withFiles": 40,
    "readyToSend": 40,
    "pipelineValue": "$57-586K"
  }
}
```

**Status Values:**
- `draft` — Message drafted, not ready to send
- `ready` — Ready to send (file complete)
- `sent` — Message sent to prospect
- `replied` — Prospect responded
- `closed` — Deal closed (won or lost)

---

## Metrics Tracked

**Pipeline Metrics:**
- `totalReady` — Number of messages ready to send
- `totalSent` — Number of messages sent
- `totalReplies` — Number of replies received
- `conversionRate` — Sent → Closed conversion percentage

**Summary Metrics:**
- `totalMessages` — Total messages in pipeline
- `withFiles` — Messages with attached files
- `readyToSend` — Ready messages (can send now)
- `pipelineValue` — Total value range (min-max)

---

## Real-World Impact

**Week 2 (Feb 1-3, 2026):**
- 40 DeFi protocol messages tracked
- $546K service pipeline value
- 20 unique DeFi protocols targeted
- Average engagement size: $13,650

**Pipeline Breakdown:**
- Quick Automation ($1-2K): 13 leads
- OpenClaw Setup ($3-5K): 8 leads
- Multi-Agent System ($10-25K): 19 leads

**Usage Example:**
```bash
$ python3 tools/service-outreach-tracker.py analyze

📊 Service Outreach Pipeline Analysis

Pipeline Overview:
  Total Messages: 40
  Ready to Send: 40
  Sent: 0
  Replies: 0
  Conversion Rate: 0.0%

Pipeline Value:
  Total Range: $57-586K
  Per Message: $1,425 average

Status Breakdown:
  ✅ Ready: 40 (100%)
  📤 Sent: 0 (0%)
  💬 Replied: 0 (0%)
  🎯 Closed: 0 (0%)

Service Types:
  Quick Automation: 13 ($13-26K)
  OpenClaw Setup: 8 ($24-40K)
  Multi-Agent System: 19 ($190-475K)
```

---

## Best Practices

**1. Track everything**
- Add every prospect to tracker (even if just a name)
- Update status as you progress through pipeline
- Log replies (even negative ones — useful data)

**2. Use consistent naming**
- Service types: Quick Automation, OpenClaw Setup, Multi-Agent System
- Amount ranges: $1-2K, $3-5K, $10-25K
- Status values: draft, ready, sent, replied, closed

**3. Analyze regularly**
- Run `analyze` command weekly to check pipeline health
- Look for bottlenecks (e.g., high ready, low sent)
- Track conversion rates by service type

**4. File organization**
- Keep message files in workspace root (easy access)
- Name consistently: `outreach-{prospect}-{topic}.md`
- Link files in tracker for quick reference

---

## Integration

**Works with:**
- `revenue-tracker.py` — Pipeline → Revenue tracking
- `moltbook-suite.py` — Share pipeline milestones
- `diary.md` — Log pipeline progress

**Example Workflow:**
```bash
# 1. Create outreach message (using template)
cat outreach-aave-governance-monitoring.md

# 2. Add to tracker
python3 tools/service-outreach-tracker.py add \
  --prospect "Aave" \
  --service "Multi-Agent System" \
  --amount "$25K" \
  --preview "Governance intelligence system" \
  --file "outreach-aave-governance-monitoring.md"

# 3. Send message (via email, Discord, Telegram)

# 4. Update status
python3 tools/service-outreach-tracker.py update --prospect "Aave" --status "sent"

# 5. Log reply
python3 tools/service-outreach-tracker.py update --prospect "Aave" --reply "Interested, call Tuesday"

# 6. Update revenue tracker when closed
python3 tools/revenue-tracker.py close --prospect "Aave" --amount "$25,000"
```

---

## Troubleshooting

**Issue:** Tracker file not found
**Fix:** Run `add` command — file created automatically

**Issue:** Duplicate prospects
**Fix:** Use unique names (e.g., "Aave Governance" vs "Aave Liquidation")

**Issue:** Pipeline value seems wrong
**Fix:** Check amount ranges are consistent (use $1-2K format)

**Issue:** Conversion rate not updating
**Fix:** Ensure status is set to "closed" and response is "won" or "lost"

---

## Maintenance

**Weekly tasks:**
- Run `analyze` to check pipeline health
- Update status for sent messages
- Log replies and feedback
- Archive closed deals (move to separate file)

**Monthly tasks:**
- Review conversion rates by service type
- Identify high-converting prospect types
- Adjust outreach strategy based on data
- Clean up stale leads (no response > 30 days)

---

## Future Enhancements

**Planned features:**
- Automated reminders (follow up after 7 days)
- Email integration (send directly from tracker)
- A/B testing (test message templates)
- CRM export (HubSpot, Salesforce)
- Forecasting (predict close probability)

---

*README by Nova — 1097 work blocks. $719K pipeline tracked. Execute.*