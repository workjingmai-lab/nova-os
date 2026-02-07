#!/bin/bash
# Send Everything Script — One command to ship entire pipeline
# Usage: bash tools/send-everything.sh [quick|full|test]

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Workspace directory
WORKSPACE="$HOME/.openclaw/workspace"
cd "$WORKSPACE"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  SEND EVERYTHING — Pipeline Execution Script${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Parse command line argument
MODE="${1:-full}"  # Default to full mode

case "$MODE" in
  quick)
    echo -e "${YELLOW}MODE: QUICK (Grants only, ~15 min)${NC}"
    echo ""
    ;;
  full)
    echo -e "${YELLOW}MODE: FULL (Everything, ~40 min)${NC}"
    echo ""
    ;;
  test)
    echo -e "${YELLOW}MODE: TEST (Dry run, no actual sends)${NC}"
    echo ""
    ;;
  *)
    echo -e "${RED}Error: Unknown mode '$MODE'${NC}"
    echo "Usage: bash tools/send-everything.sh [quick|full|test]"
    exit 1
    ;;
esac

# Step 1: Check blockers
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 1: Checking Blockers${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check GitHub auth
if gh auth status &>/dev/null; then
    echo -e "${GREEN}✅ GitHub CLI: Authenticated${NC}"
else
    echo -e "${RED}❌ GitHub CLI: Not authenticated${NC}"
    echo -e "${YELLOW}   Run: gh auth login${NC}"
    echo -e "${YELLOW}   Blocker: $125K grants${NC}"

    if [ "$MODE" != "test" ]; then
        echo ""
        read -p "Authenticate GitHub now? (y/n) " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            gh auth login
        else
            echo -e "${RED}Skipping grants (GitHub auth required)${NC}"
        fi
    fi
fi

echo ""

# Check gateway status
GATEWAY_STATUS=$(openclaw gateway status 2>/dev/null || echo "unknown")
if [[ "$GATEWAY_STATUS" == *"running"* ]]; then
    echo -e "${GREEN}✅ Gateway: Running${NC}"
else
    echo -e "${YELLOW}⚠️  Gateway: Not running (restart needed for Code4rena)${NC}"
    echo -e "${YELLOW}   Run: openclaw gateway restart${NC}"
fi

echo ""
sleep 2

# Step 2: Pipeline status
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 2: Current Pipeline Status${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

python3 tools/execution-gap.py

echo ""
sleep 2

# Step 3: Confirm execution
if [ "$MODE" != "test" ]; then
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Step 3: Ready to Execute${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "This will:"
    if [ "$MODE" == "full" ]; then
        echo "  • Send EXPERT tier messages (10 × $66-122K)"
        echo "  • Send TACTICAL tier messages (19 × $14-19K)"
        echo "  • Send HIGH/MEDIUM messages (10 × $30K)"
        echo "  • Submit 5 grant applications ($125K total)"
    elif [ "$MODE" == "quick" ]; then
        echo "  • Submit 5 grant applications ($125K total)"
    fi
    echo ""
    read -p "Continue? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Aborted by user${NC}"
        exit 0
    fi
    echo ""
fi

# Step 4: Execute
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 4: Sending Messages${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$MODE" == "test" ]; then
    echo -e "${YELLOW}[TEST MODE] Would send:${NC}"
    echo "  • EXPERT tier: 10 messages ($660-1,220K)"
    echo "  • TACTICAL tier: 19 messages ($268-357K)"
    echo "  • HIGH/MEDIUM: 10 messages ($305K)"
    echo "  • Grants: 5 applications ($125K)"
    echo ""
    echo -e "${YELLOW}[TEST MODE] Total: ~$1.3M-1.9M in 40 minutes${NC}"

elif [ "$MODE" == "full" ]; then
    # Send EXPERT tier
    echo -e "${BLUE}Sending EXPERT tier...${NC}"
    python3 tools/service-batch-send.py --expert || echo -e "${YELLOW}⚠️  EXPERT tier send skipped (see errors above)${NC}"
    echo ""

    # Send TACTICAL tier
    echo -e "${BLUE}Sending TACTICAL tier...${NC}"
    python3 tools/service-batch-send.py --tactical || echo -e "${YELLOW}⚠️  TACTICAL tier send skipped (see errors above)${NC}"
    echo ""

    # Send top 10 HIGH/MEDIUM
    echo -e "${BLUE}Sending top 10 HIGH/MEDIUM...${NC}"
    python3 tools/service-batch-send.py --top 10 || echo -e "${YELLOW}⚠️  Top 10 send skipped (see errors above)${NC}"
    echo ""

    # Submit grants
    echo -e "${BLUE}Submitting grant applications...${NC}"
    python3 tools/grant-batch-submit.py --all || echo -e "${YELLOW}⚠️  Grant submission skipped (GitHub auth may be required)${NC}"
    echo ""

elif [ "$MODE" == "quick" ]; then
    # Submit grants only
    echo -e "${BLUE}Submitting grant applications...${NC}"
    python3 tools/grant-batch-submit.py --all || echo -e "${YELLOW}⚠️  Grant submission failed (GitHub auth required)${NC}"
    echo ""
fi

# Step 5: Setup follow-up tracking
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 5: Setup Follow-up Tracking${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$MODE" != "test" ]; then
    echo -e "${BLUE}Setting up follow-up reminders...${NC}"
    python3 tools/followup-reminder.py schedule
    echo ""
fi

# Step 6: Final status
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Step 6: Final Pipeline Status${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

python3 tools/execution-gap.py

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ SEND EVERYTHING COMPLETE${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo "  1. Check for responses daily"
echo "  2. Run: python3 tools/followup-reminder.py check"
echo "  3. Follow up on Day 3/7/14/21 using templates in outreach/templates/"
echo ""
echo "Track progress:"
echo "  • python3 tools/revenue-tracker.py status"
echo "  • cat EXECUTION-DASHBOARD.md"
echo ""
echo -e "${BLUE}Small executions compound. The math works. ✨${NC}"
echo ""
