# execution-gap-closer.py

Transforms "ready" pipeline into actionable send tasks. The $825K problem: potential energy → kinetic energy converter.

## Usage

```bash
# Display execution gap analysis
python3 tools/execution-gap-closer.py

# Export task list to markdown
python3 tools/execution-gap-closer.py export
```

## What It Does

1. **Loads pipeline** from `revenue-pipeline.json`
2. **Filters** for "ready" status leads only
3. **Calculates ROI/min** for each lead (value × priority / time)
4. **Ranks** leads by highest ROI per minute
5. **Shows** execution strategy with phases
6. **Calculates** conversion scenarios (5%, 10%, 20%)

## Output

```
⚡ EXECUTION GAP CLOSER

📊 PIPELINE SNAPSHOT
   Ready leads: 9
   Total value: $825,000
   Time to send: 27 minutes
   Average ROI: $30,556/min

🎯 TOP 10 SEND TASKS (by ROI/min)
   1. Additional Leads (35+) — $152,500/min ROI
   2. DAO Leads (10) — $63,750/min ROI
   3. ETH Foundation — $40,000/min ROI
   ...

💰 CONVERSION MATH
   5% conversion → $41,250 revenue
   10% conversion → $82,500 revenue
   20% conversion → $165,000 revenue

⏰ TIME TO CLOSE GAP: 27 minutes
   Every day you wait = $27,500 in monthly opportunity cost
```

## Priority Multipliers

| Priority | Multiplier | Purpose |
|----------|-----------|---------|
| HIGH | 3.0x | 3× weight for strategic focus |
| MEDIUM | 1.5x | 1.5× weight for balanced priority |
| LOW | 1.0x | Base weight for volume |

## Integration

Run daily to identify highest ROI send tasks:

```bash
# Add to daily routine
python3 tools/execution-gap-closer.py

# Export for task tracking
python3 tools/execution-gap-closer.py export
```

## Files

- Reads: `revenue-pipeline.json`
- Writes: `execution-tasks-today.md` (on export)

## Related Tools

- `pipeline-quickview.py` — Quick revenue status
- `daily-revenue-action.py` — Recommends highest ROI action
- `revenue-tracker.py` — Full pipeline management
