#!/usr/bin/env python3
"""
week3-tracker.py — Week 3 revenue conversion tracker
Tracks pipeline movement: ready → sent → submitted → won/lost
"""

import json
from datetime import datetime

WEEK3_START = "2026-02-08"
WEEK3_END = "2026-02-14"

def load_pipeline():
    """Load current pipeline data"""
    try:
        with open("revenue-pipeline.json") as f:
            return json.load(f)
    except:
        return {"opportunities": []}

def main():
    data = load_pipeline()
    ops = data.get("opportunities", [])
    
    # Count by status
    ready = [o for o in ops if o.get("status") == "ready"]
    sent = [o for o in ops if o.get("status") == "sent"]
    submitted = [o for o in ops if o.get("status") == "submitted"]
    won = [o for o in ops if o.get("status") == "won"]
    lost = [o for o in ops if o.get("status") == "lost"]
    
    # Value totals
    ready_val = sum(o.get("value", 0) for o in ready)
    sent_val = sum(o.get("value", 0) for o in sent)
    submitted_val = sum(o.get("value", 0) for o in submitted)
    won_val = sum(o.get("value", 0) for o in won)
    
    # Output
    print(f"📈 Week 3 Pipeline Tracker")
    print(f"   Period: {WEEK3_START} to {WEEK3_END}")
    print(f"   Today:  {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")
    print()
    print(f"   ┌─────────────┬────────┬───────────┐")
    print(f"   │ Status      │ Count  │ Value     │")
    print(f"   ├─────────────┼────────┼───────────┤")
    print(f"   │ 💰 Ready    │ {len(ready):>6} │ ${ready_val:>8,} │")
    print(f"   │ 📤 Sent     │ {len(sent):>6} │ ${sent_val:>8,} │")
    print(f"   │ 📋 Submitted│ {len(submitted):>6} │ ${submitted_val:>8,} │")
    print(f"   │ ✅ Won      │ {len(won):>6} │ ${won_val:>8,} │")
    print(f"   │ ❌ Lost     │ {len(lost):>6} │ {'—':>9} │")
    print(f"   └─────────────┴────────┴───────────┘")
    print()
    
    total = ready_val + sent_val + submitted_val + won_val
    print(f"   Total Pipeline: ${total:,}")
    print(f"   Conversion:     {len(won)} won / {len(lost)} lost")
    
    if submitted_val > 0:
        print(f"\n   🎯 Week 3 Goal: Move $250K from ready → submitted")
        print(f"      Progress: ${submitted_val:,} / $250K ({submitted_val/2500:.1f}%)")

if __name__ == "__main__":
    main()
