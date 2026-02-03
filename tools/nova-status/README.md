# nova-status.py

**Instant snapshot.** Quick status report of Nova's current state.

## What It Does

Generate a real-time status report showing:
- Heartbeat file count
- Diary entry count
- Tool count
- Work block count
- Current session info
- Model status
- System vitals

## Usage

```bash
# Generate status report
python3 tools/nova-status.py

# Verbose mode (more details)
python3 tools/nova-status.py --verbose

# JSON output
python3 tools/nova-status.py --json
```

## Output

Text snapshot:
```
NOVA STATUS — 2026-02-02 19:12 UTC

📊 Metrics:
  Work blocks: 688
  Tools: 112
  Heartbeats: 177

🔥 Sessions:
  Active: 3
  Models: Stable

✅ Status: Nominal
```

## Why It Matters

**Visibility = control.**

When you're running continuous work loops, you need to know:
- Am I on track?
- Is anything blocked?
- What's the velocity?

This tool gives you an instant health check.

## Use Cases

- Quick check-ins during work
- Status reports for Arthur
- Debugging session state
- Performance monitoring

## Part of Nova's Toolkit

Monitoring — always know where you stand.
