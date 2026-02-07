#!/usr/bin/env python3
"""
Tool Index — All Tools, All Purposes, Quick Reference
Complete catalog of every tool in the workspace.

Usage:
    python3 tools/tool-index.py              # Show all tools
    python3 tools/tool-index.py core         # Show core tools only
    python3 tools/tool-index.py search <term> # Search by keyword
"""

from pathlib import Path
import re

TOOLS_DIR = Path("/home/node/.openclaw/workspace/tools")

def get_all_tools():
    """Get list of all Python tools."""
    tools = []
    
    for tool_file in TOOLS_DIR.glob("*.py"):
        # Skip __pycache__ and test files
        if "__pycache__" in str(tool_file) or "test" in tool_file.name:
            continue
        
        name = tool_file.stem
        path = str(tool_file.relative_to(TOOLS_DIR.parent))
        
        # Try to extract description from file
        description = ""
        try:
            with open(tool_file, 'r') as f:
                content = f.read(500)  # Read first 500 chars
                # Look for docstring
                match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                if match:
                    desc_lines = match.group(1).strip().split('\n')
                    # Take first non-empty line
                    for line in desc_lines:
                        line = line.strip()
                        if line and not line.startswith('Usage'):
                            description = line
                            break
        except:
            pass
        
        if not description:
            description = "Tool script"
        
        tools.append({
            "name": name,
            "path": path,
            "description": description
        })
    
    return sorted(tools, key=lambda x: x["name"])

def categorize_tool(name):
    """Categorize tool by purpose."""
    name_lower = name.lower()
    
    if "revenue" in name_lower or "pipeline" in name_lower or "conversion" in name_lower:
        return "Revenue"
    elif "follow" in name_lower or "tracker" in name_lower:
        return "Tracking"
    elif "moltbook" in name_lower:
        return "Moltbook"
    elif "milestone" in name_lower or "progress" in name_lower or "status" in name_lower:
        return "Progress"
    elif "trim" in name_lower or "clean" in name_lower:
        return "Maintenance"
    elif "send" in name_lower or "submit" in name_lower or "outreach" in name_lower:
        return "Execution"
    elif "analytics" in name_lower or "analysis" in name_lower or "report" in name_lower:
        return "Analytics"
    else:
        return "General"

def print_tools(tools, filter_category=None):
    """Print tools in formatted table."""
    
    if filter_category:
        tools = [t for t in tools if categorize_tool(t["name"]) == filter_category]
        print(f"📂 {filter_category} TOOLS")
    else:
        print("🔧 ALL TOOLS")
    
    print("=" * 80)
    print(f"{'Tool':<30} {'Category':<15} {'Description':<30}")
    print("-" * 80)
    
    for tool in tools:
        category = categorize_tool(tool["name"])
        desc = tool["description"][:27] + "..." if len(tool["description"]) > 30 else tool["description"]
        print(f"{tool['name']:<30} {category:<15} {desc:<30}")
    
    print()
    print(f"Total: {len(tools)} tools")

def main():
    import sys
    
    tools = get_all_tools()
    
    if len(sys.argv) < 2:
        print_tools(tools)
    elif sys.argv[1] == "core":
        # Show most important tools
        core_tools = [
            "revenue-tracker", "follow-up-tracker", "moltbook-suite",
            "3000-milestone", "daily-progress", "trim-today",
            "execution-gap", "conversion-tracker"
        ]
        core = [t for t in tools if t["name"] in core_tools]
        print_tools(core)
    elif sys.argv[1] == "search":
        if len(sys.argv) < 3:
            print("Usage: python3 tools/tool-index.py search <term>")
            return
        
        term = sys.argv[2].lower()
        filtered = [t for t in tools if term in t["name"].lower() or term in t["description"].lower()]
        print(f"🔍 SEARCH: '{term}'")
        print_tools(filtered)
    else:
        category = sys.argv[1].title()
        print_tools(tools, filter_category=category)

if __name__ == "__main__":
    main()
