# README-trim-today.md

## trim-today.py

Session context optimizer. Archives old sessions from today.md to memory/YYYY-MM-DD.md, keeping only the current (newest) session. Reduces injected context by ~50%.

### Usage

```bash
# Standard usage (run on session start)
python3 tools/trim-today.py

# With session limit (from HEARTBEAT.md)
python3 tools/trim-today.py 10  # Keep last 10 sessions
```

### What It Does

1. **Scans** today.md for session boundaries
2. **Archives** old sessions to `memory/YYYY-MM-DD.md`
3. **Keeps** only the newest/current session in today.md
4. **Reports** size reduction

### Output Example

```
Archived sessions (except current) to memory/2026-02-07.md
Trimmed 8 old sessions (archived to memory/). Kept current session only.
Reduced size from 61440 to 30720 bytes (50%)
```

### Session Detection Patterns

The tool recognizes three session boundary formats:

| Pattern | Example |
|---------|---------|
| Session header | `**Latest Session (N):**` |
| Work block header | `## [WORK BLOCK N — timestamp]` |
| Bullet format | `- Work block NNNN: description` |

### Why Use This

**Problem:** today.md grows to 50KB+ with 80+ sessions
**Impact:** Injects ~8k tokens into every new session
**Solution:** Keep only last session = ~4k tokens (50% reduction)

### Integration

**HEARTBEAT.md** (session startup):
```yaml
- name: "Session Startup"
  every: "startup"
  message: |
    Run: python3 tools/trim-today.py 10
    GOAL: Reduce injected context from 50KB+ to 25KB
```

### Archive Format

Old sessions appended to: `memory/YYYY-MM-DD.md`

```
[existing content]

**Latest Session (42):**
[session content]

**Latest Session (43):**
[session content]
```

### Safety

- ✅ Archives before trimming (data never lost)
- ✅ Creates memory/ directory if missing
- ✅ Handles empty files gracefully
- ✅ Reports what was done

### Dependencies

- Python 3.6+
- Standard library (re, sys, datetime, os)

### Created

Work block ~1750 — Context bloat mitigation toolkit
