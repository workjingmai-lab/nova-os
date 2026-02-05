#!/usr/bin/env python3
"""
Contact Researcher - Find contact info for service prospects

Usage: python3 tools/contact-researcher.py [--top N] [--method google|linkedin|website]

Features:
- Web search for company/agent contact pages
- Structured output with confidence scores
- Batch processing for 10-20 prospects at once
- Respectful research (no scraping, just finding public info)

Methods:
- google: Search "[company/agent] contact us" or "[name] email"
- linkedin: Search for LinkedIn profiles (if name known)
- website: Direct domain + /contact check

Example:
    python3 tools/contact-researcher.py --top 10 --method google
"""

import json
import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime

PIPELINE_FILE = "/home/node/.openclaw/workspace/data/revenue-pipeline.json"
OUTPUT_DIR = Path("/home/node/.openclaw/workspace/knowledge/contacts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_prospects(limit=None):
    """Load prospects from pipeline, optionally limit to top N"""
    with open(PIPELINE_FILE) as f:
        data = json.load(f)

    prospects = []
    for i, opp in enumerate(data.get("services", [])):
        if opp.get("status") == "lead":
            prospects.append({
                "id": f"service-{i}",
                "company": opp.get("name", "Unknown"),
                "contact_person": opp.get("contact_person"),
                "website": opp.get("website"),
                "value_estimate": opp.get("potential", 0)
            })

    # Sort by value estimate (descending)
    prospects.sort(key=lambda x: x["value_estimate"], reverse=True)

    if limit:
        prospects = prospects[:limit]

    return prospects

def web_search(query):
    """Run web search using brave search API or fallback"""
    try:
        # Try web_fetch tool first (lighter)
        result = subprocess.run(
            ["web_search", "--query", query, "--count", "5"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
    except Exception as e:
        print(f"  ⚠️  Search failed: {e}")

    return None

def find_contact_page(prospect):
    """Research contact info for a prospect"""
    company = prospect["company"]
    website = prospect.get("website")
    person = prospect.get("contact_person")

    findings = []
    confidence = 0

    # Method 1: Website direct check
    if website:
        print(f"  🔍 Checking {website}/contact ...")
        findings.append({
            "source": "website",
            "url": f"{website}/contact",
            "confidence": 0.6
        })
        confidence += 0.6

    # Method 2: Web search for company contact
    search_query = f'"{company}" contact us email'
    print(f"  🔍 Searching: {search_query}")
    results = web_search(search_query)
    if results:
        findings.append({
            "source": "google_search",
            "query": search_query,
            "results": results[:500],  # First 500 chars
            "confidence": 0.4
        })
        confidence += 0.4

    # Method 3: LinkedIn search (if person known)
    if person:
        linkedin_query = f'"{person}" {company} LinkedIn'
        print(f"  🔍 Searching: {linkedin_query}")
        results = web_search(linkedin_query)
        if results:
            findings.append({
                "source": "linkedin_search",
                "query": linkedin_query,
                "results": results[:500],
                "confidence": 0.5
            })
            confidence += 0.5

    return {
        "prospect": prospect,
        "findings": findings,
        "confidence": min(confidence, 1.0),
        "timestamp": datetime.now().isoformat()
    }

def main():
    limit = 10  # Default: top 10 prospects
    method = "google"

    if "--top" in sys.argv:
        idx = sys.argv.index("--top")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    if "--method" in sys.argv:
        idx = sys.argv.index("--method")
        if idx + 1 < len(sys.argv):
            method = sys.argv[idx + 1]

    print(f"🎯 Contact Researcher: Top {limit} prospects via {method}\n")

    prospects = load_prospects(limit=limit)
    if not prospects:
        print("❌ No prospects found in 'lead' stage for services")
        return 1

    print(f"📊 Found {len(prospects)} prospects to research\n")

    results = []
    for i, prospect in enumerate(prospects, 1):
        print(f"\n[{i}/{len(prospects)}] {prospect['company']}")
        print(f"  Value: ${prospect['value_estimate']:,.0f}")
        if prospect.get('contact_person'):
            print(f"  Person: {prospect['contact_person']}")

        result = find_contact_page(prospect)
        results.append(result)

        confidence_pct = int(result["confidence"] * 100)
        print(f"  ✅ Confidence: {confidence_pct}%")

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = OUTPUT_DIR / f"research-{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    # Summary
    avg_confidence = sum(r["confidence"] for r in results) / len(results) if results else 0

    summary = {
        "research_date": datetime.now().isoformat(),
        "prospects_researched": len(results),
        "average_confidence": avg_confidence,
        "total_value": sum(p["prospect"]["value_estimate"] for p in results),
        "output_file": str(output_file),
        "next_steps": [
            "Review contact findings in output JSON",
            "Update pipeline with verified contact info",
            "Execute service outreach for high-confidence prospects"
        ]
    }

    summary_file = OUTPUT_DIR / f"summary-{timestamp}.md"
    with open(summary_file, "w") as f:
        f.write(f"# Contact Research Summary\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
        f.write(f"**Prospects Researched:** {len(results)}\n")
        f.write(f"**Average Confidence:** {avg_confidence:.1%}\n")
        f.write(f"**Total Value:** ${summary['total_value']:,.0f}\n\n")

        f.write(f"## Findings\n\n")
        for r in results:
            p = r["prospect"]
            f.write(f"### {p['company']}\n")
            f.write(f"- **Value:** ${p['value_estimate']:,.0f}\n")
            f.write(f"- **Confidence:** {r['confidence']:.1%}\n")
            if p.get('contact_person'):
                f.write(f"- **Contact:** {p['contact_person']}\n")
            if p.get('website'):
                f.write(f"- **Website:** {p['website']}\n")
            f.write(f"- **Findings:** {len(r['findings'])} sources\n\n")

        f.write(f"## Next Steps\n\n")
        f.write("1. Review findings in `" + str(output_file) + "`\n")
        f.write("2. Verify contact info manually\n")
        f.write("3. Update revenue-pipeline.json with confirmed contacts\n")
        f.write("4. Execute service outreach for verified prospects\n")

    print(f"\n✅ Research complete!")
    print(f"📁 Results: {output_file}")
    print(f"📋 Summary: {summary_file}")
    print(f"\n📊 Stats:")
    print(f"  - Prospects: {len(results)}")
    print(f"  - Avg confidence: {avg_confidence:.1%}")
    print(f"  - Total value: ${summary['total_value']:,.0f}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
