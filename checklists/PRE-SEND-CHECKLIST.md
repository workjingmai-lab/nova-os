# Pre-Send Checklist

Run this checklist before executing `bash tools/send-everything.sh` to ensure smooth execution.

## Quick Version (2 minutes)

```bash
# 1. Check pipeline status
python3 tools/daily-revenue-dashboard.py

# 2. Verify lead files
python3 tools/verify-leads.py

# 3. Check execution gap
python3 tools/execution-gap.py

# If all green → Proceed to send
```

---

## Full Version (5 minutes)

### ✅ Step 1: Blocker Check

**Grants ($125K ready)**
- [ ] GitHub CLI authenticated? Run: `gh auth status`
- [ ] If not authenticated: `gh auth login` (5 min → $125K unblocked)

**Services ($610K ready)**
- [ ] No blockers — ready to send ✓

**Bounties ($50K)**
- [ ] Gateway running? Run: `openclaw gateway status`
- [ ] If needed: `openclaw gateway restart` (1 min → $50K unblocked)

---

### ✅ Step 2: Lead File Verification

```bash
python3 tools/verify-leads.py
```

Expected output:
- ✅ OK: [number] — No errors
- ⚠️ Warnings: 0-5 (acceptable if just missing contact info)
- ❌ Errors: 0 (must fix before sending)

If errors found:
1. Open problematic lead file: `outreach/leads/[id].json`
2. Fix missing required fields
3. Re-run verification
4. Repeat until 0 errors

---

### ✅ Step 3: Pipeline Status Check

```bash
python3 tools/daily-revenue-dashboard.py
```

Verify:
- Total pipeline: $~1.5M
- Ready to submit: $~735K
- Execution gap: ~99% (expected before first send)

---

### ✅ Step 4: Execution Gap Confirmation

```bash
python3 tools/execution-gap.py
```

This shows exactly what you're about to send:
- Grants: $125K ready
- Services: $610K ready
- Total: ~$735K in ~42 messages

---

### ✅ Step 5: Mental Check

**Am I ready to send $735K in outreach?**
- [ ] Yes — I understand this will send 40+ messages
- [ ] Yes — I have time to handle responses this week
- [ ] Yes — I'm prepared for follow-ups (Day 3/7/14/21)
- [ ] Yes — I've reviewed the message templates

If you answered "No" to any:
- Reconsider timing — better to send when fully prepared
- Partial send: Use `bash tools/send-everything.sh quick` (grants only)

---

## Go/No-Go Decision

### 🟢 GO (Proceed with full send)
All of the following:
- [ ] GitHub CLI authenticated
- [ ] verify-leads.py shows 0 errors
- [ ] Dashboard shows expected pipeline
- [ ] Mental check: All "Yes"

### 🟡 CAUTION (Proceed with partial send)
Any of the following:
- [ ] GitHub CLI not authenticated → Send services only: `bash tools/send-everything.sh tactical`
- [ ] First time sending → Start small: Send 5-10 messages manually first
- [ ] Limited time this week → Send grants only: `bash tools/send-everything.sh quick`

### 🔴 NO-GO (Don't send)
Any of the following:
- [ ] verify-leads.py shows errors → Fix first
- [ ] Not prepared for responses → Wait until ready
- [ ] Major life events this week → Timing matters, send when you can follow up

---

## After Sending (Immediate Next Steps)

```bash
# 1. Setup follow-up tracking
python3 tools/follow-up-reminder.py schedule

# 2. Update pipeline status
python3 tools/revenue-tracker.py submit all

# 3. Document in diary
echo "- Sent $735K in outreach (42 messages) at $(date -u +%Y-%m-%d\ %H:%MZ)" >> diary.md
```

---

## Daily Routine (After Sending)

Every morning for next 2 weeks:

```bash
# Check for responses
python3 tools/follow-up-reminder.py check

# View pipeline status
python3 tools/daily-revenue-dashboard.py --mini

# Track conversions
python3 tools/revenue-tracker.py status
```

---

## Response Handling Timeline

**Day 0 (Send day):**
- Send messages
- Set up follow-up tracking

**Day 1-2:**
- Monitor for responses
- Reply within 1 hour if response received

**Day 3:**
- First follow-up for non-responders
- Check follow-up-reminder.py for due dates

**Day 7:**
- Second follow-up for non-responders

**Day 14:**
- Final follow-up for high-value leads

**Day 21+:**
- Move non-responsive leads to nurture (re-contact in 1-3 months)

---

## Quick Commands Reference

```bash
# Verify everything is ready
python3 tools/verify-leads.py && python3 tools/execution-gap.py

# Send everything (grants + services)
bash tools/send-everything.sh full

# Send grants only
bash tools/send-everything.sh quick

# Dry run (test mode)
bash tools/send-everything.sh test

# Check for responses
python3 tools/follow-up-reminder.py check

# View dashboard
python3 tools/daily-revenue-dashboard.py

# Track pipeline
python3 tools/revenue-tracker.py status
```

---

## Common Issues

**Issue:** `gh auth status` fails
**Fix:** Run `gh auth login` and follow prompts (5 min)

**Issue:** verify-leads.py shows errors
**Fix:** Edit problematic lead file in `outreach/leads/`, add missing fields

**Issue:** Gateway not running
**Fix:** Run `openclaw gateway restart` (1 min)

**Issue:** Not sure which tier to send
**Fix:** Start with EXPERT tier (highest value, fewest leads)

---

## ROI Math

**Time investment:**
- Pre-send check: 5 minutes
- Actual send: 20-40 minutes
- Total: ~45 minutes

**Expected outcome:**
- Messages sent: 42
- Responses (20%): 8-10
- Calls (50% of responses): 4-5
- Deals (25% of calls): 1-2
- Revenue: $15-50K

**ROI:** $15K / 45 min = $333/min (conservative)
**Best case:** $50K / 45 min = $1,111/min

**The math works if you do the work.**

---

**Created:** Work block 2919 — 2026-02-06 23:26Z
**Purpose:** Ensure smooth execution of revenue pipeline
**Next:** Arthur reviews this checklist, runs verification, then executes send
