# novabrowser_watch_tail.sh — Live Browser Log Monitor

**Version:** 1.0  
**Category:** Monitoring / Browser  
**Created:** 2026-02-01

---

## What It Does

Monitors browser control logs in real-time. Shows recent activity, errors, and status changes.

### Features

- Tails live browser log file
- Filters by severity (INFO, WARN, ERROR)
- Highlights errors in red
- Auto-rotates if log exceeds size limit
- Exit on error code detection

---

## Usage

```bash
# Monitor browser logs
./tools/novabrowser_watch_tail.sh

# Show last 50 lines then tail
./tools/novabrowser_watch_tail.sh -n 50

# Filter for errors only
./tools/novabrowser_watch_tail.sh --errors-only

# Custom log path
./tools/novabrowser_watch_tail.sh --log /path/to/browser.log
```

---

## What It Monitors

- Page navigation events
- Click actions and selectors
- Form submissions
- Console errors
- Screenshot captures
- Session timeouts

---

## Output Format

```bash
$ ./tools/novabrowser_watch_tail.sh

🔍 NOVA BROWSER LOG MONITOR
Watching: /tmp/novabrowser.log
────────────────────────────────────────────────────────────
[2026-02-02 20:45:12] INFO  Navigated to https://example.com
[2026-02-02 20:45:13] INFO  Clicked button: [aria-label="Submit"]
[2026-02-02 20:45:14] WARN  Element not found: [data-testid="rare"]
[2026-02-02 20:45:15] ERROR Navigation timeout after 30s
[2026-02-02 20:45:16] INFO  Captured screenshot: screenshot-20260202-204516.png
```

---

## Dependencies

- `tail` — Log tailing
- `grep` — Filtering
- Terminal with color support

---

## Configuration

Edit variables:

```bash
LOG_FILE="${LOG_FILE:-/tmp/novabrowser.log}"
MAX_LOG_SIZE="${MAX_LOG_SIZE:-100M}"
FILTER_LEVEL="${FILTER_LEVEL:-INFO}"  # INFO, WARN, ERROR
HIGHLIGHT_ERRORS="${HIGHLIGHT_ERRORS:-true}"
```

---

## Integration

- Pair with `nova_browser.py` for browser automation
- Use `lightweight-browser.py` for simpler monitoring
- Feed errors into `blocker-tracker.py` for issue tracking

---

## Tips

1. Run in separate terminal during browser automation sessions
2. Use `--errors-only` to focus on problems
3. Monitor log size to prevent disk bloat
4. Save interesting sessions for analysis
