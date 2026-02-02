# quick-log.py — Fast Diary Entry

Add work block entries to diary.md instantly from the command line.

## What It Does

 Creates `[WORK BLOCK N — timestamp]` entries in diary.md with:
- Auto-incrementing block number
- UTC timestamp
- Task description
- Status indicator (✅/⚠️)
- Optional time tracking

## Usage

```bash
# Basic log entry
python3 tools/quick-log.py "Task description here"

# With status
python3 tools/quick-log.py "Fixed bug in script" "✅"

# With time tracking
python3 tools/quick-log.py "Wrote documentation" "✅" "45"
```

## Output

Appends to diary.md:

```markdown
## [WORK BLOCK 541 — 2026-02-02T12:32Z] ⚡ WORK BLOCK: Task description here

**Status:** ✅
**Time:** 45 seconds
**Result:** Entry logged via quick-log.py

---
```

## Why It Matters

Reduce logging friction:
- No manual timestamp calculation
- No block number tracking
- One command = documented work
- Integrates with all diary analysis tools

## Use Cases

- Quick logs between meetings
- capturing small wins
- Command-line workflow automation
- Script logging (wrap commands in quick-log)

## See Also

- `diary-digest.py` — Analyze your logs
- `velocity-calc.py` — Calculate metrics from logs
- `evening-reflection.py` — Daily review template
