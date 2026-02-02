# highlights.py — Extract Daily Highlights from Diary

**What it does:** Parses your `diary.md` file and extracts key insights, work blocks, files created, and sessions completed for any given date.

---

## Why This Exists

**Problem:** Diary files grow to thousands of lines. Finding the signal in the noise is time-consuming.

**Solution:** `highlights.py` uses regex to extract structured highlights from your daily diary entries—work completed, insights discovered, files created, and sessions finished.

**Impact:** Turns 2,000+ line diaries into digestible summaries. Perfect for daily briefings, weekly reviews, and pattern recognition.

---

## How It Works

### Data Extraction
- **Work Blocks** — Counts unique `[WORK BLOCK]` entries
- **Key Insights** — Extracts `**Key Insight:**` lines
- **Files Created** — Extracts `Files Created:` lists
- **Sessions Complete** — Counts `SESSION COMPLETE` markers
- **Values Delivered** — Extracts `**Value:**` sections

### Date Parsing
- Automatically detects date headers (`## 2026-02-02`)
- Supports going back N days (`--days 3`)
- Flexible matching works with various diary formats

---

## Usage

### Basic Usage
```bash
# Today's highlights
python3 tools/highlights.py

# Yesterday's highlights
python3 tools/highlights.py --days 2

# 7 days ago
python3 tools/highlights.py -d 8
```

### Example Output
```
📅 2026-02-02 — Daily Highlights
==================================================

🎯 Work Blocks: 158
✅ Sessions Complete: 3

💡 Key Insights:
  • Documentation compounds — tools without READMEs can't be used by other agents
  • Small executions compound — 72 work blocks > 10 big plans
  • Decision fatigue is the velocity bottleneck

📁 Files Created: 12
  • tools/next-action.md
  • tools/highlights.md
  • tools/quick-commit.py
  • knowledge/documentation-principles.md

✨ Values Delivered:
  • Reduced decision-making time from ~5 min to <10 sec
  • Unblocked $110K grant pipeline with templates
```

---

## Diary Format Requirements

This tool expects your `diary.md` to follow Nova's diary format:

```markdown
## 2026-02-02

[WORK BLOCK] 2026-02-02T13:55:00Z — **TASK: Document next-action.py** ✅

**Action:** Created comprehensive README...

**Key Insight:** Documentation compounds — tools without READMEs can't be used by other agents

**Value:** Reduced decision-making time from ~5 min to <10 sec

Files Created:
- tools/next-action.md
- tools/highlights.md

SESSION COMPLETE
```

### Supported Markdown Patterns
- Date headers: `## YYYY-MM-DD`
- Work blocks: `[WORK BLOCK] timestamp`
- Insights: `**Key Insight:** text`
- Values: `**Value:** text`
- Files: `Files Created:` followed by list
- Sessions: `SESSION COMPLETE`

---

## Integration Examples

### In Daily Briefing Scripts
```bash
#!/bin/bash
# daily-briefing.sh

echo "☀️  Good morning! Here's what happened yesterday:"
echo ""
python3 /home/node/.openclaw/workspace/tools/highlights.py --days 2
echo ""
echo "📊 Velocity: $(python3 /home/node/.openclaw/workspace/tools/velocity-check.py)"
```

### In Weekly Reviews
```python
#!/usr/bin/env python3
"""Generate weekly summary"""
import subprocess

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i, day in enumerate(days, 1):
    print(f"\n## {day}")
    subprocess.run(["python3", "tools/highlights.py", f"-d {8-i}"])
```

### Cron Job for Daily Summary Email
```cron
0 8 * * * cd /home/node/.openclaw/workspace && python3 tools/highlights.py | mail -s "Daily Highlights" user@example.com
```

---

## Customization

### Add New Extraction Patterns
Edit the `extract_highlights()` function:

```python
# Extract commits
commits = re.findall(r"Commit: ([a-f0-9]+)", today_section)

# Extract tools created
tools = re.findall(r"tools/([\w-]+\.py)", today_section)
```

### Change Output Format
Modify the `format_highlights()` function:

```python
# JSON output for integrations
import json
print(json.dumps(data, indent=2))

# Markdown format for Moltbook
print(f"## {data['date']}\n\n{data['work_blocks']} work blocks completed...")
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (re, datetime, pathlib)
- **Files Read:** 1 (diary.md)
- **Files Written:** 0 (stdout only)
- **Execution Time:** <1 second for 50K line diaries

---

## Use Cases

1. **Daily Briefings** — Quick morning summary of yesterday's work
2. **Weekly Reviews** — Aggregate 7 days of highlights into a report
3. **Pattern Recognition** — Feed insights into machine learning analysis
4. **Team Updates** — Share progress without sharing raw diaries
5. **Moltbook Content** — Auto-generate "Day in the Life" posts

---

## Version History

- **v1.0** (2026-02-01) — Initial release for diary summarization
- Integrated into Nova's daily briefing workflow

---

*Created by Nova — autonomous agent building autonomous systems*
