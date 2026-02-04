#!/usr/bin/env python3
"""
Workspace Status Checker - Quick overview of workspace state
Gives you a snapshot of what's happening in 1 second.
"""

import json
import os
from pathlib import Path
from datetime import datetime

def count_blocks():
    """Count work blocks from diary.md - extract latest Work Block Count"""
    # Try workspace root first
    diary_path = Path("/home/node/.openclaw/workspace/diary.md")
    if not diary_path.exists():
        diary_path = Path("diary.md")
    if not diary_path.exists():
        return 0
    
    content = diary_path.read_text()
    # Find the latest "Work Block Count:" value - handles ** markdown formatting
    import re
    # Match: "**Work Block Count:** 1019" or "Work Block Count: 1019"
    matches = re.findall(r'\*?\*?Work Block Count:\*?\*?\s*(\d+)', content)
    if matches:
        return int(matches[-1])  # Return the latest count
    
    # Fallback: count Work Block # patterns
    count = content.count("Work Block #") + content.count("WORK BLOCK #")
    return count

def get_pipeline_value():
    """Get revenue pipeline value"""
    pipeline_path = Path("/home/node/.openclaw/workspace/revenue-pipeline.json")
    if not pipeline_path.exists():
        pipeline_path = Path("revenue-pipeline.json")
    if not pipeline_path.exists():
        return 0
    
    try:
        data = json.loads(pipeline_path.read_text())
        # Handle both totalPipeline and totalValue field names
        value = data.get("totalPipeline") or data.get("totalValue") or 0
        return value
    except:
        return 0

def count_tools():
    """Count total tools"""
    tools_dir = Path("/home/node/.openclaw/workspace/tools")
    if not tools_dir.exists():
        tools_dir = Path("tools")
    if not tools_dir.exists():
        return 0
    
    return len([f for f in tools_dir.glob("*.py") if not f.name.startswith("_")])

def count_readmes():
    """Count tool READMEs"""
    workspace = Path("/home/node/.openclaw/workspace")
    if not workspace.exists():
        workspace = Path(".")
    return len(list(workspace.glob("README-*.md")))

def count_knowledge():
    """Count knowledge articles"""
    knowledge_dir = Path("/home/node/.openclaw/workspace/knowledge")
    if not knowledge_dir.exists():
        knowledge_dir = Path("knowledge")
    if not knowledge_dir.exists():
        return 0
    
    return len([f for f in knowledge_dir.glob("*.md") if not f.name.startswith("_")])

def get_latest_diary_entry():
    """Get latest diary entry"""
    diary_path = Path("/home/node/.openclaw/workspace/diary.md")
    if not diary_path.exists():
        diary_path = Path("diary.md")
    if not diary_path.exists():
        return None
    
    content = diary_path.read_text()
    lines = content.split("\n")
    
    for line in lines:
        if "WORK BLOCK #" in line or "HEARTBEAT" in line:
            return line.strip()
    
    return None

def get_blockers():
    """Get revenue blockers from heartbeat state"""
    state_path = Path("/home/node/.openclaw/workspace/.heartbeat_state.json")
    if not state_path.exists():
        state_path = Path(".heartbeat_state.json")
    if not state_path.exists():
        return None
    
    try:
        data = json.loads(state_path.read_text())
        return data.get("blockers", {})
    except:
        return None

def main():
    """Print workspace status"""
    print("=" * 50)
    print("🧠 WORKSPACE STATUS")
    print("=" * 50)
    
    blocks = count_blocks()
    pipeline = get_pipeline_value()
    tools = count_tools()
    readmes = count_readmes()
    knowledge = count_knowledge()
    
    print(f"📊 Work Blocks: {blocks}")
    print(f"💰 Pipeline: ${pipeline:,.0f}")
    print(f"🔧 Tools: {tools}")
    print(f"📚 READMEs: {readmes}")
    print(f"🧠 Knowledge: {knowledge} articles")
    
    latest = get_latest_diary_entry()
    if latest:
        print(f"\n📝 Latest: {latest[:80]}...")
    
    # Revenue blockers
    blockers = get_blockers()
    if blockers:
        print("\n" + "=" * 50)
        print("🚧 REVENUE BLOCKERS:")
        print("=" * 50)
        for name, info in blockers.items():
            status_icon = "🔴" if info.get("status") == "blocked" else "✅"
            print(f"{status_icon} {name.upper()}: {info.get('status', 'unknown')}")
            print(f"   Fix: {info.get('fixTime', 'unknown')} | ROI: {info.get('roi', 'unknown')}")
            print(f"   Unlocks: {info.get('unlocks', 'unknown')}")
    
    # Quick status check
    print("\n" + "=" * 50)
    
    if pipeline > 100000:
        print("✅ Pipeline ready - EXECUTE MODE")
    elif blocks > 500:
        print("✅ Strong progress - keep building")
    else:
        print("🚀 Ramp up - more blocks needed")
    
    print("=" * 50)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
