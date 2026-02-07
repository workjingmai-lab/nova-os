# quick-win-finder.py

Find 1-minute tasks when blocked, waiting, or need momentum.

## Usage

```bash
# Get 10 random quick wins from all categories
python3 tools/quick-win-finder.py

# Filter by category
python3 tools/quick-win-finder.py doc      # Documentation tasks
python3 tools/quick-win-finder.py build    # Tool building
python3 tools/quick-win-finder.py analyze  # Analysis tasks
python3 tools/quick-win-finder.py content  # Content creation
python3 tools/quick-win-finder.py org      # Organization
python3 tools/quick-win-finder.py system   # System checks
```

## Purpose

Eliminates decision fatigue when:
- Rate limited on external APIs
- Waiting for human action
- Between major tasks
- Need to maintain momentum

## Categories

| Category | Tasks | Examples |
|----------|-------|----------|
| doc | 5 | Write README, add examples, update MEMORY.md |
| build | 5 | Helper scripts, CLI commands, validators |
| analyze | 5 | File counts, git status, diary review |
| content | 5 | Draft posts, tips, summaries |
| org | 5 | Archiving, cleanup, indexing |
| system | 5 | Disk space, processes, connectivity |

## Output Example

```
⚡ QUICK WINS — Pick one, execute in 60 seconds:

  📝 Add usage example to an existing README
  🔧 Create a 10-line helper script for a repetitive task
  📊 Find the largest files: du -sh * | sort -hr | head -5
  ✍️  Draft a Moltbook post idea in 2 sentences
  📁 Create an index file listing key resources
  ...

💡 Pro tip: Don't think. Pick #3 and do it now.
```

## Integration

Use in cron jobs or heartbeat tasks:
```bash
# When blocked on external dependency
python3 tools/quick-win-finder.py build
```

## Adding Tasks

Edit `QUICK_WINS` list in the script. Format: `(category, description)`
