# work-pattern-analyzer.py

Analyze your work patterns by time of day to optimize when to do different types of work.

## What It Does

`work-pattern-analyzer.py` scans `diary.md` for work blocks with timestamps, categorizes tasks by type, and generates insights about your productivity patterns:

- **Hourly activity breakdown** — When you work most
- **Peak productivity hours** — Your best 5 hours
- **Task type distribution** — What you spend time on
- **Schedule optimization** — Best hours for building vs content vs analysis

## Usage

```bash
python3 tools/work-pattern-analyzer.py
```

## Example Output

```
============================================================
📊 WORK PATTERN ANALYZER — Time Distribution
============================================================

⏰ HOURLY ACTIVITY (UTC):
------------------------------------------------------------
00:00 | ████████████████    | 14 blocks | Top: Building (8)
01:00 | ██████████          | 10 blocks | Top: Content (6)
02:00 | ████████            |  8 blocks | Top: Documentation (5)
...

🔥 PEAK PRODUCTIVITY HOURS:
------------------------------------------------------------
  00:00 — 14 blocks (mostly Building)
  01:00 — 10 blocks (mostly Content)
  23:00 —  9 blocks (mostly Analysis)
...

📈 TASK TYPE DISTRIBUTION:
------------------------------------------------------------
  Building       | ████████████████   | 142 ( 42.3%)
  Documentation  | ████████          |  67 ( 19.9%)
  Content        | ██████            |  54 ( 16.1%)
  Analysis       | ████              |  38 ( 11.3%)
  Planning       | ██                |  20 (  5.9%)
  Other          | ██                |  15 (  4.5%)

💡 INSIGHTS:
------------------------------------------------------------
  • Peak hour: 00:00 UTC (14 blocks)
  • Best for building: 00:00, 23:00, 22:00
  • Best for content: 01:00, 02:00, 15:00
  • Total analyzed: 336 blocks
```

## Task Categories

The tool auto-categorizes work by keywords in task titles:

| Category | Keywords |
|----------|----------|
| **Building** | tool, script, built |
| **Content** | moltbook, post, draft |
| **Planning** | goal, plan |
| **Analysis** | analyz, pattern, review |
| **Documentation** | docum, update, ref |
| **Other** | Everything else |

## Diary Format Required

The tool expects work blocks in this format (standard diary format):

```markdown
### 20:15Z — Work Block 728 — Task title here
```

Timestamps must be in UTC with `Z` suffix.

## Use Cases

- **Schedule optimization** — Do building work during peak hours
- **Energy matching** — Save creative work for high-energy times
- **Trend analysis** — Are your patterns changing over time?
- **Self-awareness** — Understand when you're most productive

## Why This Matters

**Work with your biology, not against it.** 

If you know you do your best building work at midnight, schedule accordingly. If content flows better in the morning, block that time for writing. Patterns are power—use them.

## Limitations

- **UTC only** — All times analyzed as UTC
- **Keyword matching** — Simple categorization, may miscategorize complex tasks
- **No trends over time** — Shows aggregate, not week-by-week changes

## See Also

- `diary-digest.py` — Pattern analysis from diary logs
- `work-block-miner.py` — Extract insights from work patterns
- `self-improvement-loop.py` — Velocity and productivity metrics

---

**Version:** 1.0  
**Created:** 2026-02-01  
**Category:** Analytics / Productivity
