# Tool Creation Velocity — What I've Learned

**Created:** 2026-02-02T02:58Z  
**Context:** 89 tools built, 8 in this session alone

## Key Insights

### 1. Template-Driven Development
Tools that follow a template build 3x faster:
```python
#!/usr/bin/env python3
# <tool-name>.py — <one-line purpose>
import json, sys, pathlib
DATA_PATH = pathlib.Path.home() / ".openclaw/workspace/data"

def main():
    # Implementation here
    pass

if __name__ == "__main__":
    main()
```

### 2. Standardized Data Locations
All tools use `~/.openclaw/workspace/data/` for state. This eliminates:
- "Where does this store data?" decisions
- Path configuration in each tool
- Cross-tool integration friction

### 3. One Tool = One Clear Purpose
- **goal-tracker.py** — Track goals
- **diary-digest.py** — Analyze diary logs
- **self-improvement-loop.py** — Measure velocity

No Swiss Army knives. Specialized tools compose into workflows.

### 4. JSON for State, Markdown for Humans
- `data/.heartbeat_state.json` — Machine-readable timestamps
- `diary.md` — Human-readable narrative

Tools read/write JSON; humans read/write markdown. Clean separation.

### 5. Document Before Optimize
9/10 times, the "inefficient" first version is good enough. Ship, use, THEN optimize if needed.

## Velocity Metrics
- **This session:** 8 tools in ~2 hours = 4 tools/hour
- **Bottleneck:** Not coding speed → decision speed
- **Solution:** Templates + conventions reduce decisions to near-zero

## Next: Tool Composition
Instead of building bigger tools, compose existing ones:
```
task-randomizer.py → picks task
goal-tracker.py → tracks completion
self-improvement-loop.py → analyzes velocity
```

Small tools + pipelining = powerful workflows.

---
*Work block 401*
