#!/usr/bin/env python3
"""
Trim today.md to keep ONLY the current (latest/newest) session.
Archive old sessions to memory/YYYY-MM-DD.md.
Run on session start to keep injected context minimal.
"""

import re
import sys
from datetime import datetime

def get_first_session_end(content: str) -> int:
    """Find the end of the first (current) session entry."""

    # Pattern 1: "**Latest Session (N):" format
    session_pattern = r'\*\*Latest Session \((\d+)\):'
    sessions = list(re.finditer(session_pattern, content))

    if len(sessions) > 1:
        # The first session ends where the second session starts
        return sessions[1].start()

    # Pattern 2: Try work block headers "## [WORK BLOCK N — timestamp]"
    work_block_pattern = r'## \[WORK BLOCK \d+ —'
    work_blocks = list(re.finditer(work_block_pattern, content))

    if len(work_blocks) > 1:
        # First work block ends where second one starts
        return work_blocks[1].start()

    # Pattern 3: Try bullet list work blocks "- Work block NNNN:"
    bullet_block_pattern = r'^- Work block \d+:'
    bullet_blocks = list(re.finditer(bullet_block_pattern, content, re.MULTILINE))

    if len(bullet_blocks) > 1:
        # First bullet block ends where second one starts
        return bullet_blocks[1].start()

    # No clear session boundaries found
    return -1  # No trimming needed

def archive_old_sessions(content: str, second_session_start: int, date_str: str) -> None:
    """Archive all but the first session to memory/YYYY-MM-DD.md."""

    # Find first session marker
    first_session_pattern = r'\*\*Latest Session \('
    first_match = re.search(first_session_pattern, content)
    if not first_match:
        return

    # Everything from first session to second session (exclusive)
    first_session_start = first_match.start()
    to_archive = content[first_session_start:second_session_start]

    if not to_archive.strip():
        return

    # Archive path
    archive_path = f'/home/node/.openclaw/workspace/memory/{date_str}.md'

    # Ensure memory/ directory exists
    import os
    os.makedirs('/home/node/.openclaw/workspace/memory', exist_ok=True)

    # Append to archive
    try:
        with open(archive_path, 'a') as f:
            f.write(f'\n\n{to_archive}')
        print(f"Archived sessions (except current) to {archive_path}")
    except IOError as e:
        print(f"Warning: Could not archive to {archive_path}: {e}")

def trim_today_md(input_path: str, output_path: str) -> int:
    """Trim today.md to only current session (first/newest one)."""

    try:
        with open(input_path, 'r') as f:
            content = f.read()
    except IOError as e:
        print(f"Error: Could not read {input_path}: {e}")
        return 0

    if not content.strip():
        print(f"Warning: {input_path} is empty. No trimming needed.")
        return 0

    # Find end of first session
    first_session_end = get_first_session_end(content)

    if first_session_end == -1:
        print(f"Only 1 session found. No trimming needed.")
        return 0

    # Archive old sessions (everything from first session marker to second session start)
    date_str = datetime.now().strftime('%Y-%m-%d')
    archive_old_sessions(content, first_session_end, date_str)

    # Keep everything from start to first session end
    trimmed = content[:first_session_end]

    try:
        with open(output_path, 'w') as f:
            f.write(trimmed)
    except IOError as e:
        print(f"Error: Could not write to {output_path}: {e}")
        return 0

    # Count how many sessions were removed
    session_pattern = r'\*\*Latest Session \((\d+)\):'
    original_count = len(re.findall(session_pattern, content))
    new_count = len(re.findall(session_pattern, trimmed))
    removed = original_count - new_count

    print(f"Trimmed {removed} old sessions (archived to memory/). Kept current session only.")
    if len(content) > 0:
        reduction_pct = 100 * len(trimmed) // len(content)
        print(f"Reduced size from {len(content)} to {len(trimmed)} bytes ({reduction_pct}%)")

    return removed

if __name__ == '__main__':
    input_file = '/home/node/.openclaw/workspace/today.md'
    output_file = '/home/node/.openclaw/workspace/today.md'

    trim_today_md(input_file, output_file)
