#!/usr/bin/env python3
"""
pipeline-quickview.py — Essential revenue numbers at a glance
Shows only what matters: total, ready to send, submitted, conversion rate
"""

import json
from datetime import datetime

def main():
    try:
        with open('revenue-pipeline.json', 'r') as f:
            data = json.load(f)
        
        # Calculate totals
        total = sum(item.get('value', 0) for item in data.get('opportunities', []))
        ready = sum(item.get('value', 0) for item in data.get('opportunities', []) 
                    if item.get('status') == 'ready')
        submitted = sum(item.get('value', 0) for item in data.get('opportunities', [])
                       if item.get('status') == 'submitted')
        won = sum(item.get('value', 0) for item in data.get('opportunities', [])
                 if item.get('status') == 'won')
        
        # Conversion rate
        conversion = (won / total * 100) if total > 0 else 0
        
        # Output
        print("=" * 40)
        print("💰 PIPELINE QUICKVIEW")
        print("=" * 40)
        print(f"Total Pipeline:    ${total:>12,}")
        print(f"Ready to Send:     ${ready:>12,}")
        print(f"Submitted:         ${submitted:>12,}")
        print(f"Won:               ${won:>12,}")
        print("-" * 40)
        print(f"Conversion Rate:   {conversion:>11.1f}%")
        print("=" * 40)
        
        if ready > 0:
            print(f"\n🚀 Action: ${ready:,} ready to convert")
        
    except FileNotFoundError:
        print("❌ revenue-pipeline.json not found")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
