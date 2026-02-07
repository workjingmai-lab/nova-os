# pipeline-viz.py

Visual pipeline status dashboard with ASCII charts and actionable next steps.

## What It Does

Provides instant visual snapshot of revenue pipeline:
- ASCII bar charts showing pipeline by stage
- Conversion funnel visualization  
- Blocker identification per source
- Lead priority breakdown
- Next actions sorted by ROI

## Usage

```bash
python3 tools/pipeline-viz.py
```

## Output Sections

### Overall Pipeline
Visual bar chart showing:
- Identified: Total pipeline value
- Ready: Qualified and ready to submit
- Submitted: In review/submitted
- Won: Closed revenue

### Conversion Funnel
Funnel visualization showing conversion rates between stages.

### By Source
Breakdown for each revenue source:
- Grants ($130K ready, blocked on GitHub auth)
- Services ($424K ready, blocked on Arthur)
- Bounties ($50K ready, blocked on gateway restart)

### Lead Status
Lead counts by priority tier:
- HIGH: 3 leads (~$115K)
- MEDIUM: 10 leads (~$127.5K)
- LOW: 26 leads

### Key Metrics
- Conversion rate
- Execution gap (ready - submitted)
- Average deal size
- Time to $100K estimate

### Next Actions
Priority-ordered action list with:
- Time required
- Value unlocked
- ROI per minute

## Example Output

```
▶ OVERALL PIPELINE
--------------------------------------------------
📊 Identified   ██████████████████████████████    $900K (100.0%)
📊 Ready        ████████████████████░░░░░░░░░░    $604K ( 67.2%)
📊 Submitted    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      $5K (  0.6%)

▶ NEXT ACTIONS (Priority Order)
--------------------------------------------------
  🔥 CRITICAL Gateway restart
           Time: 1 min │ Value: $50K │ ROI: $50K/min
```

## Files

- Tool: `tools/pipeline-viz.py`
- Quick ref: `ARTHUR-QUICK-REF.md`
- Full status: `STATUS-FOR-ARTHUR.md`

## Related Tools

- `revenue-tracker.py` — Detailed pipeline tracking
- `lead-prioritizer.py` — Lead ranking and details
- `follow-up-reminder.py` — Due follow-ups
