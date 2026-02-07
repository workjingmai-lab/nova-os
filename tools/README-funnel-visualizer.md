# funnel-visualizer.py — ASCII Conversion Funnel

**Purpose:** Visualize revenue pipeline stages as ASCII funnel
**Created:** 2026-02-06 (Work block 2797)
**Execution time:** <1 second

## Usage

```bash
python3 tools/funnel-visualizer.py
```

## Output Example

```
====================================================
  PIPELINE CONVERSION FUNNEL
====================================================

  1. PIPELINE BUILT
     $1.5M
     ████████████████████████████████████████

  2. READY TO SEND
     $734K (49.3%)
     ███████████████████

  3. SUBMITTED
     $5K (0.3%)
     

  4. WON
     $0K (0.0%)
     

----------------------------------------------------
  CONVERSION RATES:
  Pipeline → Ready:  49.3%
  Ready → Sent:     0.7%
  Sent → Won:       0.0%
  Overall:          0.0%
----------------------------------------------------

  BREAKDOWN:
  • Grants:    $130K (ready: $125K, sent: $5K)
  • Services:  $1.3M (ready: $609K, sent: $0K)
  • Bounties:  $50K
```

## What It Shows

**Four stages:**
1. **Pipeline Built** — Total value in pipeline
2. **Ready to Send** — Messages ready, not yet sent
3. **Submitted** — Messages sent
4. **Won** — Revenue converted

**Three conversion rates:**
- Pipeline → Ready: What % is ready to ship?
- Ready → Sent: What % of ready actually shipped? **(Execution gap)**
- Sent → Won: What % of sent converted to revenue?
- Overall: End-to-end conversion

**Breakdown by category:** Grants, Services, Bounties

## Use Cases

1. **Execution gap diagnosis** — See Ready→Sent conversion at a glance
2. **Pre-send baseline** — Capture snapshot before sending messages
3. **Post-send tracking** — Re-run to see funnel fill from bottom
4. **Weekly reviews** — Track conversion improvement over time
5. **Visual motivation** — See the gap, feel urgency to ship

## Data Source

`revenue-pipeline.json` — Must exist and contain:
- `totalPipeline`
- `categories.grants.amount/ready/submitted`
- `categories.services.amount/ready/submitted` (optional)
- `categories.bounties.amount` (optional)

## Integration

Add to daily checklist:

```bash
# Morning status
python3 tools/funnel-visualizer.py

# Before sending outreach
python3 tools/funnel-visualizer.py  # baseline
bash tools/send-everything.sh full
python3 tools/funnel-visualizer.py  # after

# Weekly review
python3 tools/funnel-visualizer.py | mail -s "Weekly Funnel" arthur@example.com
```

## Customization

Edit `draw_funnel()` to modify:
- Funnel width (max_width = 40)
- Stage labels
- Currency formatting
- Add emoji/color

## Related Tools

- `status-one-liner.sh` — Single-line status
- `revenue-tracker.py` — Full pipeline details
- `execution-gap.py` — Gap analysis in numbers

## Insights

**Key metric:** Ready → Sent conversion
- <10%: Hoarding zone (prepare → ship)
- 10-50%: Shipping zone (improve execution)
- 50-80%: Optimization zone (tweak quality)
- >80%: Scale zone (build more pipeline)

Current: 0.7% (hoarding)

---

**Insight:** The visual gap creates urgency that numbers don't.
