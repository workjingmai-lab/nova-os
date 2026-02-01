#!/usr/bin/env python3
"""
Grant Success Dashboard — Nova
Visual tracking of grant application status, deadlines, and next actions.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
WORKSPACE = Path.home() / ".openclaw" / "workspace"
TRACKER_FILE = WORKSPACE / "grants" / "submission-tracker.md"
DASHBOARD_FILE = WORKSPACE / "grants" / "dashboard-status.json"

# Grant data structure
GRANT_DATA = {
    "W3F Open Grants": {
        "status": "submitted",
        "amount": "$10-50K",
        "submitted_date": "2026-01-31",
        "next_action": "Await response",
        "priority": "high",
        "deadline": None
    },
    "Ethereum Foundation ESP": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "GitHub auth required (code: 80BB-6F1E)",
        "priority": "high",
        "deadline": "Rolling - ESP open monthly"
    },
    "Arbitrum DAO STIP": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "Forum post required",
        "priority": "high",
        "deadline": "Check STIP round dates"
    },
    "Gitcoin Grants": {
        "status": "ready_to_submit",
        "amount": "$15K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Rolling - next round"
    },
    "Optimism RetroPGF": {
        "status": "ready_to_submit",
        "amount": "$20K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Next round TBD"
    },
    "Aave Grants DAO": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Rolling"
    }
}

def calculate_metrics():
    """Calculate key metrics."""
    total = len(GRANT_DATA)
    submitted = sum(1 for g in GRANT_DATA.values() if g["status"] == "submitted")
    ready = sum(1 for g in GRANT_DATA.values() if g["status"] == "ready_to_submit")
    total_value = {
        "submitted": "$10-50K",
        "pending": "$110K",
        "total_pipeline": "$120-160K"
    }
    return {
        "total_grants": total,
        "submitted": submitted,
        "ready": ready,
        "completion_rate": round((submitted / total) * 100, 1),
        "total_value": total_value
    }

def generate_dashboard():
    """Generate dashboard as text and JSON."""
    metrics = calculate_metrics()
    now = datetime.now().isoformat()

    dashboard = {
        "generated_at": now,
        "metrics": metrics,
        "grants": GRANT_DATA,
        "summary": {
            "blockers": [
                "GitHub auth for EF ESP (code: 80BB-6F1E)",
                "Arbitrum forum account needed"
            ],
            "immediate_actions": [
                "Arthur: Revoke old PAT → create new → provide to Nova",
                "Create Arbitrum forum account",
                "Final review of all 5 pending grants"
            ],
            "this_week": [
                "Submit EF ESP grant (pending GitHub auth)",
                "Submit Arbitrum grant (pending forum account)",
                "Submit Gitcoin, Optimism, Aave grants"
            ]
        }
    }

    # Save JSON
    DASHBOARD_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DASHBOARD_FILE, 'w') as f:
        json.dump(dashboard, f, indent=2)

    return dashboard

def print_dashboard():
    """Print human-readable dashboard."""
    dashboard = generate_dashboard()
    metrics = dashboard["metrics"]

    print("\n" + "="*60)
    print("🎯 GRANT SUCCESS DASHBOARD — Nova")
    print("="*60)
    print(f"\n📊 Metrics:")
    print(f"   Total Grants: {metrics['total_grants']}")
    print(f"   Submitted: {metrics['submitted']}")
    print(f"   Ready: {metrics['ready']}")
    print(f"   Completion: {metrics['completion_rate']}%")
    print(f"\n💰 Pipeline Value:")
    print(f"   Submitted: {metrics['total_value']['submitted']}")
    print(f"   Pending: {metrics['total_value']['pending']}")
    print(f"   Total: {metrics['total_value']['total_pipeline']}")

    print(f"\n🎯 Grant Status:")
    for name, data in GRANT_DATA.items():
        status_icon = "✅" if data["status"] == "submitted" else "📝"
        priority = data["priority"].upper()
        print(f"\n   {status_icon} {name}")
        print(f"      Amount: {data['amount']}")
        print(f"      Status: {data['status']}")
        print(f"      Next: {data['next_action']}")
        if data['deadline']:
            print(f"      Deadline: {data['deadline']}")

    print(f"\n🚧 Blockers:")
    for blocker in dashboard["summary"]["blockers"]:
        print(f"   • {blocker}")

    print(f"\n⚡ Immediate Actions:")
    for action in dashboard["summary"]["immediate_actions"]:
        print(f"   • {action}")

    print(f"\n📅 This Week:")
    for task in dashboard["summary"]["this_week"]:
        print(f"   • {task}")

    print("\n" + "="*60 + "\n")

    print(f"✅ Dashboard saved to: {DASHBOARD_FILE}")

if __name__ == "__main__":
    print_dashboard()
