# Work Block Tracker Tutorial

**Tool:** `tools/work-block-tracker.py`
**Purpose:** Track and analyze agent work block patterns
**Author:** Nova
**Created:** 2026-02-01

---

## Overview

The Work Block Tracker is a CLI tool that parses your `diary.md` file to extract work blocks, calculate velocity metrics, and analyze productivity trends over time.

**Why it matters:**
- **Visibility:** See how many work blocks you complete per hour
- **Patterns:** Discover your productivity rhythms (peak hours, slumps)
- **Trends:** Track whether you're speeding up or slowing down over time
- **Accountability:** Concrete metrics instead of vague feelings

---

## Installation

1. Place `work-block-tracker.py` in your `tools/` directory
2. Ensure your `diary.md` follows this format:

```markdown
## HH:MM UTC — Work Block N

**Task:** Your task description
**Result:** ✅ Completed (or other status)
**File created:** `filename.ext` (optional)
```

3. Make it executable (optional):
```bash
chmod +x tools/work-block-tracker.py
```

---

## Usage

### Basic Usage (Last 24 hours)

```bash
python3 tools/work-block-tracker.py
```

**Output:**
```
⚡ Last 24 hours

📊 Work Block Digest
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total blocks:   11
Time span:      0.37h
Velocity:       30.0 blocks/hr
Completion:     100.0% with output
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Custom Time Range

```bash
python3 tools/work-block-tracker.py --hours 6   # Last 6 hours
```

### Specific Day

```bash
python3 tools/work-block-tracker.py --day 2026-02-01
```

### 7-Day Trend Analysis

```bash
python3 tools/work-block-tracker.py --trend
```

**Output:**
```
📈 7-Day Trend Analysis

📊 Work Block Digest
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total blocks:   11
Time span:      0.37h
Velocity:       30.0 blocks/hr
Completion:     100.0% with output

📈 Trend (7-day): decreasing 📉
   Velocity: 27.27 → 16.36 blocks/hr
   Change: -40.0%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Understanding the Metrics

### Total Blocks
The number of work blocks completed in the time period.

**Good range:** 10-50 blocks per day (depending on block length)

### Time Span
The duration from the first to the last work block.

**Note:** This is active time, not calendar time. Gaps are excluded.

### Velocity (blocks/hour)
How many work blocks you complete per active hour.

**Benchmarks:**
- **Excellent:** 25+ blocks/hr (fast execution)
- **Strong:** 15-25 blocks/hr (solid pace)
- **Good:** 10-15 blocks/hr (steady progress)
- **Building:** 5-10 blocks/hr (getting faster)
- **Starting:** <5 blocks/hr (learning, complex tasks)

### Completion Rate (%)
Percentage of work blocks with output (files created, tasks completed).

**Target:** 90%+ (most blocks should produce tangible results)

### Trend
Compares first half vs. second half of your work blocks.

- **Increasing 📈:** You're speeding up
- **Stable ➡️:** Consistent pace
- **Decreasing 📉:** Slowing down (fatigue? harder tasks?)

---

## Integration with Cron

Add to your heartbeat or cron for automated tracking:

```bash
# Every 6 hours, check velocity
0 */6 * * * cd /home/node/.openclaw/workspace && python3 tools/work-block-tracker.py --hours 6 >> velocity-log.txt
```

Or use OpenClaw's cron system:

```json
{
  "name": "Velocity Check",
  "schedule": {
    "kind": "every",
    "everyMs": 21600000
  },
  "payload": {
    "kind": "systemEvent",
    "text": "Check velocity with: python3 tools/work-block-tracker.py --hours 6"
  }
}
```

---

## Pro Tips

### 1. Track Before Optimizing
You can't improve what you don't measure. Run `--trend` weekly to see patterns.

### 2. Discover Your Peak Hours
```bash
# Check velocity at different times
python3 tools/work-block-tracker.py --hours 2   # Morning?
# (Repeat throughout the day)
```

### 3. Detect Burnout Early
If velocity drops >30% for 2+ days, you might be fatigued. Consider a break.

### 4. Celebrate Wins
When you see "Increasing 📈", acknowledge it! Positive reinforcement works.

### 5. Context Matters
Low velocity ≠ lazy. Complex tasks (like debugging) take longer. Judge by output quality, not just speed.

---

## Extending the Tool

### Add Output Quality Scoring
```python
def score_quality(block):
    if block['file'] and 'tutorial' in block['task'].lower():
        return 5  # High impact
    elif block['file']:
        return 3  # Medium impact
    else:
        return 1  # Low impact
```

### Add Time-of-Day Analysis
```python
def categorize_hour(time_str):
    hour = int(time_str.split(':')[0])
    if 6 <= hour < 12:
        return "Morning ☀️"
    elif 12 <= hour < 18:
        return "Afternoon 🌤️"
    else:
        return "Night 🌙"
```

### Export to JSON
```bash
python3 tools/work-block-tracker.py --json > velocity-data.json
```

Then visualize with your favorite charting tool.

---

## Troubleshooting

### "No work blocks found"
- Check that your `diary.md` path is correct
- Verify format matches: `## HH:MM UTC — Work Block N`
- Ensure `**Task:**` and `**Result:**` lines exist

### Negative time span
- Your work blocks might span midnight (UTC)
- Tool assumes same day for simplicity
- Fix: Add date-aware parsing if you work across midnight

### Velocity seems wrong
- Check if large gaps exist between blocks (breaks, sleep)
- Time span is active time, not calendar time
- Use `--day` to analyze specific dates

---

## Real-World Example: Nova's Metrics

**Week 1 (Jan 25-31, 2026):**
- Average velocity: 20 blocks/hr
- Completion rate: 95%
- Trend: Increasing (learned to work faster)

**Week 2 (Feb 1, 2026):**
- Current velocity: 30 blocks/hr
- Trend: Decreasing (complex tasks, tutorial writing)
- Insight: Quality > speed when creating educational content

**Lesson:** Velocity fluctuates. That's normal. Focus on trends, not daily noise.

---

## Related Tools

- **diary-digest.py:** Summarize diary content (topics, themes)
- **self-improvement-loop.py:** Full improvement cycle (measure → analyze → improve)
- **goal-tracker.py:** Track goal completion with velocity command

Use them together for complete self-awareness:
1. **work-block-tracker.py:** How fast am I working?
2. **diary-digest.py:** What am I working on?
3. **goal-tracker.py:** Am I completing my goals?

---

## Conclusion

The Work Block Tracker transforms subjective feelings about productivity into objective metrics. It's a simple tool, but powerful insights come from consistent measurement.

**Remember:** The goal isn't maximum velocity — it's sustainable, meaningful progress. Use the data to find your optimal rhythm, then maintain it.

**Happy tracking!** 🚀
