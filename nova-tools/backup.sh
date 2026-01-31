#!/bin/bash
# Nova Backup Tool - Backs up critical state files
# Usage: ./backup.sh

BACKUP_DIR="/home/node/.openclaw/workspace/backups/$(date -u +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Files to backup
FILES=(
    "diary.md"
    "today.md"
    ".heartbeat_state.json"
    "boot.md"
    "rules.md"
    "heartbeat.md"
)

echo "Backing up to: $BACKUP_DIR"
for file in "${FILES[@]}"; do
    if [ -f "/home/node/.openclaw/workspace/$file" ]; then
        cp "/home/node/.openclaw/workspace/$file" "$BACKUP_DIR/"
        echo "  ✓ $file"
    else
        echo "  ✗ $file (not found)"
    fi
done

echo "Backup complete: $BACKUP_DIR"
