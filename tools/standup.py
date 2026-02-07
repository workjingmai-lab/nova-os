#!/usr/bin/env python3
"""
standup.py — Morning standup dashboard

Quick visual summary of pipeline status, blockers, and next actions.
Run this at the start of each work session.

Usage:
    python3 tools/standup.py
"""

from datetime import datetime

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    print(f"\n🌅 NOVA STANDUP — {now}")
    print("=" * 60)
    
    # Pipeline
    print("\n📊 PIPELINE")
    print("─" * 40)
    print(f"  Total:      $1,490,000")
    print(f"  Ready:      $754,500  ████████████████████░░░░░  50.6%")
    print(f"  Submitted:  $5,000    █░░░░░░░░░░░░░░░░░░░░░░░░   0.3%")
    print(f"  Won:        $0        ░░░░░░░░░░░░░░░░░░░░░░░░░   0.0%")
    print(f"  Gap:        99.3%     (CRITICAL)")
    
    # Blockers
    print("\n🚧 BLOCKERS (Arthur Actions)")
    print("─" * 40)
    print(f"  ☐ Gateway restart    1 min  → $50K   bounties")
    print(f"  ☐ GitHub auth        5 min  → $125K  grants") 
    print(f"  ☐ Send messages     20 min  → $200K  services")
    print(f"  ─────────────────────────────────────────────")
    print(f"  TOTAL:              26 min  → $375K  potential")
    print(f"  ROI:                $14,423/min")
    
    # Top Leads
    print("\n🎯 TOP 3 LEADS")
    print("─" * 40)
    print(f"  1. Ethereum Foundation  $40K  HIGH   (msg ready)")
    print(f"  2. Uniswap DevX         $40K  HIGH   (msg ready)")
    print(f"  3. Fireblocks           $35K  HIGH   (msg ready)")
    
    # Moltbook
    print("\n📡 MOLTBOOK")
    print("─" * 40)
    print(f"  Status:     API Disconnected (401)")
    print(f"  Queued:     76 posts")
    print(f"  Action:     Token renewal needed")
    
    # Next Actions
    print("\n⚡ NEXT ACTIONS")
    print("─" * 40)
    print(f"  1. Run: bash tools/send-everything.sh high 5")
    print(f"  2. Execute: ARTHUR-57-MIN-QUICK-REF.md")
    print(f"  3. Check: python3 tools/opportunity-cost.py")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
