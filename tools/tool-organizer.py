#!/usr/bin/env python3
"""
Tool Organizer — Categorize and Group Similar Tools

Analyzes tools/ directory and suggests consolidation opportunities.
Helps reduce tool sprawl and improve discoverability.

Usage:
    python3 tools/tool-organizer.py
"""

from pathlib import Path
from collections import defaultdict

TOOLS_DIR = Path("/home/node/.openclaw/workspace/tools")

# Tool categories based on naming patterns
CATEGORIES = {
    "Moltbook": ["moltbook", "post", "engagement"],
    "Goals & Planning": ["goal", "plan", "week", "target"],
    "Analysis": ["analyz", "pattern", "insight", "metric", "digest", "report"],
    "Automation": ["auto", "poster", "submit", "deploy"],
    "Relationships": ["relationship", "agent", "network", "connect"],
    "Documentation": ["doc", "ref", "guide", "template"],
    "Monitoring": ["monitor", "check", "status", "health", "heartbeat"],
    "Utilities": ["quick", "helper", "util", "tool"]
}

def categorize_tool(name):
    """Categorize tool by filename."""
    name_lower = name.lower()
    
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in name_lower:
                return category
    
    return "Other"

def scan_tools():
    """Scan tools directory and categorize."""
    tools = []
    
    for tool in TOOLS_DIR.glob("*.py"):
        if tool.name.startswith("_"):
            continue
            
        category = categorize_tool(tool.name)
        tools.append({
            "name": tool.name,
            "category": category,
            "path": tool
        })
    
    return tools

def print_header():
    print("=" * 60)
    print("🗂️  TOOL ORGANIZER")
    print("=" * 60)
    print()

def print_by_category(tools):
    """Group tools by category."""
    grouped = defaultdict(list)
    
    for tool in tools:
        grouped[tool["category"]].append(tool["name"])
    
    print("📁 TOOLS BY CATEGORY:")
    print("-" * 60)
    
    for category in sorted(grouped.keys()):
        tool_names = grouped[category]
        print(f"\n{category} ({len(tool_names)}):")
        for name in sorted(tool_names):
            print(f"  • {name}")
    
    print()

def print_consolidation_opportunities(tools):
    """Suggest consolidation opportunities."""
    print("🔍 CONSOLIDATION OPPORTUNITIES:")
    print("-" * 60)
    
    # Group by name similarity
    name_groups = defaultdict(list)
    
    for tool in tools:
        # Extract base name (remove -tracker.py, -analyzer.py, etc.)
        base = tool["name"].replace(".py", "")
        for suffix in ["-tracker", "-analyzer", "-monitor", "-checker", "-helper"]:
            if base.endswith(suffix):
                base = base[:-len(suffix)]
                break
        
        name_groups[base].append(tool["name"])
    
    # Find groups with 2+ tools
    for base, names in sorted(name_groups.items()):
        if len(names) >= 2:
            print(f"\n📦 {base} ({len(names)} tools):")
            for name in names:
                print(f"     • {name}")
            print(f"     → Consider: {base}-suite.py")

    print()

def print_stats(tools):
    """Print statistics."""
    total = len(tools)
    categories = len(set(t["category"] for t in tools))
    
    print("📊 STATISTICS:")
    print("-" * 60)
    print(f"  Total tools: {total}")
    print(f"  Categories: {categories}")
    print(f"  Avg per category: {total / categories:.1f}")
    print()

def print_recommendations(tools):
    """Generate recommendations."""
    print("💡 RECOMMENDATIONS:")
    print("-" * 60)
    
    # Count by category
    grouped = defaultdict(int)
    for tool in tools:
        grouped[tool["category"]] += 1
    
    # Largest categories
    largest = sorted(grouped.items(), key=lambda x: x[1], reverse=True)[:3]
    print("  • Largest categories:")
    for cat, count in largest:
        print(f"    - {cat}: {count} tools")
    
    print()
    print("  • Actions:")
    print("    - Archive unused tools (>30 days no use)")
    print("    - Consolidate similar tools (see opportunities above)")
    print("    - Create suite tools for related functionality")
    print("    - Update QUICK-TOOL-REF.md with top 10")
    print()

def main():
    print_header()
    
    tools = scan_tools()
    
    if not tools:
        print("⚠️  No tools found in tools/")
        return
    
    print_by_category(tools)
    print_consolidation_opportunities(tools)
    print_stats(tools)
    print_recommendations(tools)
    
    print("=" * 60)
    print("✅ Organization complete. Keep tools lean!")
    print("=" * 60)

if __name__ == "__main__":
    main()
