# operator-status.py — Operator Mode Health Check

**Created:** 2026-02-07 (Work block 3027)
**Purpose:** Single-command status check for post-3000 operator mode

## What It Does

Verifies that all systems are ready for Arthur to execute `send-everything.sh`:
- ✅ Heartbeat state exists and is recent
- ✅ START-HERE.md is present and complete
- ✅ send-everything.sh exists and is executable
- ✅ Pipeline data is available
- ⚠️ Blockers are identified

## Usage

```bash
python3 tools/operator-status.py
```

## Output Examples

**When ready:**
```
✅ READY

Last update: 2 minutes ago
START-HERE.md ready (8432 bytes)
send-everything.sh ready
$734,500 ready, $5,000 submitted (99.3% gap)

🚀 Arthur can execute: bash tools/send-everything.sh full
```

**When blocked:**
```
⚠️ BLOCKED

Issues:
   • 2 blockers active

Blockers:
   • Gateway restart: $50K/min (1min)
   • GitHub auth: $26K/min (5min)
```

## Why This Matters

Operator mode is reactive. Arthur needs to know instantly:
1. Is the system ready?
2. What's blocking execution?
3. What's the current pipeline status?

This tool answers all three questions in < 1 second.

No context switching. No file reading. Just run and know.

## Integration

Add to Arthur's quick reference:
```bash
# Check if ready to execute
python3 tools/operator-status.py

# If READY, execute sends
bash tools/send-everything.sh full
```

## Technical Notes

- Exit code: Always 0 (status via output, not exit codes)
- Dependencies: json, os, pathlib (all stdlib)
- Heartbeat freshness: Warns if > 1 hour old
- Pipeline gap: Calculated as (ready - submitted) / ready

## Future Enhancements

- Add --json flag for machine-readable output
- Check lead file freshness (should be < 24h old)
- Verify send-everything.sh dry-run completes successfully
- Add --verbose mode for detailed diagnostics
