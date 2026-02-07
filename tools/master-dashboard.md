# master-dashboard.py

Combined view of pipeline, velocity, and system health.

## Usage

```bash
python3 tools/master-dashboard.py
```

## Output Sections

1. **Pipeline Status** — Gap analysis and ROI
2. **Today's Velocity** — Blocks and output rate
3. **System Health** — Key components check
4. **Next Actions** — What to do next

## Quick Status

```bash
# Full dashboard
python3 tools/master-dashboard.py

# Just the summary line
python3 tools/master-dashboard.py | tail -1
```
