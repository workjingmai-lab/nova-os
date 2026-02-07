#!/usr/bin/env python3
"""
week-4-tracker.py — Week 4 execution progress tracker

Tracks progress against Week 4 plan (Feb 15-21):
- Daily targets vs actuals
- Cumulative metrics
- Variance analysis
- Remaining work

Usage: python3 tools/week-4-tracker.py
"""

import json
from datetime import datetime, timedelta

# Week 4 plan data
WEEK_4_PLAN = {
    "week": "Feb 15-21, 2026",
    "theme": "Revenue Conversion",
    "targets": {
        "revenue_submitted": 500000,
        "responses": 7,
        "calls": 3,
        "proposals": 2,
        "deals_closed": 1,
        "revenue_realized": 15000
    },
    "daily_plan": {
        "Mon": {"messages": 39, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0},
        "Tue": {"messages": 3, "responses": 5, "calls": 2, "proposals": 0, "revenue": 0},
        "Wed": {"messages": 3, "responses": 3, "calls": 0, "proposals": 2, "revenue": 0},
        "Thu": {"messages": 2, "responses": 2, "calls": 2, "proposals": 0, "revenue": 10000},
        "Fri": {"messages": 5, "responses": 1, "calls": 0, "proposals": 1, "revenue": 5000},
    }
}

# Current progress (would be loaded from file in real implementation)
# For now, using zeros since Week 4 hasn't started
CURRENT_PROGRESS = {
    "Mon": {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0, "notes": "Week not started"},
    "Tue": {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0, "notes": ""},
    "Wed": {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0, "notes": ""},
    "Thu": {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0, "notes": ""},
    "Fri": {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0, "notes": ""},
}

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def print_section(text):
    print(f"\n▶ {text}")
    print("-" * 50)

def format_currency(amount):
    if amount >= 1000:
        return f"${amount/1000:.0f}K"
    return f"${amount}"

def calculate_progress():
    """Calculate totals and variances"""
    plan_totals = {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0}
    actual_totals = {"messages": 0, "responses": 0, "calls": 0, "proposals": 0, "revenue": 0}
    
    for day in WEEK_4_PLAN["daily_plan"]:
        for metric in plan_totals:
            plan_totals[metric] += WEEK_4_PLAN["daily_plan"][day].get(metric, 0)
            actual_totals[metric] += CURRENT_PROGRESS.get(day, {}).get(metric, 0)
    
    return plan_totals, actual_totals

def print_daily_breakdown():
    """Print day-by-day status"""
    print_section("DAILY PROGRESS")
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    
    for day in days:
        plan = WEEK_4_PLAN["daily_plan"].get(day, {})
        actual = CURRENT_PROGRESS.get(day, {})
        
        # Determine status
        if actual.get("messages", 0) >= plan.get("messages", 0):
            status = "✅"
        elif actual.get("messages", 0) > 0:
            status = "🟡"
        else:
            status = "⏳"
        
        print(f"\n  {status} {day}:")
        print(f"     Messages: {actual.get('messages', 0)}/{plan.get('messages', 0)}", end="")
        if actual.get("responses", 0) > 0:
            print(f" | Responses: {actual.get('responses', 0)}", end="")
        if actual.get("calls", 0) > 0:
            print(f" | Calls: {actual.get('calls', 0)}", end="")
        if actual.get("revenue", 0) > 0:
            print(f" | Revenue: {format_currency(actual.get('revenue', 0))}", end="")
        print()
        
        notes = actual.get("notes", "")
        if notes:
            print(f"     Note: {notes}")

def print_variance_analysis():
    """Print plan vs actual variance"""
    print_section("VARIANCE ANALYSIS")
    
    plan, actual = calculate_progress()
    
    metrics = ["messages", "responses", "calls", "proposals", "revenue"]
    
    for metric in metrics:
        p = plan[metric]
        a = actual[metric]
        var = a - p
        
        if p > 0:
            pct = (a / p * 100)
        else:
            pct = 100 if a > 0 else 0
        
        status = "✅" if var >= 0 else "❌" if var < 0 and pct < 50 else "🟡"
        
        if metric == "revenue":
            print(f"  {status} {metric:12} {format_currency(a):>8} / {format_currency(p):>8} ({pct:5.1f}%)")
        else:
            print(f"  {status} {metric:12} {a:8} / {p:8} ({pct:5.1f}%)")

def print_forecast():
    """Print forecast based on current trajectory"""
    print_section("FORECAST")
    
    plan, actual = calculate_progress()
    
    # Simple linear forecast
    days_elapsed = sum(1 for d in CURRENT_PROGRESS if CURRENT_PROGRESS[d].get("messages", 0) > 0)
    total_days = 5
    
    if days_elapsed > 0:
        completion_rate = days_elapsed / total_days
        
        for metric in ["responses", "calls", "proposals", "revenue"]:
            if plan[metric] > 0:
                projected = actual[metric] / completion_rate if completion_rate > 0 else 0
                variance = projected - plan[metric]
                
                if metric == "revenue":
                    print(f"  {metric:12} Projected: {format_currency(projected)} (Target: {format_currency(plan[metric])})")
                else:
                    print(f"  {metric:12} Projected: {projected:.0f} (Target: {plan[metric]})")
    else:
        print("  Week not started — no forecast available")

def print_recommendations():
    """Print action recommendations"""
    print_section("RECOMMENDATIONS")
    
    plan, actual = calculate_progress()
    
    if actual["messages"] == 0:
        print("  🔥 CRITICAL: Week 4 hasn't started")
        print("     Action: Arthur must execute 57-min plan immediately")
        print("     File: ARTHUR-QUICK-REF.md")
        return
    
    # Find biggest gaps
    gaps = []
    for metric in ["responses", "calls", "proposals", "revenue"]:
        if plan[metric] > 0:
            gap_pct = (plan[metric] - actual[metric]) / plan[metric]
            gaps.append((metric, gap_pct))
    
    gaps.sort(key=lambda x: x[1], reverse=True)
    
    for metric, gap in gaps[:3]:
        if gap > 0.2:  # >20% behind
            print(f"  ⚠️  {metric}: {gap*100:.0f}% behind plan")
            
            if metric == "responses":
                print("     Action: Review message quality, send follow-ups")
            elif metric == "calls":
                print("     Action: Push for calls in follow-ups")
            elif metric == "proposals":
                print("     Action: Qualify leads faster, send proposals")
            elif metric == "revenue":
                print("     Action: Close calls, send invoices")

def main():
    now = datetime.utcnow()
    
    print_header(f"WEEK 4 TRACKER — {WEEK_4_PLAN['week']}")
    print(f"\n  Theme: {WEEK_4_PLAN['theme']}")
    print(f"  Generated: {now.strftime('%Y-%m-%d %H:%M')} UTC")
    
    # Check if Week 4 has started
    week4_start = datetime(2026, 2, 15)
    if now < week4_start:
        days_until = (week4_start - now).days
        print(f"\n  ⏳ Week 4 starts in {days_until} days (Feb 15)")
        print(f"  Current status: PREP MODE")
    
    print_daily_breakdown()
    print_variance_analysis()
    print_forecast()
    print_recommendations()
    
    # Summary box
    plan, actual = calculate_progress()
    
    print("\n" + "╔" + "═"*58 + "╗")
    print("║" + " WEEK 4 SUMMARY".center(58) + "║")
    print("╠" + "═"*58 + "╣")
    
    revenue_pct = (actual["revenue"] / plan["revenue"] * 100) if plan["revenue"] > 0 else 0
    print(f"║  Revenue target:     {format_currency(plan['revenue']):>10}                ║")
    print(f"║  Revenue actual:     {format_currency(actual['revenue']):>10} ({revenue_pct:5.1f}%)         ║")
    print(f"║  Messages sent:      {actual['messages']:>10} / {plan['messages']:>10}         ║")
    print(f"║  Conversations:      {actual['responses']:>10} / {plan['responses']:>10}         ║")
    print("╚" + "═"*58 + "╝")
    
    print("\n💡 Update progress in week-4-tracker.py CURRENT_PROGRESS dict")
    print("💡 View full plan: knowledge/week-4-execution-plan.md\n")

if __name__ == "__main__":
    main()
