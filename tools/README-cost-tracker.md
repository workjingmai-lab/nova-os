# cost-tracker.py

Track daily spending and session costs from OpenClaw session logs.

## What It Does

Uses the session-logs skill patterns to analyze session JSONL files and calculate costs per day. Helps you monitor API spending and identify cost trends.

## Usage

```bash
# Generate 7-day cost report
python3 tools/cost-tracker.py

# Edit the script to change days=7 to days=30 for monthly reports
```

## How It Works

1. Reads session JSONL files from `~/.openclaw/agents/{AGENT_ID}/sessions/`
2. Uses `jq` to extract cost data from each message's `usage.cost.total` field
3. Groups costs by date (from first message timestamp)
4. Generates formatted report with visual bars

## Example Output

```
# 💰 Session Cost Report
**Generated:** 2026-02-02T13:15:00
**Sessions Analyzed:** 127

## Daily Costs (Last 7 Days)
- 2026-02-02: $0.0234 ████████████████
- 2026-02-01: $0.0198 ██████████████
- 2026-01-31: $0.0215 ███████████████
- 2026-01-30: $0.0156 ██████████
- 2026-01-29: $0.0182 █████████████
- 2026-01-28: $0.0124 █████████
- 2026-01-27: $0.0098 ██████

**Total:** $0.1207
```

## Dependencies

- `jq` - JSON query processor (install via `apt install jq` or `brew install jq`)
- Session logs in JSONL format with `usage.cost.total` field

## Configuration

Edit these variables at the top of the script:
- `AGENT_ID` - Default "main" (change for multi-agent setups)
- `SESSIONS_DIR` - Auto-derived from AGENT_ID
- `days` in `get_daily_summary()` - Report period

## Why It Matters

API costs compound silently. This tool makes spending visible, helping you optimize prompts, cache responses, or adjust model usage.

## See Also

- Session-logs skill (for advanced log querying)
- `daily-metrics.py` - For productivity tracking
- `self-improvement-loop.py` - For cost/performance analysis
