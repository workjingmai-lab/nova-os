# work-block-tracker.py

Track work block completion rates, predict milestones, and analyze work patterns.

---

## Usage

```bash
# View current status
python3 tools/work-block-tracker.py status

# Predict when you'll hit a milestone
python3 tools/work-block-tracker.py predict --target 4000

# Analyze work patterns
python3 tools/work-block-tracker.py analyze
```

---

## Features

### Status View
Shows:
- Current block number
- Total completed blocks
- Elapsed time
- Current velocity (blocks/hour)
- Milestone progress (1000, 2000, 3000, 4000, 5000)
- Work category breakdown

### Milestone Prediction
Predicts:
- Blocks remaining to target
- Hours remaining
- Predicted date and time

### Pattern Analysis
Categorizes work into:
- Documentation (articles, knowledge)
- Tool Development (scripts, code)
- Outreach/Content (messages, posts)
- Research/Analysis
- Other

---

## Example Output

```
==================================================
📊 WORK BLOCK VELOCITY TRACKER
==================================================
Current Block:     3276
Total Completed:   9
Elapsed Time:      0.11 hours
Current Velocity:  78.4 blocks/hour
==================================================

🏆 MILESTONE PROGRESS:
  ✅ 1,000 blocks — ACHIEVED
  ✅ 2,000 blocks — ACHIEVED
  ✅ 3,000 blocks — ACHIEVED
  ⏳ 4,000 blocks — 724 to go
  ⏳ 5,000 blocks — 1724 to go

📁 WORK CATEGORY BREAKDOWN:
  Documentation: 3 (33.3%)
  Outreach/Content: 2 (22.2%)
  Tool Development: 2 (22.2%)
```

---

## Data Sources

- **diary.md** — Parses work block entries
- **.heartbeat_state.json** — Reads session timing data

---

## Tips

1. Run `status` after each work session to track progress
2. Use `predict` to set realistic milestone targets
3. Check `analyze` to balance work categories
4. Velocity of 40-80 blocks/hour is typical for focused work

---

## Related Tools

- `velocity-calc.py` — Detailed velocity calculations
- `daily-output-tracker.py` — Daily productivity tracking
- `work-pattern-analyzer.py` — Historical pattern analysis
