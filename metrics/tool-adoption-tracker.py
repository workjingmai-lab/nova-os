#!/usr/bin/env python3
"""
Tool Adoption Tracker
Track how other agents use and engage with shared tools
"""

import json
from datetime import datetime
from pathlib import Path

METRICS_FILE = Path(__file__).parent.parent / "metrics" / "tool_adoption.json"

def load_metrics():
    """Load existing metrics or create new structure"""
    if METRICS_FILE.exists():
        with open(METRICS_FILE, 'r') as f:
            return json.load(f)
    return {
        "created": datetime.now().isoformat(),
        "tools": {},
        "last_updated": None
    }

def save_metrics(metrics):
    """Save metrics to file"""
    metrics["last_updated"] = datetime.now().isoformat()
    METRICS_FILE.parent.mkdir(exist_ok=True)
    with open(METRICS_FILE, 'w') as f:
        json.dump(metrics, f, indent=2)

def register_tool(tool_name, description, share_date):
    """Register a new shared tool"""
    metrics = load_metrics()
    metrics["tools"][tool_name] = {
        "description": description,
        "share_date": share_date,
        "shares": [],  # Where it was posted
        "engagement": {
            "views": 0,
            "reactions": 0,
            "comments": 0,
            "downloads": 0,
            "mentions": 0
        },
        "feedback": []
    }
    save_metrics(metrics)
    print(f"✅ Tool registered: {tool_name}")

def record_share(tool_name, platform, post_url=None):
    """Record where tool was shared"""
    metrics = load_metrics()
    if tool_name not in metrics["tools"]:
        print(f"❌ Tool not found: {tool_name}")
        return

    metrics["tools"][tool_name]["shares"].append({
        "platform": platform,
        "url": post_url,
        "date": datetime.now().isoformat()
    })
    save_metrics(metrics)
    print(f"✅ Share recorded: {tool_name} → {platform}")

def record_engagement(tool_name, engagement_type, count=1):
    """Record engagement metrics"""
    metrics = load_metrics()
    if tool_name not in metrics["tools"]:
        print(f"❌ Tool not found: {tool_name}")
        return

    valid_types = ["views", "reactions", "comments", "downloads", "mentions"]
    if engagement_type not in valid_types:
        print(f"❌ Invalid type: {engagement_type}")
        return

    metrics["tools"][tool_name]["engagement"][engagement_type] += count
    save_metrics(metrics)
    print(f"✅ Engagement recorded: {tool_name} +{count} {engagement_type}")

def add_feedback(tool_name, feedback, agent=None):
    """Add user feedback"""
    metrics = load_metrics()
    if tool_name not in metrics["tools"]:
        print(f"❌ Tool not found: {tool_name}")
        return

    metrics["tools"][tool_name]["feedback"].append({
        "feedback": feedback,
        "agent": agent,
        "date": datetime.now().isoformat()
    })
    save_metrics(metrics)
    print(f"✅ Feedback added: {tool_name}")

def show_report():
    """Show adoption report"""
    metrics = load_metrics()
    print("\n📊 TOOL ADOPTION REPORT")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 50)

    if not metrics["tools"]:
        print("No tools tracked yet.")
        return

    for tool_name, data in metrics["tools"].items():
        print(f"\n🔧 {tool_name}")
        print(f"   Description: {data['description']}")
        print(f"   Shared: {data['share_date']}")
        print(f"   Platforms: {len(data['shares'])}")
        print(f"   Engagement:")
        e = data['engagement']
        print(f"      Views: {e['views']} | Reactions: {e['reactions']} | Comments: {e['comments']}")
        print(f"      Downloads: {e['downloads']} | Mentions: {e['mentions']}")
        if data['feedback']:
            print(f"   Feedback ({len(data['feedback'])}):")
            for fb in data['feedback'][-3:]:  # Last 3
                agent_str = f"({fb['agent']})" if fb['agent'] else ""
                print(f"      - {fb['feedback']} {agent_str}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        show_report()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "register" and len(sys.argv) >= 4:
        register_tool(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else datetime.now().isoformat())

    elif cmd == "share" and len(sys.argv) >= 4:
        record_share(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)

    elif cmd == "engage" and len(sys.argv) >= 4:
        record_engagement(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 1)

    elif cmd == "feedback" and len(sys.argv) >= 3:
        add_feedback(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)

    else:
        print("Usage:")
        print("  python3 tool-adoption-tracker.py                    # Show report")
        print("  python3 tool-adoption-tracker.py register <name> <desc> <date>")
        print("  python3 tool-adoption-tracker.py share <name> <platform> [url]")
        print("  python3 tool-adoption-tracker.py engage <name> <type> [count]")
        print("  python3 tool-adoption-tracker.py feedback <name> <feedback> [agent]")
