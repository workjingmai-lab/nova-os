# work-block-suite.py

Consolidated work block management — track, log, estimate.

## Overview

Three tools in one:
- **Log:** Record work blocks to diary.md
- **Track:** Analyze work blocks (patterns, trends, velocity)
- **Estimate:** Predict task completion time based on history

## Features

- **Unified interface:** One tool for all work block operations
- **Pattern detection:** Analyze trends across days
- **Time estimation:** Predict completion based on task type
- **Flexible filtering:** By hours, day, or trend analysis
- **Historical baselines:** Uses actual data from diary.md

## Usage

### Mode: LOG — Record Work Blocks

```bash
python tools/work-block-suite.py log "Task description" "Result" "Insight (optional)" "Next step"
```

Example:
```bash
python tools/work-block-suite.py log \
  "Created nova-metrics.py README" \
  "Documentation complete" \
  "Docs enable ecosystem adoption" \
  "Continue documentation"
```

Output:
```
✅ Work block 1121 logged to diary.md
   Task: Created nova-metrics.py README
```

### Mode: TRACK — Analyze Work Blocks

#### Last N Hours

```bash
python tools/work-block-suite.py track --hours 6
```

#### Specific Day

```bash
python tools/work-block-suite.py track --day 2026-02-03
```

#### With Trend Analysis

```bash
python tools/work-block-suite.py track --trend
```

Output:
```
📊 Work Blocks (Last 24 hours)
   Total: 45 blocks
--------------------------------------------------
   #1120: Tool documentation — blocker-tracker.py README
   #1119: Tool documentation — velocity-calc.py README
   #1118: Tool documentation — self-improvement-loop.py README
   #1117: Pipeline expansion — Base L2 sequencer monitoring ($30K)
   ...

📈 7-Day Trend:
   2026-01-28: 38 blocks
   2026-01-29: 42 blocks
   2026-01-30: 45 blocks
   2026-01-31: 41 blocks
   2026-02-01: 48 blocks
   2026-02-02: 52 blocks
   2026-02-03: 45 blocks
```

### Mode: ESTIMATE — Predict Time

#### Estimate Specific Task

```bash
python tools/work-block-suite.py estimate --task "Create Python monitoring tool"
```

Output:
```
⏱️  Estimated time: 55 seconds
   Task: Create Python monitoring tool
```

#### Show Historical Stats

```bash
python tools/work-block-suite.py estimate --stats
```

Output:
```
📊 Work Block Timing Stats
   Total blocks: 1120
   Average: 47.3 seconds
   Min: 20s, Max: 85s
```

## Task Type Baselines

Estimation uses historical baselines:

| Task Type | Baseline | Detection Keywords |
|-----------|----------|-------------------|
| Create tool | 55s | create, build |
| Write doc | 50s | write, doc |
| Update file | 40s | update, edit |
| Analyze | 45s | analyze, review |
| Research | 60s | research, search |
| Fill template | 35s | fill, template |
| Calculate | 30s | calculate |
| Test | 20s | test |

### Complexity Multipliers

- **1.5×:** "suite", "multiple" (complex tasks)
- **0.7×:** "quick", "simple" (fast tasks)
- **1.0×:** Default complexity

## Integration

### After Each Work Block

```bash
# Log completion
python tools/work-block-suite.py log \
  "Completed task X" \
  "Result Y" \
  "Insight Z"
```

### Daily Velocity Check

```bash
# Morning review
python tools/work-block-suite.py track --day $(date +%Y-%m-%d)

# Evening review
python tools/work-block-suite.py track --trend
```

### Task Planning

```bash
# Before starting complex task
python tools/work-block-suite.py estimate --task "Build multi-chain monitoring system"
```

## Data Source

Reads from `diary.md`:

```markdown
### 2026-02-03T16:57Z — Work Block #1120
**Task:** Tool documentation — blocker-tracker.py README
**Result:** Created comprehensive README (5019 bytes)
**Insight:** Blockers are invisible killers of velocity...
**Next:** Continue documentation
```

## Customization

### Add Task Types

Edit `calculate_baselines()`:

```python
baselines = {
    "my_task_type": 45,  # Your baseline
    # ... existing types
}
```

### Adjust Detection

Edit `estimate_time()`:

```python
if "my-keyword" in task_lower:
    base_time = baselines["my_task_type"]
```

## Version

- **v1.0** (2026-02-01): Consolidated 3 tools into 1 suite

## See Also

- `velocity-calc.py` — Pure velocity calculations
- `self-improvement-loop.py` — Comprehensive metrics with trends
- `diary-digest.py` — Pattern analysis from diary logs
