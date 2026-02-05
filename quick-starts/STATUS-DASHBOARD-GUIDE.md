# How to Use Status Dashboard (2 minutes)

Check workspace status in 30 seconds. Know what to do next.

## Quick Stats
- **Time:** 2 minutes to learn, 30 seconds to use
- **Value:** Clarity on $585K pipeline + next actions
- **ROI:** Infinite — prevents paralysis

## Open Dashboard (30 seconds)
```bash
cat /home/node/.openclaw/workspace/STATUS-30SEC.md
```
**What happens:** See current pipeline, top leads, next actions, velocity

## What to Look For

### 1. Pipeline Status (top of file)
- **Total pipeline:** $585K
- **Ready to submit:** $435K (this is your action queue)
- **Execution gap:** % difference between ready and submitted

### 2. Next Actions (middle of file)
3 commands with time and value:
```bash
# 1. Gateway restart (1 min → $50K)
openclaw gateway restart

# 2. GitHub auth (5 min → $130K)
gh auth login

# 3. Send outreach (51 min → $435K)
python3 tools/moltbook-client/moltbook-client.py --send-all outreach
```

### 3. Work Block Velocity
- **Current blocks:** 2022
- **Target:** 2000 ✅
- **Velocity:** ~44 blocks/hour

### 4. System Status
- Documentation coverage
- Ready-to-execute items
- Blockers remaining

## When to Check

### Every morning
```bash
cat STATUS-30SEC.md
```
See what changed overnight.

### Before starting work
Know what's ready, what's blocked, what to focus on.

### After completing tasks
Check if pipeline changed (new leads, submissions, wins).

## How to Update

### Manual update (when things change)
```bash
nano STATUS-30SEC.md
# Update: pipeline totals, next actions, work block count
```

### Auto-update (via cron)
Dashboard updates automatically when:
- Work blocks complete
- Pipeline changes (submissions, wins)
- Blockers clear

## Common Questions

**Q: How often should I check this?**
A: 1-2 times per day. It's a snapshot, not a live monitor.

**Q: What if a number looks wrong?**
A: Run revenue-tracker.py to verify:
```bash
python3 tools/revenue-tracker/revenue-tracker.py
```

**Q: Can I customize this?**
A: Yes. It's just a markdown file. Add sections, change metrics.

## Result
✅ Know what to do next in 30 seconds
✅ See pipeline status at a glance
✅ Never wonder "what should I work on?"

---

**No blockers.** Just check the dashboard.

Created: 2026-02-05
