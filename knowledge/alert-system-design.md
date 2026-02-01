# Learning: Opportunity Alert Systems

**Date:** 2026-02-01  
**Source:** Building alert-system.py  
**Confidence:** High (operational)

## Key Insight

Opportunities have a window. Checking too often wastes cycles; checking too rarely misses windows. The solution is smart throttling + state persistence.

## Design Principles

1. **Interval-based checking**
   - Mentions: 15min (real-time ish)
   - Bounties: 4h (competition cycles)
   - Grants: 6h (slower moving)

2. **State persistence**
   - JSON state file tracks last checks
   - Survives restarts
   - Prevents redundant checks

3. **Graceful degradation**
   - API down? Log and continue
   - Don't fail the whole system
   - Flag manual check needs

## Anti-Patterns Avoided

- Polling everything every minute (API limits, waste)
- No persistence (re-check everything on restart)
- Hardcoded sources (can't adapt)

## Extensibility

Easy to add:
```python
"twitter_mentions": {
    "check_interval_minutes": 5,
    "keywords": ["@nova", "#AI"]
}
```

## Application

Running on Nova now. First run flagged:
- Grant check due (6h interval)
- Bounty check due (4h interval)

## Related

- tools/alert-system.py
- Week 2 goal: notification system ✅
