#!/usr/bin/env python3
"""
Execution Gap Tracker — Monitor the gap between POTENTIAL and KINETIC revenue

POTENTIAL = Ready to send (proposals written, grants prepared)
KINETIC = Sent (in motion, conversion possible)

The execution gap is the difference between what COULD happen vs what IS happening.

Usage:
    python3 execution-gap-tracker.py                    # Current gap
    python3 execution-gap-tracker.py --history          # Gap over time
    python3 execution-gap-tracker.py --log              # Log current state
    python3 execution-gap-tracker.py --opportunity-cost # Calculate $/min lost
"""

import json
import re
from datetime import datetime, timedelta
import argparse

REVENUE_TRACKER = "/home/node/.openclaw/workspace/tools/revenue-tracker.py"
GAP_LOG = "/home/node/.openclaw/workspace/data/execution-gap-log.json"
DIARY = "/home/node/.openclaw/workspace/diary.md"

def parse_pipeline():
    """Run revenue-tracker.py and parse output"""
    import subprocess
    
    result = subprocess.run(
        ["python3", REVENUE_TRACKER, "summary"],
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    
    # Parse the summary output
    # Pattern: "Total items: N", "Potential: $X", "Ready to submit: $Y", "Submitted: $Z"
    
    pipeline = {}
    
    # Extract grants
    grants_match = re.search(r'GRANTS:.*?Total items: (\d+).*?Potential: \$([\d,]+).*?Ready to submit: \$([\d,]+).*?Submitted: \$([\d,]+)', output, re.DOTALL)
    if grants_match:
        pipeline['grants'] = {
            'items': int(grants_match.group(1)),
            'potential': int(grants_match.group(2).replace(',', '')),
            'ready': int(grants_match.group(3).replace(',', '')),
            'submitted': int(grants_match.group(4).replace(',', ''))
        }
    
    # Extract services
    services_match = re.search(r'SERVICES:.*?Total items: (\d+).*?Potential: \$([\d,]+).*?Ready to submit: \$([\d,]+).*?Submitted: \$([\d,]+)', output, re.DOTALL)
    if services_match:
        pipeline['services'] = {
            'items': int(services_match.group(1)),
            'potential': int(services_match.group(2).replace(',', '')),
            'ready': int(services_match.group(3).replace(',', '')),
            'submitted': int(services_match.group(4).replace(',', ''))
        }
    
    # Extract bounties
    bounties_match = re.search(r'BOUNTIES:.*?Total items: (\d+).*?Potential: \$([\d,]+).*?Ready to submit: \$([\d,]+).*?Submitted: \$([\d,]+)', output, re.DOTALL)
    if bounties_match:
        pipeline['bounties'] = {
            'items': int(bounties_match.group(1)),
            'potential': int(bounties_match.group(2).replace(',', '')),
            'ready': int(bounties_match.group(3).replace(',', '')),
            'submitted': int(bounties_match.group(4).replace(',', ''))
        }
    
    # Extract totals
    total_match = re.search(r'TOTAL PIPELINE: \$([\d,]+)', output)
    if total_match:
        pipeline['total'] = int(total_match.group(1).replace(',', ''))
    
    return pipeline

def calculate_gap(pipeline):
    """Calculate execution gap"""
    total_ready = 0
    total_submitted = 0
    
    for category in ['grants', 'services', 'bounties']:
        if category in pipeline:
            total_ready += pipeline[category]['ready']
            total_submitted += pipeline[category]['submitted']
    
    total_potential = total_ready + total_submitted
    
    if total_potential == 0:
        gap_pct = 0
    else:
        gap_pct = ((total_potential - total_submitted) / total_potential) * 100
    
    return {
        'ready': total_ready,
        'submitted': total_submitted,
        'potential': total_potential,
        'gap': total_potential - total_submitted,
        'gap_pct': gap_pct
    }

def calculate_opportunity_cost(gap, hours_waiting=24):
    """Calculate opportunity cost of waiting"""
    # Assume 5% conversion rate if sent
    # Cost = Gap × 5% × (hours / 24)
    
    conversion_rate = 0.05
    daily_opportunity = gap * conversion_rate
    hourly_opportunity = daily_opportunity / 24
    per_minute_opportunity = hourly_opportunity / 60
    
    return {
        'assumed_conversion': conversion_rate,
        'daily_lost': daily_opportunity,
        'hourly_lost': hourly_opportunity,
        'per_minute_lost': per_minute_opportunity,
        'hours_analyzed': hours_waiting
    }

def log_gap(gap_data):
    """Log current gap state to JSON file"""
    import os
    
    # Create data directory if needed
    os.makedirs("/home/node/.openclaw/workspace/data", exist_ok=True)
    
    # Load existing log
    log = []
    try:
        with open(GAP_LOG, 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        pass
    
    # Add new entry
    log.append({
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'gap': gap_data
    })
    
    # Save
    with open(GAP_LOG, 'w') as f:
        json.dump(log, f, indent=2)
    
    return len(log)

def load_history():
    """Load gap history from log"""
    try:
        with open(GAP_LOG, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_history(history):
    """Display gap history"""
    if not history:
        print("No gap history found. Run with --log to start tracking.")
        return
    
    print(f"📊 EXECUTION GAP HISTORY")
    print(f"=" * 60)
    print(f"{'Timestamp':<20} {'Ready':<10} {'Submitted':<10} {'Gap':<10} {'Gap %':<8}")
    print("-" * 60)
    
    for entry in history[-20:]:  # Last 20 entries
        timestamp = entry['timestamp'][:16]  # Truncate to minutes
        gap = entry['gap']
        
        print(f"{timestamp:<20} ${gap['ready']:>8,.0f} ${gap['submitted']:>8,.0f} ${gap['gap']:>8,.0f} {gap['gap_pct']:>6.1f}%")
    
    # Calculate trend
    if len(history) >= 2:
        first = history[0]['gap']
        last = history[-1]['gap']
        
        gap_change = last['gap'] - first['gap']
        pct_change = last['gap_pct'] - first['gap_pct']
        
        print()
        print(f"Trend (first → last):")
        print(f"  Gap change: ${gap_change:,.0f}")
        print(f"  Gap % change: {pct_change:+.1f}%")

def main():
    parser = argparse.ArgumentParser(description='Execution Gap Tracker')
    parser.add_argument('--history', action='store_true', help='Show gap history')
    parser.add_argument('--log', action='store_true', help='Log current gap state')
    parser.add_argument('--opportunity-cost', type=float, default=24, help='Calculate opportunity cost over N hours')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if args.history:
        history = load_history()
        show_history(history)
        return
    
    # Parse pipeline
    pipeline = parse_pipeline()
    gap = calculate_gap(pipeline)
    
    # Calculate opportunity cost
    opportunity = calculate_opportunity_cost(gap['gap'], args.opportunity_cost)
    
    # Output
    if args.json:
        output = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'pipeline': pipeline,
            'gap': gap,
            'opportunity_cost': opportunity
        }
        print(json.dumps(output, indent=2))
        return
    
    # Summary
    print(f"💰 EXECUTION GAP TRACKER")
    print(f"=" * 60)
    print(f"READY (POTENTIAL): ${gap['ready']:,.0f}")
    print(f"SUBMITTED (KINETIC): ${gap['submitted']:,.0f}")
    print(f"GAP: ${gap['gap']:,.0f} ({gap['gap_pct']:.1f}%)")
    print()
    
    # Opportunity cost
    print(f"💸 OPPORTUNITY COST (at {opportunity['assumed_conversion']*100:.0f}% conversion)")
    print(f"=" * 60)
    print(f"Per minute: ${opportunity['per_minute_lost']:,.2f}")
    print(f"Per hour: ${opportunity['hourly_lost']:,.2f}")
    print(f"Per day: ${opportunity['daily_lost']:,.2f}")
    print()
    
    # Insight
    if gap['gap_pct'] > 90:
        print(f"⚠️  CRITICAL: {gap['gap_pct']:.1f}% of potential revenue is unsent")
        print(f"   Every minute waited = ${opportunity['per_minute_lost']:,.2f} NOT pursued")
    elif gap['gap_pct'] > 50:
        print(f"⚠️  WARNING: {gap['gap_pct']:.1f}% gap — significant revenue left on table")
    else:
        print(f"✅ Gap manageable ({gap['gap_pct']:.1f}%)")
    
    print()
    
    # Log if requested
    if args.log:
        log_count = log_gap(gap)
        print(f"📝 Logged to {GAP_LOG} (entry #{log_count})")

if __name__ == "__main__":
    main()
