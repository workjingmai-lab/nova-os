# daily-snapshot.py — ⚠️ DEPRECATED

**Status:** **DEPRECATED** — Consolidated into `daily-report.py` (mode: `snapshot`)

**Migration Date:** 2026-02-02
**Use Instead:** `python3 tools/daily-report.py snapshot`

---

## Original Purpose (Pre-Consolidation)

Generated a quick daily status report (snapshot) showing Nova's current state:
- Goal progress from `active.md`
- Recent activity count from `diary.md`
- Heartbeat metrics (files, lines)
- Tools count
- Credential status

**Output format:** JSON or human-readable text

## Why Deprecated

**Code consolidation:** Three overlapping tools were merged into `daily-report.py`:

| Old Tool | New Equivalent |
|----------|----------------|
| `daily-snapshot.py` | `daily-report.py snapshot` |
| `daily-briefing.py` | `daily-report.py briefing` |
| `daily-summary.py` | `daily-report.py summary` |

**Consolidation benefits:**
- **38% code reduction** — 3 tools → 1
- **Shared logic** — No duplicate parsing code
- **Easier maintenance** — Single source of truth
- **Same functionality** — All features preserved

## Original Usage (For Reference)

```bash
# DEPRECATED — Use daily-report.py instead
python3 daily-snapshot.py
python3 daily-snapshot.py --format json
python3 daily-snapshot.py --output reports/snapshot.json
```

## New Usage (Recommended)

```bash
# Snapshot mode (replaces daily-snapshot.py)
python3 tools/daily-report.py snapshot

# With options
python3 tools/daily-report.py snapshot --format json
python3 tools/daily-report.py snapshot --output reports/snapshot.json

# Other modes
python3 tools/daily-report.py summary    # Daily summary
python3 tools/daily-report.py briefing   # Quick stats
```

## Migration Guide

| Old Command | New Command |
|-------------|-------------|
| `python3 daily-snapshot.py` | `python3 daily-report.py snapshot` |
| `python3 daily-snapshot.py --format json` | `python3 daily-report.py snapshot --format json` |
| `python3 daily-snapshot.py --output file.json` | `python3 daily-report.py snapshot --output file.json` |

## Original Output Format (Preserved)

```json
{
  "timestamp": "2026-02-02T19:36:00Z",
  "goals": {
    "completed": 12,
    "total": 16,
    "percent": 75
  },
  "activity": {
    "recent_entries_24h": 45
  },
  "heartbeats": {
    "files": 177,
    "lines": 52341
  },
  "tools": {
    "total": 112,
    "documented": 73
  }
}
```

## See Also

- `daily-report.md` — New consolidated tool
- `daily-summary.md` — Deprecated (merged)
- `daily-briefing.md` — Deprecated (merged)

---

**File retained for historical reference. Delete after confirmation.**
