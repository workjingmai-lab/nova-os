#!/usr/bin/env python3
"""
daily-revenue-dashboard.py — One-command revenue pipeline health check

Usage:
    python3 tools/daily-revenue-dashboard.py       # Full dashboard
    python3 tools/daily-revenue-dashboard.py --mini # Mini version (one line)
"""

import json
from pathlib import Path
from datetime import datetime

WORKSPACE = Path.home() / ".openclaw/workspace"
PIPELINE_FILE = WORKSPACE / "revenue-pipeline.json"
DIARY_FILE = WORKSPACE / "diary.md"

def load_pipeline():
    """Load revenue pipeline"""
    if not PIPELINE_FILE.exists():
        return None
    with open(PIPELINE_FILE) as f:
        return json.load(f)

def calculate_gap(pipeline):
    """Calculate execution gap percentage"""
    # Handle flat structure (grants/services/bounties are arrays at top level)
    grants = pipeline.get("grants", [])
    services = pipeline.get("services", [])
    bounties = pipeline.get("bounties", [])
    
    ready_grants = sum(g.get("amount", 0) for g in grants if g.get("status") == "ready")
    ready_services = sum(s.get("potential", 0) for s in services if s.get("status") == "ready")
    ready_bounties = sum(b.get("amount", 0) for b in bounties if b.get("status") == "ready")
    total_ready = ready_grants + ready_services + ready_bounties
    
    submitted_grants = sum(g.get("amount", 0) for g in grants if g.get("status") == "submitted")
    submitted_services = sum(s.get("potential", 0) for s in services if s.get("status") == "submitted")
    submitted_bounties = sum(b.get("amount", 0) for b in bounties if b.get("status") == "submitted")
    total_submitted = submitted_grants + submitted_services + submitted_bounties
    
    if total_ready == 0:
        return 0, total_ready, total_submitted
    
    gap_pct = ((total_ready - total_submitted) / total_ready * 100) if total_ready > 0 else 0
    return round(gap_pct, 1), total_ready, total_submitted

def get_latest_blocks():
    """Get work block count from diary.md"""
    if not DIARY_FILE.exists():
        return 0
    
    with open(DIARY_FILE) as f:
        content = f.read()
    
    # Find last work block number
    import re
    matches = re.findall(r'WORK BLOCK (\d+)', content)
    if matches:
        return int(matches[-1])
    return 0

def format_currency(amount):
    """Format as currency with K/M suffixes"""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount}"

def print_dashboard(mini=False):
    pipeline = load_pipeline()
    if not pipeline:
        print("❌ Pipeline data not found")
        return
    
    gap_pct, ready, submitted = calculate_gap(pipeline)
    # Handle both "totalPipeline" and "meta.totalPotential" structures
    meta = pipeline.get("meta", {})
    total = meta.get("totalPotential", 0) or pipeline.get("totalPipeline", 0)
    blocks = get_latest_blocks()
    
    if mini:
        # Mini dashboard: one line
        print(f"📊 {blocks} blocks | ${total:,} pipeline | {ready:,} ready | {submitted:,} sent | {gap_pct}% gap")
        return
    
    # Full dashboard
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")
    
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "DAILY REVENUE DASHBOARD" + " " * 22 + "║")
    print("╚" + "═" * 58 + "╝")
    print(f"📅 {now} | 🧱 {blocks} work blocks")
    print()
    
    # Pipeline summary
    print("💰 PIPELINE OVERVIEW")
    print("─" * 58)
    print(f"  Total Pipeline:     {format_currency(total)}")
    print(f"  Ready to Submit:    {format_currency(ready)}")
    print(f"  Submitted:          {format_currency(submitted)}")
    print(f"  Execution Gap:      {gap_pct}%")
    print()
    
    # Category breakdown (only if categories key exists)
    if "categories" not in pipeline:
        print("📊 CATEGORY BREAKDOWN")
        print("─" * 58)
        print("  (Flat structure — use revenue-tracker.py for details)")
        print()
    else:
        print("📊 CATEGORY BREAKDOWN")
        print("─" * 58)
        
        for cat_name, cat_data in pipeline["categories"].items():
            cat_amount = cat_data.get("amount", 0)
            cat_ready = cat_data.get("ready", 0)
            cat_submitted = cat_data.get("submitted", 0)
            cat_status = cat_data.get("status", "unknown")
            cat_blocker = cat_data.get("blocker", "NONE")
            
            print(f"\n  {cat_name.upper()} ({format_currency(cat_amount)})")
            print(f"    Status: {cat_status}")
            print(f"    Ready: {format_currency(cat_ready)} | Sent: {format_currency(cat_submitted)}")
            if cat_blocker != "NONE":
                print(f"    ⚠️  Blocker: {cat_blocker}")
    
    print()
    print("🎯 NEXT ACTIONS")
    print("─" * 58)
    
    if gap_pct > 50:
        print("  ⚠️  High execution gap! Run: bash tools/send-everything.sh full")
    
    if "categories" in pipeline:
        grants_blocker = pipeline["categories"]["grants"].get("blocker", "NONE")
        if grants_blocker != "NONE":
            print(f"  🔓 Unblock grants: {grants_blocker}")
    
    print("  📈 Track: python3 tools/revenue-tracker.py status")
    print("  📝 Diary: cat diary.md | tail -20")
    print()
    print("✨ Small executions compound. Keep building.")

def main():
    import sys
    mini = "--mini" in sys.argv or "-m" in sys.argv
    print_dashboard(mini=mini)

if __name__ == "__main__":
    main()
