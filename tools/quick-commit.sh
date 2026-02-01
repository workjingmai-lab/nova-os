#!/bin/bash
# quick-commit.sh — Fast git commit + push with timestamped message
# Usage: ./quick-commit.sh [optional custom message]

cd "/home/node/.openclaw/workspace" || exit 1

# Generate timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%MZ")
WORK_BLOCK=$(grep -c "WORK BLOCK" diary.md 2>/dev/null || echo "unknown")

# Custom message or default
if [ -n "$1" ]; then
    MSG="$1"
else
    MSG="Work block $WORK_BLOCK — $TIMESTAMP"
fi

# Check if there are changes
if [ -z "$(git status --porcelain)" ]; then
    echo "✨ No changes to commit"
    exit 0
fi

# Add everything
git add -A

# Commit
git commit -m "$MSG"

# Push
git push origin master

echo "✅ Committed and pushed: $MSG"
