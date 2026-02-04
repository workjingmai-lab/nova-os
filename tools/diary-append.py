#!/usr/bin/env python3
"""
diary-append.py - Safely append to diary.md without overwriting

Usage:
    python3 diary-append.py "Your diary entry here"
"""

import sys
from pathlib import Path

def append_entry(entry: str):
    diary_path = Path.home() / ".openclaw" / "workspace" / "diary.md"

    # Read existing content
    if diary_path.exists():
        content = diary_path.read_text()
    else:
        content = "# diary.md — Nova's Activity Log\n\n"

    # Append new entry
    content += f"\n{entry}\n"

    # Write back
    diary_path.write_text(content)
    print(f"✓ Appended to diary.md: {entry[:60]}...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 diary-append.py 'Your entry here'")
        sys.exit(1)

    append_entry(" ".join(sys.argv[1:]))
