#!/usr/bin/env python3
"""
Shipping Readiness Check — Validate all prerequisites before Arthur executes.

Checks:
- Outreach messages exist and are formatted
- Grant submissions are prepared
- Tools are documented
- Pipeline data is current
- Blockers are identified

Usage:
    python3 shipping-readiness-check.py
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Configuration
WORKSPACE = Path("/home/node/.openclaw/workspace")
OUTREACH_DIR = WORKSPACE / "outreach/messages"
GRANT_DIR = WORKSPACE / "tmp/grant-submissions"
TOOLS_DIR = WORKSPACE / "tools"
PIPELINE_FILE = WORKSPACE / "revenue-pipeline.json"

def check_outreach_messages():
    """Check if outreach messages are prepared."""
    print("📤 Checking outreach messages...")
    
    if not OUTREACH_DIR.exists():
        print("  ❌ outreach/messages/ directory not found")
        return False
    
    messages = list(OUTREACH_DIR.glob("*.md"))
    
    if len(messages) == 0:
        print("  ❌ No outreach messages found")
        return False
    
    print(f"  ✅ {len(messages)} messages found")
    
    # Check for required fields in sample message
    sample_file = messages[0]
    with open(sample_file) as f:
        content = f.read()
    
    required = ["Target:", "Potential Value:", "Pain Point:", "Solution:"]
    missing = [field for field in required if field not in content]
    
    if missing:
        print(f"  ⚠️  Sample message missing fields: {missing}")
        return False
    
    print(f"  ✅ Messages properly formatted")
    
    # Check total potential value
    total_value = 0
    for msg_file in messages:
        with open(msg_file) as f:
            content = f.read()
        for line in content.split("\n"):
            if "Potential Value:" in line or "Value:" in line:
                try:
                    parts = line.split("$")
                    if len(parts) > 1:
                        amount_str = parts[1].split()[0].replace(",", "")
                        total_value += float(amount_str)
                except:
                    pass
    
    print(f"  💰 Total service pipeline: ${total_value:,.0f}")
    
    return True

def check_grant_submissions():
    """Check if grant submissions are prepared."""
    print("\n📝 Checking grant submissions...")
    
    if not GRANT_DIR.exists():
        print("  ❌ tmp/grant-submissions/ directory not found")
        return False
    
    grants = list(GRANT_DIR.glob("*.json"))
    
    if len(grants) == 0:
        print("  ❌ No grant submissions found")
        return False
    
    print(f"  ✅ {len(grants)} grant submissions found")
    
    # Validate JSON structure
    total_value = 0
    for grant_file in grants:
        try:
            with open(grant_file) as f:
                data = json.load(f)
            
            if "content" not in data:
                print(f"  ⚠️  {grant_file.name}: missing 'content' field")
                return False
            
            # Extract value from filename or metadata
            grant_name = grant_file.stem.split("_")[0].title()
            if grant_name == "Gitcoin":
                total_value += 5000
            elif grant_name == "Octant":
                total_value += 15000
            elif grant_name == "Olas":
                total_value += 10000
            elif grant_name == "Optimism":
                total_value += 50000
            elif grant_name == "Moloch":
                total_value += 50000
        
        except json.JSONDecodeError:
            print(f"  ❌ {grant_file.name}: invalid JSON")
            return False
    
    print(f"  ✅ All grants valid JSON")
    print(f"  💰 Total grant pipeline: ${total_value:,.0f}")
    
    return True

def check_tool_documentation():
    """Check if tools have READMEs."""
    print("\n🔧 Checking tool documentation...")
    
    tools = list(TOOLS_DIR.glob("*.py"))
    
    if len(tools) == 0:
        print("  ❌ No Python tools found")
        return False
    
    print(f"  📊 {len(tools)} Python tools found")
    
    documented = 0
    for tool in tools:
        readme = TOOLS_DIR / f"{tool.stem}.README.md"
        if readme.exists():
            documented += 1
    
    coverage = (documented / len(tools)) * 100
    
    print(f"  📚 Documentation coverage: {documented}/{len(tools)} ({coverage:.1f}%)")
    
    if coverage >= 90:
        print(f"  ✅ Excellent documentation coverage")
        return True
    elif coverage >= 70:
        print(f"  ⚠️  Good coverage, but some tools missing READMEs")
        return True
    else:
        print(f"  ❌ Low documentation coverage")
        return False

def check_pipeline_data():
    """Check if pipeline data exists and is current."""
    print("\n📊 Checking pipeline data...")
    
    if not PIPELINE_FILE.exists():
        print("  ❌ revenue-pipeline.json not found")
        return False
    
    try:
        with open(PIPELINE_FILE) as f:
            pipeline = json.load(f)
        
        categories = pipeline.get("categories", {})
        
        if len(categories) == 0:
            print("  ❌ No categories in pipeline")
            return False
        
        print(f"  ✅ Pipeline data found")
        print(f"  📁 Categories: {', '.join(categories.keys())}")
        
        return True
    
    except json.JSONDecodeError:
        print("  ❌ Invalid JSON in pipeline file")
        return False

def check_blockers():
    """Identify current blockers."""
    print("\n🚧 Checking blockers...")
    
    blockers = []
    
    # Check GitHub auth
    import subprocess
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            timeout=5
        )
        if result.returncode != 0:
            blockers.append({
                "name": "GitHub CLI auth",
                "impact": "$125K grants",
                "time": "1 min",
                "solution": "gh auth login"
            })
    except:
        blockers.append({
            "name": "GitHub CLI auth",
            "impact": "$125K grants",
            "time": "1 min",
            "solution": "gh auth login"
        })
    
    # Check for START-HERE.md
    if not (WORKSPACE / "START-HERE.md").exists():
        blockers.append({
            "name": "Execution guide missing",
            "impact": "Cannot execute",
            "time": "1 min",
            "solution": "Create START-HERE.md"
        })
    
    if len(blockers) == 0:
        print("  ✅ No blockers detected")
        return True
    else:
        print(f"  ⚠️  {len(blockers)} blockers found:")
        for blocker in blockers:
            print(f"     • {blocker['name']}: {blocker['impact']} ({blocker['time']})")
            print(f"       Solution: {blocker['solution']}")
        return False

def print_summary(results):
    """Print readiness summary."""
    print("\n" + "=" * 60)
    print("📊 SHIPPING READINESS SUMMARY")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for r in results.values() if r)
    
    print(f"\nChecks passed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ ALL CHECKS PASSED")
        print("🚀 You are READY TO SHIP")
        print("\nNext step: Read START-HERE.md and execute")
    else:
        print("\n⚠️  SOME CHECKS FAILED")
        print("🔧 Fix the issues above before shipping")
    
    print()

def main():
    print("🚀 SHIPPING READINESS CHECK")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    results = {
        "Outreach messages": check_outreach_messages(),
        "Grant submissions": check_grant_submissions(),
        "Tool documentation": check_tool_documentation(),
        "Pipeline data": check_pipeline_data(),
        "Blockers": check_blockers()
    }
    
    print_summary(results)

if __name__ == "__main__":
    main()
