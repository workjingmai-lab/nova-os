#!/usr/bin/env python3
"""
verify-leads.py — Quick sanity check for outreach message files
Ensures all lead files are properly formatted before batch sending

Usage:
    python3 tools/verify-leads.py           # Check all leads
    python3 tools/verify-leads.py expert    # Check EXPERT tier only
    python3 tools/verify-leads.py tactical  # Check TACTICAL tier only
"""

import json
import sys
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw/workspace"
LEADS_DIR = WORKSPACE / "outreach" / "leads"
PIPELINE_FILE = WORKSPACE / "revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline data"""
    if not PIPELINE_FILE.exists():
        print(f"❌ Pipeline file not found: {PIPELINE_FILE}")
        return None
    with open(PIPELINE_FILE) as f:
        return json.load(f)

def verify_lead_file(lead_path):
    """Verify a single lead file has required fields"""
    if not lead_path.exists():
        return {"status": "missing", "errors": ["File not found"]}

    try:
        with open(lead_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {"status": "invalid", "errors": [f"Invalid JSON: {e}"]}

    errors = []
    warnings = []

    # Required fields
    required = ["name", "company", "tier", "value", "contact"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Value validation
    if "value" in data:
        try:
            value = int(data["value"])
            if value <= 0:
                warnings.append("Value should be positive integer")
        except (ValueError, TypeError):
            errors.append("Value must be an integer")

    # Contact validation
    if "contact" in data:
        contact = data["contact"]
        if not contact.get("email") and not contact.get("telegram"):
            warnings.append("No email or telegram contact found")

    # Message file check
    if "message_file" in data:
        msg_path = WORKSPACE / data["message_file"]
        if not msg_path.exists():
            warnings.append(f"Message file not found: {data['message_file']}")

    if errors:
        return {"status": "error", "errors": errors}
    if warnings:
        return {"status": "warning", "warnings": warnings}
    return {"status": "ok", "errors": [], "warnings": []}

def main():
    tier_filter = sys.argv[1] if len(sys.argv) > 1 else None

    print("🔍 Lead File Verification")
    print("=" * 50)

    pipeline = load_pipeline()
    if not pipeline:
        sys.exit(1)

    leads_by_status = pipeline.get("leads", {})

    # Collect all leads
    all_leads = []
    for status, leads in leads_by_status.items():
        for lead in leads:
            lead["status"] = status
            all_leads.append(lead)

    if tier_filter:
        tier_filter = tier_filter.upper()
        all_leads = [l for l in all_leads if l.get("tier") == tier_filter]
        print(f"Filtering by tier: {tier_filter}")

    print(f"Checking {len(all_leads)} leads...\n")

    # Verify each lead
    results = {"ok": 0, "warning": 0, "error": 0, "missing": 0}
    issues = []

    for lead in all_leads:
        lead_file = LEADS_DIR / f"{lead['id']}.json"
        result = verify_lead_file(lead_file)
        results[result["status"]] += 1

        if result["status"] in ["error", "warning", "missing"]:
            issues.append({
                "lead": lead.get("name", lead["id"]),
                "tier": lead.get("tier", "UNKNOWN"),
                "status": result["status"],
                "errors": result.get("errors", []),
                "warnings": result.get("warnings", [])
            })

    # Print summary
    print("📊 Summary:")
    print(f"  ✅ OK: {results['ok']}")
    print(f"  ⚠️  Warnings: {results['warning']}")
    print(f"  ❌ Errors: {results['error']}")
    print(f"  📁 Missing: {results['missing']}")

    # Print issues if any
    if issues:
        print(f"\n🚨 Issues Found ({len(issues)}):")
        for issue in issues:
            print(f"\n  [{issue['tier']}] {issue['lead']}")
            if issue['errors']:
                for error in issue['errors']:
                    print(f"    ❌ {error}")
            if issue['warnings']:
                for warning in issue['warnings']:
                    print(f"    ⚠️  {warning}")
    else:
        print("\n✅ All leads verified! Ready for batch sending.")

    # Exit code
    if results['error'] > 0 or results['missing'] > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
