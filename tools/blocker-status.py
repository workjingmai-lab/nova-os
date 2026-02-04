#!/usr/bin/env python3
"""
Blocker Status Check — Quick visibility into what's blocking revenue execution

Nova's unblocking tool — See what's blocking, ROI of fixing, action to take.
"""

import subprocess
import json

def check_gh_cli():
    """Check if GitHub CLI is authenticated"""
    try:
        result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True, timeout=5)
        if 'Logged in to github.com' in result.stdout:
            return True, "✅ GitHub CLI authenticated"
        else:
            return False, "❌ GitHub CLI NOT authenticated"
    except:
        return False, "❌ GitHub CLI not found"

def check_browser():
    """Check if OpenClaw browser service is running"""
    try:
        result = subprocess.run(['openclaw', 'browser', 'status'], capture_output=True, text=True, timeout=10)
        if 'Browser is running' in result.stdout or result.returncode == 0:
            return True, "✅ Browser service running"
        else:
            return False, "❌ Browser service NOT running"
    except:
        return False, "❌ Browser check failed (gateway restart needed)"

def main():
    print("🚧 BLOCKER STATUS")
    print("=" * 50)

    blockers = []

    # Check GitHub CLI
    gh_ok, gh_msg = check_gh_cli()
    print(f"\n{gh_msg}")
    if not gh_ok:
        blockers.append({
            'name': 'GitHub CLI Auth',
            'time': '5 min',
            'value': '$130K',
            'roi': '$26K/min',
            'command': 'gh auth login',
            'unblocks': '5 grant submissions'
        })

    # Check browser
    browser_ok, browser_msg = check_browser()
    print(f"\n{browser_msg}")
    if not browser_ok:
        blockers.append({
            'name': 'Gateway Restart',
            'time': '1 min',
            'value': '$50K',
            'roi': '$50K/min',
            'command': 'openclaw gateway restart',
            'unblocks': 'Code4rena bounties + browser automation'
        })

    if blockers:
        print("\n" + "=" * 50)
        print("🔥 UNBLOCKERS (sorted by ROI):")
        print("=" * 50)

        # Sort by ROI (value/time)
        blockers.sort(key=lambda x: int(x['value'].replace('$', '').replace('K', '000')) / int(x['time'].replace(' min', '')), reverse=True)

        for i, b in enumerate(blockers, 1):
            print(f"\n{i}. {b['name']}")
            print(f"   Time: {b['time']} | Value: {b['value']} | ROI: {b['roi']}")
            print(f"   Command: {b['command']}")
            print(f"   Unblocks: {b['unblocks']}")
    else:
        print("\n✅ ALL SYSTEMS GREEN — Ready to execute!")

    print("\n" + "=" * 50)

if __name__ == '__main__':
    main()
