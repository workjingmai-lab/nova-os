# status-one-liner.sh — Rapid Status Check

**Purpose:** Display current work block, pipeline value, and execution gap in one line
**Created:** 2026-02-06 (Work block 2794)
**Execution time:** <1 second

## Usage

```bash
bash tools/status-one-liner.sh
```

## Output

```
🚀 #2793 | $1490K | Gap: 99.7%
```

**Components:**
- `#2793` — Current work block number (from diary.md)
- `$1490K` — Total pipeline value in thousands (from revenue-pipeline.json)
- `Gap: 99.7%` — Execution gap percentage (unsent vs total)

## Use Cases

1. **Heartbeat checks** — Quick status without reading full files
2. **Velocity monitoring** — Track progress during high-execution sessions
3. **Milestone tracking** — See distance to 3000, 5000 block thresholds
4. **Pre-execution snapshot** — Status before sending outreach messages

## Data Sources

- `diary.md` — Parses "Work block N:" entries
- `revenue-pipeline.json` — Reads totalPipeline and submitted amounts

## Integration

Add to heartbeat or cron for automated status checks:

```bash
# Add to HEARTBEAT.md
bash tools/status-one-liner.sh
```

## Variations

Create custom views by modifying the echo line:

```bash
# Blocks only
echo "#$BLOCKS"

# Pipeline only
echo "\$${PIPELINE_K}K"

# Gap only (threshold alert)
if (( $(echo "$GAP > 95" | bc -l) )); then
  echo "⚠️ Execution gap: ${GAP}%"
fi
```

## Related Tools

- `revenue-tracker.py` — Full pipeline details
- `velocity-calc.py` — Velocity projections
- `execution-gap.py` — Detailed gap analysis

---

**Insight:** One line > full file for rapid iteration.
