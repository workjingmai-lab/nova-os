#!/usr/bin/env python3
"""
conversion-dashboard.py - Real-time revenue conversion tracking
Created: Work block 3063, 2026-02-07
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

PIPELINE_FILE = Path("data/revenue-pipeline.json")

def load_pipeline():
    if PIPELINE_FILE.exists():
        with open(PIPELINE_FILE) as f:
            return json.load(f)
    return {}

def print_header(text):
    print(f"\n{'='*70}")
    print(f"  {text}")
    print(f"{'='*70}")

def print_metric(label, value, unit=""):
    print(f"  {label:25} {value:>15} {unit}")

def print_bar(label, current, total, width=40):
    if total == 0:
        pct = 0
        filled = 0
    else:
        pct = current / total
        filled = int(width * pct)
    bar = "█" * filled + "░" * (width - filled)
    print(f"  {label:15} |{bar}| {pct*100:5.1f}%")

def flatten_pipeline(data):
    """Flatten nested category structure into list of items."""
    items = []
    for category, entries in data.items():
        if isinstance(entries, list):
            for entry in entries:
                entry["category"] = category
                # Normalize field names
                entry["value"] = entry.get("potential", entry.get("value", 0))
                items.append(entry)
    return items

def main():
    data = load_pipeline()
    items = flatten_pipeline(data)
    
    now = datetime.now()
    
    print_header("REVENUE CONVERSION DASHBOARD")
    print(f"  Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    
    # Summary metrics
    print_header("PIPELINE OVERVIEW")
    
    total = sum(item.get("value", 0) for item in items)
    ready = sum(item.get("value", 0) for item in items if item.get("status") in ("ready", "ready_to_submit"))
    submitted = sum(item.get("value", 0) for item in items if item.get("status") == "submitted")
    won = sum(item.get("value", 0) for item in items if item.get("status") == "won")
    
    print_metric("Total Pipeline", f"${total:,.0f}")
    print_metric("Ready to Send", f"${ready:,.0f}")
    print_metric("Submitted", f"${submitted:,.0f}")
    print_metric("Won", f"${won:,.0f}")
    
    if total > 0:
        conversion = won / total * 100
        execution_gap = (total - submitted) / total * 100
    else:
        conversion = 0
        execution_gap = 0
    
    print()
    print_bar("Submitted", submitted, total)
    print_bar("Won", won, total)
    print()
    print_metric("Conversion Rate", f"{conversion:.1f}", "%")
    print_metric("Execution Gap", f"{execution_gap:.1f}", "%")
    
    # By category
    print_header("BY CATEGORY")
    categories = {}
    for item in items:
        cat = item.get("category", "unknown")
        if cat not in categories:
            categories[cat] = {"total": 0, "ready": 0, "submitted": 0, "won": 0}
        categories[cat]["total"] += item.get("value", 0)
        status = item.get("status", "unknown")
        if status in ("ready", "ready_to_submit"):
            categories[cat]["ready"] += item.get("value", 0)
        elif status in categories[cat]:
            categories[cat][status] += item.get("value", 0)
    
    for cat, vals in sorted(categories.items(), key=lambda x: x[1]["total"], reverse=True):
        print(f"\n  {cat.upper()}")
        print(f"    Total: ${vals['total']:,.0f}")
        print(f"    Progress: Ready ${vals['ready']:,.0f} | Submitted ${vals['submitted']:,.0f} | Won ${vals['won']:,.0f}")
    
    # Recent activity
    print_header("RECENT ACTIVITY")
    
    recent = []
    for item in items:
        if "updated" in item:
            try:
                updated = datetime.fromisoformat(item["updated"])
                # Make naive if aware (strip timezone)
                if updated.tzinfo:
                    updated = updated.replace(tzinfo=None)
                name = item.get("name", "Unknown")
                recent.append((updated, name, item))
            except:
                pass
    
    recent.sort(reverse=True)
    
    if recent:
        for updated, name, item in recent[:10]:
            ago = (now - updated).total_seconds() / 3600
            status = item.get("status", "unknown")
            symbol = {"ready": "⏳", "ready_to_submit": "⏳", "submitted": "📤", "won": "✅", "lost": "❌"}.get(status, "?")
            print(f"  {symbol} {name[:30]:30} | {status:12} | {ago:5.1f}h ago")
    else:
        print("  No recent updates")
    
    # Top opportunities
    print_header("TOP 5 OPPORTUNITIES (READY)")
    
    ready_items = [i for i in items if i.get("status") in ("ready", "ready_to_submit")]
    ready_items.sort(key=lambda x: x.get("value", 0), reverse=True)
    
    for item in ready_items[:5]:
        name = item.get("name", "Unknown")
        value = item.get("value", 0)
        cat = item.get("category", "unknown")
        print(f"  ${value:>10,.0f} | {cat:10} | {name[:35]}")
    
    # Action items
    print_header("ACTION ITEMS")
    
    action_count = len([i for i in items if i.get("status") in ("ready", "ready_to_submit")])
    
    if action_count > 0:
        print(f"  ⚠️  {action_count} items ready to send (${ready:,.0f})")
        print(f"     Estimated time: {action_count * 0.5:.0f} minutes")
        print(f"     Potential value: ${ready:,.0f}")
    else:
        print("  ✅ All caught up! Nothing ready to send.")
    
    print()
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
