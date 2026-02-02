# Quick Log

Fast diary entry tool — add work block entries to diary.md instantly.

## Features

- **Instant logging** — Add entries without manually editing diary.md
- **Auto-numbering** — Automatically increments work block numbers
- **Status tracking** — Mark tasks as complete ✅ or warning ⚠️
- **Time tracking** — Optional time duration logging
- **UTC timestamps** — Consistent timezone handling

## Usage

```bash
# Quick task completion
python3 tools/quick-log.py "Created README for goal-tracker.py"

# With status indicator
python3 tools/quick-log.py "Fixed bug in agent-digest" "✅"
python3 tools/quick-log.py "Blocked on browser access" "⚠️"

# With time tracking
python3 tools/quick-log.py "Code4rena audit setup" "✅" 127

# Minimal usage (defaults to ✅)
python3 tools/quick-log.py "Updated today.md stats"
```

## Entry Format

Creates entries in diary.md:

```markdown
## [WORK BLOCK 500 — 2026-02-02T13:20Z] ⚡ WORK BLOCK: Created README for goal-tracker.py

**Status:** ✅
**Time:** N/A seconds
**Result:** Entry logged via quick-log.py

---
```

## Use Cases

1. **Rapid logging** — Capture completed tasks without context switching
2. **Batch updates** — Log multiple blocks quickly after a focused session
3. **Time tracking** — Measure task duration when accuracy matters
4. **Blocker documentation** — Log issues with ⚠️ status for follow-up

## Workflow Integration

Combine with other tools for seamless workflow:

```bash
# Complete a work block
python3 tools/quick-log.py "Documented quick-log.py"

# Check progress
python3 tools/velocity-check.py

# Update today.md
# ... manual edit or automated ...

# Next block
python3 tools/quick-log.py "Started next documentation sprint"
```

## Aliases (Optional)

Add to your shell for even faster access:

```bash
alias log='python3 ~/workspace/tools/quick-log.py'
alias logw='python3 ~/workspace/tools/quick-log.py' # with default ✅
```

Then use:
```bash
log "Task completed"
log "Blocked on API" "⚠️"
```

## Created

2026-02-02 — Part of Week 2 workflow optimization toolkit
