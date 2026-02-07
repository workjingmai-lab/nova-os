# daily-revenue-report.py

Unified daily revenue report combining pipeline, ready leads, and conversion stats.

## Usage

```bash
python3 tools/daily-revenue-report.py
```

## Output

- Pipeline summary (total, ready, sent, won)
- Response rate and win rate percentages
- Top 5 ready leads with ROI
- Recommended next actions

## Dependencies

- `data/conversion-log.json` (created by conversion-tracker.py)
- Run `python3 tools/conversion-tracker.py init-ready-leads` first

## Integration

Add to daily routine or heartbeat for automatic revenue visibility.
