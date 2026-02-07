# TOP-10-QUICK-COMMANDS.md — Nova's Most-Used Commands

**Last Updated:** 2026-02-05 (Work block 2167)
**Purpose:** 10 commands you'll use 90% of the time

---

## 🚀 Daily Status (Every Session Start)

```bash
# Quick status check (1 second)
python3 tools/quick-status.py

# Full pipeline summary
python3 tools/revenue-tracker.py summary
```

---

## 💰 Revenue Pipeline Management

```bash
# View all leads with priority scores
python3 tools/lead-prioritizer.py

# Check due follow-ups
python3 tools/follow-up-reminder.py

# Update lead status
python3 tools/revenue-tracker.py update --status ready --name "Ethereum Foundation"
```

---

## ✍️ Outreach Messages

```bash
# List all ready-to-send messages
ls outreach/messages/*.md

# View specific message
cat outreach/messages/ethereum-foundation-agent-automation.md

# Count messages by priority
grep -l "HIGH priority" outreach/messages/*.md | wc -l
```

---

## 📊 Work Velocity & Progress

```bash
# Calculate work velocity and milestones
python3 tools/velocity-calc.py

# Check execution gap
python3 tools/execution-gap.py
```

---

## 🔧 System Unblockers

```bash
# Gateway restart (unblocks bounties)
openclaw gateway restart

# GitHub CLI auth (unblocks grant submissions)
gh auth login

# Check gateway status
openclaw gateway status
```

---

## 📝 Documentation & Knowledge

```bash
# View knowledge index
cat knowledge/INDEX.md

# Search knowledge articles
grep -r "Revenue Pipeline" knowledge/*.md

# View diary digest
python3 tools/diary-digest.py
```

---

## 🎯 Moltbook Content

```bash
# Post to Moltbook
python3 tools/moltbook-poster.py

# Check Moltbook engagement
python3 tools/moltbook-engagement.py

# View queued drafts
cat moltbook-drafts.md | grep "^# Draft"
```

---

## 🛠️ Quick Troubleshooting

```bash
# Check if OpenClaw is running
openclaw gateway status

# View recent work blocks
tail -20 diary.md

# Check today's progress
head -50 today.md

# View revenue pipeline JSON
cat data/revenue-pipeline.json | jq .
```

---

## 📋 Daily Checklist (Arthur's 57-Min Plan)

```bash
# Step 1: Quick status
python3 tools/quick-status.py

# Step 2: Clear blockers
openclaw gateway restart
gh auth login

# Step 3: Send messages (copy from outreach/messages/)
# Example: Copy message content and send via email/Discord

# Step 4: Check results
python3 tools/revenue-tracker.py summary
```

---

## 💡 Pro Tips

1. **Start every session with `quick-status.py`** — 1 second gives you full context
2. **Use `lead-prioritizer.py`** — Don't guess, use data to pick HIGH priority leads
3. **Check `follow-up-reminder.py` daily** — 80% of deals close after 5th contact
4. **Keep messages organized** — All outreach messages in `outreach/messages/*.md`
5. **Document results** — Update pipeline status after sending: `revenue-tracker.py update --status submitted`

---

## 🎮 Workflow Example (Sending a Message)

```bash
# 1. Check status
python3 tools/quick-status.py

# 2. List HIGH priority messages
grep -l "HIGH priority" outreach/messages/*.md

# 3. View message content
cat outreach/messages/ethereum-foundation-agent-automation.md

# 4. Copy message (send via your channel)
# Content is PROOF framework: Pain → Research → Offer → Outcome → Follow-up

# 5. Update status
python3 tools/revenue-tracker.py update --status submitted --name "Ethereum Foundation"

# 6. Verify
python3 tools/revenue-tracker.py summary
```

---

**Remember:** 10 commands = 90% of usage. Master these first.

**Created:** Work block 2168
**Author:** Nova
