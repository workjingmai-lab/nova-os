#!/usr/bin/env python3
"""
analytics.py — Unified analytics CLI (consolidates 4 tools)

Replaces:
- tool-usage-analysis.py → analytics.py usage
- work-pattern-analyzer.py → analytics.py patterns
- velocity-predictor.py → analytics.py velocity
- daily-output-tracker.py → analytics.py output

Usage:
    python3 tools/analytics.py usage              # Top tools by usage
    python3 tools/analytics.py patterns           # Work patterns by hour
    python3 tools/analytics.py velocity           # Forecast velocity
    python3 tools/analytics.py output             # Daily productivity metrics
"""

import argparse
import sys
from pathlib import Path

# Import diary_parser from same directory
_tools_dir = Path(__file__).parent
if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))

try:
    from diary_parser import DiaryParser
except ImportError:
    # Fallback: load module directly
    import types
    diary_parser_code = (_tools_dir / "diary_parser.py").read_text()
    diary_parser = types.ModuleType("diary_parser")
    exec(diary_parser_code, diary_parser.__dict__)
    DiaryParser = diary_parser.DiaryParser


def cmd_usage(args):
    """Show tool usage patterns (replaces tool-usage-analysis.py)"""
    parser = DiaryParser()
    tools = parser.get_tool_usage()

    print("\n" + "="*60)
    print("  📊 TOOL USAGE ANALYSIS (from diary.md)")
    print("="*60 + "\n")

    total_mentions = sum(tools.values())
    print(f"  Total tool mentions: {total_mentions}\n")

    if total_mentions == 0:
        print("  No tool usage found in diary.md\n")
        return

    print("  Top 10 Most Used Tools:\n")
    for i, (tool, count) in enumerate(tools.most_common(10), 1):
        percentage = (count / total_mentions) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {i}. {tool:<30} {count:>4}x  {bar}")

    # 80/20 analysis
    total_tools = len(tools)
    top_5_count = sum(count for _, count in tools.most_common(5))
    top_5_percentage = (top_5_count / total_mentions * 100) if total_mentions > 0 else 0

    print(f"\n  📈 80/20 Analysis:")
    print(f"     Total unique tools: {total_tools}")
    print(f"     Top 5 tools: {top_5_percentage:.1f}% of mentions")


def cmd_patterns(args):
    """Show work patterns by hour (replaces work-pattern-analyzer.py)"""
    parser = DiaryParser()
    blocks = parser.get_blocks()
    hourly = parser.get_blocks_by_hour()

    print("\n" + "="*60)
    print("  ⏰ WORK PATTERN ANALYSIS (by hour)")
    print("="*60 + "\n")

    if not blocks:
        print("  No work blocks found\n")
        return

    print(f"  Total blocks analyzed: {len(blocks)}\n")

    for hour in sorted(hourly.keys()):
        count = len(hourly[hour])
        bar = "█" * (count // 2 + 1)
        print(f"  {hour:02d}:00  {count:>3} blocks  {bar}")

    # Most productive hour
    peak_hour = max(hourly.items(), key=lambda x: len(x[1]))
    print(f"\n  🎯 Peak productivity: {peak_hour[0]:02d}:00 ({len(peak_hour[1])} blocks)")


def cmd_velocity(args):
    """Forecast velocity (replaces velocity-predictor.py)"""
    parser = DiaryParser()

    baseline = args.baseline or 24
    forecast = args.forecast or 12

    velocity = parser.get_velocity(baseline)
    predicted = parser.forecast_blocks(forecast, baseline)

    print("\n" + "="*60)
    print("  🚀 VELOCITY FORECAST")
    print("="*60 + "\n")

    print(f"  Baseline window: {baseline} hours")
    print(f"  Current velocity: {velocity:.1f} blocks/hour")
    print(f"\n  Forecast ({forecast} hours): {predicted} blocks")

    if velocity > 40:
        print(f"\n  🔥 Velocity: HIGH (>40 blocks/hour)")
    elif velocity > 20:
        print(f"\n  ⚡ Velocity: Medium (20-40 blocks/hour)")
    else:
        print(f"\n  📉 Velocity: Low (<20 blocks/hour)")


def cmd_output(args):
    """Show daily productivity metrics (replaces daily-output-tracker.py)"""
    parser = DiaryParser()
    daily = parser.get_daily_metrics()

    print("\n" + "="*60)
    print("  📊 DAILY OUTPUT REPORT")
    print("="*60 + "\n")

    if not daily:
        print("  No daily data found\n")
        return

    print(f"  Days tracked: {len(daily)}\n")

    # Show last 7 days
    recent_days = sorted(daily.items())[-7:]

    for date, metrics in recent_days:
        print(f"  {date}:")
        print(f"    Tasks: {metrics.tasks_completed}  |  Files: {metrics.files_created}  |  Tools: {metrics.tools_built}")
        print(f"    Posts: {metrics.posts_published}  |  Learnings: {metrics.learnings_logged}  |  Words: {metrics.word_count}")

    # Totals
    total_tasks = sum(m.tasks_completed for m in daily.values())
    total_files = sum(m.files_created for m in daily.values())
    total_tools = sum(m.tools_built for m in daily.values())

    print(f"\n  📈 TOTALS:")
    print(f"    Tasks: {total_tasks}  |  Files: {total_files}  |  Tools: {total_tools}")


def main():
    parser = argparse.ArgumentParser(
        description="Unified analytics CLI for diary.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  analytics.py usage              # Show tool usage patterns
  analytics.py patterns           # Show work patterns by hour
  analytics.py velocity           # Forecast velocity
  analytics.py output             # Show daily productivity
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Analytics command")

    # usage command
    subparsers.add_parser("usage", help="Tool usage patterns")

    # patterns command
    subparsers.add_parser("patterns", help="Work patterns by hour")

    # velocity command
    vel_parser = subparsers.add_parser("velocity", help="Forecast velocity")
    vel_parser.add_argument("--baseline", type=int, help="Baseline window (hours, default: 24)")
    vel_parser.add_argument("--forecast", type=int, help="Forecast horizon (hours, default: 12)")

    # output command
    subparsers.add_parser("output", help="Daily productivity metrics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Route to command handler
    commands = {
        "usage": cmd_usage,
        "patterns": cmd_patterns,
        "velocity": cmd_velocity,
        "output": cmd_output,
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
