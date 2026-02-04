#!/usr/bin/env python3
"""
Fix pipeline values in service-outreach-tracker.json

Parses amountRange strings (e.g., "$15K-$25K") and calculates numeric pipeline_value.
"""

import json
import re
from pathlib import Path

PIPELINE_FILE = Path("/home/node/.openclaw/workspace/service-outreach-tracker.json")

def parse_amount_range(amount_range: str) -> int:
    """Parse amountRange like '$15K-$25K' and return midpoint value in thousands."""
    if not amount_range:
        return 0

    # Extract all numbers from the string
    numbers = re.findall(r'(\d+)', amount_range.replace('K', '000').replace('M', '000000'))

    if not numbers:
        return 0

    # Convert to integers
    values = [int(n) for n in numbers]

    # If single value, use it; if range, use midpoint
    if len(values) == 1:
        return values[0] // 1000  # Convert to thousands
    else:
        return sum(values) // len(values) // 1000  # Midpoint in thousands

def fix_pipeline_values():
    """Update all messages with numeric pipeline_value."""
    with open(PIPELINE_FILE) as f:
        data = json.load(f)

    messages = data.get("messages", [])
    updated = 0
    total_value = 0

    for msg in messages:
        amount_range = msg.get("amountRange", "")
        current_value = msg.get("pipeline_value", 0)

        # Only update if pipeline_value is 0 or missing
        if current_value == 0 and amount_range:
            new_value = parse_amount_range(amount_range)
            if new_value > 0:
                msg["pipeline_value"] = new_value
                total_value += new_value
                updated += 1
                print(f"✓ {msg.get('company', 'Unknown')}: {amount_range} → ${new_value}K")
        else:
            total_value += current_value

    # Save updated tracker
    data["messages"] = messages
    with open(PIPELINE_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print()
    print(f"Updated: {updated} messages")
    print(f"Total pipeline value: ${total_value}K")
    print()

if __name__ == "__main__":
    fix_pipeline_values()
