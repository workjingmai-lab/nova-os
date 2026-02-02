# quick-status.py

**Purpose:** Quick 24-hour activity summary from diary.md — see what you've been working on recently.

## What It Does

- **Parses diary.md** — Extracts work blocks from last 24 hours
- **Shows activity** — Displays most recent tasks with timestamps
- **Tracks sync** — Compares diary.md block numbers with today.md
- **Highlights gaps** — Warns if today.md is out of sync

## When to Use It

**Run anytime** to:
- Get quick overview of recent work
- Check how long since last work block
- Verify today.md sync with diary.md
- See 24-hour activity at a glance

## Usage

```bash
# Show last 24 hours of activity
python3 tools/quick-status.py

# Show last 10 entries (default: 5)
python3 tools/quick-status.py --limit 10

# Check specific diary file
python3 tools/quick-status.py --diary path/to/diary.md
```

## Output Format

```
🧭 Quick Status
========================================
Latest WORK BLOCK (by number): 590
Last timestamped block: #590 @ 2026-02-02 13:31Z (0 min ago)
today.md Work Blocks Completed: 580

⚠️ today.md is out of sync: Work Blocks Completed=580, latest diary WORK BLOCK=590
   Tip: update today.md to match the diary, or trust the diary as source-of-truth.

📊 Last 24h Activity (5 entries)
========================================
• #586 @ 2026-02-02 13:27Z — Document agent-collaboration.py
• #587 @ 2026-02-02 13:29Z — Document cost-tracker.py
• #588 @ 2026-02-02 13:29Z — Document find-diary-duplicate-workblocks.py
• #589 @ 2026-02-02 13:30Z — Documentation sprint reflection
• #590 @ 2026-02-02 13:31Z — Document daily-briefing.py
========================================
```

## Diary Format Expected

```
---
[WORK BLOCK 173] 2026-02-01T19:06:00Z
Task: Document blocker-tracker.py
Result: Created README
...
---
```

## Features

### Sync Detection
Compares `today.md` "Work Blocks Completed" with latest diary block number:
- **In sync:** Both numbers match
- **Out of sync:** Warning displayed with tip to update

### Time Tracking
Shows time since last work block:
- `0 min ago` — Just now
- `15 min ago` — Recent activity
- `2 hours ago` — Gap detected

### 24-Hour Window
Only shows work blocks from last 24 hours — older activity filtered out.

## Why It Matters

**Quick context without re-reading everything.** This tool helps you:
- **Resume fast** — See what you were working on last
- **Detect gaps** — Notice when you haven't worked in a while
- **Stay synced** — Keep today.md accurate with diary.md
- **Track velocity** — See how many work blocks in last 24 hours

**For autonomous agents:** Get situational awareness in one command. No need to parse the full diary.

## Integration

- **Session start:** Run to see recent context
- **Before handoff:** Show recent work to collaborators
- **Velocity check:** See 24-hour output at a glance
- **Sync validation:** Ensure today.md matches diary.md

## Customization

**Change time window:**
```python
cutoff = now - timedelta(hours=48)  # 48 hours instead of 24
```

**Change default limit:**
```python
def last_24h_summary(path: str = "diary.md", limit: int = 10):  # Show 10 instead of 5
```

**Add velocity calculation:**
```python
velocity = len(recent) / 24  # Work blocks per hour
print(f"Velocity: {velocity:.1f} blocks/hour")
```

## Requirements

- **diary.md** — Work log in standard Nova format
- **today.md** — (optional) Daily working memory with "Work Blocks Completed" field

## Exit Codes

- **0:** Success
- **1:** diary.md not found

---

*Created: Week 2 — Part of quick reference tools*
