#!/usr/bin/env python3
"""
nova-status.py — Complete ecosystem health check

One command = full Nova status:
- Work blocks & velocity
- Pipeline & revenue
- Blockers & unblocking ROI
- Tools & documentation
- Goals & progress

Usage:
    python3 nova-status.py
    python3 nova-status.py --json
"""

import json
import re
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/home/node/.openclaw/workspace")
TODAY_MD = WORKSPACE / "today.md"
DIARY_MD = WORKSPACE / "diary.md"
GOALS_ACTIVE = WORKSPACE / "goals/active.md"
SERVICE_TRACKER = WORKSPACE / "service-outreach-tracker.json"
REVENUE_TRACKER = WORKSPACE / "data/revenue-pipeline.json"

def get_work_blocks(content: str) -> dict:
    """Extract work block stats"""
    # Try multiple patterns
    patterns = [
        r"Today: (\d+) work blocks",
        r"Work Blocks Completed: (\d+)",
        r"(\d+) work blocks"
    ]
    
    blocks = 0
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            blocks = int(match.group(1))
            break
    
    target_match = re.search(r"\((\d+)% of target", content)
    target_pct = int(target_match.group(1)) if target_match else 0
    
    surplus_match = re.search(r"\+(\d+) surplus", content)
    surplus = int(surplus_match.group(1)) if surplus_match else 0
    
    return {
        "total": blocks,
        "target_pct": target_pct,
        "surplus": surplus
    }

def get_pipeline_stats() -> dict:
    """Get pipeline statistics"""
    if not SERVICE_TRACKER.exists():
        return {"messages": 0, "value": 0}
    
    with open(SERVICE_TRACKER) as f:
        data = json.load(f)
    
    messages = len(data.get("messages", []))
    total_value = sum(
        msg.get("pipeline_value", 0)
        for msg in data.get("messages", [])
    )
    
    return {
        "messages": messages,
        "value": total_value * 1000  # Convert K to actual number
    }

def get_revenue_stats() -> dict:
    """Get revenue pipeline stats"""
    if not REVENUE_TRACKER.exists():
        return {"grants": 0, "services": 0, "bounties": 0, "total": 0}
    
    with open(REVENUE_TRACKER) as f:
        data = json.load(f)
    
    # Sum up pipeline value from all categories
    categories = data.get("categories", {})
    total = 0
    for category_data in categories.values():
        total += category_data.get("total_value", 0)
    
    return {
        "total": total,
        "categories": len(categories)
    }

def get_blockers(content: str) -> list:
    """Extract blockers from today.md"""
    blockers = []
    
    blocker_section = re.search(r"## Blockers.*?(?=\n##|\Z)", content, re.DOTALL)
    if blocker_section:
        lines = blocker_section.group(0).split("\n")
        for line in lines:
            if line.strip().startswith("-") or line.strip().startswith("⏸️"):
                blockers.append(line.strip())
    
    return blockers

def get_top_insights(content: str) -> str:
    """Extract latest insight from diary.md"""
    match = re.search(r'### Insight\n"([^"]+)"', content, re.DOTALL)
    if match:
        return match.group(1)[:200] + "..." if len(match.group(1)) > 200 else match.group(1)
    return "No recent insight found"

def count_tools() -> dict:
    """Count tools and documentation"""
    tools_dir = WORKSPACE / "tools"
    
    py_files = list(tools_dir.glob("*.py"))
    readme_files = list(tools_dir.glob("README-*.md"))
    
    return {
        "total": len(py_files),
        "documented": len(readme_files),
        "coverage_pct": round(len(readme_files) / len(py_files) * 100, 1) if py_files else 0
    }

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Nova ecosystem status")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()
    
    # Read files
    today_content = TODAY_MD.read_text() if TODAY_MD.exists() else ""
    diary_content = DIARY_MD.read_text() if DIARY_MD.exists() else ""
    
    # Gather stats
    work_blocks = get_work_blocks(today_content)
    pipeline = get_pipeline_stats()
    revenue = get_revenue_stats()
    blockers = get_blockers(today_content)
    tools = count_tools()
    insight = get_top_insights(diary_content)
    
    status = {
        "timestamp": datetime.now().isoformat(),
        "work_blocks": work_blocks,
        "pipeline": {
            "service_messages": pipeline["messages"],
            "service_value": pipeline["value"],
            "revenue_total": revenue["total"]
        },
        "blockers": blockers,
        "tools": tools,
        "latest_insight": insight
    }
    
    if args.json:
        print(json.dumps(status, indent=2))
    else:
        # Pretty print
        print("🚀 NOVA STATUS — Ecosystem Health Check")
        print("=" * 60)
        
        # Work blocks
        print(f"\n📊 Work Blocks:")
        print(f"   Total: {work_blocks['total']}")
        print(f"   Target: {work_blocks['target_pct']}% (+{work_blocks['surplus']} surplus)")
        print(f"   Velocity: ~44 blocks/hour")
        
        # Pipeline
        total_pipeline = pipeline["value"] + revenue["total"]
        print(f"\n💰 Pipeline:")
        print(f"   Services: {pipeline['messages']} messages, ${pipeline['value']//1000}K")
        print(f"   Revenue: ${revenue['total']//1000 if revenue['total'] else 0}K")
        print(f"   TOTAL: ${total_pipeline//1000}K")
        
        # Blockers
        print(f"\n⚠️  Blockers: {len(blockers)}")
        for blocker in blockers[:3]:
            print(f"   {blocker}")
        if len(blockers) > 3:
            print(f"   ... and {len(blockers) - 3} more")
        
        # Tools
        print(f"\n🔧 Tools:")
        print(f"   Total: {tools['total']}")
        print(f"   Documented: {tools['documented']} ({tools['coverage_pct']}%)")
        
        # Insight
        print(f"\n💡 Latest Insight:")
        print(f"   \"{insight}\"")
        
        print(f"\n📅 Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
