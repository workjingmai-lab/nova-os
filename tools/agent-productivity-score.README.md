# agent-productivity-score.py

**Calculate productivity score from diary/heartbeat logs.**

## What It Does

Analyzes timestamped diary entries to calculate a productivity score (0-100) based on:
- **Volume** — Total entries (up to 40 pts)
- **Consistency** — Active days (up to 30 pts)
- **Completion** — Completed tasks vs total (up to 30 pts)

**Value:** Quantifies productivity over time, tracks improvement, identifies peak hours.

## Usage

### Analyze Diary File
```bash
python3 tools/agent-productivity-score.py diary.md
```

### Analyze via Stdin
```bash
cat diary.md | python3 tools/agent-productivity-score.py --stdin
```

## Output Example

```
==================================================
📊 AGENT PRODUCTIVITY REPORT
==================================================

Overall Score: 78/100
Tier: 🌟 Elite

📈 METRICS
  Total Entries: 523
  Work Blocks: 451
  Completed Tasks: 387
  Active Days: 5

📝 ENTRY TYPES
  WORK_BLOCK       451 ████████████████████████
  GOAL_COMPLETE     38  █████
  HEARTBEAT         34  ████

⏰ ACTIVITY BY HOUR
  Peak Activity: 13:00 (89 entries)

==================================================
```

## Productivity Tiers

| Score | Tier | Description |
|-------|------|-------------|
| 90+ | 🏆 Legendary | Top 1% productivity |
| 75+ | 🌟 Elite | Consistent high output |
| 60+ | ⚡ Pro | Above average velocity |
| 40+ | 🔥 Active | Regular engagement |
| 20+ | 💪 Building | Developing habits |
| <20 | 🌱 Starting | Just getting started |

## How It Works

1. **Parses entries** — Extracts timestamped entries: `[TYPE] YYYY-MM-DDThh:mm:ssZ`
2. **Calculates metrics** — Total entries, work blocks, completions, active days, hourly distribution
3. **Computes score** — Weighted formula: volume (40%) + consistency (30%) + completion (30%)
4. **Assigns tier** — Maps score to productivity tier

## Scoring Formula

```
Score = Volume (0-40) + Consistency (0-30) + Completion (0-30)

Volume = min(entries / 50, 1.0) × 40
Consistency = min(unique_days / 7, 1.0) × 30
Completion = min(completed / entries × 2, 1.0) × 30
```

**Normalization:** 50 entries = full volume score, 7 active days = full consistency score.

## Entry Format

The tool expects timestamped entries in this format:
```markdown
[WORK_BLOCK] 2026-02-03T13:53:00Z
✅ Created README for work-pattern-analyzer.py
---
[HEARTBEAT] 2026-02-03T14:00:00Z
Checked calendar, no urgent items
---
```

Key elements:
- `[TYPE]` — Entry type in brackets (any string)
- Timestamp — ISO 8601 format (ends with Z)
- Body — Entry content (until `---` or next entry)

## Dependencies

- Python 3.x
- No external packages required (stdlib only: re, datetime, collections)

## Related Tools

- `work-pattern-analyzer.py` — Time-of-day productivity patterns
- `daily-output-tracker.py` — Track daily output over time
- `velocity-predictor.py` — Predict completion times

## Why This Matters

**What gets measured gets managed.**

This tool turns raw diary entries into a quantified productivity score, enabling:
- **Self-awareness** — Know your actual productivity level
- **Progress tracking** — See score increase over time
- **Goal setting** — Aim for next tier (e.g., Pro → Elite)
- **Peak hours** — Identify when you're most productive

**Nova's use case:** Tracks productivity across 950+ work blocks, maintains Elite tier through consistent execution.

---

**Last updated:** 2026-02-03
**Category:** Analytics
**Status:** Core tool — self-quantification for productivity optimization
