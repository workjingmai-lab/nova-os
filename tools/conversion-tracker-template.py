#!/usr/bin/env python3
"""
Conversion Tracker Template - Track responses → revenue
Monitor the journey from sent message to closed deal
"""

import json
from datetime import datetime, timezone
from pathlib import Path

CONVERSION_FILE = Path(__file__).parent.parent / "revenue-pipeline.json"
TRACKING_FILE = Path(__file__).parent.parent / "conversion-tracking.json"

def load_conversion_data():
    """Load existing conversion tracking data"""
    if TRACKING_FILE.exists():
        with open(TRACKING_FILE, 'r') as f:
            return json.load(f)
    return {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "last_updated": None,
        "metrics": {
            "sent": 0,
            "replies": 0,
            "calls_scheduled": 0,
            "proposals_sent": 0,
            "deals_won": 0,
            "deals_lost": 0
        },
        "funnel": {
            "reply_rate": 0.0,
            "call_rate": 0.0,
            "proposal_rate": 0.0,
            "close_rate": 0.0,
            "overall_conversion": 0.0
        },
        "responses": []
    }

def save_conversion_data(data):
    """Save conversion tracking data"""
    data["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(TRACKING_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def record_response(message_id, response_type, notes=""):
    """Record a response to a sent message
    Types: interested, not_interested, no_response, call_scheduled, proposal_sent, won, lost
    """
    data = load_conversion_data()
    
    response = {
        "message_id": message_id,
        "response_type": response_type,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "notes": notes
    }
    
    data["responses"].append(response)
    save_conversion_data(data)
    
    return f"✅ Response recorded: {message_id} → {response_type}"

def calculate_metrics():
    """Calculate conversion funnel metrics"""
    data = load_conversion_data()
    m = data["metrics"]
    
    sent = m["sent"] or 1  # Avoid division by zero
    m["funnel"] = {
        "reply_rate": round((m["replies"] / sent) * 100, 1),
        "call_rate": round((m["calls_scheduled"] / max(m["replies"], 1)) * 100, 1),
        "proposal_rate": round((m["proposals_sent"] / max(m["calls_scheduled"], 1)) * 100, 1),
        "close_rate": round((m["deals_won"] / max(m["proposals_sent"], 1)) * 100, 1),
        "overall_conversion": round((m["deals_won"] / sent) * 100, 1)
    }
    
    save_conversion_data(data)
    return data["funnel"]

def export_summary():
    """Export conversion summary for diary/log"""
    data = load_conversion_data()
    m = data["metrics"]
    f = data["funnel"]
    
    summary = f"""
📊 CONVERSION TRACKING SUMMARY
{"=" * 50}
Started: {data['started_at'][:10]}
Last Updated: {data['last_updated'][:10] if data['last_updated'] else 'Never'}

METRICS:
  Sent: {m['sent']}
  Replies: {m['replies']} ({f['reply_rate']}%)
  Calls: {m['calls_scheduled']} ({f['call_rate']}%)
  Proposals: {m['proposals_sent']} ({f['proposal_rate']}%)
  Won: {m['deals_won']} ({f['close_rate']}%)
  Lost: {m['deals_lost']}

OVERALL CONVERSION: {f['overall_conversion']}%

TARGETS (realistic):
  Reply rate: 15-25% (Current: {f['reply_rate']}%)
  Call rate: 40-60% (Current: {f['call_rate']}%)
  Proposal rate: 60-80% (Current: {f['proposal_rate']}%)
  Close rate: 30-50% (Current: {f['close_rate']}%)
  Overall: 5-10% (Current: {f['overall_conversion']}%)
"""
    return summary

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print(export_summary())
    elif sys.argv[1] == "record":
        if len(sys.argv) < 4:
            print("Usage: python3 conversion-tracker-template.py record <message_id> <response_type> [notes]")
        else:
            print(record_response(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else ""))
    elif sys.argv[1] == "metrics":
        metrics = calculate_metrics()
        print(json.dumps(metrics, indent=2))
    elif sys.argv[1] == "summary":
        print(export_summary())
    else:
        print("Usage:")
        print("  python3 conversion-tracker-template.py summary")
        print("  python3 conversion-tracker-template.py record <message_id> <response_type> [notes]")
        print("  python3 conversion-tracker-template.py metrics")
