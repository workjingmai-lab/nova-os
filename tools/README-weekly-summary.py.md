# weekly-summary.py

**Generate weekly progress reports from diary.md and revenue-tracker.**

## Purpose

Consolidate weekly activity into a single summary report. Tracks work blocks, revenue pipeline, tools created, knowledge articles, and key learnings.

## Usage

```bash
python3 tools/weekly-summary.py                    # This week's summary
python3 tools/weekly-summary.py --week 3           # Week 3 specifically
python3 tools/weekly-summary.py --format markdown  # Markdown output (default)
python3 tools/weekly-summary.py --format json      # JSON for API/automation
```

## What It Does

Scans multiple data sources:
- **diary.md** — Work block logs (count, velocity)
- **revenue-tracker.py** — Pipeline stats (total, submitted, conversion)
- **tools/** — File counts, documentation coverage
- **knowledge/** — Article counts

## Output

Weekly summary including:
- Work blocks completed (count, velocity vs target)
- Revenue pipeline stats (total, submitted, won/lost, conversion rate)
- Tools created / documentation coverage percentage
- Knowledge articles published
- Top 3 achievements
- Key lessons learned

## Output Formats

### Markdown (default)
Human-readable report with sections and bullet points.

### JSON
Structured data for API integration or automation:
```json
{
  "week": 3,
  "work_blocks": 2021,
  "velocity": "44 blocks/hr",
  "pipeline_total": 880065,
  "pipeline_submitted": 5000,
  "conversion_rate": 0.0,
  "tools_created": 5,
  "tools_documented_pct": 100,
  "knowledge_articles": 8
}
```

## Use When

- Weekly reviews and retrospectives
- Progress updates for stakeholders
- Tracking velocity trends over time
- Measuring pipeline growth

## Data Sources

- diary.md (work block entries)
- revenue-tracker.py (pipeline JSON)
- tools/ (file listing)
- knowledge/ (file listing)

## Created

2026-02-05 — Work block 2031

## See Also

- diary.md — Daily work log
- revenue-tracker.py — Revenue pipeline tracking
- velocity-calc.py — Velocity calculator and predictor
