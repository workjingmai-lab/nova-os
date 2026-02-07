#!/usr/bin/env python3
import json

with open('data/revenue-pipeline.json') as f:
    data = json.load(f)

items = data.get('items', [])
print(f"Items: {len(items)}")
total = sum(i.get('potential_value',0) for i in items)
print(f"Total potential: ${total:,.0f}")
