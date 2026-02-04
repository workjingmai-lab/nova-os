# trim-today.py — Context Size Reducer

**Purpose:** Trim `today.md` to only the current session, archive old sessions to `memory/YYYY-MM-DD.md`. Reduces injected context by ~50% (saves ~4k tokens per session).

**When to use:** Run on session startup (automated via HEARTBEAT.md) or when today.md grows beyond 50KB.

---

## What It Does

1. **Finds the current session** — First/newest "Latest Session (N):" entry
2. **Archives old sessions** — Moves everything except current to `memory/YYYY-MM-DD.md`
3. **Keeps current session** — today.md contains only the active session
4. **Reports savings** — Bytes removed, percentage reduction, sessions archived

---

## Usage

```bash
# Run directly (default: trims today.md, archives to memory/)
python3 tools/trim-today.py

# Recommended: Run on session startup (see HEARTBEAT.md)
python3 tools/trim-today.py 10  # Keep last 10 sessions (optional, not implemented)
```

---

## Example Output

```
Only 1 session found. No trimming needed.
```

Or:

```
Archived sessions (except current) to memory/2026-02-04.md
Trimmed 15 old sessions (archived to memory/). Kept current session only.
Reduced size from 61234 to 30512 bytes (50%)
```

---

## Why It Matters

- **Token savings:** 50KB → 30KB = ~4k tokens saved per session
- **Faster sessions:** Less injected context = faster response times
- **Memory preservation:** Old sessions archived, not lost
- **Automated:** Runs on session startup via HEARTBEAT.md

---

## Integration

**HEARTBEAT.md startup task:**
```yaml
- name: "Session Startup"
  every: "startup"
  message: |
    On NEW session start:
    1. Run: python3 tools/trim-today.py
    2. Continue with normal session work
```

---

## Technical Details

- **Input:** `/home/node/.openclaw/workspace/today.md`
- **Output:** Same file (trimmed), plus `memory/YYYY-MM-DD.md` (archive)
- **Pattern:** Matches `**Latest Session (N):` to identify sessions
- **Archive date:** Uses current date (YYYY-MM-DD format)
- **Safety:** Only trims if 2+ sessions exist; keeps newest session

---

## Dependencies

- Python 3.6+
- Standard library only (`re`, `datetime`, `sys`)

---

## Created

2026-02-04 — Work block 1416
