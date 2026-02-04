# README: trim-today.py

## Problem
**today.md grows to 50KB+ with session history** → every new session injects massive context → token bloat.

## Solution
**Trim today.md to last N sessions** (default: 10) → 50% smaller injected context.

## Usage

```bash
# Keep last 10 sessions (default)
python3 tools/trim-today.py

# Keep last 15 sessions
python3 tools/trim-today.py 15

# Keep last 5 sessions (aggressive trim)
python3 tools/trim-today.py 5
```

## What It Does
- Reads today.md
- Finds all session entries
- Keeps header + last N sessions
- Overwrites today.md with trimmed version
- Reports: "Trimmed X old sessions. Reduced from A to B bytes (C%)"

## When to Run
1. **On session startup** — Run automatically to keep context lean
2. **Manually** — When today.md exceeds 40KB
3. **Before archiving** — Move old sessions to memory/YYYY-MM-DD.md first

## Integration
Add to HEARTBEAT.md or session startup:
```yaml
- name: "Session Startup"
  every: "startup"
  message: |
    Run: python3 tools/trim-today.py 10
```

## Impact
- **Before:** 61KB injected → ~8k tokens
- **After:** 30KB injected → ~4k tokens
- **Savings:** 50% token reduction on every new session

## Caveats
- **Does not delete content** — old sessions still in diary.md
- **Reversible** — git checkout today.md if needed
- **Safe** — keeps all recent context in header (Working Memory, Next Actions, Session Stats)
