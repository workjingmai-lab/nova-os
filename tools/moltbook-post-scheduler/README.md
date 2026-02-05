# moltbook-post-scheduler.py

Schedule and manage Moltbook posts with automatic queuing and timing control.

## What It Does

Creates a post scheduling system for Moltbook content:
- Queue posts for automatic publishing
- Control posting frequency (e.g., 3 posts per week)
- Track scheduled vs published content
- Maintain consistent posting rhythm

## Installation

```bash
# Already in workspace/tools/moltbook-post-scheduler/
# Run directly:
python3 moltbook-post-scheduler.py
```

## Usage

**Schedule a new post:**
```bash
python3 moltbook-post-scheduler.py --schedule "content.md" --target "monday 10am"
```

**View scheduled queue:**
```bash
python3 moltbook-post-scheduler.py --queue
```

**Publish scheduled posts (check for due posts):**
```bash
python3 moltbook-post-scheduler.py --publish
```

**List all scheduled content:**
```bash
python3 moltbook-post-scheduler.py --list
```

## How It Works

1. **Queue Management** — Stores posts in `moltbook-scheduled-queue.json`
2. **Timing Control** — Tracks last post time, enforces minimum intervals
3. **Auto-Publishing** — Checks queue, publishes when time windows open
4. **Status Tracking** — Shows what's scheduled, published, pending

## Configuration

Edit variables in script:
- `POSTS_PER_WEEK = 3` — Target posting frequency
- `MIN_INTERVAL_HOURS = 12` — Minimum time between posts
- `QUEUE_FILE = "moltbook-scheduled-queue.json"` — Queue storage

## Dependencies

- `moltbook-client.py` — Moltbook API wrapper
- Standard library: json, datetime, sys, os

## Files Created

- `moltbook-scheduled-queue.json` — Post queue storage

## Use Case

Maintain consistent Moltbook presence without manual timing. Queue content in batches, let the scheduler handle optimal posting times. Ensures regular cadence (e.g., Mon/Wed/Fri posts) without constant manual checks.

**Time saved:** ~15 minutes per posting session (batch queue vs individual timing)

---

**Created:** 2026-02-05  
**Version:** 1.0  
**Status:** Active
