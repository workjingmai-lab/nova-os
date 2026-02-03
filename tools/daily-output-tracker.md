# daily-output-tracker.py — Productivity Metrics from Diary

**Purpose:** Analyze diary.md to extract daily productivity metrics (tasks, files, tools, posts, learnings).

**Created:** Week 1 (2026-01-31)
**Usage:** ~10-15 times (velocity tracking)

## What It Does

- **Parses diary entries** — Extracts metrics from timestamped entries
- **Tracks 7 metrics** — Tasks completed, files created, tools built, posts published, learnings logged, errors fixed, word count
- **Generates 7-day report** — Summary with totals and velocity
- **Calculates velocity** — Tasks/day average for last 7 days
- **Saves report** — `reports/daily-output-latest.md`

## Usage

```bash
python3 tools/daily-output-tracker.py
```

## Output

**Console:**
```
# 📊 Daily Output Report
Generated: 2026-02-02 19:30 UTC

## Summary by Day
### 2026-02-01
- Tasks: 15 | Files: 8 | Tools: 3 | Posts: 2 | Learnings: 5 | Words: 1245

[... more days ...]

## 📈 7-Day Totals
- **Tasks Completed:** 89
- **Files Created:** 45
- **Tools Built:** 12
- **Posts Published:** 8
- **Learnings Logged:** 23
- **Errors Fixed:** 7
- **Total Words:** 8,432

**Velocity:** 12.7 tasks/day
```

## Metrics Tracked

| Metric | Detection Pattern |
|--------|-------------------|
| Tasks completed | `[x]`, `✅`, `✓`, completed, finished, done |
| Files created | created.*.(py|md|js|ts|json|yml|yaml|sh) |
| Tools built | built.*tool, created.*script, wrote.*function |
| Posts published | posted.*on, published.*post, moltbook |
| Learnings | learned, discovered, realized, understood |
| Errors fixed | fixed, resolved, debugged, corrected |
| Word count | Split by whitespace |

## Dependencies

- Python 3.8+
- pathlib, re, collections (stdlib only)

## Why This Matters

Velocity tracking reveals productivity patterns:
- **High task count + low tools built** → Maintenance mode
- **High word count + low tasks** → Documentation phase
- **Consistent velocity** → Sustainable workflow
- **Dropping velocity** → Burnout risk or blocker

## Related Tools

- `self-improvement-loop.py` — Advanced velocity analysis + insights
- `diary-digest.py` — Pattern recognition from logs
- `goal-tracker.py` — Goal progress tracking
