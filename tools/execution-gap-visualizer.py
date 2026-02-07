#!/usr/bin/env python3
"""
Execution Gap Visualizer — Shows the gap between ready and sent revenue

Makes the invisible visible: "You have $X ready but haven't sent anything."

Usage:
    python3 execution-gap-visualizer.py
"""

import json
from pathlib import Path

PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline data."""
    try:
        with open(PIPELINE_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Pipeline file not found")
        return None

def calculate_metrics(pipeline):
    """Calculate metrics from raw pipeline data."""
    total = 0
    ready = 0
    submitted = 0
    won = 0

    for category in ["grants", "services", "bounties"]:
        for item in pipeline.get(category, []):
            potential = item.get("potential", 0)
            status = item.get("status", "lead")
            total += potential

            if status in ["ready", "ready_to_submit", "messages_ready", "outreach-ready"]:
                ready += potential
            elif status == "submitted":
                submitted += potential
                ready += potential  # Submitted was ready before
            elif status == "won":
                won += potential
                submitted += potential
                ready += potential

    gap_dollars = ready - submitted
    gap_percent = (gap_dollars / ready * 100) if ready > 0 else 0

    return {
        "total": total,
        "ready": ready,
        "submitted": submitted,
        "won": won,
        "gap_dollars": gap_dollars,
        "gap_percent": gap_percent
    }

def format_currency(amount):
    """Format as currency."""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount:.0f}"

def visualize(metrics):
    """Print visual gap representation."""
    print("\n" + "="*60)
    print("💰 EXECUTION GAP VISUALIZER")
    print("="*60)

    print(f"\n📊 Pipeline Status:")
    print(f"   Total:     {format_currency(metrics['total'])}")
    print(f"   Ready:     {format_currency(metrics['ready'])}")
    print(f"   Submitted: {format_currency(metrics['submitted'])}")
    print(f"   Won:       {format_currency(metrics['won'])}")

    print(f"\n🚨 THE GAP:")
    print(f"   Gap:       {format_currency(metrics['gap_dollars'])} ({metrics['gap_percent']:.1f}%)")

    # Visual bar
    bar_width = 40
    ready_ratio = metrics['submitted'] / metrics['ready'] if metrics['ready'] > 0 else 0
    filled = int(bar_width * ready_ratio)
    empty = bar_width - filled

    filled_bar = '█' * filled
    empty_bar = '░' * empty
    print(f"\n   Progress:  [{filled_bar}{empty_bar}] {ready_ratio*100:.1f}%")
    print(f"              {format_currency(metrics['submitted'])} sent / {format_currency(metrics['ready'])} ready")

    print(f"\n⏱️  Time to Close Gap:")
    minutes = metrics['gap_dollars'] / 10_000  # Assuming $10K/min
    print(f"   At $10K/min: {minutes:.0f} minutes")

    print(f"\n💡 Reality Check:")
    if metrics['gap_percent'] > 95:
        print(f"   ⚠️  You have {format_currency(metrics['gap_dollars'])} ready to send.")
        print(f"   ⚠️  Why haven't you hit send yet?")
    elif metrics['gap_percent'] > 50:
        print(f"   📈 Good progress, but {format_currency(metrics['gap_dollars'])} still on the table.")
    else:
        print(f"   ✅ Execution is happening!")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    pipeline = load_pipeline()
    if pipeline:
        metrics = calculate_metrics(pipeline)
        visualize(metrics)
