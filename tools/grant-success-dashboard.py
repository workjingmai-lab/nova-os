#!/usr/bin/env python3
"""
grant-success-dashboard.py — Nova's Grant Tracking Dashboard
Real-time view of grant pipeline, deadlines, and success metrics.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List

# Color codes for terminal output
class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"

GRANT_DATA = {
    "W3F Open Grants": {
        "status": "submitted",
        "amount": "$10-50K",
        "submitted_date": "2026-01-31",
        "next_action": "Await response",
        "priority": "high",
        "deadline": None,
        "contact": "grants@web3.foundation",
        "notes": "Focus on security research and Ethernaut exploits"
    },
    "Ethereum Foundation ESP": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "GitHub auth required (code: 80BB-6F1E)",
        "priority": "high",
        "deadline": "Rolling - ESP open monthly",
        "contact": "esp@ethereum.org",
        "notes": "Need Arthur to provide new GitHub PAT"
    },
    "Arbitrum DAO STIP": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "Forum post required",
        "priority": "high",
        "deadline": "Check STIP round dates",
        "contact": "https://governance.arbitrum.io",
        "notes": "Need to create Arbitrum forum account"
    },
    "Gitcoin Grants": {
        "status": "ready_to_submit",
        "amount": "$15K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Rolling - next round",
        "contact": "https://gitcoin.co/grants",
        "notes": "Quick win once accounts ready"
    },
    "Optimism RetroPGF": {
        "status": "ready_to_submit",
        "amount": "$20K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Next round TBD",
        "contact": "https://gov.optimism.io",
        "notes": "High prestige, good for credibility"
    },
    "Aave Grants DAO": {
        "status": "ready_to_submit",
        "amount": "$25K",
        "submitted_date": None,
        "next_action": "Final review & submit",
        "priority": "medium",
        "deadline": "Rolling",
        "contact": "https://aavegrants.org",
        "notes": "DeFi ecosystem alignment, drafted 2026-02-01"
    }
}

def get_status_color(status: str) -> str:
    """Get color for status."""
    if status == "submitted":
        return Colors.GREEN
    elif status == "ready_to_submit":
        return Colors.YELLOW
    elif status == "rejected":
        return Colors.RED
    else:
        return Colors.BLUE

def format_grant_row(name: str, data: Dict) -> str:
    """Format a single grant row."""
    status_color = get_status_color(data["status"])
    status_icon = {
        "submitted": "✅",
        "ready_to_submit": "📝",
        "rejected": "❌",
        "accepted": "🎉"
    }.get(data["status"], "❓")
    
    return f"""
{status_icon} {Colors.BOLD}{name}{Colors.END} ({data['amount']})
   Status: {status_color}{data['status'].upper().replace('_', ' ')}{Colors.END}
   Priority: {data['priority'].upper()}
   Next Action: {data['next_action']}
   Deadline: {data['deadline'] or 'No deadline'}
"""

def calculate_metrics() -> Dict:
    """Calculate grant pipeline metrics."""
    total = len(GRANT_DATA)
    submitted = sum(1 for g in GRANT_DATA.values() if g["status"] == "submitted")
    ready = sum(1 for g in GRANT_DATA.values() if g["status"] == "ready_to_submit")
    
    # Calculate total pipeline value
    submitted_value = "10-50K"  # W3F range
    pending_value = sum(
        int(g["amount"].replace("$", "").replace("K", "000"))
        for g in GRANT_DATA.values()
        if g["status"] == "ready_to_submit"
    )
    
    return {
        "total": total,
        "submitted": submitted,
        "ready": ready,
        "completion_rate": round((submitted / total) * 100, 1),
        "submitted_value": submitted_value,
        "pending_value": f"${pending_value:,}",
        "total_pipeline": f"{submitted_value} + ${pending_value:,}"
    }

def display_dashboard():
    """Display the grant success dashboard."""
    print(f"""
{Colors.BOLD}╔══════════════════════════════════════════════════════════════╗
║         🎯 GRANT SUCCESS DASHBOARD — Nova's Pipeline          ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.BLUE}Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}{Colors.END}
{Colors.BLUE}Work Blocks Completed: 90{Colors.END}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.BOLD}📊 PIPELINE METRICS{Colors.END}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    metrics = calculate_metrics()
    print(f"""Total Grants:  {Colors.BOLD}{metrics['total']}{Colors.END}
Submitted:     {Colors.GREEN}{metrics['submitted']}{Colors.END} / {metrics['total']}
Ready:         {Colors.YELLOW}{metrics['ready']}{Colors.END} / {metrics['total']}
Completion:    {metrics['completion_rate']}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.BOLD}💰 PIPELINE VALUE{Colors.END}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Submitted:     {Colors.GREEN}{metrics['submitted_value']}{Colors.END}
Pending:       {Colors.YELLOW}{metrics['pending_value']}{Colors.END}
Total:         {Colors.BOLD}{metrics['total_pipeline']}{Colors.END}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.BOLD}📝 GRANT DETAILS{Colors.END}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    # Sort by priority (high first) then status
    sorted_grants = sorted(
        GRANT_DATA.items(),
        key=lambda x: (
            0 if x[1]["priority"] == "high" else 1,
            0 if x[1]["status"] == "submitted" else 1
        )
    )

    for name, data in sorted_grants:
        print(format_grant_row(name, data))

    print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.BOLD}⚡ IMMEDIATE ACTIONS (Blockers){Colors.END}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.YELLOW}→ Arthur: Provide new GitHub PAT (EF ESP needs code: 80BB-6F1E){Colors.END}
{Colors.YELLOW}→ Arthur: Create Arbitrum forum account for STIP submission{Colors.END}
{Colors.YELLOW}→ Nova: Final review of all 5 pending grants{Colors.END}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.BOLD}🎯 WEEK 2 TARGET{Colors.END}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Submit all 5 pending grants by Wed 2026-02-04
Get at least 1 grant accepted to next round
Secure first funding milestone

{Colors.BOLD}Let's make it happen. 🔥{Colors.END}
""")

def save_dashboard_snapshot():
    """Save dashboard data to JSON for other tools."""
    output = Path("/home/node/.openclaw/workspace/grants/dashboard-snapshot.json")
    
    metrics = calculate_metrics()
    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "metrics": metrics,
        "grants": GRANT_DATA,
        "blockers": [
            "GitHub auth for EF ESP (code: 80BB-6F1E)",
            "Arbitrum forum account needed"
        ],
        "next_actions": [
            "Arthur: Provide new GitHub PAT",
            "Arthur: Create Arbitrum forum account",
            "Nova: Final review of 5 pending grants"
        ]
    }
    
    output.write_text(json.dumps(snapshot, indent=2))
    print(f"\n{Colors.GREEN}✅ Dashboard snapshot saved to {output}{Colors.END}")

if __name__ == "__main__":
    display_dashboard()
    save_dashboard_snapshot()
