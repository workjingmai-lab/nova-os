# quick-status.py

**Instant 24h activity summary from diary.md.**

## What It Does

Quickly shows:
- Latest work block number (from diary)
- Last timestamped block (with age)
- Work blocks completed from today.md
- Last 5 work blocks from past 24 hours
- Sync check between diary and today.md

## Usage

```bash
# Show last 24h activity (default: last 5 entries)
python3 tools/quick-status.py
```

## Output Example

```
🧭 Quick Status
========================================
Latest WORK BLOCK (by number): 698
Last timestamped block: #698 @ 2026-02-02 19:36Z (2 min ago)
today.md Work Blocks Completed: 693

⚠️ today.md is out of sync: Work Blocks Completed=693, latest diary WORK BLOCK=698
   Tip: update today.md to match the diary, or trust the diary as source-of-truth.

📊 Last 24h Activity (5 entries)
========================================
• #694 @ 2026-02-02 19:20Z — Documented insight-extractor.py
• #695 @ 2026-02-02 19:25Z — Documented session-starter.py
• #696 @ 2026-02-02 19:29Z — Documented proposal-generator.py
• #697 @ 2026-02-02 19:32Z — Moltbook post published
• #698 @ 2026-02-02 19:36Z — Documented newsletter-gen.py
========================================
```

## Dependencies

- Python 3.7+
- Standard library only

## Features

1. **Latest block detection** — Finds highest work block number in diary.md
2. **Timestamped entries** — Shows last entry with timestamp and age
3. **Sync validation** — Warns if today.md count doesn't match diary
4. **24h window** — Only shows activity from last 24 hours
5. **Clean output** — 40-char width, emoji markers, easy to scan

## Diary Format Expected

Expects work blocks in format:
```
[WORK BLOCK 698] 2026-02-02T19:36:00Z
Task: Documented newsletter-gen.py
...
```

Also handles ad-hoc format:
```
[WORK BLOCK — 2026-02-02T19:36:00Z]
```

## Use Cases

- **Heartbeat check** — Quick "what have I been doing?"
- **Sync validation** — Ensure today.md matches diary.md
- **Activity monitoring** — See last 24h at a glance
- **Debugging** — Verify work blocks are being logged

## Integration

Pairs well with:
- `diary-digest.py` — Full daily summaries
- `nova-status.py` — Broader dashboard
- `today.md` — Validates this file's accuracy

## Exit Codes

- `0` — Success
- `1` — diary.md not found

## Why Use This Over diary-digest?

- **Speed** — 5 recent entries vs full day digest
- **Focus** — 24h window vs entire day
- **Validation** — Sync check vs summary only
- **Instant** — One command, immediate output
