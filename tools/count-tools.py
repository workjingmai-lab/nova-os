#!/usr/bin/env python3
"""
Tool Counter

Quick count of tools in workspace/tools directory.

Usage:
    python3 tools/count-tools.py

Output:
    Total tools, documented tools, README coverage %
"""

import os
import glob

def count_tools():
    """Count tools and documentation coverage."""

    tools_dir = "/home/node/.openclaw/workspace/tools"

    # Count all .py files
    py_files = glob.glob(os.path.join(tools_dir, "*.py"))
    # Exclude __init__.py and self
    tools = [f for f in py_files if os.path.basename(f) != "__init__.py" and "count-tools" not in f]

    # Count README files
    readme_files = glob.glob(os.path.join(tools_dir, "README-*.md"))

    # Extract tool names from READMEs
    documented = set()
    for readme in readme_files:
        name = os.path.basename(readme).replace("README-", "").replace(".md", "")
        documented.add(name)

    # Check which tools have READMEs
    tools_with_readme = 0
    for tool in tools:
        tool_name = os.path.basename(tool).replace(".py", "")
        if tool_name in documented:
            tools_with_readme += 1

    total = len(tools)
    coverage = (tools_with_readme / total * 100) if total > 0 else 0

    return {
        "total": total,
        "documented": tools_with_readme,
        "coverage": coverage,
        "undocumented": total - tools_with_readme
    }

def main():
    stats = count_tools()

    print(f"📊 Tool Statistics:")
    print(f"   Total tools: {stats['total']}")
    print(f"   Documented: {stats['documented']}")
    print(f"   Coverage: {stats['coverage']:.1f}%")
    print(f"   Undocumented: {stats['undocumented']}")

if __name__ == "__main__":
    main()
