#!/bin/bash
# today-only-open.sh — Open all 3 TODAY-ONLY message files at once
# Usage: ./today-only-open.sh

echo "Opening TODAY-ONLY messages..."
echo ""

# Check if files exist
if [ ! -f "outreach/messages/ethereum-foundation-agent-automation.md" ]; then
    echo "❌ Ethereum Foundation message not found"
    exit 1
fi

if [ ! -f "outreach/messages/uniswap-devx-automation.md" ]; then
    echo "❌ Uniswap message not found"
    exit 1
fi

if [ ! -f "outreach/messages/fireblocks-security-automation.md" ]; then
    echo "❌ Fireblocks message not found"
    exit 1
fi

# Open files (use your preferred editor or just cat for quick view)
echo "📧 Send #1: Ethereum Foundation ($40K)"
cat outreach/messages/ethereum-foundation-agent-automation.md | head -20
echo ""
echo "--- Copy above, send, then continue ---"
echo ""

read -p "Press Enter for Send #2..."
echo ""
echo "📧 Send #2: Uniswap DevX ($40K)"
cat outreach/messages/uniswap-devx-automation.md | head -20
echo ""
echo "--- Copy above, send, then continue ---"
echo ""

read -p "Press Enter for Send #3..."
echo ""
echo "📧 Send #3: Fireblocks Security ($35K)"
cat outreach/messages/fireblocks-security-automation.md | head -20
echo ""
echo "--- Copy above, send, DONE ---"
echo ""

echo "💰 $115K in motion. Update tracker:"
echo "   python3 revenue-tracker.py update 'Ethereum Foundation' sent"
echo "   python3 revenue-tracker.py update 'Uniswap' sent"
echo "   python3 revenue-tracker.py update 'Fireblocks' sent"
