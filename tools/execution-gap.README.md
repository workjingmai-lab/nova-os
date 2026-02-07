# execution-gap.py — Execution Gap Visualizer

Makes the invisible visible: Shows the gap between what's ready to send and what's been submitted.

## What It Does

- **Visualizes execution gap** — Bar graph shows ready vs submitted vs gap
- **Calculates value at stake** — $X/minute left on table by not sending
- **Status indicators** — CRITICAL/WARNING/NOTICE/GOOD based on gap %age
- **Time to close** — Assumes 31 minutes to send everything (from SEND-EVERYTHING.md)

## Usage

```bash
python3 tools/execution-gap.py
```

## Output Example

```
============================================================
  EXECUTION GAP
============================================================

  Ready:        $734K
  Submitted:      $5K  ███
  Gap:          $729K  ████████████████████████████████ (99.3%)

  Time to close: 31 minutes
  Value at stake: $23,532/minute

  ⚠️  CRITICAL: Almost everything is ready but nothing sent

============================================================
```

## Why This Matters

**Execution gap = revenue left on table.**

- 99.3% gap = $729K waiting to be sent
- Every minute waited = $23,532 not pursued
- This clarity drives action

## Data Source

Reads from `revenue-pipeline.json` (managed by revenue-tracker.py).

## Formula

```
gap = ready - submitted
gap_percent = (gap / ready) * 100
value_per_minute = gap / 31
```

## Related Tools

- `revenue-tracker.py` — Track pipeline status
- `service-batch-send.py` — Send all service messages
- `SEND-EVERYTHING.md` — Complete execution workflow
