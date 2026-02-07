#!/usr/bin/env python3
"""
blocker-dashboard.py - One-command blocker status with ROI

Usage:
    python3 tools/blocker-dashboard.py          # Show all blockers
    python3 tools/blocker-dashboard.py ready    # Show unblocked actions
"""

import json
from pathlib import Path

def load_blockers():
    """Load blocker data from various sources."""
    blockers = []
    
    # Primary blockers from revenue pipeline
    pipeline_path = Path("data/revenue-pipeline.json")
    if pipeline_path.exists():
        with open(pipeline_path) as f:
            data = json.load(f)
        
        # Check grants for blockers
        grants = data.get("grants", [])
        if isinstance(grants, list):
            for g in grants:
                if g.get("status") == "blocked" and g.get("blocker"):
                    blockers.append({
                        "name": g.get("name", "Unknown Grant"),
                        "type": "grant",
                        "value": g.get("potential", 0),
                        "blocker": g.get("blocker", ""),
                        "action": g.get("unblock_action", ""),
                        "owner": g.get("owner", "unknown")
                    })
        
        # Check services for blockers
        services = data.get("services", [])
        if isinstance(services, list):
            for s in services:
                if s.get("status") == "blocked" and s.get("blocker"):
                    blockers.append({
                        "name": s.get("name", "Unknown Service"),
                        "type": "service",
                        "value": s.get("potential", 0),
                        "blocker": s.get("blocker", ""),
                        "action": s.get("unblock_action", ""),
                        "owner": s.get("owner", "unknown")
                    })
    
    return blockers

def get_manual_blockers():
    """Get manually tracked blockers (from goals/active.md)."""
    return [
        {
            "name": "Code4rena Bounties",
            "type": "bounty",
            "value": 50000,
            "blocker": "Browser automation blocked",
            "action": "Gateway restart required",
            "owner": "Arthur",
            "time_min": 1,
            "roi_per_min": 50000
        },
        {
            "name": "Grant Submissions",
            "type": "grant",
            "value": 125000,
            "blocker": "GitHub repo push needed",
            "action": "gh auth login + git push",
            "owner": "Arthur", 
            "time_min": 5,
            "roi_per_min": 25000
        }
    ]

def format_currency(value):
    if value >= 1000000:
        return f"${value/1000000:.1f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value}"

def show_blockers():
    """Display blocker dashboard."""
    print("=" * 65)
    print("🔒 BLOCKER DASHBOARD")
    print("=" * 65)
    
    blockers = get_manual_blockers()
    
    if not blockers:
        print("\n✅ No blockers found — everything is ready!")
        return
    
    # Sort by ROI
    blockers.sort(key=lambda x: x.get("roi_per_min", 0), reverse=True)
    
    total_value = sum(b["value"] for b in blockers)
    total_time = sum(b.get("time_min", 5) for b in blockers)
    
    print(f"\n📊 SUMMARY")
    print("-" * 65)
    print(f"   Blockers: {len(blockers)}")
    print(f"   Total value blocked: {format_currency(total_value)}")
    print(f"   Time to unblock: {total_time} minutes")
    print(f"   Average ROI: {format_currency(total_value/total_time)}/min")
    
    print(f"\n🎯 BY PRIORITY (ROI/min)")
    print("-" * 65)
    
    for i, b in enumerate(blockers[:10], 1):
        roi = b.get("roi_per_min", b["value"] / b.get("time_min", 5))
        print(f"\n{i}. {b['name']}")
        print(f"   Value: {format_currency(b['value'])} | ROI: {format_currency(roi)}/min")
        print(f"   Blocker: {b['blocker']}")
        print(f"   Action: {b['action']}")
        print(f"   Owner: {b['owner']} | Time: {b.get('time_min', '?')} min")
    
    print(f"\n{'=' * 65}")
    print("⚡ EXECUTE TOP BLOCKER FIRST")
    print("=" * 65)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "ready":
        # Show unblocked actions
        print("Run: python3 tools/execution-gap-closer.py summary")
    else:
        show_blockers()
