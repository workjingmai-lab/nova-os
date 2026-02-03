# velocity-check.py

Quick count of tasks completed today from `diary.md`.

## What It Does

`velocity-check.py` scans your `diary.md` for entries with today's date and completion markers (✅, Done, Completed), then outputs the count.

## Usage

```bash
python3 tools/velocity-check.py
```

## Example Output

```bash
$ python3 tools/velocity-check.py
🚀 Tasks completed today: 47
```

## Patterns Matched

The tool looks for diary entries matching these patterns:

- `2026-02-02 ... ✅` — Tasks with checkmarks
- `2026-02-02 ... Done` — Explicit "Done" marker
- `2026-02-02 ... Completed` — Explicit "Completed" marker

## Use Cases

- **Quick velocity check** — How much have I done today?
- **Motivation tracking** — See progress in real-time
- **End-of-day review** — Count completed work blocks
- **Baseline setting** — Understand your daily capacity

## Why It Exists

**Instant feedback.** Sometimes you need a quick number to know if you're on track. No complex analytics, no charts—just "how many things did I finish today?"

## Limitations

- **Simple pattern matching** — Only looks for basic completion markers
- **Single-day view** — Doesn't show trends or averages
- **No categorization** — Counts all tasks equally

## Better Alternatives (for deep analytics)

- `self-improvement-loop.py` — Velocity tracking with insights and trends
- `daily-output-tracker.py` — Comprehensive productivity metrics
- `work-block-miner.py` — Pattern analysis from work blocks

## See Also

- `self-improvement-loop.py` — Advanced velocity tracking and insights
- `block-counter.py` — Work block statistics
- `daily-report.py` — Full daily summaries with velocity metrics

---

**Version:** 1.0  
**Created:** 2025-01-31  
**Category:** Analytics / Productivity
