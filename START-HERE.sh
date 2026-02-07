#!/bin/bash
# START-HERE.sh — Arthur's Entry Point
# Run this to see current status and what to do next

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  NOVA STATUS DASHBOARD — $(date '+%Y-%m-%d %H:%M UTC')"                
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Run status dashboard
python3 nova-status.py 2>/dev/null || echo "⚠️  nova-status.py not found"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🚀 NEXT ACTIONS (Pick One)                                   ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║                                                              ║"
echo "║  1. GATEWAY RESTART  (1 min → unblock $50K bounties)        ║"
echo "║     → openclaw gateway restart                               ║"
echo "║                                                              ║"
echo "║  2. GITHUB AUTH      (5 min → unblock $125K grants)         ║"
echo "║     → gh auth login                                          ║"
echo "║                                                              ║"
echo "║  3. SEND MESSAGES    (36 min → $332K services)              ║"
echo "║     → See: SERVICE-OUTREACH-EXECUTION-GUIDE.md               ║"
echo "║                                                              ║"
echo "║  4. SUBMIT GRANTS    (15 min → $125K grants)                ║"
echo "║     → See: GRANT-SUBMISSION-QUICK-REF.md                     ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "💡 Tip: Run ./START-HERE.sh anytime for fresh status"
echo ""
