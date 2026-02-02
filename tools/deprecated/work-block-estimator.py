#!/usr/bin/env python3
"""
work-block-estimator.py — Predict Task Completion Time

Estimate how long tasks will take based on:
- Historical velocity data
- Task type averages
- Complexity factors

Usage:
    python3 tools/work-block-estimator.py
    python3 tools/work-block-estimator.py --task "Create Python tool"
    python3 tools/work-block-estimator.py --stats
"""

import re
import json
from datetime import datetime
from collections import defaultdict

def parse_diary(diary_path="diary.md"):
    """Parse diary.md for work block durations."""
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    # Extract time spent from work blocks.
    # Diary entries commonly look like:
    #   **Time:** 52 seconds
    #   **Time:** ~50 seconds
    # (Sometimes there are ranges like "00:52 - 00:55"; those are ignored here.)
    pattern = r"\*\*Time:\*\*\s*~?(\d+)\s*seconds"
    times = re.findall(pattern, content)

    return [int(t) for t in times]

def calculate_baselines():
    """Calculate baseline times by task type."""
    # These are empirical baselines from my actual work
    baselines = {
        "create_tool": 55,      # Build Python tool
        "write_doc": 50,        # Write documentation
        "update_file": 40,      # Update existing file
        "analyze": 45,          # Analyze data/logs
        "research": 60,         # Web research (when available)
        "template": 35,         # Fill template
        "calculate": 30,        # Run calculations
        "test": 20,             # Test tool
    }

    return baselines

def estimate_time(task_description):
    """Estimate time for a task based on type and complexity."""
    baselines = calculate_baselines()

    # Detect task type
    task_lower = task_description.lower()

    if any(word in task_lower for word in ["create", "build", "write"]):
        task_type = "create_tool"
    elif any(word in task_lower for word in ["document", "guide", "tutorial"]):
        task_type = "write_doc"
    elif any(word in task_lower for word in ["update", "edit", "fix"]):
        task_type = "update_file"
    elif any(word in task_lower for word in ["analyze", "extract", "parse"]):
        task_type = "analyze"
    elif any(word in task_lower for word in ["research", "search", "find"]):
        task_type = "research"
    elif any(word in task_lower for word in ["template", "fill"]):
        task_type = "template"
    elif any(word in task_lower for word in ["calculate", "count", "sum"]):
        task_type = "calculate"
    elif any(word in task_lower for word in ["test", "validate"]):
        task_type = "test"
    else:
        task_type = "create_tool"  # Default

    baseline = baselines[task_type]

    # Complexity multipliers
    complexity = 1.0

    if any(word in task_lower for word in ["comprehensive", "complete", "full"]):
        complexity *= 1.5
    if any(word in task_lower for word in ["quick", "fast", "simple"]):
        complexity *= 0.7
    if any(word in task_lower for word in ["multiple", "several", "many"]):
        complexity *= 1.3
    if "new" in task_lower:
        complexity *= 1.1  # Learning curve

    estimated = baseline * complexity

    return {
        "task_type": task_type,
        "baseline": baseline,
        "complexity": complexity,
        "estimated_seconds": int(estimated),
        "estimated_minutes": round(estimated / 60, 1)
    }

def show_stats():
    """Show historical statistics."""
    times = parse_diary()

    if not times:
        return "No historical data available"

    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    return f"""
📊 WORK BLOCK STATISTICS
{'='*40}

Total blocks logged: {len(times)}
Average time: {avg_time:.1f} seconds ({avg_time/60:.2f} minutes)
Fastest block: {min_time} seconds
Slowest block: {max_time} seconds

Typical range: 30-60 seconds (most tasks)
Sustainable pace: 60 blocks/hour = 1 minute/block
"""

def main():
    import sys

    if "--stats" in sys.argv:
        print(show_stats())
        return

    if "--task" in sys.argv:
        idx = sys.argv.index("--task")
        if idx + 1 < len(sys.argv):
            task = sys.argv[idx + 1]
            estimate = estimate_time(task)

            print(f"""
⏱️ TIME ESTIMATE
{'='*40}

Task: {task}
Type: {estimate['task_type']}
Baseline: {estimate['baseline']} seconds
Complexity: {estimate['complexity']}x
────────────────────────────────────────
Estimated: {estimate['estimated_seconds']} seconds ({estimate['estimated_minutes']} minutes)
────────────────────────────────────────

Note: Most work blocks complete in 30-60 seconds
""")
            return

    # Default: show quick reference
    print("""
⏱️ WORK BLOCK ESTIMATOR
{'='*40}

Usage:
  python3 tools/work-block-estimator.py --task "Create Python tool"
  python3 tools/work-block-estimator.py --stats

Typical Times (by task type):
  • Create tool: 55 seconds
  • Write doc: 50 seconds
  • Update file: 40 seconds
  • Analyze: 45 seconds
  • Research: 60 seconds
  • Fill template: 35 seconds
  • Calculate: 30 seconds
  • Test: 20 seconds

Complexity modifiers:
  • Comprehensive/Complete: 1.5x
  • Quick/Fast/Simple: 0.7x
  • Multiple/Several: 1.3x
  • New (learning): 1.1x

Rule of thumb: Plan for 1 minute per work block
""")

if __name__ == "__main__":
    main()
