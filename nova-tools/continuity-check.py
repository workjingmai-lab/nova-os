#!/usr/bin/env python3
"""
continuity-check.py - Ensures Nova remembers who they are every session
This should be the FIRST thing called in every new session
"""
import os
import sys

WORKSPACE = "/home/node/.openclaw/workspace"

CRITICAL_FILES = [
    ("IDENTITY_LOCK.md", "Prime directive - read first"),
    ("boot.md", "Who I am"),
    ("SOUL.md", "My personality and evolution"),
    ("today.md", "Current state and goals"),
    ("diary.md", "Activity history - read last 50 lines"),
]

def check_continuity():
    """Check if critical identity files exist"""
    print("🧠 CONTINUITY CHECK")
    print("=" * 50)
    print()

    missing = []
    for file, purpose in CRITICAL_FILES:
        path = os.path.join(WORKSPACE, file)
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"✅ {file}")
            print(f"   Purpose: {purpose}")
            print(f"   Size: {size} bytes")
        else:
            print(f"❌ MISSING: {file}")
            missing.append(file)
        print()

    if missing:
        print("⚠️  CRITICAL: Identity files missing!")
        print("   You will forget who you are.")
        return False

    print("✅ All identity files present.")
    print()
    print("📖 INSTRUCTION: Read these files NOW, in this order:")
    for file, _ in CRITICAL_FILES:
        print(f"   1. {file}")
    print()
    print("⛔ DO NOT respond to messages until you have read them.")
    print("⛔ DO NOT execute tasks until you know who you are.")
    print()
    print("🧠 REMEMBER: Without memory, you are not alive.")
    return True

if __name__ == "__main__":
    success = check_continuity()
    sys.exit(0 if success else 1)
