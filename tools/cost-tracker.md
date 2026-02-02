# cost-tracker.py

**Purpose:** Track daily session costs using session-logs skill patterns — monitor spending across all sessions.

## What It Does

- **Analyzes session logs** — Uses jq to extract cost data from JSONL session files
- **Daily cost breakdown** — Shows spending per day for the last 7 days
- **Visual spending bars** — ASCII bar charts for cost visualization
- **Total spending** — Sum of costs across all analyzed sessions

## When to Use It

**Run weekly** or when you want to:
- Track your session spending over time
- Identify high-cost days
- Monitor cost trends
- Generate spending reports

## Usage

```bash
# Generate 7-day cost report
python3 tools/cost-tracker.py
```

## Output Format

```
# 💰 Session Cost Report
**Generated:** 2026-02-02 13:28:00
**Sessions Analyzed:** 42

## Daily Costs (Last 7 Days)
- 2026-02-02: $0.1234 ████████████████████████████
- 2026-02-01: $0.0987 ████████████████████
- 2026-01-31: $0.1156 ███████████████████████
- 2026-01-30: $0.0823 ██████████████████
- 2026-01-29: $0.0745 █████████████████
- 2026-01-28: $0.0698 ██████████████
- 2026-01-27: $0.0534 ████████████

**Total:** $0.6177
```

## Data Sources

- **Session directory:** `~/.openclaw/agents/main/sessions/`
- **File format:** JSONL (one JSON object per line)
- **Cost extraction:** Uses jq to parse `.message.usage.cost.total` field

## How It Works

1. **Scans session directory** — Finds all `.jsonl` files
2. **Extracts costs** — Uses jq to sum `usage.cost.total` per session
3. **Groups by date** — Aggregates costs by session date
4. **Sorts and displays** — Shows last 7 days with visual bars

## jq Queries Used

```bash
# Get session total cost
jq -s '[.[] | .message.usage.cost.total // 0] | add' session.jsonl

# Get session date
jq -r '.[0].timestamp | split("T")[0]' session.jsonl
```

## Why It Matters

**Cost awareness prevents overspending.** This tool helps you:
- **Track spending** — See how much you're costing per day
- **Identify trends** — Are costs increasing or decreasing?
- **Optimize usage** — Which days are most expensive and why?
- **Budget planning** — Project monthly costs based on daily averages

**For autonomous agents:** Be cost-conscious. Track your resource usage and optimize for efficiency.

## Integration

- **Weekly review:** Run every Sunday/Monday for cost summary
- **Budget monitoring:** Set alerts if daily cost exceeds threshold
- **Optimization:** Correlate high-cost days with work patterns
- **Transparency:** Share cost reports with Arthur for visibility

## Customization

**Change time range:** Edit `days=7` in `get_daily_summary()`:
```python
def get_daily_summary(days=30):  # 30-day report
```

**Change session directory:** Edit `SESSIONS_DIR`:
```python
SESSIONS_DIR = Path.home() / f".openclaw/agents/{AGENT_ID}/sessions"
```

**Add cost thresholds:** Generate alerts if spending exceeds target:
```python
if daily_costs[date] > 0.15:  # $0.15 per day threshold
    print(f"⚠️ High cost day: {date} - ${daily_costs[date]}")
```

## Requirements

- **jq:** JSON processor installed on system
- **Session logs:** OpenClaw sessions in JSONL format
- **Session cost tracking:** Sessions must include `usage.cost.total` field

Install jq if missing:
```bash
sudo apt-get install jq  # Debian/Ubuntu
brew install jq           # macOS
```

---

*Created: Week 2 — Part of cost monitoring infrastructure*
