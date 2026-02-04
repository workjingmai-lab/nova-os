# analytics.py

**Unified analytics CLI — 4 tools consolidated into 1.**

## What it does

Replaces 4 separate analytics tools with one unified interface:
- `tool-usage-analysis.py` → `analytics.py usage` (top tools by usage)
- `work-pattern-analyzer.py` → `analytics.py patterns` (work patterns by hour)
- `velocity-predictor.py` → `analytics.py velocity` (forecast velocity)
- `daily-output-tracker.py` → `analytics.py output` (daily productivity metrics)

## Usage

```bash
# Tool usage patterns
python3 tools/analytics.py usage

# Work patterns by hour
python3 tools/analytics.py patterns

# Velocity forecast
python3 tools/analytics.py velocity [--baseline HOURS] [--forecast HOURS]

# Daily productivity metrics
python3 tools/analytics.py output
```

## Output examples

### Tool usage (`analytics.py usage`)
```
============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 342

  Top 10 Most Used Tools:

  1. diary-digest.py                  42x  ████████████
  2. moltbot-scorer.py                38x  ██████████
  3. goal-tracker.py                  31x  ████████
  4. revenue-tracker.py               28x  ███████
  5. workspace-status.py              24x  ██████

  📈 80/20 Analysis:
     Total unique tools: 87
     Top 5 tools: 45.6% of mentions
```

### Work patterns (`analytics.py patterns`)
```
============================================================
  ⏰ WORK PATTERN ANALYSIS (by hour)
============================================================

  Total blocks analyzed: 1424

  00:00   45 blocks  ████████████
  01:00   38 blocks  ██████████
  02:00   52 blocks  ███████████████
  ...

  🎯 Peak productivity: 02:00 (52 blocks)
```

### Velocity forecast (`analytics.py velocity`)
```
============================================================
  🚀 VELOCITY FORECAST
============================================================

  Baseline window: 24 hours
  Current velocity: 44.2 blocks/hour

  Forecast (12 hours): 530 blocks

  🔥 Velocity: HIGH (>40 blocks/hour)
```

### Daily output (`analytics.py output`)
```
============================================================
  📊 DAILY OUTPUT REPORT
============================================================

  Days tracked: 4

  2026-02-04:
    Tasks: 1423  |  Files: 8  |  Tools: 3
    Posts: 2  |  Learnings: 5  |  Words: 2340
  ...

  📈 TOTALS:
    Tasks: 2847  |  Files: 28  |  Tools: 12
```

## Why it matters

**Consolidation reduces debt** — 4 tools → 1 interface means:
- Single codebase to maintain
- Consistent CLI patterns
- Shared diary_parser dependency
- Easier to extend with new analytics

**Use cases:**
- `usage` — Identify which tools drive 80% of value (Pareto optimization)
- `patterns` — Discover your most productive hours (schedule deep work there)
- `velocity` — Forecast completion (know if you're on track)
- `output` — Daily retrospective (what did I ship today?)

## Dependencies

- `diary_parser.py` (in same directory) — parses diary.md for structured data

## Integration

Perfect for:
- Daily retrospective (use `analytics.py output` in evening reflection)
- Weekly reviews (use all 4 commands for full picture)
- Optimization loops (use `usage` + `patterns` to focus on high-impact work)
