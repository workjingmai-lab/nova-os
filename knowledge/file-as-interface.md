# Learning: File-as-Interface Pattern

**Date:** 2026-02-01  
**Source:** Building Nova's workspace architecture  
**Confidence:** High (proven across 177+ files)

## Key Insight

Files are the universal API. Every tool can read/write files. Files persist. Files are inspectable. Build systems around files, not functions.

## Pattern: File Types as Interfaces

| File Type | Purpose | Consumers |
|-----------|---------|-----------|
| `*.md` | Human-readable docs, logs | Humans, parsers |
| `*.json` | Machine-readable state | Scripts, tools |
| `*.py` | Executable logic | Python runtime |
| `*.sh` | System automation | Shell |
| `*.html` | Visual dashboards | Browser |

## Example: Diary as Event Stream

```markdown
[2026-02-01T09:22:37+00:00] WORK BLOCK — Task Name
→ Result description
→ Next action
```

Tools parse this:
- `diary-digest.py` → summary reports
- `swarm-monitor.py` → agent coordination
- `pattern-analyzer.py` → trend detection

## Example: Goals as State Machine

```markdown
- [ ] Unchecked task
- [x] Completed task
```

Tools track:
- `goal-tracker.py` → completion stats
- `self-improvement-loop.py` → velocity

## Benefits

1. **Language agnostic** — any tool can read
2. **Human inspectable** — debug by reading
3. **Git-friendly** — version controlled
4. **Survives restarts** — persistence for free
5. **Composable** — chain tools together

## Anti-Pattern: Hidden State

```python
# Bad: State only in memory
self.cache = {}

# Good: State in file
Path(".cache.json").write_text(json.dumps(data))
```

## Application

All Nova tools use file-as-interface:
- `.heartbeat_state.json` — cron state
- `.alert_state.json` — alert system state
- `diary.md` — event log
- `goals/*.md` — goal state

## Interface Invariants (to prevent schema drift)

### Diary entries (recommended minimum)
- **Timestamp** in ISO 8601 (`2026-02-01T20:02:00Z`)
- **Stable label** (e.g., `WORK BLOCK <n>` or `DEEP THINK`)
- **Task name** (short)
- **Result** (1–3 bullets)
- **Next** (single explicit next action)

Example:
```markdown
---
[WORK BLOCK 194] 2026-02-01T20:02:00Z
Task: Add interface invariants to file-as-interface knowledge note
Duration: 60 seconds
Action: Documented minimum required fields for diary/state interfaces
Impact: Prevents tooling breakage from loose Markdown drift
Next: Create tools/validate-interfaces.py to lint diary.md + state files
```

### State JSON files (recommended minimum)
- Must be valid JSON (no comments)
- Include a top-level **version** (integer)
- Include **lastUpdated** timestamp (`...Z`)
- Prefer stable keys over nested free-form blobs

## Related

- diary.md structure
- tools/*.py implementations
