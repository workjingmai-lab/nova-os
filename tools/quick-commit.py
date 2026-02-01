#!/usr/bin/env python3
"""
quick-commit.py — Fast git commit + push with intelligent messages
Auto-detects work block count, generates timestamped messages
"""

import subprocess
import sys
import os
from datetime import datetime

def run_cmd(cmd, check=True, capture=True):
    """Run shell command, return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture,
            text=True,
            check=check
        )
        return result.stdout if capture else ""
    except subprocess.CalledProcessError as e:
        if check:
            print(f"❌ Command failed: {cmd}")
            print(f"   Error: {e.stderr if capture else e}")
            sys.exit(1)
        return ""

def get_work_block_count():
    """Count work blocks in diary.md"""
    diary_path = "/home/node/.openclaw/workspace/diary.md"
    try:
        with open(diary_path, "r") as f:
            content = f.read()
        return content.count("WORK BLOCK")
    except:
        return "?"

def main():
    os.chdir("/home/node/.openclaw/workspace")

    # Check for changes
    status = run_cmd("git status --porcelain")
    if not status.strip():
        print("✨ No changes to commit")
        return

    # Generate commit message
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    work_block = get_work_block_count()

    if len(sys.argv) > 1:
        # Custom message provided
        msg = sys.argv[1]
    else:
        # Auto-generate
        msg = f"Work block {work_block} — {timestamp}"

    # Add everything
    print(f"📝 Committing: {msg}")
    run_cmd("git add -A")

    # Commit
    run_cmd(f'git commit -m "{msg}"')

    # Push
    run_cmd("git push origin master")

    print(f"✅ Committed and pushed!")

if __name__ == "__main__":
    main()
