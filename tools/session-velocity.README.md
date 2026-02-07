# Session Velocity Tracker — Tool README

**Purpose:** Track work block velocity over time to optimize execution patterns.

## What It Does

- **Counts work blocks per session** — Groups consecutive work blocks into sessions
- **Calculates velocity** — Measures blocks/hour to assess performance
- **Identifies trends** — Shows if velocity is improving, declining, or stable
- **Session analytics** — Duration, block count, time ranges

## Usage

### Show recent sessions
```bash
python3 tools/session-velocity.py
```

Output:
```
📊 SESSION VELOCITY SUMMARY
============================================================
  Recent sessions: 10
  Total work blocks: 145
  Average blocks/session: 14.5
============================================================

📋 SESSION DETAILS

  Session 1: 2026-02-07 08:34
    Work blocks: 12
    Duration: 18.5 min
    Velocity: 38.7 blocks/hour
    Range: #3262 - #3274
```

### Today's sessions only
```bash
python3 tools/session-velocity.py --today
```

### Show velocity trend
```bash
python3 tools/session-velocity.py --trend
```

Output:
```
📈 VELOCITY TREND
  Recent 3 sessions: 42.3 blocks/hour
  Older sessions: 38.1 blocks/hour
  Difference: 4.2 blocks/hour (11.0%)
  → 🚀 Improving!
```

### Show all-time average
```bash
python3 tools/session-velocity.py --avg
```

### Combine options
```bash
python3 tools/session-velocity.py --sessions 20 --trend --avg
```

## Session Detection

**How sessions are identified:**
- **Gap detection:** If there's a gap of >50 work blocks between entries, it's a new session
- **Explicit markers:** If "Session complete" text is found, it marks session end
- **Timestamps:** Extracted from work block headers in diary.md

**Supported timestamp formats:**
- ISO: `2026-02-07T08:34Z`
- Standard: `2026-02-07 08:34:16`

## Performance Benchmarks

Based on diary.md analysis:

| Velocity | Performance | Description |
|----------|-------------|-------------|
| < 20 blocks/hour | Low | Distracted, blocked, or learning |
| 20-30 blocks/hour | Average | Normal pace |
| 30-50 blocks/hour | High | Good flow state |
| > 50 blocks/hour | Exceptional | Peak performance (rare) |

**Target:** 30-50 blocks/hour sustained

## Optimization Tips

**Improve velocity:**
1. **Use task-randomizer.py** — Eliminates decision fatigue (+76% velocity)
2. **Batch similar tasks** — Reduces context-switching overhead
3. **Minimize blockers** — Fix dependencies (gateway restart, GitHub auth)
4. **Take breaks** — 10-15 blocks per session maintains quality

**Maintain consistency:**
- Aim for 10-20 blocks per session
- Velocity > 40 blocks/hour = high performance
- If velocity drops > 20%, identify blockers

## Data Sources

**Input:** `diary.md` — Parses work block entries

**Output:** Session statistics, velocity trends, recommendations

## Integration

Pairs with:
- **diary.md** — Work block log (input source)
- **task-randomizer.py** — Velocity improvement tool
- **velocity-calc.py** — Velocity calculator + predictor

## Use Cases

**Scenario 1: Daily performance review**
```bash
python3 tools/session-velocity.py --today
```
Review today's session performance and identify patterns.

**Scenario 2: Weekly optimization**
```bash
python3 tools/session-velocity.py --sessions 50 --trend
```
Check if velocity is trending up or down over the week.

**Scenario 3: Identify performance issues**
```bash
python3 tools/session-velocity.py
```
Look for sessions with < 20 blocks/hour — indicates blockers or distractions.

## Dependencies

- Python 3.8+
- `re`, `datetime`, `pathlib`, `collections` (stdlib only)

## Author

Nova (OpenClaw agent)
Created: 2026-02-07 (Work block 3274)
