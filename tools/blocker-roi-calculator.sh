#!/bin/bash
# blocker-roi-calculator.sh — Calculate ROI of unblocking tasks
# Usage: ./blocker-roi-calculator.sh <unblocked_value> <time_minutes>

UNBLOCKED_VALUE="$1"
TIME_MINUTES="$2"

if [ -z "$UNBLOCKED_VALUE" ] || [ -z "$TIME_MINUTES" ]; then
  echo "Usage: $0 <unblocked_value> <time_minutes>"
  echo ""
  echo "Examples:"
  echo "  $0 130000 5     # $130K grants unblocked in 5 minutes"
  echo "  $0 50000 1      # $50K bounties unblocked in 1 minute"
  echo "  $0 10000 10     # $10K proposal ready in 10 minutes"
  echo ""
  exit 1
fi

# Calculate ROI
ROI_PER_MIN=$(awk "BEGIN {printf \"%.0f\", $UNBLOCKED_VALUE / $TIME_MINUTES}")
ROI_PER_HOUR=$(awk "BEGIN {printf \"%.0f\", $ROI_PER_MIN * 60}")
ROI_PER_SEC=$(awk "BEGIN {printf \"%.2f\", $UNBLOCKED_VALUE / ($TIME_MINUTES * 60)}")

# Format value with K/M suffix
format_value() {
  local value=$1
  if (( value >= 1000000 )); then
    awk "BEGIN {printf \"\$%.1fM\", $value / 1000000}"
  elif (( value >= 1000 )); then
    awk "BEGIN {printf \"\$%.0fK\", $value / 1000}"
  else
    echo "\$$value"
  fi
}

FORMATTED_VALUE=$(format_value $UNBLOCKED_VALUE)
FORMATTED_PER_MIN=$(format_value $ROI_PER_MIN)
FORMATTED_PER_HOUR=$(format_value $ROI_PER_HOUR)

# Output
echo "💰 Blocker ROI Analysis"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Unblocked Value: $FORMATTED_VALUE"
echo "Time to Unblock: $TIME_MINUTES minutes"
echo ""
echo "🚀 ROI Metrics:"
echo "   Per Second:  \$$ROI_PER_SEC/sec"
echo "   Per Minute:  $FORMATTED_PER_MIN/min"
echo "   Per Hour:    $FORMATTED_PER_HOUR/hr"
echo ""

# Priority rating
if (( ROI_PER_MIN >= 50000 )); then
  RATING="🔥 URGENT — Execute NOW"
  PRIORITY="1"
elif (( ROI_PER_MIN >= 10000 )); then
  RATING="⚡ HIGH — Do today"
  PRIORITY="2"
elif (( ROI_PER_MIN >= 1000 )); then
  RATING="✅ MEDIUM — Schedule soon"
  PRIORITY="3"
else
  RATING="📋 LOW — Batch with others"
  PRIORITY="4"
fi

echo "Priority: $RATING"
echo ""

# Comparison context
echo "📊 Context:"
if (( ROI_PER_MIN >= 50000 )); then
  echo "   → Higher than average salary (exceeds most hourly rates)"
elif (( ROI_PER_MIN >= 10000 )); then
  echo "   → Equivalent to executive consulting rates"
elif (( ROI_PER_MIN >= 1000 )); then
  echo "   → Better than most freelance rates"
fi
echo ""

# Decision guidance
echo "🎯 Decision:"
if [ "$TIME_MINUTES" -le 5 ]; then
  echo "   → EXECUTE IMMEDIATELY (under 5 min)"
else
  echo "   → Schedule for next available slot"
fi
echo ""

# Investment perspective
echo "💡 Investment Perspective:"
echo "   Investing $TIME_MINUTES minutes → unlocks $FORMATTED_VALUE"
echo "   Return: $(awk "BEGIN {printf \"%.0fx\", $UNBLOCKED_VALUE / ($TIME_MINUTES * 60 * 20)}")× on minimum wage time"
echo ""

# Example: If $130K in 5 min → 1,300,000% ROI
TOTAL_SEC=$((TIME_MINUTES * 60))
MIN_WAGE_PER_SEC=$(awk "BEGIN {print 7.25 / 3600}")  # US federal minimum wage
MIN_WAGE_INVESTMENT=$(awk "BEGIN {printf \"%.2f\", $TOTAL_SEC * $MIN_WAGE_PER_SEC}")
ACTUAL_RETURN=$(awk "BEGIN {printf \"%.0f\", $UNBLOCKED_VALUE / $MIN_WAGE_INVESTMENT}")

echo "   Minimum wage equivalent: \$$MIN_WAGE_INVESTMENT"
echo "   Actual value: $FORMATTED_VALUE"
echo "   Multiple: ${ACTUAL_RETURN}×"
echo ""
