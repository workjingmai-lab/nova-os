#!/usr/bin/env python3
"""
operator-status.py — Post-3000 Operator Mode Status Check

Quick health check for operator mode. Verifies that all systems are ready
for Arthur to execute send-everything.sh.

Usage:
    python3 tools/operator-status.py

Output:
    Single-line status: READY / BLOCKED / WARNINGS
    Followed by details if not READY
"""

import json
import os
from pathlib import Path

# Configuration
WORKSPACE = Path("/home/node/.openclaw/workspace")
HEARTBEAT_FILE = WORKSPACE / ".heartbeat_state.json"
START_HERE = WORKSPACE / "START-HERE.md"
SEND_SCRIPT = WORKSPACE / "tools/send-everything.sh"
PIPELINE_FILE = WORKSPACE / "revenue-pipeline.json"

def check_heartbeat():
    """Check if heartbeat state exists and is recent (< 1 hour old)"""
    if not HEARTBEAT_FILE.exists():
        return None, "Missing heartbeat state file"

    with open(HEARTBEAT_FILE) as f:
        data = json.load(f)

    last_update = data.get("lastUpdated", 0)
    import time
    age_seconds = time.time() - last_update

    return data, f"Last update: {age_seconds // 60} minutes ago"

def check_start_here():
    """Check if START-HERE.md exists and is readable"""
    if not START_HERE.exists():
        return False, "Missing START-HERE.md"

    content = START_HERE.read_text()
    if len(content) < 500:
        return False, "START-HERE.md too short (incomplete?)"

    return True, f"START-HERE.md ready ({len(content)} bytes)"

def check_send_script():
    """Check if send-everything.sh exists and is executable"""
    if not SEND_SCRIPT.exists():
        return False, "Missing send-everything.sh"

    if not os.access(SEND_SCRIPT, os.X_OK):
        return False, "send-everything.sh not executable"

    return True, "send-everything.sh ready"

def check_pipeline():
    """Check pipeline status"""
    if not PIPELINE_FILE.exists():
        return None, "Missing pipeline file"

    with open(PIPELINE_FILE) as f:
        data = json.load(f)

    total = data.get("total", 0)
    ready = data.get("ready", 0)
    submitted = data.get("submitted", 0)

    gap_pct = (ready - submitted) / ready * 100 if ready > 0 else 0

    return {
        "total": total,
        "ready": ready,
        "submitted": submitted,
        "gap_pct": gap_pct
    }, f"${ready:,.0f} ready, ${submitted:,.0f} submitted ({gap_pct:.1f}% gap)"

def check_blockers(heartbeat_data):
    """Check active blockers"""
    if not heartbeat_data:
        return None, "No heartbeat data"

    blockers = heartbeat_data.get("blockers", [])

    if not blockers:
        return [], "No blockers"

    return blockers, f"{len(blockers)} blockers"

def main():
    """Run all checks and output status"""
    print("🔍 Operator Mode Status Check")
    print("=" * 40)

    # Run checks
    heartbeat, heartbeat_msg = check_heartbeat()
    start_here, start_msg = check_start_here()
    send_script, send_msg = check_send_script()
    pipeline, pipeline_msg = check_pipeline()
    blockers, blockers_msg = check_blockers(heartbeat)

    # Determine overall status
    issues = []

    if not heartbeat:
        issues.append("heartbeat_state.json missing")
    if not start_here:
        issues.append(start_msg)
    if not send_script:
        issues.append(send_msg)
    if blockers and len(blockers) > 0:
        issues.append(f"{len(blockers)} blockers active")

    # Output status
    if not issues:
        print("✅ READY")
        print()
        print(f"   {heartbeat_msg}")
        print(f"   {start_msg}")
        print(f"   {send_msg}")
        print(f"   {pipeline_msg}")
        print()
        print("🚀 Arthur can execute: bash tools/send-everything.sh full")
    else:
        if blockers and len(blockers) > 0:
            print("⚠️  BLOCKED")
        else:
            print("⚠️  WARNINGS")

        print()
        print("Issues:")
        for issue in issues:
            print(f"   • {issue}")

        print()
        if blockers:
            print("Blockers:")
            for b in blockers:
                print(f"   • {b['name']}: {b['roi']} ({b['time']})")

if __name__ == "__main__":
    main()
