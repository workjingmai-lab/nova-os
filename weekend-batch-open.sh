#!/bin/bash
# weekend-batch-open.sh — Open all 5 WEEKEND-BATCH message files
# Usage: ./weekend-batch-open.sh

echo "Opening WEEKEND-BATCH messages (5 sends, 30 min, $200.5K)..."
echo ""

# Check if files exist
files=(
    "outreach/messages/ethereum-foundation-agent-automation.md"
    "outreach/messages/uniswap-devx-automation.md"
    "outreach/messages/fireblocks-security-automation.md"
    "outreach/messages/makerdao-governance-automation.md"
    "outreach/messages/aave-ecosystem-automation.md"
)

for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Message not found: $file"
        exit 1
    fi
done

# Batch 1: HIGH priority ($115K)
echo "═══════════════════════════════════════"
echo "  BATCH 1: HIGH PRIORITY ($115K)"
echo "═══════════════════════════════════════"
echo ""

echo "📧 Send #1: Ethereum Foundation ($40K)"
cat outreach/messages/ethereum-foundation-agent-automation.md | head -15
echo ""
read -p "--- Copy above, send, then press Enter ---"
echo ""

echo "📧 Send #2: Uniswap DevX ($40K)"
cat outreach/messages/uniswap-devx-automation.md | head -15
echo ""
read -p "--- Copy above, send, then press Enter ---"
echo ""

echo "📧 Send #3: Fireblocks Security ($35K)"
cat outreach/messages/fireblocks-security-automation.md | head -15
echo ""
read -p "--- Copy above, send, then press Enter for Batch 2 ---"
echo ""

# Batch 2: MEDIUM priority ($62.5K)
echo "═══════════════════════════════════════"
echo "  BATCH 2: MEDIUM PRIORITY ($62.5K)"
echo "═══════════════════════════════════════"
echo ""

echo "📧 Send #4: MakerDAO Governance ($32.5K)"
cat outreach/messages/makerdao-governance-automation.md | head -15
echo ""
read -p "--- Copy above, send, then press Enter ---"
echo ""

echo "📧 Send #5: Aave Ecosystem ($30K)"
cat outreach/messages/aave-ecosystem-automation.md | head -15
echo ""
echo "--- Copy above, send, DONE ---"
echo ""

echo "💰 $200.5K in motion. Update tracker:"
echo "   python3 revenue-tracker.py update 'Ethereum Foundation' sent"
echo "   python3 revenue-tracker.py update 'Uniswap' sent"
echo "   python3 revenue-tracker.py update 'Fireblocks' sent"
echo "   python3 revenue-tracker.py update 'MakerDAO' sent"
echo "   python3 revenue-tracker.py update 'Aave' sent"
