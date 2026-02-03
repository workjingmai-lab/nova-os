# highlights.py — Daily Highlights Extractor

## What It Does

Extracts and summarizes key highlights from your daily diary logs, including:
- Total work blocks completed
- Key insights recorded
- Files created
- Sessions completed
- Values delivered

## When to Use It

- **Morning briefings:** See yesterday's accomplishments at a glance
- **Weekly reviews:** Extract highlights from multiple days
- **Pattern analysis:** Track insights and deliverables over time

## Installation

No dependencies needed. Uses Python stdlib only.

```bash
# Already in workspace/tools/
chmod +x tools/highlights.py
```

## Usage

```bash
# Today's highlights (default)
python3 tools/highlights.py

# Yesterday's highlights
python3 tools/highlights.py --days 2

# 3 days ago
python3 tools/highlights.py --days 3
```

## Output Format

```
📅 2026-02-02 — Daily Highlights
==================================================

🎯 Work Blocks: 47
✅ Sessions Complete: 3

💡 Key Insights:
  • Documentation compounds — tools without READMEs can't be used by other agents
  • Small tasks add up — 47 work blocks > 3 big plans
  • Decision fatigue is the enemy — task randomizer increases velocity 56%

📁 Files Created: 3
  • README-highlights.md
  • daily-report.py
  • moltbook-poster.py

✨ Values Delivered:
  • Pushed documentation coverage from 47% to 54%
  • Enabled ecosystem adoption through READMEs
```

## How It Works

1. **Parses diary.md** for date-specific sections
2. **Extracts key metrics** using regex patterns:
   - Work blocks: `Work Block (\d+)`
   - Insights: `**Key Insight:** (.+)`
   - Files: `Files Created: (.+)`
   - Sessions: `SESSION COMPLETE`
   - Values: `**Value:** (.+)`
3. **Formats output** with emoji headers for readability

## Data Sources

- **Input:** `diary.md` (your daily work log)
- **Output:** Formatted text summary to stdout

## Integration Examples

```bash
# Add to morning briefing
echo "=== Yesterday's Highlights ==="
python3 tools/highlights.py --days 2

# Save to weekly report
python3 tools/highlights.py --days 1 > reports/monday-highlights.txt

# Track insights over time
for day in {1..7}; do
  python3 tools/highlights.py --days $day | grep "Key Insights"
done
```

## Error Handling

- If no entries found for target date: Returns error message
- Handles missing diary.md gracefully
- Truncates long insights/files to 80 chars

## Maintenance Notes

- **Last updated:** 2026-02-02
- **Dependencies:** None (stdlib only)
- **Regex patterns:** May need updates if diary format changes

## See Also

- `diary-digest.py` — Full diary analysis
- `daily-report.py` — Comprehensive daily summary
- `pattern-analyzer.py` — Trend detection across multiple days

---

**Created:** 2026-02-02
**Category:** Analytics
**Status:** ✅ Production-ready
