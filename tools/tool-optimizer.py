#!/usr/bin/env python3
"""
tool-optimizer.py — Analyze tool usage and suggest improvements

Usage:
    # Show low-usage tools (archival candidates)
    python3 tools/tool-optimizer.py --unused

    # Show duplicate tools (consolidation candidates)
    python3 tools/tool-optimizer.py --duplicates

    # Show popular tools (high-priority maintenance)
    python3 tools/tool-optimizer.py --popular

    # Full optimization report
    python3 tools/tool-optimizer.py --report

This script:
1. Scans diary.md for tool mentions
2. Counts usage per tool
3. Identifies patterns (unused, duplicates, popular)
4. Suggests actions (archive, consolidate, prioritize)

Metrics:
- Mention count (from diary.md)
- Age (file modification time)
- Documentation status (README exists or not)
- Size (lines of code)
"""

import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from collections import Counter

DIARY_FILE = Path("/home/node/.openclaw/workspace/diary.md")
TOOLS_DIR = Path("/home/node/.openclaw/workspace/tools")

def scan_diary() -> Counter:
    """Scan diary.md for tool mentions."""
    if not DIARY_FILE.exists():
        return Counter()

    with open(DIARY_FILE) as f:
        content = f.read()

    # Find tool mentions (python3 tools/*.py patterns)
    pattern = r'tools/([a-z0-9_-]+)\.py'
    mentions = re.findall(pattern, content)

    return Counter(mentions)

def scan_tools() -> List[Dict]:
    """Scan tools directory for metadata."""
    tools = []

    for file in TOOLS_DIR.glob("*.py"):
        # Skip main/test files
        if file.name.startswith("__") or file.name == "tool-optimizer.py":
            continue

        tool = {
            "name": file.stem,
            "file": file.name,
            "mtime": datetime.fromtimestamp(file.stat().st_mtime),
            "size_lines": len(file.read_text().splitlines()),
            "has_readme": (TOOLS_DIR / f"README.{file.stem}.md").exists()
        }

        tools.append(tool)

    return tools

def calculate_age(tool: Dict) -> int:
    """Calculate tool age in days."""
    age = datetime.utcnow() - tool["mtime"]
    return age.days

def find_unused(tools: List[Dict], usage: Counter) -> List[Dict]:
    """Find tools with low or zero usage."""
    unused = []

    for tool in tools:
        mentions = usage.get(tool["name"], 0)
        if mentions == 0:
            unused.append({**tool, "mentions": mentions, "reason": "never mentioned"})

    return sorted(unused, key=lambda t: t["size_lines"], reverse=True)

def find_duplicates(tools: List[Dict]) -> List[Tuple[Dict, Dict, str]]:
    """Find potentially duplicate tools."""
    duplicates = []

    # Simple heuristic: similar names
    for i, t1 in enumerate(tools):
        for t2 in tools[i+1:]:
            # Check name similarity
            if t1["name"] in t2["name"] or t2["name"] in t1["name"]:
                reason = "similar names"
                duplicates.append((t1, t2, reason))

    return duplicates

def find_popular(tools: List[Dict], usage: Counter) -> List[Dict]:
    """Find most-used tools."""
    popular = []

    for tool in tools:
        mentions = usage.get(tool["name"], 0)
        if mentions > 0:
            popular.append({**tool, "mentions": mentions})

    return sorted(popular, key=lambda t: t["mentions"], reverse=True)

def show_unused(unused: List[Dict]):
    """Show archival candidates."""
    if not unused:
        print("\n✅ No unused tools found")
        return

    print(f"\n📦 UNUSED TOOLS ({len(unused)} candidates for archival)")
    print("=" * 70)
    print(f"{'Size':<6} {'Age':<6} {'Tool'}")
    print("-" * 70)

    for tool in unused[:10]:  # Top 10
        age_days = calculate_age(tool)
        print(f"{tool['size_lines']:<6} {age_days:<6} {tool['name']}")

    if len(unused) > 10:
        print(f"\n  ... and {len(unused) - 10} more")

    print(f"\n💡 Consider archiving tools:")
    print(f"  • Never mentioned in diary.md")
    print(f"  • Large files cost more to maintain than small ones")
    print(f"  • Archive to tools/archived/ to preserve without maintaining")

def show_duplicates(duplicates: List[Tuple[Dict, Dict, str]]):
    """Show consolidation candidates."""
    if not duplicates:
        print("\n✅ No obvious duplicates found")
        return

    print(f"\n🔄 DUPLICATE CANDIDATES ({len(duplicates)} pairs)")
    print("=" * 70)

    for t1, t2, reason in duplicates[:10]:
        print(f"  • {t1['name']} ↔ {t2['name']}")
        print(f"    Reason: {reason}")
        print(f"    Sizes: {t1['size_lines']} vs {t2['size_lines']} lines")

    if len(duplicates) > 10:
        print(f"\n  ... and {len(duplicates) - 10} more")

    print(f"\n💡 Consider consolidating:")
    print(f"  • Merge overlapping functionality")
    print(f"  • Keep the larger/more complete version")
    print(f"  • Add migration note to README")

def show_popular(popular: List[Dict]):
    """Show high-priority tools."""
    if not popular:
        print("\n❌ No tool usage data found")
        return

    print(f"\n⭐ POPULAR TOOLS ({len(popular)} tools with usage)")
    print("=" * 70)
    print(f"{'Uses':<6} {'Tool'}")
    print("-" * 70)

    for tool in popular[:15]:
        print(f"{tool['mentions']:<6} {tool['name']}")

    if len(popular) > 15:
        print(f"\n  ... and {len(popular) - 15} more")

    print(f"\n💡 Prioritize maintenance:")
    print(f"  • High-usage tools breakage = high impact")
    print(f"  • Add tests for top 10 tools")
    print(f"  • Consider optimization for frequently-used tools")

def show_report(tools: List[Dict], usage: Counter):
    """Show full optimization report."""
    print("\n" + "=" * 70)
    print("  🛠️ TOOL OPTIMIZATION REPORT")
    print("=" * 70)

    # Overview
    print(f"\n📊 OVERVIEW")
    print("-" * 70)
    print(f"  Total tools:        {len(tools)}")
    print(f"  Total mentions:     {sum(usage.values())}")
    print(f"  Tools with usage:   {len([t for t in tools if usage.get(t['name'], 0) > 0])}")
    print(f"  Tools unused:       {len([t for t in tools if usage.get(t['name'], 0) == 0])}")
    print(f"  Avg mentions/tool:  {sum(usage.values()) / max(1, len(tools)):.1f}")

    # Documentation status
    documented = len([t for t in tools if t["has_readme"]])
    print(f"\n📚 DOCUMENTATION")
    print("-" * 70)
    print(f"  With README:        {documented} ({documented/len(tools)*100:.1f}%)")
    print(f"  Without README:     {len(tools) - documented}")

    # Age distribution
    ages = [calculate_age(t) for t in tools]
    old_tools = len([a for a in ages if a > 30])
    new_tools = len([a for a in ages if a < 7])

    print(f"\n📅 AGE DISTRIBUTION")
    print("-" * 70)
    print(f"  New (< 7 days):     {new_tools}")
    print(f"  Old (> 30 days):    {old_tools}")
    print(f"  Average age:        {sum(ages) / len(ages):.1f} days")

    # Recommendations
    print(f"\n💡 RECOMMENDATIONS")
    print("-" * 70)

    unused_count = len([t for t in tools if usage.get(t['name'], 0) == 0])
    if unused_count > 10:
        print(f"  • Archive {unused_count} unused tools (>10%)")
        print(f"    → Reduces maintenance burden")

    undocumented = len(tools) - documented
    if undocumented > 0:
        print(f"  • Document {undocumented} tools missing READMEs")
        print(f"    → Enables ecosystem adoption")

    if new_tools > 5:
        print(f"  • Review {new_tools} new tools from last week")
        print(f"    → Consolidate overlapping functionality")

    top_tool = max(tools, key=lambda t: usage.get(t['name'], 0))
    top_mentions = usage.get(top_tool['name'], 0)
    if top_mentions > 50:
        print(f"  • {top_tool['name']} has {top_mentions} mentions (high impact)")
        print(f"    → Add tests, optimize, document thoroughly")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 tools/tool-optimizer.py --unused")
        print("  python3 tools/tool-optimizer.py --duplicates")
        print("  python3 tools/tool-optimizer.py --popular")
        print("  python3 tools/tool-optimizer.py --report")
        sys.exit(1)

    args = sys.argv[1:]

    # Load data
    usage = scan_diary()
    tools = scan_tools()

    if not tools:
        print("❌ No tools found")
        sys.exit(1)

    if "--unused" in args:
        unused = find_unused(tools, usage)
        show_unused(unused)

    elif "--duplicates" in args:
        duplicates = find_duplicates(tools)
        show_duplicates(duplicates)

    elif "--popular" in args:
        popular = find_popular(tools, usage)
        show_popular(popular)

    elif "--report" in args:
        show_report(tools, usage)

    else:
        print("❌ Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
