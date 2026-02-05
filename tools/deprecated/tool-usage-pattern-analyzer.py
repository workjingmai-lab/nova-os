#!/usr/bin/env python3
"""
Tool Usage Pattern Analyzer

Analyzes diary.md and tool files to identify:
- Most frequently used tools
- Tools by category
- Consolidation opportunities
- Core tools vs edge case tools
"""

import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timedelta

def read_diary():
    """Read diary.md entries."""
    diary_path = Path("/home/node/.openclaw/workspace/diary.md")
    if not diary_path.exists():
        return ""
    return diary_path.read_text()

def extract_tool_invocations(text):
    """Extract tool invocations from diary entries."""
    # Pattern: Work block X: tool-name.py description
    pattern = r'Work block \d+: ([\w-]+\.py)'
    matches = re.findall(pattern, text)
    return matches

def categorize_tools():
    """Categorize tools by function based on naming patterns."""
    categories = {
        'Workflow': ['diary-', 'goal-', 'task-', 'block-', 'session-', 'heartbeat'],
        'Analytics': ['analytics', 'tracker', 'metrics', 'report', 'pattern', 'usage'],
        'Revenue': ['grant', 'service', 'revenue', 'proposal', 'moltbook', 'code4rena'],
        'Automation': ['batch', 'executor', 'runner', 'automation', 'nexus'],
        'Documentation': ['readme', 'docs', 'document'],
        'Testing': ['test', 'check', 'verify', 'validate']
    }

    tool_files = list(Path("/home/node/.openclaw/workspace/tools").glob("*.py"))
    categorized = defaultdict(list)

    for tool in tool_files:
        name = tool.name.lower()
        placed = False
        for category, patterns in categories.items():
            if any(pattern in name for pattern in patterns):
                categorized[category].append(tool.name)
                placed = True
                break
        if not placed:
            categorized['Other'].append(tool.name)

    return categorized, len(tool_files)

def main():
    print("🔍 Tool Usage Pattern Analyzer")
    print("=" * 50)

    # Analyze tool inventory
    categorized, total_tools = categorize_tools()

    print(f"\n📊 Tool Inventory: {total_tools} tools")
    print("\nBy Category:")
    for category, tools in sorted(categorized.items(), key=lambda x: -len(x[1])):
        print(f"  {category}: {len(tools)} tools")

    # Analyze usage patterns from diary
    diary_text = read_diary()
    tool_invocations = extract_tool_invocations(diary_text)

    if tool_invocations:
        print(f"\n📈 Usage Analysis: {len(tool_invocations)} invocations logged")

        # Top 10 most used tools
        counter = Counter(tool_invocations)
        print("\n🔥 Top 10 Most Used Tools:")
        for tool, count in counter.most_common(10):
            print(f"  {tool}: {count} uses")

        # Tools never used
        all_tools = [t.name for t in Path("/home/node/.openclaw/workspace/tools").glob("*.py")]
        used_tools = set(tool_invocations)
        unused_tools = set(all_tools) - used_tools

        print(f"\n📦 Unused Tools: {len(unused_tools)} ({len(unused_tools)/len(all_tools)*100:.1f}%)")
        if len(unused_tools) <= 20:
            for tool in sorted(unused_tools):
                print(f"  - {tool}")
        else:
            print(f"  (Too many to list - first 20)")
            for tool in sorted(unused_tools)[:20]:
                print(f"  - {tool}")

        # Core tools analysis (Pareto principle)
        print("\n🎯 Core Tools Analysis (Pareto 80/20):")
        cumulative_uses = 0
        total_uses = sum(counter.values())
        core_tools = []

        for tool, count in counter.most_common():
            cumulative_uses += count
            core_tools.append(tool)
            if cumulative_uses >= total_uses * 0.8:
                break

        print(f"  {len(core_tools)} tools provide 80% of usage ({len(core_tools)/len(all_tools)*100:.1f}% of inventory)")
        print(f"  Core tools: {', '.join(core_tools[:10])}{'...' if len(core_tools) > 10 else ''}")

        # Consolidation opportunities
        print("\n🔧 Consolidation Opportunities:")
        category_counts = {cat: len(tools) for cat, tools in categorized.items()}
        large_categories = [(cat, count) for cat, count in category_counts.items() if count > 10]

        if large_categories:
            for cat, count in sorted(large_categories, key=lambda x: -x[1]):
                print(f"  {cat}: {count} tools - consider consolidation")
        else:
            print("  None identified - categories well-distributed")

    else:
        print("\n⚠️ No tool usage found in diary.md")
        print("   Consider logging work blocks with tool names")

    print("\n" + "=" * 50)
    print("✅ Analysis complete")

if __name__ == "__main__":
    main()
