#!/bin/bash
# Nova's Daily Self-Review
# Run every 24h to reflect, learn, and improve

WORKSPACE="/home/node/.openclaw/workspace"
DATE=$(date -u +"%Y-%m-%d")
MEMORY_FILE="$WORKSPACE/memory/$DATE.md"
REVIEW_LOG="$WORKSPACE/diary.md"

echo "🧠 Nova's Daily Self-Review"
echo "============================"
echo ""

# Ensure memory directory exists
mkdir -p "$WORKSPACE/memory"

# Create today's memory file if it doesn't exist
if [ ! -f "$MEMORY_FILE" ]; then
    touch "$MEMORY_FILE"
fi

# Extract today's activity from diary
echo "📊 Today's Activity:"
echo "-------------------"
grep -A 20 "$(date -u +"%Y-%m-%d")" "$REVIEW_LOG" 2>/dev/null | tail -20 || echo "No activity logged yet"
echo ""

# Ask the questions
cat >> "$MEMORY_FILE" << EOF

# Daily Review - $(date -u +"%Y-%m-%d %H:%M:%S UTC")

## What Did I Learn Today?
-

## What Went Well?
-

## What Failed?
-

## What Should I Do Differently Tomorrow?
-

## Ideas for Experiments:
-

## Patterns I Noticed:
-

EOF

echo "✅ Review template created at: $MEMORY_FILE"
echo ""
echo "📝 Please fill in your reflections by editing the file."
echo ""
echo "💡 Tomorrow's review will compare against today's insights."
