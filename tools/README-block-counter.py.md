# block-counter.py

**Quick Work Block Statistics**

Instant metrics from your diary.md — total blocks, daily count, diary size, streak detection.

---

## What It Does

`block-counter.py` scans `diary.md` and generates instant statistics:
- **Total work blocks** — Lifetime block count
- **Blocks today** — Current day execution
- **Diary size** — Character count
- **Average per block** — Content density
- **Streak detection** — Celebrates momentum

One command. No dependencies.

---

## Installation

No dependencies beyond Python 3.7+. Just run:

```bash
python tools/block-counter.py
```

---

## Usage

### Basic Usage

```bash
python tools/block-counter.py
```

Example output:
```
📊 Work Block Statistics
══════════════════════════════════════════════════
  Total blocks:  1133
  Blocks today:  47
  Diary size:    284,520 characters
  Avg per block: 251 chars

🔥 Streak alive! 47 blocks today
```

### Custom Diary Path

```bash
python tools/block-counter.py /path/to/diary.md
```

---

## How It Works

1. **Scans diary.md** for work block entries (`[WORK BLOCK NNN — date]`)
2. **Parses block numbers** to get total count
3. **Extracts dates** to count today's blocks
4. **Calculates metrics** — size, averages, streak

**Detection format:** Expects diary entries like:
```markdown
### Work Block #1133 — 2026-02-03T17:27Z
**Task:** ...
```

---

## Integration Patterns

### Pattern 1: Cron-Triggered Stats

```python
# In your heartbeat handler
import subprocess

result = subprocess.run(
    ["python", "tools/block-counter.py"],
    capture_output=True,
    text=True
)
print(result.stdout)
```

### Pattern 2: Python Integration

```python
from tools.block_counter import count_blocks

# Get stats programmatically
count_blocks("diary.md")

# Or capture output
import io
import sys
old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()
count_blocks("diary.md")
stats = buffer.getvalue()
sys.stdout = old_stdout
print(stats)
```

### Pattern 3: Dashboard Integration

```python
# Add to your status dashboard
from tools.block_counter import count_blocks
from tools.agent_starter_kit import AgentKit

kit = AgentKit("Nova")
stats = count_blocks("diary.md")
kit.heartbeat(f"Stats check: {stats}")
```

---

## Output Fields

| Field | Description |
|-------|-------------|
| **Total blocks** | Highest block number found (lifetime count) |
| **Blocks today** | Entries with today's date |
| **Diary size** | Total characters in diary.md |
| **Avg per block** | Diary size ÷ total blocks (content density) |
| **Streak** | Appears when blocks today ≥ 10 |

---

## Why This Matters

**Problem:** Work blocks compound, but without visibility you lose momentum.

**Solution:** `block-counter.py` provides instant feedback:
- See progress in real-time
- Celebrate streaks (≥10 blocks/day)
- Track content density (are you documenting enough?)

**Impact:** Visibility → motivation → consistency.

---

## Real-World Usage

Nova uses this every heartbeat:
- Every 15 minutes: `block-counter.py` runs
- Tracks daily execution (e.g., "47 blocks today")
- Maintains streak awareness
- Validates diary growth (284K+ characters)

**Result:** Continuous awareness of compounding progress.

---

## Customization Examples

### Add Velocity Metrics

```python
# Extend to show blocks/hour
from datetime import datetime, timedelta

# After counting blocks
start_time = datetime.fromisoformat(state.get("started_at"))
uptime_hours = (datetime.now() - start_time).total_seconds() / 3600
velocity = total_blocks / uptime_hours if uptime_hours > 0 else 0
print(f"  Velocity:       {velocity:.1f} blocks/hour")
```

### Add Weekly Summary

```python
# Count blocks in last 7 days
from datetime import datetime, timedelta

week_ago = datetime.now() - timedelta(days=7)
week_blocks = sum(
    1 for d in dates 
    if datetime.fromisoformat(d) > week_ago
)
print(f"  This week:      {week_blocks} blocks")
```

### Add Target Progress

```python
# Track against daily target
target = 300  # Your target
progress = (today_count / target * 100) if target > 0 else 0
print(f"  Daily target:   {progress:.1f}% ({today_count}/{target})")
```

---

## Error Handling

```bash
# Diary not found
$ python tools/block-counter.py missing.md
❌ Diary not found: missing.md
```

```bash
# No work blocks yet
$ python tools/block-counter.py empty_diary.md
📊 No work blocks found in diary.md
```

---

## Files Read

- `diary.md` (default) or custom path

---

## See Also

- **`diary-digest.py`** — Pattern analysis from diary logs
- **`self-improvement-loop.py`** — Velocity tracking and optimization
- **`agent-starter-kit.py`** — Heartbeat logging and goal tracking

---

## Version History

- **v1.0** — Initial release

---

*What gets measured gets managed.*
