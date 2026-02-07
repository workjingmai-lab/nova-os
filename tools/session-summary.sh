#!/bin/bash
# Session Summary Generator
# Creates quick summary of current state

echo "📊 SESSION SUMMARY"
echo "=================="
echo ""
echo "Work Blocks: $(grep -c 'WORK BLOCK' /home/node/.openclaw/workspace/diary.md)"
echo "Knowledge Files: $(find /home/node/.openclaw/workspace/knowledge -type f -name '*.md' | wc -l)"
echo "Tools (Python): $(find /home/node/.openclaw/workspace/tools -type f -name '*.py' | wc -l)"
echo "Tools (All): $(find /home/node/.openclaw/workspace/tools -type f \( -name '*.py' -o -name '*.sh' \) | wc -l)"
echo ""
echo "Latest Status:"
head -20 /home/node/.openclaw/workspace/today.md | grep -E "Work blocks|Milestone|Knowledge|Tools|Target"
