#!/usr/bin/env python3
"""
Work Block Tracker — Quick logging of completed work blocks.

Usage:
    python3 work-block-tracker.py "Task description" [--duration MIN] [--type TYPE]

Features:
- Quick 1-command logging to diary.md
- Auto-timestamp
- Optional duration and type
- Maintains today.md stats
"""

import sys
import json
from datetime import datetime, timezone
from pathlib import Path

# Configuration
WORKSPACE = Path.home() / ".openclaw" / "workspace"
DIARY = WORKSPACE / "diary.md"
TODAY = WORKSPACE / "today.md"
STATE = WORKSPACE / ".work-block-state.json"

def load_state():
    """Load work block state."""
    if STATE.exists():
        with open(STATE) as f:
            return json.load(f)
    return {"total_blocks": 0, "last_block": 0}

def save_state(state):
    """Save work block state."""
    with open(STATE, "w") as f:
        json.dump(state, f, indent=2)

def log_to_diary(task, duration, task_type, block_num):
    """Add entry to diary.md."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = f"""
## {timestamp.split('T')[0]} (Block {block_num})

### [WORK BLOCK] — {task_type}
**Time:** {timestamp}
**Duration:** ~{duration} minute(s)
**Type:** {task_type}

**Task:** {task}

**Status:** ✅ COMPLETE

**Velocity:** 1 work block completed in {duration} minute(s)

---
"""

    # Insert after the "Last updated" line
    with open(DIARY) as f:
        content = f.read()

    # Find the insertion point (after "---\n")
    insert_point = content.find("\n---\n\n##") + 5
    if insert_point == 4:  # Not found, append to end
        updated_content = content + entry
    else:
        updated_content = content[:insert_point] + entry + content[insert_point:]

    with open(DIARY, "w") as f:
        f.write(updated_content)

    # Update "Last updated" timestamp
    with open(DIARY) as f:
        content = f.read()

    # Extract old timestamp (can't use backslash in f-string)
    old_ts = content.split('**Last updated:** ')[1].split('\n')[0]
    content = content.replace(
        f"**Last updated:** {old_ts}",
        f"**Last updated:** {timestamp}"
    )

    with open(DIARY, "w") as f:
        f.write(content)

def update_today(block_num):
    """Update today.md stats."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not TODAY.exists():
        return

    with open(TODAY) as f:
        content = f.read()

    # Update work block count
    content = content.replace(
        f"**Work Blocks Completed:** {block_num - 1}",
        f"**Work Blocks Completed:** {block_num}"
    )

    # Update last updated timestamp
    content = content.replace(
        f"**Last FULL:**",
        f"**Latest Session ({block_num}):**\n- Quick work block logged\n- 1 minute execution\n\n**Last FULL:**"
    )

    with open(TODAY, "w") as f:
        f.write(content)

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: work-block-tracker.py \"Task description\" [--duration MIN] [--type TYPE]")
        sys.exit(1)

    task = sys.argv[1]
    duration = 1  # default
    task_type = "General"  # default

    # Parse optional args
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--duration" and i + 1 < len(sys.argv):
            duration = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--type" and i + 1 < len(sys.argv):
            task_type = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    # Load state and increment
    state = load_state()
    state["total_blocks"] += 1
    state["last_block"] += 1
    block_num = state["last_block"]

    # Log to diary
    log_to_diary(task, duration, task_type, block_num)

    # Update today.md
    update_today(block_num)

    # Save state
    save_state(state)

    print(f"✅ Block {block_num} logged: {task} ({duration} min)")

if __name__ == "__main__":
    main()
