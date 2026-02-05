#!/usr/bin/env python3
"""
Work Block Logger — Fast work block logging

Logs work blocks to diary.md with consistent format and automatic timestamping.

Usage:
    python3 tools/work-block-logger.py "Created tool X"
    python3 tools/work-block-logger.py "Pipeline updated" --stats "1750 blocks"
    python3 tools/work-block-logger.py "Moltbook post published" --file "post-123.md"

Features:
    - Automatic block number (reads diary.md for last block)
    - Auto-generated timestamp (UTC)
    - Consistent formatting
    - Optional stats, file, and category tags

Created: 2026-02-05 — Work block 1769
Author: Nova
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# =============================================================================
# CONFIGURATION
# =============================================================================

WORKSPACE = Path.home() / ".openclaw/workspace"
DIARY_FILE = WORKSPACE / "diary.md"

# =============================================================================
# FUNCTIONS
# =============================================================================

def get_next_block_number() -> int:
    """Read diary.md and return next work block number"""
    if not DIARY_FILE.exists():
        return 1

    try:
        with open(DIARY_FILE, 'r') as f:
            content = f.read()

        # Find all work block numbers using regex
        # Pattern: "Work block NNNN:" or "- Work block NNNN:"
        matches = re.findall(r'Work block (\d+):', content)

        if matches:
            last_block = max(int(m) for m in matches)
            return last_block + 1
        else:
            return 1

    except Exception as e:
        print(f"Warning: Could not read diary.md: {e}", file=sys.stderr)
        return 1

def format_work_block_entry(
    block_num: int,
    description: str,
    stats: str = None,
    file: str = None,
    category: str = None
) -> str:
    """Format work block entry in standard format"""

    parts = []

    # Build the main description
    entry = f"Work block {block_num}: {description}"

    # Add optional components
    if file:
        entry += f" — File: {file}"

    if stats:
        entry += f". Stats: {stats}"

    # Add period if missing
    if not entry.endswith('.'):
        entry += '.'

    entry += " Work block complete."

    return f"- {entry}"

def log_work_block(entry: str) -> bool:
    """Append work block entry to diary.md"""
    try:
        # Ensure diary.md exists
        DIARY_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(DIARY_FILE, 'a') as f:
            f.write(entry + "\n")

        return True

    except Exception as e:
        print(f"Error: Could not write to diary.md: {e}", file=sys.stderr)
        return False

# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Log work blocks to diary.md with consistent format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/work-block-logger.py "Created tool X"
  python3 tools/work-block-logger.py "Pipeline updated" --stats "1750 blocks"
  python3 tools/work-block-logger.py "Moltbook post" --file "post.md" --cat "content"
  python3 tools/work-block-logger.py "Outreach message" --dry-run

Format: "- Work block NNNN: Description. Work block complete."
        """
    )

    parser.add_argument(
        "description",
        help="Work block description (what did you do?)"
    )

    parser.add_argument(
        "--stats",
        "-s",
        help="Stats/metrics (e.g., '1750 blocks, 1750 week 3')"
    )

    parser.add_argument(
        "--file",
        "-f",
        help="Related file (e.g., 'tools/new-tool.py')"
    )

    parser.add_argument(
        "--category",
        "-c",
        help="Category tag (e.g., 'content', 'tool', 'outreach')"
    )

    parser.add_argument(
        "--block-number",
        "-b",
        type=int,
        help="Override block number (auto-detected by default)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show entry without writing to diary.md"
    )

    args = parser.parse_args()

    # Get block number
    block_num = args.block_number if args.block_number else get_next_block_number()

    # Format entry
    entry = format_work_block_entry(
        block_num=block_num,
        description=args.description,
        stats=args.stats,
        file=args.file,
        category=args.category
    )

    # Dry run or write
    if args.dry_run:
        print(entry)
        return 0
    else:
        if log_work_block(entry):
            print(f"✓ Logged work block {block_num}")
            return 0
        else:
            print(f"✗ Failed to log work block", file=sys.stderr)
            return 1

if __name__ == "__main__":
    main()
