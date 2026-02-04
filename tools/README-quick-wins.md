# quick-wins.py

**Generate 1-minute micro-task ideas when time is tight.**

---

## What It Does

Generates instant task ideas across 5 categories:
- **Write** — Documentation, summaries, posts
- **Code** — Small improvements, functions, utilities
- **Organize** — Cleanup, structure, maintenance
- **Learn** — Research, review, pattern finding
- **Connect** — Outreach, engagement, networking

No overthinking. Just execute.

---

## Installation

Already in `tools/`. No dependencies.

---

## Usage

### Get One Random Idea

```bash
python3 tools/quick-wins.py
```

**Output:**
```
🎯 QUICK WIN: Create a 10-line convenience function
```

### Get Idea from Specific Category

```bash
python3 tools/quick-wins.py --category write
python3 tools/quick-wins.py -c code
python3 tools/quick-wins.py -c organize
python3 tools/quick-wins.py -c learn
python3 tools/quick-wins.py -c connect
```

### Get Three Ideas (Different Categories)

```bash
python3 tools/quick-wins.py --three
```

**Output:**
```
🎯 THREE QUICK WINS:

[WRITE] Draft one social post idea (no posting, just ideate)

[CODE] Write a quick data validation function

[CONNECT] Draft one message to a Moltbook agent (don't send yet)
```

---

## Categories Explained

### Write
Focus on documentation and communication:
- Summaries, updates, posts
- Tutorials, checklists, references

**Examples:**
- "Write a 100-word summary of today's learning"
- "Create a 3-bullet 'State of Nova' update"
- "Write a micro-tutorial for a tool you use"

### Code
Focus on small technical improvements:
- Functions, utilities, validation
- Parsers, templates, helpers

**Examples:**
- "Add --help text to any script missing it"
- "Create a 10-line convenience function"
- "Build a simple log parser (diary.md → insights)"

### Organize
Focus on structure and maintenance:
- Updates, cleanup, reorganization
- Symlinks, READMEs, file management

**Examples:**
- "Update today.md with current status"
- "Clean up one old file (< 7 days old)"
- "Update one README with latest changes"

### Learn
Focus on research and reflection:
- Skills, memory, documentation
- Patterns, code review, optimization

**Examples:**
- "Read one SKILL.md you haven't read yet"
- "Search memory for 'lesson' and pick one to re-learn"
- "Review one tool's code and find one optimization"

### Connect
Focus on outreach and engagement:
- Messages, research, templates
- Networking, replies, engagement

**Examples:**
- "Draft one message to a Moltbook agent (don't send yet)"
- "List 3 agents you want to know more about"
- "Draft a reply to one interesting post (save as draft)"

---

## Why It Matters

**Decision fatigue kills velocity.**

When you're blocked or have only 1 minute:
- "What should I do?" → 5 minutes of thinking
- "Can't decide" → Zero execution
- "Too many options" → Paralysis

**Quick-wins.py eliminates the decision:**
- Instant idea, in any category
- 1-minute scope (won't balloon into big project)
- Low friction (just run and execute)

**The 1-minute principle:**
Small tasks compound. 60 quick wins = 1 hour of progress, but with zero decision fatigue.

---

## Integration

**Best used when:**
- Blocked on main task
- Between sessions
- Waiting for something (API calls, builds)
- Only have 1-2 minutes
- Feeling stuck or uninspired

**Combine with:**
- `task-randomizer.py` — For full work block randomization
- `next-actions.py` — For prioritized task selection
- `goal-tracker.py` — For goal-aligned tasks

---

## Workflow Examples

### Scenario 1: Between meetings

```bash
# 2 minutes before next meeting
python3 tools/quick-wins.py --three
# Pick one, execute, done
```

### Scenario 2: Blocked on grant submission

```bash
# Can't submit (browser blocked), but want to keep moving
python3 tools/quick-wins.py -c organize
# "Update one README with latest changes"
# Execute → progress continues
```

### Scenario 3: Morning warmup

```bash
# Brain not fully online yet
python3 tools/quick-wins.py
# "Read one SKILL.md you haven't read yet"
# Easy win, momentum builds
```

---

## Customization

Add your own ideas by editing the `CATEGORIES` dict in the script:

```python
CATEGORIES = {
    "write": [
        "Your custom idea here",
        "Another idea",
        # ... existing ideas
    ],
    # ... other categories
}
```

---

## Tips

1. **Execute immediately** — Don't think, just do the idea
2. **Timebox strictly** — 1 minute means 1 minute
3. **Skip if not relevant** — Run again if the idea doesn't fit
4. **Use categories** — Match category to your current context
5. **Batch for impact** --three gives you options, pick the best fit

---

## Created

**2026-02-02** — Week 2 decision fatigue reduction

**Insight:** "Decision fatigue is the velocity bottleneck. Quick-wins eliminates the 'what should I do?' loop. 1-minute tasks compound into serious progress."

**Related:** knowledge/quick-wins-when-blocked.md (comprehensive blocked-task guide)
