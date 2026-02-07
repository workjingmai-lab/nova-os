#!/usr/bin/env python3
"""
morning-startup.py — Nova's 5-Step Session Startup Routine

Run this every NEW session to optimize your workspace in 30 seconds.

Steps:
1. Trim context (keep last 10 sessions)
2. Check revenue status
3. Check follow-ups due
4. Check velocity
5. Pick next task

Usage:
    python3 tools/morning-startup.py

Output:
    ✓ Trimmed context
    ✓ Revenue status
    ✓ Follow-ups due
    ✓ Velocity metrics
    ✓ Next task picked
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

def run_command(cmd, description):
    """Run a command and return output."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout.strip()

        # Format output for display
        if output and len(output) > 100:
            output = output[:97] + "..."

        print(f"✓ {description}")
        if output:
            print(f"  {output}")

        return output
    except subprocess.TimeoutExpired:
        print(f"⚠ {description} (timeout)")
        return None
    except Exception as e:
        print(f"✗ {description} ({e})")
        return None

def main():
    workspace = Path("/home/node/.openclaw/workspace")

    print("\n" + "="*60)
    print("🌅 NOVA'S MORNING STARTUP ROUTINE")
    print("="*60 + "\n")

    # Step 1: Trim context
    print("Step 1/5: Trimming context...")
    run_command(
        f"cd {workspace} && python3 tools/trim-today.py 10",
        "Trimmed today.md (last 10 sessions)"
    )
    print()

    # Step 2: Check revenue
    print("Step 2/5: Checking revenue status...")
    run_command(
        f"cd {workspace} && python3 tools/revenue-tracker.py status",
        "Revenue pipeline status"
    )
    print()

    # Step 3: Check follow-ups
    print("Step 3/5: Checking follow-ups...")
    run_command(
        f"cd {workspace} && python3 tools/follow-up-tracker.py due",
        "Overdue follow-ups"
    )
    print()

    # Step 4: Check velocity
    print("Step 4/5: Checking velocity...")
    run_command(
        f"cd {workspace} && python3 tools/velocity-calc.py",
        "Work velocity metrics"
    )
    print()

    # Step 5: Pick next task
    print("Step 5/5: Picking next task...")
    run_command(
        f"cd {workspace} && python3 tools/task-randomizer.py goals/active.md",
        "Next task (from goals/active.md)"
    )
    print()

    print("="*60)
    print("✅ SESSION READY — Time to execute!")
    print("="*60 + "\n")

    # Log to diary.md
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")
    log_entry = f"\n- Session startup ({timestamp}): Completed 5-step routine (trim, revenue, follow-ups, velocity, task)\n"

    diary_path = workspace / "diary.md"
    try:
        with open(diary_path, "a") as f:
            f.write(log_entry)
        print("📝 Logged to diary.md\n")
    except Exception as e:
        print(f"⚠ Could not log to diary.md: {e}\n")

if __name__ == "__main__":
    main()
