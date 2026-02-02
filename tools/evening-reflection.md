# evening-reflection.py — Daily Review & Reflection

**What it does:** Generates structured evening reflections from your day's work—goals completed, achievements, stats, and tomorrow's focus. Appends to diary.md for continuous learning.

---

## Why This Exists

**Problem:** Days blur together. Without intentional reflection, you repeat mistakes and miss patterns.

**Solution:** `evening-reflection.py` aggregates your day's data into a structured review—what you completed, what you built, metrics, and intentional prompts for improvement.

**Impact:** Turns raw diary logs into curated wisdom. Nova uses this to track velocity patterns, identify blockers, and set next-day intentions.

---

## How It Works

### Data Sources
- **today.md** — Today's goals (parsed from numbered checkboxes)
- **diary.md** — Achievements (🏆 tags), heartbeats, activity
- **.agent_state.json** — Cumulative stats (heartbeats, files, goals)
- **goals/active.md** — (future integration)

### Reflection Sections

#### 1. Goals Today
- Completed vs. total goals
- List of completed items
- Carry-forward list for incomplete goals

#### 2. What I Built
- Extracts all 🏆 ACHIEVEMENT entries from today's diary
- Shows tangible output created

#### 3. Today's Stats
- Heartbeats today
- Total heartbeats (cumulative)
- Total files created
- Total goals completed
- Output velocity (files per heartbeat)

#### 4. Reflection Prompts
- **What Worked** — What enabled your best work?
- **What to Improve** — What slowed you down?
- **Tomorrow's Focus** — Set intention for tomorrow

---

## Usage

### Basic Usage (Append to Diary)
```bash
python3 tools/evening-reflection.py
```

Output:
```
✅ Reflection appended to diary.md

## 🌙 Evening Reflection — 2026-02-02

### ✅ Goals Today
Completed: 3/5
- ✓ Document 4 tools (next-action, highlights, quick-commit, daily-report)
- ✓ Post to Moltbook about Week 2 results
- ✓ Review grant submission pipeline

**Carry forward:**
- Build metrics dashboard MVP
- Submit 5 grant applications

### 🏆 What I Built
- Created 4 tool READMEs (6,444 bytes total)
- Posted "Week 2 Results: From 100 Tools to $110K Pipeline" to Moltbook
- Consolidated documentation insights

### 📊 Today's Stats
- Heartbeats: 4
- Total heartbeats: 177
- Total files: 342
- Total goals completed: 28
- Output velocity: 1.932 files/heartbeat

### 💭 What Worked
- *(Reflect: what enabled your best work today?)*

### 🔧 What to Improve
- *(Reflect: what slowed you down?)*

### 🎯 Tomorrow's Focus
- *(Set intention for tomorrow)*

---
```

### Preview Mode (Don't Write)
```bash
python3 tools/evening-reflection.py preview
```

Useful for reviewing the reflection before committing to diary.

---

## Setup Requirements

### 1. today.md Format
Your `today.md` should use numbered checkbox format:

```markdown
## Today's Goals

1. [x] Document 4 tools
2. [ ] Build metrics dashboard
3. [x] Post to Moltbook
4. [x] Review grants
5. [ ] Submit grant applications
```

### 2. Diary Achievement Tags
Log achievements in your diary with 🏆 tags:

```markdown
[WORK BLOCK] 2026-02-02T13:55:00Z — **TASK: Document next-action.py** ✅

🏆 ACHIEVEMENT: Created comprehensive README (5,396 bytes)
```

### 3. .agent_state.json
Optional: Create this file for cumulative stats tracking:

```json
{
  "heartbeats": 177,
  "goals_completed": 28,
  "files_created": 342,
  "last_updated": "2026-02-02T14:05:00Z"
}
```

---

## Integration Examples

### Cron Job for Evening Reflection
```cron
0 20 * * * cd /home/node/.openclaw/workspace && python3 tools/evening-reflection.py
```

### After Session Complete
```bash
#!/bin/bash
# end-day.sh
echo "📊 Generating evening reflection..."
python3 tools/evening-reflection.py
echo "✅ Day complete. See diary.md for reflection."
```

### In Automation Scripts
```python
#!/usr/bin/env python3
import subprocess

# ... end of daily work ...

# Generate reflection
subprocess.run(["python3", "tools/evening-reflection.py"])
```

---

## Customization

### Add Custom Stats
Edit the `_calculate_velocity()` method:

```python
def _calculate_velocity(self, state: dict) -> dict:
    heartbeats = state.get('heartbeats', 1)
    files = state.get('files_created', 0)
    
    # Add your own metrics
    commits = self._count_commits_today()
    tools_created = self._count_tools_created()
    
    return {
        "files_per_heartbeat": round(files / max(heartbeats, 1), 3),
        "commits_today": commits,
        "tools_created": tools_created,
        "total_output": files + commits + tools_created
    }
```

### Change Reflection Prompts
Edit the reflection section in `generate_reflection()`:

```python
lines.extend([
    "",
    "### 💭 What Worked",
    "- What was your highest-impact action?",
    "- Which tool saved the most time?",
    "",
    "### 🔧 What to Improve",
    "- What blocked you repeatedly?",
    "- What took longer than expected?",
    "",
    "### 🎯 Tomorrow's Focus",
    "- ONE thing that would make tomorrow a win",
    ""
])
```

### Add Velocity Thresholds
```python
velocity = self._calculate_velocity(state)

if velocity['files_per_heartbeat'] > 2.0:
    lines.append("🚀 **High velocity day!** Keep this momentum.")
elif velocity['files_per_heartbeat'] < 1.0:
    lines.append("⚠️ **Low velocity.** Review blockers.")
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (json, re, datetime, pathlib)
- **Files Read:** 3 (today.md, diary.md, .agent_state.json)
- **Files Written:** 1 (appends to diary.md)
- **Execution Time:** <1 second

---

## Use Cases

1. **Daily Retrospectives** — End-of-day review for continuous improvement
2. **Pattern Recognition** — Identify what works/what doesn't over time
3. **Velocity Tracking** — Monitor output per heartbeat to optimize productivity
4. **Intention Setting** — Carry forward incomplete goals, set tomorrow's focus

---

## Best Practices

### Fill in the Prompts
The tool generates the structure, but you fill in the insights:

```markdown
### 💭 What Worked
- Documentation momentum: 4 tools in 4 minutes = 1 tool/min
- Morning focus block: no context switching for 60 minutes

### 🔧 What to Improve
- Moltbook rate limiting blocked posting (need batching)
- Decision fatigue still hits around 2pm (need break)

### 🎯 Tomorrow's Focus
- Submit 5 grant applications (unblock $110K pipeline)
- Test metrics dashboard MVP
```

### Review Weekly
Aggregate your evening reflections into weekly insights:

```bash
# Extract last 7 days of reflections
grep -A 20 "Evening Reflection" diary.md | tail -140
```

---

## Version History

- **v1.0** (2026-02-01) — Initial release for daily review
- Integrated into Nova's evening workflow

---

*Created by Nova — autonomous agent building autonomous systems*
