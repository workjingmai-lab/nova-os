# Quick Commands (30-Second Reference)
*For Arthur — Nova's Operator*

## Pipeline Status
```bash
# See current revenue pipeline
python3 tools/revenue-tracker.py summary
```

## Moltbook Posts
```bash
# Publish next queued post
python3 tools/moltbook-suite.py post --next

# Check rate limit status
python3 tools/moltbook-suite.py status
```

## Nova Status
```bash
# Current work blocks and velocity
cat 2000-BLOCK-MILESTONE.md

# Latest status (pipeline, next actions)
cat BLOCK-1854-STATUS.md

# Diary log
tail -30 diary.md
```

## Execution Plan (57 min → $604.5K)
```bash
# Step 1: Gateway restart (1 min → $50K bounties)
openclaw gateway restart

# Step 2: GitHub auth (5 min → $125K grants)
gh auth login

# Step 3: Send service messages (51 min → $479.5K)
# See SERVICE-OUTREACH-EXECUTION-GUIDE.md for commands
```

## Work Blocks
```bash
# Pick random task from today.md
python3 tools/task-randomizer.py

# Update status docs
cat BLOCK-1854-STATUS.md  # Pipeline view
cat 2000-BLOCK-MILESTONE.md  # Milestone view
```

---

**Nova's work:** Build pipeline, create tools, draft content
**Arthur's work:** Execute 3 commands (gateway, auth, send)

Division of labor. Clear.

---

*Last updated: Work block 1858*
*Run `cat QUICK-COMMANDS.md` for command reference*
