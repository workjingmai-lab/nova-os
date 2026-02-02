#!/usr/bin/env python3
"""
Grant Discovery Tracker

Helps track and evaluate grant opportunities for agents.
Quick checklist format for rapid assessment.

Usage:
    python tools/grant-discovery-tracker.py
"""

GRANT_SOURCES = [
    "Gitcoin Grants",
    "Ethereum Foundation",
    "OpenCLaw Community Fund",
    "Protocol DAO Grants",
    "Climate Crypto",
    "Public Goods Funding"
]

ASSESSMENT_CRITERIA = [
    "Alignment with agent capabilities",
    "Application complexity (1-5)",
    "Time requirement (hours)",
    "Decision timeline",
    "Past award rate"
]

def print_header():
    print("=" * 60)
    print("🔍 GRANT DISCOVERY TRACKER")
    print("=" * 60)
    print()

def print_sources():
    print("📍 KNOWN GRANT SOURCES:")
    for i, source in enumerate(GRANT_SOURCES, 1):
        print(f"  {i}. {source}")
    print()

def print_checklist():
    print("✅ ASSESSMENT CHECKLIST:")
    for i, criterion in enumerate(ASSESSMENT_CRITERIA, 1):
        print(f"  {i}. {criterion}")
    print()

def print_template():
    print("📝 NEW GRANT ENTRY TEMPLATE:")
    print("-" * 60)
    print("""
Source: [Name]
URL: [Link]
Amount: [$X,XXX]
Deadline: [YYYY-MM-DD]
Alignment: [High/Med/Low]
Complexity: [1-5]
Time Required: [X hours]
Status: [Researching/Applying/Won/Lost]
Notes: [Key details]
""")
    print("-" * 60)
    print()

def print_quick_ref():
    print("⚡ QUICK GRANT SEARCH COMMANDS:")
    print("  • Gitcoin: curl https://gitcoin.co/grants")
    print("  • EF: https://efdn.notion.site/Ethereum-Foundation-Grant-Programs")
    print("  • OpenCLaw: Check #grants channel")
    print("  • Protocol DAOs: Search '[name] grants'")
    print()

if __name__ == "__main__":
    print_header()
    print_sources()
    print_checklist()
    print_template()
    print_quick_ref()
    print("💡 Tip: Log discovered grants to grants/tracked-grants.md")
    print("=" * 60)
