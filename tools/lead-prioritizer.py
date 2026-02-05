#!/usr/bin/env python3
"""
Lead Prioritizer — Rank revenue pipeline leads by ROI potential.

Helps focus on highest-value opportunities first.
Calculates priority score based on: potential value, blockers, readiness.

Usage:
    python3 lead-prioritizer.py                    # All leads, ranked
    python3 lead-prioritizer.py --category service # Services only
    python3 lead-prioritizer.py --blocked          # Show blocked items only
    python3 lead-prioritizer.py --ready            # Show ready-to-send only

Created: 2026-02-04 (Work block 1652)
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
PIPELINE_FILE = "/home/node/.openclaw/workspace/revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline from JSON file."""
    try:
        with open(PIPELINE_FILE, 'r') as f:
            data = json.load(f)

        # Transform to flat list format
        leads = []
        categories = data.get('categories', {})

        # Map category names
        category_map = {
            'grants': 'grant',
            'services': 'service',
            'bounties': 'bounty'
        }

        for cat_name, cat_data in categories.items():
            # Try different keys for opportunity lists
            opportunities = (cat_data.get('opportunities', []) or
                           cat_data.get('topProspects', []) or
                           cat_data.get('bounties', []))

            status = cat_data.get('status', 'unknown')
            blocker = cat_data.get('blocker', '')

            for opp in opportunities:
                leads.append({
                    'category': category_map.get(cat_name, cat_name),
                    'name': opp.get('name', 'Unknown'),
                    'potential': opp.get('amount', 0) // 1000,  # Convert to thousands
                    'status': status,
                    'notes': f"Blocker: {blocker}" if blocker and blocker != 'NONE' else 'Ready to send'
                })

        return leads
    except FileNotFoundError:
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        print("Run revenue-tracker.py first to create pipeline.")
        return None
    except Exception as e:
        print(f"❌ Error loading pipeline: {e}")
        return None

def calculate_score(item):
    """
    Calculate priority score (0-100).

    Formula:
    - Base score: potential value (normalized to 0-60)
    - Readiness bonus: +30 if no blockers
    - Blocker penalty: -40 if blocked
    - Category bonus: +10 for high-conversion categories

    Returns:
        tuple: (score, reason)
    """
    score = 0
    reasons = []

    # Value score (0-60) — more aggressive
    potential = item.get('potential', 0)
    value_score = min(potential, 60)  # $60K+ = max value score
    score += value_score
    reasons.append(f"Value: ${potential}K")

    # Readiness bonus — higher reward for ready items
    notes = item.get('notes', '').lower()
    if 'blocked' in notes or 'gateway restart' in notes or 'github' in notes or 'browser' in notes:
        score -= 40
        reasons.append("⛔ Blocked (needs Arthur action)")
    elif 'ready' in notes or 'zero blockers' in notes or 'no blockers' in notes or 'blocker: none' in notes:
        score += 30
        reasons.append("✅ Ready to send")
    else:
        reasons.append("⏳ May need research")

    # Category bonus
    category = item.get('category', '')
    if category == 'grant':
        score += 10
        reasons.append("Grant (higher conversion)")
    elif category == 'service':
        score += 5
        reasons.append("Service (direct outreach)")

    return int(max(0, min(score, 100))), reasons

def categorize_leads(leads):
    """Group leads by priority tier."""
    high = []      # Score 70+
    medium = []    # Score 40-69
    low = []       # Score < 40

    for lead in leads:
        score, reasons = calculate_score(lead)
        lead['score'] = score
        lead['reasons'] = reasons

        if score >= 70:
            high.append(lead)
        elif score >= 40:
            medium.append(lead)
        else:
            low.append(lead)

    return high, medium, low

def print_lead(lead, show_reasons=False):
    """Print a single lead with score."""
    score = lead.get('score', 0)
    name = lead.get('name', 'Unknown')
    potential = lead.get('potential', 0)
    status = lead.get('status', 'unknown')
    category = lead.get('category', 'unknown')

    # Score bar
    bar_length = score // 10
    bar = "█" * bar_length + "░" * (10 - bar_length)

    print(f"\n  [{category.upper()}] {name}")
    print(f"  Score: {score}/100 | {bar} | ${potential}K | {status}")

    if show_reasons:
        print(f"  Reasons:")
        for reason in lead.get('reasons', []):
            print(f"    • {reason}")

def print_summary(high, medium, low):
    """Print summary statistics."""
    total = len(high) + len(medium) + len(low)
    total_value = sum(l.get('potential', 0) for l in high + medium + low)
    high_value = sum(l.get('potential', 0) for l in high)

    print(f"\n{'='*60}")
    print(f"  📊 LEAD PRIORITY SUMMARY")
    print(f"{'='*60}")
    print(f"  Total leads: {total}")
    print(f"  Total pipeline: ${total_value}K")
    print(f"\n  Priority breakdown:")
    print(f"    🔥 HIGH (70+): {len(high)} leads = ${sum(l.get('potential', 0) for l in high)}K")
    print(f"    ⚡ MEDIUM (40-69): {len(medium)} leads = ${sum(l.get('potential', 0) for l in medium)}K")
    print(f"    💤 LOW (<40): {len(low)} leads = ${sum(l.get('potential', 0) for l in low)}K")
    print(f"\n  🎯 Focus on HIGH first — {len(high)} leads = ${high_value}K")
    print(f"{'='*60}")

def main():
    parser = argparse.ArgumentParser(description='Prioritize revenue pipeline leads')
    parser.add_argument('--category', choices=['grant', 'service', 'bounty'],
                        help='Filter by category')
    parser.add_argument('--ready', action='store_true',
                        help='Show only ready-to-send (no blockers)')
    parser.add_argument('--blocked', action='store_true',
                        help='Show only blocked items')
    parser.add_argument('--top', type=int, default=None,
                        help='Show top N leads only')
    parser.add_argument('--reasons', action='store_true',
                        help='Show scoring reasons')
    args = parser.parse_args()

    # Load pipeline (returns list)
    all_leads = load_pipeline()
    if not all_leads:
        return

    # Apply filters
    if args.category:
        all_leads = [l for l in all_leads if l['category'] == args.category]

    if args.ready:
        all_leads = [l for l in all_leads if 'ready' in l.get('notes', '').lower() or
                     'zero blockers' in l.get('notes', '').lower() or
                     'no blockers' in l.get('notes', '').lower() or
                     'blocker: none' in l.get('notes', '').lower()]

    if args.blocked:
        all_leads = [l for l in all_leads if 'blocked' in l.get('notes', '').lower() or
                     'gateway' in l.get('notes', '').lower() or
                     'github' in l.get('notes', '').lower() or
                     'browser' in l.get('notes', '').lower()]

    if not all_leads:
        print("❌ No leads found matching filters.")
        return

    # Categorize by score
    high, medium, low = categorize_leads(all_leads)
    all_ranked = high + medium + low

    # Apply --top limit
    if args.top:
        all_ranked = all_ranked[:args.top]
        high = [l for l in high if l in all_ranked]
        medium = [l for l in medium if l in all_ranked]
        low = [l for l in low if l in all_ranked]

    # Print results
    print("\n🎯 LEAD PRIORITIZATION")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if high:
        print(f"\n🔥 HIGH PRIORITY (Score 70+)")
        for lead in high:
            print_lead(lead, args.reasons)

    if medium:
        print(f"\n⚡ MEDIUM PRIORITY (Score 40-69)")
        for lead in medium:
            print_lead(lead, args.reasons)

    if low:
        print(f"\n💤 LOW PRIORITY (Score < 40)")
        for lead in low:
            print_lead(lead, args.reasons)

    # Print summary
    print_summary(high, medium, low)

    # Action recommendations
    print(f"\n💡 NEXT ACTIONS:")
    if high:
        highest = max(high, key=lambda x: x.get('score', 0))
        print(f"  1. Focus on: [{highest['category'].upper()}] {highest['name']} (${highest['potential']}K)")
        if 'ready' in str(highest.get('notes', '')).lower():
            print(f"     → ✅ Ready to send NOW")
        else:
            print(f"     → ⏳ May need prep/research")
    if args.blocked is False and any('blocked' in str(l.get('notes', '')).lower() or
                                      'gateway' in str(l.get('notes', '')).lower() or
                                      'github' in str(l.get('notes', '')).lower()
                                      for l in all_leads):
        print(f"  2. Unblock items: Run gateway restart (1 min → $180K unblocked)")
    print(f"  3. Track progress: revenue-tracker.py update <category> --name <name> --status submitted")

if __name__ == '__main__':
    main()
