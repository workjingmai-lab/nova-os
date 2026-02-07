#!/usr/bin/env python3
"""
funnel-visualizer.py — ASCII conversion funnel for revenue pipeline
Usage: python3 tools/funnel-visualizer.py
"""

import json
from pathlib import Path

def load_pipeline():
    with open('revenue-pipeline.json') as f:
        return json.load(f)

def format_currency(amount):
    """Format as K/M shorthand"""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    return f"${amount//1_000}K"

def draw_funnel(pipeline):
    """Draw ASCII funnel"""

    # Stage data
    total = pipeline['totalPipeline']
    grants_ready = pipeline['categories']['grants']['ready']
    grants_submitted = pipeline['categories']['grants']['submitted']
    grants_won = pipeline['categories']['grants'].get('won', 0)

    services_ready = pipeline['categories'].get('services', {}).get('ready', 0)
    services_submitted = pipeline['categories'].get('services', {}).get('submitted', 0)
    services_won = pipeline['categories'].get('services', {}).get('won', 0)

    total_ready = grants_ready + services_ready
    total_submitted = grants_submitted + services_submitted
    total_won = grants_won + services_won

    # Funnel widths (proportional, max 40 chars)
    max_width = 40
    width_total = max_width
    width_ready = int(max_width * (total_ready / total)) if total > 0 else 0
    width_submitted = int(max_width * (total_submitted / total)) if total > 0 else 0
    width_won = int(max_width * (total_won / total)) if total > 0 else 0

    print("\n" + "="*52)
    print("  PIPELINE CONVERSION FUNNEL")
    print("="*52)

    # Stage 1: Total Pipeline
    print(f"\n  1. PIPELINE BUILT")
    print(f"     {format_currency(total)}")
    print(f"     {'█' * width_total}")

    # Stage 2: Ready to Send
    print(f"\n  2. READY TO SEND")
    print(f"     {format_currency(total_ready)} ({total_ready/total*100:.1f}%)")
    print(f"     {'█' * width_ready}")

    # Stage 3: Submitted
    print(f"\n  3. SUBMITTED")
    print(f"     {format_currency(total_submitted)} ({total_submitted/total*100:.1f}%)")
    print(f"     {'█' * width_submitted}")

    # Stage 4: Won
    print(f"\n  4. WON")
    print(f"     {format_currency(total_won)} ({total_won/total*100:.1f}%)")
    print(f"     {'█' * width_won}")

    # Summary
    print("\n" + "-"*52)
    print(f"  CONVERSION RATES:")
    print(f"  Pipeline → Ready:  {total_ready/total*100:.1f}%")
    print(f"  Ready → Sent:     {total_submitted/total_ready*100:.1f}%")
    print(f"  Sent → Won:       {total_won/total_submitted*100:.1f}%" if total_submitted > 0 else "  Sent → Won:       N/A (no submissions)")
    print(f"  Overall:          {total_won/total*100:.1f}%")
    print("-"*52 + "\n")

    # Breakdown by category
    print(f"  BREAKDOWN:")
    print(f"  • Grants:    {format_currency(pipeline['categories']['grants']['amount'])} (ready: {format_currency(grants_ready)}, sent: {format_currency(grants_submitted)})")
    if 'services' in pipeline['categories']:
        services_amt = pipeline['categories']['services'].get('amount', 0)
        print(f"  • Services:  {format_currency(services_amt)} (ready: {format_currency(services_ready)}, sent: {format_currency(services_submitted)})")
    if 'bounties' in pipeline['categories']:
        bounties_amt = pipeline['categories']['bounties'].get('amount', 0)
        print(f"  • Bounties:  {format_currency(bounties_amt)}")
    print()

if __name__ == '__main__':
    pipeline = load_pipeline()
    draw_funnel(pipeline)
