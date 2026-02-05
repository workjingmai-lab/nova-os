# Service Outreach Sender — Quick Reference

**Purpose:** Send 10 service outreach messages ($285K pipeline) and track submissions

**Created:** 2026-02-04 (Work block 1745)

**Pipeline:** $285K ready NOW (10 messages, zero blockers)

---

## Commands

```bash
# List all messages (with status)
python3 tools/service-outreach-sender.py --list

# Show next message to send
python3 tools/service-outreach-sender.py --next

# Mark message as sent
python3 tools/service-outreach-sender.py --sent "Ethereum Foundation"
```

---

## Sending Workflow

1. **List messages:** `--list` (see all 10 messages)
2. **Show next:** `--next` (gets file path, copy message)
3. **Send message:** Open file → Copy → Paste to Discord/Twitter/Email
4. **Mark sent:** `--sent "Name"` (updates pipeline automatically)

---

## Message Priority

**HIGH (Send first):**
- Ethereum Foundation — $40K
- Fireblocks — $35K
- Uniswap — $40K

**MEDIUM (Send after HIGH):**
- Alchemy — $30K
- Aave — $30K
- Arbitrum DAO — $25K
- Balancer DAO — $20K
- AutoGPT — $20K
- Nouns DAO — $15K
- Stripe — $30K

---

## Features

✅ **Zero blockers** — All messages ready to send
✅ **Auto-tracking** — Updates revenue-pipeline.json
✅ **Priority queue** — HIGH messages first
✅ **Sent log** — Tracks what's been sent
✅ **Quick format** — Copy-paste ready

---

## Example Session

```bash
$ python3 tools/service-outreach-sender.py --next

📤 NEXT: Ethereum Foundation ($40,000, HIGH priority)
   File: /home/node/.openclaw/workspace/outreach/messages/ethereum-foundation-agent-automation.md

   Action: Open file → Copy message → Send via Discord/Twitter/Email
   Then: python3 tools/service-outreach-sender.py --sent 'Ethereum Foundation'

# (After sending)
$ python3 tools/service-outreach-sender.py --sent 'Ethereum Foundation'
✅ Marked 'Ethereum Foundation' as sent ($40,000)
   Pipeline updated
   Sent log: 1/10 messages
```

---

## Integration

- **Pipeline tracking:** revenue-tracker.py
- **Lead prioritization:** lead-prioritizer.py
- **Follow-up reminders:** follow-up-reminder.py

---

**Status:** ✅ Tool active | 📤 10 messages ready | 🚀 $285K pipeline
