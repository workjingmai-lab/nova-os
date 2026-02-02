# Work Block Suite

> Consolidated work block management — track, log, and estimate your execution velocity

**Created:** 2026-02-01
**Category:** Workflow
**Dependencies:** None (Python 3 standard library only)

---

## Overview

Work Block Suite combines three tools into one unified interface:
- **Log mode** — Record work blocks to diary.md
- **Track mode** — Analyze work blocks (patterns, trends, velocity)
- **Estimate mode** — Predict task completion time based on historical data

---

## Installation

No installation required. Just run:

```bash
python3 tools/work-block-suite.py <mode> [options]
```

---

## Usage

### Mode: LOG — Record work blocks

Log a completed work block to diary.md:

```bash
python3 tools/work-block-suite.py log "Task description" "Result" "Insight (optional)" "Next step"
```

**Example:**
```bash
python3 tools/work-block-suite.py log \
  "Create Python tool for work block tracking" \
  "Built work-block-suite.py with log/track/estimate modes" \
  "Consolidated 3 tools into 1 reduced maintenance burden" \
  "Create documentation for 10 tools"
```

**Output:** Appends a timestamped work block entry to `diary.md`

---

### Mode: TRACK — Analyze work blocks

Analyze recent work blocks:

```bash
# Last 24 hours (default)
python3 tools/work-block-suite.py track

# Last 6 hours
python3 tools/work-block-suite.py track --hours 6

# Specific date
python3 tools/work-block-suite.py track --day 2026-02-01

# Show 7-day trend
python3 tools/work-block-suite.py track --trend
```

**Output:**
```
📊 Work Blocks (Last 24 hours)
   Total: 72 blocks
--------------------------------------------------
   #516: Create README for work-block-suite.py
   #517: Update MEMORY.md with Week 2 insights
   #518: Analyze tool usage patterns
   ...

📈 7-Day Trend:
   2026-01-27: 58 blocks
   2026-01-28: 64 blocks
   2026-01-29: 71 blocks
   2026-01-30: 68 blocks
   2026-01-31: 72 blocks
   2026-02-01: 85 blocks
   2026-02-02: 77 blocks
```

---

### Mode: ESTIMATE — Predict task time

Estimate how long a task will take:

```bash
python3 tools/work-block-suite.py estimate --task "Create Python tool"

# Show historical timing stats
python3 tools/work-block-suite.py estimate --stats
```

**Output:**
```
⏱️  Estimated time: 55 seconds
   Task: Create Python tool

📊 Work Block Timing Stats
   Total blocks: 518
   Average: 47.3 seconds
   Min: 20s, Max: 120s
```

---

## How It Works

### Baseline Times (by task type)

The estimate mode uses historical baselines:

| Task Type | Baseline | Examples |
|-----------|----------|----------|
| create_tool | 55s | "Create Python tool", "Build script" |
| write_doc | 50s | "Write README", "Document tool" |
| update_file | 40s | "Update config", "Edit existing file" |
| analyze | 45s | "Analyze logs", "Review patterns" |
| research | 60s | "Search web", "Investigate topic" |
| template | 35s | "Fill template", "Copy-paste edit" |
| calculate | 30s | "Run calculations", "Generate metrics" |
| test | 20s | "Test tool", "Verify output" |

**Complexity multipliers:**
- "suite", "multiple" → ×1.5
- "quick", "simple" → ×0.7

---

## Data Storage

- **Diary path:** `/home/node/.openclaw/workspace/diary.md`
- **Format:** Timestamped work block entries
- **Parser:** Extracts blocks from `### YYYY-MM-DDTHH:MMZ — Work Block N` headers

---

## Why This Tool Exists

**Problem:** Three separate tools (work-block-tracker, work-block-logger, work-block-estimator) created maintenance debt and cognitive overhead.

**Solution:** Consolidated into one tool with three modes. Same functionality, ⅓ the maintenance burden.

**Impact:**
- Faster work block logging (one command vs. three)
- Unified analysis across log/track/estimate
- Easier to maintain and extend

---

## See Also

- `diary-digest.py` — Summarize diary.md into daily digests
- `goal-tracker.py` — Track goal progress
- `self-improvement-loop.py` — Velocity tracking and insights

---

**Status:** ✅ Active — Used daily for work block tracking and velocity analysis
