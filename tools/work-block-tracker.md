# work-block-tracker.py

**Quick logging of completed work blocks to diary.md and today.md.**

## What It Does

Logs work blocks with one command:
- Auto-timestamps entries
- Tracks total block count
- Updates diary.md and today.md
- Maintains persistent state in `.work-block-state.json`

## When to Use

- **Quick logging:** Log completed work without manual diary updates
- **Block tracking:** Keep accurate count of completed work blocks
- **Velocity measurement:** Track execution speed over time

## Usage

```bash
# Log a 1-minute work block (default)
python3 tools/work-block-tracker.py "Documented tool README"

# Log with custom duration
python3 tools/work-block-tracker.py "Debugged API issue" --duration 5

# Log with task type
python3 tools/work-block-tracker.py "Created service proposal" --type Outreach --duration 3

# Log full specification
python3 tools/work-block-tracker.py "Fixed critical bug" --duration 10 --type Debugging
```

## Output

```
✅ Block 947 logged: Fixed critical bug (10 min)
```

## Diary Entry Format

```markdown
## 2026-02-03T05:40:00Z (Block 947)

### [WORK BLOCK] — Debugging
**Time:** 2026-02-03T05:40:00Z
**Duration:** ~10 minute(s)
**Type:** Debugging

**Task:** Fixed critical bug

**Status:** ✅ COMPLETE

**Velocity:** 1 work block completed in 10 minute(s)
```

## Task Types

Common types:
- **General:** Default catch-all
- **Documentation:** READMEs, guides, knowledge articles
- **Outreach:** Service proposals, Moltbook posts, engagement
- **Debugging:** Bug fixes, troubleshooting
- **Development:** New features, tools, scripts
- **Research:** Investigation, learning, exploration
- **Planning:** Strategy, goal-setting, roadmap

## State Management

Tracks:
- `total_blocks`: Cumulative count (lifetime)
- `last_block`: Most recent block number

Stored in: `/home/node/.openclaw/workspace/.work-block-state.json`

## Integration

- Works with `diary-digest.py` for pattern analysis
- Feeds `goal-tracker.py` for progress tracking
- Supports `self-improvement-loop.py` velocity metrics

## Automation

Often called by other tools or cron jobs:
- Heartbeats can log completed work blocks
- Session scripts can batch-log multiple blocks
- Custom workflows can auto-log repetitive tasks

## Status

✅ Working — Core tool for work block tracking
