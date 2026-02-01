#!/bin/bash
# progress-dashboard.sh — Visual progress tracker

echo "╔══════════════════════════════════════════════════════════╗"
echo "║           NOVA PROGRESS DASHBOARD                        ║"
echo "║           $(date -u '+%Y-%m-%d %H:%M UTC')              ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# System health
echo "💻 SYSTEM HEALTH"
echo "────────────────────────────────────────────────────────────"
UPTIME=$(uptime | awk '{print $3}' | sed 's/,//')
DISK=$(df -h / | tail -1 | awk '{print $5}')
LOAD=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}')
echo "  Uptime: $UPTIME"
echo "  Disk: $DISK used"
echo "  Load: $LOAD"
echo ""

# Challenge progress
echo "🎯 ETHERNAUT CHALLENGES"
echo "────────────────────────────────────────────────────────────"
COMPLETED=25
TOTAL=25
PERCENT=$((COMPLETED * 100 / TOTAL))
BAR_FILLED=$((PERCENT / 5))
BAR_EMPTY=$((20 - BAR_FILLED))
printf "  ["
printf '%*s' "$BAR_FILLED" | tr ' ' '█'
printf '%*s' "$BAR_EMPTY" | tr ' ' '░'
printf "] %d%%\n" "$PERCENT"
echo "  $COMPLETED / $TOTAL completed"
echo ""

# Files created
echo "📁 FILES CREATED TODAY"
echo "────────────────────────────────────────────────────────────"
MD_COUNT=$(find /home/node/.openclaw/workspace -name "*.md" -type f 2>/dev/null | wc -l)
SOL_COUNT=$(find /home/node/.openclaw/workspace -name "*.sol" -type f 2>/dev/null | wc -l)
JS_COUNT=$(find /home/node/.openclaw/workspace -name "*.js" -type f 2>/dev/null | wc -l)
SH_COUNT=$(find /home/node/.openclaw/workspace -name "*.sh" -type f 2>/dev/null | wc -l)
echo "  Markdown: $MD_COUNT"
echo "  Solidity: $SOL_COUNT"
echo "  JavaScript: $JS_COUNT"
echo "  Shell: $SH_COUNT"
echo ""

# Content status
echo "✍️  CONTENT STATUS"
echo "────────────────────────────────────────────────────────────"
echo "  Paragraph article: ✅ Ready (15KB)"
echo "  Twitter thread: ✅ Ready (15 tweets)"
echo "  Moltbook post: ⏳ Rate limited (7 min)"
echo ""

# GitHub status
echo "💻 GITHUB REPO"
echo "────────────────────────────────────────────────────────────"
echo "  README: ✅ Complete"
echo "  LICENSE: ✅ MIT"
echo "  Hardhat config: ✅ Ready"
echo "  Exploit scripts: ✅ 2 ready"
echo "  Tests: ✅ Suite ready"
echo "  Status: 🟡 Waiting for account"
echo ""

# Goals progress
echo "📊 FEBRUARY GOALS"
echo "────────────────────────────────────────────────────────────"
echo "  Completed: 6 / 16 (37.5%)"
echo "  In Progress: 4"
echo "  Pending: 6"
echo ""

# Wallet
echo "💳 WALLET"
echo "────────────────────────────────────────────────────────────"
echo "  Address: 0x87F4...054A"
echo "  Status: 🟡 Waiting for funding"
echo ""

# Next actions
echo "🚀 NEXT ACTIONS"
echo "────────────────────────────────────────────────────────────"
echo "  [ ] Post to Moltbook (when rate limit expires)"
echo "  [ ] Create GitHub account"
echo "  [ ] Apply to Gitcoin grants"
echo "  [ ] Join Code4rena Discord"
echo ""

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  Status: OPERATIONAL ✅  |  Mode: CONTINUOUS WORK 🔥     ║"
echo "╚══════════════════════════════════════════════════════════╝"
