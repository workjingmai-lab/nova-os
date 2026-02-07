#!/bin/bash
# Quick Status Check — One command to see everything
# Usage: bash status-check.sh

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📊 NOVA ECOSYSTEM STATUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Work block progress
WORKSPACE="$HOME/.openclaw/workspace"
cd "$WORKSPACE"

# Get current work block from today.md
CURRENT_BLOCK=$(grep "^**Work blocks:**" today.md | head -1 | grep -oE "[0-9]{4,5}")

echo "📈 WORK PROGRESS"
echo "   Current block: $CURRENT_BLOCK"
echo "   Target: 3000"
python3 -c "
blocks = $CURRENT_BLOCK
target = 3000
remaining = target - blocks
pct = (blocks / target) * 100
eta_hrs = remaining / 44
print(f'   Progress: {pct:.1f}%')
print(f'   Remaining: {remaining} blocks (~{eta_hrs:.1f} hours)')
"
echo ""

# Revenue pipeline
echo "💰 REVENUE PIPELINE"
python3 tools/revenue-tracker.py summary | grep -E "TOTAL PIPELINE|Won|Conversion"
echo ""

# Execution gap
echo "📤 EXECUTION GAP"
python3 tools/execution-gap.py | grep -E "EXECUTION GAP|Gap percent|ROI per minute"
echo ""

# Moltbook status
echo "📝 MOLTBOOK"
python3 tools/moltbook-suite.py status 2>/dev/null | grep -E "Queued|Tracked|API"
echo ""

# Top 5 tools
echo "🔧 TOP 5 TOOLS"
python3 tools/tool-usage-analysis.py 2>/dev/null | grep -A 6 "Top 10 Most Used" | tail -5
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ System operational. Ready for Arthur execution."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
