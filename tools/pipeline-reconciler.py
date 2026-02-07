#!/usr/bin/env python3
"""
Pipeline Reconciler — Data Consistency Checker

Checks all pipeline data sources for consistency:
- revenue-pipeline.json
- service-outreach-tracker.json
- today.md (if present)
- Actual calculated values from source data

Usage:
    python3 tools/pipeline-reconciler.py
    python3 tools/pipeline-reconciler.py --fix
    python3 tools/pipeline-reconciler.py --verbose

Author: Nova
Created: 2026-02-05 — Work block 2163
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def load_json(path: str) -> Dict:
    """Load JSON file safely."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing {path}: {e}")
        return {}

def extract_number(text: str) -> float:
    """Extract dollar amount from text (e.g., '$880K' -> 880000)."""
    if not text:
        return 0

    # Remove common formatting
    text = text.strip().replace('$', '').replace(',', '').upper()

    # Handle K/M/B suffixes
    multiplier = 1
    if text.endswith('K'):
        multiplier = 1000
        text = text[:-1]
    elif text.endswith('M'):
        multiplier = 1000000
        text = text[:-1]
    elif text.endswith('B'):
        multiplier = 1000000000
        text = text[:-1]

    try:
        return float(text) * multiplier
    except ValueError:
        return 0

def calculate_service_actual(tracker_data: Dict) -> Dict[str, Any]:
    """Calculate actual service pipeline from messages array."""
    messages = tracker_data.get('messages', [])

    # Note: pipeline_value is in thousands (20 = $20K), need to multiply by 1000
    total_value = sum(m.get('pipeline_value', 0) * 1000 for m in messages)
    ready_count = len(messages)
    sent_count = sum(1 for m in messages if m.get('status') == 'sent')

    avg_value = total_value / ready_count if ready_count > 0 else 0

    return {
        'total_value': total_value,
        'ready_count': ready_count,
        'sent_count': sent_count,
        'avg_value': avg_value
    }

def parse_today_md(today_path: str) -> Dict[str, Any]:
    """Extract pipeline value from today.md if present."""
    try:
        with open(today_path, 'r') as f:
            content = f.read()

        # Look for patterns like "Pipeline: $880K" or "$880K pipeline"
        import re

        # Pattern 1: "Pipeline: $XXXK" or "Pipeline: $XXXM"
        pattern1 = r'Pipeline:\s*\$([0-9.]+)([KMB])'
        matches = re.findall(pattern1, content, re.IGNORECASE)

        if matches:
            value, suffix = matches[0]
            return extract_number(f'${value}{suffix}')

        # Pattern 2: "$XXXK total pipeline"
        pattern2 = r'\$([0-9.]+)([KMB])[^a-z]*pipeline'
        matches = re.findall(pattern2, content, re.IGNORECASE)

        if matches:
            value, suffix = matches[0]
            return extract_number(f'${value}{suffix}')

        return 0
    except FileNotFoundError:
        return 0
    except Exception as e:
        if verbose:
            print(f"⚠️  Warning parsing today.md: {e}")
        return 0

def format_currency(value: float) -> str:
    """Format value as currency string."""
    if value >= 1000000:
        return f'${value/1000000:.2f}M'
    elif value >= 1000:
        return f'${value/1000:.0f}K'
    else:
        return f'${value:.0f}'

def check_consistency() -> Dict[str, Any]:
    """Check consistency across all data sources."""
    workspace = Path('/home/node/.openclaw/workspace')

    # Load data sources
    pipeline_data = load_json(workspace / 'revenue-pipeline.json')
    tracker_data = load_json(workspace / 'service-outreach-tracker.json')

    # Calculate actual values from source data
    service_actual = calculate_service_actual(tracker_data)

    # Get claimed values from JSON summaries
    pipeline_total = pipeline_data.get('totalPipeline', 0)
    pipeline_services = pipeline_data.get('categories', {}).get('services', {}).get('amount', 0)
    pipeline_grants = pipeline_data.get('categories', {}).get('grants', {}).get('amount', 0)
    pipeline_bounties = pipeline_data.get('categories', {}).get('bounties', {}).get('amount', 0)

    # Get tracker summary (may be outdated)
    tracker_summary = tracker_data.get('summary', {})
    tracker_total = extract_number(str(tracker_summary.get('pipelineValue', 0)))

    # Parse today.md if present
    today_value = parse_today_md(workspace / 'today.md')

    # Build comparison
    results = {
        'actual_services': service_actual['total_value'],
        'actual_grants': pipeline_grants,
        'actual_bounties': pipeline_bounties,
        'actual_total': service_actual['total_value'] + pipeline_grants + pipeline_bounties,

        'pipeline_json_total': pipeline_total,
        'pipeline_json_services': pipeline_services,

        'tracker_summary_total': tracker_total,

        'today_md_total': today_value,

        'discrepancies': [],
        'warnings': []
    }

    # Check for discrepancies (>5% OR >$100K difference)
    threshold = 0.05
    min_abs_diff = 100000  # $100K

    # Pipeline JSON vs actual
    diff = results['pipeline_json_total'] - results['actual_total']
    if abs(diff) > max(results['actual_total'] * threshold, min_abs_diff):
        results['discrepancies'].append({
            'source': 'revenue-pipeline.json total',
            'claimed': results['pipeline_json_total'],
            'actual': results['actual_total'],
            'difference': diff,
            'severity': 'HIGH' if abs(diff) > 200000 else 'MEDIUM'
        })

    # Pipeline JSON services vs actual
    diff = results['pipeline_json_services'] - results['actual_services']
    if abs(diff) > max(results['actual_services'] * threshold, min_abs_diff):
        results['discrepancies'].append({
            'source': 'revenue-pipeline.json services',
            'claimed': results['pipeline_json_services'],
            'actual': results['actual_services'],
            'difference': diff,
            'severity': 'HIGH' if abs(diff) > 200000 else 'MEDIUM'
        })

    # Tracker summary vs actual
    if tracker_summary:
        diff = results['tracker_summary_total'] - results['actual_total']
        if abs(diff) > max(results['actual_total'] * threshold, min_abs_diff):
            results['discrepancies'].append({
                'source': 'service-outreach-tracker.json summary',
                'claimed': results['tracker_summary_total'],
                'actual': results['actual_total'],
                'difference': diff,
                'severity': 'LOW'  # Summary field is known to be stale
            })

    # today.md vs actual
    if today_value > 0:
        diff = today_value - results['actual_total']
        if abs(diff) > max(results['actual_total'] * threshold, min_abs_diff):
            results['discrepancies'].append({
                'source': 'today.md',
                'claimed': today_value,
                'actual': results['actual_total'],
                'difference': diff,
                'severity': 'MEDIUM'
            })

    # Add service stats
    results['service_stats'] = service_actual

    return results

def print_report(results: Dict[str, Any]):
    """Print consistency report."""
    print("=" * 60)
    print("📊 PIPELINE RECONCILIATION REPORT")
    print("=" * 60)
    print()

    # Actual values (source of truth)
    print("✅ ACTUAL VALUES (from source data):")
    print(f"   Services: {format_currency(results['actual_services'])} ({results['service_stats']['ready_count']} ready, {results['service_stats']['sent_count']} sent)")
    print(f"   Grants:   {format_currency(results['actual_grants'])}")
    print(f"   Bounties: {format_currency(results['actual_bounties'])}")
    print(f"   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"   TOTAL:    {format_currency(results['actual_total'])}")
    print()

    # Claimed values
    print("📋 CLAIMED VALUES (from summaries):")
    print(f"   revenue-pipeline.json:  {format_currency(results['pipeline_json_total'])}")
    if results['tracker_summary_total'] > 0:
        print(f"   tracker.json summary:   {format_currency(results['tracker_summary_total'])}")
    if results['today_md_total'] > 0:
        print(f"   today.md:               {format_currency(results['today_md_total'])}")
    print()

    # Discrepancies
    if results['discrepancies']:
        print("⚠️  DISCREPANCIES FOUND:")
        print()
        for d in results['discrepancies']:
            severity_icon = "🔴" if d['severity'] == 'HIGH' else "🟡" if d['severity'] == 'MEDIUM' else "🟢"
            print(f"   {severity_icon} {d['source']}")
            print(f"      Claimed: {format_currency(d['claimed'])}")
            print(f"      Actual:  {format_currency(d['actual'])}")
            print(f"      Diff:    {format_currency(d['difference'])} ({'+' if d['difference'] > 0 else ''}{d['difference']/1000:.0f}K)")
            print()
    else:
        print("✅ ALL DATA SOURCES CONSISTENT")
        print()

    # Service stats
    if results['service_stats']['ready_count'] > 0:
        print("📈 SERVICE OUTREACH STATS:")
        print(f"   Messages ready: {results['service_stats']['ready_count']}")
        print(f"   Messages sent:  {results['service_stats']['sent_count']}")
        print(f"   Avg value:      {format_currency(results['service_stats']['avg_value'])} per message")
        print(f"   Conversion:     {results['service_stats']['sent_count']/results['service_stats']['ready_count']*100:.1f}%")
        print()

    print("=" * 60)

def main():
    """Main entry point."""
    global verbose
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    results = check_consistency()
    print_report(results)

    # Exit code based on discrepancies
    high_severity = any(d['severity'] == 'HIGH' for d in results['discrepancies'])
    sys.exit(1 if high_severity else 0)

if __name__ == '__main__':
    main()
