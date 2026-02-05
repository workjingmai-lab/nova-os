#!/usr/bin/env python3
"""
Blocks Calculator — Quick velocity projections for work block planning.

Shows how many work blocks you can complete in a given time at different velocities.
Useful for milestone planning and timeboxing.

Usage:
    python3 tools/blocks-calculator.py              # Default: 1 hour at 44 blocks/hr
    python3 tools/blocks-calculator.py 30           # 30 minutes at 44 blocks/hr
    python3 tools/blocks-calculator.py 120 55       # 120 minutes at 55 blocks/hr
"""

import sys

def calculate_blocks(minutes: int, velocity: int) -> dict:
    """
    Calculate work blocks for given time and velocity.

    Args:
        minutes: Time available in minutes
        velocity: Blocks per hour

    Returns:
        dict with blocks, time, velocity details
    """
    hours = minutes / 60
    blocks = int(hours * velocity)
    return {
        "blocks": blocks,
        "minutes": minutes,
        "hours": round(hours, 2),
        "velocity": velocity,
        "blocks_per_min": round(velocity / 60, 2)
    }

def main():
    # Parse arguments
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    velocity = int(sys.argv[2]) if len(sys.argv) > 2 else 44

    # Calculate
    result = calculate_blocks(minutes, velocity)

    # Display
    print(f"📊 Blocks Calculator — {minutes} minutes @ {result['velocity']} blocks/hr")
    print(f"   Time: {result['hours']} hours ({minutes} minutes)")
    print(f"   Velocity: {result['velocity']} blocks/hr ({result['blocks_per_min']} blocks/min)")
    print(f"   Result: {result['blocks']} work blocks")
    print()
    print("🔹 Velocity Scenarios:")
    print(f"   • 25 blocks/hr → {calculate_blocks(minutes, 25)['blocks']} blocks (relaxed)")
    print(f"   • 44 blocks/hr → {calculate_blocks(minutes, 44)['blocks']} blocks (sustained)")
    print(f"   • 55 blocks/hr → {calculate_blocks(minutes, 55)['blocks']} blocks (burst)")
    print(f"   • 70 blocks/hr → {calculate_blocks(minutes, 70)['blocks']} blocks (peak)")

if __name__ == "__main__":
    main()
