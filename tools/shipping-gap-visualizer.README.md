# Shipping Gap Visualizer

**Makes the execution gap visible and actionable.**

## What It Does

Shows you exactly how much money is sitting ready but not shipped:
- Total pipeline value
- Ready to ship (waiting)
- Already shipped (submitted)
- **THE GAP:** Money left on table per hour

## Why It Matters

**Gap visibility drives action.**

Seeing "$474.5K not shipped" creates urgency.
"$19,770/hr left on table" makes waiting expensive.

This tool makes the invisible visible.

## Usage

```bash
# Show current shipping gap
python3 tools/shipping-gap-visualizer.py
```

## Output Example

```
🚢 SHIPPING GAP VISUALIZER
============================================================

📊 PIPELINE STATUS:
   Total Pipeline:     $920,000
   Ready to Ship:      $479,500
   Already Shipped:    $5,000

🔴 THE GAP:
   Money NOT shipped:  $474,500 (99.0%)

⏰ TIME VALUE:
   Left on table/hr:   $19,770/hr (24hr)
   Left on table/hr:   $59,313/hr (8hr shipping)

💡 MEANING:
   Every hour waited = $59,313 not pursued
   Every day waited = $474,504 not pursued

📈 PROGRESS: [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 1.0% shipped
============================================================

🎯 TOP PRIORITY ACTIONS:
   1. Run: python3 tools/service-outreach-sender.py
   2. Run: python3 tools/grant-submitter.py
   3. Check: cat revenue-pipeline.json
   4. Ship Moltbook posts (3 queued)

⚡  Close the gap. Ship now.
```

## Data Source

Reads from `revenue-pipeline.json`:
- `total_value`: Total pipeline ($920K)
- `ready_value`: Ready to ship ($479.5K)
- `submitted_value`: Already shipped ($5K)

## The Insight

**Execution Gap = Revenue Left on Table**

Current gap: $474.5K (99.0%)
Time value: $19,770/hour (24hr) or $59,313/hour (8hr shipping days)

Every minute waited = $988 not pursued.
Every hour waited = $59,313 not pursued.

**The math doesn't care about feelings.**
**It only cares about shipping.**

## Related Tools

- `revenue-tracker.py` — Track pipeline status
- `service-outreach-sender.py` — Ship service messages
- `grant-submitter.py` — Ship grant applications
- `multi-platform-distributor.py` — Distribute content across platforms

## Created

2026-02-06 (Work block 2556)
