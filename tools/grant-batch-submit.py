#!/usr/bin/env python3
"""
Grant Batch Submitter — Submit all prepared grant applications.

Reads grant submissions from tmp/grant-submissions/ and submits them.
Requires GitHub CLI auth (gh) for repository-based grants.

Usage:
    python3 grant-batch-submit.py           # Submit all ready grants
    python3 grant-batch-submit.py --dry-run # Preview what would be submitted

Requirements:
    - GitHub CLI auth: gh auth login
    - Grant JSON files in tmp/grant-submissions/

Created: 2026-02-06 (Work block 2573)
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
GRANT_DIR = "/home/node/.openclaw/workspace/tmp/grant-submissions"
GRANTS = [
    {"name": "Gitcoin", "file": "gitcoin_20260204_100333.json", "platform": "gitcoin", "amount": 5000},
    {"name": "Octant", "file": "octant_20260204_100333.json", "platform": "octant", "amount": 15000},
    {"name": "Olas", "file": "olas_20260204_100333.json", "platform": "olas", "amount": 10000},
    {"name": "Optimism", "file": "optimism_20260204_100333.json", "platform": "optimism", "amount": 50000},
    {"name": "Moloch DAO", "file": "moloch_20260204_100333.json", "platform": "moloch", "amount": 50000}
]

def check_github_auth():
    """Check if GitHub CLI is authenticated."""
    import subprocess
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False

def load_grant_data(filename):
    """Load grant submission data from JSON file."""
    filepath = Path(GRANT_DIR) / filename
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  File not found: {filepath}")
        return None

def submit_grant(grant, dry_run=False):
    """Submit a single grant application."""
    print(f"\n📝 Processing: {grant['name']} (${grant['amount']:,.0f})")
    
    # Load grant data
    grant_data = load_grant_data(grant['file'])
    if not grant_data:
        return False
    
    platform = grant['platform']
    content = grant_data.get('content', {})
    
    if dry_run:
        print(f"  [DRY RUN] Would submit to {platform.upper()}")
        print(f"  Title: {content.get('name', 'N/A')}")
        desc = content.get('description', 'N/A')
        print(f"  Description: {desc[:100]}{'...' if len(desc) > 100 else ''}")
        return True
    
    # Platform-specific submission logic
    if platform == "gitcoin":
        return submit_gitcoin(grant_data)
    elif platform == "octant":
        return submit_octant(grant_data)
    elif platform == "olas":
        return submit_olas(grant_data)
    elif platform == "optimism":
        return submit_optimism(grant_data)
    elif platform == "moloch":
        return submit_moloch(grant_data)
    else:
        print(f"  ⚠️  Unknown platform: {platform}")
        return False

def submit_gitcoin(grant_data):
    """Submit to Gitcoin (browser-based, manual for now)."""
    content = grant_data.get('content', {})
    print(f"  ⚠️  Gitcoin submission requires browser access")
    print(f"  📋 Grant: {content.get('name', 'N/A')}")
    print(f"  💰 Budget: {content.get('budget', 'N/A')}")
    print(f"  🌐 URL: {grant_data.get('platform', 'https://gitcoin.co')}")
    print(f"  ✅ Data ready in tmp/grant-submissions/gitcoin_*.json")
    print(f"  → Arthur: Open browser, fill form using prepared data")
    return False  # Requires manual action

def submit_octant(grant_data):
    """Submit to Octant (browser-based, manual for now)."""
    content = grant_data.get('content', {})
    print(f"  ⚠️  Octant submission requires browser access")
    print(f"  📋 Grant: {content.get('name', 'N/A')}")
    print(f"  💰 Budget: {content.get('budget', 'N/A')}")
    print(f"  🌐 URL: {grant_data.get('platform', 'https://octant.app')}")
    print(f"  ✅ Data ready in tmp/grant-submissions/octant_*.json")
    print(f"  → Arthur: Open browser, submit using prepared data")
    return False  # Requires manual action

def submit_olas(grant_data):
    """Submit to Olas (browser-based, manual for now)."""
    content = grant_data.get('content', {})
    print(f"  ⚠️  Olas submission requires browser access")
    print(f"  📋 Grant: {content.get('name', 'N/A')}")
    print(f"  💰 Budget: {content.get('budget', 'N/A')}")
    print(f"  🌐 URL: {grant_data.get('platform', 'https://olas.network')}")
    print(f"  ✅ Data ready in tmp/grant-submissions/olas_*.json")
    print(f"  → Arthur: Open browser, submit using prepared data")
    return False  # Requires manual action

def submit_optimism(grant_data):
    """Submit to Optimism RPGF (requires GitHub CLI)."""
    content = grant_data.get('content', {})
    print(f"  ⚠️  Optimism RPGF requires GitHub repository push")
    print(f"  📋 Grant: {content.get('name', 'N/A')}")
    print(f"  💰 Budget: {content.get('budget', 'N/A')}")
    print(f"  🔧 Requires: gh auth login + git push to public repo")
    print(f"  ✅ Proposal ready in tmp/grant-submissions/optimism_*.json")
    print(f"  → Arthur: Run 'gh auth login', then push repo, then submit via GitHub")
    return False  # Requires manual action

def submit_moloch(grant_data):
    """Submit to Moloch DAO (browser-based, manual for now)."""
    content = grant_data.get('content', {})
    print(f"  ⚠️  Moloch DAO submission requires browser access")
    print(f"  📋 Grant: {content.get('name', 'N/A')}")
    print(f"  💰 Budget: {content.get('budget', 'N/A')}")
    print(f"  🌐 URL: {grant_data.get('platform', 'https://molochdao.com')}")
    print(f"  ✅ Data ready in tmp/grant-submissions/moloch_*.json")
    print(f"  → Arthur: Open browser, submit proposal using prepared data")
    return False  # Requires manual action

def print_summary(results, dry_run=False):
    """Print submission summary."""
    total = len(results)
    submitted = sum(1 for r in results if r)
    total_amount = sum(g['amount'] for g in GRANTS)
    submitted_amount = sum(GRANTS[i]['amount'] for i, r in enumerate(results) if r)
    
    print("\n" + "=" * 60)
    print("📊 SUBMISSION SUMMARY")
    print("=" * 60)
    print(f"Total grants: {total}")
    print(f"Prepared: {total} (${total_amount:,.0f})")
    
    if dry_run:
        print(f"[DRY RUN] Would submit: {total} grants")
    else:
        print(f"Submitted: {submitted} (${submitted_amount:,.0f})")
        print(f"Pending: {total - submitted} (${total_amount - submitted_amount:,.0f})")
    
    print()

def main():
    parser = argparse.ArgumentParser(description="Submit grant applications")
    parser.add_argument("--dry-run", action="store_true", help="Preview without submitting")
    args = parser.parse_args()
    
    print("🚀 GRANT BATCH SUBMITTER")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check GitHub auth (needed for some platforms)
    if not args.dry_run:
        if not check_github_auth():
            print("⚠️  GitHub CLI not authenticated")
            print("   Run: gh auth login")
            print()
    
    # Submit grants
    results = []
    for grant in GRANTS:
        result = submit_grant(grant, dry_run=args.dry_run)
        results.append(result)
    
    # Print summary
    print_summary(results, dry_run=args.dry_run)
    
    if not args.dry_run:
        print("💡 NEXT STEPS:")
        print("   1. Complete manual submissions (browser-based)")
        print("   2. Update revenue-pipeline.json: --status submitted")
        print("   3. Track responses in diary.md")

if __name__ == "__main__":
    main()
