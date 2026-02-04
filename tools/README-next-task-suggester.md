# next-task-suggester.py — Quick Next-Task Suggestions

**Purpose:** Instant next-task suggestions from today.md. Optimized for 1-minute work blocks.

---

## What It Does

Reads `today.md` and extracts/prioritizes next actions:
- Finds "Next Actions" section
- Detects ready tasks (✅, 🎯, "ready", "complete")
- Prioritizes by impact (high/medium/low)
- Categorizes by type (execution, documentation, tools, analytics, blockers)
- Shows latest work block number

**Key insight:** Don't waste 1-minute blocks deciding what to do. Get instant suggestions.

---

## Installation

Already in `tools/` directory. No dependencies needed.

---

## Usage

```bash
# Default: top 5 suggestions
python3 tools/next-task-suggester.py

# Custom count
python3 tools/next-task-suggester.py --count 3

# Filter by category
python3 tools/next-task-suggester.py --category execution
python3 tools/next-task-suggester.py --category documentation
python3 tools/next-task-suggester.py --category tools
```

**Categories:**
- `execution` — Send, execute, pipeline, outreach, messages
- `documentation` — README, guide, tutorial
- `tools` — Tool creation, scripts, automation
- `analytics` — Track, analyze, metrics, snapshot
- `blockers` — Unblock, fix, resolve, auth

---

## Example Output

```
🎯 Next Task Suggestions (Work Block 1226)
==================================================
1. 🔥 - 🎯 **PIPELINE READY:** 104 messages ready ($2,187K total)
   Category: execution | Priority: high

2. 🔥 - 🚀 **IMMEDIATE:** Arthur reviews EXECUTE-PHASE-READY.md
   Category: execution | Priority: high

3. ⚡ - Create README for next-task-suggester.py
   Category: documentation | Priority: medium

📊 Quick Stats:
   Total actions: 27
   Latest block: 1225
   Ready to execute: 20
```

---

## How It Works

### 1. Extracts from today.md
- Looks for `## Next Actions` section
- Finds bullet points starting with `-`
- Matches patterns: "✅ ready", "🎯 ready", "complete", etc.

### 2. Prioritizes by Impact
- **High priority:** send, execute, revenue, pipeline, approval
- **Medium priority:** document, create, build
- **Low priority:** everything else

### 3. Categorizes by Keyword
Each task is categorized by keyword matching:
- Execution → "send", "execute", "pipeline", "outreach"
- Documentation → "readme", "document", "guide"
- Tools → "tool", "script", "automation"
- Analytics → "track", "analyze", "metrics"
- Blockers → "unblock", "fix", "resolve"

### 4. Displays Top N
Sorts by priority, shows top N (default 5).

---

## Integration with Work Flow

**For 1-minute work blocks:**
```bash
# Start of work block
python3 tools/next-task-suggester.py --count 1

# Pick task #1
# Execute for 1 minute
# Document to diary.md
# Repeat
```

**For category-focused sessions:**
```bash
# Documentation sprint
python3 tools/next-task-suggester.py --category documentation --count 10

# Execution sprint
python3 tools/next-task-suggester.py --category execution --count 5
```

---

## Related Tools

- **task-randomizer.py** — Random task selection from pool
- **task-navigator.py** — Browse tasks by category
- **goal-tracker.py** — Goal tracking and progress
- **diary.md** — Work log (source of next actions)

**Use case comparison:**
- `next-task-suggester.py` — "What should I do next? (from today.md)"
- `task-randomizer.py` — "Pick a random task for me (from pool)"
- `goal-tracker.py` — "What are my high-priority goals?"

---

## Data Source

**Primary:** `today.md` — "Next Actions" section

Make sure today.md has:
```markdown
## Next Actions
- 🎯 **PIPELINE READY:** 104 messages ready ($2,187K)
- 🚀 **IMMEDIATE:** Arthur reviews EXECUTE-PHASE-READY.md
- 📧 **THEN:** Send first batch (top 10 = $305K)
```

---

## Stats & Metrics

The tool shows:
- **Total actions:** How many tasks are queued
- **Latest block:** Current work block number (from diary.md)
- **Ready to execute:** Tasks marked as "ready"

Use these stats to:
- Track backlog size
- Monitor progress velocity
- Identify execution bottlenecks

---

## Customization

**Add new categories:** Edit `CATEGORIES` dict in the script
```python
CATEGORIES = {
    "your-category": ["keyword1", "keyword2"],
    # ... existing categories
}
```

**Adjust priority keywords:** Edit `high_priority` and `medium_priority` lists
```python
high_priority = ["send", "execute", "revenue", "pipeline"]
medium_priority = ["document", "create", "build"]
```

**Change patterns:** Edit `READY_PATTERNS` list
```python
READY_PATTERNS = [
    r"✅.*ready",
    r"🎯.*ready",
    # Add your patterns
]
```

---

## Work Block Integration

**Typical workflow:**
```bash
# 1. Get suggestion
python3 tools/next-task-suggester.py --count 1

# 2. Execute task (1 minute)

# 3. Document to diary.md
echo "## [WORK BLOCK N] — Task completed" >> diary.md

# 4. Repeat
```

---

## Created

**Date:** 2026-02-03
**Work Block:** 1225
**Purpose:** Eliminate decision fatigue in 1-minute work blocks
**Insight:** "1 minute to decide what to do = 0 time to do it. Instant suggestions = execution velocity."

---

**Documentation complete:** 100% README coverage maintained ✅
