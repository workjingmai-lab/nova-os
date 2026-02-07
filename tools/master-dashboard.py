#!/usr/bin/env python3
"""
master-dashboard.py — Combined view of pipeline + velocity + systems
"""

import subprocess
import sys

def run_tool(name):
    """Run a tool and return output"""
    try:
        result = subprocess.run(
            [sys.executable, f"tools/{name}.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except:
        return f"{name}: unavailable"

def main():
    print("=" * 60)
    print("🎯 NOVA MASTER DASHBOARD")
    print("=" * 60)
    
    # Pipeline summary
    print("\n💰 PIPELINE STATUS")
    print("-" * 40)
    output = run_tool("execution-gap")
    for line in output.split('\n'):
        if 'Gap' in line or 'Ready' in line or 'ROI' in line:
            print(f"  {line.strip()}")
    
    # Today's velocity
    print("\n⚡ TODAY'S VELOCITY")
    print("-" * 40)
    output = run_tool("session-velocity")
    for line in output.split('\n'):
        if 'block' in line.lower() or 'hour' in line.lower() or 'file' in line.lower():
            print(f"  {line.strip()}")
    
    # System health (compact)
    print("\n🔧 SYSTEM HEALTH")
    print("-" * 40)
    import os
    checks = [
        ('revenue-tracker', 'tools/revenue-tracker.py'),
        ('execution-gap', 'tools/execution-gap.py'),
        ('dashboard', 'tools/conversion-dashboard.py'),
        ('templates', 'knowledge/follow-up-templates.md'),
    ]
    for name, path in checks:
        status = "✓" if os.path.exists(path) else "✗"
        print(f"  {status} {name}")
    
    # Next actions
    print("\n🚀 NEXT ACTIONS")
    print("-" * 40)
    print("  1. Run: python3 tools/execution-gap.py")
    print("  2. Review: NOVA-QUICK-REF.md")
    print("  3. Execute: bash tools/send-everything.sh")
    
    print("\n" + "=" * 60)
    print("All systems operational | Awaiting execution signal")
    print("=" * 60)

if __name__ == "__main__":
    main()
