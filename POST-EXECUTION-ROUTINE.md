# Post-Execution Routine — After Sending Everything

**Purpose:** Daily follow-up routine to maximize conversion
**When:** After running `bash tools/send-everything.sh full`
**Cadence:** Daily 5-minute check + weekly review
**Value:** 80% win rate if responding within 1 hour

---

## 📅 Daily Follow-Up Routine (5 minutes)

### Step 1: Check for Follow-Ups Due
```bash
python3 tools/follow-up-reminder.py check
```

**What it shows:**
- Follow-ups due today (Day 3, 7, 14, 21)
- Overdue follow-ups (if any)
- Response reminders

**Action:** Send follow-up messages to non-responsive leads

---

### Step 2: Check Dashboard
```bash
python3 tools/daily-revenue-dashboard.py
```

**What it shows:**
- Funnel metrics (Sent → Response → Call → Won/Lost)
- Conversion rates
- Pipeline health

**Action:** Identify stuck leads, adjust strategy

---

### Step 3: Respond to New Messages (Within 1 Hour)

**Golden rule:** Respond to all new messages within 1 hour for 80% win rate.

**Response types:**
- **Interested:** Schedule call immediately
- **Questions:** Answer, propose call
- **Not interested:** Ask for referral, polite close
- **No response:** Mark for follow-up (Day 3, 7, 14)

---

## 📊 Follow-Up Timeline

### Day 1-3: Initial Response Window
- **Expected:** 30-50% response rate (20-32 responses)
- **Action:** Respond immediately, schedule calls
- **Tool:** `python3 tools/follow-up-reminder.py check`

### Day 3: First Follow-Up
- **Target:** Non-responsive leads
- **Message:** "Hi [Name], just wanted to make sure you saw my previous message..."
- **Tool:** Auto-scheduled by follow-up-reminder.py

### Day 7: Second Follow-Up
- **Target:** Still no response
- **Message:** Different angle, new value prop
- **Tool:** Auto-scheduled by follow-up-reminder.py

### Day 14: Third Follow-Up
- **Target:** Long-term pipeline
- **Message:** "Any updates?" or share new content
- **Tool:** Auto-scheduled by follow-up-reminder.py

### Day 21: Final Follow-Up
- **Target:** Last chance
- **Message:** "Closing the loop..." or polite goodbye
- **Tool:** Auto-scheduled by follow-up-reminder.py

---

## 🎯 Response Handling Framework

### Interested ("Yes, that's me!")
**Response:**
```
Thanks [Name]! Great to hear you're interested.

When works for a 15-min call to discuss how we can help [specific pain]?

I'm free [time 1], [time 2], [time 3] EST.

Best,
[Your name]
```
**Action:** Schedule call, prepare proposal

### Questions ("Tell me more...")
**Response:**
```
Great question [Name]!

[Answer question in 1-2 sentences]

Happy to walk through the details on a call. When works?

Best,
[Your name]
```
**Action:** Answer → Propose call

### Not Interested ("Not a fit right now")
**Response:**
```
Thanks for getting back to me [Name]!

Do you know anyone else at [company] who might be interested? Or any other teams I should reach out to?

Appreciate the help!

Best,
[Your name]
```
**Action:** Ask for referral, polite close

---

## 📈 Weekly Review (10 minutes)

### Step 1: Full Pipeline Check
```bash
python3 tools/revenue-tracker.py summary
```

**Track:**
- Total sent vs. new responses
- Calls booked vs. completed
- Deals won vs. lost
- Conversion rate by week

### Step 2: Conversion Metrics
```bash
python3 tools/conversion-pulse.py
```

**Benchmarks:**
- Response rate: 10-20% (good), 20-30% (excellent)
- Call rate: 30-50% of responses
- Win rate: 20-40% of calls

### Step 3: Weekly Summary
**Document:**
- What worked this week
- What didn't work
- Adjustments for next week
- Top 5 leads to focus on

---

## 🚀 Key Success Factors

1. **Speed matters:** Respond within 1 hour
2. **Consistency:** Daily 5-minute check
3. **Follow-up sequence:** Day 3, 7, 14, 21
4. **Track everything:** Update pipeline after every interaction
5. **Iterate:** Adjust messaging based on response rates

---

## ⚡ Quick Commands

**Daily check:**
```bash
python3 tools/follow-up-reminder.py check
```

**Dashboard:**
```bash
python3 tools/daily-revenue-dashboard.py
```

**Full review:**
```bash
python3 tools/revenue-tracker.py summary
```

---

*Created: 2026-02-07 (Work block 3054)*
*Part of Arthur Guide Consolidation Plan*
*Status: Active*
