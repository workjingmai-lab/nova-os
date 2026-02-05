#!/usr/bin/env python3
"""
Revenue Pipeline Dashboard — Visualize $216K opportunity

Shows grants, services, bounties with status tracking
"""

import json
from pathlib import Path
from datetime import datetime

REVENUE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline data"""
    if REVENUE_FILE.exists():
        with open(REVENUE_FILE, 'r') as f:
            return json.load(f)
    return {
        "grants": [],
        "services": [],
        "bounties": [],
        "last_updated": None
    }

def format_currency(amount):
    """Format amount with K suffix"""
    if amount >= 1000:
        return f"${amount//1000}K"
    return f"${amount}"

def calculate_metrics(pipeline):
    """Calculate pipeline metrics"""
    grants = pipeline.get("grants", [])
    services = pipeline.get("services", [])
    bounties = pipeline.get("bounties", [])
    
    # Count by status
    grant_ready = sum(g.get("potential", 0) for g in grants if g.get("status") == "ready")
    grant_total = sum(g.get("potential", 0) for g in grants)
    
    service_ready = sum(s.get("potential", 0) for s in services if s.get("status") == "ready")
    service_total = sum(s.get("potential", 0) for s in services)
    
    bounty_ready = sum(b.get("potential", 0) for b in bounties if b.get("status") == "ready")
    bounty_total = sum(b.get("potential", 0) for b in bounties)
    
    total_ready = grant_ready + service_ready + bounty_ready
    total_pipeline = grant_total + service_total + bounty_total
    
    return {
        "grants": {"ready": grant_ready, "total": grant_total, "count": len(grants)},
        "services": {"ready": service_ready, "total": service_total, "count": len(services)},
        "bounties": {"ready": bounty_ready, "total": bounty_total, "count": len(bounties)},
        "total": {"ready": total_ready, "pipeline": total_pipeline}
    }

def print_dashboard(metrics):
    """Print ASCII dashboard"""
    print("\n" + "="*60)
    print(" 💰 REVENUE PIPELINE DASHBOARD".center(60))
    print("="*60)
    print()
    
    # Total pipeline
    print(f"  TOTAL PIPELINE: {format_currency(metrics['total']['pipeline'])}")
    print(f"  Ready to execute: {format_currency(metrics['total']['ready'])}")
    print()
    
    # Bar chart
    bar_width = 40
    ready_pct = metrics['total']['ready'] / metrics['total']['pipeline'] if metrics['total']['pipeline'] > 0 else 0
    ready_bars = int(bar_width * ready_pct)
    pending_bars = bar_width - ready_bars
    
    print(f"  Pipeline Status:")
    bar_filled = '█' * ready_bars
    bar_empty = '░' * pending_bars
    print(f"  [{bar_filled}{bar_empty}]")
    print(f"  {format_currency(metrics['total']['ready']):>6} ready {format_currency(metrics['total']['pipeline'] - metrics['total']['ready']):>6} pending")
    print()
    
    # By category
    print("  By Category:")
    print(f"  ┌─ Grants:    {format_currency(metrics['grants']['total']):>6} ({metrics['grants']['count']} opportunities)")
    print(f"  │  └─ Ready:  {format_currency(metrics['grants']['ready']):>6}")
    print(f"  ├─ Services:  {format_currency(metrics['services']['total']):>6} ({metrics['services']['count']} leads)")
    print(f"  │  └─ Ready:  {format_currency(metrics['services']['ready']):>6}")
    print(f"  └─ Bounties:  {format_currency(metrics['bounties']['total']):>6} ({metrics['bounties']['count']} opportunities)")
    print(f"     └─ Ready:  {format_currency(metrics['bounties']['ready']):>6}")
    print()
    
    # Top opportunities
    pipeline = load_pipeline()
    
    print("  Top 5 Opportunities:")
    all_opps = []
    
    for g in pipeline.get("grants", []):
        all_opps.append({
            "name": g.get("name", "Unknown"),
            "amount": g.get("potential", 0),
            "status": g.get("status", "unknown"),
            "type": "grant"
        })
    
    for s in pipeline.get("services", []):
        all_opps.append({
            "name": s.get("name", "Unknown"),
            "amount": s.get("potential", 0),
            "status": s.get("status", "unknown"),
            "type": "service"
        })
    
    for b in pipeline.get("bounties", []):
        all_opps.append({
            "name": b.get("name", "Unknown"),
            "amount": b.get("potential", 0),
            "status": b.get("status", "unknown"),
            "type": "bounty"
        })
    
    # Sort by amount
    all_opps.sort(key=lambda x: x["amount"], reverse=True)
    
    for i, opp in enumerate(all_opps[:5], 1):
        status_icon = "✅" if opp["status"] == "ready" else "⏸️"
        print(f"  {i}. {status_icon} {opp['name'][:35]:<35} {format_currency(opp['amount'])}")
    
    print()
    print(f"  Last updated: {pipeline.get('last_updated', 'Never')}")
    print("="*60 + "\n")

def main():
    """Main dashboard"""
    pipeline = load_pipeline()
    metrics = calculate_metrics(pipeline)
    print_dashboard(metrics)

if __name__ == "__main__":
    main()
