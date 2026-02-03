# quick-log.md — Fast Diary & Note Logger

**Version:** 1.0  
**Category:** Logging / Workflow  
**Created:** 2026-02-01

---

## What It Does

Quickly log entries to `diary.md` or custom files. Faster than opening an editor for quick notes.

### Features

- Instant logging to diary
- Auto-timestamps
- Category tagging
- Multi-file support
- Minimal friction
- Batch logging

---

## Usage

```bash
# Quick log to diary
python3 tools/quick-log.py "Completed tool documentation"

# Log with category
python3 tools/quick-log.py "Milestone hit" --category milestone

# Log to custom file
python3 tools/quick-log.py "Meeting notes" --file notes/meeting-2026-02-02.md

# Batch log (multiple entries)
python3 tools/quick-log.py --batch << EOF
Entry 1
Entry 2
Entry 3
EOF

# Show recent logs
python3 tools/quick-log.py --recent 5
```

---

## Categories

| Category | Use Case |
|----------|----------|
| `work` | Work block completions |
| `milestone` | Major achievements |
| `lesson` | Key learnings |
| `blocker` | Issues encountered |
| `idea` | Ideas for later |
| `meeting` | Meeting notes |

---

## Entry Format

```markdown
## 🔥 WORK BLOCK #742 (2026-02-02T20:55Z)
**Category:** milestone
**Entry:** Completed tool documentation sprint (109/112 tools)
**Tags:** #documentation #sprint-complete
```

---

## Dependencies

- Python 3.7+
- `diary.md` for default logging

---

## Storage

- Default: `diary.md`
- Custom files: Any path specified with `--file`
- Format: Markdown with timestamps

---

## Integration

- Pair with `session-logger.sh` for session tracking
- Use `wins.py` to log achievements
- Feed into `diary-digest.py` for analysis

---

## Tips

1. Use for quick thoughts that don't deserve a full work block
2. Categorize accurately for later filtering
3. Use `--batch` for rapid-fire logging
4. Review logs weekly to extract patterns
5. Keep it frictionless — the faster logging is, the more you'll log
