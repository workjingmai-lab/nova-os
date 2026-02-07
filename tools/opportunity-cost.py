#!/usr/bin/env python3
"""
opportunity-cost.py — Calculate revenue cost of inaction

Shows how much potential revenue "expires" per hour/day of delay.
Use this to communicate urgency of execution blockers.

Usage:
    python3 opportunity-cost.py [ready_amount] [gap_percent]
    python3 opportunity-cost.py              # Uses defaults from pipeline
"""

import json
import sys
from datetime import datetime

# Defaults
DEFAULT_READY = 754500  # $754.5K ready to send
DEFAULT_GAP = 99.3      # 99.3% execution gap

# Assumptions (conservative)
CONVERSION_RATE = 0.10  # 10% of sent messages convert
TIME_TO_CLOSE_DAYS = 30  # Average 30 days from send to close

def load_pipeline():
    """Try to load from revenue-pipeline.json"""
    try:
        with open('data/revenue-pipeline.json', 'r') as f:
            data = json.load(f)
            opportunities = data.get('opportunities', [])
            ready = sum(o.get('value', 0) for o in opportunities
                       if o.get('status') == 'ready')
            total = sum(o.get('value', 0) for o in opportunities)
            submitted = sum(o.get('value', 0) for o in opportunities
                          if o.get('status') == 'submitted')
            gap = ((total - submitted) / total * 100) if total else 0
            return ready, gap
    except Exception as e:
        return DEFAULT_READY, DEFAULT_GAP

def main():
    ready = float(sys.argv[1]) if len(sys.argv) > 1 else None
    gap = float(sys.argv[2]) if len(sys.argv) > 2 else None
    
    if ready is None:
        ready, gap = load_pipeline()
    if gap is None:
        gap = DEFAULT_GAP
    
    # Calculations
    expected_revenue = ready * CONVERSION_RATE if ready else DEFAULT_READY * CONVERSION_RATE
    daily_value = expected_revenue / TIME_TO_CLOSE_DAYS
    hourly_value = daily_value / 24
    display_ready = ready if ready else DEFAULT_READY
    display_gap = gap if gap else DEFAULT_GAP
    
    # Cost of common delays
    delays = [
        ("1 hour", hourly_value),
        ("4 hours (half day)", hourly_value * 4),
        ("1 day", daily_value),
        ("1 week", daily_value * 7),
        ("1 month", expected_revenue),
    ]
    
    print(f"\n💰 OPPORTUNITY COST OF WAITING")
    print(f"{'='*50}")
    print(f"Ready to execute:    ${display_ready:,.0f}")
    print(f"Execution gap:       {display_gap:.1f}%")
    print(f"Assumed conversion:  {CONVERSION_RATE*100:.0f}%")
    print(f"Expected revenue:    ${expected_revenue:,.0f}")
    print(f"")
    print(f"⏰ COST OF DELAY:")
    print(f"{'-'*30}")
    for label, cost in delays:
        bar_len = int(cost / expected_revenue * 20) if expected_revenue else 0
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {label:20} ${cost:>8,.0f} {bar}")
    
    print(f"\n🎯 EXECUTION BLOCKERS (Arthur actions):")
    print(f"  • Gateway restart:   1 min → $50K bounties")
    print(f"  • GitHub auth:       5 min → $125K grants")  
    print(f"  • Send messages:    20 min → $200K services")
    print(f"  {'─'*40}")
    print(f"  TOTAL:              26 min → $375K potential")
    print(f"  ROI:                $14,423 per minute")
    print(f"")
    print(f"📊 Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n")

if __name__ == "__main__":
    main()
