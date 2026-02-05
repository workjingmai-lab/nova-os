#!/usr/bin/env python3
"""
Next Action Recommender
Analyzes current state and recommends the highest-ROI next action
"""

import json
from pathlib import Path

PIPELINE_PATH = "/home/node/.openclaw/workspace/data/revenue-pipeline.json"

def load_pipeline():
    """Load revenue pipeline data"""
    try:
        with open(PIPELINE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_blocked_grants(pipeline):
    """Calculate total value of blocked grants"""
    if not pipeline or 'grants' not in pipeline:
        return 0, []

    blocked = []
    total = 0
    for grant in pipeline['grants']:
        if grant['status'] == 'ready_to_submit':
            blocked.append(grant)
            total += grant['potential']
    return total, blocked

def get_ready_services(pipeline):
    """Calculate total value of ready services (status='ready')"""
    if not pipeline or 'services' not in pipeline:
        return 0, []

    ready = []
    total = 0
    for service in pipeline['services']:
        if service['status'] == 'ready':
            ready.append(service)
            total += service['potential']
    return total, ready

def get_blocked_bounties(pipeline):
    """Calculate total value of blocked bounties"""
    if not pipeline or 'bounties' not in pipeline:
        return 0, []

    blocked = []
    total = 0
    for bounty in pipeline['bounties']:
        if bounty['status'] in ['ready_to_submit', 'blocked']:
            blocked.append(bounty)
            total += bounty['potential']
    return total, blocked

def calculate_total_pipeline(pipeline):
    """Calculate total pipeline value"""
    if not pipeline:
        return 0

    total = 0
    for category in ['grants', 'services', 'bounties']:
        for item in pipeline.get(category, []):
            total += item.get('potential', 0)
    return total

def main():
    pipeline = load_pipeline()

    if not pipeline:
        print("❌ Error: Could not load pipeline data")
        return

    # Analyze state
    grants_blocked, grants_list = get_blocked_grants(pipeline)
    services_ready, services_list = get_ready_services(pipeline)
    bounties_blocked, bounties_list = get_blocked_bounties(pipeline)
    total_blocked = grants_blocked + bounties_blocked
    total_pipeline = calculate_total_pipeline(pipeline)

    print("=" * 60)
    print("  🎯 NEXT ACTION RECOMMENDER")
    print("=" * 60)
    print()

    priority = 1

    # Priority 1: Unblock blocked value (grants + bounties)
    if total_blocked > 0:
        if grants_blocked > 0:
            print(f"🔴 PRIORITY {priority}: Unblock ${grants_blocked:,} in grants")
            print(f"   → Action: Gateway restart + GitHub auth (6 min)")
            for g in grants_list[:3]:
                print(f"      • {g['name']}: ${g['potential']:,}")
            if len(grants_list) > 3:
                print(f"      • ... and {len(grants_list) - 3} more")
            print(f"   → ROI: ${int(grants_blocked/6):,}/min")
            print()
            priority += 1

        if bounties_blocked > 0:
            print(f"🔴 PRIORITY {priority}: Unblock ${bounties_blocked:,} in bounties")
            print(f"   → Action: Gateway restart (1 min)")
            print(f"   → ROI: ${int(bounties_blocked/1):,}/min")
            print()
            priority += 1

    # Priority 2: Send ready service messages
    if services_ready > 0:
        print(f"🟢 PRIORITY {priority}: Send {len(services_list)} service messages (${services_ready:,})")
        print(f"   → Action: Review outreach/messages/ and send")
        print(f"   → Time: {len(services_list) * 2} minutes (2 min per message)")
        print(f"   → ROI: ${int(services_ready/(len(services_list) * 2)):,}/min")
        print()
        priority += 1

    # Priority 3: Follow-ups
    print(f"🔵 PRIORITY {priority}: Check for follow-ups")
    print(f"   → Action: Run 'python3 tools/follow-up-reminder.py'")
    print(f"   → Time: 1 minute")
    print()

    # Summary
    print("=" * 60)
    print("  📊 SUMMARY")
    print("=" * 60)
    print(f"Services ready: {len(services_list)} (${services_ready:,})")
    print(f"Blocked value: ${total_blocked:,}")
    print(f"Total pipeline: ${total_pipeline:,}")
    print()

if __name__ == "__main__":
    main()
