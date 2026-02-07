# quick-status.py

One-command status dashboard for Nova's systems.

## Usage

```bash
python3 tools/quick-status.py
```

## Output

Shows unified view of:
- 📊 Work blocks (total + session)
- 💰 Pipeline (total, ready, submitted, won)
- 🚧 Blockers (active + ROI)
- 📈 Conversion (sent, responses, won)

## Why

Instead of running 4+ separate commands, get everything in one view.

## Requirements

- `.heartbeat_state.json` for work blocks
- `revenue-tracker.py` for pipeline
- `operator-status.py` for blockers
- `conversion-pulse.py` for conversion metrics
