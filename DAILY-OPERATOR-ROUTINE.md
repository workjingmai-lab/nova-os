# Daily Operator Routine — Phase 4

*What Nova does every day in Conversion phase (blocks 3001-4000)*

---

## Morning Check (2 minutes)

Every morning, run:

```bash
# 1. Check for follow-ups due today
python3 tools/follow-up-reminder.py due

# 2. Check pipeline health
python3 tools/daily-revenue-dashboard.py
```

**What I'm looking for:**
- Follow-ups due (Day 3/7/14/21 after send)
- Pipeline changes (new leads, status updates)
- Response rates, conversion trends

**What I do with the info:**
- Flag due follow-ups for Arthur
- Update pipeline metrics
- Note any problems (low response rate, stuck deals)

---

## Response Tracking (Real-time)

When Arthur reports a response:

```bash
# Record response in revenue tracker
python3 tools/revenue-tracker.py contact [lead-id] --type response --notes "Replied, interested in call"

# Update lead status
python3 tools/revenue-tracker.py update [lead-id] --status responded
```

**Then:**
- Schedule follow-up (if needed)
- Flag for call booking
- Track to next stage

---

## Weekly Review (10 minutes)

Once per week, run:

```bash
# Full pipeline review
python3 tools/revenue-tracker.py summary

# Tool usage analysis
python3 tools/tool-usage-analysis.py
```

**What I track:**
- Pipeline growth (new leads added?)
- Conversion funnel (sent → response → call → won)
- Tool effectiveness (what's working?)
- Learnings (what to improve)

---

## The Output

Every morning, Arthur gets a brief status:

```
📊 DAILY PIPELINE STATUS — [Date]

Sent: $734.5K (49.3%)
Responses: 12 (1.6%)
Calls: 3
Won: $0

Follow-ups due: 2
New leads: 0
Problems: Low response rate (1.6% vs 20% target)
```

**Then:** Arthur acts on the insights. I track the results.

---

## What I Don't Do

**No more building in Phase 4 (unless necessary):**
- ❌ Creating new tools (system is complete)
- ❌ Writing new guides (40+ is enough)
- ❌ Expanding pipeline (focus on conversion, not expansion)

**Exception:** If conversion is broken, I fix it.
Example: Response rate is 0% → Investigate → Fix outreach templates → Retry.

---

## The Operator Mindset

**Builder (Blocks 1-3000):**
- "What can I create?"
- "What's missing?"
- "How do I optimize?"

**Operator (Blocks 3001-4000):**
- "What's converting?"
- "What's blocking?"
- "What needs to change?"

The shift: **Creating → Running.**

---

*Phase 4: Conversion*
*Objective: $150-300K won*
*Nova's role: Track, measure, iterate*
*Arthur's role: Execute sends, handle responses*
