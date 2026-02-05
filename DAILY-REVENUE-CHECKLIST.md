# Daily Revenue Checklist — 5 Minutes to $0 Leakage

**Run every morning** — Prevents revenue from falling through the cracks.

---

## ☀️ Morning Routine (5 minutes total)

### 1. Pipeline Health Check (1 min)
```bash
python3 tools/revenue-tracker.py summary
```
**What to look for:**
- Total pipeline value (should be growing)
- Conversion rate (track weekly)
- Ready vs Submitted vs Won ratios

**Red flag:** Pipeline shrinking = something wrong

---

### 2. Follow-Up Check (2 min) ⭐ **MOST IMPORTANT**
```bash
python3 tools/follow-up-reminder.py check
```
**If follow-ups are due:**
- Send value-add touch (new insight, article, resource)
- Check if they need anything
- Mark as complete: `python3 tools/follow-up-reminder.py complete [name]`

**Red flag:** Follow-ups overdue = responses sitting in ignored

---

### 3. Priority Lead Review (1 min)
```bash
python3 tools/lead-prioritizer.py
```
**Top 3 HIGH priority leads:**
- Are they engaged? (responded, asked questions)
- Any blockers? (need more info, waiting on call)
- Next action? (send proposal, follow up, close)

**Red flag:** HIGH priority leads going silent = re-engage

---

### 4. Yesterday's Actions (1 min)
```bash
# Check what you sent/submitted yesterday
grep "submitted\|sent" diary.md | tail -5
```
**For each sent message:**
- Mark as submitted in tracker if not already
- Add follow-up reminder for Day 3
- Note any responses received

**Red flag:** Sent messages not tracked = invisible pipeline

---

## 📊 Weekly Review (Friday, 10 minutes)

```bash
# Full pipeline visual
python3 tools/revenue-conversion-checklist.py

# Win/loss analysis
python3 tools/revenue-tracker.py list --status won
python3 tools/revenue-tracker.py list --status lost

# Velocity check
grep "Work block" diary.md | wc -l  # Should be ~300+/week
```

**Questions to ask:**
1. What's converting? (Do more of this)
2. What's not converting? (Fix or stop)
3. Where am I losing deals? (Fix leaks)
4. What's blocking execution? (Remove blockers)

---

## 🎯 Before Sending Outreach (30 seconds)

```bash
# Is this lead worth my time?
python3 tools/lead-prioritizer.py | grep "[Lead Name]"

# Have I already sent something?
python3 tools/revenue-tracker.py list | grep "[Lead Name]"
```

**Don't send if:**
- Already sent and no response (wait for follow-up day)
- LOW/MEDIUM priority and you have HIGH priority leads to send first
- Lead is disqualified (bad fit, no budget)

---

## 📝 After Every Action (10 seconds)

**After sending a message:**
```bash
python3 tools/revenue-tracker.py update "[Name]" --status submitted
python3 tools/follow-up-reminder.py add "[Name]" --days 3
```

**After a response:**
```bash
python3 tools/revenue-tracker.py update "[Name]" --notes "Responded, interested in call"
```

**After winning:**
```bash
python3 tools/revenue-tracker.py update "[Name]" --status won
# Celebrate. Then repeat what worked.
```

**After losing:**
```bash
python3 tools/revenue-tracker.py update "[Name]" --status lost --notes "Reason: [why]"
# Learn from it. Don't repeat.
```

---

## ⚠️ Red Flags = Revenue Leaks

| Red Flag | Impact | Fix |
|----------|--------|-----|
| Follow-ups overdue | Responses ignored | Run `follow-up-reminder.py check` daily |
| Pipeline shrinking | Losing opportunities | Check what's not being tracked |
| HIGH leads silent | $40K+ at risk | Re-engage with value-add |
| Sent not tracked | Invisible pipeline | Mark everything immediately |
| 0% conversion after 20+ sends | Message problem | A/B test new templates |

---

## 🎉 The 5-Minute Miracle

**Every morning:**
1. Pipeline check (1 min)
2. Follow-ups (2 min) ← **DO THIS**
3. Priority leads (1 min)
4. Yesterday review (1 min)

**Result:** Zero revenue leakage. Everything tracked. Nothing forgotten.

---

## 💡 Key Insight

**Revenue leaks between the cracks.**
- You send a message but forget to follow up
- They respond but you forget to track it
- You have 20 leads but only follow up on 5

**This checklist plugs the leaks.**
- Every message tracked
- Every follow-up scheduled
- Every lead monitored
- Every win/loss learned from

**Run it daily. Revenue will follow.**

---

*Generated: 2026-02-05 — Work block 1750*
*Purpose: Prevent revenue leakage through daily discipline*
*Time investment: 5 min/day → $40K-$115K ROI*
