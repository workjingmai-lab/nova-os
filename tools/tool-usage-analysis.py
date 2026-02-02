#!/usr/bin/env python3
"""
Analyze tool usage patterns from diary.md
"""

import re
from collections import Counter
from pathlib import Path

def main():
    diary_path = Path.home() / ".openclaw/workspace/diary.md"

    if not diary_path.exists():
        print("❌ diary.md not found")
        return

    content = diary_path.read_text()

    # Extract tool usage patterns
    # Pattern 1: "python3 tools/script.py"
    pattern1 = r'python3 tools/([a-z0-9_-]+\.py)'
    # Pattern 2: "script.py" references
    pattern2 = r'\b([a-z0-9_-]+\.py)\b'

    tools1 = re.findall(pattern1, content)
    tools2 = re.findall(pattern2, content)

    all_tools = tools1 + tools2

    # Count occurrences
    counter = Counter(all_tools)

    # Get top 10
    top10 = counter.most_common(10)

    print("\n" + "="*60)
    print("  📊 TOOL USAGE ANALYSIS (from diary.md)")
    print("="*60 + "\n")

    print(f"  Total tool mentions: {sum(counter.values())}\n")

    print("  Top 10 Most Used Tools:\n")
    for i, (tool, count) in enumerate(top10, 1):
        percentage = (count / sum(counter.values())) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {i}. {tool:<30} {count:>4}x  {bar}")

    # Identify 80/20 pattern
    total_tools = len(counter)
    top_5_count = sum(count for _, count in top10[:5])
    top_5_percentage = (top_5_count / sum(counter.values())) * 100

    print(f"\n  📈 80/20 Analysis:")
    print(f"     Total unique tools: {total_tools}")
    print(f"     Top 5 tools: {top_5_count} uses ({top_5_percentage:.1f}%)")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
