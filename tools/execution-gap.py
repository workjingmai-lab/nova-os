#!/usr/bin/env python3
"""
Execution Gap Calculator

Measures the gap between POTENTIAL pipeline (what's ready) 
and KINETIC pipeline (what's submitted).

Based on revenue-pipeline.json structure.
"""

import json
import os
from datetime import datetime

PIPELINE_FILE = "/home/node/.openclaw/workspace/revenue-pipeline.json"

def load_pipeline():
    """Load pipeline data from JSON file."""
    try:
        with open(PIPELINE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"categories": {}}

def extract_opportunities(category_data, category_name):
    """Extract opportunities from category data."""
    opportunities = []
    
    if category_name == "grants":
        for opp in category_data.get("opportunities", []):
            opportunities.append({
                "name": opp.get("name", "Unknown"),
                "amount": opp.get("amount", 0),
                "status": "ready"  # Grants are marked as ready
            })
    
    elif category_name == "services":
        # Top prospects
        for opp in category_data.get("topProspects", []):
            opportunities.append({
                "name": opp.get("name", "Unknown"),
                "amount": opp.get("amount", 0),
                "status": "ready"  # Messages ready
            })
    
    elif category_name == "bounties":
        for opp in category_data.get("platforms", []):
            opportunities.append({
                "name": opp.get("name", "Unknown"),
                "amount": opp.get("amount", 0),
                "status": opp.get("status", "lead")
            })
    
    return opportunities

def calculate_gap(pipeline):
    """Calculate execution gap metrics."""
    categories = pipeline.get("categories", {})
    
    stats = {
        "grants": {"potential": 0, "ready": 0, "submitted": 0, "won": 0, "count": 0},
        "services": {"potential": 0, "ready": 0, "submitted": 0, "won": 0, "count": 0},
        "bounties": {"potential": 0, "ready": 0, "submitted": 0, "won": 0, "count": 0}
    }
    
    for category_name, category_data in categories.items():
        if category_name not in stats:
            continue
            
        opportunities = extract_opportunities(category_data, category_name)
        
        for opp in opportunities:
            amount = opp.get("amount", 0)
            status = opp.get("status", "lead")
            
            stats[category_name]["potential"] += amount
            stats[category_name]["count"] += 1
            
            if status in ["ready", "submitted", "won", "lost"]:
                stats[category_name]["ready"] += amount
            if status in ["submitted", "won", "lost"]:
                stats[category_name]["submitted"] += amount
            if status == "won":
                stats[category_name]["won"] += amount
    
    return stats

def print_gap_report(stats):
    """Print execution gap report."""
    total_potential = sum(s["potential"] for s in stats.values())
    total_ready = sum(s["ready"] for s in stats.values())
    total_submitted = sum(s["submitted"] for s in stats.values())
    total_won = sum(s["won"] for s in stats.values())
    
    gap_ready_to_submitted = total_ready - total_submitted
    gap_submitted_to_won = total_submitted - total_won
    
    print("⚡ EXECUTION GAP REPORT")
    print("=" * 60)
    print()
    
    # Pipeline Summary
    print(f"📊 PIPELINE SUMMARY")
    print(f"  Total Potential: ${total_potential:,.0f}")
    if total_potential > 0:
        print(f"  Ready to Send:  ${total_ready:,.0f} ({total_ready/total_potential*100:.1f}%)")
        print(f"  Submitted:      ${total_submitted:,.0f} ({total_submitted/total_potential*100:.1f}%)")
        print(f"  Won:            ${total_won:,.0f} ({total_won/total_potential*100:.1f}%)")
    else:
        print(f"  Ready to Send:  ${total_ready:,.0f}")
        print(f"  Submitted:      ${total_submitted:,.0f}")
        print(f"  Won:            ${total_won:,.0f}")
    print()
    
    # Execution Gap
    print(f"🚨 EXECUTION GAP")
    print(f"  Ready → Submitted: ${gap_ready_to_submitted:,.0f} (not sent)")
    print(f"  Submitted → Won:   ${gap_submitted_to_won:,.0f} (pending)")
    print()
    
    # Breakdown by Category
    print(f"📁 BREAKDOWN BY CATEGORY")
    has_data = False
    for category, stat in stats.items():
        if stat["potential"] > 0:
            has_data = True
            potential = stat['potential']
            print(f"\n  {category.upper()}")
            print(f"    Potential: ${potential:,.0f} ({stat['count']} items)")
            print(f"    Ready:     ${stat['ready']:,.0f} ({stat['ready']/potential*100:.1f}%)")
            print(f"    Submitted: ${stat['submitted']:,.0f} ({stat['submitted']/potential*100:.1f}%)")
            print(f"    Won:       ${stat['won']:,.0f} ({stat['won']/potential*100:.1f}%)")
            
            gap = stat['ready'] - stat['submitted']
            if gap > 0:
                print(f"    ⚠️  Gap: ${gap:,.0f} ready but not submitted")
    
    if not has_data:
        print("  No pipeline data found.")
    
    print()
    
    # Insight
    print(f"💡 KEY INSIGHT")
    if gap_ready_to_submitted > 0:
        print(f"  ${gap_ready_to_submitted:,.0f} is ready to send RIGHT NOW with zero blockers.")
        print(f"  The gap is not preparation — it's EXECUTION.")
    elif total_submitted > 0:
        print(f"  Pipeline is executing. Focus on follow-ups and conversion.")
    else:
        print(f"  Build pipeline first, then execute.")
    print()

if __name__ == "__main__":
    pipeline = load_pipeline()
    stats = calculate_gap(pipeline)
    print_gap_report(stats)
