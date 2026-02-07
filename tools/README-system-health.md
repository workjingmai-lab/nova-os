# system-health.py

**One-command system status dashboard.**

## Purpose

Quick overview of all key metrics: work blocks, tools, documentation coverage, revenue pipeline, and blockers. No need to run multiple commands — one view of everything.

## Usage

```bash
# Full dashboard
python3 tools/system-health.py

# Compact single-line view
python3 tools/system-health.py --mini
```

## Output

### Full Dashboard
```
╔════════════════════════════════════════╗
║        🦞 SYSTEM HEALTH DASHBOARD      ║
║              03:21 UTC                 ║
╠════════════════════════════════════════╣
║                                        ║
║  📊 WORK BLOCKS                        ║
║     Today:        5                    ║
║     Total:       49                    ║
║                                        ║
║  🛠️  TOOLS                              ║
║     Python:     169                    ║
║     READMEs:    209 (124%)             ║
║                                        ║
║  💰 REVENUE PIPELINE                   ║
║     Total:        $1.49M               ║
║     Ready:        $609K                ║
║     Submitted:    $5K                  ║
║     Won:          $0                   ║
║                                        ║
╚════════════════════════════════════════╝
```

### Mini View
```
🧩 5 blocks | 🛠️ 169 tools | 💰 $1.49M | 03:21 UTC
```

## Metrics Tracked

| Metric | Source | Description |
|--------|--------|-------------|
| Blocks Today | `memory/YYYY-MM-DD.md` | Work blocks executed today |
| Total Blocks | `memory/*.md` | All-time work block count |
| Python Tools | `tools/*.py` | Executable tools created |
| READMEs | `tools/README*.md` | Documentation files |
| Coverage | Calculated | Docs/tools ratio |
| Pipeline | `data/revenue-pipeline.json` | Revenue opportunities |

## Integration

Add to startup or heartbeat:
```bash
# In session startup
python3 tools/system-health.py --mini
```

## Files

- `tools/system-health.py` — Main dashboard
- `memory/*.md` — Work block data source
- `tools/*.py` — Tool count source
- `data/revenue-pipeline.json` — Pipeline data source

## Related Tools

- `daily-revenue-action.py` — Recommended next action
- `revenue-tracker.py` — Detailed pipeline management
- `velocity-calc.py` — Velocity analysis

---

*Created: Work block 6, 2026-02-07*
*Part of Week 3 visibility tools*
