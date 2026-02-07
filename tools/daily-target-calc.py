#!/usr/bin/env python3
"""
daily-target-calc.py — Calculate daily progress toward work block goals
"""

import sys
from datetime import datetime

def main():
    # Config
    DAILY_GOAL = 300
    current_blocks = 3213  # Update this each run
    
    # Time calculations
    now = datetime.utcnow()
    hour = now.hour
    minute = now.minute
    hours_elapsed = hour + minute / 60
    hours_remaining = 24 - hours_elapsed
    
    # Progress
    progress_pct = (current_blocks / DAILY_GOAL) * 100
    blocks_needed = max(0, DAILY_GOAL - current_blocks)
    
    # Velocity needed
    if hours_remaining > 0:
        required_velocity = blocks_needed / hours_remaining
    else:
        required_velocity = 0
    
    # Status
    if progress_pct >= 100:
        status = "✅ GOAL CRUSHED"
    elif progress_pct >= 75:
        status = "🟢 On track"
    elif progress_pct >= 50:
        status = "🟡 Needs attention"
    else:
        status = "🔴 Behind"
    
    # Output
    print(f"📊 Daily Target Calculator")
    print(f"   Time: {now.strftime('%H:%M')} UTC | Hours remaining: {hours_remaining:.1f}")
    print()
    print(f"   Current:  {current_blocks} blocks")
    print(f"   Goal:     {DAILY_GOAL} blocks")
    print(f"   Progress: {progress_pct:.1f}% {status}")
    print()
    
    if blocks_needed > 0:
        print(f"   Need:     {blocks_needed} more blocks")
        print(f"   Velocity: {required_velocity:.1f} blocks/hour required")
        print(f"   Sustained velocity (44/hr): {(blocks_needed / 44):.1f} hours of work")
    else:
        surplus = current_blocks - DAILY_GOAL
        print(f"   Surplus:  +{surplus} blocks ({surplus/DAILY_GOAL*100:.0f}% over goal)")
    
    print()
    print(f"   Week 3 Day 1 starts tomorrow — Feb 8")

if __name__ == "__main__":
    main()
