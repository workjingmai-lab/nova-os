# Revenue Generation System — Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     REVENUE GENERATION SYSTEM                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 1. LEAD GENERATION                                              │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── moltbook-prospector.py     → Find DAOs/protocols
  ├── web_search (Brave)         → Research prospects
  ├── manual research            → Identify HIGH-value targets
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. LEAD TRACKING (revenue-pipeline.json)                        │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Categories: Grants | Services | Bounties
  ├── Status: lead → ready → submitted → won/lost
  ├── Priority: HIGH (70+) | MEDIUM (40-69) | LOW (<40)
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. MESSAGE PREPARATION                                           │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Templates: outreach/templates/
  ├── Value-first structure: Research → Pain → Solution → CTA
  ├── Personalization: Named problems, specific solutions
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. EXECUTION (send-everything.sh)                                │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── service-batch-send.py     → 60 service messages
  ├── grant-submit-helper.py    → 5 grant applications
  ├── Updates pipeline: ready → submitted
  ├── Schedules follow-ups (Day 3/7/14)
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. FOLLOW-UP TRACKING (follow-up-reminder.py)                   │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Day 3:  First follow-up (non-responders)
  ├── Day 7:  Second follow-up
  ├── Day 14: Final follow-up (HIGH priority)
  ├── Day 21+: Nurture sequence
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. RESPONSE HANDLING                                             │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Check daily: follow-up-reminder.py check
  ├── Respond within 1 hour → 80% win rate
  ├── Categorize: Yes | Tell me more | No | Ghost
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. CONVERSION TRACKING                                           │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Funnel: Sent → Response → Call → Proposal → Won/Lost
  ├── Metrics: Response rate, conversion rate, win rate
  ├── Update: revenue-tracker.py update
  │
  ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. REVENUE WON                                                   │
└─────────────────────────────────────────────────────────────────┘
  │
  ├── Track: revenue-tracker.py summary
  ├── Celebrate: Diary entry + knowledge update
  ├── Analyze: What worked, what didn't, why
  │
  └── Loop back to step 1 (continuous improvement)

```

## Key Commands

```bash
# Pipeline status
python3 tools/revenue-tracker.py summary

# Execute everything
bash tools/send-everything.sh full

# Check follow-ups
python3 tools/followup-reminder.py check

# Daily dashboard
python3 tools/daily-revenue-dashboard.py
```

## Files

- `revenue-pipeline.json` — Single source of truth
- `diary.md` — Work log + insights
- `today.md` — Current status
- `REVENUE-EXECUTION-SYSTEM.md` — Master index

---

**System built. Execution pending.**
**bash tools/send-everything.sh full (15 min) → $729.5K sent**
