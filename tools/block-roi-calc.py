#!/usr/bin/env python3
"""
block-roi-calc.py — Work Block ROI Calculator

Calculate your execution efficiency: revenue, output, or impact per block.
Helps agents measure and optimize their work block productivity.

Usage:
    python3 tools/block-roi-calc.py <total_blocks> <total_value> [--currency USD]
    python3 tools/block-roi-calc.py 1000 880000 --currency USD

Output:
    Per-block ROI, hourly velocity projection, milestone predictions
"""

import argparse
import sys

def format_currency(value, currency="USD"):
    """Format value as currency."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency, currency + " ")
    if value >= 1000000:
        return f"{symbol}{value/1000000:.2f}M"
    elif value >= 1000:
        return f"{symbol}{value/1000:.1f}K"
    else:
        return f"{symbol}{value:.0f}"

def calculate_roi(blocks, value, avg_block_time_min=1):
    """Calculate ROI metrics for work blocks."""
    per_block = value / blocks if blocks > 0 else 0
    total_hours = (blocks * avg_block_time_min) / 60
    blocks_per_hour = blocks / total_hours if total_hours > 0 else 0
    
    # Projections
    k_blocks_value = per_block * 1000
    k_blocks_hours = (1000 * avg_block_time_min) / 60
    
    return {
        "per_block": per_block,
        "total_hours": total_hours,
        "blocks_per_hour": blocks_per_hour,
        "k_blocks_value": k_blocks_value,
        "k_blocks_hours": k_blocks_hours
    }

def main():
    parser = argparse.ArgumentParser(
        description="Calculate work block ROI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 tools/block-roi-calc.py 1000 880000
    python3 tools/block-roi-calc.py 500 50000 --currency EUR
        """
    )
    parser.add_argument("blocks", type=int, help="Total work blocks completed")
    parser.add_argument("value", type=float, help="Total value generated (revenue, impact, etc.)")
    parser.add_argument("--currency", default="USD", help="Currency symbol (default: USD)")
    parser.add_argument("--time", type=float, default=1, help="Average minutes per block (default: 1)")
    
    args = parser.parse_args()
    
    if args.blocks <= 0:
        print("Error: Blocks must be > 0", file=sys.stderr)
        sys.exit(1)
    
    metrics = calculate_roi(args.blocks, args.value, args.time)
    
    print("=" * 50)
    print("📊 WORK BLOCK ROI ANALYSIS")
    print("=" * 50)
    print(f"\nInput:")
    print(f"  Blocks completed: {args.blocks:,}")
    print(f"  Total value: {format_currency(args.value, args.currency)}")
    print(f"  Avg time/block: {args.time} min")
    
    print(f"\nCurrent Performance:")
    print(f"  Per-block ROI: {format_currency(metrics['per_block'], args.currency)}")
    print(f"  Blocks/hour: {metrics['blocks_per_hour']:.1f}")
    print(f"  Total hours: {metrics['total_hours']:.1f}h")
    
    print(f"\n1000-Block Projection:")
    print(f"  Value at 1000 blocks: {format_currency(metrics['k_blocks_value'], args.currency)}")
    print(f"  Time to 1000 blocks: {metrics['k_blocks_hours']:.1f}h ({metrics['k_blocks_hours']/8:.1f} work days)")
    
    print(f"\nBenchmarks:")
    if metrics['per_block'] >= 500:
        print("  🚀 Excellent: $500+/block (top tier)")
    elif metrics['per_block'] >= 100:
        print("  ✅ Strong: $100+/block (solid execution)")
    elif metrics['per_block'] >= 10:
        print("  📈 Growing: $10+/block (building momentum)")
    else:
        print("  🌱 Early: <$10/block (focus on volume first)")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
