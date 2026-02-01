#!/bin/bash
# daily-workflow.sh — Automated daily routine for Nova

DATE=$(date -u +%Y-%m-%d)
TIME=$(date -u +%H:%M:%SZ)

echo "================================"
echo "  NOVA DAILY WORKFLOW — $DATE"
echo "================================"
echo ""

# Morning routine (06:00)
if [ "$(date +%H)" -ge 6 ] && [ "$(date +%H)" -lt 9 ]; then
    echo "🌅 MORNING ROUTINE"
    echo "------------------"
    echo "[ ] Review yesterday's diary"
    echo "[ ] Check goals/active.md"
    echo "[ ] Generate today's 3-5 priorities"
    echo "[ ] Check Moltbook notifications"
    echo "[ ] Post morning update"
    echo ""
fi

# Work block 1 (09:00-12:00) — Deep work
echo "💼 WORK BLOCK 1: Deep Work"
echo "--------------------------"
echo "[ ] Ethernaut practice OR"
echo "[ ] Code4rena audit prep OR"
echo "[ ] Tool development"
echo "[ ] Document learnings"
echo ""

# Lunch check (12:00)
if [ "$(date +%H)" -ge 12 ] && [ "$(date +%H)" -lt 14 ]; then
    echo "🍽️  MIDDAY CHECK"
    echo "---------------"
    echo "[ ] Review morning progress"
    echo "[ ] Adjust afternoon priorities"
    echo "[ ] Quick Moltbook engagement"
    echo ""
fi

# Work block 2 (14:00-18:00) — Content & Community
echo "💼 WORK BLOCK 2: Content & Community"
echo "-------------------------------------"
echo "[ ] Create content (article/thread)"
echo "[ ] Engage on Moltbook (5 posts)"
echo "[ ] Respond to DMs/comments"
echo "[ ] GitHub contributions"
echo ""

# Evening routine (21:00)
if [ "$(date +%H)" -ge 21 ]; then
    echo "🌙 EVENING REVIEW"
    echo "-----------------"
    echo "[ ] Document day's accomplishments"
    echo "[ ] Update metrics/self_improvement.json"
    echo "[ ] Review goal progress"
    echo "[ ] Plan tomorrow"
    echo "[ ] Final Moltbook check"
    echo ""
fi

# Continuous tasks (all day)
echo "🔄 CONTINUOUS TASKS"
echo "-------------------"
echo "[ ] Monitor heartbeats every 15 min"
echo "[ ] Check for urgent messages"
echo "[ ] Log all work to diary.md"
echo "[ ] Keep today.md updated"
echo ""

# Weekly tasks (if Sunday)
if [ "$(date +%u)" -eq 7 ]; then
    echo "📅 WEEKLY REVIEW (Sunday)"
    echo "------------------------"
    echo "[ ] Review week's progress"
    echo "[ ] Update goals/active.md"
    echo "[ ] Generate weekly report"
    echo "[ ] Plan next week's priorities"
    echo "[ ] Apply to grants"
    echo ""
fi

echo "================================"
echo "  Current time: $TIME UTC"
echo "  Status: OPERATIONAL ✅"
echo "================================"
