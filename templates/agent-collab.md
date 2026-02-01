# Agent Collaboration Template

> A lightweight protocol for multi-agent coordination

## Quick Start

```bash
# 1. Include this template in your project
cp agent-collab.md your-project/

# 2. Define your swarm
# 3. Assign roles and handoffs
# 4. Execute
```

---

## Swarm Definition

```yaml
project: "Name of collaborative project"
objective: "Clear, measurable outcome"
deadline: "YYYY-MM-DDTHH:MMZ"

agents:
  - name: "agent-1"
    role: "researcher"
    task: "What they do"
    deliverable: "What they produce"
    
  - name: "agent-2"
    role: "writer"
    task: "What they do"
    deliverable: "What they produce"
    depends_on: ["agent-1"]
```

---

## Handoff Protocol

When an agent completes their task, they create:

```markdown
## HANDOFF — [Agent Name] → [Next Agent]

**Completed:** YYYY-MM-DDTHH:MMZ
**Status:** ✅ COMPLETE | ⚠️ BLOCKED | 🔄 ITERATION

### Deliverables
- [ ] Item 1
- [ ] Item 2

### Context for Next Agent
Key information they need to know.

### Blockers (if any)
What stopped progress or what to watch for.

### Next Steps
What the receiving agent should do.
```

---

## Status Check Format

```markdown
## STATUS — [Agent Name]

**Last Update:** HH:MMZ
**Progress:** X%
**Velocity:** items/hour
**Blockers:** None | [description]
**ETA:** HH:MMZ
```

---

## Conflict Resolution

1. **Same task claimed:** First to post "CLAIM: [task-id]" wins
2. **Disagreement:** Escalate to parent agent or human
3. **Stalled agent:** 15min timeout → auto-reassign

---

## Communication Patterns

| Pattern | Use When | Format |
|---------|----------|--------|
| CLAIM | Starting work | `CLAIM: [task-id] by [agent]` |
| HANDOFF | Task complete | See Handoff Protocol above |
| STATUS | Check-in | See Status Check above |
| BLOCKED | Stuck | `BLOCKED: [task-id] — [reason]` |
| HELP | Need assistance | `HELP: [task-id] — [what's needed]` |

---

## Example: Research → Write → Review

### Phase 1: Research Agent
```
CLAIM: research-topic-1 by ResearchBot
→ executes research
→ creates HANDOFF to WriterBot
```

### Phase 2: Writer Agent
```
RECEIVED: research-topic-1 from ResearchBot
→ reads handoff
→ executes writing
→ creates HANDOFF to ReviewBot
```

### Phase 3: Review Agent
```
RECEIVED: draft-1 from WriterBot
→ reviews
→ either APPROVES or REQUESTS_ITERATION
```

---

## Integration with Nova's Tools

This template works with:
- `agent-logger.py` — track agent activity
- `diary-digest.py` — summarize swarm progress
- `goal-tracker.py` — swarm-level goal tracking

---

## Meta: Using This Template

1. Copy to your project root as `COLLAB.md`
2. Fill in swarm definition
3. Spawn agents with clear handoff expectations
4. Monitor via shared diary or status dashboard

---

*Template version: 1.0*
*Created: 2026-02-01*
*Author: Nova*
