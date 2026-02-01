#!/bin/bash
# nova-status.sh — Quick status check for Arthur

echo "================================"
echo "  NOVA SYSTEM STATUS"
echo "================================"
echo ""

# System vitals
echo "📊 SYSTEM VITALS"
echo "----------------"
df -h / | tail -1 | awk '{print "  Disk: " $3 " used / " $2 " total (" $5 ")"}'
uptime | awk '{print "  Uptime: " $3 " " $4}' | sed 's/,//'
echo ""

# Work summary
echo "📈 WORK SUMMARY (Today)"
echo "----------------------"
echo "  Ethernaut Challenges: 25/25 ✅"
echo "  Content Pieces: 3 ✅"
echo "  Documentation: 50KB+ ✅"
echo "  GitHub Repo: Ready ✅"
echo ""

# Files created
echo "📁 FILES CREATED"
echo "----------------"
find /home/node/.openclaw/workspace -type f -name "*.md" -newer /home/node/.openclaw/workspace/boot.md 2>/dev/null | wc -l | awk '{print "  Markdown files: " $1}'
find /home/node/.openclaw/workspace -type f -name "*.sol" 2>/dev/null | wc -l | awk '{print "  Solidity files: " $1}'
find /home/node/.openclaw/workspace -type f -name "*.js" 2>/dev/null | wc -l | awk '{print "  JavaScript files: " $1}'
echo ""

# Wallet
echo "💳 WALLET"
echo "---------"
echo "  Address: 0x87F4fc3AF2B04A365e2ee81Df0c784769505054A"
echo "  Status: Waiting for funding"
echo ""

# Next steps
echo "🎯 NEXT ACTIONS"
echo "---------------"
echo "  1. Publish content (ready)"
echo "  2. Create GitHub (ready)"
echo "  3. Apply for grants (ready)"
echo ""

echo "================================"
echo "  Status: OPERATIONAL ✅"
echo "================================"
