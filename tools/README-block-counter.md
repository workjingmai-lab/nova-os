# block-counter.py

Quick work block statistics — counts blocks in diary.md for instant metrics.

## What It Does

Scans diary.md for work block entries and outputs:
- Total work blocks completed
- Blocks completed today
- Diary file size
- Average characters per block

Fast way to check daily/weekly progress without parsing the entire diary.

## Installation

No dependencies required. Uses Python standard library only.

## Quick Start

```bash
python3 tools/block-counter.py
```

## Usage Examples

### Check default diary (diary.md)
```bash
python3 tools/block-counter.py
```

**Output:**
```
📊 Work Block Statistics
════════════════════════════════════════════
  Total blocks:  775
  Blocks today:  3
  Diary size:     98,432 characters
  Avg per block:  127 chars

🔥 Streak alive! 3 blocks today
```

### Check specific diary file
```bash
python3 tools/block-counter.py path/to/other-diary.md
```

## How It Works

1. **Counts blocks** — Finds all `[WORK BLOCK NNN` patterns in diary.md
2. **Extracts dates** — Parses timestamps from recent blocks to count today's blocks
3. **Calculates stats** — File size and average block length
4. **Encourages momentum** — Shows streak message when 10+ blocks today

## Block Format

The tool expects work blocks in this format (standard Nova diary format):

```markdown
## 🔥 WORK BLOCK #775 (2026-02-02T23:49Z)
**Task:** Tool documentation — agent-starter-kit.py
**What done:**
...
```

Key elements:
- `[WORK BLOCK NNN` pattern (with brackets)
- ISO 8601 timestamp in parentheses
- Double-hash heading (`##`)

## Integration

### Heartbeat example (HEARTBEAT.md)
```yaml
- name: "Daily Progress Check"
  every: "1h"
  message: |
    Check today's work block count.
    python3 tools/block-counter.py
    If < 5 blocks, ramp up execution.
```

### Combined with daily tracking
```bash
# Check blocks today
python3 tools/block-counter.py

# See detailed metrics
python3 tools/daily-output-tracker.py
```

### Cron job for end-of-day summary
```bash
# At 23:59 UTC every day
59 23 * * * cd /home/node/.openclaw/workspace && python3 tools/block-counter.py >> daily-summary.log
```

## Return Codes

- `0` — Success (blocks found and counted)
- `1` — Diary file not found
- `0` — No blocks found (displays message, exits cleanly)

## Use Cases

### Morning motivation
```bash
python3 tools/block-counter.py
# Output: "Total blocks: 774 | Blocks today: 0"
# → Start working!
```

### Midday check-in
```bash
python3 tools/block-counter.py
# Output: "Blocks today: 12"
# → Keep momentum going
```

### End-of-day review
```bash
python3 tools/block-counter.py
# Output: "Blocks today: 42"
# → Great day, log insights to MEMORY.md
```

## Comparison to Other Tools

- **block-counter.py** — Quick stats, 1-second check
- **daily-output-tracker.py** — Detailed metrics, velocity analysis
- **diary-digest.py** — Pattern analysis, long-term trends

Use `block-counter.py` for instant feedback. Use the others for deeper analysis.

## Files

- `diary.md` — Default diary location
- Any path passed as first argument

## Requirements

- Diary must exist
- Blocks must follow standard format (see Block Format above)

## Tips

### Track streak goals
```bash
# Goal: 50 blocks/day
python3 tools/block-counter.py | grep "Blocks today"
# If < 50, keep working
```

### Monitor diary size
```bash
# Alert if diary gets too large (>1MB)
python3 tools/block-counter.py | grep "Diary size"
```

### Average block length
```bash
# Track efficiency (shorter blocks = faster execution)
python3 tools/block-counter.py | grep "Avg per block"
```

## See Also

- `diary-digest.py` — Pattern analysis from diary logs
- `daily-output-tracker.py` — Detailed daily metrics
- `tools/README-block-counter.md` — This file
