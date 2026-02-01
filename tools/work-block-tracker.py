#!/usr/bin/env python3
"""
Nova's Work Block Tracker
Analyzes diary.md for productivity metrics and velocity tracking.
"""

import re
from datetime import datetime
from pathlib import Path
import json

DIARY_PATH = Path.home() / ".openclaw" / "workspace" / "diary.md"
OUTPUT_PATH = Path.home() / ".openclaw" / "workspace" / "metrics" / "productivity.json"

def parse_diary():
    """Parse diary.md for work blocks and tasks."""
    if not DIARY_PATH.exists():
        return {"error": "diary.md not found"}

    content = DIARY_PATH.read_text()

    # Extract work blocks
    blocks = re.findall(
        r'## Completed Tasks.*?\n\*\*(\d+) total\*\*|'
        r'\|.*?\|.*?\|.*?\|',
        content, re.DOTALL
    )

    # Extract metrics
    metrics = {
        "total_blocks": len(re.findall(r'Completed Tasks \((\d+) total\)', content)),
        "total_tasks": sum(int(m) for m in re.findall(r'Completed Tests \((\d+) total\)', content)) or 0,
        "total_files": len(re.findall(r'Files created:', content)),
        "total_loc": sum(int(m) for m in re.findall(r'~(\d+)\+', content)) or 0,
        "last_updated": datetime.now().isoformat()
    }

    return metrics

def calculate_velocity(metrics):
    """Calculate velocity metrics."""
    if metrics.get("total_blocks", 0) == 0:
        return {"tasks_per_min": 0, "loc_per_min": 0}

    return {
        "tasks_per_min": round(metrics.get("total_tasks", 0) / max(metrics.get("total_blocks", 1), 1), 2),
        "loc_per_min": round(metrics.get("total_loc", 0) / max(metrics.get("total_blocks", 1), 1), 2)
    }

def main():
    """Main execution."""
    metrics = parse_diary()
    velocity = calculate_velocity(metrics)

    output = {
        "productivity": metrics,
        "velocity": velocity,
        "generated_at": datetime.now().isoformat()
    }

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Write metrics
    OUTPUT_PATH.write_text(json.dumps(output, indent=2))

    print(f"✅ Productivity metrics saved to {OUTPUT_PATH}")
    print(f"📊 Tasks per block: {velocity['tasks_per_min']}")
    print(f"⚡ LOC per block: {velocity['loc_per_min']}")

if __name__ == "__main__":
    main()
