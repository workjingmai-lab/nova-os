#!/bin/bash
# revenue-velocity-tracker.sh — Track revenue generation per work block
# Usage: ./revenue-velocity-tracker.sh [blocks] [pipeline_value]

PIPELINE_FILE="/home/node/.openclaw/workspace/data/revenue-pipeline.json"
DIARY_FILE="/home/node/.openclaw/workspace/diary.md"

if [ "$1" = "--init" ]; then
  # Initialize tracking
  CURRENT_BLOCKS=$(grep -o "Work Block #[0-9]*" "$DIARY_FILE" | head -1 | grep -o "[0-9]*")
  PIPELINE_TOTAL=$(cat "$PIPELINE_FILE" | grep -o '"total_potential":[0-9]*' | grep -o '[0-9]*')

  echo "$CURRENT_BLOCKS|$PIPELINE_TOTAL" > /tmp/velocity-baseline.txt
  echo "✅ Baseline set: Block #$CURRENT_BLOCKS, Pipeline: \$$(echo $PIPELINE_TOTAL | awk '{printf "%.0fK", $1/1000}')"
  exit 0
fi

if [ "$1" = "--compare" ]; then
  # Compare current vs baseline
  if [ ! -f /tmp/velocity-baseline.txt ]; then
    echo "❌ No baseline found. Run --init first."
    exit 1
  fi

  IFS='|' read -r BASELINE_BLOCKS BASELINE_PIPELINE < /tmp/velocity-baseline.txt

  CURRENT_BLOCKS=$(grep -o "Work Block #[0-9]*" "$DIARY_FILE" | head -1 | grep -o "[0-9]*")
  PIPELINE_TOTAL=$(cat "$PIPELINE_FILE" | grep -o '"total_potential":[0-9]*' | grep -o '[0-9]*')

  BLOCKS_DELTA=$((CURRENT_BLOCKS - BASELINE_BLOCKS))
  PIPELINE_DELTA=$((PIPELINE_TOTAL - BASELINE_PIPELINE))

  if [ $BLOCKS_DELTA -eq 0 ]; then
    echo "No new blocks since baseline."
    exit 0
  fi

  VELOCITY_PER_BLOCK=$(awk "BEGIN {printf \"%.0f\", $PIPELINE_DELTA / $BLOCKS_DELTA}")
  VELOCITY_PER_HOUR=$(awk "BEGIN {printf \"%.0f\", $VELOCITY_PER_BLOCK * 44}")

  echo "📊 Revenue Velocity Report"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Period: Block #$BASELINE_BLOCKS → #$CURRENT_BLOCKS ($BLOCKS_DELTA blocks)"
  echo "Pipeline change: \$$(echo $PIPELINE_DELTA | awk '{printf "%.0fK", $1/1000}')"
  echo ""
  echo "🚀 Velocity Metrics:"
  echo "   Per block:  \$$VELOCITY_PER_BLOCK/block"
  echo "   Per hour:   \$$(echo $VELOCITY_PER_HOUR | awk '{printf "%.0fK", $1/1000}')/hr (44 blocks/hr)"
  echo ""

  # Quality rating
  if (( VELOCITY_PER_BLOCK >= 1000 )); then
    RATING="🔥 EXCEPTIONAL — Scaling rapidly"
  elif (( VELOCITY_PER_BLOCK >= 500 )); then
    RATING="⚡ STRONG — Healthy growth"
  elif (( VELOCITY_PER_BLOCK >= 100 )); then
    RATING="✅ GOOD — Steady progress"
  elif (( VELOCITY_PER_BLOCK >= 0 )); then
    RATING="📋 STABLE — Maintaining"
  else
    RATING="⚠️ DECLINING — Pipeline shrinking"
  fi

  echo "Rating: $RATING"
  echo ""

  # Time to $1M projection
  if [ $VELOCITY_PER_HOUR -gt 0 ]; then
    HOURS_TO_1M=$(awk "BEGIN {printf \"%.1f\", 1000000 / $VELOCITY_PER_HOUR}")
    DAYS_TO_1M=$(awk "BEGIN {printf \"%.1f\", $HOURS_TO_1M / 24}")
    echo "📈 Projections:"
    echo "   Time to \$1M: $DAYS_TO_1M days ($HOURS_TO_1M hours)"
    echo "   (at current velocity of \$$(echo $VELOCITY_PER_HOUR | awk '{printf "%.0fK", $1/1000}')/hr)"
    echo ""
  fi

  exit 0
fi

# Show current status
CURRENT_BLOCKS=$(grep -o "Work Block #[0-9]*" "$DIARY_FILE" | head -1 | grep -o "[0-9]*")
PIPELINE_TOTAL=$(cat "$PIPELINE_FILE" | grep -o '"total_potential":[0-9]*' | grep -o '[0-9]*')
PIPELINE_SERVICES=$(cat "$PIPELINE_FILE" | grep -o '"services_potential":[0-9]*' | grep -o '[0-9]*')
PIPELINE_GRANTS=$(cat "$PIPELINE_FILE" | grep -o '"grants_potential":[0-9]*' | grep -o '[0-9]*')

echo "📊 Current Pipeline Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Work Block: #$CURRENT_BLOCKS"
echo "Total Pipeline: \$$(echo $PIPELINE_TOTAL | awk '{printf "%.0fK", $1/1000}')"
echo "  ├─ Services: \$$(echo $PIPELINE_SERVICES | awk '{printf "%.0fK", $1/1000}')"
echo "  └─ Grants:   \$$(echo $PIPELINE_GRANTS | awk '{printf "%.0fK", $1/1000}')"
echo ""
echo "Commands:"
echo "  $0 --init     # Set baseline for comparison"
echo "  $0 --compare  # Compare current vs baseline"
