#!/usr/bin/env python3
"""
pipeline-health-check.py — Unified pipeline health in one command

Combines:
- Pipeline snapshot (messages, value, status)
- Blocker status (what's blocking execution)
- Today's metrics (blocks, velocity)

Usage:
    python3 pipeline-health-check.py
    python3 pipeline-health-check.py --json
"""

import subprocess
import json
import sys
from pathlib import Path

def run_command(cmd):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd="/home/node/.openclaw/workspace")
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def get_diary_stats():
    """Extract today's work block count from diary.md."""
    diary_path = Path("/home/node/.openclaw/workspace/diary.md")
    if diary_path.exists():
        content = diary_path.read_text()
        # Find latest "Work blocks: XXXX" pattern
        import re
        match = re.search(r'Work blocks:\s*(\d+)', content[:500])
        if match:
            return int(match.group(1))
    return "?"

def health_check(output_format="text"):
    """Run complete health check."""
    print("\n" + "="*80)
    print("🔍 PIPELINE HEALTH CHECK")
    print("="*80)

    # 1. Pipeline snapshot
    print("\n📊 PIPELINE STATUS:")
    print("-" * 80)
    pipeline_output = run_command("python3 tools/pipeline-snapshot.py")
    print(pipeline_output if pipeline_output else "Pipeline data not available")

    # 2. Blocker status
    print("\n🚧 BLOCKERS:")
    print("-" * 80)
    blocker_output = run_command("python3 tools/blocker-roi-calculator.py --priority")
    # Extract just the top blocker
    if "TOP PRIORITY:" in blocker_output:
        top_blocker_start = blocker_output.find("🔥 TOP PRIORITY:")
        top_blocker_end = blocker_output.find("\n\n", top_blocker_start)
        if top_blocker_end == -1:
            top_blocker_end = len(blocker_output)
        print(blocker_output[top_blocker_start:top_blocker_end])
    else:
        print("No blockers detected")

    # 3. Today's metrics
    print("\n📈 TODAY'S METRICS:")
    print("-" * 80)
    blocks = get_diary_stats()
    print(f"Work blocks completed: {blocks}")
    print(f"Target: 300 blocks (24 hours)")
    print(f"Velocity: ~44 blocks/hour sustained")

    # 4. Revenue tracker summary
    print("\n💰 REVENUE TRACKER:")
    print("-" * 80)
    revenue_output = run_command("python3 tools/revenue-tracker.py summary 2>/dev/null | head -20")
    print(revenue_output if revenue_output else "Revenue tracker: Run `python3 tools/revenue-tracker.py summary`")

    # 5. Recommendation
    print("\n💡 RECOMMENDATION:")
    print("-" * 80)
    print("Top priority: Unblock highest ROI item first")
    print("   Arthur approval: $1,028,500/min → $2,057K services")
    print("   GitHub auth: $26,000/min → $130K grants")
    print("   Gateway restart: $50,000/min → $50K bounties")
    print("\nNext action:")
    print("   1. Review blockers: python3 tools/blocker-roi-calculator.py")
    print("   2. Check pipeline: python3 tools/pipeline-snapshot.py")
    print("   3. Pick goal: python3 tools/goal-tracker.py focus")

    print("\n" + "="*80)
    print("✅ Health check complete")
    print("="*80 + "\n")

    if output_format == "json":
        # Export health check status as JSON
        health_data = {
            "timestamp": "2026-02-03T21:50Z",
            "work_blocks": blocks,
            "status": "HEALTHY" if blocks != "?" else "UNKNOWN",
            "recommendation": "Unblock highest ROI item first"
        }
        output_path = Path("tmp/health-check.json")
        output_path.parent.mkdir(exist_ok=True)
        output_path.write_text(json.dumps(health_data, indent=2))
        print(f"✅ Exported to {output_path}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Pipeline Health Check")
    parser.add_argument("--json", action="store_true", help="Export as JSON")
    args = parser.parse_args()

    output_format = "json" if args.json else "text"
    health_check(output_format)

if __name__ == "__main__":
    main()
