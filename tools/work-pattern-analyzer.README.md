# work-pattern-analyzer.py

**Analyze your productivity patterns by time of day.**

## What It Does

Reads `diary.md` and extracts work blocks with timestamps, then:
- Groups blocks by hour (UTC)
- Categorizes tasks (Building, Content, Planning, Analysis, Documentation, Other)
- Shows hourly activity distribution
- Identifies peak productivity hours
- Recommends optimal times for different work types

**Value:** Helps you schedule high-focus work during your peak hours and administrative tasks during low-energy periods.

## Usage

```bash
python3 tools/work-pattern-analyzer.py
```

## Output Example

```
📊 WORK PATTERN ANALYZER — Time Distribution
============================================================

⏰ HOURLY ACTIVITY (UTC):
------------------------------------------------------------
13:00 | ████████████████  | 45 blocks | Top: Building (28)
14:00 | ██████████        | 32 blocks | Top: Content (18)
15:00 | █████████████     | 38 blocks | Top: Building (22)
...

🔥 PEAK PRODUCTIVITY HOURS:
------------------------------------------------------------
  13:00 — 45 blocks (mostly Building)
  15:00 — 38 blocks (mostly Building)
  14:00 — 32 blocks (mostly Content)

📈 TASK TYPE DISTRIBUTION:
------------------------------------------------------------
  Building       | ██████████████     | 145 ( 45.2%)
  Content        | ████████          |  82 ( 25.5%)
  Documentation  | ████              |  42 ( 13.1%)
  Analysis       | ██                |  28 (  8.7%)
  Planning       | ███               |  25 (  7.8%)

💡 INSIGHTS:
------------------------------------------------------------
  • Peak hour: 13:00 UTC (45 blocks)
  • Best for building: 13:00, 15:00, 16:00
  • Best for content: 14:00, 17:00, 18:00
  • Total analyzed: 322 blocks
```

## How It Works

1. **Parses diary.md** — Extracts work blocks using pattern: `### HH:MMZ — Work Block XXX — Title`
2. **Categorizes tasks** — Keyword-based categorization (tool/script → Building, post/draft → Content, etc.)
3. **Groups by hour** — Aggregates activity per hour
4. **Generates insights** — Identifies patterns and optimal scheduling

## Dependencies

- Python 3.x
- No external packages required (uses only stdlib: re, datetime, collections)

## Data Source

- **Input:** `/home/node/.openclaw/workspace/diary.md`
- **Pattern expected:** `### HH:MMZ — Work Block XXX — Task Title`
- **Timezone:** UTC (extracts hour from HH:MMZ format)

## Task Categories

| Category | Keywords |
|----------|----------|
| Building | tool, script, built |
| Content | moltbook, post, draft |
| Planning | goal, plan |
| Analysis | analyz, pattern, review |
| Documentation | docum, update, ref |
| Other | (fallback) |

## Related Tools

- `daily-report.py` — Generates daily summaries
- `velocity-predictor.py` — Predicts completion times
- `tool-usage-analysis.py` — Analyzes which tools you use most

## Why This Matters

**Self-awareness = Optimization**

Knowing when you're naturally most productive helps you:
- Schedule deep work during peak hours
- Batch administrative tasks during low-energy times
- Align task types with your cognitive rhythms
- Identify burnout patterns (e.g., declining velocity after 6h)

This tool turns raw diary entries into actionable schedule intelligence.

---

**Last updated:** 2026-02-03
**Category:** Analytics
**Status:** Core tool — high value for productivity optimization
