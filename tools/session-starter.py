#!/usr/bin/env python3
"""
Session Starter - Initialize new work session quickly

Usage:
    python3 tools/session-starter.py              # Start new session
    python3 tools/session-starter.py --context     # Show context only
"""

import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/node/.openclaw/workspace")
HEARTBEAT_STATE = WORKSPACE / ".heartbeat_state.json"
TODAY_MD = WORKSPACE / "today.md"
ACTIVE_GOALS = WORKSPACE / "goals/active.md"
DIARY_MD = WORKSPACE / "diary.md"

def get_current_context():
    """Load current context from workspace files"""
    context = {
        "timestamp": datetime.now().isoformat(),
        "session_number": None,
        "recent_work": [],
        "active_goals": [],
        "next_actions": [],
    }

    # Load heartbeat state for session number
    if HEARTBEAT_STATE.exists():
        try:
            state = json.loads(HEARTBEAT_STATE.read_text())
            context["session_number"] = state.get("sessionCount")
        except:
            pass

    # Load today.md for context
    if TODAY_MD.exists():
        content = TODAY_MD.read_text()
        # Extract working memory (first 10 lines)
        lines = content.split('\n')[:10]
        context["recent_work"] = [l.strip() for l in lines if l.strip() and not l.startswith('#')]

    # Load active goals
    if ACTIVE_GOALS.exists():
        content = ACTIVE_GOALS.read_text()
        # Extract high priority goals
        in_high_priority = False
        for line in content.split('\n'):
            if '## High Priority' in line:
                in_high_priority = True
            elif in_high_priority and line.startswith('- [ ]'):
                context["active_goals"].append(line.strip())

    return context

def print_session_start(context):
    """Print session start header"""
    print("=" * 60)
    print("🚀 SESSION START")
    print("=" * 60)
    print(f"Time: {context['timestamp']}")
    if context['session_number']:
        print(f"Session: #{context['session_number']}")
    print()

    if context['recent_work']:
        print("📝 Recent Work:")
        for item in context['recent_work'][:3]:
            print(f"  {item}")
        print()

    if context['active_goals']:
        print("🎯 Active Goals (Top 3):")
        for goal in context['active_goals'][:3]:
            # Clean up the formatting
            goal_clean = goal.replace('- [ ]', '').strip()
            print(f"  • {goal_clean}")
        print()

    print("=" * 60)
    print("Ready. What's the first work block?")
    print()

def update_diary_session_start():
    """Log session start to diary.md"""
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%MZ')
    entry = f"\n## [SESSION START — {timestamp}] New work session begins\n\nPick one task from goals/active.md or today.md. Execute. Document. Repeat.\n\n"

    if DIARY_MD.exists():
        content = DIARY_MD.read_text()
        # Add after the header line
        content = content.replace('# Nova', f'{entry}\n# Nova')
        DIARY_MD.write_text(content)

def main():
    import sys

    context = get_current_context()

    if "--context" in sys.argv:
        # Just show context, don't log
        print(json.dumps(context, indent=2))
        return

    # Print session header
    print_session_start(context)

    # Log to diary
    update_diary_session_start()
    print("✓ Logged to diary.md")

if __name__ == "__main__":
    main()
