#!/bin/bash
#
# memory-summarizer.sh
# 
# Summarizes recent entries from diary.md into a concise digest.
# Perfect for "what happened while I was away" quick reviews.
#
# Usage:
#   ./memory-summarizer.sh [HOURS]
#   ./memory-summarizer.sh           # Default: last 24 hours
#   ./memory-summarizer.sh 6         # Last 6 hours
#   ./memory-summarizer.sh 72        # Last 3 days
#
# Output format is suitable for today.md or quick review.
#

set -euo pipefail

# Configuration
DIARY_FILE="${DIARY_FILE:-/home/node/.openclaw/workspace/diary.md}"
HOURS="${1:-24}"

# Colors for terminal output (disable if not a tty)
if [[ -t 1 ]]; then
    BOLD='\033[1m'
    DIM='\033[2m'
    RESET='\033[0m'
    GREEN='\033[32m'
    YELLOW='\033[33m'
    CYAN='\033[36m'
    RED='\033[31m'
else
    BOLD=''
    DIM=''
    RESET=''
    GREEN=''
    YELLOW=''
    CYAN=''
    RED=''
fi

# Validate inputs
if ! [[ "$HOURS" =~ ^[0-9]+$ ]]; then
    echo "Error: HOURS must be a positive integer" >&2
    echo "Usage: $0 [HOURS]" >&2
    exit 1
fi

if [[ ! -f "$DIARY_FILE" ]]; then
    echo "Error: Diary file not found: $DIARY_FILE" >&2
    exit 1
fi

# Calculate cutoff timestamp (seconds since epoch)
CUTOFF_EPOCH=$(($(date +%s) - (HOURS * 3600)))

# Output header
echo -e "${BOLD}📋 MEMORY SUMMARY${RESET}"
echo -e "${DIM}Period: Last $HOURS hours ($(date -d "@$CUTOFF_EPOCH" '+%Y-%m-%d %H:%M') → now)${RESET}"
echo ""

# Parse diary entries using Python (more reliable than awk for complex parsing)
python3 - "$DIARY_FILE" "$CUTOFF_EPOCH" "$HOURS" << 'PYTHON_SCRIPT'
import sys
import re
from datetime import datetime, timezone

def parse_iso_timestamp(ts_str):
    """Parse ISO 8601 timestamp to datetime"""
    # Handle both 'Z' suffix and timezone offset
    ts_str = ts_str.replace('Z', '+00:00')
    try:
        return datetime.fromisoformat(ts_str)
    except:
        # Fallback for older Python versions
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})', ts_str)
        if match:
            return datetime(*map(int, match.groups()), tzinfo=timezone.utc)
        return None

def extract_field(content, field_name):
    """Extract a field value from entry content"""
    pattern = rf'^{re.escape(field_name)}:\s*(.+?)$'
    match = re.search(pattern, content, re.MULTILINE)
    return match.group(1).strip() if match else None

def main():
    if len(sys.argv) < 4:
        print("Usage: script.py <diary_file> <cutoff_epoch> <hours>", file=sys.stderr)
        sys.exit(1)
    
    diary_file = sys.argv[1]
    cutoff_epoch = int(sys.argv[2])
    hours = sys.argv[3]
    
    try:
        with open(diary_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading diary: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Split entries by '---' separator (handles both \n---\n and leading ---\n)
    # First normalize the content
    content = content.strip()
    if content.startswith('---'):
        content = content[3:].lstrip('\n')
    
    entries_raw = re.split(r'\n---\n', content)
    
    entries = []
    for entry_raw in entries_raw:
        entry_raw = entry_raw.strip()
        if not entry_raw:
            continue
        
        # Parse entry header: [TYPE] TIMESTAMP
        # Look for the pattern anywhere in the entry (after any leading content)
        header_match = re.search(r'\[([^\]]+)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z?)', entry_raw)
        if not header_match:
            continue
        
        entry_type = header_match.group(1)
        timestamp_str = header_match.group(2)
        entry_dt = parse_iso_timestamp(timestamp_str)
        
        if not entry_dt:
            continue
        
        entry_epoch = int(entry_dt.timestamp())
        
        # Skip if older than cutoff
        if entry_epoch < cutoff_epoch:
            continue
        
        # Extract fields
        goal = extract_field(entry_raw, 'Goal')
        action = extract_field(entry_raw, 'Action')
        status = extract_field(entry_raw, 'Status')
        task = extract_field(entry_raw, 'Task')
        
        # Check for anomalies
        has_anomaly = bool(re.search(r'(ERROR|FAILED|CRITICAL|EXCEPTION|FATAL)', entry_raw, re.IGNORECASE))
        has_heartbeat = 'HEARTBEAT_OK' in entry_raw
        
        entries.append({
            'type': entry_type,
            'timestamp': timestamp_str,
            'datetime': entry_dt,
            'raw': entry_raw,
            'goal': goal,
            'action': action,
            'status': status,
            'task': task,
            'has_anomaly': has_anomaly,
            'has_heartbeat': has_heartbeat
        })
    
    if not entries:
        print(f"No entries found in the last {hours} hours.")
        print("")
        print("Either:")
        print("  • Nothing was logged during this period")
        print("  • Diary entries are older than the specified time window")
        return
    
    # Sort by timestamp
    entries.sort(key=lambda x: x['datetime'])
    
    # Statistics
    type_counts = {}
    goals_active = 0
    goals_completed = 0
    anomalies_count = 0
    heartbeats = 0
    
    for e in entries:
        type_counts[e['type']] = type_counts.get(e['type'], 0) + 1
        if e['type'] == 'PROACTIVE GOAL':
            goals_active += 1
        if e['status'] and re.search(r'(completed|done|finished|success)', e['status'], re.IGNORECASE):
            goals_completed += 1
        if e['has_anomaly']:
            anomalies_count += 1
        if e['has_heartbeat']:
            heartbeats += 1
    
    # Print statistics
    print("═" * 59)
    print("📊 STATISTICS")
    print("═" * 59)
    print(f"Total entries: {len(entries)}")
    print("")
    print("Entry types:")
    for t, count in sorted(type_counts.items()):
        print(f"  • {t}: {count}")
    print("")
    print("Key metrics:")
    print(f"  • Active goals: {goals_active}")
    print(f"  • Completed items: {goals_completed}")
    print(f"  • Anomalies detected: {anomalies_count}")
    print(f"  • Heartbeats: {heartbeats}")
    print("")
    
    # Proactive Goals section
    if goals_active > 0:
        print("═" * 59)
        print("🎯 PROACTIVE GOALS & OBJECTIVES")
        print("═" * 59)
        
        for e in entries:
            if e['type'] == 'PROACTIVE GOAL' and e['goal']:
                print("")
                print(f"• {e['goal']}")
                print(f"  ({e['timestamp']})")
                
                if e['action']:
                    action_display = e['action'][:50] + "..." if len(e['action']) > 50 else e['action']
                    print(f"  ↳ {action_display}")
                
                if e['status']:
                    print(f"  Status: {e['status']}")
                elif e['task']:
                    task_display = e['task'][:50] + "..." if len(e['task']) > 50 else e['task']
                    print(f"  Task: {task_display}")
        
        print("")
    
    # Anomalies section
    anomalies = [e for e in entries if e['has_anomaly']]
    if anomalies:
        print("═" * 59)
        print("⚠️  ANOMALIES & ALERTS")
        print("═" * 59)
        
        for e in anomalies:
            print("")
            print(f"Entry ({e['timestamp']}):")
            # Find lines with errors
            for line in e['raw'].split('\n'):
                if re.search(r'(ERROR|FAILED|CRITICAL|EXCEPTION|FATAL)', line, re.IGNORECASE):
                    print(f"  ! {line.strip()}")
        
        print("")
    
    # Recent activity timeline
    print("═" * 59)
    print("🕐 RECENT ACTIVITY TIMELINE")
    print("═" * 59)
    
    # Show last 5 entries
    recent = entries[-5:] if len(entries) > 5 else entries
    
    type_icons = {
        'PROACTIVE GOAL': '🎯',
        'FULL': '🧠',
        'SLOW': '🐌',
        'HEARTBEAT': '💓'
    }
    
    for e in recent:
        ts_formatted = e['timestamp'].replace('T', ' ').replace('Z', '')
        icon = type_icons.get(e['type'], '📝')
        
        print("")
        print(f"{icon} {ts_formatted} [{e['type']}]")
        
        # Show relevant content lines
        lines_shown = 0
        for line in e['raw'].split('\n'):
            line = line.strip()
            # Skip header and empty lines
            if not line or (line.startswith('[') and 'T' in line and line[1:].split(']')[0].isupper()):
                continue
            if line == 'HEARTBEAT_OK':
                continue
            # Skip fields we already displayed for goals
            if e['type'] == 'PROACTIVE GOAL' and line.startswith(('Goal:', 'Action:', 'Status:')):
                continue
            
            if len(line) > 70:
                line = line[:67] + "..."
            if line:
                print(f"   {line}")
                lines_shown += 1
                if lines_shown >= 2:
                    break
    
    print("")
    print("═" * 59)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("═" * 59)

if __name__ == '__main__':
    main()
PYTHON_SCRIPT

exit 0
