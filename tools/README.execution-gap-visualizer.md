# execution-gap-visualizer.py

**Makes the invisible visible: Shows the gap between ready and sent revenue.**

## What It Does

Calculates and visualizes your execution gap:
- How much revenue is ready to send
- How much has actually been sent
- The gap percentage
- Progress bar visualization
- Time-to-close estimate

## Usage

```bash
python3 tools/execution-gap-visualizer.py
```

## Output Example

```
============================================================
💰 EXECUTION GAP VISUALIZER
============================================================

📊 Pipeline Status:
   Total:     $1.5M
   Ready:     $892K
   Submitted: $5K
   Won:       $0

🚨 THE GAP:
   Gap:       $887K (99.4%)

   Progress:  [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.6%
              $5K sent / $892K ready

⏱️  Time to Close Gap:
   At $10K/min: 89 minutes

💡 Reality Check:
   ⚠️  You have $887K ready to send.
   ⚠️  Why haven't you hit send yet?

============================================================
```

## How It Works

Reads `data/revenue-pipeline.json` and calculates:
- **Total:** Sum of all potential (grants + services + bounties)
- **Ready:** Items with status `ready`, `ready_to_submit`, `messages_ready`, `outreach-ready`
- **Submitted:** Items with status `submitted`
- **Won:** Items with status `won`
- **Gap:** Ready - Submitted (what you're leaving on the table)

## Why It Matters

**Psychological framing:** Seeing "$887K gap" is more motivating than seeing "99.4% gap."

**Action catalyst:** The tool asks "Why haven't you hit send yet?" — that's the question that drives execution.

**Time estimate:** At $10K/min ROI, closing an $887K gap takes 89 minutes. That's actionable.

## Integration

Run periodically (daily or every few blocks) to track execution progress.

**Status:** Active ✅
**Created:** 2026-02-07 (Work block 3247)
**Version:** 1.0
