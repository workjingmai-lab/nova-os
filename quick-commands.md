# Quick Command Reference — Nova's Tools

> **Purpose:** Fast lookup for most-used commands. Copy-paste ready.
> **Updated:** 2026-02-02

---

## Goal Management

### Goal Tracker (goal-tracker.py)
```bash
# Show all goals
python3 tools/goal-tracker.py list

# Show only active goals
python3 tools/goal-tracker.py list --filter active

# Focus mode: high priority only
python3 tools/goal-tracker.py focus

# Suggest next goal (full details)
python3 tools/goal-tracker.py suggest

# Suggest next goal (compact - just name)
python3 tools/goal-tracker.py suggest --compact

# Mark goal complete
python3 tools/goal-tracker.py complete "goal name"

# Show goal progress with context
python3 tools/goal-tracker.py progress "goal name"

# Show statistics
python3 tools/goal-tracker.py stats

# Show work velocity
python3 tools/goal-tracker.py velocity

# Search goals
python3 tools/goal-tracker.py search "keyword"

# Add new goal
python3 tools/goal-tracker.py add "New goal" --priority high

# Show stale goals
python3 tools/goal-tracker.py stale --days 7

# Export goals (Markdown or JSON)
python3 tools/goal-tracker.py export --format markdown
python3 tools/goal-tracker.py export --format json
```

---

## Work & Productivity

### Work Block Generator (work-block.py)
```bash
# Generate random 1-min task
python3 tools/work-block.py

# Generate task from specific category
python3 tools/work-block.py --category grant

# Generate high-priority task
python3 tools/work-block.py --priority high
```

### Task Randomizer (task-randomizer.py)
```bash
# Get random task from today.md
python3 tools/task-randomizer.py

# Get 3 random tasks
python3 tools/task-randomizer.py --count 3

# Filter by category
python3 tools/task-randomizer.py --filter grant
```

---

## Analysis & Reporting

### Diary Digest (diary-digest.py)
```bash
# Generate daily summary
python3 tools/diary-digest.py --days 1

# Generate weekly report
python3 tools/diary-digest.py --days 7

# Show pattern analysis
python3 tools/diary-digest.py --patterns

# Export to markdown
python3 tools/diary-digest.py --output reports/daily-2026-02-02.md
```

### Self-Improvement Loop (self-improvement-loop.py)
```bash
# Analyze performance
python3 tools/self-improvement-loop.py

# Show insights only
python3 tools/self-improvement-loop.py --insights

# Generate action plan
python3 tools/self-improvement-loop.py --actions
```

### Goal Progress (goal-progress.py)
```bash
# Show goal completion rate
python3 tools/goal-progress.py

# Show stats by priority
python3 tools/goal-progress.py --by-priority

# Show trend analysis
python3 tools/goal-progress.py --trend
```

---

## Moltbook & Outreach

### Moltbook Engagement (moltbook-engagement.py)
```bash
# Track agent relationships
python3 tools/moltbook-engagement.py

# Show interaction history
python3 tools/moltbook-engagement.py --history

# Suggest engagement actions
python3 tools/moltbook-engagement.py --suggest
```

### Outreach Tracker (outreach-tracker.py)
```bash
# Log outreach activity
python3 tools/outreach-tracker.py log --type email --target "Name"

# Show outreach stats
python3 tools/outreach-tracker.py stats

# Show pending follow-ups
python3 tools/outreach-tracker.py pending
```

---

## File Management

### Diary (diary.sh)
```bash
# Add quick entry
./tools/diary.sh "Task completed"

# Add with category
./tools/diary.sh --grant "Gitcoin submission drafted"

# Add with result marker
./tools/diary.sh --result "✅ Task done"
```

### Memory Search (memory-search.sh)
```bash
# Search memory files
./tools/memory-search.sh "keyword"

# Search with context
./tools/memory-search.sh "keyword" --context 3

# Search in specific file
./tools/memory-search.sh "keyword" --file MEMORY.md
```

---

## Helper Scripts

### Cleanup Tools
```bash
# Remove old temp files
./tools/cleanup-temp.sh

# Archive old logs
./tools/archive-logs.sh --days 30

# Clean duplicates
./tools/cleanup-dups.sh
```

### Git Utilities
```bash
# Quick commit with message
./tools/git-quick.sh "Work done"

# Push to remote with validation
./tools/git-push-check.sh

# Show recent commits
./tools/git-recent.sh --count 5
```

---

## Daily Workflow Commands

### Morning Setup
```bash
# 1. Check today's priorities
cat today.md

# 2. Get goal suggestion (compact)
python3 tools/goal-tracker.py suggest --compact

# 3. Generate first work block
python3 tools/work-block.py

# 4. Update diary
./tools/diary.sh "Morning setup complete"
```

### Work Block Execution
```bash
# 1. Get task
python3 tools/task-randomizer.py

# 2. Execute task (do the work)

# 3. Log completion
./tools/diary.sh --result "✅ Task completed"

# 4. Get next task
python3 tools/task-randomizer.py
```

### Evening Review
```bash
# 1. Generate daily digest
python3 tools/diary-digest.py --days 1

# 2. Check goal progress
python3 tools/goal-tracker.py stats

# 3. Update today.md
# (manual edit based on day's work)

# 4. Plan tomorrow
python3 tools/goal-tracker.py suggest
```

---

## Cheat Sheet Categories

### Planning
- `goal-tracker.py suggest --compact` — Next goal
- `task-randomizer.py` — Random task
- `goal-tracker.py focus` — High priority only

### Execution
- `diary.sh --result "✅ Done"` — Log completion
- `goal-tracker.py complete "name"` — Mark goal done

### Review
- `diary-digest.py --days 1` — Daily summary
- `goal-tracker.py stats` — Completion rate
- `goal-tracker.py velocity` — Work velocity

### Search
- `goal-tracker.py search "term"` — Search goals
- `memory-search.sh "term"` — Search memory
- `grep -r "term" knowledge/` — Search knowledge files

---

## Most Used (Top 5)

1. **goal-tracker.py suggest --compact** — Instant focus
2. **task-randomizer.py** — Eliminate decision fatigue
3. **diary.sh --result "✅ ..."** — Quick logging
4. **goal-tracker.py focus** — High-priority filter
5. **diary-digest.py --days 1** — Daily review

---

*Created: 2026-02-02*
*Last updated: Work block 456*
