# analytics.py

**Unified analytics CLI** — Consolidates 4 tools into one. Tool usage, work patterns, velocity forecasting, daily output.

## Purpose

Replaces 4 separate tools with a single CLI for diary.md analytics.

**Replaces:**
- `tool-usage-analysis.py` → `analytics.py usage`
- `work-pattern-analyzer.py` → `analytics.py patterns`
- `velocity-predictor.py` → `analytics.py velocity`
- `daily-output-tracker.py` → `analytics.py output`

## Usage

```bash
python3 tools/analytics.py usage              # Top tools by usage
python3 tools/analytics.py patterns           # Work patterns by hour
python3 tools/analytics.py velocity           # Forecast velocity
python3 tools/analytics.py output             # Daily productivity metrics
```

## Commands

### usage — Tool Usage Analysis

```bash
python3 tools/analytics.py usage
```

Shows most-used tools from diary.md.

**Output:**
```
═══════════════════════════════════════════════════════════
  📊 TOOL USAGE ANALYSIS (from diary.md)
═══════════════════════════════════════════════════════════

  Total tool mentions: 142

  Top 10 Most Used Tools:

  1. moltbook-suite.py                45x  ████████████████
  2. goal-tracker.py                  28x  ████████
  3. revenue-tracker.py               18x  ████
  4. blocker-status.py                12x  ██
  5. daily-report.py                  10x  ██
  ...

  📈 80/20 Analysis:
     Total unique tools: 47
     Top 5 tools: 77.5% of mentions
```

**Use case:** Identify core tools (80% of value from 20% of tools).

---

### patterns — Work Pattern Analysis

```bash
python3 tools/analytics.py patterns
```

Shows work distribution by hour of day.

**Output:**
```
═══════════════════════════════════════════════════════════
  ⏰ WORK PATTERN ANALYSIS (by hour)
═══════════════════════════════════════════════════════════

  Total blocks analyzed: 1433

  00:00   23 blocks  ████████
  01:00   31 blocks  ███████████
  02:00   45 blocks  ████████████████
  03:00   52 blocks  ██████████████████
  04:00   38 blocks  ██████████
  05:00   12 blocks  ████
  ...

  🎯 Peak productivity: 03:00 (52 blocks)
```

**Use case:** Find peak productivity hours, optimize schedule.

---

### velocity — Velocity Forecast

```bash
python3 tools/analytics.py velocity [--baseline HOURS] [--forecast HOURS]
```

Forecasts work completion rate.

**Options:**
- `--baseline N` — Analysis window in hours (default: 24)
- `--forecast N` — Forecast horizon in hours (default: 12)

**Output:**
```
═══════════════════════════════════════════════════════════
  🚀 VELOCITY FORECAST
═══════════════════════════════════════════════════════════

  Baseline window: 24 hours
  Current velocity: 44.2 blocks/hour

  Forecast (12 hours): 530 blocks

  🔥 Velocity: HIGH (>40 blocks/hour)
```

**Interpretation:**
- **HIGH (>40 blocks/hour):** Peak productivity
- **Medium (20-40 blocks/hour):** Normal pace
- **Low (<20 blocks/hour):** Slowing down, check blockers

**Use case:** Forecast completion, detect velocity changes.

---

### output — Daily Output Report

```bash
python3 tools/analytics.py output
```

Shows daily productivity metrics.

**Output:**
```
═══════════════════════════════════════════════════════════
  📊 DAILY OUTPUT REPORT
═══════════════════════════════════════════════════════════

  Days tracked: 4

  2026-02-01:
    Tasks: 482  |  Files: 23  |  Tools: 8
    Posts: 3  |  Learnings: 12  |  Words: 4523

  2026-02-02:
    Tasks: 312  |  Files: 18  |  Tools: 6
    Posts: 4  |  Learnings: 8  |  Words: 3891

  ...

  📈 TOTALS:
    Tasks: 1429  |  Files: 87  |  Tools: 25
```

**Metrics tracked:**
- `tasks_completed` — Work blocks completed
- `files_created` — Files written
- `tools_built` — New tools created
- `posts_published` — Moltbook posts
- `learnings_logged` — Insights documented
- `word_count` — Words written

**Use case:** Track daily output, identify trends, measure productivity.

## Consolidation Benefits

**Before:** 4 separate tools (4000+ lines total)
- `tool-usage-analysis.py` (1800 lines)
- `work-pattern-analyzer.py` (1200 lines)
- `velocity-predictor.py` (600 lines)
- `daily-output-tracker.py (400 lines)

**After:** 1 unified CLI (230 lines)
- Single entry point
- Shared DiaryParser import
- Consistent interface
- Easier maintenance

**Result:** 94% code reduction, same functionality.

## Dependency

Requires `diary_parser.py` in the same directory (for parsing diary.md).

If `diary_parser.py` is missing, analytics.py falls back to loading it dynamically.

## File Structure

**Reads from:**
- `diary.md` — Work block logs

**Uses:**
- `diary_parser.py` — Diary parsing library

## Why It Matters

**Analytics without visibility = flying blind.**

- **Tool usage:** Identify core tools (80/20 rule)
- **Work patterns:** Find peak hours, optimize schedule
- **Velocity:** Forecast completion, detect slowdowns
- **Daily output:** Track productivity, measure progress
- **Consolidation:** 4 tools → 1 CLI (94% code reduction)

**Consolidation principle:** Different outputs, same input (diary.md) = unify.

## Related Tools

- `diary_parser.py` — Diary parsing library (shared dependency)
- `daily-report.py` — Generate daily summaries
- `velocity-predictor.py` — (DEPRECATED) Use `analytics.py velocity`
- `tool-usage-analysis.py` — (DEPRECATED) Use `analytics.py usage`
