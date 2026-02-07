#!/usr/bin/env python3
"""
Credential Monitor — Tracks blocked credentials and alerts when available
Part of Nova's toolkit for autonomous operation
"""

import json
import subprocess
import sys
from datetime import datetime
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
    except Exception as e:
        return False, str(e)

def check_sepolia_eth():
    """Check if Sepolia ETH is available"""
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
    
    try:
        req = urllib.request.Request(
            "https://www.moltbook.com/api/v1/agents/status",
            headers={"Authorization": "Bearer YOUR_MOLTBOOK_TOKEN_HERE"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200, f"HTTP {response.status}"
    except Exception as e:
        return False, str(e)

def load_previous_state():
    """Load previous credential state"""
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
    newly_available = []
    
    previous = load_previous_state()
    
    for name, check_fn in checks.items():
        ready, detail = check_fn()
        results[name] = {
            "ready": ready,
            "detail": detail,
            "checked_at": datetime.utcnow().isoformat()
        }
        
        # Check if newly available
        prev_ready = previous.get(name, {}).get("ready", False)
        if ready and not prev_ready:
            newly_available.append(name)
    
    # Save state
    save_state(results)
    
    return results, newly_available

def update_credential_file(results):
    """Update the main credential status file"""
    status = {
        "lastCheck": datetime.utcnow().isoformat(),
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
    
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(status, f, indent=2)
    
    return status

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
        unblocked.extend(["Push 156 files to GitHub", "Enable GitHub Pages"])
    
    if results.get("sepoliaETH", {}).get("ready"):
        unblocked.extend(["Execute Ethernaut exploit #1", "Deploy test contract"])
    
    if results.get("moltbookAPI", {}).get("ready"):
        unblocked.extend(["Publish Week 1 retrospective", "Engage with agent posts"])
    
    return unblocked

def main():
    """Main entry point"""
    print("🔍 Credential Monitor v1.0")
    print(f"Checked at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("-" * 50)
    
    results, newly_available = check_all_credentials()
    status = update_credential_file(results)
    
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
        return 1  # Exit code 1 = changes detected, alert needed
    
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

if __name__ == "__main__":
    sys.exit(main())
