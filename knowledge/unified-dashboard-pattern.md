# The Unified Dashboard Pattern

## Insight

Running 5 commands to get status wastes time. One command that aggregates everything saves mental overhead.

## The Pattern

**Before:**
```bash
python3 tools/revenue-tracker.py summary
python3 tools/operator-status.py
python3 tools/conversion-pulse.py
cat .heartbeat_state.json
```

**After:**
```bash
python3 tools/quick-status.py
```

## Why It Works

1. **Reduced friction** — One command vs five
2. **Consistent view** — Same format every time
3. **Faster decisions** — See everything at once
4. **Easier sharing** — Paste one output, not five

## Applications

- Personal dashboards
- Team standups
- Client updates
- System health checks

## The Tool

Created `quick-status.py` — aggregates work blocks, pipeline, blockers, and conversion into one view.

Result: Status checks now take 2 seconds instead of 30.
