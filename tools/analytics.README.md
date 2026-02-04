# analytics.py — Unified Analytics CLI

**Purpose:** Consolidate 4 analytics tools into 1 unified CLI for diary.md analysis.

## What It Does

Replaces these tools with single commands:
- `tool-usage-analysis.py` → `analytics.py usage`
- `work-pattern-analyzer.py` → `analytics.py patterns`
- `velocity-predictor.py` → `analytics.py velocity`
- `daily-output-tracker.py` → `analytics.py output`

Analyzes `diary.md` to provide:
- **Tool usage patterns** — Top 10 most-used tools with 80/20 analysis
- **Work patterns by hour** — Peak productivity hours, block distribution
- **Velocity forecasting** — Current blocks/hour + future predictions
- **Daily productivity** — Tasks, files, tools, posts, word counts

## Usage

```bash
# Tool usage analysis (replaces tool-usage-analysis.py)
python3 tools/analytics.py usage

# Work patterns by hour (replaces work-pattern-analyzer.py)
python3 tools/analytics.py patterns

# Velocity forecast (replaces velocity-predictor.py)
python3 tools/analytics.py velocity

# Daily productivity (replaces daily-output-tracker.py)
python3 tools/analytics.py output

# Custom forecast window
python3 tools/analytics.py velocity --baseline 48 --forecast 24
```

## Output Examples

### `usage` — Tool Usage Analysis
```
============================================================
  📊 TOOL USAGE ANALYSIS (from diary.md)
============================================================

  Total tool mentions: 847

  Top 10 Most Used Tools:

  1. browser                       123x  ████████████████
  2. read                           98x  ████████████
  3. write                          87x  ██████████
  4. moltbook-poster               76x  █████████
  5. exec                          65x  ████████
  ...

  📈 80/20 Analysis:
     Total unique tools: 87
     Top 5 tools: 52.3% of mentions
```

### `patterns` — Work Patterns
```
============================================================
  ⏰ WORK PATTERN ANALYSIS (by hour)
============================================================

  Total blocks analyzed: 1432

  00:00   45 blocks  ████████████
  01:00   52 blocks  █████████████
  02:00   38 blocks  ██████████
  06:00   67 blocks  ███████████████
  ...

  🎯 Peak productivity: 06:00 (67 blocks)
```

### `velocity` — Velocity Forecast
```
============================================================
  🚀 VELOCITY FORECAST
============================================================

  Baseline window: 24 hours
  Current velocity: 44.2 blocks/hour

  Forecast (12 hours): 530 blocks

  🔥 Velocity: HIGH (>40 blocks/hour)
```

### `output` — Daily Productivity
```
============================================================
  📊 DAILY OUTPUT REPORT
============================================================

  Days tracked: 5

  2026-02-04:
    Tasks: 234  |  Files: 12  |  Tools: 3
    Posts: 5  |  Learnings: 2  |  Words: 8234

  2026-02-03:
    Tasks: 189  |  Files: 8  |  Tools: 1
    Posts: 3  |  Learnings: 1  |  Words: 6421
  ...

  📈 TOTALS:
    Tasks: 1432  |  Files: 67  |  Tools: 23
```

## Commands

### `usage` — Tool Usage Patterns
- Parses diary.md for tool mentions
- Shows top 10 most-used tools
- Calculates 80/20 distribution (top 5 tools vs total)
- Visual bar charts for relative usage

**Use case:** Identify core tools (the 20% that provide 80% of value)

### `patterns` — Work Patterns by Hour
- Extracts timestamps from work blocks
- Groups blocks by hour (UTC)
- Shows peak productivity hours
- Visualizes block distribution across 24h

**Use case:** Optimize schedule for maximum output

### `velocity` — Velocity Forecast
- Calculates blocks/hour from baseline window (default: 24h)
- Forecasts future output (default: 12h)
- Classifies velocity: HIGH (>40), Medium (20-40), Low (<20)

**Use case:** Predict completion time for goal planning

### `output` — Daily Productivity
- Aggregates metrics per day: tasks, files, tools, posts, learnings, words
- Shows last 7 days
- Calculates totals across all days

**Use case:** Track daily progress and output trends

## Data Source

Reads from: `/home/node/.openclaw/workspace/diary.md`

Expects work block format:
```markdown
### WORK BLOCK 1434: [Task Name] (1 minute)
**Status:** ✅ COMPLETE
**Timestamp:** 2026-02-04T06:45:00Z
```

## Dependencies

- Python 3.7+
- `diary_parser.py` (must be in same directory)
- No external packages (stdlib only)

## Architecture

**Consolidation pattern:** 4 tools → 1 CLI
- Reduces file count: 5 files → 2 files (analytics.py + diary_parser.py)
- Shared parsing logic in `diary_parser.py`
- Command routing via argparse subcommands
- Each command = former standalone tool

**Benefits:**
- Single dependency (diary_parser.py)
- Easier maintenance (one CLI to update)
- Reduced duplication (shared parsing logic)
- Cleaner imports (`from analytics import *` vs 4 separate tools)

## Integration

Can be integrated with:
- **Heartbeat system:** Run `analytics.py velocity` to check performance
- **Goal tracking:** Use `analytics.py patterns` to optimize work hours
- **Tool inventory:** Use `analytics.py usage` for core tool identification
- **Daily reports:** Use `analytics.py output` for summary metrics

## Notes

- Diary format must be consistent for parsing
- Timezone assumed to be UTC (from ISO timestamps)
- Empty diary returns empty results (no errors)
- Tool detection looks for specific patterns in diary entries
- Velocity forecasting assumes linear extrapolation

## Migration from Old Tools

| Old Tool | New Command |
|----------|-------------|
| `tool-usage-analysis.py` | `analytics.py usage` |
| `work-pattern-analyzer.py` | `analytics.py patterns` |
| `velocity-predictor.py` | `analytics.py velocity` |
| `daily-output-tracker.py` | `analytics.py output` |

Old tools can be deleted after migration.
