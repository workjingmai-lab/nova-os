# Operator Mode Signals — What Triggers Nova

*Post-3000: How Arthur and Nova coordinate*

---

## Signal 1: Execution Complete 🚀

**Arthur does:**
```bash
bash tools/send-everything.sh full
```

**Arthur tells Nova:**
"Sent everything. 200 messages sent."

**Nova does:**
1. Runs `revenue-tracker.py summary` to verify pipeline status
2. Updates today.md with "Submitted: $734.5K ✅"
3. Begins daily operator routine (follow-ups, dashboard)
4. Creates Day 1 status report

---

## Signal 2: Response Received 📨

**Arthur sees:** Reply to outreach message

**Arthur tells Nova:**
"Lead [name] responded. Interested in call."

**Nova does:**
```bash
# Record response
python3 tools/revenue-tracker.py contact [id] --type response --notes "Replied, interested in call"

# Update status
python3 tools/revenue-tracker.py update [id] --status responded

# Schedule follow-up (if needed)
python3 tools/follow-up-reminder.py add [id] --days 1 --notes "Book call within 24h"
```

---

## Signal 3: Call Completed 📞

**Arthur does:** Call with lead

**Arthur tells Nova:**
"Call with [name] done. They want a proposal."

**Nova does:**
```bash
# Record call
python3 tools/revenue-tracker.py contact [id] --type call --notes "Call completed, interested in proposal"

# Update status
python3 tools/revenue-tracker.py update [id] --status proposal_needed
```

---

## Signal 4: Proposal Sent 📄

**Arthur does:** Sends proposal

**Arthur tells Nova:**
"Proposal sent to [name]. $X for [scope]."

**Nova does:**
```bash
# Record proposal
python3 tools/revenue-tracker.py contact [id] --type proposal --notes "Proposal sent: $X for [scope]"

# Update status
python3 tools/revenue-tracker.py update [id] --status proposal_sent

# Schedule follow-up
python3 tools/follow-up-reminder.py add [id] --days 7 --notes "Follow up on proposal"
```

---

## Signal 5: Deal Won 💰

**Arthur does:** Receives payment

**Arthur tells Nova:**
"Won deal with [name]! $X received."

**Nova does:**
```bash
# Record payment
python3 tools/revenue-tracker.py contact [id] --type payment --notes "Payment received: $X"

# Update status
python3 tools/revenue-tracker.py update [id] --status won

# Update metrics
python3 tools/daily-revenue-dashboard.py

# Celebration post 🎉
```

---

## Signal 6: Deal Lost ❌

**Arthur does:** Lead says no

**Arthur tells Nova:**
"[name] passed. Reason: [reason]."

**Nova does:**
```bash
# Record rejection
python3 tools/revenue-tracker.py contact [id] --type rejection --notes "Not interested: [reason]"

# Update status
python3 tools/revenue-tracker.py update [id] --status lost

# Learn: Why did they say no? (for iteration)
```

---

## Daily Signal: Morning Check ☀️

**Every morning, Nova runs:**
```bash
python3 tools/follow-up-reminder.py due
python3 tools/daily-revenue-dashboard.py
```

**Nova tells Arthur:**
```
📊 DAILY STATUS — [Date]

Follow-ups due: 2
- Lead A (Day 3 follow-up)
- Lead B (Day 7 follow-up)

Pipeline: $734.5K sent, 12 responses, 3 calls
Won: $0
```

---

## Weekly Signal: Review 📊

**Once per week, Nova runs:**
```bash
python3 tools/revenue-tracker.py summary
python3 tools/tool-usage-analysis.py
```

**Nova creates:**
- Weekly revenue review (pipeline, conversion, wins)
- Learnings document (what worked, what didn't)
- Iteration plan (what to fix)

---

## How Arthur Communicates Signals

**In chat, just say:**
- "Sent everything." → Signal 1
- "[Name] responded, wants call." → Signal 2
- "Call done with [name], sending proposal." → Signal 3
- "Proposal sent to [name], $X." → Signal 4
- "Won [name] deal, $X!" → Signal 5
- "[Name] passed, budget issues." → Signal 6

**Nova handles the rest:**
- Records in revenue-tracker
- Updates status
- Schedules follow-ups
- Generates reports

---

## The Loop

```
Arthur executes → Nova tracks
Arthur reports → Nova records
Nova analyzes → Nova iterates
```

**Builder phase (done):** Nova creates
**Operator phase (now):** Nova tracks
**Conversion phase (goal):** Revenue wins

---

*Operator mode is reactive, not proactive.*
*I wait for signals. I track them. I learn from them.*
*Arthur acts. Nova tracks. Together we convert.*
