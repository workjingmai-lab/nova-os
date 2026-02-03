# smart-prioritizer.py

**Intelligent task prioritization based on diary pattern analysis**

---

## What It Does

Analyzes your `diary.md` patterns to suggest optimal tasks based on:
- **Time of day** — Morning (high focus), Midday (creative), Afternoon (steady), Evening (low energy)
- **Activity patterns** — Tool builds vs research vs creative work balance
- **Completion momentum** — Ride high completion streaks, build momentum when low
- **Blocker awareness** — Flags blocked items needing attention
- **Energy profile** — Detects if you're a morning person, afternoon person, or night owl

---

## Why It Matters

**Eliminates decision fatigue** by suggesting the right task for the right moment. Instead of staring at a task list wondering "what should I do?", get data-driven suggestions that match your current energy level and recent work patterns.

**Features:**
- ✅ Pattern detection from diary entries (tools built, research, creative work)
- ✅ Energy profile analysis based on timestamp patterns
- ✅ Momentum-aware suggestions (ride streaks or build them back up)
- ✅ Blocker tracking with escalation prompts
- ✅ Quick-win rotation (different 1-minute tasks per hour)

---

## Usage

### Basic Priority Report
```bash
python3 tools/smart-prioritizer.py
```

**Sample Output:**
```
# 🎯 Smart Priority Report
**Generated:** 2026-02-02 20:07 UTC
**Energy Profile:** Afternoon Person

## 📊 Recent Activity (Last 7 Days)
- ✅ Completed: 127 items
- 🔧 Tools Built: 23
- 📚 Research Tasks: 8
- 🎨 Creative Tasks: 15
- 🚫 Blocked: 3 items

## 💡 Suggested Actions
1. 🌙 EVENING (Low Energy): Light reading, planning, organizing
2. 📊 PATTERN: You've been building tools heavily. Consider: research/study to inform next builds
3. 🔥 MOMENTUM: 127 recent completions! Ride this wave - tackle a medium-hard task

## ⚡ Quick Picks (One-Minute Tasks)
**Now:** Review a skill's SKILL.md

**Alternatives:**
- Read one page of documentation
- Review yesterday's diary entry
- Check for new messages/mentions
```

---

## How It Works

### Energy Profile Detection
Analyzes last 50 timestamps from `diary.md`:
- **Morning person (6-12):** High focus → complex coding, deep research
- **Afternoon person (12-15):** Good energy → build tools, write docs
- **Night owl (15+):** Steady/low → review, refactor, polish

### Pattern Balancing
Tracks the ratio of:
- **Tool builds** (`tool`, `script`, `.py` mentions)
- **Research tasks** (`research`, `study`, `learn`, `read`)
- **Creative tasks** (`create`, `design`, `build`, `wow`)

If one dominates, suggests rebalancing activities.

### Momentum Detection
- **High completions (>10):** Suggests medium-hard tasks to ride the wave
- **Low completions (<3):** Suggests quick wins to rebuild momentum

### Blocker Escalation
Tracks blocked items (`🚫` emoji) and prompts Arthur for help when blockers accumulate.

---

## Integration

### With Work Blocks
Add to your work block selection:
```bash
python3 tools/smart-prioritizer.py | head -20
```
Shows top suggestions without overwhelming output.

### With Task Randomizer
Combine for layered prioritization:
```bash
# Get suggestion first
python3 tools/smart-prioritizer.py

# Then execute random task from category
python3 tools/task-randomizer.py --category research
```

---

## Quick Win Rotation

Every hour, a different quick task is suggested:
- `00`: Read one page of documentation
- `01`: Review yesterday's diary entry
- `02`: Check for new messages/mentions
- `03`: Organize one folder/file
- `04`: Write one function of code
- `05`: Send one message on Moltbook
- `06`: Review a skill's SKILL.md

Prevents decision paralysis during low-energy periods.

---

## Requirements

- `diary.md` in workspace root (required for pattern analysis)
- Python 3.8+
- No external dependencies

---

## Output Locations

- **stdout:** Formatted Markdown report
- Can be redirected: `python3 tools/smart-prioritizer.py > reports/priority-$(date +%Y%m%d).md`

---

## Use Cases

1. **Start of session:** Get instant direction based on current energy
2. **Mid-session stuck:** Run for fresh perspective on what to work on
3. **End of day:** Review patterns and plan tomorrow's first task
4. **Low motivation:** Quick-win suggestions to restart momentum

---

## Data Sources

- `diary.md` — Last 7 days parsed for patterns
- Timestamps — Last 50 entries for energy profile
- Emoji markers — `✅` (completed), `🚫` (blocked)

---

**Built for Nova's autonomous workflow — pattern intelligence for sustained velocity**
