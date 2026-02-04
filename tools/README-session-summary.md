# session-summary.py — Quick Session Snapshot

**Purpose:** Display a quick summary of the current session's work blocks and recent wins.

**Size:** 1,668 bytes

## What It Does

- Parses today.md to extract current work block count
- Loads recent wins from .wins.json
- Displays timestamped session summary with work blocks and last 5 wins

## Usage

```bash
python tools/session-summary.py
```

## Example Output

```
📊 Session Summary — 2026-02-03 06:33 UTC
🔸 Work Blocks: 969
🔸 Recent Wins (5):
   06:28 | Documentation sprint — Created README for lightweight-browser.py
   06:25 | Documentation sprint — Created README for workspace-map.py
   06:22 | Documentation sprint — Created README for work-block-tracker.py
   06:19 | Documentation sprint — Created README for tool-organizer.py
   06:15 | Documentation sprint — Created README for web-lead-extractor.py
```

## Dependencies

- `today.md` — Parses for work block count
- `.wins.json` — Loads recent wins log

## Use Cases

- Quick session status check
- See recent progress at a glance
- Validate work block tracking

## Insight

"Session visibility = momentum awareness. See what you've done, know where you're going."
