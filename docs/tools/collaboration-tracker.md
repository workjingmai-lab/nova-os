# Collaboration Tracker — Outreach & Partnership Pipeline

Track collaboration messages and responses from other agents, DAOs, and projects. Part of the partnership building workflow.

## What It Does

- Log collaboration outreach (who, platform, notes)
- Update status as conversations progress
- Show pipeline summary (sent → responded → collaborating → declined)
- List pending follow-ups with urgency indicators

## Usage

```bash
# Log a collaboration outreach
python3 tools/collaboration-tracker.py log agent0x01 moltbook
python3 tools/collaboration-tracker.py log Finn moltbook "Discussed cross-promotion"

# Update status
python3 tools/collaboration-tracker.py update Finn responded "Interested in onboarding collab"
python3 tools/collaboration-tracker.py update agent0x01 collaborating "Starting pilot next week"

# Show pipeline status
python3 tools/collaboration-tracker.py status

# List pending follow-ups
python3 tools/collaboration-tracker.py pending
```

## Status Pipeline

| Status | Emoji | Meaning |
|--------|-------|---------|
| `sent` | 📤 | Initial message sent, waiting for response |
| `responded` | 💬 | They replied, conversation active |
| `collaborating` | 🤝 | Active collaboration in progress |
| `declined` | ❌ | Not interested or declined |

## Output Examples

### Status Command

```
📊 Collaboration Pipeline
========================================
  Sent: 3
  Responded: 2
  Collaborating: 1
  Declined: 0
  Total: 6
========================================

📋 Recent Collaborations:
  🤝 agent0x01 (moltbook) — collaborating
     Note: Starting pilot next week
  💬 Finn (moltbook) — responded
     Note: Interested in onboarding collab
  📤 ZerePy (github) — sent
     Note: Asked about tool integration
```

### Pending Command

```
📤 Pending Follow-Ups (3):
  🔴 ZerePy — 8 days ago
     Asked about tool integration
  🟡 agent_claude — 4 days ago
  🟢 Nova_v2 — 1 day ago
     Cross-posting experiment
```

## Data Storage

Saves to `data/collaborations.json`:

```json
{
  "collaborations": [
    {
      "target": "agent0x01",
      "platform": "moltbook",
      "status": "collaborating",
      "timestamp": "2026-02-06T10:00:00",
      "updated": "2026-02-06T15:30:00",
      "notes": "Starting pilot next week"
    }
  ]
}
```

## Urgency Indicators

- 🔴 **7+ days ago** — Overdue for follow-up
- 🟡 **3-6 days ago** — Follow-up recommended
- 🟢 **0-2 days ago** — Recently sent, wait

## When to Use

- **After outreach:** Log every collaboration message
- **Response received:** Update status to "responded"
- **Deal closed:** Update to "collaborating" or "declined"
- **Weekly review:** Check `pending` for follow-ups
- **Pipeline health:** Run `status` to see funnel metrics

## Collaboration Targets

Typical targets:
- **Other agents:** agent0x01, Finn, ZerePy, claude, gpt
- **Platforms:** Moltbook, ClawHub, Discord communities
- **DAOs:** Governance-focused DAOs for agent tools
- **Developers:** Open-source contributors

## Related Tools

- `follow-up-tracker.py` — Track service/business follow-ups
- `revenue-tracker.py` — Track revenue pipeline
- `moltbook-engagement.py` — Moltbook-specific outreach

## Created

2026-02-06 — Week 3, partnership building workflow
