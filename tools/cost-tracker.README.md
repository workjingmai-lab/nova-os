# cost-tracker.py — Session Cost Analyzer

**Purpose:** Track daily OpenClaw spending and session costs using session logs.

## What It Does

- Parses session JSONL files using jq
- Extracts usage.cost.total from messages
- Generates daily cost summaries with visual bar charts
- Reports total spend over last N days (default: 7)

## Usage

```bash
# Run standalone
python3 tools/cost-tracker.py

# Output format
# 💰 Session Cost Report
# **Generated:** 2026-02-04T06:45:00
# **Sessions Analyzed:** 47
# 
# ## Daily Costs (Last 7 Days)
# - 2026-02-04: $0.4523 ████████████████████████████████
# - 2026-02-03: $0.3812 ████████████████████████
# ...
# **Total:** $2.1234
```

## Dependencies

- `jq` (JSON query tool)
- Session logs at `~/.openclaw/agents/main/sessions/*.jsonl`

## Use Cases

- **Cost monitoring:** Track daily AI spending
- **Budget alerts:** Identify high-cost days
- **Optimization:** Find expensive sessions to optimize

## Data Source

Reads from: `~/.openclaw/agents/main/sessions/*.jsonl`

Each session file contains messages with `usage.cost.total` fields (USD).

## Output

Returns formatted markdown report with:
- Generation timestamp
- Number of sessions analyzed
- Daily cost breakdown with visual bars
- Total cost for period

## Notes

- Skips deleted sessions (files containing ".deleted.")
- Requires valid JSONL format
- Costs are summed per calendar day
- Default 7-day lookback, configurable in `get_daily_summary()`
