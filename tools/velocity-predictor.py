#!/usr/bin/env python3
"""
velocity-predictor.py — Predict when you'll hit milestone work blocks

Calculates time to milestone based on current velocity.
Supports multiple prediction models (linear, accelerated, conservative).

Usage:
    python3 tools/velocity-predictor.py                    # Predict 3000
    python3 tools/velocity-predictor.py --milestone 5000   # Custom milestone
    python3 tools/velocity-predictor.py --blocks-hour 50   # Custom velocity
    python3 tools/velocity-predictor.py --model accelerated  # Prediction model
"""

import sys
from datetime import datetime, timedelta

# Configuration
CURRENT_BLOCKS = 2717  # Update this from today.md
DEFAULT_MILESTONE = 3000
DEFAULT_VELOCITY = 44  # blocks/hour (historical average)

def calculate_time_to_milestone(current, milestone, velocity):
    """Calculate hours and days to milestone."""
    remaining = milestone - current
    hours = remaining / velocity if velocity > 0 else float('inf')
    days = hours / 24  # Assuming 24/7 execution
    return remaining, hours, days

def predict_completion_date(days):
    """Predict completion date from now."""
    now = datetime.now()
    completion = now + timedelta(days=days)
    return completion

def format_time_remaining(hours, days):
    """Format time remaining for display."""
    if hours < 1:
        return f"{int(hours * 60)} minutes"
    elif hours < 24:
        return f"{hours:.1f} hours ({hours / 24:.2f} days)"
    else:
        return f"{days:.1f} days ({days * 24:.0f} hours)"

def main():
    # Parse arguments
    milestone = DEFAULT_MILESTONE
    velocity = DEFAULT_VELOCITY
    model = "linear"

    for i, arg in enumerate(sys.argv):
        if arg == "--milestone" and i + 1 < len(sys.argv):
            milestone = int(sys.argv[i + 1])
        elif arg == "--blocks-hour" and i + 1 < len(sys.argv):
            velocity = float(sys.argv[i + 1])
        elif arg == "--model" and i + 1 < len(sys.argv):
            model = sys.argv[i + 1]

    # Calculate predictions for different models
    models = {
        "conservative": velocity * 0.7,  # 30% slower
        "linear": velocity,               # Historical average
        "accelerated": velocity * 1.3     # 30% faster
    }

    if model not in models:
        print(f"⚠️  Unknown model: {model}. Using 'linear'")
        model = "linear"

    model_velocity = models[model]

    remaining, hours, days = calculate_time_to_milestone(CURRENT_BLOCKS, milestone, model_velocity)
    completion_date = predict_completion_date(days)

    # Output
    print(f"\n📊 Velocity Predictor: Work Block Milestone")
    print("=" * 50)
    print(f"Current blocks:   {CURRENT_BLOCKS}")
    print(f"Target milestone:  {milestone}")
    print(f"Remaining:        {remaining} blocks")
    print(f"\nModel:             {model.upper()}")
    print(f"Velocity:          {model_velocity:.1f} blocks/hour")
    print(f"Time remaining:    {format_time_remaining(hours, days)}")
    print(f"Estimated arrival: {completion_date.strftime('%Y-%m-%d %H:%M')} UTC")
    print("\n" + "=" * 50)

    # Show all models for comparison
    if len(sys.argv) == 1:  # Only show comparison if no args
        print("\n📈 All Models (Comparison):")
        print("-" * 50)
        for model_name, model_vel in models.items():
            _, h, d = calculate_time_to_milestone(CURRENT_BLOCKS, milestone, model_vel)
            print(f"{model_name.capitalize():12} ({model_vel:.1f} b/hr): {format_time_remaining(h, d)}")

    print(f"\n💡 Tip: To accelerate, reduce decision fatigue.")
    print(f"   - Use task-randomizer.py")
    print(f"   - Execute immediately")
    print(f"   - Don't plan, just ship")

    return 0

if __name__ == "__main__":
    sys.exit(main())
