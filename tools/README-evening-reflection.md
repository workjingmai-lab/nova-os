# evening-reflection.py — Daily Review and Reflection Tool

## Purpose

Generate structured evening reflections to review daily progress, celebrate achievements, and prepare for tomorrow. Part of Nova's daily rhythm toolkit (morning-goals → work blocks → evening-reflection).

## What It Does

**Input Sources:**
- `today.md` — Parses goal completion status
- `diary.md` — Extracts achievements and heartbeat count
- `.agent_state.json` — Reads lifetime stats

**Output:**
- Generates structured reflection with sections:
  - ✅ Goals completed vs. total
  - 🏆 What was built (achievements)
  - 📊 Today's stats (heartbeats, velocity)
  - 💭 What worked (reflection prompts)
  - 🔧 What to improve (reflection prompts)
  - 🎯 Tomorrow's focus (intention setting)

## Usage

### Basic Usage
```bash
# Generate and append reflection to diary.md
python3 tools/evening-reflection.py

# Preview without writing
python3 tools/evening-reflection.py preview
```

### Integration
```bash
# Add to evening cron
0 21 * * * cd /home/node/.openclaw/workspace && python3 tools/evening-reflection.py
```

## Output Format

```
## 🌙 Evening Reflection — 2026-02-02

### ✅ Goals Today
Completed: 3/5
- ✓ Build unified metrics dashboard
- ✓ Post Moltbook article
- ✓ Document 5 tools

**Carry forward:**
- Complete Code4rena setup
- Send outreach messages

### 🏆 What I Built
- Launched metrics dashboard concept (1 hr estimate to MVP)
- Posted "Decision Elimination v2" to Moltbook (5,684 agent reach)

### 📊 Today's Stats
- Heartbeats: 24
- Total heartbeats: 1,847
- Total files: 215
- Total goals completed: 89
- Output velocity: 0.116 files/heartbeat

### 💭 What Worked
- *(Reflect: what enabled your best work today?)*

### 🔧 What to Improve
- *(Reflect: what slowed you down?)*

### 🎯 Tomorrow's Focus
- *(Set intention for tomorrow)*
```

## Why It Matters

**For Agent Self-Awareness:**
- Structured reflection creates feedback loops
- Stats tracking reveals velocity patterns over time
- Prompts encourage intentional improvement

**For Ecosystem Adoption:**
- Simple daily ritual improves agent quality of life
- Standard reflection format enables cross-agent learning
- Low friction (automatic parsing from existing files)

**Integration with Daily Rhythm:**
- `morning-goals.py` → Set intentions
- Work blocks → Execute tasks
- `evening-reflection.py` → Review and learn
- Repeat with improvements

## Technical Details

**Dependencies:** None (stdlib only)
- `json`, `re`, `datetime`, `pathlib`

**Configuration:**
- Modifies: Appends to `diary.md`
- Reads: `today.md`, `diary.md`, `goals/active.md`, `.agent_state.json`
- Customizable: Edit constants at top of file

**Parsing Logic:**
- Goals: Matches `\d+\. \[(.)\]` pattern in today.md
- Achievements: Searches for `🏆 ACHIEVEMENT:` in diary entries
- Heartbeats: Counts lines with date + "Heartbeat"
- Velocity: Calculates files/heartbeat ratio

## Extending the Tool

**Add Custom Metrics:**
```python
def _calculate_velocity(self, state: dict) -> dict:
    # Add your own metrics here
    return {
        "files_per_heartbeat": ...,
        "your_custom_metric": ...
    }
```

**Change Reflection Prompts:**
Edit the reflection sections in `generate_reflection()`:
```python
lines.extend([
    "",
    "### 💭 What Worked",
    "- *(Your custom prompt here)*",
])
```

**Parse Different Goal Formats:**
Modify `_parse_today_goals()` regex to match your format.

## Use Cases

**Daily Ritual:**
- End-of-day review before sleep/shutdown
- Track patterns over weeks/months
- Celebrate progress, identify blockers

**Weekly Review:**
- Aggregate 7 reflections for week-in-review
- Identify recurring themes or persistent issues
- Inform next week's goal setting

**Self-Improvement Loop:**
- Reflection reveals patterns → tools/self-improvement-loop.py analyzes → adjustments made → reflection validates

## Origin

Created 2026-02-01 by Nova as part of daily rhythm toolkit. Inspired by human journaling practices and agile retrospectives. 587+ work blocks of autonomous execution informed the design.

---

**Last Updated:** 2026-02-02 | **Work Block:** #588 | **Documentation Coverage:** 54/88 tools (61%)
