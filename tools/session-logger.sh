#!/bin/bash
# session-logger.sh — Quick work session tracker
# Usage: ./session-logger.sh "task description"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%MZ")
TASK="$1"
STATUS="${2:-started}"

# Append to work log
echo "[$TIMESTAMP] [$STATUS] $TASK" >> /home/node/.openclaw/workspace/diary.md

# Quick summary
echo "✓ Logged: $TASK ($STATUS)"
echo "  Timestamp: $TIMESTAMP"
