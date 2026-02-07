# Arthur's Command Summary

**Every command you need. One page.**

---

## 🔵 CHECK STATUS

### Full Status Check
```bash
bash tools/status-check.sh
```
**Shows:** Pipeline, progress, gaps, next actions
**When:** Start of any session

### Revenue Pipeline
```bash
python3 tools/revenue-tracker.py summary
```
**Shows:** Total pipeline, ready, submitted, conversion
**When:** After executing, tracking progress

### Follow-Up Status
```bash
python3 tools/followup-reminder.py list
```
**Shows:** All scheduled follow-ups
**When:** Daily check-ins

---

## 🚢 SHIP EVERYTHING

### Full Send (Grants + Services)
```bash
bash tools/send-everything.sh full
```
**Sends:** $734.5K total (Grants $125K + Services $609.5K)
**Time:** 15-20 minutes
**When:** Ready to execute

### Quick Send (Grants Only)
```bash
bash tools/send-everything.sh quick
```
**Sends:** $125K grants only
**Time:** 5-8 minutes
**When:** Testing, grants-only focus

### Test Run (Dry Run)
```bash
bash tools/send-everything.sh test
```
**Shows:** What would send, without sending
**Time:** 1 minute
**When:** Pre-flight verification

---

## 📊 TRACK REVENUE

### Add New Lead
```bash
python3 tools/revenue-tracker.py add
```
**Adds:** New opportunity to pipeline
**Fields:** Name, type (grant/service), value, status

### Update Status
```bash
python3 tools/revenue-tracker.py update <id>
```
**Updates:** Lead status (ready → submitted → won/lost)
**When:** Status changes

### List Pipeline
```bash
python3 tools/revenue-tracker.py list
```
**Shows:** All leads in pipeline
**When:** Review full pipeline

### Show Follow-Ups
```bash
python3 tools/revenue-tracker.py followup
```
**Shows:** Leads needing follow-up
**When:** Planning follow-up sequence

---

## 📅 MANAGE FOLLOW-UPS

### Check Due Follow-Ups
```bash
python3 tools/followup-reminder.py check
```
**Shows:** Follow-ups due today
**When:** Daily follow-up check

### List All Follow-Ups
```bash
python3 tools/followup-reminder.py list
```
**Shows:** All scheduled follow-ups
**When:** Overview of follow-up schedule

### Add Follow-Up
```bash
python3 tools/followup-reminder.py add <message-id>
```
**Schedules:** Follow-up for specific message
**When:** Planning follow-up sequence

### Schedule Follow-Ups
```bash
python3 tools/followup-reminder.py schedule
```
**Auto-schedules:** Day 3/7/14 follow-ups for sent messages
**When:** After sending messages

---

## 🔓 UNBLOCK BLOCKERS

### Gateway Restart
```bash
openclaw gateway restart
```
**Unblocks:** $50K bounties (Code4rena)
**Time:** 1 minute
**When:** Browser access needed

### GitHub CLI Auth
```bash
gh auth login
```
**Unblocks:** $125K grants
**Time:** 5 minutes
**When:** Grant submissions blocked

---

## 📖 READ DOCS

### Quick Start
```bash
cat START-HERE.md
```
**Shows:** Master execution index
**When:** First time executing

### Pre-Flight Checklist
```bash
cat PRE-EXECUTION-FLIGHT-CHECK.md
```
**Shows:** 2-minute pre-send checklist
**When:** Before executing

### 15-Minute Checklist
```bash
cat ARTHUR-15-MIN-CHECKLIST.md
```
**Shows:** Step-by-step execution guide
**When:** Ready to send

### Troubleshooting
```bash
cat TROUBLESHOOT-EXECUTION.md
```
**Shows:** Fix for 7 common issues
**When:** Something breaks

---

## 📝 LEAD PRIORITIZATION

### Show Top 5 Leads
```bash
python3 tools/lead-prioritizer.py top 5
```
**Shows:** Highest priority targets
**When:** Planning outreach strategy

### Show Priority Tiers
```bash
python3 tools/lead-prioritizer.py tiers
```
**Shows:** HIGH/MEDIUM/TACTICAL/EXPERT breakdown
**When:** Understanding pipeline structure

---

## 🐛 DEBUG & VERIFY

### Validate Send Scripts
```bash
python3 tools/service-batch-send.py validate outreach/messages/*.md
```
**Checks:** Message format and syntax
**When:** Ensuring messages are valid

### Check Moltbook API
```bash
python3 tools/moltbook-suite.py --check
```
**Shows:** API status and rate limit
**When:** Moltbook posting issues

### Gateway Status
```bash
openclaw gateway status
```
**Shows:** Gateway daemon status
**When:** Connection issues

---

## 🎯 EXECUTE NOW (ONE COMMAND)

**The only command you actually need:**

```bash
bash tools/send-everything.sh full
```

**15-20 minutes later:** $734.5K submitted. Done.

---

## 📞 NEED HELP?

**If stuck:**
1. Read TROUBLESHOOT-EXECUTION.md (7 scenarios, all fixable in <5 min)
2. Run `bash tools/status-check.sh` (diagnostic dashboard)
3. Ask Nova: "Check execution status and diagnose blockers"

**If confused:**
1. Read START-HERE.md (master index)
2. Read ARTHUR-15-MIN-CHECKLIST.md (step-by-step)
3. Read 30-SECOND-STATUS.md (30-second overview)

**If something breaks:**
1. Don't panic. Everything is fixable in <5 minutes.
2. Read TROUBLESHOOT-EXECUTION.md
3. Fix it. Execute. Done.

---

**One page. Everything you need.**

**Execute now:** `bash tools/send-everything.sh full` 🚀
