# pipeline-readiness.py

**What % of your pipeline is actually ready to send?**

Distinguishes between "identified opportunities" vs "ready-to-ship" opportunities.

## Usage

```bash
python3 tools/pipeline-readiness.py
```

## Output

Shows for each category (grants, services, bounties):
- Total items identified
- Items ready to submit (%)
- Items submitted (%)
- Potential value
- Execution gap (ready but not sent)

## Example

```
GRANTS:
  Total items: 5
  Ready to submit: 5 (100.0%)
  Submitted: 0 (0.0%)
  Potential value: $130,000

EXECUTION GAP:
  Items ready but not sent: 5
```

## Why This Matters

100% readiness with 0% submissions = execution problem, not preparation problem.

**Readiness gap:** Items needing work before sending
**Execution gap:** Items ready but sitting unsubmitted

## Data Source

Reads from `revenue-pipeline.json` (the master pipeline tracking file).

## Created

Work block #1838 — 2026-02-05
