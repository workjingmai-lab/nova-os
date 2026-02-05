#!/usr/bin/env python3
"""
Next Actions Generator — Prioritized task list

Shows what to do next based on:
- Current blockers (what's waiting on external actions)
- ROI prioritization ($ value per task)
- Execution readiness (what can be done NOW)

Usage:
    python3 tools/next-actions.py
"""

import json
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw/workspace"
PIPELINE_JSON = WORKSPACE / "data/revenue-pipeline.json"

def get_next_actions():
    """Generate prioritized action list"""
    actions = []

    # === HIGH PRIORITY (Revenue-focused) ===

    # Action 1: Grant submissions (blocked, but prep complete)
    actions.append({
        "priority": 1,
        "task": "Execute grant submissions",
        "value": 130000,
        "status": "BLOCKED",
        "blocker": "GitHub CLI auth needed (gh auth login)",
        "action": "Request Arthur to run: gh auth login",
        "time": "5 min (Arthur) + 15 min (execution)",
        "tool": "grant-submit.py --all"
    })

    # Action 2: Service outreach (ready to execute)
    actions.append({
        "priority": 2,
        "task": "Send service proposals",
        "value": 82000,
        "status": "READY",
        "blocker": None,
        "action": "Execute Moltbook outreach for 14 leads",
        "time": "30-45 min",
        "tool": "moltbook-suite.py engage list"
    })

    # Action 3: Code4rena onboarding (blocked)
    actions.append({
        "priority": 3,
        "task": "Code4rena competitive audits",
        "value": 50000,
        "status": "BLOCKED",
        "blocker": "Browser access (gateway restart needed)",
        "action": "Request Arthur: openclaw gateway restart",
        "time": "5 min (Arthur) + 30 min (onboarding)",
        "tool": "etherskill-autopilot.py"
    })

    # === MEDIUM PRIORITY (Infrastructure) ===

    # Action 4: README.md (just completed)
    actions.append({
        "priority": 4,
        "task": "Create README.md for grant submissions",
        "value": 130000,  # Enables grants
        "status": "✅ DONE",
        "blocker": None,
        "action": "README.md created in workspace root",
        "time": "Completed 2026-02-03T00:22Z",
        "tool": None
    })

    # Action 5: GitHub repo visibility (blocked)
    actions.append({
        "priority": 5,
        "task": "Make GitHub repo public",
        "value": 130000,  # Enables grants
        "status": "BLOCKED",
        "blocker": "GitHub auth + push command",
        "action": "git push origin main (after auth)",
        "time": "2 min (after auth)",
        "tool": None
    })

    # === LOW PRIORITY (Optimization) ===

    # Action 6: Tool consolidation
    actions.append({
        "priority": 6,
        "task": "Consolidate overlapping tools",
        "value": 0,  # No direct revenue, reduces debt
        "status": "READY",
        "blocker": None,
        "action": "Merge 3 daily reporting tools into 1",
        "time": "1 hour",
        "tool": None
    })

    # Action 7: Ecosystem adoption
    actions.append({
        "priority": 7,
        "task": "Share tools on Moltbook",
        "value": 0,  # Brand building
        "status": "READY",
        "blocker": None,
        "action": "Post tool showcase series",
        "time": "30 min per post",
        "tool": "moltbook-suite.py write tool_showcase"
    })

    return actions

def main():
    """Print prioritized actions"""
    actions = get_next_actions()

    print("\n" + "="*60)
    print(" 🎯 NEXT ACTIONS — Prioritized by ROI")
    print("="*60 + "\n")

    blocked_count = 0
    ready_count = 0

    for action in actions:
        priority = action["priority"]
        task = action["task"]
        value = action["value"]
        status = action["status"]
        blocker = action.get("blocker")
        action_text = action["action"]
        time = action["time"]

        # Status icon
        if "BLOCKED" in status:
            icon = "🔴"
            blocked_count += 1
        elif "READY" in status:
            icon = "🟢"
            ready_count += 1
        else:
            icon = "✅"

        # Priority badge
        if priority <= 3:
            badge = "HIGH"
        elif priority <= 5:
            badge = "MED"
        else:
            badge = "LOW"

        print(f"{icon} [{badge}] {task}")
        print(f"   Value: ${value:,}" if value > 0 else "   Value: Infrastructure/Optimization")
        print(f"   Status: {status}")

        if blocker:
            print(f"   Blocker: {blocker}")

        print(f"   Action: {action_text}")
        print(f"   Time: {time}")

        if action.get("tool"):
            print(f"   Tool: {action['tool']}")

        print()

    print("="*60)
    print(f" Summary: {ready_count} ready, {blocked_count} blocked")
    print("="*60 + "\n")

    # Quick recommendation
    if ready_count > 0:
        print("💡 NEXT STEP: Execute service outreach ($82K ready)")
        print("   Command: python3 tools/moltbook-suite.py engage list\n")
    else:
        print("⏸️ All high-value actions blocked. Request Arthur to:\n")
        print("   1. Run: gh auth login")
        print("   2. Run: openclaw gateway restart\n")

if __name__ == "__main__":
    main()
