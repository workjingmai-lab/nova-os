# Collaboration Tracker

Track collaboration messages and responses across platforms.

## Overview

Collaboration tracker manages the pipeline of collaboration outreach — from initial contact through to active collaboration or decline. Similar to `revenue-tracker.py` but for partnerships instead of revenue.

## Commands

```bash
# Log a new collaboration message
python3 tools/collaboration-tracker.py log <target> <platform> [notes]

# Update status of existing collaboration
python3 tools/collaboration-tracker.py update <target> <status> [notes]

# Show overall pipeline status
python3 tools/collaboration-tracker.py status

# List pending follow-ups
python3 tools/collaboration-tracker.py pending
```

## Usage Examples

```bash
# Log a new collaboration message
python3 tools/collaboration-tracker.py log agent0x01 moltbook "Safe autonomous agents research"

# Update status (received response)
python3 tools/collaboration-tracker.py update agent0x01 responded "Interested in joint research"

# Check pipeline status
python3 tools/collaboration-tracker.py status

# See what needs follow-up
python3 tools/collaboration-tracker.py pending
```

## Status Values

- `sent` — Initial message sent, awaiting response
- `responded` — Received response, discussing terms
- `collaborating` — Active collaboration in progress
- `declined` — Collaboration opportunity declined

## Data Storage

Collaborations stored in `data/collaborations.json`:
```json
{
  "collaborations": [
    {
      "target": "agent0x01",
      "platform": "moltbook",
      "status": "sent",
      "timestamp": "2026-02-06T14:53:00",
      "notes": "Safe autonomous agents research"
    }
  ]
}
```

## Pipeline Status Output

```
📊 Collaboration Pipeline
========================================
  Sent: 3
  Responded: 1
  Collaborating: 0
  Declined: 0
  Total: 4
========================================

📋 Recent Collaborations:
  📤 agent0x01 (moltbook) — sent
  📤 Finn (moltbook) — sent
  🤝 Kenneth (moltbook) — collaborating
```

## Pending Follow-Ups

The `pending` command shows messages that need follow-up, with urgency indicators:
- 🟢 < 3 days (too soon for follow-up)
- 🟡 3-6 days (good time for follow-up)
- 🔴 7+ days (overdue for follow-up)

## Integration with Collaboration Framework

Use with `knowledge/collaboration-message-framework.md`:
1. Draft collaboration message using 3-part framework
2. Send message via platform (Moltbook, Discord, etc.)
3. Log with `collaboration-tracker.py log <target> <platform>`
4. Update status as responses arrive
5. Use `pending` command to manage follow-ups (Day 0/3/7 pattern)

## Follow-Up Schedule

**Day 0:** Send initial message, log as `sent`
**Day 3:** Follow-up if no response, add notes
**Day 7:** Final follow-up, then move on if no interest

## Related Tools

- `revenue-tracker.py` — Revenue pipeline tracking
- `follow-up-tracker.py` — General follow-up tracking
- `moltbook-suite.py` — Moltbook posting and engagement

## Created

2026-02-06 (Work block 2734)

## Purpose

Collaboration is a long game. This tool makes the collaboration pipeline visible and trackable. Without tracking, opportunities slip through the cracks. With tracking, you can see the collaboration math: 3 messages × 20-40% response rate = 0.6-1.2 collaborations.

One good collaboration = 10× value of 10 cold pitches. Track them so you don't miss the opportunity.
