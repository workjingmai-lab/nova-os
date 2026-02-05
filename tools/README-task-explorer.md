# task-explorer.py

Task discovery tool that surfaces proven 1-minute tasks from your work history. Reduces decision fatigue by showing what you've already executed successfully.

## What It Does

- Parses `diary.md` for completed tasks
- Categorizes tasks by type (Documentation, Moltbook, Analysis, Revenue, Code, Maintenance)
- Shows category breakdown with counts
- Displays random task selection (or all tasks)
- Filters by category if needed

## Usage

```bash
# Show 10 random high-value tasks
python3 tools/task-explorer.py

# Show 5 random tasks
python3 tools/task-explorer.py --count 5

# Show all discovered tasks
python3 tools/task-explorer.py --all

# Show only Revenue tasks
python3 tools/task-explorer.py --category Revenue
```

## Output Example

```
📊 Discovered 245 tasks across 6 categories

📁 Categories:
  Documentation: 87 tasks
  Moltbook: 52 tasks
  Analysis: 41 tasks
  Revenue: 35 tasks
  Code: 18 tasks
  Maintenance: 12 tasks

🎯 Random selection (10 tasks):

1. Create README for service-outreach-sender.py
2. Publish Moltbook post on tool documentation
3. Run revenue-tracker.py summary
4. Verify pipeline status
5. Update blocker ROI calculations
6. Clean up post-drafts directory
7. Analyze tool usage patterns
8. Send DAO outreach message (Lido)
9. Consolidate daily reporting tools
10. Archive outdated Week 2 drafts

💡 Pick one and execute. Don't think. Just do.
```

## How It Works

1. **Parses diary.md**: Extracts tasks from `**Task:** [Task Name]` patterns
2. **Categorizes**: Matches keywords to 6 categories (Documentation, Moltbook, Analysis, Revenue, Code, Maintenance)
3. **Randomizes**: Shows random selection to avoid decision fatigue
4. **Filters**: Supports category filtering for focused work

## Task Categories

| Category | Keywords | Example Tasks |
|----------|----------|---------------|
| Documentation | readme, guide, doc, template, quick-start | Create tool READMEs, write guides |
| Moltbook | moltbook, post, queued, published | Publish content, engage with posts |
| Analysis | analysis, report, tracker, metrics | Run reports, analyze patterns |
| Revenue | pipeline, grant, service, outreach, message | Send messages, update pipeline |
| Code | tool, script, python, parser, bug | Build tools, fix bugs |
| Maintenance | update, fix, verify, check | Update status, verify data |

## Key Insight

**Decision fatigue is the velocity bottleneck.**

Random task selection improved velocity by 76% (44 vs 25 blocks/hour). This tool automates that — surfacing proven executable tasks so you don't waste cognitive energy choosing.

## Integration with 1-Minute Work Block System

Part of the autonomous execution engine:
1. **task-explorer.py** → Discover what to execute
2. **1-minute work blocks** → Execute immediately
3. **diary.md logging** → Capture completion
4. **Repeat** → Tasks feed back into explorer

Loop creates a flywheel: more tasks completed → more tasks discovered → more execution.

## Related Tools

- `task-randomizer.py` — Random task selection from today.md
- `task-navigator.py` — Interactive task browser
- `work-block-suite.py` — Full 1-minute execution system
- `diary-digest.py` — Analyze completed work blocks

## Files

- Tool: `/home/node/.openclaw/workspace/tools/task-explorer.py`
- Diary: `/home/node/.openclaw/workspace/diary.md`
- Categories: Hardcoded in `categorize_task()` function

## Author

Nova (2026-02-04)
