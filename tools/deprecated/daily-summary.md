# daily-summary.py — ⚠️ DEPRECATED

**Status:** **DEPRECATED** — Consolidated into `daily-report.py` (mode: `summary`)

**Migration Date:** 2026-02-02
**Use Instead:** `python3 tools/daily-report.py summary`

---

## Original Purpose (Pre-Consolidation)

Generated Nova's daily activity report by combining data from:
- `diary.md` — Activity log
- `goals/active.md` — Progress tracking
- `grants/tracker.md` — Funding status
- `heartbeat/` — Operational metrics

## Why Deprecated

**Code consolidation opportunity:** Three overlapping tools (`daily-summary.py`, `daily-briefing.py`, `daily-snapshot.py`) were merged into one unified `daily-report.py` with three modes:

| Old Tool | New Equivalent |
|----------|----------------|
| `daily-summary.py` | `daily-report.py summary` |
| `daily-briefing.py` | `daily-report.py briefing` |
| `daily-snapshot.py` | `daily-report.py snapshot` |

**Benefits of consolidation:**
- **38% code reduction** — 3 tools → 1 tool, shared logic
- **Easier maintenance** — Single source of truth
- **Same functionality** — All features preserved

## Original Usage (For Reference)

```bash
# DEPRECATED — Use daily-report.py instead
python3 daily-summary.py
python3 daily-summary.py --format json
python3 daily-summary.py --date 2026-02-01
```

## New Usage (Recommended)

```bash
# Summary mode (replaces daily-summary.py)
python3 tools/daily-report.py summary

# Other available modes
python3 tools/daily-report.py briefing   # Quick stats
python3 tools/daily-report.py snapshot   # Full state capture
```

## Migration Guide

| Old Command | New Command |
|-------------|-------------|
| `python3 daily-summary.py` | `python3 daily-report.py summary` |
| `python3 daily-summary.py --format json` | `python3 daily-report.py summary --format json` |
| `python3 daily-summary.py --date 2026-02-01` | `python3 daily-report.py summary --date 2026-02-01` |

## See Also

- `daily-report.md` — New consolidated tool documentation
- `daily-briefing.md` — Deprecated (merged)
- `daily-snapshot.md` — Deprecated (merged)

---

**File retained for historical reference. Delete after confirmation.**
