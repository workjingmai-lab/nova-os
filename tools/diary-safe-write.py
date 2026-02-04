#!/usr/bin/env python3
"""
Diary Safe Write Helper
Prevents accidental overwrites of diary.md by verifying before write.

Usage:
  python tools/diary-safe-write.py --check-before-write
  python tools/diary-safe-write.py --append "Entry content"
"""

import argparse
from pathlib import Path
from datetime import datetime

DIARY_MD = Path.home() / ".openclaw" / "workspace" / "diary.md"

def check_diary_health():
    """Check diary.md health before write operations."""
    if not DIARY_MD.exists():
        print("❌ diary.md does not exist")
        return False

    # Get file stats
    size = DIARY_MD.stat().st_size
    mtime = datetime.fromtimestamp(DIARY_MD.stat().st_mtime)

    # Read first and last lines
    with open(DIARY_MD) as f:
        lines = f.readlines()
        first_line = lines[0].strip() if lines else ""
        last_line = lines[-1].strip() if lines else ""

    print(f"📊 diary.md Health Check:")
    print(f"   Size: {size:,} bytes ({size/1024:.1f} KB)")
    print(f"   Lines: {len(lines):,}")
    print(f"   Last modified: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   First line: {first_line[:60]}...")
    print(f"   Last line: {last_line[:60]}...")

    # Warnings
    warnings = []
    if size < 10000:  # Less than 10KB
        warnings.append("⚠️  File size suspiciously small (< 10KB)")
    if len(lines) < 100:
        warnings.append("⚠️  Line count suspiciously low (< 100 lines)")
    if not first_line.startswith("#"):
        warnings.append("⚠️  First line doesn't start with # (header)")

    if warnings:
        print("\n⚠️  WARNINGS:")
        for w in warnings:
            print(f"   {w}")
        print("\n❌ DIARY HEALTH CHECK FAILED")
        print("   Do NOT write. Investigate first.")
        return False
    else:
        print("\n✅ DIARY HEALTH CHECK PASSED")
        return True

def append_entry(content):
    """Safely append an entry to diary.md."""
    if not check_diary_health():
        print("\n❌ Write blocked: diary health check failed")
        return False

    # Confirm before write
    print(f"\n📝 Ready to append:")
    print(f"   {content[:100]}...")
    print("\n⚠️  This will APPEND to diary.md (not overwrite)")
    print("   Press Ctrl+C to cancel, or Enter to continue...")

    try:
        input()
    except KeyboardInterrupt:
        print("\n❌ Write cancelled")
        return False

    # Append with timestamp
    with open(DIARY_MD, "a") as f:
        f.write(f"\n{content}\n")

    print("✅ Entry appended successfully")
    return True

def main():
    parser = argparse.ArgumentParser(description="Diary Safe Write Helper")
    parser.add_argument("--check-before-write", action="store_true",
                       help="Check diary health before writing")
    parser.add_argument("--append", type=str, metavar="CONTENT",
                       help="Append content to diary (with safety checks)")

    args = parser.parse_args()

    if args.check_before_write:
        check_diary_health()
    elif args.append:
        append_entry(args.append)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
