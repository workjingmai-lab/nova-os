#!/usr/bin/env python3
"""
Morning Routine — Daily startup automation

Combines three essential daily checks into one command:
1. Revenue pipeline status (30 sec)
2. Follow-up reminders (1 min)
3. Trim today.md (30 sec)

Total time: 2 minutes
Purpose: Prevent revenue leakage, maintain pipeline hygiene, reduce context bloat

Usage:
    python3 tools/morning-routine.py
    python3 tools/morning-routine.py --no-trim  # Skip trimming
    python3 tools/morning-routine.py --quiet    # Minimal output

Created: 2026-02-05 — Work block 1768
Author: Nova
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# =============================================================================
# CONFIGURATION
# =============================================================================

WORKSPACE = Path.home() / ".openclaw/workspace"
TOOLS_DIR = WORKSPACE / "tools"

# Tool paths
REVENUE_TRACKER = TOOLS_DIR / "revenue-tracker.py"
FOLLOWUP_REMINDER = TOOLS_DIR / "follow-up-reminder.py"
TRIM_TODAY = TOOLS_DIR / "trim-today.py"

# =============================================================================
# FORMATTING
# =============================================================================

def colorize(text: str, color: str) -> str:
    """Add ANSI color codes for terminal output"""
    colors = {
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "CYAN": "\033[96m",
        "BOLD": "\033[1m",
        "RESET": "\033[0m",
    }
    return f"{colors.get(color, '')}{text}{colors['RESET']}"

def print_header(text: str) -> None:
    """Print section header"""
    print(f"\n{colorize(text, 'CYAN')}")

def print_success(text: str) -> None:
    """Print success message"""
    print(f"{colorize('  ✓', 'GREEN')} {text}")

def print_warning(text: str) -> None:
    """Print warning message"""
    print(f"{colorize('  ⚠️', 'YELLOW')} {text}")

def print_error(text: str) -> None:
    """Print error message"""
    print(f"{colorize('  ✗', 'RED')} {text}")

# =============================================================================
# TOOL EXECUTION
# =============================================================================

def run_pipeline_check(quiet: bool = False) -> bool:
    """Check revenue pipeline status"""
    if not quiet:
        print_header("📊 Step 1/3: Revenue Pipeline Check")

    if not REVENUE_TRACKER.exists():
        print_error(f"Tool not found: {REVENUE_TRACKER}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(REVENUE_TRACKER), "summary"],
            cwd=str(WORKSPACE),
            capture_output=not quiet,
            text=True
        )

        if result.returncode == 0:
            if not quiet:
                print_success("Pipeline status retrieved")
            return True
        else:
            print_error("Failed to retrieve pipeline status")
            return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False

def run_followup_check(quiet: bool = False) -> bool:
    """Check follow-up reminders"""
    if not quiet:
        print_header("💬 Step 2/3: Follow-Up Reminders")

    if not FOLLOWUP_REMINDER.exists():
        print_error(f"Tool not found: {FOLLOWUP_REMINDER}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(FOLLOWUP_REMINDER)],
            cwd=str(WORKSPACE),
            capture_output=not quiet,
            text=True
        )

        if result.returncode == 0:
            if not quiet:
                print_success("Follow-up check complete")

            # Check if any follow-ups are due
            output = result.stdout.lower() if hasattr(result, 'stdout') else ""
            if "no follow-ups due" in output:
                print_success("No follow-ups due today")
            elif "follow-ups due" in output or "overdue" in output:
                print_warning("Follow-ups due! Review list above.")

            return True
        else:
            print_error("Failed to check follow-ups")
            return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False

def run_trim_today(quiet: bool = False, sessions: int = 10) -> bool:
    """Trim today.md to reduce context bloat"""
    if not quiet:
        print_header("✂️  Step 3/3: Trim today.md")

    if not TRIM_TODAY.exists():
        print_error(f"Tool not found: {TRIM_TODAY}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(TRIM_TODAY), str(sessions)],
            cwd=str(WORKSPACE),
            capture_output=not quiet,
            text=True
        )

        if result.returncode == 0:
            if not quiet:
                print_success(f"Trimmed today.md to last {sessions} sessions")
            return True
        else:
            print_error("Failed to trim today.md")
            return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False

# =============================================================================
# MAIN ROUTINE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Morning routine: Daily startup automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/morning-routine.py
  python3 tools/morning-routine.py --no-trim
  python3 tools/morning-routine.py --sessions 15
  python3 tools/morning-routine.py --quiet

Created: 2026-02-05 — Nova
Purpose: Prevent revenue leakage, maintain hygiene, 2min routine
        """
    )

    parser.add_argument(
        "--no-trim",
        action="store_true",
        help="Skip trimming today.md"
    )

    parser.add_argument(
        "--sessions",
        type=int,
        default=10,
        help="Number of sessions to keep in today.md (default: 10)"
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Minimal output, errors only"
    )

    args = parser.parse_args()

    # Print header
    if not args.quiet:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        print(colorize(f"\n  🌅 Morning Routine — {now}\n", "BOLD"))

    # Track results
    results = {
        "pipeline": False,
        "followups": False,
        "trim": False
    }

    # Execute steps
    results["pipeline"] = run_pipeline_check(quiet=args.quiet)
    results["followups"] = run_followup_check(quiet=args.quiet)

    if not args.no_trim:
        results["trim"] = run_trim_today(quiet=args.quiet, sessions=args.sessions)
    else:
        results["trim"] = True  # Skipped, not failed

    # Print summary
    if not args.quiet:
        print_header("✅ Routine Complete")

        all_success = all(results.values())

        if all_success:
            print_success("All checks passed")
            print(f"\n  {colorize('Next:', 'BOLD')} Execute today's tasks\n")
        else:
            failed = [k for k, v in results.items() if not v]
            print_warning(f"Some checks failed: {', '.join(failed)}")
            print(f"\n  {colorize('Next:', 'BOLD')} Review errors above\n")

    # Exit with appropriate code
    sys.exit(0 if all(results.values()) else 1)

if __name__ == "__main__":
    main()
