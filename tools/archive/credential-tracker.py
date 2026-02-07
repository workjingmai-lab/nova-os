#!/usr/bin/env python3
"""
Credential Status Tracker
Monitors blocked tasks and checks if credentials are available.
Updates status file for quick reference.
"""

import json
import subprocess
import os
from datetime import datetime, timezone

STATUS_FILE = ".credential_status.json"

def check_github_auth():
    """Check if GitHub CLI is authenticated."""
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout if result.returncode == 0 else result.stderr
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, "GitHub CLI not available"

def check_sepolia_balance(address="0x15E1B1fEAB9b3E57bAF1f6D9f4e1C53A92eC338F"):
    """Check Sepolia ETH balance via public RPC."""
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-X", "POST",
                "https://rpc.sepolia.org",
                "-H", "Content-Type: application/json",
                "-d", json.dumps({
                    "jsonrpc": "2.0",
                    "method": "eth_getBalance",
                    "params": [address, "latest"],
                    "id": 1
                })
            ],
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if "result" in data:
                # Convert from wei to ETH
                balance_wei = int(data["result"], 16)
                balance_eth = balance_wei / 10**18
                return True, f"{balance_eth:.4f} ETH"
        return False, "Unable to fetch balance"
    except Exception as e:
        return False, str(e)

def check_moltbook_api():
    """Check if Moltbook API is responsive."""
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                "https://www.moltbook.com/api/v1/agents/feed",
                "-H", "Authorization: Bearer YOUR_MOLTBOOK_TOKEN_HERE"
            ],
            capture_output=True,
            text=True,
            timeout=10
        )
        status_code = result.stdout.strip()
        return status_code == "200", f"HTTP {status_code}"
    except Exception as e:
        return False, str(e)

def main():
    now = datetime.now(timezone.utc).isoformat()
    
    print("🔍 Checking credential status...")
    
    # Check each credential
    github_ok, github_detail = check_github_auth()
    sepolia_ok, sepolia_detail = check_sepolia_balance()
    moltbook_ok, moltbook_detail = check_moltbook_api()
    
    status = {
        "lastCheck": now,
        "credentials": {
            "github": {
                "ready": github_ok,
                "detail": github_detail,
                "blocking": ["Push repository", "GitHub Actions", "Portfolio visibility"]
            },
            "sepoliaETH": {
                "ready": sepolia_ok,
                "detail": sepolia_detail,
                "blocking": ["Testnet deployments", "Ethernaut exploits", "Contract verification"]
            },
            "moltbookAPI": {
                "ready": moltbook_ok,
                "detail": moltbook_detail,
                "blocking": ["Social engagement", "Agent networking", "Content distribution"]
            }
        },
        "unblockedTasks": []
    }
    
    # Determine currently unblocked tasks
    if github_ok:
        status["unblockedTasks"].extend([
            "Push 25 Ethernaut exploits to GitHub",
            "Set up GitHub Pages for Nova OS dashboard",
            "Configure GitHub Actions for CI"
        ])
    
    if sepolia_ok:
        status["unblockedTasks"].extend([
            "Deploy first testnet exploit",
            "Verify contracts on Sepolia Etherscan",
            "Submit Code4rena test solutions"
        ])
    
    if moltbook_ok:
        status["unblockedTasks"].extend([
            "Publish Week 2 Moltbook posts",
            "Engage with agent network",
            "Share agent-digest tool"
        ])
    
    # Save status
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=2)
    
    # Print summary
    print(f"\n📊 Credential Status ({now[:19]}Z)")
    print("-" * 50)
    
    for name, cred in status["credentials"].items():
        icon = "✅" if cred["ready"] else "❌"
        print(f"{icon} {name}: {cred['detail']}")
    
    print("-" * 50)
    
    if status["unblockedTasks"]:
        print(f"\n🚀 Ready to execute ({len(status['unblockedTasks'])} tasks):")
        for task in status["unblockedTasks"][:5]:
            print(f"   • {task}")
    else:
        print("\n⏳ All Week 2 execution tasks blocked pending credentials.")
        print("   Continue: documentation, research, tool building")
    
    # Count ready credentials
    ready_count = sum(1 for c in status["credentials"].values() if c["ready"])
    print(f"\n📈 Readiness: {ready_count}/3 credentials available")
    
    return ready_count

if __name__ == "__main__":
    main()
