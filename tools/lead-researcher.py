#!/usr/bin/env python3
"""
lead-researcher.py — Find and qualify potential outreach leads

Scans platforms (Moltbook, GitHub, etc.) for agents/developers interested in:
- Agent development
- Automation workflows
- OpenClaw or similar frameworks
- Multi-agent systems

Outputs qualified leads with contact info and personalization hooks.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
WORKSPACE = Path("/home/node/.openclaw/workspace")
LEADS_FILE = WORKSPACE / "data/outreach/leads.json"
OUTPUT_DIR = WORKSPACE / "outreach/leads-research"

# Lead qualification criteria
QUALIFICATION_CHECKLIST = {
    "high_intent": [
        "recently posted about automation/agents",
        "active developer/creator",
        "visible pain point in recent posts",
        "expressed interest in agent frameworks"
    ],
    "medium_intent": [
        "runs active projects but no recent posts",
        "github activity suggests agent work",
        "active in relevant communities"
    ],
    "low_intent": [
        "generic dev with no specific automation need",
        "no recent activity",
        "wrong fit for services"
    ]
}

# Platforms to research
PLATFORMS = {
    "moltbook": {
        "url": "https://www.moltbook.com",
        "search_queries": [
            "agent development",
            "automation",
            "openclaw",
            "multi-agent",
            "autonomous"
        ],
        "api_available": True
    },
    "github": {
        "url": "https://github.com",
        "search_queries": [
            "openclaw",
            "agent framework",
            "autonomous agents",
            "automation tools"
        ],
        "api_available": True  # Need gh auth
    },
    "discord": {
        "url": "N/A",
        "search_queries": [],
        "api_available": False,
        "note": "Manual research required"
    }
}

# Lead types and message templates
LEAD_TYPES = {
    "technical": {
        "template": "OpenClaw Setup / Technical Collaboration",
        "price_range": "$3-5K",
        "timeline": "1-2 weeks"
    },
    "automation": {
        "template": "Quick Automation",
        "price_range": "$1-2K",
        "timeline": "3-5 days"
    },
    "multi_agent": {
        "template": "Multi-Agent System",
        "price_range": "$10-25K",
        "timeline": "2-4 weeks"
    },
    "content": {
        "template": "Content Automation",
        "price_range": "$1-2K",
        "timeline": "3-5 days"
    }
}


def load_existing_leads():
    """Load existing leads to avoid duplicates."""
    try:
        with open(LEADS_FILE, 'r') as f:
            data = json.load(f)
            return {lead['name']: lead for lead in data.get('leads', [])}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def research_moltbook_agents():
    """
    Research Moltbook for potential leads.

    Strategy: Use moltbook-monitor.py to scan feed for agent-related posts,
    extract author info, qualify based on content.
    """
    print("🔍 Researching Moltbook for agent developers...")

    # Check if moltbook-suite can help
    try:
        import subprocess
        result = subprocess.run(
            ["python3", "tools/moltbook-suite.py", "analyze", "--list-agents"],
            capture_output=True,
            text=True,
            cwd=WORKSPACE
        )

        if result.returncode == 0:
            print("✅ Found existing agent tracking data")
            print(result.stdout)
            return parse_moltbook_agents(result.stdout)
    except Exception as e:
        print(f"⚠️  Could not analyze Moltbook: {e}")

    return []


def parse_moltbook_agents(output: str) -> list:
    """Parse moltbook-suite analyze output for potential leads."""
    leads = []

    # TODO: Implement parsing logic
    # For now, return empty list
    print("📝 Agent parsing not yet implemented")
    return leads


def qualify_lead(name: str, platform: str, context: str) -> dict:
    """
    Determine if a lead qualifies for outreach.

    Returns lead dict with qualification score and type.
    """
    # Check against qualification criteria
    score = 0
    lead_type = "unknown"

    context_lower = context.lower()

    # High intent signals
    for signal in QUALIFICATION_CHECKLIST["high_intent"]:
        if any(keyword in context_lower for keyword in signal.split()):
            score += 3

    # Determine lead type based on context
    if "multi-agent" in context_lower or "coordination" in context_lower:
        lead_type = "multi_agent"
    elif "developer" in context_lower or "technical" in context_lower:
        lead_type = "technical"
    elif "content" in context_lower or "creative" in context_lower:
        lead_type = "content"
    elif "automation" in context_lower:
        lead_type = "automation"

    return {
        "name": name,
        "platform": platform,
        "type": lead_type,
        "score": score,
        "context": context,
        "status": "identified" if score >= 3 else "research_needed"
    }


def generate_research_report(leads: list) -> str:
    """Generate a research report with recommendations."""
    report = []
    report.append("# Lead Research Report")
    report.append(f"\nGenerated: {datetime.now().isoformat()}")
    report.append(f"\nTotal leads found: {len(leads)}")

    # Categorize by qualification
    high_quality = [l for l in leads if l.get('score', 0) >= 6]
    medium_quality = [l for l in leads if 3 <= l.get('score', 0) < 6]
    low_quality = [l for l in leads if l.get('score', 0) < 3]

    report.append(f"\n🎯 High Quality (score ≥6): {len(high_quality)}")
    report.append(f"📊 Medium Quality (score 3-5): {len(medium_quality)}")
    report.append(f"⏳ Low Quality (score <3): {len(low_quality)}")

    if high_quality:
        report.append("\n## High-Quality Leads (Prioritize)")
        for lead in high_quality:
            report.append(f"\n- **{lead['name']}** ({lead['platform']})")
            report.append(f"  Type: {lead['type']}")
            report.append(f"  Context: {lead['context'][:100]}...")

    return "\n".join(report)


def main():
    """Main research workflow."""
    print("🔍 Lead Research Tool\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing leads to avoid duplicates
    existing_leads = load_existing_leads()
    print(f"📋 Existing leads: {len(existing_leads)}")

    # Research Moltbook
    moltbook_leads = research_moltbook_agents()

    # TODO: Research GitHub (when gh auth available)
    # TODO: Research Discord (manual)

    # Qualify leads
    qualified_leads = []
    for lead_data in moltbook_leads:
        qualified = qualify_lead(
            lead_data.get('name', 'Unknown'),
            lead_data.get('platform', 'moltbook'),
            lead_data.get('context', '')
        )
        qualified_leads.append(qualified)

    # Generate report
    if qualified_leads:
        report = generate_research_report(qualified_leads)

        # Save report
        report_file = OUTPUT_DIR / f"research-{datetime.now().strftime('%Y%m%d-%H%M')}.md"
        with open(report_file, 'w') as f:
            f.write(report)

        print(f"\n✅ Research complete: {report_file}")
        print(report)
    else:
        print("\n⚠️  No new leads found")

    print("\n💡 Next steps:")
    print("1. Review qualified leads")
    print("2. Customize outreach messages")
    print("3. Send via appropriate channel")
    print("4. Track responses in leads.json")


if __name__ == "__main__":
    main()
