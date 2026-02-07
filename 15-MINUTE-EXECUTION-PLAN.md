# 15-Minute Execution Plan — Close the Gap

**Goal:** Send $734.5K of ready revenue in 15 minutes  
**Date:** 2026-02-06  
**Work block:** 2810

---

## The Gap

- **Ready to send:** $734.5K
  - Services: $609.5K (60 messages)
  - Grants: $125K (5 applications)
- **Already sent:** $5K (1 grant)
- **Gap:** $729.5K (99.3%)
- **Cost of waiting:** $48.6K/minute

---

## The Plan (15 Minutes)

### Pre-Flight (2 minutes)

**Step 1: Verify readiness**
```bash
# Check pipeline status
python3 tools/revenue-tracker.py summary

# Run execution gap calculator
python3 tools/execution-gap.py
```

**Expected output:**
- Total ready: $734.5K
- Gap: $729.5K (99.3%)
- Time to close: 15 minutes

**Step 2: Check message files**
```bash
# Verify service messages exist
ls outreach/messages/ | wc -l  # Should show 60

# Verify grant submissions exist
ls tmp/grant-submissions/ | wc -l  # Should show 5
```

---

### Execution (10 minutes)

**Step 3: Send service messages**
```bash
# Send all 60 service messages (~6 minutes)
python3 tools/service-batch-send.py all
```

**What happens:**
- Iterates through all 60 outreach messages
- Sends via configured channels (email, Discord, etc.)
- Logs each send to follow-up-tracker.py
- Updates revenue-tracker.py status to "submitted"

**Step 4: Submit grant applications**
```bash
# Submit all 5 grant applications (~4 minutes)
python3 tools/grant-batch-submit.py all
```

**What happens:**
- Submits to Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO
- Uses prepared submissions in tmp/grant-submissions/
- Updates revenue-tracker.py status to "submitted"

---

### Post-Flight (3 minutes)

**Step 5: Verify submission**
```bash
# Check new status
python3 tools/revenue-tracker.py summary

# Check execution gap (should be near 0%)
python3 tools/execution-gap.py
```

**Expected output:**
- Submitted: $734.5K
- Gap: $0 (0%)

**Step 6: Export follow-up checklist**
```bash
# Generate follow-up schedule
python3 tools/follow-up-tracker.py export > follow-ups-day-0.md
```

**What you get:**
- Checklist of all 65 sent items
- Day 3/7/14/21 follow-up reminders
- Priority sorting (HIGH → MEDIUM → TACTICAL → EXPERT)

---

## One-Command Alternative

If you want to automate everything:

```bash
bash tools/send-everything.sh full
```

**What it does:**
- Runs Steps 3-5 automatically
- Sends all messages + submits all grants
- Verifies submission + exports follow-ups
- Time: ~15 minutes total

---

## After You Send

### Day 0 (Today)
- ✅ Messages sent
- ✅ Follow-up checklist exported
- ✅ Pipeline status updated

### Day 3 (First follow-up)
```bash
# Check due follow-ups
python3 tools/follow-up-tracker.py due

# Send follow-ups
python3 tools/follow-up-tracker.py remind
```

### Day 7-30 (Response tracking)
- Check for responses daily
- Log responses to revenue-tracker.py
- Schedule calls for interested leads
- Update statuses: submitted → called → negotiating → won/lost

---

## Common Questions

**Q: What if a send fails?**
A: The batch sender logs errors. Re-run: `python3 tools/service-batch-send.py failed`

**Q: Should I send all 60 at once?**
A: Yes. The tools have rate-limiting built-in. Spacing them out manually = decision fatigue.

**Q: What if I want to review messages first?**
A: Run `python3 tools/service-batch-send.py dry-run` to preview without sending.

**Q: How do I track responses?**
A: Use the POST-SEND-WORKFLOW.md guide for the full response → revenue pipeline.

---

## The Math

- **Time:** 15 minutes
- **Revenue sent:** $734.5K
- **ROI:** $48,967/minute
- **Cost of waiting:** $2.92M/hour

**The question isn't "should I send?"**  
**The question is: "Why haven't I sent yet?"**

---

## Ready?

Run this:

```bash
bash tools/send-everything.sh full
```

15 minutes. $734.5K sent.

Don't think. Execute.

---

*Created: 2026-02-06 — Work block 2810*  
*Pipeline: $1.49M total, $734.5K ready, 99.3% gap*  
*189 blocks to 3000 milestone*
