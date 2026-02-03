#!/usr/bin/env python3
"""
Service Outreach Response Tracker
Tracks outbound service proposals and monitors responses
"""

import json
from datetime import datetime
from pathlib import Path

TRACKER_FILE = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")

def load_tracker():
    """Load or initialize tracker"""
    if TRACKER_FILE.exists():
        with open(TRACKER_FILE) as f:
            return json.load(f)
    return {
        "lastUpdated": None,
        "totalSent": 0,
        "totalReplies": 0,
        "conversionRate": 0.0,
        "messages": []
    }

def save_tracker(data):
    """Save tracker data"""
    data["lastUpdated"] = datetime.utcnow().isoformat() + "Z"
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_sent(prospect, service_type, amount_range, message_preview):
    """Log a sent message"""
    data = load_tracker()
    data["messages"].append({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "prospect": prospect,
        "serviceType": service_type,
        "amountRange": amount_range,
        "messagePreview": message_preview[:100] + "..." if len(message_preview) > 100 else message_preview,
        "status": "sent",
        "response": None
    })
    data["totalSent"] = len(data["messages"])
    data["conversionRate"] = (data["totalReplies"] / data["totalSent"] * 100) if data["totalSent"] > 0 else 0
    save_tracker(data)
    return data

def log_reply(prospect, response_type, notes):
    """Log a response to a sent message"""
    data = load_tracker()
    for msg in reversed(data["messages"]):  # Check most recent first
        if msg["prospect"] == prospect and msg["status"] == "sent":
            msg["status"] = "replied"
            msg["response"] = {
                "type": response_type,  # interested, declined, negotiating, follow_up
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "notes": notes
            }
            data["totalReplies"] = sum(1 for m in data["messages"] if m["status"] in ["replied", "negotiating", "won"])
            data["conversionRate"] = (data["totalReplies"] / data["totalSent"] * 100) if data["totalSent"] > 0 else 0
            save_tracker(data)
            return msg
    return None

def get_summary():
    """Get outreach summary"""
    data = load_tracker()
    pending = sum(1 for m in data["messages"] if m["status"] == "sent")
    replied = data["totalReplies"]
    return {
        "sent": data["totalSent"],
        "pending": pending,
        "replied": replied,
        "conversionRate": data["conversionRate"],
        "lastUpdated": data["lastUpdated"]
    }

def get_pending_followups(hours_threshold=48):
    """Get messages needing follow-up"""
    data = load_tracker()
    now = datetime.utcnow()
    pending = []
    for msg in data["messages"]:
        if msg["status"] == "sent":
            sent_time = datetime.fromisoformat(msg["timestamp"].replace("Z", ""))
            hours_since = (now - sent_time).total_seconds() / 3600
            if hours_since >= hours_threshold:
                pending.append({
                    "prospect": msg["prospect"],
                    "hours_since": round(hours_since, 1),
                    "serviceType": msg["serviceType"]
                })
    return pending

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"

    if cmd == "summary":
        summary = get_summary()
        print(f"📊 Outreach Summary:")
        print(f"   Sent: {summary['sent']}")
        print(f"   Pending: {summary['pending']}")
        print(f"   Replied: {summary['replied']}")
        print(f"   Conversion: {summary['conversionRate']:.1f}%")

    elif cmd == "pending":
        pending = get_pending_followups()
        if pending:
            print(f"⏰ Follow-ups needed ({len(pending)}):")
            for p in pending:
                print(f"   {p['prospect']} — {p['hours_since']}h ago — {p['serviceType']}")
        else:
            print("✅ No follow-ups needed yet")

    elif cmd == "log":
        # Usage: python service-outreach-tracker.py log "Prospect" "Service Type" "$1-2K" "Message..."
        if len(sys.argv) >= 5:
            log_sent(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")
            print(f"✅ Logged outreach to {sys.argv[2]}")
