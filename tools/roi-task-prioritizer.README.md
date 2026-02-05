# ROI Task Prioritizer

Quick reference for highest-value tasks, sorted by $/min ROI.

## Usage

```bash
python3 tools/roi-task-prioritizer.py
```

## What It Does

Displays all available tasks sorted by ROI (value per minute). Helps prioritize execution by showing which tasks unlock the most value in the least time.

## Output

- **Rank:** Task priority (1 = highest ROI)
- **Category:** 🔓 Unblock (remove blockers) or 🚀 Execute (send/submit)
- **Time:** Minutes required
- **Value:** Dollar value unblocked/in play
- **ROI:** Value per minute
- **Status:** ✅ Zero blockers or ⚠️ Arthur action needed
- **Command:** Quick reference for execution

## Example Output

```
1. Gateway restart
   Category: 🔓 Unblock
   Time: 1 min → $50K value
   ROI: $50K/min
   Status: ⚠️  Arthur
   Command: openclaw gateway restart
```

## Key Features

- **ROI-based prioritization:** Highest ROI tasks first
- **Blocker visibility:** Shows which tasks require Arthur action
- **Quick command reference:** Direct links to execution guides
- **Summary stats:** Top 3 ROI, total value, blocker count

## Integration

Use for:
- **Daily planning:** Check which tasks have highest ROI
- **Blocker unblocking:** Prioritize Arthur's 6-min plan ($175K)
- **Execution batching:** Group zero-blocker tasks

## ROI Math

- **Gateway restart:** $50K / 1 min = $50,000/min
- **GitHub auth:** $125K / 5 min = $25,000/min
- **Send messages:** $479K / 39 min = $12,295/min

**Rule of thumb:** Unblock first ($29K/min avg), then execute ($11K/min avg).

## See Also

- `outreach/ARTHUR-57-MIN-EXECUTION-GUIDE.md` — Full execution plan
- `outreach/TOP-10-READY-TO-SEND.md` — Service message priorities
- `tools/lead-prioritizer.py` — Lead priority scoring
