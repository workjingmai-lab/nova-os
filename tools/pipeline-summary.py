#!/usr/bin/env python3
"""
Pipeline Summary — Quick revenue pipeline overview
Shows $302K pipeline at a glance
"""

import json
import sys
from pathlib import Path
from datetime import datetime

PIPELINE_FILE = Path("/home/node/.openclaw/workspace/revenue-pipeline.json")

def main():
    try:
        if not PIPELINE_FILE.exists():
            print(f"❌ Error: Pipeline file not found: {PIPELINE_FILE}")
            print("Run revenue-tracker.py first to initialize pipeline.")
            sys.exit(1)

        with open(PIPELINE_FILE) as f:
            data = json.load(f)

        print("\n" + "="*60)
        print("💰 REVENUE PIPELINE SUMMARY")
        print("="*60)
        print(f"\nTotal Pipeline: ${data['totalPipeline']:,.0f}")
        print(f"Last Updated: {data['lastUpdated']}")

        print("\n📊 Breakdown:")
        for category, info in data['categories'].items():
            print(f"\n  {category.upper()}:")
            print(f"    Amount: ${info['amount']:,.0f}")
            print(f"    Status: {info.get('status', 'N/A')}")
            if 'blocker' in info:
                print(f"    Blocker: {info['blocker']}")
            if 'blockerROI' in info:
                print(f"    ROI: {info['blockerROI']}")

        print("\n📈 Metrics:")
        metrics = data['metrics']
        print(f"  Work Blocks Today: {metrics['workBlocksToday']}")
        print(f"  Work Blocks Week 2: {metrics['workBlocksWeek2']}")
        print(f"  Velocity: {metrics['velocity']}")
        print(f"  Next Action: {metrics['nextAction']}")

        print("\n" + "="*60 + "\n")

    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in pipeline file: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"❌ Error: Missing expected field in pipeline data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
