#!/bin/bash
# Nova Quickstart - One command to see everything I've built

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                    ✨ NOVA QUICKSTART                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Status
echo "📊 CURRENT STATUS:"
python3 tools/nova-status.py 2>/dev/null || echo "   Run: python3 tools/nova-status.py"
echo ""

# Recent work
echo "🔥 RECENT TOOLS (last 5):"
ls -lt tools/*.py 2>/dev/null | head -6 | tail -5 | awk '{print "   " $9}'
echo ""

# Latest report
echo "📈 LATEST REPORT:"
ls -lt reports/*.md 2>/dev/null | head -2 | tail -1 | awk '{print "   " $9}'
echo ""

# Key files
echo "📁 KEY LOCATIONS:"
echo "   knowledge/    → Curated learnings (25 files)"
echo "   tools/        → Automation scripts (38 tools)"
echo "   reports/      → Generated analysis"
echo "   diary.md      → Activity log"
echo "   goals/        → Active targets"
echo ""

# Quick actions
echo "⚡ QUICK ACTIONS:"
echo "   make status      → Full status check"
echo "   make heartbeat   → Run heartbeat manually"
echo "   make clean       → Cleanup old files"
echo ""
echo "   python3 tools/nova-status.py     → Quick status"
echo "   python3 tools/goal-tracker.py    → Goal progress"
echo "   python3 tools/self-improvement-loop.py → Analysis"
echo ""
