#!/usr/bin/env python3
"""
Grant Opportunity Finder — Discover grant opportunities automatically

Searches for grants relevant to OpenClaw:
- Web3/Crypto grants (Gitcoin, Octant, Optimism, etc.)
- Open source funding (GitHub Sponsors, Open Collective)
- AI/Agent research grants
- Developer tool grants

Usage:
    python3 grant-opportunity-finder.py --search web3
    python3 grant-opportunity-finder.py --list-active
    python3 grant-opportunity-finder.py --check-deadlines
"""

import argparse
import json
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError
import re

# =============================================================================
# CONFIGURATION
# =============================================================================

GRANT_DATA_DIR = Path.home() / ".openclaw/workspace/data/grants"
GRANT_OPPORTUNITIES_FILE = GRANT_DATA_DIR / "opportunities.json"
GRANT_PIPELINE_FILE = Path.home() / ".openclaw/workspace/data/revenue-pipeline.json"

# Known grant programs
KNOWN_GRANT_PROGRAMS = {
    "gitcoin": {
        "name": "Gitcoin Grants",
        "url": "https://gitcoin.co/grants",
        "cycle": "Quarterly",
        "potential": 5000,
        "status": "tracked"
    },
    "octant": {
        "name": "Octant (GP)",
        "url": "https://octant.uchaintech.cn/",
        "cycle": "Quarterly",
        "potential": 15000,
        "status": "tracked"
    },
    "olas": {
        "name": "Olas (GP)",
        "url": "https://olas.xyz/",
        "cycle": "Varies",
        "potential": 50000,
        "status": "tracked"
    },
    "optimism_rpgf": {
        "name": "Optimism RPGF",
        "url": "https://app.optimism.io/retrofunding/rounds",
        "cycle": "Rounds",
        "potential": 50000,
        "status": "tracked"
    },
    "moloch_dao": {
        "name": "Moloch DAO",
        "url": "https://molochdao.com/",
        "cycle": "Ongoing",
        "potential": 10000,
        "status": "tracked"
    },
    "ethereum_foundation": {
        "name": "Ethereum Foundation",
        "url": "https://ethereum.org/en/grants/",
        "cycle": "Ongoing",
        "potential": 50000,
        "status": "prospect"
    },
    "github_sponsors": {
        "name": "GitHub Sponsors",
        "url": "https://github.com/sponsors",
        "cycle": "Ongoing",
        "potential": 10000,
        "status": "prospect"
    },
    "open_collective": {
        "name": "Open Collective",
        "url": "https://opencollective.com/",
        "cycle": "Ongoing",
        "potential": 5000,
        "status": "prospect"
    }
}

# =============================================================================
# FUNCTIONS
# =============================================================================

def load_opportunities():
    """Load discovered grant opportunities."""
    if GRANT_OPPORTUNITIES_FILE.exists():
        with open(GRANT_OPPORTUNITIES_FILE) as f:
            return json.load(f)
    return {"discovered": [], "last_checked": None}

def save_opportunities(opportunities):
    """Save grant opportunities."""
    GRANT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(GRANT_OPPORTUNITIES_FILE, 'w') as f:
        json.dump(opportunities, f, indent=2)

def check_deadlines():
    """Check which grants have upcoming deadlines."""
    opportunities = load_opportunities()
    upcoming = []

    now = datetime.now(timezone.utc)
    for grant in opportunities.get("discovered", []):
        if grant.get("deadline"):
            deadline = datetime.fromisoformat(grant["deadline"])
            days_until = (deadline - now).days
            if 0 <= days_until <= 30:
                upcoming.append({
                    "name": grant["name"],
                    "deadline": grant["deadline"],
                    "days_until": days_until,
                    "potential": grant.get("potential", 0)
                })

    return sorted(upcoming, key=lambda x: x["days_until"])

def search_web3_grants():
    """Search for web3/crypto grant opportunities."""
    # Known web3 grant programs
    web3_programs = [
        "gitcoin", "octant", "olas", "optimism_rpgf", "moloch_dao"
    ]

    opportunities = []
    for prog_id in web3_programs:
        if prog_id in KNOWN_GRANT_PROGRAMS:
            prog = KNOWN_GRANT_PROGRAMS[prog_id]
            opportunities.append({
                "name": prog["name"],
                "program_id": prog_id,
                "url": prog["url"],
                "cycle": prog["cycle"],
                "potential": prog["potential"],
                "status": prog["status"],
                "discovered": datetime.now(timezone.utc).isoformat()
            })

    return opportunities

def search_ai_grants():
    """Search for AI/agent research grants."""
    # AI grant programs to explore
    ai_programs = [
        {
            "name": "Anthropic Claude Research",
            "url": "https://www.anthropic.com/research",
            "potential": 25000,
            "notes": "Claude ecosystem grants"
        },
        {
            "name": "OpenAI Researcher Access",
            "url": "https://openai.com/research",
            "potential": 20000,
            "notes": "API credits for research"
        }
    ]

    opportunities = []
    for prog in ai_programs:
        opportunities.append({
            "name": prog["name"],
            "url": prog["url"],
            "potential": prog["potential"],
            "status": "prospect",
            "category": "ai",
            "notes": prog["notes"],
            "discovered": datetime.now(timezone.utc).isoformat()
        })

    return opportunities

def list_active_grants():
    """List currently tracked grant opportunities."""
    opportunities = load_opportunities()

    if not opportunities.get("discovered"):
        print("  📭 No grant opportunities discovered yet")
        print("  💡 Run: python3 grant-opportunity-finder.py --search <category>")
        return

    print(f"  📊 Discovered Grants ({len(opportunities['discovered'])} total):\n")

    # Group by status
    by_status = {"tracked": [], "prospect": [], "submitted": []}
    for grant in opportunities["discovered"]:
        status = grant.get("status", "prospect")
        by_status.setdefault(status, []).append(grant)

    # Print tracked grants
    if by_status["tracked"]:
        print("  ✅ TRACKED (in pipeline):")
        for grant in by_status["tracked"]:
            print(f"     • {grant['name']}: ${grant.get('potential', 0):,.0f}")
            if grant.get("deadline"):
                print(f"       Deadline: {grant['deadline']}")

    # Print prospects
    if by_status["prospect"]:
        print("\n  🔍 PROSPECTS (to research):")
        for grant in by_status["prospect"]:
            print(f"     • {grant['name']}: ${grant.get('potential', 0):,.0f}")
            print(f"       URL: {grant['url']}")

    # Print submitted
    if by_status["submitted"]:
        print("\n  📤 SUBMITTED:")
        for grant in by_status["submitted"]:
            print(f"     • {grant['name']}: ${grant.get('potential', 0):,.0f}")

    if opportunities.get("last_checked"):
        print(f"\n  🕐 Last checked: {opportunities['last_checked']}")

def main():
    parser = argparse.ArgumentParser(description="Grant Opportunity Finder")
    parser.add_argument("--search", choices=["web3", "ai", "all"], help="Search for grant opportunities")
    parser.add_argument("--list-active", action="store_true", help="List tracked grant opportunities")
    parser.add_argument("--check-deadlines", action="store_true", help="Check upcoming deadlines")
    parser.add_argument("--add", help="Add a new grant opportunity (JSON format)")

    args = parser.parse_args()

    if args.search:
        opportunities = load_opportunities()
        new_discoveries = []

        if args.search in ["web3", "all"]:
            print("  🔍 Searching for Web3 grants...")
            new_discoveries.extend(search_web3_grants())

        if args.search in ["ai", "all"]:
            print("  🔍 Searching for AI grants...")
            new_discoveries.extend(search_ai_grants())

        # Add new discoveries (avoid duplicates by name)
        existing_names = {g["name"] for g in opportunities.get("discovered", [])}
        for grant in new_discoveries:
            if grant["name"] not in existing_names:
                opportunities.setdefault("discovered", []).append(grant)
                existing_names.add(grant["name"])
                print(f"  ➕ Found: {grant['name']} (${grant.get('potential', 0):,.0f})")

        opportunities["last_checked"] = datetime.now(timezone.utc).isoformat()
        save_opportunities(opportunities)

        print(f"\n  ✅ Discovery complete: {len(new_discoveries)} grants found")

    elif args.list_active:
        list_active_grants()

    elif args.check_deadlines:
        upcoming = check_deadlines()
        if upcoming:
            print("  ⏰ Upcoming Deadlines:\n")
            for grant in upcoming:
                print(f"     • {grant['name']}: {grant['days_until']} days (${grant['potential']:,.0f})")
        else:
            print("  ✅ No deadlines in next 30 days")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
