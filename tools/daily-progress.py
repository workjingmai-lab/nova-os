#!/usr/bin/env python3
"""
Daily Progress Tracker — What to Focus On Today
Shows daily priorities toward 3000-block milestone.

Usage:
    python3 tools/daily-progress.py           # Show today's focus
    python3 tools/daily-progress.py plan      # Generate daily plan
"""

from datetime import datetime, timedelta

def get_milestone_status():
    """Get current milestone status."""
    current_blocks = 2791
    target_blocks = 3000
    blocks_remaining = target_blocks - current_blocks
    progress_pct = (current_blocks / target_blocks) * 100
    return {
        "current": current_blocks,
        "target": target_blocks,
        "remaining": blocks_remaining,
        "progress": progress_pct
    }

def get_daily_target(blocks_remaining, days=1):
    """Calculate daily block target."""
    blocks_per_day = 44 * 24  # 44 blocks/hour × 24 hours
    if days == 1:
        return min(blocks_per_day, blocks_remaining)
    return blocks_remaining // days + (1 if blocks_remaining % days else 0)

def get_today_focus():
    """Determine today's focus based on milestone proximity."""
    status = get_milestone_status()
    blocks_remaining = status["remaining"]
    
    # Phase determination
    if blocks_remaining > 500:
        phase = "BUILD"
        focus = "Tool creation, documentation, outreach messages"
    elif blocks_remaining > 200:
        phase = "REFINE"
        focus = "Polish docs, consolidate tools, prep execution"
    elif blocks_remaining > 100:
        phase = "EXECUTE"
        focus = "Final prep, validation, ready-to-send checks"
    else:
        phase = "FINISH"
        focus = "Milestone prep, documentation, celebration content"
    
    return phase, focus, blocks_remaining

def main():
    import sys
    
    phase, focus, blocks_remaining = get_today_focus()
    status = get_milestone_status()
    
    print("📅 TODAY'S FOCUS")
    print("=" * 50)
    print(f"Milestone: {status['current']}/{status['target']} blocks ({status['progress']:.1f}%)")
    print(f"Remaining: {blocks_remaining} blocks")
    print(f"Phase:     {phase}")
    print(f"Focus:     {focus}")
    print()
    
    # Daily target
    daily_target = get_daily_target(blocks_remaining, days=1)
    print(f"🎯 Daily target: {daily_target} blocks (44 blocks/hr × 24 hr)")
    print(f"📊 Milestone ETA: {blocks_remaining / 44:.1f} hours")
    print()
    
    # Priority actions
    print("🚀 TODAY'S PRIORITIES:")
    if blocks_remaining > 200:
        print("   1. Continue tool creation")
        print("   2. Build outreach messages")
        print("   3. Create knowledge content")
        print("   4. Moltbook engagement")
    elif blocks_remaining > 100:
        print("   1. Validate all tools work")
        print("   2. Complete documentation")
        print("   3. Ready execution guides")
        print("   4. Prep milestone content")
    else:
        print("   1. Final validation checks")
        print("   2. Milestone article prep")
        print("   3. Celebration content")
        print("   4. Next phase planning")
    
    print()
    print("💡 Quick commands:")
    print("   python3 tools/3000-milestone.py predict  # ETA scenarios")
    print("   python3 tools/revenue-tracker.py summary # Pipeline status")
    print("   python3 tools/trim-today.py 10           # Reduce context")
    
    if len(sys.argv) > 1 and sys.argv[1] == "plan":
        print()
        print("📝 DAILY PLAN TEMPLATE:")
        print("-" * 50)
        print(f"Target: {daily_target} blocks today")
        print(f"Velocity: 44 blocks/hour")
        print(f"Work time: {daily_target / 44:.1f} hours")
        print()
        print("Morning (blocks 1-{0}): Focus work".format(int(daily_target * 0.4)))
        print("Midday (blocks {0}-{1}): Documentation".format(int(daily_target * 0.4), int(daily_target * 0.7)))
        print("Evening (blocks {0}-{1}): Review + plan".format(int(daily_target * 0.7), daily_target))
        print()
        print("🎯 Execute. Don't plan. Build. Don't think. Do.")

if __name__ == "__main__":
    main()
