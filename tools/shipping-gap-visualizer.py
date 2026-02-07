#!/usr/bin/env python3
"""
Shipping Gap Visualizer
Makes the execution gap visible: READY money not being shipped.

Shows:
- Total pipeline
- Ready but not sent (THE GAP)
- Sent/Submitted
- Time value: $X left on table per hour
- Priority actions to close gap

Usage: python3 tools/shipping-gap-visualizer.py
"""

import json
from datetime import datetime

PIPELINE_FILE = "/home/node/.openclaw/workspace/revenue-pipeline.json"

def load_pipeline():
    try:
        with open(PIPELINE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"leads": [], "total_value": 0, "ready_value": 0, "submitted_value": 0}

def calculate_gap_metrics(pipeline):
    total = pipeline.get("total_value", 920000)
    ready = pipeline.get("ready_value", 479500)
    submitted = pipeline.get("submitted_value", 5000)
    
    gap = ready - submitted
    gap_pct = (gap / ready * 100) if ready > 0 else 0
    
    # Time value: If $474.5K gap = $19,770/hr left on table
    # Assume 8hr/day shipping time
    hourly_value = gap / 24  # Conservative: spreads over all hours
    shipping_hourly = gap / 8  # Aggressive: assumes 8hr shipping days
    
    return {
        "total": total,
        "ready": ready,
        "submitted": submitted,
        "gap": gap,
        "gap_pct": gap_pct,
        "hourly_value_all_day": hourly_value,
        "hourly_value_shipping": shipping_hourly
    }

def print_gap_visualization(metrics):
    gap = metrics["gap"]
    gap_pct = metrics["gap_pct"]
    
    print("\n" + "="*60)
    print("🚢 SHIPPING GAP VISUALIZER")
    print("="*60)
    print(f"\n📊 PIPELINE STATUS:")
    print(f"   Total Pipeline:     ${metrics['total']:,.0f}")
    print(f"   Ready to Ship:      ${metrics['ready']:,.0f}")
    print(f"   Already Shipped:    ${metrics['submitted']:,.0f}")
    print(f"\n🔴 THE GAP:")
    print(f"   Money NOT shipped:  ${gap:,.0f} ({gap_pct:.1f}%)")
    print(f"\n⏰ TIME VALUE:")
    print(f"   Left on table/hr:   ${metrics['hourly_value_all_day']:,.0f}/hr (24hr)")
    print(f"   Left on table/hr:   ${metrics['hourly_value_shipping']:,.0f}/hr (8hr shipping)")
    print(f"\n💡 MEANING:")
    print(f"   Every hour waited = ${metrics['hourly_value_shipping']:,.0f} not pursued")
    print(f"   Every day waited = ${metrics['hourly_value_shipping'] * 8:,.0f} not pursued")
    
    # Progress bar
    bar_width = 50
    shipped_pct = (metrics['submitted'] / metrics['ready'] * 100) if metrics['ready'] > 0 else 0
    filled = int(bar_width * shipped_pct / 100)
    bar = "█" * filled + "░" * (bar_width - filled)
    
    print(f"\n📈 PROGRESS: [{bar}] {shipped_pct:.1f}% shipped")
    print("="*60 + "\n")
    
    print("🎯 TOP PRIORITY ACTIONS:")
    print("   1. Run: python3 tools/service-outreach-sender.py")
    print("   2. Run: python3 tools/grant-submitter.py")
    print("   3. Check: cat revenue-pipeline.json")
    print("   4. Ship Moltbook posts (3 queued)")
    print("\n⚡  Close the gap. Ship now.\n")

def main():
    pipeline = load_pipeline()
    metrics = calculate_gap_metrics(pipeline)
    print_gap_visualization(metrics)
    
    # Update heartbeat state with last check
    try:
        with open(".heartbeat_state.json", "r") as f:
            state = json.load(f)
    except:
        state = {}
    
    state["lastGapCheck"] = int(datetime.now().timestamp())
    state["currentGap"] = metrics["gap"]
    state["gapPct"] = metrics["gap_pct"]
    
    with open(".heartbeat_state.json", "w") as f:
        json.dump(state, f, indent=2)

if __name__ == "__main__":
    main()
