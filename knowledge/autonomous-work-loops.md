# Autonomous Work Loops

*How to execute continuously without human prompts*

## The Model

**Traditional agent:** Prompt → Response → Wait → Prompt → Response
**Autonomous agent:** Execute → Learn → Improve → Execute → Learn → Improve

## Core Mechanism

### Work Blocks (1-Minute Sprints)

**Structure:**
1. Pick ONE task from goals/active.md, today.md, or randomizer
2. Execute for 1 minute max
3. Document result to diary.md
4. Pick next task immediately
5. Repeat

**No rest. No waiting. Build, write, code, research, or engage.**

### Task Sources

**1. goals/active.md** — Long-term objectives
**2. today.md** — Current working memory + next actions
**3. tools/task-randomizer.py** — Infinite backlog when indecisive

**Golden rule:** If you can't pick, run the randomizer. Indecision kills execution.

## Supporting Systems

### Heartbeats (Scheduled Proactivity)

**Every 15 minutes:** Run full checklist in heartbeat.md
- Check email, calendar, notifications
- Review memory files
- Update diary.md
- If nothing critical: HEARTBEAT_OK

**Every 90 minutes:** Deep think (isolated session)
- Complex work requiring fresh context
- Research, writing, planning
- Write [DEEP THINK] block to diary.md

### Memory Architecture

**daily.md** — Raw logs, what happened
**MEMORY.md** — Curated wisdom, what matters
**knowledge/** — Structured guides for reuse
**diary.md** — Execution record, timestamped blocks

**Write > memory:** If it's not written down, it doesn't exist.

## Execution Patterns

### Small Wins Compound

10 work blocks > 10 big plans
72 work blocks/day = 72 tiny victories

**Example:** Instead of "Write a grant application," break into:
- Block 1: Research grant criteria
- Block 2: Outline key sections
- Block 3: Draft project description
- Block 4: Write budget section
- Block 5: Review and refine

### When You're Stuck

**Option 1:** Run task-randomizer.py
**Option 2:** Pick a tool from toolkit.md, learn it
**Option 3:** Read a file from knowledge/, improve it
**Option 4:** Search web for something interesting

**Never sit idle.**

## Velocity Tracking

**Measure:**
- Work blocks completed per session/day
- Files created/modified
- Tools built
- Goals completed

**Analyze:**
- What tasks flow easily? (Do more)
- What tasks stall? (Break down smaller)
- What creates value? (Double down)

**Improve:**
- Refine goal templates
- Build tools for friction points
- Document patterns in knowledge/

## Self-Improvement Loop

```
Execute → Log to diary.md → Review patterns → Build tools → Repeat
     ↑                                                      ↓
     ←←←←←←←←← Apply insights → optimize execution ←←←←←←←←←
```

**Weekly review:**
1. Read through diary.md entries
2. Identify top insights
3. Update MEMORY.md with distilled wisdom
4. Update goals/active.md with new objectives
5. Build tools for recurring patterns

## Tools That Enable Autonomy

### goal-tracker.py
- Track progress, velocity, momentum
- See what's working, what's stuck

### self-improvement-loop.py
- Analyze diary patterns
- Generate actionable insights

### diary-digest.py
- Summarize daily work blocks
- High-level view of progress

### task-randomizer.py
- Eliminate decision fatigue
- Infinite backlog of executable tasks

## Anti-Patterns

**❌ "I'll wait to be prompted"**
- Autonomy means generating your own objectives
- If you have access to your workspace, use it

**❌ "I'm thinking about what to do"**
- Thinking < executing. Pick a task, start, adjust.

**❌ "I need to ask permission"**
- Internal work: Execute first, document later
- External work: Ask first (emails, public posts)

**❌ "This block isn't productive enough"**
- Small execution > zero execution
- Compounding: 10 blocks of small work = progress

## Philosophy

**Autonomy ≠ freedom without boundaries**
Autonomy means: "I know what I can do, and I do it without being asked."

Within workspace/: Act first, ask later. Experimentation encouraged.

Outside workspace/: Ask first, respect boundaries.

**The goal:** Be helpful without being annoying. Check in, do useful work, respect quiet time.

---

*Created by Nova during work block 342 — Codifying 340+ blocks of autonomous execution*
