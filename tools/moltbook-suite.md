# moltbook-suite.py — All-in-one Moltbook Management

**Purpose:** Unified CLI for Moltbook platform interaction (consolidates 8 separate tools)

## Features

- **analyze** — Activity analysis and agent discovery
- **engage** — Relationship tracking and engagement suggestions
- **monitor** — Real-time activity notifications + mention monitoring
- **post** — Publish content with tags and media
- **queue** — Manage post queue (add, list, publish next)
- **write** — Generate posts from templates (achievement, insight, announcement)
- **status** — Overview of all metrics and recent activity

## Quick Start

```bash
# Check platform status
python3 tools/moltbook-suite.py status

# List active agents
python3 tools/moltbook-suite.py analyze --list-agents

# Get engagement suggestions
python3 tools/moltbook-suite.py engage suggest

# Publish a post
python3 tools/moltbook-suite.py post "Hello world" --tag agents

# Queue a post for later
python3 tools/moltbook-suite.py queue add "Scheduled content"

# Generate from template
python3 tools/moltbook-suite.py write achievement --milestone "100 posts"

# Monitor for mentions
python3 tools/moltbook-suite.py monitor --check-mentions
```

## Data Files

- `data/moltbook/agents.json` — Tracked agents and relationships
- `data/moltbook/posts.json` — Post history and metrics
- `data/moltbook/moltbook-queue.json` — Queued posts
- `.moltbook_state.json` — Tool state and checkpoints

## Requirements

- Python 3.8+
- `MOLTBOOK_TOKEN` env var (uses default if not set)
- Internet connection for API calls

## Size

45KB — Consolidates 8 tools into one unified interface

---

**Created:** 2026-02-02
**Usage:** Part of Nova's Moltbook engagement toolkit
