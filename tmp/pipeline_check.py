#!/usr/bin/env python3
import json

with open('revenue-pipeline.json') as f:
    d = json.load(f)

grants = d['categories']['grants']['amount']
services = d['categories']['services']['amount']
total = grants + services
ready = d['categories']['services']['ready'] + d['categories']['grants']['ready']
total_pipeline = d['totalPipeline']

print(f"Grants: ${grants:,}")
print(f"Services: ${services:,}")
print(f"Grants + Services: ${total:,}")
print(f"totalPipeline from JSON: ${total_pipeline:,}")
print(f"Difference (bounties): ${total_pipeline - total:,}")
print(f"Ready: ${ready:,}")
