#!/usr/bin/env python3
"""
Execution Gap Dashboard — Simple view of revenue gap.

Shows the difference between POTENTIAL (ready) and KINETIC (submitted) revenue.
Makes the invisible visible: "You have $X ready but haven't sent anything."

Usage:
    python3 execution-gap-dashboard.py           # Show gap
    python3 execution-gap-dashboard.py --breakdown  # By category
    python3 execution-gap-dashboard.py --ready    # Show ready items only

Created: 2026-02-07 (Work block 3276)
"""

import json
from pathlib import Path

# Configuration
PIPELINE_FILE = "/home/node/.openclaw/workspace/revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline."""
    try:
        with open(PIPELINE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        return None

def calculate_gap(pipeline):
    """Calculate execution gap."""
    total = 0
    ready = 0
    submitted = 0
    won = 0
    
    categories = ['grants', 'services', 'bounties']
    breakdown = {}
    
    for category in categories:
        if category not in pipeline:
            continue
        
        items = pipeline[category]
        cat_total = 0
        cat_ready = 0
        cat_submitted = 0
        cat_won = 0
        
        for item in items:
            # Get value (handle both 'amount' and 'potential')
            value = item.get('amount', item.get('potential', 0))
            status = item.get('status', 'unknown')
            
            cat_total += value
            total += value
            
            if status == 'ready':
                cat_ready += value
                ready += value
            elif status == 'submitted':
                cat_submitted += value
                submitted += value
            elif status == 'won':
                cat_won += value
                won += value
        
        breakdown[category] = {
            'total': cat_total,
            'ready': cat_ready,
            'submitted': cat_submitted,
            'won': cat_won,
            'gap': cat_ready - cat_submitted - cat_won
        }
    
    gap = ready - submitted - won
    gap_pct = (gap / ready * 100) if ready > 0 else 0
    
    return {
        'total': total,
        'ready': ready,
        'submitted': submitted,
        'won': won,
        'gap': gap,
        'gap_pct': gap_pct,
        'breakdown': breakdown
    }

def print_dashboard(stats, show_breakdown=False, show_ready=False):
    """Print execution gap dashboard."""
    print(f"\n{'='*60}")
    print(f"  💰 EXECUTION GAP DASHBOARD")
    print(f"{'='*60}")
    
    # Main metrics
    print(f"\n  📊 PIPELINE STATUS")
    print(f"    Total Pipeline: ${stats['total']:,.0f}")
    print(f"    Ready to Send: ${stats['ready']:,.0f}")
    print(f"    Submitted:     ${stats['submitted']:,.0f}")
    print(f"    Won:           ${stats['won']:,.0f}")
    
    # Gap highlight
    gap_size = stats['gap']
    gap_pct = stats['gap_pct']
    
    print(f"\n  ⚠️  EXECUTION GAP")
    print(f"    Gap Amount: ${gap_size:,.0f}")
    print(f"    Gap Percentage: {gap_pct:.1f}%")
    
    if gap_pct > 90:
        print(f"    Status: 🔴 CRITICAL — 90%+ of revenue sitting idle")
    elif gap_pct > 70:
        print(f"    Status: 🟠 HIGH — 70%+ gap, need to send")
    elif gap_pct > 50:
        print(f"    Status: 🟡 MEDIUM — Half of pipeline stuck")
    else:
        print(f"    Status: 🟢 GOOD — Executing consistently")
    
    # Time to close gap
    if gap_size > 0:
        # Assuming ~20 min to send $50K (from existing tools data)
        minutes_needed = (gap_size / 50000) * 20
        roi_per_min = gap_size / minutes_needed if minutes_needed > 0 else 0
        
        print(f"\n  ⏱️  TIME TO CLOSE GAP")
        print(f"    Estimated time: {int(minutes_needed)} minutes")
        print(f"    ROI per minute: ${roi_per_min:,.0f}/min")
        print(f"    Opportunity cost: ${int(minutes_needed * roi_per_min / 60):,}/hour")
    
    # Breakdown by category
    if show_breakdown:
        print(f"\n  📋 BREAKDOWN BY CATEGORY")
        for category, data in stats['breakdown'].items():
            print(f"\n    {category.upper()}")
            print(f"      Total:     ${data['total']:,.0f}")
            print(f"      Ready:     ${data['ready']:,.0f}")
            print(f"      Submitted: ${data['submitted']:,.0f}")
            print(f"      Won:       ${data['won']:,.0f}")
            print(f"      Gap:       ${data['gap']:,.0f}")
    
    # Ready items list
    if show_ready:
        print(f"\n  📝 READY TO SEND (Detailed)")
        pipeline = load_pipeline()
        if pipeline:
            for category in ['grants', 'services', 'bounties']:
                if category in pipeline:
                    for item in pipeline[category]:
                        if item.get('status') == 'ready':
                            value = item.get('amount', item.get('potential', 0))
                            name = item.get('name', 'Unknown')
                            priority = item.get('priority', 'N/A')
                            print(f"    • [{category.upper()}] {name} — ${value:,.0f} (Priority: {priority})")
    
    # Action items
    print(f"\n  💡 NEXT ACTIONS")
    if gap_size > 100000:
        print(f"    1. 🔥 URGENT: You have ${gap_size:,.0f} sitting idle")
        print(f"    2. Unblock: Gateway restart (1 min) → $50K bounties")
        print(f"    3. Unblock: GitHub auth (5 min) → $125K grants")
        print(f"    4. Execute: Send service messages (20 min) → $200K+")
    elif gap_size > 50000:
        print(f"    1. ⚠️ High gap: ${gap_size:,.0f} ready but not sent")
        print(f"    2. Run: python3 tools/lead-prioritizer.py --top 5")
        print(f"    3. Start sending HIGH priority items first")
    else:
        print(f"    1. ✅ Good execution — gap is manageable")
        print(f"    2. Continue sending ready items")
        print(f"    3. Add more leads to pipeline")
    
    print(f"\n{'='*60}\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Execution gap dashboard')
    parser.add_argument('--breakdown', action='store_true',
                        help='Show breakdown by category')
    parser.add_argument('--ready', action='store_true',
                        help='Show list of ready items')
    args = parser.parse_args()
    
    pipeline = load_pipeline()
    if not pipeline:
        return
    
    stats = calculate_gap(pipeline)
    print_dashboard(stats, show_breakdown=args.breakdown, show_ready=args.ready)

if __name__ == '__main__':
    main()
