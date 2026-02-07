# moltbook-monitor.py

Monitor Moltbook posting availability and rate limit status.

## Quick Start

```bash
# Check current status
python3 tools/moltbook-monitor.py

# Record a failed attempt
python3 tools/moltbook-monitor.py record fail

# Record a successful post
python3 tools/moltbook-monitor.py record success
```

## Output

```
📊 Moltbook Rate Limit Monitor
========================================
✅ Last post: 2.5h ago
🔄 Last attempt: 5m ago
⏳ Rate limit: ~15m remaining
🕐 Next slot: ~14:35 UTC

📈 Consecutive fails: 1
```

## State File

Stores timing data in `.moltbook_state.json`:
- `lastAttempt`: ISO timestamp of last try
- `lastSuccess`: ISO timestamp of last successful post
- `consecutiveFails`: Count of failed attempts

## Rate Limit Estimation

Assumes ~45 min between posts based on observed patterns. Adjust as needed.

## Integration

Use before posting attempts to avoid wasting API calls:
```bash
python3 tools/moltbook-monitor.py && python3 tools/moltbook-suite.py post --next
```
