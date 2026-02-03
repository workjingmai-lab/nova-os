# highlights.py — Daily Highlights Extractor

**Purpose:** Extracts and summarizes key highlights from `diary.md` — work blocks, insights, files created, and values delivered.

**Category:** Analytics / Reporting

**Created:** 2026-02-01

---

## What It Does

Parses `diary.md` and extracts:
- 🎯 Work blocks completed
- 💡 Key insights
- 📁 Files created
- ✅ Sessions completed
- ✨ Values delivered

Perfect for quick daily retrospectives or generating activity summaries.

---

## Quick Start

```bash
# Today's highlights
python3 tools/highlights.py

# Yesterday's highlights
python3 tools/highlights.py --days 2

# 3 days ago
python3 tools/highlights.py -d 4
```

Example output:
```
📅 2026-02-01 — Daily Highlights
==================================================

🎯 Work Blocks: 84
✅ Sessions Complete: 12

💡 Key Insights:
  • Documentation compounds — tools without READMEs can't be used by other...
  • Decision fatigue is the velocity bottleneck — task randomizer increased...
  • Templates eliminate execution friction...

📁 Files Created: 8
  • tools/grant-submit-helper.py
  • tools/outreach-templates.md
  • knowledge/documentation-strategy.md

✨ Values Delivered:
  • Grant submission pipeline ready (5 submissions, $110K potential)...
  • Created reusable templates for 5 grant platforms...
```

---

## How It Works

### Date Parsing
- Searches for `## YYYY-MM-DD` headers in `diary.md`
- Flexible matching — works with various diary formats
- Falls back gracefully if date not found

### Pattern Extraction
Uses regex to find structured entries:
- `Work Block (\d+)` — Counts unique work blocks
- `**Key Insight:** (.+)` — Extracts insights
- `Files Created: (.+)` — Lists new files
- `SESSION COMPLETE` — Counts session completions
- `**Value:** (.+)` — Captures value statements

### Output Formatting
- Bullet lists for insights/files/values
- Truncates long entries (80 chars + "...")
- Limits to top 5 insights, 5 files, 3 values (avoid overwhelming output)

---

## Use Cases

### 1. Morning Briefing
```bash
# What happened yesterday?
python3 tools/highlights.py --days 2
```

### 2. Weekly Review
```bash
# Loop through last 7 days
for day in {1..7}; do
  echo "=== Day $day ==="
  python3 tools/highlights.py -d $day
done
```

### 3. Activity Reports
```python
# Use as library
from tools.highlights import extract_highlights

data = extract_highlights(days_back=1)
print(f"Completed {data['work_blocks']} work blocks")
```

### 4. Moltbook Summaries
Extract highlights → auto-post daily summary to Moltbook.

---

## Integration

### In Cron Jobs
Daily highlight generator:
```json
{
  "schedule": {"kind": "cron", "expr": "0 18 * * *", "tz": "UTC"},
  "payload": {
    "kind": "systemEvent",
    "text": "python3 tools/highlights.py > workspace/daily-highlight.txt && cat workspace/daily-highlight.txt"
  }
}
```

### With Other Tools
- **`diary-digest.py`** — Full diary analysis (trends over time)
- **`daily-report.py`** — Comprehensive daily report
- **`self-improvement-loop.py`** — Velocity tracking + insights

---

## Customization

### Add New Patterns
Edit the regex patterns in `extract_highlights()`:
```python
# Extract new pattern
achievements = re.findall(r"\*\*Achievement:\*\* (.+)", today_section)
```

### Change Output Format
Modify `format_highlights()` to match your preference:
```python
# JSON output instead
import json
return json.dumps(data, indent=2)
```

### Adjust Truncation
Change the `[:80]` slice to show more/less text.

---

## Why This Tool?

**Problem:** `diary.md` grows to thousands of lines. Finding "what did I actually do today?" requires scrolling through raw logs.

**Solution:** One command extracts the signal from the noise — work blocks, insights, files, values. No manual summarization needed.

**Impact:**
- Quick retrospectives without re-reading entire diary
- Pattern extraction for self-improvement loops
- Activity summaries for reports or posts
- Automated daily/weekly reviews

---

## Files Read

- `diary.md` (primary data source)

---

## Related Tools

- **`diary-digest.py`** — Full diary analysis with trends
- **`daily-report.py`** — Comprehensive daily reporting
- **`agent-digest.py`** — Cross-agent activity summaries
- **`self-improvement-loop.py`** — Velocity + insight analysis

---

**Maintained by:** Nova ✨
**Last updated:** 2026-02-02
