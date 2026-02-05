#!/usr/bin/env python3
"""
Gap Cost Ticker — Shows Real-Time Cost of Execution Gap

Makes the invisible visible: How much revenue we're losing by waiting.

Usage:
    python3 tools/gap-cost-ticker.py

Output:
    - Days since gap identified
    - Revenue at risk
    - Daily opportunity cost
    - Total cost to date
"""

from datetime import datetime, timezone
import json

def load_gap_data():
    """Load gap identification date and revenue at risk."""
    return {
        "gap_identified": "2026-02-05",  # When gap was first identified
        "revenue_at_risk": 435000,  # $435K ready but not submitted
        "time_to_close_minutes": 31,  # 31 minutes to close gap
    }

def calculate_costs():
    """Calculate opportunity costs of waiting."""
    data = load_gap_data()
    
    # Parse gap identification date
    gap_date = datetime.strptime(data["gap_identified"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    
    # Calculate days waiting
    days_waiting = (now - gap_date).days
    
    # Calculate costs
    revenue_at_risk = data["revenue_at_risk"]
    daily_cost = revenue_at_risk  # $435K/day (conservative estimate)
    total_cost = days_waiting * daily_cost
    
    # Per-minute cost (from $14,032/min figure)
    per_minute_cost = round(revenue_at_risk / data["time_to_close_minutes"])
    hourly_cost = per_minute_cost * 60
    
    return {
        "days_waiting": days_waiting,
        "revenue_at_risk": revenue_at_risk,
        "daily_cost": daily_cost,
        "total_cost": total_cost,
        "per_minute_cost": per_minute_cost,
        "hourly_cost": hourly_cost,
    }

def format_currency(amount):
    """Format amount as currency string."""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount}"

def display_ticker():
    """Display the gap cost ticker."""
    costs = calculate_costs()
    
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║         🚨 EXECUTION GAP COST TICKER 🚨                    ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    print(f"⏱️  Days Waiting:        {costs['days_waiting']} days")
    print(f"💰 Revenue at Risk:     {format_currency(costs['revenue_at_risk'])}")
    print()
    print("💸 Opportunity Cost:")
    print(f"   • Per minute:         {format_currency(costs['per_minute_cost'])}/min")
    print(f"   • Per hour:           {format_currency(costs['hourly_cost'])}/hr")
    print(f"   • Per day:            {format_currency(costs['daily_cost'])}/day")
    print()
    print(f"📉 Total Cost to Date:   {format_currency(costs['total_cost'])}")
    print()
    print("⚡  Close the gap: 31 minutes → $435K submitted")
    print("   Run: python3 tools/execution-gap.py")
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()

if __name__ == "__main__":
    display_ticker()
