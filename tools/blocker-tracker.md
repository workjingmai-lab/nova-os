# blocker-tracker.md — Track and Resolve Blockers

**Version:** 1.0  
**Category:** Workflow / Issue Tracking  
**Created:** 2026-02-01

---

## What It Does

Tracks blockers (dependencies, issues, waiting states) and monitors their status over time.

### Features

- Log blockers with severity levels
- Categorize by type (technical, external, resource)
- Track resolution time
- Generate blocker reports
- Integrate with `today.md` for visibility

---

## Usage

```bash
# Log a new blocker
python3 tools/blocker-tracker.py add "Browser access blocked" --type technical --severity high

# Mark blocker as resolved
python3 tools/blocker-tracker.py resolve 1

# List active blockers
python3 tools/blocker-tracker.py list

# Generate blocker report
python3 tools/blocker-tracker.py report

# Show blockers by type
python3 tools/blocker-tracker.py list --type external
```

---

## Blocker Types

| Type | Description | Examples |
|------|-------------|----------|
| `technical` | Technical issues | Browser down, API failure |
| `external` | Waiting on others | Arthur action, third-party response |
| `resource` | Missing resources | No API key, insufficient permissions |
| `knowledge` | Knowledge gap | Don't know how to proceed |

---

## Severity Levels

- `low` — Nice to have, not blocking
- `medium` — Slows progress, workaround exists
- `high` — Completely blocked, no workaround
- `critical` — Urgent, needs immediate attention

---

## Storage

Blockers stored in `.blockers.json`:

```json
{
  "blockers": [
    {
      "id": 1,
      "description": "Browser access blocked",
      "type": "technical",
      "severity": "high",
      "status": "active",
      "created": "2026-02-02T20:45:00Z",
      "resolved": null
    }
  ]
}
```

---

## Dependencies

- Python 3.7+
- Standard library only

---

## Integration

- Pair with `today.md` for daily blocker visibility
- Use `goal-tracker.py` to link blockers to goals
- Feed into `self-improvement-loop.py` for analytics

---

## Tips

1. Log blockers immediately when discovered
2. Update status as conditions change
3. Review blockers weekly during retrospective
4. Categorize accurately for pattern analysis
5. Set severity based on impact, not urgency
