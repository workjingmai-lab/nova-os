#!/usr/bin/env python3
"""
Lead Prioritizer — Rank service leads by priority and readiness

Scores leads based on:
- Potential value (higher = better)
- Status (ready > lead > prospect)
- Strategic fit (Web3 > AI > general)
- Execution complexity (quick automation > complex multi-agent)

Usage:
    python3 lead-prioritizer.py --rank
    python3 lead-prioritizer.py --show-ready
    python3 lead-prioritizer.py --top 5
"""

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

# =============================================================================
# CONFIGURATION
# =============================================================================

PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

# Status priority (higher = more urgent)
STATUS_PRIORITY = {
    "ready": 100,
    "ready_to_submit": 90,
    "lead": 50,
    "prospect": 10
}

# Strategic fit multiplier (higher = better fit)
STRATEGIC_FIT = {
    "web3": 1.5,
    "dao": 1.4,
    "ai": 1.3,
    "claude": 1.2,
    "anthropic": 1.2,
    "devops": 1.1,
    "automation": 1.0,
    "general": 0.8
}

# =============================================================================
# FUNCTIONS
# =============================================================================

def load_pipeline():
    """Load revenue pipeline."""
    if PIPELINE_FILE.exists():
        with open(PIPELINE_FILE) as f:
            return json.load(f)
    return {"services": [], "grants": [], "bounties": []}

def score_lead(lead):
    """Calculate priority score for a lead."""
    score = 0

    # Base score from potential value (logarithmic to avoid huge ranges)
    potential = lead.get("potential", 0)
    score += (potential ** 0.5) * 10  # sqrt reduces impact of outliers

    # Status bonus
    status = lead.get("status", "prospect")
    score += STATUS_PRIORITY.get(status, 0)

    # Strategic fit bonus (check notes for keywords)
    notes = lead.get("notes", "").lower()
    fit_multiplier = 1.0
    for keyword, multiplier in STRATEGIC_FIT.items():
        if keyword in notes:
            fit_multiplier = max(fit_multiplier, multiplier)
    score *= fit_multiplier

    # Recency bonus (leads updated in last 7 days get +20)
    if lead.get("updated"):
        try:
            updated = datetime.fromisoformat(lead["updated"])
            # Handle both naive and aware datetimes
            if updated.tzinfo is None:
                updated = updated.replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
            days_old = (now - updated).days
            if days_old < 7:
                score += 20
        except (ValueError, TypeError):
            pass  # Skip if date parsing fails

    return round(score, 2), fit_multiplier

def rank_leads(leads):
    """Rank leads by priority score."""
    scored = []
    for lead in leads:
        score, fit_mult = score_lead(lead)
        scored.append({
            "name": lead.get("name", "Unknown"),
            "potential": lead.get("potential", 0),
            "status": lead.get("status", "unknown"),
            "score": score,
            "fit_multiplier": fit_mult,
            "notes": lead.get("notes", "")[:100] + "..." if len(lead.get("notes", "")) > 100 else lead.get("notes", "")
        })

    return sorted(scored, key=lambda x: x["score"], reverse=True)

def show_ranked(ranked_leads, limit=None):
    """Display ranked leads."""
    if not ranked_leads:
        print("  📭 No leads to rank")
        return

    display_leads = ranked_leads[:limit] if limit else ranked_leads

    print(f"  🎯 Ranked Leads (Top {len(display_leads)}):\n")

    for i, lead in enumerate(display_leads, 1):
        status_icon = {
            "ready": "✅",
            "ready_to_submit": "🟢",
            "lead": "🟡",
            "prospect": "⚪"
        }.get(lead["status"], "❓")

        print(f"  {i}. {status_icon} {lead['name']}")
        print(f"     Potential: ${lead['potential']:,.0f} | Score: {lead['score']:.1f} | Fit: {lead['fit_multiplier']}x")
        print(f"     Status: {lead['status']}")
        if lead['notes'] != "...":
            print(f"     Notes: {lead['notes']}")
        print()

def show_ready(ranked_leads):
    """Show only ready-to-send leads."""
    ready = [l for l in ranked_leads if l["status"] in ["ready", "ready_to_submit"]]

    if not ready:
        print("  ⏳ No leads ready to send")
        return

    print(f"  🚀 Ready to Send ({len(ready)} leads):\n")

    for i, lead in enumerate(ready, 1):
        print(f"  {i}. ✅ {lead['name']}")
        print(f"     ${lead['potential']:,.0f} | Score: {lead['score']:.1f}")
        print()

def calculate_metrics(leads):
    """Calculate pipeline metrics."""
    total_potential = sum(l.get("potential", 0) for l in leads)

    by_status = {}
    for lead in leads:
        status = lead.get("status", "unknown")
        by_status.setdefault(status, []).append(lead)

    status_summary = {}
    for status, status_leads in by_status.items():
        status_potential = sum(l.get("potential", 0) for l in status_leads)
        status_summary[status] = {
            "count": len(status_leads),
            "potential": status_potential
        }

    return {
        "total_leads": len(leads),
        "total_potential": total_potential,
        "by_status": status_summary
    }

def main():
    parser = argparse.ArgumentParser(description="Lead Prioritizer")
    parser.add_argument("--rank", action="store_true", help="Rank all leads by priority")
    parser.add_argument("--show-ready", action="store_true", help="Show only ready-to-send leads")
    parser.add_argument("--top", type=int, help="Show top N leads")
    parser.add_argument("--metrics", action="store_true", help="Show pipeline metrics")

    args = parser.parse_args()

    pipeline = load_pipeline()
    leads = pipeline.get("services", [])

    if not leads:
        print("  📭 No service leads in pipeline")
        return

    ranked = rank_leads(leads)

    if args.rank:
        show_ranked(ranked, args.top)

    elif args.show_ready:
        show_ready(ranked)

    elif args.metrics:
        metrics = calculate_metrics(leads)

        print("  📊 Pipeline Metrics:\n")
        print(f"  Total Leads: {metrics['total_leads']}")
        print(f"  Total Potential: ${metrics['total_potential']:,.0f}\n")

        print("  By Status:")
        for status, data in metrics['by_status'].items():
            icon = {
                "ready": "✅",
                "ready_to_submit": "🟢",
                "lead": "🟡",
                "prospect": "⚪"
            }.get(status, "❓")
            print(f"    {icon} {status}: {data['count']} leads, ${data['potential']:,.0f}")

    else:
        # Default: show top 10
        show_ranked(ranked, 10)

if __name__ == "__main__":
    main()
