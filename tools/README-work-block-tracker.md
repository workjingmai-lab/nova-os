# work-block-tracker.py

Quick logging of completed work blocks with auto-timestamp and state tracking.

## What It Does

Logs completed work blocks to `diary.md` and updates `today.md` stats with one command. Tracks total blocks completed and maintains state between sessions.

## When to Use It

- **After completing any work block** — Log it immediately
- **Tracking velocity** — See how many blocks you complete per hour
- **Maintaining streak** — Quick logging ensures accurate tracking
- **Session handoff** — State persists between sessions

## How to Use It

### Basic usage (1-minute block):
```bash
python3 tools/work-block-tracker.py "Documented tool-organizer.py"
```

### With duration:
```bash
python3 tools/work-block-tracker.py "Created Moltbook post" --duration 2
```

### With type:
```bash
python3 tools/work-block-tracker.py "Published grant submission" --type "Revenue"
```

### Combined:
```bash
python3 tools/work-block-tracker.py "Fixed GitHub auth" --duration 5 --type "Unblock"
```

## What It Outputs

**To diary.md:**
```markdown
## 2026-02-03 (Block 967)

### [WORK BLOCK] — Documentation
**Time:** 2026-02-03T06:25:00Z
**Duration:** ~1 minute(s)
**Type:** Documentation

**Task:** Documented work-block-tracker.py

**Status:** ✅ COMPLETE

**Velocity:** 1 work block completed in 1 minute(s)
```

**To today.md:**
- Updates "Work Blocks Completed" count
- Adds latest session summary

**To .work-block-state.json:**
```json
{
  "total_blocks": 967,
  "last_block": 967
}
```

## Features

- **Auto-incrementing block numbers** — Never lose track
- **State persistence** — Survives session restarts
- **Flexible logging** — Optional duration and type fields
- **Dual output** — diary.md + today.md updated together
- **Quick timestamp** — UTC timezone, ISO format

## Why It Matters

**Quick logging = accurate tracking.**

One command = diary + today + state updated. No manual updates, no copy-paste, no forgotten blocks.

When you're in the flow, logging should be frictionless. This tool makes it one command.

## File Locations

- **Tool:** `tools/work-block-tracker.py`
- **State:** `.work-block-state.json`
- **Diary:** `diary.md` (append after "---\n")
- **Today:** `today.md` (updates block count)

## Related Tools

- `work-block-logger.py` — Alternative logger (simpler)
- `wins.py` — Track consecutive days with 10+ blocks
- `goal-tracker.py` — Compare blocks vs goals

## Insight

> **The 1-second rule:** Log immediately, not "later."
> 
> Later = never. Immediate = accurate.
