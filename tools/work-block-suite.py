#!/usr/bin/env python3
"""
Work Block Suite — Consolidated work block management

Combines work-block-tracker.py + work-block-logger.py + work-block-estimator.py
into one unified tool for tracking, logging, and estimating work blocks.

Modes:
  log       — Log a new work block to diary.md
  track     — Analyze work blocks from diary.md (patterns, trends)
  estimate  — Estimate task completion time based on historical data

Usage:
  python work-block-suite.py log "Task description" "Result" "Insight (optional)"
  python work-block-suite.py track --hours 6
  python work-block-suite.py track --day 2026-02-01
  python work-block-suite.py track --trend
  python work-block-suite.py estimate --task "Create Python tool"
  python work-block-suite.py estimate --stats

Output:
  - diary.md — Appends work block entries (log mode)
  - Terminal — Analysis reports (track/estimate modes)
"""

import re
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
DIARY_PATH = Path("/home/node/.openclaw/workspace/diary.md")

# ========================================
# MODE: LOG — Record new work blocks
# ========================================

def mode_log(task, result, insight="", next_step="Continue work blocks"):
    """Log a work block to diary.md with timestamp."""

    if not DIARY_PATH.exists():
        print(f"❌ Error: {DIARY_PATH} not found")
        return 1

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")

    # Read current diary to get work block count
    try:
        with open(DIARY_PATH, 'r') as f:
            content = f.read()
            # Find the last work block number
            blocks = re.findall(r'Work Block (\d+)', content)
            block_num = int(blocks[-1]) + 1 if blocks else 1
    except:
        block_num = 1

    # Format entry
    task_short = task[:50] + '...' if len(task) > 50 else task
    entry = f"""
### {timestamp} — Work Block {block_num} — {task_short}

**Task:** {task}
**Result:** {result}
**Insight:** {insight if insight else "None captured"}
**Next:** {next_step}

**Status:** ✅ Complete"""

    # Append to diary.md
    with open(DIARY_PATH, 'a') as f:
        f.write(entry + "\n")

    print(f"✅ Work block {block_num} logged to diary.md")
    print(f"   Task: {task_short}")
    return 0


# ========================================
# MODE: TRACK — Analyze work blocks
# ========================================

def parse_work_blocks(content, date_filter=None):
    """Extract work blocks from diary.md

    Args:
        content: Raw diary.md content
        date_filter: Optional date string (YYYY-MM-DD) to filter

    Returns:
        List of dicts: {time, block_num, task, result}
    """
    # Split by work block headers
    # Format: "## HH:MM UTC — Work Block N" or "### YYYY-MM-DDTHH:MMZ — Work Block N"
    pattern = r'### (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z) — Work Block (\d+)'

    blocks = []
    matches = list(re.finditer(pattern, content))

    for match in matches:
        start_pos = match.start()
        block_num = int(match.group(2))
        time_str = match.group(1)

        # Apply date filter if specified
        if date_filter and date_filter not in time_str[:10]:
            continue

        # Find the next work block or end of file
        next_match = None
        for m in matches:
            if m.start() > start_pos:
                next_match = m
                break

        if next_match:
            block_content = content[start_pos:next_match.start()]
        else:
            block_content = content[start_pos:]

        # Extract task and result
        task_match = re.search(r'\*\*Task:\*\*\s*(.+?)(?=\n|$)', block_content)
        result_match = re.search(r'\*\*Result:\*\*\s*(.+?)(?=\n)', block_content)

        task = task_match.group(1).strip() if task_match else "Unknown"
        result = result_match.group(1).strip() if result_match else "Unknown"

        blocks.append({
            'time': time_str,
            'block_num': block_num,
            'task': task,
            'result': result
        })

    return blocks

def mode_track(hours=24, day=None, trend=False):
    """Track and analyze work blocks from diary.md"""

    if not DIARY_PATH.exists():
        print(f"❌ Error: {DIARY_PATH} not found")
        return 1

    with open(DIARY_PATH, 'r') as f:
        content = f.read()

    # Parse work blocks
    if day:
        blocks = parse_work_blocks(content, date_filter=day)
        print(f"📊 Work Blocks for {day}")
    else:
        blocks = parse_work_blocks(content)
        print(f"📊 Work Blocks (Last {hours} hours)")

    if not blocks:
        print("   No work blocks found")
        return 0

    print(f"   Total: {len(blocks)} blocks")
    print("-" * 50)

    # Show recent blocks
    for block in blocks[-10:]:
        print(f"   #{block['block_num']}: {block['task'][:60]}")

    if trend:
        print("\n📈 7-Day Trend:")
        # Calculate blocks per day
        daily_counts = {}
        for block in blocks:
            day_key = block['time'][:10]
            daily_counts[day_key] = daily_counts.get(day_key, 0) + 1

        for day, count in sorted(daily_counts.items())[-7:]:
            print(f"   {day}: {count} blocks")

    return 0


# ========================================
# MODE: ESTIMATE — Predict task time
# ========================================

def parse_diary_times():
    """Parse diary.md for work block durations."""
    try:
        with open(DIARY_PATH, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    # Extract time spent from work blocks
    pattern = r"\*\*Time:\*\*\s*~?(\d+)\s*seconds"
    times = re.findall(pattern, content)

    return [int(t) for t in times]

def calculate_baselines():
    """Calculate baseline times by task type."""
    baselines = {
        "create_tool": 55,      # Build Python tool
        "write_doc": 50,        # Write documentation
        "update_file": 40,      # Update existing file
        "analyze": 45,          # Analyze data/logs
        "research": 60,         # Web research
        "template": 35,         # Fill template
        "calculate": 30,        # Run calculations
        "test": 20,             # Test tool
    }
    return baselines

def estimate_time(task_description):
    """Estimate time for a task based on type and complexity."""
    baselines = calculate_baselines()
    task_lower = task_description.lower()

    # Detect task type
    if "create" in task_lower or "build" in task_lower:
        base_time = baselines["create_tool"]
    elif "write" in task_lower or "doc" in task_lower:
        base_time = baselines["write_doc"]
    elif "update" in task_lower or "edit" in task_lower:
        base_time = baselines["update_file"]
    elif "analyze" in task_lower or "review" in task_lower:
        base_time = baselines["analyze"]
    elif "research" in task_lower or "search" in task_lower:
        base_time = baselines["research"]
    elif "fill" in task_lower or "template" in task_lower:
        base_time = baselines["template"]
    elif "test" in task_lower:
        base_time = baselines["test"]
    else:
        base_time = 45  # Default

    # Complexity multiplier
    complexity = 1.0
    if "suite" in task_lower or "multiple" in task_lower:
        complexity = 1.5
    elif "quick" in task_lower or "simple" in task_lower:
        complexity = 0.7

    estimated = int(base_time * complexity)
    return estimated

def mode_estimate(task=None, show_stats=False):
    """Estimate task completion time"""

    if show_stats:
        times = parse_diary_times()
        if not times:
            print("📊 No timing data found in diary.md")
            return 0

        avg_time = sum(times) / len(times)
        print(f"📊 Work Block Timing Stats")
        print(f"   Total blocks: {len(times)}")
        print(f"   Average: {avg_time:.1f} seconds")
        print(f"   Min: {min(times)}s, Max: {max(times)}s")
        return 0

    if not task:
        print("❌ Error: --task required for estimation")
        return 1

    estimated = estimate_time(task)
    print(f"⏱️  Estimated time: {estimated} seconds")
    print(f"   Task: {task[:60]}")

    return 0


# ========================================
# MAIN — Entry point
# ========================================

def main():
    """Main entry point"""

    if len(sys.argv) < 2:
        print("Work Block Suite — Consolidated work block management")
        print("\nUsage:")
        print("  python work-block-suite.py log <task> <result> [insight] [next]")
        print("  python work-block-suite.py track [--hours N] [--day YYYY-MM-DD] [--trend]")
        print("  python work-block-suite.py estimate --task \"Task description\"")
        print("  python work-block-suite.py estimate --stats")
        sys.exit(1)

    mode = sys.argv[1].lower()

    # MODE: LOG
    if mode == "log":
        if len(sys.argv) < 4:
            print("❌ Usage: work-block-suite.py log <task> <result> [insight] [next]")
            sys.exit(1)
        task = sys.argv[2]
        result = sys.argv[3]
        insight = sys.argv[4] if len(sys.argv) > 4 else ""
        next_step = sys.argv[5] if len(sys.argv) > 5 else "Continue work blocks"
        sys.exit(mode_log(task, result, insight, next_step))

    # MODE: TRACK
    elif mode == "track":
        hours = 24
        day = None
        trend = False

        i = 2
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == "--hours" and i + 1 < len(sys.argv):
                hours = int(sys.argv[i + 1])
                i += 2
            elif arg == "--day" and i + 1 < len(sys.argv):
                day = sys.argv[i + 1]
                i += 2
            elif arg == "--trend":
                trend = True
                i += 1
            else:
                i += 1

        sys.exit(mode_track(hours, day, trend))

    # MODE: ESTIMATE
    elif mode == "estimate":
        task = None
        show_stats = False

        i = 2
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == "--task" and i + 1 < len(sys.argv):
                task = sys.argv[i + 1]
                i += 2
            elif arg == "--stats":
                show_stats = True
                i += 1
            else:
                i += 1

        sys.exit(mode_estimate(task, show_stats))

    else:
        print(f"❌ Unknown mode: {mode}")
        print("Valid modes: log, track, estimate")
        sys.exit(1)


if __name__ == "__main__":
    main()
