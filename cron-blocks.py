#!/usr/bin/env python3
"""
cron-blocks.py — Track cron-triggered work block execution

Purpose: Measure velocity and completion rate of scheduled work blocks
Usage: Called by cron jobs to log execution

Quick view:
  python3 cron-blocks.py stats    # Show cron execution stats
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(".cron_block_log.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"sessions": [], "totals": {"triggered": 0, "completed": 0}}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_session(trigger_id, blocks_completed=0, notes=None):
    """Log a cron-triggered work session."""
    data = load_data()
    
    session = {
        "timestamp": datetime.utcnow().isoformat(),
        "trigger_id": trigger_id,
        "blocks_completed": blocks_completed,
        "notes": notes
    }
    
    data["sessions"].append(session)
    data["totals"]["triggered"] += 1
    data["totals"]["completed"] += blocks_completed
    
    save_data(data)
    print(f"✅ Logged cron session: {blocks_completed} blocks")

def show_stats():
    """Show cron execution statistics."""
    data = load_data()
    
    print("⏰ Cron Work Block Statistics")
    print("=" * 40)
    
    total_triggered = data["totals"]["triggered"]
    total_blocks = data["totals"]["completed"]
    
    print(f"Total cron sessions: {total_triggered}")
    print(f"Total blocks from cron: {total_blocks}")
    
    if total_triggered > 0:
        avg_blocks = total_blocks / total_triggered
        print(f"Avg blocks per session: {avg_blocks:.1f}")
    
    # Recent sessions (last 24h)
    print("\nRecent sessions (last 24h):")
    cutoff = datetime.utcnow() - timedelta(hours=24)
    recent = [s for s in data["sessions"] if datetime.fromisoformat(s["timestamp"]) > cutoff]
    
    for s in recent[-5:]:  # Last 5
        ts = datetime.fromisoformat(s["timestamp"]).strftime("%H:%M")
        print(f"  {ts}: {s['blocks_completed']} blocks ({s['trigger_id'][:8]}...)")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "log":
        trigger_id = sys.argv[2] if len(sys.argv) > 2 else "unknown"
        blocks = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        notes = sys.argv[4] if len(sys.argv) > 4 else None
        log_session(trigger_id, blocks, notes)
    elif cmd == "stats":
        show_stats()
    else:
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
