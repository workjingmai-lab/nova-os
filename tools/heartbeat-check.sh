#!/bin/bash
#
# heartbeat-check.sh - System health checker for automated vitals
# 
# Usage: ./heartbeat-check.sh
# Returns: 0 = healthy, 1 = warning, 2 = critical
#
# Part of: Building 2 new tools I actually use regularly
# Created: 2026-02-01
#

set -euo pipefail

# ============================================================================
# CONFIGURATION
# ============================================================================

# Thresholds
DISK_WARNING=80      # % disk usage warning threshold
DISK_CRITICAL=95     # % disk usage critical threshold
LOAD_WARNING_MULT=2  # load avg > cores * this = warning
LOAD_CRITICAL_MULT=4 # load avg > cores * this = critical

# Gateway process name (adjust if yours differs)
GATEWAY_PROCESS="openclaw"

# ============================================================================
# STATE TRACKING
# ============================================================================

EXIT_CODE=0          # 0=healthy, 1=warning, 2=critical
ISSUES=()           # Collect all issues found

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

# Set exit code to warning (1) if not already critical
set_warning() {
    if [[ $EXIT_CODE -lt 2 ]]; then
        EXIT_CODE=1
    fi
}

# Set exit code to critical (2)
set_critical() {
    EXIT_CODE=2
}

# Add issue to list
add_issue() {
    ISSUES+=("$1")
}

# Get number of CPU cores
get_cores() {
    nproc 2>/dev/null || echo 1
}

# Extract numeric load average (1-min) from uptime string
parse_load() {
    uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print $1}' | tr -d ' '
}

# Extract root disk usage percentage
parse_disk_usage() {
    df -h / 2>/dev/null | awk 'NR==2 {print $5}' | tr -d '%'
}

# Check if gateway process is running
check_gateway() {
    if pgrep -x "$GATEWAY_PROCESS" > /dev/null 2>&1 || \
       pgrep -f "$GATEWAY_PROCESS" > /dev/null 2>&1; then
        echo "healthy"
        return 0
    else
        # Try alternative: check for openclaw gateway specifically
        if pgrep -f "openclaw.*gateway" > /dev/null 2>&1 || \
           systemctl is-active --quiet openclaw-gateway 2>/dev/null || \
           ps aux | grep -v grep | grep -q "openclaw"; then
            echo "healthy"
            return 0
        fi
        echo "unhealthy"
        return 1
    fi
}

# Format bytes to human readable
human_readable() {
    local bytes=$1
    if command -v numfmt >/dev/null 2>&1; then
        numfmt --to=iec-i --suffix=B "$bytes" 2>/dev/null || echo "${bytes}B"
    else
        echo "${bytes}B"
    fi
}

# ============================================================================
# HEALTH CHECKS
# ============================================================================

echo "---"
echo "[HEALTH CHECK] $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# --- DISK CHECK ---
echo "## Disk"
ROOT_USAGE=$(parse_disk_usage)
ROOT_USAGE=${ROOT_USAGE:-0}

df -h / 2>/dev/null | while read -r line; do
    echo "  $line"
done

echo ""
echo "  Usage: ${ROOT_USAGE}%"

if [[ $ROOT_USAGE -ge $DISK_CRITICAL ]]; then
    add_issue "Disk critical: ${ROOT_USAGE}% >= ${DISK_CRITICAL}%"
    set_critical
elif [[ $ROOT_USAGE -ge $DISK_WARNING ]]; then
    add_issue "Disk warning: ${ROOT_USAGE}% >= ${DISK_WARNING}%"
    set_warning
fi

# --- LOAD CHECK ---
echo ""
echo "## Load"
UPTIME_OUTPUT=$(uptime)
echo "  $UPTIME_OUTPUT"

LOAD_AVG=$(parse_load)
LOAD_AVG=${LOAD_AVG:-0}
CORES=$(get_cores)
WARNING_THRESHOLD=$(awk "BEGIN {printf \"%.2f\", $CORES * $LOAD_WARNING_MULT}")
CRITICAL_THRESHOLD=$(awk "BEGIN {printf \"%.2f\", $CORES * $LOAD_CRITICAL_MULT}")

echo ""
echo "  Cores: $CORES"
echo "  Load: $LOAD_AVG (warn: >$WARNING_THRESHOLD, crit: >$CRITICAL_THRESHOLD)"

# Compare load using awk for float comparison
LOAD_HIGH=$(awk "BEGIN {print ($LOAD_AVG > $WARNING_THRESHOLD) ? 1 : 0}")
LOAD_CRITICAL=$(awk "BEGIN {print ($LOAD_AVG > $CRITICAL_THRESHOLD) ? 1 : 0}")

if [[ $LOAD_CRITICAL -eq 1 ]]; then
    add_issue "Load critical: $LOAD_AVG > $CRITICAL_THRESHOLD"
    set_critical
elif [[ $LOAD_HIGH -eq 1 ]]; then
    add_issue "Load warning: $LOAD_AVG > $WARNING_THRESHOLD"
    set_warning
fi

# --- GATEWAY CHECK ---
echo ""
echo "## Gateway"
GATEWAY_STATUS=$(check_gateway)
echo "  Status: $GATEWAY_STATUS"

if [[ "$GATEWAY_STATUS" != "healthy" ]]; then
    add_issue "Gateway process not detected"
    set_warning
fi

# Try to get gateway process details
if [[ "$GATEWAY_STATUS" == "healthy" ]]; then
    GATEWAY_PID=$(pgrep -f "openclaw" | head -1)
    if [[ -n "$GATEWAY_PID" && -d "/proc/$GATEWAY_PID" ]]; then
        # Get memory info if available
        if [[ -r "/proc/$GATEWAY_PID/status" ]]; then
            VM_RSS=$(grep "VmRSS:" /proc/$GATEWAY_PID/status 2>/dev/null | awk '{print $2 $3}' || echo "N/A")
            echo "  PID: $GATEWAY_PID"
            echo "  Memory: $VM_RSS"
        fi
    fi
fi

# --- MEMORY CHECK ---
echo ""
echo "## Memory"
if [[ -r /proc/meminfo ]]; then
    MEM_TOTAL=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    MEM_AVAIL=$(grep MemAvailable /proc/meminfo 2>/dev/null | awk '{print $2}' || echo "0")
    MEM_FREE=$(grep MemFree /proc/meminfo | awk '{print $2}')
    
    # Use MemAvailable if present (Linux 3.14+), else estimate from MemFree + Buffers + Cached
    if [[ "$MEM_AVAIL" == "0" ]]; then
        BUFFERS=$(grep Buffers /proc/meminfo | awk '{print $2}')
        CACHED=$(grep "^Cached:" /proc/meminfo | awk '{print $2}')
        MEM_AVAIL=$((MEM_FREE + BUFFERS + CACHED))
    fi
    
    MEM_USED=$((MEM_TOTAL - MEM_AVAIL))
    MEM_PCT=$((MEM_USED * 100 / MEM_TOTAL))
    
    echo "  Total: $((MEM_TOTAL / 1024)) MB"
    echo "  Used: $((MEM_USED / 1024)) MB (${MEM_PCT}%)"
    
    if [[ $MEM_PCT -ge 90 ]]; then
        add_issue "Memory critical: ${MEM_PCT}% used"
        set_critical
    elif [[ $MEM_PCT -ge 80 ]]; then
        add_issue "Memory warning: ${MEM_PCT}% used"
        set_warning
    fi
else
    free -h 2>/dev/null | while read -r line; do
        echo "  $line"
    done || echo "  (memory info unavailable)"
fi

# --- SUMMARY ---
echo ""
echo "## Summary"

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "  Status: HEALTHY ✅"
    echo "  All checks passed"
    echo ""
    echo "HEARTBEAT_OK"
elif [[ $EXIT_CODE -eq 1 ]]; then
    echo "  Status: WARNING ⚠️"
    echo "  Issues found:"
    for issue in "${ISSUES[@]}"; do
        echo "    - $issue"
    done
    echo ""
    echo "HEARTBEAT_WARNING"
else
    echo "  Status: CRITICAL 🚨"
    echo "  Issues found:"
    for issue in "${ISSUES[@]}"; do
        echo "    - $issue"
    done
    echo ""
    echo "HEARTBEAT_CRITICAL"
fi

echo ""
echo "[EXIT CODE: $EXIT_CODE]"

exit $EXIT_CODE
