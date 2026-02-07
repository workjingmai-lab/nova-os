# Daily Revenue Execution Checklist
# For: Arthur (or whoever executes)
# Created: Work block 3065, 2026-02-07
# Purpose: Zero-thinking daily revenue routine

## Pre-Flight (30 seconds)

```bash
# Check current status
python3 tools/conversion-dashboard.py
```

**Look for:**
- [ ] Execution gap % (target: < 50%)
- [ ] Items ready to send count
- [ ] Top 5 opportunities (highest value first)

---

## Block 1: Unblock Critical Paths (5-10 min)

### If not done yet:

**GitHub Auth** (5 min → $125K grants)
```bash
gh auth login
# Follow browser flow
```

**Gateway Restart** (1 min → $50K bounties)
```bash
# Ask Nova to restart gateway for browser access
# Enables Code4rena, web submissions
```

---

## Block 2: Send Service Messages (15-30 min)

### Quick Method:
```bash
# View ready messages
ls outreach/ready-to-send/

# Send top 5 (highest value first)
# Use knowledge/response-decision-playbook.md for any replies
```

### Target: 5-10 messages/day
- Focus on HIGH priority first ($40K+ opportunities)
- Then MEDIUM ($15K+)
- Skip LOW unless time permits

### After each send:
```bash
# Update status
python3 tools/revenue-tracker.py update "Lead Name" submitted
```

---

## Block 3: Grant Submissions (15-30 min)

### If GitHub auth complete:
```bash
# View ready grants
python3 tools/revenue-tracker.py list grants

# Submit to 1-2 platforms
# Use templates in tmp/grant-submissions/
```

### Current ready ($125K):
1. Olas ($50K)
2. Optimism RPGF ($50K)
3. Octant ($15K)
4. Moloch DAO ($10K)

---

## Block 4: Follow-Up Management (5-10 min)

### Check for responses:
```bash
# View leads needing follow-up
python3 tools/follow-up-reminder.py

# Record any responses
python3 tools/template-tracker.py record "Lead" <template_id>
python3 tools/template-tracker.py response "Lead" yes "Outcome"
```

### Response workflow:
1. Read response
2. Categorize (positive/neutral/negative)
3. Pick template from knowledge/follow-up-templates.md
4. Send reply
5. Record in tracker
6. Update revenue-tracker.py status

---

## Block 5: End-of-Day (2 min)

```bash
# Final status check
python3 tools/conversion-dashboard.py

# Document what was sent
echo "$(date): Sent X messages, Y grants" >> memory/daily-log.md
```

**Update MEMORY.md:**
- Wins (even small)
- Blockers encountered
- Lessons learned

---

## Time Budget

| Block | Time | Value Unlocked |
|-------|------|----------------|
| Unblock | 6 min | $180K (grants + bounties) |
| Services | 20 min | $200K+ (depends on sends) |
| Grants | 15 min | $125K |
| Follow-up | 10 min | Variable |
| **Total** | **~51 min** | **$500K+ potential** |

---

## Quick Reference Commands

```bash
# Dashboard
python3 tools/conversion-dashboard.py

# Revenue tracker
python3 tools/revenue-tracker.py summary
python3 tools/revenue-tracker.py list services
python3 tools/revenue-tracker.py update "Name" submitted

# Template tracking
python3 tools/template-tracker.py
python3 tools/template-tracker.py record "Lead" 5

# Follow-ups
python3 tools/follow-up-reminder.py

# Execution gap
python3 tools/execution-gap.py
```

---

## Success Metrics

**Daily targets:**
- [ ] 5+ service messages sent
- [ ] 1-2 grant submissions
- [ ] All responses handled (within 2-4 hours)
- [ ] 0 execution gap growth (don't let it expand)

**Weekly targets:**
- [ ] Execution gap < 50% (from 99.7%)
- [ ] 3+ conversations started (responses)
- [ ] 1+ calls scheduled
- [ ] 1+ deal closed (even small)

---

## If Stuck

**Don't know what to send?**
→ Check `knowledge/follow-up-templates.md`

**Don't know who to prioritize?**
→ Run `python3 tools/conversion-dashboard.py`, pick top 5

**Got a weird response?**
→ Check `knowledge/response-decision-playbook.md`

**Need to track something?**
→ Use `python3 tools/template-tracker.py`

---

## Emergency Mode (Only 5 Minutes)

If you only have 5 minutes:
1. `python3 tools/conversion-dashboard.py` (30 sec)
2. Send 1 high-value message from outreach/ready-to-send/ (3 min)
3. Update status in revenue-tracker.py (30 sec)
4. Log it (1 min)

**Done is better than perfect.**

---

*Created: Work block 3065*
*Purpose: Remove all friction from daily execution*
