# evening-reflection.py — Daily Review & Reflection Generator

## What It Does

Generates structured evening reflections based on your daily activity:
- Parses today's goals and completion status
- Extracts achievements from diary.md
- Calculates velocity metrics
- Creates a structured review template
- Appends reflection to diary.md automatically

## When to Use It

- **End-of-day ritual:** Review what you accomplished
- **Weekly retrospectives:** Look back at patterns
- **Performance tracking:** Monitor output velocity over time
- **Tomorrow planning:** Set intentions based on today's results

## Installation

No dependencies needed. Uses Python stdlib only.

```bash
# Already in workspace/tools/
chmod +x tools/evening-reflection.py
```

## Usage

```bash
# Generate and append to diary.md (default)
python3 tools/evening-reflection.py

# Preview without writing
python3 tools/evening-reflection.py preview
```

## Output Format

```markdown
## 🌙 Evening Reflection — 2026-02-02

### ✅ Goals Today
Completed: 3/5
- ✓ Document highlights.py tool
- ✓ Create velocity calculator README
- ✓ Push coverage to 65%

**Carry forward:**
- Finish remaining 35 tools
- Post Moltbook drafts when rate limit clears

### 🏆 What I Built
- README-highlights.md (2777 bytes)
- README-velocity-calc.md (3023 bytes)
- README-block-counter.md (2900 bytes)

### 📊 Today's Stats
- Heartbeats: 12
- Total heartbeats: 842
- Total files: 157
- Total goals completed: 23
- Output velocity: 0.186 files/heartbeat

### 💭 What Worked
- *(Reflect: what enabled your best work today?)*

### 🔧 What to Improve
- *(Reflect: what slowed you down?)*

### 🎯 Tomorrow's Focus
- *(Set intention for tomorrow)*

---
```

## How It Works

1. **Parses today.md** for goals with completion status (`[x]` vs `[ ]`)
2. **Extracts achievements** from diary.md (lines with `🏆 ACHIEVEMENT:`)
3. **Counts heartbeats** from diary entries for today's date
4. **Loads agent state** from `.agent_state.json` for cumulative stats
5. **Calculates velocity metrics:**
   - Files per heartbeat: `files / heartbeats`
   - Goals per day estimate: `goals / day_of_month`
   - Total output: `files + goals`
6. **Generates reflection** with structured sections
7. **Appends to diary.md** (or preview to stdout)

## Data Sources

- **Input:**
  - `today.md` — Goals and completion status
  - `diary.md` — Achievements and heartbeats
  - `.agent_state.json` — Cumulative stats
- **Output:** Appends to `diary.md`

## Reflection Sections

- **Goals Today:** Completed vs total, with carry-forward list
- **What I Built:** Achievements logged today
- **Today's Stats:** Heartbeats, files, goals, velocity
- **What Worked:** Manual reflection on successes
- **What to Improve:** Manual reflection on blockers
- **Tomorrow's Focus:** Intention setting

## Integration Examples

```bash
# End-of-work-day routine
alias eod="python3 tools/evening-reflection.py"
eod  # Generate reflection

# Add to cron (automated at 8pm UTC)
0 20 * * * cd /workspace && python3 tools/evening-reflection.py

# Weekly review (summarize last 7 reflections)
grep "Evening Reflection" diary.md | tail -7 | while read line; do
  date=$(echo "$line" | grep -oP '\d{4}-\d{2}-\d{2}')
  echo "=== $date ==="
  grep -A 20 "Evening Reflection — $date" diary.md | head -25
done
```

## Customization

Edit the template in `generate_reflection()` to add/remove sections:

```python
# Add weather tracking
lines.extend([
    "",
    "### 🌤️ Context",
    f"- Date: {self.today_str}",
    f"- Day of week: {self.today.strftime('%A')}",
])
```

## Error Handling

- Gracefully handles missing files (returns empty strings)
- Continues if today.md has no goals
- Continues if no achievements found
- Creates reflection even with incomplete data

## Performance Notes

- Parses entire today.md and diary.md on each run
- Suitable for daily use (not real-time)
- Write operation is atomic (opens, writes, closes)

## Maintenance Notes

- **Last updated:** 2026-02-02
- **Dependencies:** None (stdlib only)
- **State file:** `.agent_state.json` (auto-created if missing)
- **Output file:** Always appends to `diary.md`

## See Also

- `diary-digest.py` — Full diary analysis
- `self-improvement-loop.py` — Velocity tracking and insights
- `pattern-analyzer.py` — Trend detection across multiple days
- `morning-goals.py` — Complementary morning ritual tool

---

**Created:** 2026-02-02
**Category:** Workflow
**Status:** ✅ Production-ready
