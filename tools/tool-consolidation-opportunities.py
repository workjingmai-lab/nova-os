#!/usr/bin/env python3
"""
Tool Consolidation Opportunities Analyzer

Identifies tools that could be consolidated based on:
- Similar naming patterns
- Small file sizes (< 2KB = potential utils to merge)
- Duplicate functionality patterns
"""

import re
from pathlib import Path
from collections import defaultdict

def get_tool_stats():
    """Get statistics about all tools."""
    tools_dir = Path("/home/node/.openclaw/workspace/tools")
    tools = []

    for tool_file in tools_dir.glob("*.py"):
        stats = tool_file.stat()
        content = tool_file.read_text()

        tools.append({
            'name': tool_file.name,
            'size': stats.st_size,
            'lines': len(content.split('\n')),
            'functions': len(re.findall(r'^def \w+', content, re.MULTILINE)),
            'classes': len(re.findall(r'^class \w+', content, re.MULTILINE)),
            'has_readme': (tool_file.parent / f"{tool_file.stem}.README.md").exists()
        })

    return tools

def find_consolidation_opportunities(tools):
    """Identify consolidation opportunities."""
    opportunities = []

    # 1. Tiny tools (< 2KB) - potential utils to merge
    tiny_tools = [t for t in tools if t['size'] < 2048]
    if tiny_tools:
        opportunities.append({
            'type': 'Tiny Tools (< 2KB)',
            'count': len(tiny_tools),
            'candidates': [t['name'] for t in sorted(tiny_tools, key=lambda x: x['size'])[:10]],
            'recommendation': 'Consider merging into utility modules'
        })

    # 2. Similar naming patterns (potential duplicates)
    name_groups = defaultdict(list)
    for tool in tools:
        # Extract base name (remove suffixes like -checker, -analyzer, etc.)
        base = re.sub(r'-(?:checker|analyzer|tracker|monitor|scanner|tool|util)$', '', tool['name'])
        name_groups[base].append(tool['name'])

    duplicates = {k: v for k, v in name_groups.items() if len(v) > 1}
    if duplicates:
        dup_candidates = []
        for base, names in sorted(duplicates.items(), key=lambda x: -len(x[1])):
            dup_candidates.extend(names[:5])
        opportunities.append({
            'type': 'Similar Names (Potential Duplicates)',
            'count': sum(len(v) for v in duplicates.values()),
            'candidates': dup_candidates[:15],
            'recommendation': 'Review for functional overlap'
        })

    # 3. Single-function tools (potential candidates for consolidation)
    single_func = [t for t in tools if t['functions'] == 1 and t['classes'] == 0 and t['size'] < 4096]
    if single_func:
        opportunities.append({
            'type': 'Single-Function Tools (< 4KB)',
            'count': len(single_func),
            'candidates': [t['name'] for t in sorted(single_func, key=lambda x: x['size'])[:10]],
            'recommendation': 'Consider consolidating into theme-based modules'
        })

    # 4. Tools without READMEs (from earlier stats)
    no_readme = [t for t in tools if not t['has_readme']]
    if no_readme:
        opportunities.append({
            'type': 'Undocumented Tools (No README)',
            'count': len(no_readme),
            'candidates': [t['name'] for t in sorted(no_readme, key=lambda x: x['name'])[:15]],
            'recommendation': 'Add READMEs or consider deprecation'
        })

    return opportunities

def main():
    print("🔧 Tool Consolidation Opportunities")
    print("=" * 60)

    tools = get_tool_stats()
    total_size = sum(t['size'] for t in tools) / 1024  # KB

    print(f"\n📊 Tool Inventory: {len(tools)} tools ({total_size:.1f} KB total)")
    print(f"   Average size: {total_size/len(tools):.1f} KB per tool")

    # Size distribution
    tiny = sum(1 for t in tools if t['size'] < 2048)
    small = sum(1 for t in tools if 2048 <= t['size'] < 10240)
    large = sum(1 for t in tools if t['size'] >= 10240)

    print(f"\n📏 Size Distribution:")
    print(f"   Tiny (< 2KB): {tiny} tools ({tiny/len(tools)*100:.1f}%)")
    print(f"   Small (2-10KB): {small} tools ({small/len(tools)*100:.1f}%)")
    print(f"   Large (≥ 10KB): {large} tools ({large/len(tools)*100:.1f}%)")

    # Find opportunities
    opportunities = find_consolidation_opportunities(tools)

    print(f"\n🎯 Consolidation Opportunities:")
    for opp in opportunities:
        print(f"\n   {opp['type']}: {opp['count']} tools")
        print(f"   💡 {opp['recommendation']}")
        if opp['candidates']:
            print(f"   Examples: {', '.join(opp['candidates'][:8])}")

    # Complexity analysis
    complex_tools = sorted(tools, key=lambda x: -x['functions'])[:10]
    print(f"\n🏗️ Most Complex Tools (by function count):")
    for tool in complex_tools:
        print(f"   {tool['name']}: {tool['functions']} functions, {tool['size']/1024:.1f} KB")

    print("\n" + "=" * 60)
    print("✅ Analysis complete")

if __name__ == "__main__":
    main()
