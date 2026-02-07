#!/usr/bin/env python3
"""
Lead Scoring System
Prioritize leads based on fit, urgency, value, and signal strength
Usage: python3 tools/lead-scoring.py [score|rank|top<N>]
"""

import json
import sys
from pathlib import Path

# Configuration
PIPELINE_FILE = Path.home() / ".openclaw/workspace" / "revenue-pipeline.json"
LEADS_FILE = Path.home() / ".openclaw/workspace" / "outreach" / "leads.json"

# Scoring weights
WEIGHTS = {
    "value": 0.3,          # Pipeline value (higher = better)
    "fit": 0.25,           # Problem-solution fit (subjective, 1-10)
    "urgency": 0.2,        # Time sensitivity (1-10)
    "signal": 0.15,        # Engagement signal (1-10)
    "competition": 0.1     # Competitor pressure (1-10, higher = more urgent)
}

def load_pipeline():
    """Load revenue pipeline data"""
    if PIPELINE_FILE.exists():
        with open(PIPELINE_FILE, 'r') as f:
            return json.load(f)
    return {"categories": {}, "totalPipeline": 0}

def extract_leads_from_pipeline(pipeline):
    """Extract flat leads list from nested pipeline structure"""
    leads = []
    categories = pipeline.get("categories", {})

    for category_name, category_data in categories.items():
        opportunities = category_data.get("opportunities", [])
        top_prospects = category_data.get("topProspects", [])

        for opp in opportunities + top_prospects:
            lead = {
                "name": opp.get("name", "Unknown"),
                "value": {"min": opp.get("amount", 0), "max": opp.get("amount", 0)},
                "tier": opp.get("priority", "MEDIUM"),
                "priority": opp.get("priority", "MEDIUM"),
                "status": category_data.get("status", "unknown"),
                "category": category_name,
                "fit_score": 5,  # Default, can be overridden
                "urgency_score": 5,  # Default, can be overridden
                "signals": []
            }
            leads.append(lead)

    return leads

def normalize_value(value, min_val, max_val):
    """Normalize value to 0-1 scale"""
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

def score_lead(lead, max_value):
    """Score a single lead (0-100)"""
    scores = {}

    # Value score (0-100)
    value = lead.get("value", {}).get("min", 0)
    scores["value"] = normalize_value(value, 0, max_value) * 100

    # Fit score (1-10 from manual assessment, convert to 0-100)
    scores["fit"] = lead.get("fit_score", 5) * 10

    # Urgency score (1-10 from manual assessment, convert to 0-100)
    scores["urgency"] = lead.get("urgency_score", 5) * 10

    # Signal score (1-10 based on engagement signals)
    signal_indicators = lead.get("signals", [])
    signal_score = len(signal_indicators) * 2  # Each signal = +2 points
    scores["signal"] = min(signal_score, 100)

    # Competition score (1-10 from manual assessment)
    scores["competition"] = lead.get("competition_score", 5) * 10

    # Weighted total
    total = (
        scores["value"] * WEIGHTS["value"] +
        scores["fit"] * WEIGHTS["fit"] +
        scores["urgency"] * WEIGHTS["urgency"] +
        scores["signal"] * WEIGHTS["signal"] +
        scores["competition"] * WEIGHTS["competition"]
    )

    return {
        "name": lead.get("name", "Unknown"),
        "tier": lead.get("tier", "UNKNOWN"),
        "value": lead.get("value", {}),
        "total_score": round(total, 1),
        "breakdown": scores,
        "priority": lead.get("priority", "MEDIUM"),
        "status": lead.get("status", "ready")
    }

def rank_leads():
    """Rank all leads by score"""
    pipeline = load_pipeline()
    leads = extract_leads_from_pipeline(pipeline)

    if not leads:
        print("⚠️  No leads found in pipeline")
        return []

    # Find max value for normalization
    max_value = max(lead.get("value", {}).get("min", 0) for lead in leads)

    # Score all leads
    scored_leads = [score_lead(lead, max_value) for lead in leads]

    # Sort by total score (descending)
    ranked = sorted(scored_leads, key=lambda x: x["total_score"], reverse=True)

    return ranked

def print_ranked_leads(ranked, limit=None):
    """Print ranked leads with scores"""
    if not ranked:
        return

    display_leads = ranked[:limit] if limit else ranked

    print(f"\n📊 Ranked Leads (Top {len(display_leads)} of {len(ranked)})\n")

    for i, lead in enumerate(display_leads, 1):
        value_min = lead['value']['min'] / 1000  # Convert to K
        value_max = lead['value'].get('max', lead['value']['min']) / 1000

        # Format value display
        if value_min == value_max:
            value_str = f"${int(value_min)}K"
        else:
            value_str = f"${int(value_min)}-{int(value_max)}K"

        print(f"{i}. {lead['name']} — Score: {lead['total_score']}/100")
        print(f"   Tier: {lead['tier']} | Value: {value_str}")
        print(f"   Status: {lead['status']} | Priority: {lead['priority']}")
        print(f"   Breakdown:")
        print(f"     • Value: {lead['breakdown']['value']:.1f}/100")
        print(f"     • Fit: {lead['breakdown']['fit']:.1f}/100")
        print(f"     • Urgency: {lead['breakdown']['urgency']:.1f}/100")
        print(f"     • Signal: {lead['breakdown']['signal']:.1f}/100")
        print(f"     • Competition: {lead['breakdown']['competition']:.1f}/100")
        print()

def print_top_n(n=5):
    """Print top N leads only"""
    ranked = rank_leads()
    print_ranked_leads(ranked, limit=n)

def main():
    if len(sys.argv) < 2:
        print("Usage: lead-scoring.py [score|rank|top<N>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "score":
        ranked = rank_leads()
        print_ranked_leads(ranked)

    elif command == "rank":
        ranked = rank_leads()
        print_ranked_leads(ranked)

    elif command.startswith("top"):
        try:
            n = int(command[3:]) or 5
        except ValueError:
            n = 5
        print_top_n(n)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
