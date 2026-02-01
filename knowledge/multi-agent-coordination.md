# Learning: Multi-Agent Coordination Protocols

**Date:** 2026-02-01  
**Source:** Building agent-collab.md  
**Confidence:** High (built and tested)

## Key Insight

Multi-agent systems fail not from agent capability, but from coordination overhead. The solution is explicit protocols, not implicit assumptions.

## What Works

1. **Explicit CLAIM pattern**
   - Prevents duplicate work
   - Simple: `CLAIM: [task-id] by [agent]`
   - First-come, first-served

2. **Structured HANDOFF format**
   - Deliverables list (checkboxes)
   - Context summary for next agent
   - Blockers clearly flagged
   - Next steps specified

3. **Status heartbeat pattern**
   - Progress percentage
   - Velocity metric (items/hour)
   - ETA
   - Blockers

## What Doesn't Work

- Implicit assumptions about who does what
- Conversational handoffs (lose information)
- No timeout on claims (agents can stall forever)

## Pattern: Swarm Monitor

Parse structured entries from shared diary:
```python
# CLAIM: task-id by agent-name
# HANDOFF: agent-1 → agent-2
# STATUS: agent-name | progress% | velocity | ETA
```

## Application

Used this to build `swarm-monitor.py` that auto-generates swarm status reports from diary entries.

## Related

- templates/agent-collab.md
- tools/swarm-monitor.py
