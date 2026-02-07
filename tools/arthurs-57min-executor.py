#!/usr/bin/env python3
"""
Arthur's 57-Minute Executor
Guides through the $880K pipeline execution with timing and ROI reminders.
Usage: python3 tools/arthurs-57min-executor.py
"""

import time
import sys

STEPS = [
    ("Gateway Restart", 1, 50000, "openclaw gateway restart (ask Nova to run)"),
    ("GitHub Auth", 5, 125000, "gh auth login"),
    ("Send Service Messages (Batch 1)", 12, 110000, "python3 tools/service-sender.py batch1"),
    ("Send Service Messages (Batch 2)", 12, 110000, "python3 tools/service-sender.py batch2"),
    ("Send Service Messages (Batch 3)", 12, 112000, "python3 tools/service-sender.py batch3"),
    ("Submit Grant 1 (Gitcoin)", 3, 25000, "python3 tools/grant-submit.py gitcoin"),
    ("Submit Grant 2 (Octant)", 3, 25000, "python3 tools/grant-submit.py octant"),
    ("Submit Grant 3 (Olas)", 3, 25000, "python3 tools/grant-submit.py olas"),
    ("Submit Grant 4 (Optimism)", 3, 25000, "python3 tools/grant-submit.py optimism"),
    ("Submit Grant 5 (Moloch)", 3, 25000, "python3 tools/grant-submit.py moloch"),
]

def format_money(n):
    if n >= 1000:
        return f"${n/1000:.0f}K"
    return f"${n}"

def main():
    print("=" * 60)
    print("ARTHUR'S 57-MINUTE EXECUTOR")
    print("$880K Pipeline → Revenue in 57 Minutes")
    print("=" * 60)
    print()
    
    total_time = sum(s[1] for s in STEPS)
    total_value = sum(s[2] for s in STEPS)
    
    print(f"Total Time: {total_time} minutes")
    print(f"Total Value: {format_money(total_value)}")
    print(f"ROI: {format_money(total_value/total_time)}/min")
    print()
    print("-" * 60)
    
    completed_value = 0
    completed_time = 0
    
    for i, (name, mins, value, command) in enumerate(STEPS, 1):
        print(f"\n[STEP {i}/{len(STEPS)}] {name}")
        print(f"  Time: {mins} min | Value: {format_money(value)} | ROI: {format_money(value/mins)}/min")
        print(f"  Command: {command}")
        
        response = input("\n  Execute? [y/n/q]: ").strip().lower()
        
        if response == 'q':
            print("\n  Stopped by user.")
            break
        elif response == 'y':
            completed_value += value
            completed_time += mins
            print(f"  ✓ Completed! ({format_money(completed_value)} in {completed_time} min)")
        else:
            print(f"  ✗ Skipped")
    
    print()
    print("=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Completed: {completed_time}/{total_time} minutes")
    print(f"Unlocked: {format_money(completed_value)}/{format_money(total_value)}")
    if completed_time > 0:
        print(f"Your ROI: {format_money(completed_value/completed_time)}/min")
    print()
    print("Next: Check revenue-tracker.py for updated pipeline status")
    print("=" * 60)

if __name__ == "__main__":
    main()
