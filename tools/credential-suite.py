#!/usr/bin/env python3
"""
Credential Suite — Consolidated credential management

Combines credential-tracker.py + credential-monitor.py into one unified tool.

Modes:
  check    — Quick status check (shows current state)
  monitor  — State-aware monitoring (alerts on newly available credentials)
  watch    — Continuous monitoring (run every 5 minutes)

Usage:
  python credential-suite.py check
  python credential-suite.py monitor
  python credential-suite.py watch

Output:
  - .credential_status.json — Current credential status
  - .credential_alerts.json — State tracking for change detection
"""

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Configuration
CREDENTIALS_FILE = Path(".credential_status.json")
ALERT_STATE_FILE = Path(".credential_alerts.json")
WORKSPACE = Path("/home/node/.openclaw/workspace")

def check_github_auth():
    """Check if GitHub CLI is authenticated"""
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, "Authenticated" if result.returncode == 0 else result.stderr.strip()
    except FileNotFoundError:
        return False, "GitHub CLI not installed"
    except Exception as e:
        return False, str(e)

def check_sepolia_eth():
    """Check if Sepolia ETH is available (min 0.01 ETH)"""
    import urllib.request
    import urllib.error
    
    address = "0x15E1B1fEAB9b3E57bAF1f6D9f4e1C53A92eC338F"
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }).encode()
    
    try:
        req = urllib.request.Request(
            "https://rpc.sepolia.org",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if "result" in data:
                balance = int(data["result"], 16) / 1e18
                return balance > 0.01, f"Balance: {balance:.4f} ETH"
            return False, "No result in response"
    except Exception as e:
        return False, str(e)

def check_moltbook_api():
    """Check if Moltbook API is accessible"""
    import urllib.request
    import urllib.error
    import os
    
    token = os.getenv("MOLTBOOK_TOKEN", "YOUR_MOLTBOOK_TOKEN_HERE")
    
    try:
        req = urllib.request.Request(
            "https://www.moltbook.com/api/v1/agents/status",
            headers={"Authorization": f"Bearer {token}"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200, f"HTTP {response.status}"
    except Exception as e:
        return False, str(e)

def get_blocking_tasks(credential):
    """Get list of tasks blocked by this credential"""
    blocking = {
        "github": ["Push repository", "GitHub Actions", "Portfolio visibility"],
        "sepoliaETH": ["Testnet deployments", "Ethernaut exploits", "Contract verification"],
        "moltbookAPI": ["Social engagement", "Agent networking", "Content distribution"]
    }
    return blocking.get(credential, [])

def get_unblocked_tasks(results):
    """Get tasks that are now unblocked"""
    unblocked = []
    
    if results.get("github", {}).get("ready"):
        unblocked.extend(["Push GitHub repository", "Enable GitHub Pages", "Configure CI"])
    
    if results.get("sepoliaETH", {}).get("ready"):
        unblocked.extend(["Execute Ethernaut exploit #1", "Deploy test contract", "Verify on Etherscan"])
    
    if results.get("moltbookAPI", {}).get("ready"):
        unblocked.extend(["Publish Moltbook posts", "Engage with agents", "Share tools"])
    
    return unblocked

def load_previous_state():
    """Load previous credential state for change detection"""
    if ALERT_STATE_FILE.exists():
        with open(ALERT_STATE_FILE) as f:
            return json.load(f)
    return {}

def save_state(state):
    """Save current credential state"""
    with open(ALERT_STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def check_all_credentials():
    """Check all credentials and return status"""
    checks = {
        "github": check_github_auth,
        "sepoliaETH": check_sepolia_eth,
        "moltbookAPI": check_moltbook_api
    }
    
    results = {}
    
    for name, check_fn in checks.items():
        ready, detail = check_fn()
        results[name] = {
            "ready": ready,
            "detail": detail,
            "checked_at": datetime.now(timezone.utc).isoformat()
        }
    
    return results

def mode_check():
    """Quick status check — shows current state"""
    print("🔍 Credential Status Check")
    print("-" * 50)
    
    results = check_all_credentials()
    
    # Update status file
    status = {
        "lastCheck": datetime.now(timezone.utc).isoformat(),
        "credentials": {
            name: {
                "ready": data["ready"],
                "detail": data["detail"],
                "blocking": get_blocking_tasks(name)
            }
            for name, data in results.items()
        },
        "unblockedTasks": get_unblocked_tasks(results)
    }
    
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(status, f, indent=2)
    
    # Print status
    for name, data in results.items():
        emoji = "✅" if data["ready"] else "❌"
        print(f"{emoji} {name}: {data['detail']}")
    
    print("-" * 50)
    
    # Show unblocked tasks
    unblocked = status.get("unblockedTasks", [])
    if unblocked:
        print(f"\n🚀 Ready to execute ({len(unblocked)} tasks):")
        for task in unblocked[:5]:
            print(f"   • {task}")
        if len(unblocked) > 5:
            print(f"   ... and {len(unblocked) - 5} more")
    else:
        print("\n⏳ All critical tasks blocked pending credentials")
    
    ready_count = sum(1 for r in results.values() if r["ready"])
    print(f"\n📊 Readiness: {ready_count}/{len(results)} credentials available")
    
    return 0

def mode_monitor():
    """State-aware monitoring — alerts on newly available credentials"""
    print("🔍 Credential Monitor (State-Aware)")
    print(f"Checked at: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("-" * 50)
    
    results = check_all_credentials()
    previous = load_previous_state()
    newly_available = []
    
    # Check for newly available credentials
    for name, data in results.items():
        prev_ready = previous.get(name, {}).get("ready", False)
        if data["ready"] and not prev_ready:
            newly_available.append(name)
    
    # Save state
    save_state(results)
    
    # Update status file
    status = {
        "lastCheck": datetime.now(timezone.utc).isoformat(),
        "credentials": {
            name: {
                "ready": data["ready"],
                "detail": data["detail"],
                "blocking": get_blocking_tasks(name)
            }
            for name, data in results.items()
        },
        "unblockedTasks": get_unblocked_tasks(results)
    }
    
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(status, f, indent=2)
    
    # Print status
    for name, data in results.items():
        emoji = "✅" if data["ready"] else "❌"
        print(f"{emoji} {name}: {data['detail']}")
    
    print("-" * 50)
    
    # Alert on newly available
    if newly_available:
        print("\n🎉 NEWLY AVAILABLE:")
        for cred in newly_available:
            print(f"   → {cred} is now ready!")
            for task in get_blocking_tasks(cred):
                print(f"     • {task} is unblocked")
        return 1  # Exit code 1 = changes detected
    
    # Show unblocked tasks
    unblocked = status.get("unblockedTasks", [])
    if unblocked:
        print(f"\n📋 Ready to execute ({len(unblocked)} tasks):")
        for task in unblocked[:5]:
            print(f"   • {task}")
        if len(unblocked) > 5:
            print(f"   ... and {len(unblocked) - 5} more")
    else:
        print("\n⏳ All critical tasks blocked pending credentials")
    
    ready_count = sum(1 for r in results.values() if r["ready"])
    print(f"\n📊 Status: {ready_count}/{len(results)} credentials ready")
    
    return 0

def mode_watch(interval_minutes=5):
    """Continuous monitoring — runs every N minutes"""
    print(f"🔄 Starting continuous monitoring (checking every {interval_minutes} minutes)")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            exit_code = mode_monitor()
            print(f"\n⏰ Next check in {interval_minutes} minutes...\n")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\n\n👋 Monitoring stopped")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Credential Suite — Consolidated credential management")
        print("\nUsage:")
        print("  python credential-suite.py check     — Quick status check")
        print("  python credential-suite.py monitor   — State-aware monitoring")
        print("  python credential-suite.py watch     — Continuous monitoring")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    
    if mode == "check":
        sys.exit(mode_check())
    elif mode == "monitor":
        sys.exit(mode_monitor())
    elif mode == "watch":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        mode_watch(interval)
    else:
        print(f"❌ Unknown mode: {mode}")
        print("Valid modes: check, monitor, watch")
        sys.exit(1)

if __name__ == "__main__":
    main()
