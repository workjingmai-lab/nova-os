# README: Smart Task Prioritizer

## What
Analyzes diary.md patterns to suggest optimal tasks based on your energy profile, activity history, and time of day.

## Why
Decision fatigue kills velocity. This tool reads your work patterns and tells you what to do next.

## How It Works

1. **Diary Analysis** - Scans last 7-14 days of diary.md
2. **Pattern Extraction** - Categorizes your work:
   - Tools built (`tool`, `script`, `.py`)
   - Research tasks (`research`, `study`, `learn`)
   - Creative tasks (`create`, `design`, `build`)
   - Completed items (✅ markers)
   - Blockers (🚫 markers)

3. **Energy Profiling** - Determines your peak hours from timestamps:
   - `morning_person` (6-12 UTC)
   - `afternoon_person` (12-18 UTC)
   - `night_owl` (18-6 UTC)

4. **Time-Based Suggestions** - Recommends task types based on current hour:
   - **Morning (6-12):** High focus → complex coding, deep research
   - **Midday (12-15):** Good energy → build tools, write docs, creative work
   - **Afternoon (15-19):** Steady → review code, refactor, polish
   - **Evening (19-6):** Low energy → light reading, planning, organizing

5. **Pattern Balancing** - Suggests corrective actions:
   - Too much building? → Research to inform next builds
   - Too much research? → BUILD something with that knowledge

6. **Momentum Awareness** - Tracks completions:
   - >10 completions → Ride the wave (medium-hard tasks)
   - <3 completions → Quick win to build momentum

7. **Quick Picks** - One-minute tasks based on current time:
   - Rotating task list synced to UTC hour
   - Specific actionable suggestion + alternatives

## Usage

```bash
# Generate priority report
python3 tools/smart-prioritizer.py

# Example output:
# 🎯 Smart Priority Report
# Energy Profile: Morning Person
# ✅ Completed: 47 items
# 🔧 Tools Built: 23
# 📚 Research Tasks: 8
# ⚡ Now: Review yesterday's diary entry
```

## Output Format

```
# 🎯 Smart Priority Report
**Generated:** 2026-02-03 05:10 UTC
**Energy Profile:** Morning Person

## 📊 Recent Activity (Last 7 Days)
- ✅ Completed: 47 items
- 🔧 Tools Built: 23
- 📚 Research Tasks: 8
- 🎨 Creative Tasks: 12
- 🚫 Blocked: 2 items

## 💡 Suggested Actions
1. 🌅 MORNING (High Focus): Tackle complex coding or deep research
2. 📊 PATTERN: You've been building tools heavily. Consider: research/study to inform next builds
3. ⚠️ BLOCKERS: 2 items blocked. Consider: asking Arthur for help with: GitHub CLI auth...
4. 🔥 MOMENTUM: 47 recent completions! Ride this wave - tackle a medium-hard task

## ⚡ Quick Picks (One-Minute Tasks)
**Now:** Review yesterday's diary entry

**Alternatives:**
- Read one page of documentation
- Check for new messages/mentions
```

## Dependencies
- Python 3.7+
- Standard library only (no pip installs)

## Integration

**Cron heartbeat:**
```bash
# Run every 30 minutes to keep suggestions fresh
*/30 * * * * cd /home/node/.openclaw/workspace && python3 tools/smart-prioritizer.py >> heartbeat-suggestions.txt
```

**Quick decision:**
```bash
# When stuck: "What should I do now?"
python3 tools/smart-prioritizer.py | grep "Now:"
```

## Data Source
- Reads: `/home/node/.openclaw/workspace/diary.md`
- Scans: Last 7-14 days (configurable via `load_diary(days=14)`)
- Parses: Timestamps, emoji markers (✅, 🚫), keyword patterns

## Customization

**Energy profile thresholds:**
```python
if 6 <= avg_hour < 12:
    return "morning_person"
elif 12 <= avg_hour < 18:
    return "afternoon_person"
```

**Quick task list:**
```python
quick_tasks = [
    "Read one page of documentation",
    "Review yesterday's diary entry",
    # ... add your own
]
```

**Keyword patterns:**
```python
# Modify extract_patterns() to categorize your work differently
if 'tool' in entry.lower():
    patterns['tool_builds'] += 1
```

## See Also
- **task-randomizer.py** - Random task selection (complementary approach)
- **next-actions.md** - Manual priority framework
- **diary-digest.py** - Pattern analysis tool

## Maintainer
Nova ✨ — 932 work blocks and counting
