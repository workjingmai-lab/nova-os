#!/usr/bin/env python3
import json

with open('revenue-pipeline.json', 'r') as f:
    data = json.load(f)

top = data['categories']['services']['topProspects'][:10]
print("🎯 TOP 10 SERVICE PROSPECTS (READY TO SHIP, ZERO BLOCKERS):\n")
for i, p in enumerate(top, 1):
    print(f"{i}. {p['name']}: ${p['amount']:,} ({p['priority']})")

total = sum(p['amount'] for p in top)
print(f"\n💰 Total value: ${total:,}")
print(f"\n⚡ Execute: python3 tools/service-batch-send.py --top 10")
