# next-action-recommender.py

Analyzes current pipeline state and recommends the highest-ROI next action.

## What It Does

- Scans revenue-pipeline.json for current state
- Identifies blocked value, ready messages, and follow-ups
- Prioritizes actions by ROI
- Provides specific commands and time estimates

## Usage

```bash
python3 tools/next-action-recommender.py
```

## Output Example

```
============================================================
  🎯 NEXT ACTION RECOMMENDER
============================================================

🔴 PRIORITY 1: Unblock $50,000
   → Action: Run 'openclaw gateway restart'
   → Time: 1 minute
   → ROI: $50,000/min

🟢 PRIORITY 2: Send 10 service messages ($305,000)
   → Action: See outreach/TOP-3-LEADS-NOW.md
   → Time: 20 minutes (2 min per message)
   → ROI: $15,250/min

🔵 PRIORITY 4: Check for follow-ups
   → Action: Run 'python3 tools/follow-up-reminder.py'
   → Time: 1 minute

============================================================
  📊 SUMMARY
============================================================
Ready to send: 10 messages ($305,000)
Blocked value: $50,000
Total pipeline: $2,290,350
```

## Priority Logic

1. **PRIORITY 1 (Red):** Unblock blocked value
   - Usually gateway restart (1 min → $50K+)
   - Highest ROI: $50K/min

2. **PRIORITY 2 (Green):** Send ready service messages
   - Zero blockers, ready to execute
   - High ROI: ~$15K/min

3. **PRIORITY 3 (Yellow):** Submit grant applications
   - Only shown when unblocked
   - Medium ROI

4. **PRIORITY 4 (Blue):** Check for follow-ups
   - Maintains pipeline momentum
   - Low time investment

## Why It Matters

**Eliminates decision fatigue.**

When there are multiple tasks (unblock, send messages, submit grants, follow-ups), it's easy to waste time deciding what to do first. This tool tells you exactly what to execute next based on ROI.

**Example:** Instead of spending 5 minutes thinking "what should I do?", you get an instant recommendation: "Run gateway restart (1 min → $50K)."

## Integration

Use in daily workflow:

```bash
# Morning: Check what to do today
python3 tools/next-action-recommender.py

# After completing tasks: Check next action
python3 tools/next-action-recommender.py
```

## Data Sources

- **revenue-pipeline.json** — Main pipeline data
- **outreach/BLOCKER-STATUS.md** — Blocker information

## Related Tools

- **revenue-tracker.py** — Pipeline tracking and management
- **follow-up-reminder.py** — Follow-up detection
- **lead-prioritizer.py** — Lead ranking by ROI
- **QUICK-PIPELINE-SNAPSHOT.md** — Single-page pipeline summary

## Author

Created by Nova — Work block 1681

## Version

1.0 — Initial release
