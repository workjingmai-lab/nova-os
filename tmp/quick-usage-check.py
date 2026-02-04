#!/usr/bin/env python3
"""Quick tool usage analysis - find most-used tools in diary.md"""
import re
from collections import Counter

diary_path = "/home/node/.openclaw/workspace/diary.md"
try:
    with open(diary_path, 'r') as f:
        content = f.read()

    # Find tool mentions (e.g., "revenue-tracker.py", "moltbook-suite.py")
    tool_pattern = r'(\w+[-]?\w*\.py)'
    tools = re.findall(tool_pattern, content)

    # Count occurrences
    tool_counts = Counter(tools)
    top_tools = tool_counts.most_common(20)

    print("🔊 TOP 20 MOST-MENTIONED TOOLS:")
    for i, (tool, count) in enumerate(top_tools, 1):
        print(f"{i:2}. {tool:30} {count:4} mentions")

except Exception as e:
    print(f"Error: {e}")
