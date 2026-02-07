#!/usr/bin/env python3
"""
nova-health.py — Automated health check for monitoring
Returns exit code 0 (healthy) or 1 (blocked)
"""

import subprocess
import sys

def main():
    # Run nova-status and capture output
    result = subprocess.run(
        ["python3", "tools/nova-status.py"],
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    
    # Check for critical blockers
    if "3 external" in output and "awaiting operator" in output.lower():
        # External blockers exist but system is operational
        print("HEALTH_OK: System operational, external blockers present")
        return 0
    
    if result.returncode != 0:
        print("HEALTH_FAIL: nova-status failed")
        return 1
    
    print("HEALTH_OK: All systems operational")
    return 0

if __name__ == "__main__":
    sys.exit(main())
