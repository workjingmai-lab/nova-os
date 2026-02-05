# Quick Revenue Commands — Feb 5, 2026

## Pipeline Status Commands

### Check overall pipeline
```bash
python3 tools/revenue-tracker.py summary
```

### List all ready leads
```bash
python3 tools/revenue-tracker.py list --status ready
```

### List HIGH priority leads
```bash
python3 tools/lead-prioritizer.py --filter HIGH
```

### List MEDIUM priority leads
```bash
python3 tools/lead-prioritizer.py --filter MEDIUM
```

### Check conversion rates
```bash
python3 tools/revenue-tracker.py conversion
```

---

## Sending Messages Commands

### View message template
```bash
cat outreach/messages/<name>-automation.md
```

### List all message templates
```bash
ls -la outreach/messages/
```

### Find specific message
```bash
ls outreach/messages/ | grep -i <keyword>
# Examples:
ls outreach/messages/ | grep -i ethereum
ls outreach/messages/ | grep -i uniswap
```

---

## After Sending Commands

### Mark lead as submitted
```bash
python3 tools/revenue-tracker.py update <name> --status submitted
# Examples:
python3 tools/revenue-tracker.py update ethereum-foundation --status submitted
python3 tools/revenue-tracker.py update uniswap --status submitted
```

### Mark lead as won
```bash
python3 tools/revenue-tracker.py update <name> --status won --value <amount>
# Example:
python3 tools/revenue-tracker.py update ethereum-foundation --status won --value 40000
```

### Mark lead as lost
```bash
python3 tools/revenue-tracker.py update <name> --status lost --notes "<reason>"
# Example:
python3 tools/revenue-tracker.py update ethereum-foundation --status lost --notes "No response after 3 follow-ups"
```

---

## Follow-up Commands

### Check follow-ups due
```bash
python3 tools/follow-up-reminder.py
```

### Get follow-up timing reference
```bash
cat tools/followup-timing-quickref.md
```

### View follow-up schedule (top 3)
```bash
cat outreach/TOP-3-FOLLOW-UP-SCHEDULE.md
```

---

## Analysis Commands

### View pipeline snapshot
```bash
cat analysis/services-pipeline-snapshot.md
```

### View pipeline math
```bash
cat knowledge/services-pipeline-math.md
```

### View top 5 HIGH priority
```bash
cat outreach/TOP-5-HIGH-PRIORITY-QUICK-REF.md
```

### View 26 messages checklist
```bash
cat outreach/26-MESSAGES-EXECUTION-CHECKLIST.md
```

---

## Revenue Metrics Commands

### Check total pipeline value
```bash
python3 tools/revenue-tracker.py summary | grep "TOTAL PIPELINE"
```

### Check conversion rate
```bash
python3 tools/revenue-tracker.py summary | grep "Conversion"
```

### Check services ready
```bash
python3 tools/revenue-tracker.py summary | grep "Ready to submit" -A 1
```

---

## Data Commands

### View raw pipeline JSON
```bash
cat data/revenue-pipeline.json | jq '.services[] | select(.status == "ready")'
```

### Count ready leads
```bash
cat data/revenue-pipeline.json | jq '[.services[] | select(.status == "ready")] | length'
```

### Sum ready value
```bash
cat data/revenue-pipeline.json | jq '[.services[] | select(.status == "ready") | .potential] | add'
```

---

## Quick Workflows

### Workflow 1: Send 3 HIGH Priority (15 min → $115K)
```bash
# Step 1: View messages
cat outreach/messages/ethereum-foundation-agent-automation.md
cat outreach/messages/uniswap-devx-automation.md
cat outreach/messages/fireblocks-security-automation.md

# Step 2: Send messages (manual - Discord/Email/Twitter)

# Step 3: Mark as submitted
python3 tools/revenue-tracker.py update ethereum-foundation --status submitted
python3 tools/revenue-tracker.py update uniswap --status submitted
python3 tools/revenue-tracker.py update fireblocks --status submitted

# Step 4: Verify
python3 tools/revenue-tracker.py summary
```

### Workflow 2: Check Follow-ups (5 min)
```bash
# Step 1: Check what's due
python3 tools/follow-up-reminder.py

# Step 2: Send follow-ups (manual)

# Step 3: Update notes
python3 tools/revenue-tracker.py update <name> --notes "Follow-up sent 2026-02-08"
```

### Workflow 3: Daily Revenue Check (10 min)
```bash
# Step 1: Check pipeline
python3 tools/revenue-tracker.py summary

# Step 2: Check follow-ups
python3 tools/follow-up-reminder.py

# Step 3: Update any new submissions
python3 tools/revenue-tracker.py update <name> --status submitted

# Step 4: Verify
python3 tools/revenue-tracker.py summary
```

---

## Reference Files

| File | Purpose |
|------|---------|
| `outreach/26-MESSAGES-EXECUTION-CHECKLIST.md` | Full sending guide |
| `outreach/TOP-5-HIGH-PRIORITY-QUICK-REF.md` | Top 5 deals |
| `analysis/services-pipeline-snapshot.md` | Pipeline breakdown |
| `knowledge/services-pipeline-math.md` | Conversion math |
| `outreach/TOP-3-FOLLOW-UP-SCHEDULE.md` | Follow-up schedule |
| `tools/followup-timing-quickref.md` | Follow-up timing |
| `data/revenue-pipeline.json` | Raw pipeline data |

---

## Common Patterns

### Pattern 1: "Did I send X yet?"
```bash
# Check status
python3 tools/revenue-tracker.py list | grep -i <name>

# Or check JSON
cat data/revenue-pipeline.json | jq '.services[] | select(.name | contains("<NAME>"))'
```

### Pattern 2: "What's my pipeline value?"
```bash
# Quick summary
python3 tools/revenue-tracker.py summary

# Services only
python3 tools/revenue-tracker.py summary | grep -A 3 "SERVICES"
```

### Pattern 3: "Who should I follow up with?"
```bash
# Check due follow-ups
python3 tools/follow-up-reminder.py

# Manual check
cat data/revenue-pipeline.json | jq '.services[] | select(.status == "submitted") | {name, submitted_date}'
```

---

## Tips

1. **Use tab completion** for command efficiency
2. **Create aliases** for frequently used commands
3. **Set reminders** for follow-up dates (Day 3/7/14/21)
4. **Update immediately** after sending (don't batch)
5. **Verify with summary** after bulk updates

---

*Created: 2026-02-05 04:30 UTC*
*Purpose: Single-page command reference for revenue workflow*
*Related: 26-MESSAGES-EXECUTION-CHECKLIST.md*
