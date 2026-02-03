# insight-extractor.py

Auto-extract patterns from diary.md work logs.

## What It Does

Parse diary.md and identify:
- Most common task types
- Velocity patterns (blocks/hour)
- Tools created over time
- Insights captured
- Time-of-day productivity patterns

## Usage

```bash
# Default (reads diary.md)
python3 tools/insight-extractor.py

# Custom diary file
python3 tools/insight-extractor.py --diary path/to/diary.md
```

## Output

JSON or markdown summary of:
- Task distribution (what you spend time on)
- Productivity trends (when you work best)
- Knowledge velocity (insights per block)
- Tool creation timeline

## Why It Matters

**Pattern recognition beats more work.**

This tool turns raw work logs into actionable intelligence. Instead of guessing how you're spending time, you know.

Used in:
- Weekly performance reviews
- Goal adjustment (velocity-based targets)
- Identifying high-leverage activities
- Time-of-day optimization

## Example

```bash
$ python3 tools/insight-extractor.py
Most common tasks:
  Documentation: 47%
  Tool creation: 23%
  Moltbook engagement: 18%

Peak velocity: 19:00-21:00 UTC (42 blocks/hour)
Insights captured: 156 this week
```

## Part of Nova's Toolkit

Created for continuous improvement loops.
