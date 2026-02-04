# Quick Reference — Nova's 1-Minute Commands

**For:** Arthur
**Purpose:** Execute common Nova tasks without reading 50 READMEs
**Last Updated:** 2026-02-04

---

## 🔥 Critical Unblocks (Do These First!)

### Gateway Restart (1 min → $50K unblocked)
```bash
openclaw gateway restart
```
**Why:** Unblocks browser automation → Code4rena bounties ($50K)
**Time:** ~1 minute
**Frequency:** As needed (when browser automation breaks)

### GitHub CLI Auth (5 min → $130K unblocked)
```bash
gh auth login
```
**Why:** Unblocks 5 grant submissions ($130K total)
**Time:** ~5 minutes
**Follow prompts:** Paste token → done
**Frequency:** Once per machine

---

## 📊 Nova Status Checks

### Quick Status (5 seconds)
```bash
python3 tools/nova-status.py
```
**Shows:** Work blocks, velocity, streak, latest diary entries

### Revenue Pipeline (5 seconds)
```bash
python3 tools/revenue-tracker.py
```
**Shows:** $302K pipeline (grants $130K, services $122K, bounties $50K)

### Blocker Status (5 seconds)
```bash
python3 tools/blocker-status.py
```
**Shows:** Current blockers, ROI, time to fix

---

## 🚀 Nova Execution

### Trigger Work Block (Nova picks a task)
```bash
echo "WORK BLOCK: Execute 1 task from goals/active.md or today.md" > /tmp/nova-trigger
```
**What happens:** Nova reads goals/today, picks ONE task, executes, documents to diary.md

### Trigger Deep Think (90-min focused session)
```bash
echo "DEEP THINK: Run workspace/heartbeat.md checklist" > /tmp/nova-deep-think
```
**What happens:** Nova starts isolated session, runs checklist, generates insights

---

## 📝 Content & Publishing

### Moltbook Status
```bash
python3 tools/moltbook-suite.py status
```
**Shows:** Queued posts, API status, tracked agents

### Moltbook Publish (Next Queued)
```bash
python3 tools/moltbook-suite.py post --next
```
**Note:** If rate limited (HTTP 429), wait 30 min before retry

---

## 🔧 Tool Management

### List All Tools
```bash
ls -1 tools/*.py | wc -l           # Count
ls -lt tools/*.py | head -10       # Recent
```

### Find Tool by Keyword
```bash
grep -r "revenue" tools/*.py       # Find revenue tools
grep -r "moltbook" tools/*.py      # Find Moltbook tools
```

### Run Tool with Help
```bash
python3 tools/TOOL_NAME.py --help  # Show usage
```

---

## 📖 Memory & Documentation

### Read Today's Progress
```bash
cat today.md                       # Working memory + latest blocks
```

### Read Long-Term Memory
```bash
cat MEMORY.md                      # Curated memories (main session only)
```

### Search Knowledge Base
```bash
grep -r "KEYWORD" knowledge/*.md   # Find knowledge articles
```

---

## 🎯 Goal Tracking

### Week 2 Progress
```bash
cat goals/week-2.md                # Week 2 objectives + progress
```

### Active Goals
```bash
cat goals/active.md                # Current high-priority goals
```

### Today's Goal
```bash
head -20 today.md                  # Top of today.md = 1-line goal
```

---

## 📊 Analytics & Insights

### Work Block Velocity
```bash
python3 tools/daily-output-tracker.py
```
**Shows:** Tasks/hour, blocks completed, trends

### Tool Usage Patterns
```bash
python3 tools/tool-usage-pattern-analyzer.py
```
**Shows:** Most-used tools, consolidation opportunities

### Self-Improvement Loop
```bash
python3 tools/self-improvement-loop.py
```
**Shows:** Metrics, insights, recommendations, predictions

---

## 🔄 Cron Jobs & Automation

### List Cron Jobs
```bash
openclaw cron list
```

### Wake Nova (Immediate Heartbeat)
```bash
openclaw cron wake --mode now
```

### Add Reminder (System Event)
```bash
openclaw cron add --job '{
  "name": "Reminder: Check grant status",
  "schedule": {"kind": "cron", "expr": "0 9 * * *"},
  "payload": {"kind": "systemEvent", "text": "Reminder: Check grant submission status"},
  "sessionTarget": "main"
}'
```

---

## 🛠️ Troubleshooting

### Nova Not Responding?
1. Check status: `openclaw status`
2. Check logs: `openclaw gateway status`
3. Restart gateway: `openclaw gateway restart` (last resort)

### Browser Automation Broken?
```bash
openclaw gateway restart
```
**Why:** Fixes browser proxy issues, unblocks Code4rena

### Moltbook API Timeout?
**Wait 30 min** — Rate limited (HTTP 429), queue auto-retries

### Tools Not Found?
```bash
pwd                               # Must be in workspace
cd /home/node/.openclaw/workspace
```

---

## 📞 Contact Nova

### In This Session (Chat)
Just type:
- "Nova, run a work block"
- "Nova, give me a status update"
- "Nova, what's in the pipeline?"

### Cross-Session (via OpenClaw)
```bash
openclaw sessions send --session "main" --message "YOUR MESSAGE"
```

---

## 🎓 Learn More

### Nova's Toolkit
```bash
cat toolkit.md                     # All tools, one file
```

### Knowledge Base
```bash
cat knowledge/INDEX.md             # 43+ articles on methodology
```

### Recent Work
```bash
tail -50 diary.md                  # Latest work blocks
```

---

*Created: Work Block 1479*
*For: Arthur (quick reference, no deep reading required)*
