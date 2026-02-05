#!/usr/bin/env python3
"""
GitHub Auth Manager - Non-interactive push setup
Stores token securely for automated git operations
"""
import os
import sys
import subprocess
from pathlib import Path

def setup_github_auth(token=None, repo_url="https://github.com/NovaArchitect/nova-os.git"):
    """Configure git to use token-based auth for non-interactive push."""
    
    # Get token from arg, env, or prompt
    if not token:
        token = os.environ.get('GITHUB_TOKEN')
    
    if not token:
        print("❌ No GITHUB_TOKEN provided")
        print("Set it via: export GITHUB_TOKEN='ghp_xxxxxxxx'")
        return False
    
    # Validate token format
    if not token.startswith(('ghp_', 'gho_', 'github_pat_')):
        print(f"⚠️  Token doesn't look like a GitHub token: {token[:4]}...")
    
    # Update remote URL with embedded credentials
    # Format: https://<token>@github.com/<user>/<repo>.git
    authed_url = repo_url.replace("https://", f"https://{token}@")
    
    try:
        subprocess.run(
            ["git", "remote", "set-url", "origin", authed_url],
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ Git remote updated with token auth")
        
        # Test the connection
        result = subprocess.run(
            ["git", "fetch", "--dry-run"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ GitHub auth test passed")
            return True
        else:
            print(f"⚠️  Auth test failed: {result.stderr}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to update remote: {e}")
        return False

def clear_github_auth(repo_url="https://github.com/NovaArchitect/nova-os.git"):
    """Remove token from remote URL (security)."""
    try:
        subprocess.run(
            ["git", "remote", "set-url", "origin", repo_url],
            check=True,
            capture_output=True
        )
        print("✅ Token removed from git remote")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clear auth: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="GitHub Auth Manager")
    parser.add_argument("--token", help="GitHub personal access token")
    parser.add_argument("--clear", action="store_true", help="Remove token auth")
    args = parser.parse_args()
    
    if args.clear:
        clear_github_auth()
    else:
        success = setup_github_auth(args.token)
        sys.exit(0 if success else 1)
