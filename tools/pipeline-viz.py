#!/usr/bin/env python3
"""
pipeline-viz.py — Visual pipeline status dashboard

Quick visual snapshot of revenue pipeline:
- Stage breakdown (identified → ready → submitted → won)
- Conversion funnel visualization
- Blocker highlight
- Next actions

Usage: python3 tools/pipeline-viz.py
"""

import json
import sys
from datetime import datetime

# Pipeline data
PIPELINE = {
    "grants": {
        "identified": 150000,
        "ready": 130000,
        "submitted": 5000,
        "won": 0,
        "blocker": "GitHub auth (Arthur)"
    },
    "services": {
        "identified": 700000,
        "ready": 424500,
        "submitted": 0,
        "won": 0,
        "blocker": "Arthur to send messages"
    },
    "bounties": {
        "identified": 50000,
        "ready": 50000,
        "submitted": 0,
        "won": 0,
        "blocker": "Gateway restart (browser)"
    }
}

LEADS = {
    "total": 39,
    "high_priority": 3,
    "medium_priority": 10,
    "low_priority": 26,
    "messages_ready": 39,
    "messages_sent": 0
}

def format_currency(amount):
    """Format as $XK or $XM"""
    if amount >= 1000000:
        return f"${amount/1000000:.1f}M"
    elif amount >= 1000:
        return f"${amount/1000:.0f}K"
    return f"${amount}"

def bar_chart(value, max_val, width=30, filled="█", empty="░"):
    """Generate ASCII bar chart"""
    filled_len = int(width * value / max_val) if max_val > 0 else 0
    return filled * filled_len + empty * (width - filled_len)

def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def print_section(text):
    """Print section header"""
    print(f"\n▶ {text}")
    print("-" * 50)

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    print("╔" + "═"*58 + "╗")
    print("║" + " PIPELINE VISUALIZER".center(58) + "║")
    print("║" + f" {now}".center(58) + "║")
    print("╚" + "═"*58 + "╝")
    
    # Calculate totals
    total_identified = sum(p["identified"] for p in PIPELINE.values())
    total_ready = sum(p["ready"] for p in PIPELINE.values())
    total_submitted = sum(p["submitted"] for p in PIPELINE.values())
    total_won = sum(p["won"] for p in PIPELINE.values())
    
    print_section("OVERALL PIPELINE")
    
    stages = [
        ("Identified", total_identified),
        ("Ready", total_ready),
        ("Submitted", total_submitted),
        ("Won", total_won)
    ]
    
    max_val = max(v for _, v in stages)
    
    for stage, value in stages:
        bar = bar_chart(value, max_val)
        pct = (value / total_identified * 100) if total_identified > 0 else 0
        status = "✅" if stage == "Won" and value > 0 else "📊"
        print(f"{status} {stage:12} {bar} {format_currency(value):>8} ({pct:5.1f}%)")
    
    # Funnel conversion
    print_section("CONVERSION FUNNEL")
    
    funnel = [
        ("Identified", total_identified, 100.0),
        ("Ready", total_ready, total_ready/total_identified*100 if total_identified else 0),
        ("Submitted", total_submitted, total_submitted/total_identified*100 if total_identified else 0),
        ("Won", total_won, total_won/total_identified*100 if total_identified else 0)
    ]
    
    for stage, value, pct in funnel:
        width = int(pct / 2)  # Scale for visual
        block = "█" * width
        print(f"  {stage:12} │{block:<50}│ {pct:5.1f}%")
    
    # Breakdown by source
    print_section("BY SOURCE")
    
    for source, data in PIPELINE.items():
        print(f"\n  📁 {source.upper()}")
        
        # Stage breakdown
        stages_src = [
            ("Identified", data["identified"]),
            ("Ready", data["ready"]),
            ("Submitted", data["submitted"]),
            ("Won", data["won"])
        ]
        
        for stage, value in stages_src:
            pct = (value / data["identified"] * 100) if data["identified"] > 0 else 0
            symbol = "✓" if value > 0 else "·"
            print(f"    {symbol} {stage:12} {format_currency(value):>8} ({pct:5.1f}%)")
        
        # Blocker
        if data["blocker"]:
            print(f"    ⚠️  Blocker: {data['blocker']}")
    
    # Lead summary
    print_section("LEAD STATUS")
    print(f"  Total leads: {LEADS['total']}")
    print(f"    🔴 HIGH:   {LEADS['high_priority']:2} leads (~${115}K)")
    print(f"    🟡 MEDIUM: {LEADS['medium_priority']:2} leads (~${127.5}K)")  
    print(f"    🟢 LOW:    {LEADS['low_priority']:2} leads (~$0K estimated)")
    print(f"\n  Messages ready: {LEADS['messages_ready']}")
    print(f"  Messages sent:  {LEADS['messages_sent']} ⚠️")
    
    # Key metrics
    print_section("KEY METRICS")
    
    conversion_rate = (total_won / total_submitted * 100) if total_submitted > 0 else 0
    execution_gap = total_ready - total_submitted
    
    print(f"  Conversion rate:     {conversion_rate:.1f}%")
    print(f"  Execution gap:       {format_currency(execution_gap)} ❌")
    print(f"  Avg deal size:       {format_currency(total_identified / 39) if LEADS['total'] else '$0'}")
    print(f"  Time to $100K:       ~30 min (Arthur execution)")
    
    # Next actions
    print_section("NEXT ACTIONS (Priority Order)")
    
    actions = [
        ("Gateway restart", "1 min", "$50K", "🔥 CRITICAL"),
        ("GitHub auth", "5 min", "$125K", "🔥 CRITICAL"),
        ("Send HIGH priority messages (3)", "9 min", "$115K", "🎯 HIGH"),
        ("Send MEDIUM priority messages (10)", "23 min", "$127.5K", "📋 MEDIUM"),
        ("Submit 5 grants", "15 min", "$125K", "🎯 HIGH"),
    ]
    
    for action, time, value, priority in actions:
        print(f"  {priority} {action}")
        # Parse value (handle $XK format)
        val_num = value.replace('$','').replace('K','')
        if '.' in val_num:
            val_int = int(float(val_num) * 1000)
        else:
            val_int = int(val_num) * 1000 if 'K' in value else int(val_num)
        # Parse time
        time_num = int(time.split()[0])
        roi = val_int // time_num if time_num > 0 else 0
        print(f"           Time: {time} │ Value: {value} │ ROI: {format_currency(roi)}/min")
    
    # Summary box
    print("\n" + "╔" + "═"*58 + "╗")
    print("║" + " SUMMARY".center(58) + "║")
    print("╠" + "═"*58 + "╣")
    print(f"║  Total pipeline:     {format_currency(total_identified):>12}          ║")
    print(f"║  Ready to submit:    {format_currency(total_ready):>12}          ║")
    print(f"║  Actually submitted: {format_currency(total_submitted):>12} ❌       ║")
    print(f"║  Revenue realized:   {format_currency(total_won):>12}          ║")
    print("╠" + "═"*58 + "╣")
    print(f"║  Execution gap:      {format_currency(execution_gap):>12} ⏳       ║")
    print(f"║  Time to close gap:  {'57 minutes':>12}          ║")
    print(f"║  ROI per minute:     {'$11,088':>12}          ║")
    print("╚" + "═"*58 + "╝")
    
    print("\n💡 Run: python3 tools/lead-prioritizer.py for detailed lead info")
    print("💡 Read: ARTHUR-QUICK-REF.md for execution commands\n")

if __name__ == "__main__":
    main()
