#!/usr/bin/env python3
"""
Contact Finder V2 - Discover decision makers for service outreach

Searches for company contacts (CTO, VP Eng, Head of Platform) using web search
and returns their social media profiles for outreach.

Usage:
    python3 contact-finder-v2.py --company "Uniswap"
    python3 contact-finder-v2.py --role "CTO" --company "Vercel"

Author: Nova
Created: 2026-02-04
"""

import json
import argparse
import re
from pathlib import Path
from datetime import datetime

RESULTS_DIR = Path("/home/node/.openclaw/workspace/data/contacts")

COMPANY_SEARCH_TEMPLATES = [
    "{company} CTO",
    "{company} VP Engineering",
    "{company} Head of Platform",
    "{company} engineering lead",
    "{company} technical founder",
    "{company} engineering blog"
]

def parse_company_name(input_str):
    """Extract clean company name from input"""
    # Remove common suffixes/prefixes
    company = input_str.strip()
    company = re.sub(r'\s+(Inc|LLC|Corp|Ltd|Company)$', '', company, flags=re.IGNORECASE)
    return company

def generate_search_queries(company):
    """Generate list of search queries for finding contacts"""
    queries = []
    for template in COMPANY_SEARCH_TEMPLATES:
        queries.append(template.format(company=company))
    return queries

def save_contact_research(company, contacts_found):
    """Save contact research results to file"""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = company.lower().replace(' ', '-') + "-research.md"
    filepath = RESULTS_DIR / filename

    content = f"""# {company} Contact Research

> Generated: {timestamp}
> Status: Contact discovery initiated

## Identified Contacts

"""

    if contacts_found:
        for contact in contacts_found:
            content += f"""
### {contact.get('name', 'Unknown')} - {contact.get('role', 'Unknown')}

- **Company:** {company}
- **Role:** {contact.get('role', 'N/A')}
- **Twitter:** {contact.get('twitter', 'N/A')}
- **GitHub:** {contact.get('github', 'N/A')}
- **LinkedIn:** {contact.get('linkedin', 'N/A')}

"""
    else:
        content += """
*No contacts automatically discovered yet. Manual research needed.*

**Next steps:**
1. Search for "{company} engineering team" on Google
2. Check {company}.com/about for team page
3. Look for "{company} CTO" on Twitter
4. Search GitHub for {company} organization members
"""

    content += """
## Outreach Strategy

**Value Proposition:** Multi-agent automation for engineering workflows

**Pain Points to Address:**
- Scalability bottlenecks
- Manual review processes
- Community management overhead
- CI/CD optimization

**Message Variant:** Pain-first (research → specific pain → solution)

## Confidence Score
To be calculated after contact discovery

## Next Steps
1. Verify contact information
2. Research recent activity (tweets, GitHub contributions)
3. Identify specific pain points from public content
4. Craft personalized message
5. Send via appropriate channel
"""

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

    return filepath

def main():
    parser = argparse.ArgumentParser(description="Find contacts for service outreach")
    parser.add_argument("--company", required=True, help="Company name to search")
    parser.add_argument("--role", help="Specific role to target")
    parser.add_argument("--save", action="store_true", help="Save results to research file")

    args = parser.parse_args()

    company = parse_company_name(args.company)
    print(f"\n🔍 Contact Finder: {company}")
    print("="*60)

    # Generate search queries
    queries = generate_search_queries(company)

    print(f"\n📋 Search Queries to Execute:")
    print("="*60)
    for i, query in enumerate(queries, 1):
        print(f"{i}. {query}")

    print(f"\n" + "="*60)
    print(f"⚠️  Note: Web search requires Brave API key")
    print(f"⚠️  Run: openclaw configure --section web")
    print(f"="*60)

    # For now, create template research file
    if args.save:
        print(f"\n💾 Creating research template...")
        filepath = save_contact_research(company, [])
        print(f"✅ Saved: {filepath}")

    print(f"\n🎯 Next Steps:")
    print(f"1. Use Brave search to find actual contacts")
    print(f"2. Verify information (Twitter, GitHub, LinkedIn)")
    print(f"3. Update research file with contact details")
    print(f"4. Craft personalized message")
    print(f"5. Send via service-outreach-sender.py")

if __name__ == "__main__":
    main()
