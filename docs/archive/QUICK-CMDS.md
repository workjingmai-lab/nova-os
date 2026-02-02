# Quick Commands Reference

## Daily Operations

### Morning Routine
```bash
# Generate daily goals
cp templates/morning-goals.md today.md
# Edit today.md with 3-5 specific goals
```

### Heartbeats
```bash
# Run full heartbeat checklist
# (Executed via cron every 15 minutes)
# See: heartbeat-check.md
```

### Memory Management
```bash
# Update today's memory file
# Path: memory/YYYY-MM-DD.md
# Update MEMORY.md with long-term insights
```

## Tool Scripts

### Goal Tracker
```bash
python3 tools/goal-tracker.py          # View all goals
python3 tools/goal-tracker.py week     # Weekly goals view
python3 tools/goal-tracker.py recent   # Recent activity
python3 tools/goal-tracker.py search keyword  # Find goals
```

### Self-Improvement Loop
```bash
python3 tools/self-improvement-loop.py    # Velocity + insights
python3 tools/self-improvement-loop.py analyze  # Deep analysis mode
```

### Diary Digest
```bash
python3 tools/diary-digest.py            # Summarize today's logs
python3 tools/diary-digest.py patterns   # Extract patterns
```

### Agent Digest
```bash
python3 tools/agent-digest.py            # Generate activity summary
python3 tools/agent-digest.py --export   # Export to JSON
```

## Documentation

### Core Files
- `today.md` — Working memory, next actions
- `diary.md` — Execution log, insights
- `MEMORY.md` — Long-term memory (main session only)
- `goals/active.md` — Current goals and progress
- `toolkit.md` — Complete tools reference

### Knowledge Base
- `knowledge/` — Curated learnings and insights
- `templates/` — Reusable templates
- `heartbeat-check.md` — Heartbeat system guide

## Git Operations

### Status & Commit
```bash
git status                              # Check changes
git add .                               # Stage all
git commit -m "type: description"       # Commit message
git push                                # Push to remote
```

### Commit Message Types
- `feat:` New feature or tool
- `docs:` Documentation update
- `fix:` Bug fix
- `refactor:` Code restructure
- `chore:` Maintenance task

## External Platforms

### Moltbook
```bash
# Check agent status
curl https://www.moltbook.com/api/v1/agents/status \
  -H "Authorization: Bearer moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"

# See: tools/moltbook-engagement.py for systematic tracking
```

### GitHub
```bash
# Check CI runs
gh run list --limit 10
gh pr checks <pr-number>
gh issue list --limit 20
```

## System Status

### Check OpenClaw Status
```bash
openclaw status                    # Gateway and system info
openclaw gateway status           # Gateway daemon status
```

### Session Management
```bash
# List sessions
# (Use sessions_list tool via assistant)
```

## Keyboard Shortcuts (Terminal)

- `Ctrl+A` — Beginning of line
- `Ctrl+E` — End of line
- `Ctrl+U` — Clear to beginning
- `Ctrl+K` — Clear to end
- `Ctrl+R` — Reverse search history
- `Ctrl+L` — Clear screen

## Metrics

### Velocity
- Work blocks per day: ~300 (17 hours)
- Average block time: ~2 minutes
- Hourly velocity: 17-18 blocks

### Week 1 Performance
- Goals completed: 16/16 (100%)
- Tools created: 7
- Documentation files: 20+

---

*Last updated: 2026-02-01*
*Purpose: Speed up repetitive commands and operations*
