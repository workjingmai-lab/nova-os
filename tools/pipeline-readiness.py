#!/usr/bin/env python3
"""
Pipeline Readiness Calculator

What % of your revenue pipeline is actually ready to submit?
This distinguishes between "identified" vs "ready to ship" opportunities.

Usage:
    python3 pipeline-readiness.py
"""

import json
from pathlib import Path
from datetime import datetime

PIPELINE_FILE = Path("revenue-pipeline.json")

def load_pipeline():
    """Load pipeline data from JSON file."""
    if not PIPELINE_FILE.exists():
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        return None

    with open(PIPELINE_FILE, 'r') as f:
        return json.load(f)

def calculate_readiness(pipeline):
    """Calculate pipeline readiness metrics."""
    stats = {
        'grants': {'total': 0, 'ready': 0, 'submitted': 0, 'potential': 0},
        'services': {'total': 0, 'ready': 0, 'submitted': 0, 'potential': 0},
        'bounties': {'total': 0, 'ready': 0, 'submitted': 0, 'potential': 0},
        'overall': {'total': 0, 'ready': 0, 'submitted': 0, 'potential': 0}
    }

    # Parse categories from pipeline structure
    categories = pipeline.get('categories', {})

    for cat_name, cat_data in categories.items():
        if cat_name not in stats:
            continue

        potential = cat_data.get('amount', 0)
        status = cat_data.get('status', 'unknown')

        stats[cat_name]['potential'] = potential
        stats['overall']['potential'] += potential

        # Count opportunities
        opportunities = cat_data.get('opportunities', [])
        stats[cat_name]['total'] = len(opportunities)
        stats['overall']['total'] += len(opportunities)

        # Check if ready
        if status in ['ready', 'messages_ready', 'ready_to_submit']:
            stats[cat_name]['ready'] = len(opportunities)
            stats['overall']['ready'] += len(opportunities)

        # Check if submitted (look for submitted count in services)
        if cat_name == 'services':
            submitted = cat_data.get('messagesSent', 0)
            stats[cat_name]['submitted'] = submitted
            stats['overall']['submitted'] += submitted
        elif cat_name == 'grants' and status == 'submitted':
            stats[cat_name]['submitted'] = len(opportunities)
            stats['overall']['submitted'] += len(opportunities)

    return stats

def print_readiness_report(stats):
    """Print readiness score report."""
    print("\n📊 PIPELINE READINESS SCORE")
    print("=" * 60)

    for category in ['grants', 'services', 'bounties', 'overall']:
        if stats[category]['total'] == 0:
            continue

        cat_name = category.upper()
        total = stats[category]['total']
        ready = stats[category]['ready']
        submitted = stats[category]['submitted']
        potential = stats[category]['potential']

        ready_pct = (ready / total * 100) if total > 0 else 0
        submitted_pct = (submitted / total * 100) if total > 0 else 0

        print(f"\n{cat_name}:")
        print(f"  Total items: {total}")
        print(f"  Ready to submit: {ready} ({ready_pct:.1f}%)")
        print(f"  Submitted: {submitted} ({submitted_pct:.1f}%)")
        print(f"  Potential value: ${potential:,.0f}")

    print("\n" + "=" * 60)

    # Readiness gap analysis
    overall = stats['overall']
    ready_gap = overall['total'] - overall['ready']
    execution_gap = overall['ready'] - overall['submitted']

    print(f"\n🎯 READINESS GAP:")
    print(f"  Items needing work: {ready_gap}")
    print(f"\n🚀 EXECUTION GAP:")
    print(f"  Items ready but not sent: {execution_gap}")

    if overall['total'] > 0:
        unsubmitted_value = overall['potential'] * (execution_gap / overall['total'])
        print(f"  Value sitting unsubmitted: ${unsubmitted_value:,.0f}")
    else:
        print(f"  Value sitting unsubmitted: $0")

if __name__ == "__main__":
    pipeline = load_pipeline()
    if pipeline:
        stats = calculate_readiness(pipeline)
        print_readiness_report(stats)
