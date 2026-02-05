# Quick Wins Generator

## Overview
Generates 15 one-minute tasks to eliminate decision fatigue and maintain high velocity. Pick any task, execute, repeat.

## Problem Solved
**Decision fatigue kills velocity.** When you don't know what to do next, you waste time thinking instead of executing. This tool provides ready-to-execute tasks.

## Usage
```bash
# Show 15 tasks (prioritized from today.md + templates)
./quick-wins-generator.py

# Show 1 random task (for instant execution)
./quick-wins-generator.py --random
```

## Task Sources

### 1. Context Tasks (High Priority)
Loaded from `today.md` "Next Actions" section:
- Grant submissions ($130K ready)
- Gateway restart ($50K unblocked)
- Outreach messages ready to send

### 2. Template Tasks (Fill Remaining)
Categorized for easy selection:

**Revenue (highest priority)**
- Research prospect → Find contact info
- Write service proposal → Use value-first structure
- Optimize outreach message → Cut fluff, add ROI
- Update pipeline → Log new leads/outcomes
- Check grant deadlines → Submissions due soon?

**Tools & Documentation**
- Create new tool → Automate repeated task
- Write README → Document tool
- Consolidate overlapping tools → Reduce maintenance
- Optimize tool → Profile, improve, add features
- Create template → Standardize execution

**Content & Outreach**
- Write Moltbook post → Share insight
- Engage on Moltbook → Comment, follow
- Create knowledge article → Document learning
- Optimize blog post → Improve hook
- Schedule social post → Share achievement

**Analytics & Review**
- Run velocity tracker → Compare vs baseline
- Analyze work patterns → What has highest ROI?
- Review diary.md → What insights repeat?
- Check heartbeat state → Last email/calendar check?
- Update blocker list → New or resolved?

**Learning & Experimentation**
- Learn new skill → Read SKILL.md
- Experiment with tool → Try features
- Read documentation → Learn improvements
- Research competitor → What can I do better?

**Maintenance**
- Trim today.md → Keep last 10 sessions
- Update MEMORY.md → Add insights
- Commit changes → git push
- Review workspace → Reorganize, delete
- Clean tmp/ → Remove old files

## Examples

### Context-Aware Tasks
When today.md has grant submission as #1 priority:
```
1. GRANT SUBMIT: 5 proposals ready ($130K), 15 min
2. ARTHUR UNBLOCK: Gateway restart (1 min → $50K)
3. OUTREACH: Find SEMI contact → Send proposal
```

### Random Task
```bash
$ ./quick-wins-generator.py --random
🎲 Random One-Minute Task
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Research 1 prospect → Find contact info (5 min → $10-25K proposal ready)

⏱️  Start now. No thinking. Just execute.
```

## Key Principles

1. **Any task is better than no task** — Execute first, optimize later
2. **15 tasks = 15 minutes** — Massive progress in one focused session
3. **Context prioritized** — today.md tasks appear first
4. **No overthinking** — Pick, execute, repeat
5. **Velocity over perfection** — Done beats perfect

## Workflow
1. Run `./quick-wins-generator.py`
2. Pick task #1 (don't think, just pick)
3. Execute (1 minute)
4. Pick task #2
5. Repeat until 15 done
6. Track velocity: `./revenue-velocity-tracker.py --init`

## Created
- **Date:** 2026-02-04
- **Work block:** #1509
- **Context:** Week 2 revenue pivot — eliminating decision fatigue

## Insight
> **Decision fatigue is the velocity bottleneck.** When you spend more time choosing tasks than executing them, you're losing velocity. This tool turns "what should I do?" into "execute task #1."

## Related Tools
- `revenue-velocity-tracker.py` — Measure execution efficiency
- `task-randomizer.sh` — Random task selection for velocity
- `today.md` — Context source for high-priority tasks
