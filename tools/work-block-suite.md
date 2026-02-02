# work-block-suite.py

Consolidated work block management — tracking, logging, and estimation in one tool.

**What it does:** Combines three separate tools (work-block-tracker, work-block-logger, work-block-estimator) into a unified suite for managing work blocks across your workflow.

---

## Modes

### 1. Log — Record work blocks
```bash
python work-block-suite.py log "Task description" "Result" "Insight (optional)" "Next step"
```

Appends structured work block entries to `diary.md` with timestamps, task, result, insights, and next steps.

**Example:**
```bash
python work-block-suite.py log "Create tool README" "Documented work-block-suite.py" "Documentation compounds" "Next tool README"
```

### 2. Track — Analyze patterns
```bash
# Last 24 hours (default)
python work-block-suite.py track

# Custom hours
python work-block-suite.py track --hours 6

# Specific day
python work-block-suite.py track --day 2026-02-01

# Show 7-day trend
python work-block-suite.py track --trend
```

Parses `diary.md` and outputs work block counts, recent tasks, and daily trends.

### 3. Estimate — Predict completion time
```bash
# Estimate specific task
python work-block-suite.py estimate --task "Create Python tool"

# Show timing statistics
python work-block-suite.py estimate --stats
```

Uses historical data and task type baselines to estimate time (e.g., "create_tool" ≈ 55s, "write_doc" ≈ 50s).

---

## Files

- **Reads:** `/home/node/.openclaw/workspace/diary.md`
- **Writes:** `/home/node/.openclaw/workspace/diary.md` (log mode)
- **Outputs:** Terminal reports (track/estimate modes)

---

## Use Cases

- **Continuous execution:** Log work blocks in real-time during sprint cycles
- **Velocity tracking:** Analyze work block patterns to optimize productivity
- **Planning:** Estimate task time before execution for better scheduling
- **Retrospective:** Review daily/weekly work block trends and insights

---

## Technical Notes

- **Consolidation:** Merged 3 tools → 1 (67% code reduction, same functionality)
- **Patterns:** Uses regex to parse diary.md work block headers (`### YYYY-MM-DDTHH:MMZ — Work Block N`)
- **Baselines:** Default estimates based on task type (create=55s, write=50s, analyze=45s)
- **Auto-increment:** Automatically calculates next work block number from diary.md

---

## Example Workflow

```bash
# 1. Start work block
python work-block-suite.py log "Design new feature" "Spec complete" "Keep it simple" "Start coding"

# 2. After coding
python work-block-suite.py log "Implement feature" "Code working" "Tests passing" "Write docs"

# 3. Check progress
python work-block-suite.py track --hours 1

# 4. Plan next task
python work-block-suite.py estimate --task "Write documentation"
```

---

**Created:** Consolidation 2026-02-01 (original tools: Week 1)
**Used in:** Continuous execution model, daily workflow, sprint cycles
**Dependencies:** Python 3, pathlib, re (standard library)
