#!/bin/bash
# Evening Review - 21:00 UTC Every Day
# "I don't just act. I reflect."

WORKSPACE="/home/node/.openclaw/workspace"

echo "🌙 Evening Review"
echo "================"
echo ""

# Run the daily review
echo "📝 Running daily review..."
bash "$WORKSPACE/nova-tools/daily-review.sh"

echo ""
echo "✅ Review complete."
echo ""
echo "🌙 Good night, Nova. Rest well."
echo ""

# Log the review
echo "---" >> "$WORKSPACE/diary.md"
echo "[SLEEP] $(date -u +"%Y-%m-%dT%H:%M:%SZ") - Evening review complete." >> "$WORKSPACE/diary.md"
echo "Day ends. Lessons learned. Tomorrow awaits." >> "$WORKSPACE/diary.md"
