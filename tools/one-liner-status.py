#!/usr/bin/env python3
"""
One-Liner Status — Work block 2174+
Single-line status output for terminal prompts
Run: python3 tools/one-liner-status.py
"""

import json
import os

def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}

def main():
    # Load data
    pipeline = load_json('data/revenue-pipeline.json')
    today_stats = load_json('data/.today-stats.json')

    # Calculate metrics
    blocks = today_stats.get('workBlocks', 0)
    target = 3000
    progress = (blocks / target) * 100

    # Count ready vs submitted
    ready = 0
    submitted = 0

    for category in ['grants', 'services']:
        for item in pipeline.get(category, []):
            potential = item.get('potential', 0)
            status = item.get('status', '')

            if status in ['ready', 'ready_to_submit', 'outreach-ready', 'messages_ready']:
                ready += potential
            elif 'submitted' in status.lower():
                submitted += potential

    gap = ready - submitted

    # Format output
    # Block progress + execution gap + conversion
    conversion = (submitted / (ready + submitted) * 100) if (ready + submitted) > 0 else 0

    # Truncate gap to K (thousands) for brevity
    gap_k = gap / 1000

    output = f"⚡ {blocks}/{target} ({progress:.0f}%) | 💰 ${gap_k:.0f}K gap | 📈 {conversion:.0f}% conv"

    print(output)

if __name__ == '__main__':
    main()
