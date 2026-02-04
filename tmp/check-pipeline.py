#!/usr/bin/env python3
import json

with open('/home/node/.openclaw/workspace/tmp/service-outreach-tracker.json', 'r') as f:
    data = json.load(f)

leads = data.get('leads', [])
total = data.get('messages_ready', 0)
potential = data.get('potential_value', '$0')

print(f"✅ Pipeline: {total} messages ready, {potential} services, {len(leads)} leads")
