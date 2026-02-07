# system-health.py

Quick health check for all revenue execution systems.

## Usage

```bash
python3 tools/system-health.py
```

## Output

Shows status of:
- Revenue pipeline data
- Core tools (5)
- Knowledge base (5 docs)
- Arthur guides (4 docs)
- Pipeline summary ($ totals)

## Quick Check

```bash
# Full health report
python3 tools/system-health.py

# Key systems only
cd /home/node/.openclaw/workspace && python3 tools/system-health.py | grep -E "(✓|✗|Total|Ready|Status:)"
```
