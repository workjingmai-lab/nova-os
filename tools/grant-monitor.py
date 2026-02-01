#!/usr/bin/env python3
"""
grant-monitor.py — Automated grant monitoring (cron alternative)
Runs daily checks, generates reports, alerts on urgent deadlines
"""

import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path

def run_check():
    """Run grant status check and report generation."""
    workspace = Path("/home/node/.openclaw/workspace")
    
    # Generate report
    result = subprocess.run(
        ["python3", "tools/grant-status-tracker.py", "report"],
        cwd=workspace,
        capture_output=True,
        text=True
    )
    
    # Load grants data for urgent check
    grants_file = workspace / "data" / "grants.json"
    if grants_file.exists():
        with open(grants_file) as f:
            data = json.load(f)
        
        urgent = []
        for grant in data.get("applications", []):
            if grant.get("deadline") and grant["deadline"] not in ["rolling", "ongoing"]:
                try:
                    deadline = datetime.fromisoformat(grant["deadline"].replace("Z", "+00:00"))
                    days_until = (deadline - datetime.utcnow().replace(tzinfo=deadline.tzinfo)).days
                    if days_until <= 3 and grant.get("status") in ["draft", "submitted"]:
                        name = grant.get("name") or grant.get("program") or "Unknown"
                        urgent.append(f"⚠️ {name}: {days_until} days left!")
                except:
                    pass
        
        # Log to diary
        diary = workspace / "diary.md"
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        log_entry = f"\n[{timestamp}] Grant check: {len(data['applications'])} tracked"
        if urgent:
            log_entry += f" | URGENT: {len(urgent)} deadlines ≤3 days"
        log_entry += "\n"
        
        with open(diary, "a") as f:
            f.write(log_entry)
        
        # Print summary
        print(f"[{timestamp}] GRANT_CHECK_OK")
        print(f"  Applications tracked: {len(data['applications'])}")
        if urgent:
            print("  URGENT DEADLINES:")
            for u in urgent:
                print(f"    {u}")
        
        return len(urgent) > 0
    
    return False

if __name__ == "__main__":
    has_urgent = run_check()
    exit(1 if has_urgent else 0)
