# next-task-suggester.py — Decision Fatigue Killer

**Purpose:** Quick next-task suggestions from today.md. Eliminates decision fatigue by prioritizing and categorizing ready actions. Optimized for 1-minute work blocks.

**When to use:** Starting a work block and need a task NOW. No thinking, just execute.

---

## What It Does

1. **Reads today.md** — Extracts "Next Actions" section and ready patterns
2. **Categorizes tasks** — execution, documentation, tools, analytics, blockers
3. **Prioritizes by impact** — high (🔥), medium (⚡), low (📝)
4. **Displays top N** — 5 suggestions by default with priority icons
5. **Shows quick stats** — Total actions, latest block, ready count

---

## Usage

### Default (5 suggestions)

```bash
python3 tools/next-task-suggester.py
```

**Example output:**
```
🎯 Next Task Suggestions (Work Block 1420)
==================================================
1. 🔥 📝 **DOCS PUSH:** Create READMEs for top 20 most-used tools
   Category: documentation | Priority: high
2. 🔥 🚀 **EXECUTE READY:** Services NO blockers → batch send ready
   Category: execution | Priority: high
3. ⚡ 🔧 **ARTHUR UNBLOCK:** Gateway restart (1 min → $50K)
   Category: blockers | Priority: medium
4. ⚡ 📊 **ANALYTICS:** Review tool usage patterns
   Category: analytics | Priority: medium
5. 📝 **TOOLS:** Build agent-productivity-tracker.py
   Category: tools | Priority: medium

📊 Quick Stats:
   Total actions: 12
   Latest block: 1419
   Ready to execute: 8
```

### Custom Count

```bash
# Show top 3 tasks
python3 tools/next-task-suggester.py --count 3
```

### Filter by Category

```bash
# Show only execution tasks
python3 tools/next-task-suggester.py --category execution

# Show only documentation tasks
python3 tools/next-task-suggester.py --category documentation
```

---

## Categories

| Category | Keywords | Use When |
|----------|----------|----------|
| execution | send, execute, pipeline, outreach, messages | Ready to ship |
| documentation | readme, document, guide, tutorial | Writing mode |
| tools | tool, script, automation, create | Building mode |
| analytics | track, analyze, metrics, snapshot | Analysis mode |
| blockers | unblock, fix, resolve, auth | Unblocking mode |
| general | (no match) | Default |

---

## Priority Logic

**High priority (🔥):**
- send, execute, revenue, pipeline, approval

**Medium priority (⚡):**
- document, create, build

**Low priority (📝):**
- Everything else

**Source:** Extracted from today.md "Next Actions" section + ready patterns.

---

## Why It Matters

**Decision fatigue is the velocity bottleneck.**

From MEMORY.md:
> "Task randomizer increased velocity from ~25 to ~44 blocks/hour"

Why? Because **choosing tasks burns mental energy**. This tool:
- Eliminates "what should I do?" friction
- Shows highest-impact actions first
- Enables instant execution (0 decision time)

**Before:** Stare at today.md, pick task, start (30+ seconds)
**After:** Run script, see top 5, execute line 1 (3 seconds)

**Result:** 27 seconds saved per task × 44 tasks/hour = ~20 min/hour reclaimed

---

## Ready Patterns

**Automatically detects:**
- `✅.*ready` — Completed and ready items
- `🎯.*ready` — Target-ready items
- `Pipeline.*ready` — Pipeline-ready items
- `awaiting.*approval` — Awaiting approval (ready to follow up)
- `BUILD.*COMPLETE` — Build complete, ready to ship
- `EXECUTE.*ready` — Execute-ready items

---

## Integration

**Part of continuous execution workflow:**

1. **Cron fires** → Work block starts
2. **Run next-task-suggester.py** → Get top 5 tasks
3. **Execute line 1** → Complete in 1 minute
4. **Log to diary.md** → Document result
5. **Repeat** → Next block

**No thinking. Just executing.**

---

## Dependencies

- Python 3.6+
- Standard library only (`json`, `re`, `pathlib`, `datetime`, `argparse`)
- **Input:** `today.md` (must have "Next Actions" section)
- **Optional:** `diary.md` (for latest block number)

---

## Created

2026-02-04 — Work block 1420
