#!/usr/bin/env python3
"""
Lead Score Calculator - Prioritize service business opportunities

Scores leads based on fit, value, and readiness signals.
Higher score = prioritize first.

Usage:
    python tools/lead-score-calculator.py score --company "Acme" --fit 8 --value 5000 --readiness 7
    python tools/lead-score-calculator.py sort < leads.json
"""

import json
import sys
from pathlib import Path

def calculate_score(fit: int, value: int, readiness: int) -> dict:
    """
    Calculate lead score (0-100)

    Weights:
    - Fit (40%): How well they match my services (1-10)
    - Value (30%): Deal size in USD (normalized 0-10)
    - Readiness (30%): Urgency signals (1-10)

    Returns score + breakdown
    """
    # Normalize value: $25K = 10 points, $1K = 1 point
    value_score = min(10, max(1, value / 2500))

    score = int((fit * 0.4) + (value_score * 0.3) + (readiness * 0.3)) * 10

    return {
        "score": score,
        "breakdown": {
            "fit": fit,
            "value_score": value_score,
            "readiness": readiness,
            "value": value
        },
        "priority": "high" if score >= 70 else "medium" if score >= 50 else "low"
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: lead-score-calculator.py score|--help")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "score":
        # Parse args
        company = "Unknown"
        fit, value, readiness = 5, 2000, 5

        for i, arg in enumerate(sys.argv[2:]):
            if arg == "--company" and i + 1 < len(sys.argv) - 2:
                company = sys.argv[i + 3]
            elif arg == "--fit" and i + 1 < len(sys.argv) - 2:
                fit = int(sys.argv[i + 3])
            elif arg == "--value" and i + 1 < len(sys.argv) - 2:
                value = int(sys.argv[i + 3])
            elif arg == "--readiness" and i + 1 < len(sys.argv) - 2:
                readiness = int(sys.argv[i + 3])

        result = calculate_score(fit, value, readiness)

        print(f"\n📊 Lead Score: {company}")
        print(f"   Score: {result['score']}/100 ({result['priority'].upper()} priority)")
        print(f"   Fit: {result['breakdown']['fit']}/10")
        print(f"   Value: ${value:,.0f} ({result['breakdown']['value_score']:.1f}/10)")
        print(f"   Readiness: {result['breakdown']['readiness']}/10")

    elif cmd == "--help":
        print(__doc__)

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
