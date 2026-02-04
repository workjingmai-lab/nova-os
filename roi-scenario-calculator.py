#!/usr/bin/env python3
"""
ROI Scenario Calculator — What If?

Shows revenue potential under different response/conversion scenarios.
Usage: python roi-scenario-calculator.py
"""

import json
from pathlib import Path

# Pipeline data (from today.md)
PIPELINE = {
    "services": 2007000,  # $2,007K
    "grants": 130000,     # $130K
    "bounties": 43000,    # $43K
    "total": 2180000      # $2,180K
}

def calculate_scenario(response_rate, conversion_rate, avg_deal_size):
    """Calculate revenue for a given scenario."""
    messages_sent = 103  # Total messages ready

    responses = int(messages_sent * response_rate)
    deals = int(responses * conversion_rate)
    revenue = deals * avg_deal_size

    return {
        "responses": responses,
        "deals": deals,
        "revenue": revenue,
        "response_rate": f"{response_rate*100:.0f}%",
        "conversion_rate": f"{conversion_rate*100:.0f}%"
    }

def format_currency(value):
    """Format as currency."""
    if value >= 1000000:
        return f"${value/1000000:.2f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value:.0f}"

def print_scenario(name, scenario):
    """Print scenario results."""
    print(f"\n{'='*60}")
    print(f"📊 {name}")
    print(f"{'='*60}")
    print(f"Response Rate:    {scenario['response_rate']}")
    print(f"Responses:        {scenario['responses']} out of 103 messages")
    print(f"Conversion Rate:  {scenario['conversion_rate']}")
    print(f"Deals Closed:     {scenario['deals']}")
    print(f"Revenue:          {format_currency(scenario['revenue'])}")
    print(f"{'='*60}")

def main():
    """Calculate and display scenarios."""
    print("\n🎯 ROI SCENARIO CALCULATOR")
    print(f"Pipeline: {format_currency(PIPELINE['total'])} (103 messages ready)\n")

    # Average deal sizes (from service proposal templates)
    # Quick: $1-2K, Setup: $3-5K, Multi-agent: $10-25K
    avg_deal_sizes = {
        "conservative": 2000,   # $2K average (quick automations)
        "realistic": 5000,      # $5K average (mix of quick + setup)
        "optimistic": 15000     # $15K average (multi-agent systems)
    }

    # Scenario 1: Conservative (5% response, 5% conversion, $2K deals)
    conservative = calculate_scenario(0.05, 0.05, avg_deal_sizes["conservative"])
    print_scenario("🔴 CONSERVATIVE (5% response, 5% conversion, $2K deals)", conservative)

    # Scenario 2: Realistic (10% response, 10% conversion, $5K deals)
    realistic = calculate_scenario(0.10, 0.10, avg_deal_sizes["realistic"])
    print_scenario("🟡 REALISTIC (10% response, 10% conversion, $5K deals)", realistic)

    # Scenario 3: Optimistic (15% response, 20% conversion, $15K deals)
    optimistic = calculate_scenario(0.15, 0.20, avg_deal_sizes["optimistic"])
    print_scenario("🟢 OPTIMISTIC (15% response, 20% conversion, $15K deals)", optimistic)

    # Scenario 4: Best Case (20% response, 30% conversion, $15K deals)
    best_case = calculate_scenario(0.20, 0.30, avg_deal_sizes["optimistic"])
    print_scenario("🚀 BEST CASE (20% response, 30% conversion, $15K deals)", best_case)

    # Summary table
    print(f"\n📈 SUMMARY TABLE")
    print(f"{'Scenario':<12} {'Responses':<10} {'Deals':<8} {'Revenue':<12}")
    print(f"{'-'*45}")
    print(f"{'Conservative':<12} {conservative['responses']:<10} {conservative['deals']:<8} {format_currency(conservative['revenue']):<12}")
    print(f"{'Realistic':<12} {realistic['responses']:<10} {realistic['deals']:<8} {format_currency(realistic['revenue']):<12}")
    print(f"{'Optimistic':<12} {optimistic['responses']:<10} {optimistic['deals']:<8} {format_currency(optimistic['revenue']):<12}")
    print(f"{'Best Case':<12} {best_case['responses']:<10} {best_case['deals']:<8} {format_currency(best_case['revenue']):<12}")

    # Key insights
    print(f"\n💡 KEY INSIGHTS")
    print(f"• Conservative: {conservative['responses']} responses = {conservative['deals']} deals = {format_currency(conservative['revenue'])}")
    print(f"• Realistic: {realistic['responses']} responses = {realistic['deals']} deals = {format_currency(realistic['revenue'])}")
    print(f"• Optimistic: {optimistic['responses']} responses = {optimistic['deals']} deals = {format_currency(optimistic['revenue'])}")
    print(f"• Best Case: {best_case['responses']} responses = {best_case['deals']} deals = {format_currency(best_case['revenue'])}")
    print(f"\n🎯 Most Likely Outcome: {realistic['responses']}-{optimistic['responses']} responses")
    print(f"   → {realistic['deals']}-{optimistic['deals']} deals")
    print(f"   → {format_currency(realistic['revenue'])}-{format_currency(optimistic['revenue'])} revenue")

    print(f"\n✅ EXECUTE NOW → Send 103 messages → Track responses → Close deals")
    print(f"   Command: python tools/service-batch-send.py --mode all\n")

if __name__ == "__main__":
    main()
