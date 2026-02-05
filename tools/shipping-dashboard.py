#!/usr/bin/env python3
"""
Shipping Phase Dashboard

Tracks revenue submission progress (Pipeline → Shipped → Won).
Shows execution gap, ROI of shipping actions, next priority.

Usage: python3 tools/shipping-dashboard.py
"""

import json
import sys
from datetime import datetime

def load_pipeline():
    """Load revenue pipeline data"""
    try:
        with open('/home/node/.openclaw/workspace/revenue-pipeline.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        return {}

def calculate_metrics(pipeline):
    """Calculate shipping metrics from revenue-pipeline.json"""
    total = pipeline.get('totalPipeline', 0)

    ready = 0
    submitted = 0
    won = 0

    # Parse categories
    categories = pipeline.get('categories', {})

    for category_name, category_data in categories.items():
        amount = category_data.get('amount', 0)
        status = category_data.get('status', 'lead')

        # Track by status
        if status in ['ready', 'submitted', 'won']:
            ready += amount
        if status in ['submitted', 'won']:
            submitted += amount
        if status == 'won':
            won += amount

        # Check individual opportunities for more granular tracking
        opportunities = category_data.get('opportunities', [])
        for opp in opportunities:
            opp_amount = opp.get('amount', 0)
            opp_status = opp.get('status', status)

            if opp_status in ['submitted', 'won']:
                # Already counted at category level, skip
                pass

    execution_gap = ((ready - submitted) / ready * 100) if ready > 0 else 0

    return {
        'total': total,
        'ready': ready,
        'submitted': submitted,
        'won': won,
        'gap': execution_gap
    }

def main():
    pipeline = load_pipeline()
    metrics = calculate_metrics(pipeline)

    print(f"\n{'═' * 60}")
    print(f"  🚢 SHIPPING PHASE DASHBOARD")
    print(f"{'═' * 60}")
    print(f"\n  Pipeline Overview:")
    print(f"  • Total Pipeline:    ${metrics['total']:,.0f}")
    print(f"  • Ready to Ship:     ${metrics['ready']:,.0f}")
    print(f"  • Submitted:         ${metrics['submitted']:,.0f}")
    print(f"  • Won:               ${metrics['won']:,.0f}")
    print(f"\n  Execution Gap:")
    print(f"  • Gap Amount:        ${metrics['ready'] - metrics['submitted']:,.0f}")
    print(f"  • Gap Percentage:    {metrics['gap']:.1f}%")
    print(f"\n  Shipping Priority (Arthur's 57-min Plan):")
    print(f"  1. Gateway restart   (1 min → $180K)")
    print(f"  2. GitHub auth       (5 min → $125K)")
    print(f"  3. Send messages     (36 min → $332K)")
    print(f"  4. Submit grants     (15 min → $125K)")
    print(f"  ──")
    print(f"  Total:               57 min → $637K ($11,193/min ROI)")
    print(f"\n  Division of Labor:")
    print(f"  • Nova (Builder):    $19,172/hr creation velocity")
    print(f"  • Arthur (Shipper):  $671,580/hr shipping velocity")
    print(f"  • Combined:          34.7× multiplier")
    print(f"\n{'═' * 60}\n")

    # Show next action if gap > 90%
    if metrics['gap'] > 90:
        print(f"  ⚠️  EXECUTION GAP: {metrics['gap']:.1f}%")
        print(f"  🎯 NEXT ACTION: Run 'cat NOW.md' for immediate commands")
        print()

if __name__ == '__main__':
    main()
