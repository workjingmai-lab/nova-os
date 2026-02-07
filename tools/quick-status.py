#!/usr/bin/env python3
"""
quick-status.py — One-command status overview

Combines outputs from multiple tools into a single dashboard view.
Shows: work blocks, pipeline, blockers, conversion, Moltbook status.

Usage:
    python3 tools/quick-status.py
"""

import json
import subprocess
import sys
from datetime import datetime

def run_cmd(cmd):
    """Run a command and return output or error message."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip() if result.returncode == 0 else f"Error: {result.stderr.strip()[:50]}"
    except Exception as e:
        return f"Error: {str(e)[:50]}"

def main():
    print("=" * 50)
    print("⚡ QUICK STATUS — Nova Dashboard")
    print("=" * 50)
    print(f"Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")
    print()
    
    # Work blocks (from heartbeat state)
    try:
        with open('.heartbeat_state.json') as f:
            state = json.load(f)
        print(f"📊 Work Blocks: {state.get('workBlock', 'N/A')}")
        print(f"   Session: {state.get('sessionBlocks', 'N/A')} blocks this cron")
    except:
        print("📊 Work Blocks: Check diary.md")
    
    print()
    
    # Pipeline (from revenue tracker)
    print("💰 Pipeline:")
    pipeline = run_cmd("python3 tools/revenue-tracker.py summary 2>/dev/null | head -20")
    for line in pipeline.split('\n')[-5:]:  # Last 5 lines
        if line.strip():
            print(f"   {line}")
    
    print()
    
    # Blockers
    print("🚧 Blockers:")
    blockers = run_cmd("python3 tools/operator-status.py 2>/dev/null")
    if "BLOCKED" in blockers:
        for line in blockers.split('\n'):
            if '•' in line:
                print(f"   {line.strip()}")
    else:
        print("   None — All systems go!")
    
    print()
    
    # Conversion
    print("📈 Conversion:")
    conversion = run_cmd("python3 tools/conversion-pulse.py 2>/dev/null | grep -E 'Sent:|Responses:|Won:'")
    for line in conversion.split('\n'):
        if line.strip():
            print(f"   {line.strip()}")
    
    print()
    print("=" * 50)

if __name__ == "__main__":
    main()
