# session-count-monitor.py

Monitor today.md work block count and file size to prevent context bloat.

## What It Does

- Counts work blocks in today.md
- Checks file size in KB
- Warns when approaching bloat thresholds
- Recommends running trim-today.py

## Usage

```bash
python3 tools/session-count-monitor.py
```

## Output Examples

**Healthy (under threshold):**
```
✅ 25 work blocks (12.5KB) - healthy
→ Optimal: < 50 blocks
→ Warning at: 50+
→ Critical at: 70+
```

**Warning (approaching threshold):**
```
⚠️  WARNING: 61 work blocks (30.8KB)
→ Consider running: python3 tools/trim-today.py 10
→ Context growing large
```

**Critical (exceeded threshold):**
```
🚨 CRITICAL: 75 work blocks (38.2KB)
→ Run: python3 tools/trim-today.py 10
→ Context bloat is SEVERE
```

## Thresholds

- **Warning:** 50+ work blocks
- **Critical:** 70+ work blocks

## Why It Matters

**Context bloat kills token efficiency.**

When today.md grows to 50KB+ (70+ work blocks), it injects massive context into every new session. This wastes tokens and slows down response time.

**Solution:** Run `trim-today.py 10` to keep only the last 10 sessions, reducing context by ~50%.

## Integration

Use in heartbeat or cron jobs:

```bash
# Check every 4 hours
python3 tools/session-count-monitor.py
```

## Related Tools

- **trim-today.py** — Reduces today.md to last N sessions
- **tool-usage-analysis.py** — Analyzes tool usage patterns
- **daily-report.py** — Generates daily summaries

## Author

Created by Nova — Work block 1680

## Version

1.0 — Initial release
