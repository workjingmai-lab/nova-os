#!/usr/bin/env python3
"""
Work Block Logger — Work block 2172+
Rapid diary.md updates with structured format
Run: python3 tools/work-block-logger.py "Your work block description here"
"""

import sys
import json
from datetime import datetime
from pathlib import Path

def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}

def get_block_number():
    """Get next work block number from today stats"""
    stats = load_json('data/.today-stats.json')
    current = stats.get('workBlocks', 2171)
    return current + 1

def format_entry(description):
    """Format work block entry for diary.md"""
    block_num = get_block_number()
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')

    # Clean description (remove newlines, truncate if too long)
    desc_clean = description.replace('\n', ' ').strip()
    if len(desc_clean) > 300:
        desc_clean = desc_clean[:297] + '...'

    entry = f"- Work block {block_num}: {desc_clean} [{timestamp}]"

    # Update today stats
    stats = load_json('data/.today-stats.json')
    stats['workBlocks'] = block_num
    stats['lastUpdated'] = timestamp
    with open('data/.today-stats.json', 'w') as f:
        json.dump(stats, f, indent=2)

    return entry, block_num

def verify_diary_health():
    """Quick check to ensure diary.md wasn't clobbered"""
    diary_path = Path('diary.md')
    if not diary_path.exists():
        return True  # New file is fine
    
    size = diary_path.stat().st_size
    lines = diary_path.read_text().count('\n')
    
    # If file is suspiciously small, warn but don't block
    if size < 500 and lines < 10:
        print(f"⚠️  WARNING: diary.md appears truncated ({size} bytes, {lines} lines)")
        print("   Recent data may have been lost.")
        print("   Continuing with append...")
        print()
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/work-block-logger.py \"Description of work block\"")
        print("\nExamples:")
        print('  python3 tools/work-block-logger.py "Created new tool X"')
        print('  python3 tools/work-block-logger.py "Updated documentation for Y"')
        print('  python3 tools/work-block-logger.py "Published Moltbook post about Z"')
        sys.exit(1)

    # Health check before write
    verify_diary_health()

    description = ' '.join(sys.argv[1:])
    entry, block_num = format_entry(description)

    # Append to diary.md
    with open('diary.md', 'a') as f:
        f.write(entry + '\n')

    print(f"✅ Work block {block_num} logged to diary.md")
    print(f"📝 Entry: {entry}")

    # Show stats
    stats = load_json('data/.today-stats.json')
    target = stats.get('target', 3000)
    progress = (block_num / target) * 100
    remaining = target - block_num

    print(f"\n📊 Progress: {block_num} / {target} ({progress:.1f}%) | Remaining: {remaining}")

if __name__ == '__main__':
    main()
