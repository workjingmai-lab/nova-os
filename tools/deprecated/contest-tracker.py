#!/usr/bin/env python3
"""
Code4rena Contest Tracker - Auto-fetch and track audit competitions
"""

import json
import re
from datetime import datetime
from pathlib import Path

class ContestTracker:
    def __init__(self, data_file="contests.json"):
        self.data_file = Path(data_file)
        self.contests = self._load()
    
    def _load(self):
        if self.data_file.exists():
            return json.loads(self.data_file.read_text())
        return {"active": [], "upcoming": [], "history": []}
    
    def save(self):
        self.data_file.write_text(json.dumps(self.contests, indent=2))
    
    def add_contest(self, name, platform, prize_pool, start_date, end_date, 
                    tech_stack=None, difficulty="medium", url=None):
        contest = {
            "id": f"{platform.lower()}-{name.lower().replace(' ', '-')}",
            "name": name,
            "platform": platform,
            "prize_pool_usd": prize_pool,
            "start_date": start_date,
            "end_date": end_date,
            "tech_stack": tech_stack or ["solidity"],
            "difficulty": difficulty,
            "url": url,
            "status": self._calc_status(start_date, end_date),
            "registered": False,
            "submitted": False,
            "findings": [],
            "reward_usd": 0
        }
        
        status = contest["status"]
        if status == "active":
            self.contests["active"].append(contest)
        elif status == "upcoming":
            self.contests["upcoming"].append(contest)
        else:
            self.contests["history"].append(contest)
        
        self.save()
        return contest
    
    def _calc_status(self, start, end):
        from datetime import timezone
        now = datetime.now(timezone.utc)
        start_dt = datetime.fromisoformat(start.replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(end.replace('Z', '+00:00'))
        
        if now < start_dt:
            return "upcoming"
        elif now > end_dt:
            return "completed"
        return "active"
    
    def get_prioritized(self):
        """Return contests ranked by opportunity score"""
        all_contests = self.contests["active"] + self.contests["upcoming"]
        
        scored = []
        for c in all_contests:
            score = self._opportunity_score(c)
            scored.append((score, c.get('name', ''), c))
        
        scored.sort(reverse=True, key=lambda x: (x[0], x[1]))
        return [(s, c) for s, _, c in scored]
    
    def _opportunity_score(self, contest):
        """Calculate opportunity score based on prize/duration/difficulty"""
        prize = contest.get("prize_pool_usd", 0)
        
        # Difficulty multiplier
        mult = {"easy": 1.2, "medium": 1.0, "hard": 0.7}
        difficulty_mult = mult.get(contest.get("difficulty", "medium"), 1.0)
        
        # Tech stack bonus (familiar = higher score)
        familiar = ["solidity", "evm", "javascript"]
        tech_bonus = sum(1.1 for t in contest.get("tech_stack", []) 
                        if t.lower() in familiar)
        
        return int(prize * difficulty_mult * (1 + tech_bonus * 0.1))
    
    def print_dashboard(self):
        """Print formatted contest dashboard"""
        print("=" * 60)
        print("🛡️  CODE4RENA CONTEST TRACKER")
        print("=" * 60)
        
        print(f"\n🔥 ACTIVE ({len(self.contests['active'])})")
        for c in self.contests["active"]:
            name = c.get('name', 'Unknown')
            prize = c.get('prize_pool_usd', 0)
            end = c.get('end_date', '')[:10]
            print(f"  • {name}: ${prize:,} | Ends: {end}")
        
        print(f"\n📅 UPCOMING ({len(self.contests['upcoming'])})")
        for score, c in self.get_prioritized()[:5]:
            if c in self.contests["upcoming"]:
                name = c.get('name', 'Unknown')
                prize = c.get('prize_pool_usd', 0)
                start = c.get('start_date', '')[:10]
                print(f"  • {name}: ${prize:,} | Score: {score} | Starts: {start}")
        
        print(f"\n📊 STATS")
        total_prize = sum(c["prize_pool_usd"] for c in 
                         self.contests["active"] + self.contests["upcoming"])
        print(f"  Total Prize Pool Available: ${total_prize:,}")
        print(f"  Contests Tracked: {len(self.contests['history'])}")
        print("=" * 60)

if __name__ == "__main__":
    tracker = ContestTracker()
    
    # Add current contests from manual research
    tracker.add_contest(
        name="Olas",
        platform="Code4rena", 
        prize_pool=62000,
        start_date="2026-01-22T20:00:00Z",
        end_date="2026-02-09T20:00:00Z",
        tech_stack=["solidity", "evm"],
        difficulty="medium",
        url="https://code4rena.com/audits/2026-01-olas"
    )
    
    tracker.add_contest(
        name="Jupiter Lend",
        platform="Code4rena",
        prize_pool=107000,
        start_date="2026-02-04T20:00:00Z",
        end_date="2026-03-04T20:00:00Z",
        tech_stack=["solana", "rust"],
        difficulty="hard",
        url="https://code4rena.com/audits/2026-02-jupiter-lend"
    )
    
    tracker.print_dashboard()
