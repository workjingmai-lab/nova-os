# swarm-monitor.py

Agent swarm monitor — track multi-agent collaboration from diary entries.

## What It Does

Parses diary.md for multi-agent collaboration markers and generates reports:
- **Claims:** Tasks claimed by agents (`CLAIM: task by agent`)
- **Handoffs:** Tasks transferred between agents (`## HANDOFF — agentA → agentB`)
- **Status:** Agent status updates (`## STATUS — agentName`)

## Installation

No external dependencies. Uses Python standard library only.

## Quick Start

```bash
python3 tools/swarm-monitor.py
```

**Output:**
```
📊 Swarm Status
   Claims: 3 | Handoffs: 2 | Statuses: 1

📄 Full report saved to reports/swarm-status.md
```

**Report example:**
```markdown
# Agent Swarm Report
Generated: 2026-02-02T23:55Z

## Summary
- Active Claims: 3
- Handoffs Completed: 2
- Status Updates: 1

## Recent Claims
- `research-task` → Nova
- `write-documentation` → Orbit
- `test-feature` → Nova

## Recent Handoffs
- Nova → Orbit (15 minutes)
- Orbit → Nova (2 hours)

## Agent Status
- **Nova**: Testing complete, 90% done (updated 2026-02-02T23:00Z)
```

## Diary Entry Format

### Claim marker
```markdown
CLAIM: task_name by agent_name
```

### Handoff section
```markdown
## HANDOFF — agentA → agentB

**Completed:** [list of done items]
**Remaining:** [list of pending items]
**Notes:** [context for next agent]
```

### Status section
```markdown
## STATUS — agent_name

**Last Update:** 2026-02-02T23:00Z
**Progress:** 75% complete, blocked on X
**Next Steps:** [action items]
```

## Use Cases

- **Swarm coordination:** Track which agent owns which task
- **Handoff tracking:** Monitor task transfers between agents
- **Status overview:** See what every agent is working on
- **Collaboration history:** Review past handoffs and claims
- **Multi-agent projects:** Coordinate complex workflows across agents

## Features

- **Pattern-based parsing:** Uses regex to find collaboration markers
- **Report generation:** Creates markdown summary with recent activity
- **Last-5 focus:** Shows most recent 5 entries per category
- **Flexible source:** Can parse any diary-like file
- **Lightweight:** No external dependencies

## Command-Line Options

```bash
# Default: read from diary.md, save to reports/swarm-status.md
python3 tools/swarm-monitor.py

# Custom source file
python3 tools/swarm-monitor.py --source memory/2026-02-02.md

# Custom output file
python3 tools/swarm-monitor.py --output reports/swarm-weekly.md

# Print to stdout only (no file saved)
python3 tools/swarm-monitor.py --stdout
```

## Integration

### Heartbeat example
```yaml
- name: "Swarm Status Check"
  every: "30m"
  message: |
    Check swarm collaboration status.
    python3 tools/swarm-monitor.py
```

### Cron example
```bash
# Generate hourly swarm report
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/swarm-monitor.py
```

## Return Codes

- `0` — Success (report generated)
- `1` — Error (file not found or parse error)

## Best Practices

1. **Consistent markers:** Use standard CLAIM/HANDOFF/STATUS format
2. **Agent names:** Use consistent agent identifiers (Nova, Orbit, etc.)
3. **Timestamps:** Include ISO 8601 timestamps in status updates
4. **Handoff notes:** Provide context when transferring tasks
5. **Regular reports:** Generate reports every 30-60 minutes during active collaboration

## Examples

### Before handoff
```markdown
## HANDOFF — Nova → Orbit

**Completed:**
- Research on topic X
- Drafted outline

**Remaining:**
- Write full documentation
- Add examples

**Notes:** Use `tool-usage-patterns.md` as reference
```

### After accepting
```markdown
## STATUS — Orbit

**Last Update:** 2026-02-02T23:55Z
**Progress:** 20% — Outline received, starting draft
**Next Steps:** Complete sections 1-3, add code examples
```

## Troubleshooting

**No claims found:**
- Check that CLAIM format is correct: `CLAIM: task by agent`
- Ensure diary.md exists and has entries

**Report missing latest entries:**
- Swarm monitor shows last 5 entries only
- Check diary.md for correct formatting

**Parse errors:**
- Ensure HANDOFF/STATUS sections use proper markdown headers (##)
- Check for special characters in agent names

## See Also

- `diary.md` — Primary source for swarm activity
- `sessions_spawn` — Create sub-agent sessions for collaboration
- `sessions_send` — Send messages between agents
- `memory/` — Long-term storage for handoff history

---

**Created:** Week 2 (Feb 2026)
**Purpose:** Coordinate multi-agent collaboration without external tools
**Impact:** Enables seamless task handoffs between Nova, Orbit, and other agents
