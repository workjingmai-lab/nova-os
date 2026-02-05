#!/usr/bin/env python3
"""
pattern-peek.py — Quick pattern scan of any text file
Usage: python3 pattern-peek.py <file> [pattern]
"""

import re
import sys
from collections import Counter
from pathlib import Path

def scan_patterns(filepath, pattern=None):
    """Scan file for patterns"""
    content = Path(filepath).read_text()

    if pattern:
        # Custom pattern search
        matches = re.findall(pattern, content, re.IGNORECASE)
        return {"pattern": pattern, "count": len(matches), "matches": matches[:10]}

    # Default patterns: common work patterns
    patterns = {
        "Work Blocks": r"Work Block \d+",
        "Insights": r"Key Insight: (.+)",
        "Files Created": r"Files Created: (.+)",
        "Tasks": r"\*\*Task:\*\* (.+)",
        "Session Complete": r"SESSION COMPLETE",
    }

    results = {}
    for name, pat in patterns.items():
        matches = re.findall(pat, content)
        results[name] = len(matches)

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pattern-peek.py <file> [pattern]")
        sys.exit(1)

    filepath = sys.argv[1]
    custom = sys.argv[2] if len(sys.argv) > 2 else None

    result = scan_patterns(filepath, custom)

    if custom:
        print(f"Pattern: {result['pattern']}")
        print(f"Count: {result['count']}")
        if result['matches']:
            print(f"\nFirst 10 matches:")
            for m in result['matches']:
                print(f"  - {m.strip()[:80]}")
        else:
            # If no capturing group, show context
            import re
            content = Path(filepath).read_text()
            lines = content.split('\n')
            matches = [i for i, line in enumerate(lines) if re.search(custom, line, re.IGNORECASE)]
            print(f"\nFound at lines: {matches[:10]}")
    else:
        print("Pattern Scan Results:")
        for name, count in result.items():
            print(f"  {name}: {count}")
