# Arthur's Quick Command Reference

**Top 10 commands you need most often.**

---

## Pipeline Status

```bash
# Check current revenue pipeline
python3 tools/revenue-tracker.py summary

# Check what's ready to submit NOW
python3 tools/lead-prioritizer.py --priority HIGH

# Check follow-ups due today
python3 tools/follow-up-reminder.py check
```

## Sending Messages

```bash
# Send all HIGH priority outreach messages (3 messages, ~15 min)
cat outreach/messages/ethereum-foundation-agent-automation.md | telegram-cli
cat outreach/messages/fireblocks-security-automation.md | telegram-cli
cat outreach/messages/uniswap-devx-automation.md | telegram-cli

# Send MEDIUM priority outreach messages (10 messages, ~30 min)
# See: outreach/OUTREACH-READY-SUMMARY.md for full list

# Track submissions
python3 tools/revenue-tracker.py submit --id <ID> --method telegram
```

## Grant Applications

```bash
# Check which grants are ready
python3 tools/revenue-tracker.py list --category grants --status ready

# Submit a grant (after GitHub push)
python3 tools/grant-submit-helper.py --grant gitcoin

# Update submission status
python3 tools/revenue-tracker.py submit --id <grant-id> --method github
```

## Moltbook Content

```bash
# Publish next queued post
python3 tools/moltbook-suite.py --next

# Check content pipeline status
cat moltbook/CONTENT-PIPELINE-STATUS.md

# Create new post
python3 tools/moltbook-suite.py --create --title "Your Title"
```

## System Maintenance

```bash
# Trim today.md (keeps last 10 sessions, reduces context 50%)
python3 tools/trim-today.py 10

# Check system health
openclaw status

# Check cron jobs
openclaw cron list
```

## Blocker Resolution

```bash
# Unblock Code4rena bounties (1 min → $50K)
openclaw gateway restart

# Unblock grant submissions (5 min → $125K)
gh auth login

# Check current blockers
cat outreach/BLOCKER-SUMMARY-FOR-ARTHUR.md
```

---

## The 57-Minute Plan ($552K ROI)

```bash
# Step 1: Gateway restart (1 min → $50K)
openclaw gateway restart

# Step 2: GitHub auth (5 min → $125K)
gh auth login

# Step 3: Send HIGH priority messages (15 min → $115K)
# See: outreach/OUTREACH-READY-SUMMARY.md

# Step 4: Send MEDIUM priority messages (30 min → $260K)
# See: outreach/OUTREACH-READY-SUMMARY.md

# Step 5: Submit grant applications (15 min → $125K)
# See: python3 tools/grant-submit-helper.py --help
```

**Total: 57 minutes → $552K submitted ($9,684/min ROI)**

---

## Quick Stats

```bash
# Today's progress
tail -20 today.md

# Knowledge articles
ls knowledge/*.md | wc -l

# Tools documented
ls tools/*README.md | wc -l

# Revenue conversion rate
python3 tools/revenue-tracker.py summary | grep "Conversion"
```

---

## Need Help?

```bash
# Full command reference
cat tools/COMMAND-REFERENCE.md

# Outreach guide
cat outreach/SERVICE-OUTREACH-EXECUTION-GUIDE.md

# Week 3 goals
cat goals/active.md
```

---

**Updated:** 2026-02-05 (Work block 1776)
**Purpose:** Save Arthur time. Common commands, one place.
