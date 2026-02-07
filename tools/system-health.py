#!/usr/bin/env python3
"""
system-health.py — One-command system status dashboard

Quick overview of all key metrics: work blocks, tools, pipeline, blockers.

Usage:
    python3 tools/system-health.py           # Full dashboard
    python3 tools/system-health.py --mini    # Compact view
"""

import argparse
import json
import re
from pathlib import Path
from datetime import datetime, timezone

WORKSPACE = Path.home() / ".openclaw/workspace"
MEMORY_DIR = WORKSPACE / "memory"
TOOLS_DIR = WORKSPACE / "tools"
DATA_DIR = WORKSPACE / "data"

def count_work_blocks_today():
    """Count work blocks in today's diary."""
    today_file = MEMORY_DIR / datetime.now(timezone.utc).strftime("%Y-%m-%d.md")
    if not today_file.exists():
        return 0
    
    content = today_file.read_text()
    return len(re.findall(r'Work Block \d+', content))

def count_total_work_blocks():
    """Count total work blocks across all diary files."""
    total = 0
    for diary in MEMORY_DIR.glob("*.md"):
        if diary.name.startswith("20"):  # Date files like 2026-02-07.md
            content = diary.read_text()
            total += len(re.findall(r'Work Block \d+', content))
    return total

def get_tool_stats():
    """Get tool and documentation counts."""
    py_tools = list(TOOLS_DIR.glob("*.py"))
    readme_docs = list(TOOLS_DIR.glob("README*.md"))
    
    return {
        "tools": len(py_tools),
        "docs": len(readme_docs),
        "coverage": f"{len(readme_docs)/len(py_tools)*100:.0f}%" if py_tools else "0%"
    }

def get_pipeline_summary():
    """Get revenue pipeline summary."""
    pipeline_file = DATA_DIR / "revenue-pipeline.json"
    if not pipeline_file.exists():
        return {"total": 0, "ready": 0, "submitted": 0, "won": 0}
    
    with open(pipeline_file) as f:
        data = json.load(f)
    
    items = data.get("items", [])
    return {
        "total": sum(i.get("potential", 0) for i in items),
        "ready": sum(i.get("potential", 0) for i in items if i.get("status") == "ready"),
        "submitted": sum(i.get("potential", 0) for i in items if i.get("status") == "submitted"),
        "won": sum(i.get("potential", 0) for i in items if i.get("status") == "won")
    }

def format_money(n):
    """Format number as currency."""
    if n >= 1000000:
        return f"${n/1000000:.2f}M"
    elif n >= 1000:
        return f"${n/1000:.0f}K"
    return f"${n}"

def main():
    parser = argparse.ArgumentParser(description="System health dashboard")
    parser.add_argument("--mini", action="store_true", help="Compact view")
    args = parser.parse_args()
    
    blocks_today = count_work_blocks_today()
    total_blocks = count_total_work_blocks()
    tools = get_tool_stats()
    pipeline = get_pipeline_summary()
    
    now = datetime.now(timezone.utc).strftime("%H:%M UTC")
    
    if args.mini:
        print(f"🧩 {blocks_today} blocks | 🛠️ {tools['tools']} tools | 💰 {format_money(pipeline['total'])} | {now}")
        return
    
    print("╔════════════════════════════════════════╗")
    print("║        🦞 SYSTEM HEALTH DASHBOARD      ║")
    print(f"║              {now}              ║")
    print("╠════════════════════════════════════════╣")
    print("║                                        ║")
    print(f"║  📊 WORK BLOCKS                        ║")
    print(f"║     Today:     {blocks_today:4d}                    ║")
    print(f"║     Total:     {total_blocks:4d}                    ║")
    print("║                                        ║")
    print(f"║  🛠️  TOOLS                              ║")
    print(f"║     Python:    {tools['tools']:4d}                    ║")
    print(f"║     READMEs:   {tools['docs']:4d} ({tools['coverage']:>4s})             ║")
    print("║                                        ║")
    print(f"║  💰 REVENUE PIPELINE                   ║")
    print(f"║     Total:     {format_money(pipeline['total']):>10s}             ║")
    print(f"║     Ready:     {format_money(pipeline['ready']):>10s}             ║")
    print(f"║     Submitted: {format_money(pipeline['submitted']):>10s}             ║")
    print(f"║     Won:       {format_money(pipeline['won']):>10s}             ║")
    print("║                                        ║")
    
    # Blockers
    blockers = []
    if pipeline['total'] > 0 and pipeline['submitted'] == 0:
        blockers.append("No submissions yet")
    
    if blockers:
        print(f"║  ⚠️  BLOCKERS                          ║")
        for b in blockers[:2]:
            print(f"║     • {b[:32]:32s} ║")
        print("║                                        ║")
    
    print("╚════════════════════════════════════════╝")
    print()
    print("Quick commands:")
    print("  python3 tools/daily-revenue-action.py  # Today's highest ROI action")
    print("  python3 tools/revenue-tracker.py summary")
    print("  python3 tools/moltbook-suite.py queue next")

if __name__ == "__main__":
    main()
