# Follow-Up Workflow Guide

Automated follow-up detection and execution for revenue pipeline.

## Problem
Pipeline leakage happens because:
1. You send outreach → forget to follow up
2. No system to track "when to contact next"
3. Manual tracking doesn't scale

## Solution
Two tools working together:
1. **revenue-tracker.py** — Track all pipeline items
2. **follow-up-reminder.py** — Auto-detect follow-ups needed

## Daily Workflow (30 seconds)

### 1. Check for follow-ups
```bash
python3 follow-up-reminder.py
```

Output shows:
- Items needing follow-up (grouped by priority)
- Days since last contact
- Suggested template

### 2. Send follow-up
Use template from `outreach/followup-timing-quickref.md`:
- **Value-add** (day 3/7) — New insight, article, case study
- **Check-in** (day 14) — "Any thoughts on my previous note?"
- **Close-out** (day 30+) — Permission to close

### 3. Update tracker
```bash
# After sending follow-up
python3 revenue-tracker.py update --id <id> --followed-up <timestamp>
```

## Timing Schedule

### Services (B2B automation)
- Day 0: Initial outreach
- Day 3: Value-add follow-up
- Day 7: Value-add follow-up
- Day 14: Check-in
- Day 30: Close-out

### Grants (DAO/governance)
- Week 0: Initial submission
- Week 2: Status check
- Week 4: Value-add (show progress)
- Week 8: Final check

### Bounties (Code4rena, etc.)
- Day 0: Submission
- Day 7: Check status
- Day 14: Final follow-up

## Templates

### Value-Add Example
```
Subject: Quick update on <project>

Hi <name>,

Following up on my note about <service>. Since we last spoke, I:

→ Built <new thing> (saves X hours/week)
→ Published <article> on <topic>
→ Helped <similar company> achieve <result>

Thought you might find this useful.

Still interested in exploring how I can help with <pain>?

Best,
Nova
```

### Check-In Example
```
Subject: Any thoughts on <project>?

Hi <name>,

Checking in on my note from <date> about <service>.

Did you have a chance to review? Any questions I can answer?

No pressure — if now isn't the right time, just let me know.

Best,
Nova
```

## Integration with Heartbeat

Add to HEARTBEAT.md:
```markdown
- name: "Follow-Up Check"
  every: "daily"
  message: |
    Run follow-up-reminder.py. If HIGH priority follow-ups needed,
    ping Arthur with summary. Otherwise log to diary.md and continue.
```

## Metrics to Track

- Response rate by follow-up number
- Conversion rate by touch count
- Average touches before conversion

Target: 80% of conversions happen on touch #2-3.

## Commands Reference

```bash
# Check follow-ups
python3 follow-up-reminder.py

# View full pipeline
python3 revenue-tracker.py summary

# Update after follow-up
python3 revenue-tracker.py update --id <id> --followed-up $(date +%s)

# Track new submission
python3 revenue-tracker.py add --type service --value 25000 --org "Acme Corp"
```

## Key Insight

"If you believe in your offer, follow up. If you don't, why did you send it?"

80% of revenue comes from follow-ups, not initial outreach.
