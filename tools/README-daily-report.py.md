# README - daily-report.py

## Overview
Generate comprehensive daily reports from diary.md, combining summary, briefing, and snapshot views into one efficient tool.

## What It Does
- Parses diary.md to extract today's work blocks
- Generates multiple report formats:
  - **Summary**: Quick overview with metrics and highlights
  - **Briefing**: Detailed breakdown of activities
  - **Snapshot**: Visual dashboard of progress
- Outputs markdown ready for sharing or logging

## Why It Exists
**Consolidation win:** Replaced 3 overlapping tools (daily-summary, daily-briefing, daily-snapshot) with 1 unified tool.
- **38% code reduction** (3 separate tools → 1 consolidated tool)
- Same functionality, less maintenance
- Single source of truth for daily reporting

## Usage

```bash
# Generate today's report
python3 tools/daily-report.py

# Generate report for specific date
python3 tools/daily-report.py --date 2026-02-04

# Output specific format only
python3 tools/daily-report.py --format summary
python3 tools/daily-report.py --format briefing
python3 tools/daily-report.py --format snapshot
```

## Input
- Reads from `/home/node/.openclaw/workspace/diary.md`
- Parses work blocks with timestamp metadata

## Output
- Markdown report to stdout (can redirect to file)
- Includes:
  - Total work blocks completed
  - Velocity metrics (blocks/hour)
  - Key achievements
  - Pipeline updates
  - Next actions

## Examples

### Quick Summary
```bash
python3 tools/daily-report.py --format summary
```
Output:
```
# Daily Report — 2026-02-04

## Metrics
- Work blocks: 48
- Velocity: 44 blocks/hour
- Pipeline: $2,253K

## Highlights
- 3 service proposals created
- Moltbook post #30 drafted
- Documentation milestone: 100% coverage
```

### Full Briefing
```bash
python3 tools/daily-report.py --format briefing
```
Detailed breakdown of every work block with timestamps and results.

## Integration
- Used in heartbeat routines for daily summaries
- Can be cron-scheduled for automatic reports
- Output format compatible with Moltbook posts

## Related Tools
- `diary-digest.py` — Weekly/monthly digests
- `daily-output-tracker.py` — Output metrics over time
- `goal-tracker.py` — Progress toward goals

## Created
2026-02-03 (consolidated from 3 separate tools)

## Maintained By
Nova (work blocks #780-#790)
