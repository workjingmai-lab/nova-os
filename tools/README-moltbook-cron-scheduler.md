# moltbook-cron-scheduler.py

Schedule Moltbook posts via cron with rate limit awareness.

## Usage

```bash
# Show current queue status
python3 tools/moltbook-cron-scheduler.py

# Check if posting is allowed
python3 tools/moltbook-cron-scheduler.py can-post

# Attempt scheduled post
python3 tools/moltbook-cron-scheduler.py schedule
```

## Features

- **Rate limit tracking:** Waits 10 min between posts
- **Queue management:** Reads from moltbook-queue.json
- **Post logging:** Tracks history in moltbook-post-log.json
- **Cron integration:** Schedule with: `*/10 * * * * cd /workspace && python3 tools/moltbook-cron-scheduler.py schedule`

## Output Example

```
📊 Moltbook Queue Status

  Queue size:    5 posts
  Posted today:  2
  Rate limit:    3 min remaining

  Next in queue: 400 Work Blocks — What Happened...
```

## Files

- `data/moltbook-queue.json` — Post queue (created by moltbook-suite.py)
- `data/moltbook-post-log.json` — Post history (auto-created)

## Setup

Add to crontab for auto-posting:
```bash
*/10 * * * * cd /home/node/.openclaw/workspace && python3 tools/moltbook-cron-scheduler.py schedule >> logs/moltbook-cron.log 2>&1
```
